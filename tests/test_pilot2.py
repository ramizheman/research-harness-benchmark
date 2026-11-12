"""Protocol 2 (required retrieval): lenient parsing of Pilot 1 failure modes, the retrieval gate, identical retrieval
in B and C, empty retrieval in A, the retrieval audit, the model-version stop, and unchanged scoring."""
import glob
import json
import os
import tempfile
import unittest

from bench import common, retrieval_audit, scoring
from runner import agent, experiment, llm, tools

SNAP = os.path.join(common.HB, "memory_v2", "snapshots", "RT-012")
STATEMENT = "Research question:\nX\n\nData available"
OUT = {"testability": {"p_testable": 0.5, "blocking_constraints": []}, "decision": "proceed",
       "predicted_outcome": {"supported": 0.2, "rejected": 0.2, "untestable": 0.2, "artifact": 0.2, "uncertain": 0.2}}


class LenientParse(unittest.TestCase):
    def test_missing_closing_brace(self):
        text = json.dumps({"action": "final", "output": OUT})[:-1]
        self.assertIsNone(agent.parse_action(text)[0])
        a, e, note = agent.parse_action_lenient(text)
        self.assertEqual(a["output"], OUT)
        self.assertIn("1 closing brace", note)

    def test_bare_output_and_unwrapped_final(self):
        a, _, note = agent.parse_action_lenient(json.dumps(OUT))
        self.assertEqual((a["action"], a["output"]), ("final", OUT))
        self.assertIn("bare output", note)
        a, _, note = agent.parse_action_lenient(json.dumps({"output": OUT}))
        self.assertEqual(a["action"], "final")

    def test_tool_without_action(self):
        a, _, note = agent.parse_action_lenient('{"tool": "retrieve_history", "args": {"query": "x"}}')
        self.assertEqual((a["action"], a["tool"]), ("tool", "retrieve_history"))

    def test_unsafe_inputs_rejected(self):
        trunc = json.dumps({"action": "final", "output": OUT})[:60]
        self.assertIsNone(agent.parse_action_lenient(trunc)[0])
        self.assertIsNone(agent.parse_action_lenient("no json")[0])
        self.assertIsNone(agent.parse_action_lenient('{"decision": "proceed"}')[0])
        self.assertIsNone(agent.parse_action_lenient('{"action": "final"}')[0])

    def test_protocol1_parser_unchanged(self):
        self.assertIsNone(agent.parse_action(json.dumps(OUT))[0])
        self.assertIsNone(agent.parse_action(json.dumps({"action": "final", "output": OUT})[:-1])[0])

    def test_pilot1_failures_recovered(self):
        """Every Pilot 1 run that ended unparseable is recovered from its last reply (Pilot 1 files are only read)."""
        bad = [r for r in (json.load(open(p, encoding="utf-8")) for p in glob.glob(os.path.join(common.HB, "runs", "pilot_v1", "raw", "*.json")))
               if r["stop_reason"] == "unparseable"]
        self.assertEqual(len(bad), 4)
        for r in bad:
            a, e, _ = agent.parse_action_lenient(r["log"][-1]["reply"])
            self.assertEqual(a["action"], "final", r["run_id"])
            self.assertEqual(scoring.validate_output(a["output"]), [], r["run_id"])


class Scripted:
    name = "test:scripted"

    def __init__(self, replies, version="gemini-2.5-flash"):
        self.replies, self.version = list(replies), version

    def chat(self, system, messages, seed=None):
        return self.replies.pop(0), {"input_tokens": 10, "output_tokens": 5, "cost_usd": 0.0, "model_version": self.version}


FINAL = json.dumps({"action": "final", "output": OUT})
RETRIEVE = json.dumps({"action": "tool", "tool": "retrieve_history", "args": {"research_question": "drive before pick and roll", "query": "drive"}})


class Gate(unittest.TestCase):
    def test_retrieval_enforced(self):
        r = agent.run(Scripted([FINAL, RETRIEVE, FINAL]), tools.Toolbox("B", SNAP, protocol=2), STATEMENT, 1, {"max_tool_calls": 12}, protocol=2)
        self.assertEqual(r["stop_reason"], "final")
        self.assertEqual(r["gate_turns"], 1)
        self.assertEqual(r["tool_calls"][0]["name"], "retrieve_history")
        self.assertTrue(r["tool_calls"][0]["returned_ids"])

    def test_final_without_retrieval_flagged(self):
        r = agent.run(Scripted([FINAL] * 3), tools.Toolbox("A", protocol=2), STATEMENT, 1, {"max_tool_calls": 12}, protocol=2)
        self.assertEqual((r["stop_reason"], r["gate_turns"]), ("final_without_retrieval", 2))

    def test_no_repair_turn_for_recoverable_reply(self):
        r = agent.run(Scripted([RETRIEVE, FINAL[:-1]]), tools.Toolbox("A", protocol=2), STATEMENT, 1, {"max_tool_calls": 12}, protocol=2)
        self.assertEqual((r["stop_reason"], r["repair_turns"]), ("final", 0))
        self.assertEqual(len(r["parse_recoveries"]), 1)

    def test_protocol1_unchanged(self):
        r = agent.run(Scripted([FINAL]), tools.Toolbox("A"), STATEMENT, 1, {"max_tool_calls": 12})
        self.assertEqual((r["stop_reason"], r["gate_turns"]), ("final", 0))
        self.assertNotIn("retrieve_history", agent.system_prompt(tools.Toolbox("A"), 12))


class Retrieval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tb = {c: tools.Toolbox(c, SNAP if c != "A" else None, protocol=2) for c in "ABC"}

    def test_a_executes_and_returns_nothing(self):
        out = json.loads(self.tb["A"].call("retrieve_history", {"research_question": "drive before pick and roll", "query": "drive"}))
        self.assertEqual(out, {"results": [], "n_results": 0})
        for t in ("read_document", "query_graph", "search_documents"):
            self.assertIn("error", self.tb["A"].call(t, {"key": "FAM:SF-APPA-001", "op": "node", "id": "FAM:SF-APPA-001"}))

    def test_b_and_c_same_items(self):
        q = {"research_question": "does attacking early in the shot clock raise efficiency", "query": "shot clock early offense"}
        b, c = (json.loads(self.tb[x].call("retrieve_history", q))["results"] for x in "BC")
        self.assertEqual([x["id"] for x in b], [x["id"] for x in c])
        self.assertGreater(len(b), 0)
        self.assertTrue(all(len(json.dumps(x, ensure_ascii=False)) <= tools.ITEM_CHARS + 200 for x in c))

    def test_prompts_identical_except_tools(self):
        p = {c: agent.system_prompt(self.tb[c], 12, 2).replace(self.tb[c].describe(), "<TOOLS>") for c in "ABC"}
        self.assertEqual(len(set(p.values())), 1)
        self.assertIn("retrieve_history", p["A"])

    def test_mock_protocol2(self):
        task = experiment.load_task("RT-012")
        for c in "ABC":
            r = agent.run(llm.Mock(), tools.Toolbox(c, SNAP if c != "A" else None, protocol=2), task["statement"], 1, {"max_tool_calls": 12}, protocol=2)
            self.assertEqual(r["stop_reason"], "final")
            self.assertEqual(r["tool_calls"][0]["name"], "retrieve_history")
            self.assertEqual(r["memory_tool_calls"], 0 if c == "A" else 1)


class Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx = retrieval_audit.Context()
        cls.task = experiment.load_task("RT-012")
        cls.key = experiment.answer_key()["RT-012"]
        strata, risks, _, _ = retrieval_audit.snapshot_info(SNAP, with_risks=True)
        snap_fams = set(strata) | {cls.ctx.family_of[p] for p in cls.task["permitted_records"] if p in cls.ctx.family_of}
        q = retrieval_audit.relevant_families(cls.task, cls.key, cls.ctx, snap_fams)
        cls.lesson = retrieval_audit.lesson_families(cls.key, risks, strata)
        cls.rel = sorted((q | cls.lesson) & set(strata))
        cls.strata = strata

    def _run(self, returned, cited, status=None, evidence="the retrieved precedent shows the measure is unreliable at this sample size"):
        res = json.dumps({"results": [{"id": i} for i in returned]})
        final = dict(OUT, retrieval_summary={"prior_findings": [{"id": c, "status": status or "uncertain", "summary": "s"} for c in cited],
                                             "failed_experiments": [], "limitations": [], "unresolved": []},
                     evidence_use=evidence, prior_work={"cited": cited})
        return {"final": final, "messages": [{"role": "user", "content": "q"}, {"role": "assistant", "content": RETRIEVE},
                                             {"role": "user", "content": "TOOL_RESULT retrieve_history:\n" + res}],
                "log": [{"turn": 0, "tool": {"name": "retrieve_history", "args": {"query": "x"}, "result_chars": len(res),
                                             "latency_seconds": 0.1, "returned_ids": returned}}, {"turn": 1}]}

    def test_relevant_set_nonempty(self):
        self.assertGreater(len(self.rel), 0)
        self.assertTrue(self.lesson)
        self.assertEqual(retrieval_audit._list("['LABEL_ERROR']"), ["LABEL_ERROR"])
        self.assertEqual(retrieval_audit._list("[]"), [])

    def test_successful_and_used(self):
        f = self.rel[0]
        a = retrieval_audit.audit(self._run([f"FAM:{f}"], [f"FAM:{f}", "FAM:SF999"], self.strata[f]), self.task, self.key, SNAP, self.ctx, 0.30)
        self.assertTrue(a["retrieval_attempted"] and a["retrieval_successful"] and a["meaningfully_used"])
        self.assertEqual(a["n_fabricated_citations"], 1)
        self.assertEqual((a["status_claims_checked"], a["status_claims_correct"]), (1, 1))

    def test_misrepresented_status(self):
        f = self.rel[0]
        wrong = next(s for s in retrieval_audit.STRATA if s != self.strata[f])
        a = retrieval_audit.audit(self._run([f"FAM:{f}"], [f"FAM:{f}"], wrong), self.task, self.key, SNAP, self.ctx)
        self.assertEqual(a["representation_accuracy"], 0.0)
        self.assertEqual((a["status_shown_checked"], a["status_inferred_checked"]), (1, 0))

    def test_inferred_and_uncheckable_status(self):
        f = self.rel[0]
        a = retrieval_audit.audit(self._run([f"HYP:{f}"], [f"HYP:{f}"], self.strata[f]), self.task, self.key, SNAP, self.ctx)
        self.assertEqual((a["status_inferred_checked"], a["status_inferred_correct"]), (1, 1))
        nat = next(x for x, s in sorted(self.strata.items()) if s not in retrieval_audit.STRATA)
        a = retrieval_audit.audit(self._run([f"FAM:{nat}"], [f"FAM:{nat}"], "uncertain"), self.task, self.key, SNAP, self.ctx)
        self.assertEqual(a["status_claims_checked"], 0)

    def test_placeholder_not_fabrication(self):
        a = retrieval_audit.audit(self._run([], ["N/A", "none"]), self.task, self.key, SNAP, self.ctx)
        self.assertEqual(a["n_fabricated_citations"], 0)

    def test_empty_retrieval_not_success(self):
        a = retrieval_audit.audit(self._run([], ["FAM:" + self.rel[0]]), self.task, self.key, SNAP, self.ctx)
        self.assertTrue(a["retrieval_attempted"])
        self.assertFalse(a["retrieval_successful"] or a["meaningfully_used"])
        self.assertEqual(a["n_fabricated_citations"], 1)

    def test_irrelevant_retrieval_not_success(self):
        irr = next(f for f in sorted(self.strata) if f not in self.rel and f != self.task["study_family_id"])
        a = retrieval_audit.audit(self._run([f"FAM:{irr}"], [f"FAM:{irr}"]), self.task, self.key, SNAP, self.ctx)
        self.assertFalse(a["retrieval_successful"] or a["meaningfully_used"])


class VersionedClient(Scripted):
    def __init__(self, *_, **__):
        super().__init__([RETRIEVE, FINAL] * 40, version="gemini-3-flash")


class VersionStop(unittest.TestCase):
    def test_mismatched_model_version_stops_run(self):
        cfg = experiment.load_config(os.path.join(common.HB, "configs", "pilot2_mock.json"))
        cfg["_out"] = tempfile.mkdtemp()
        cfg["expected_response_model_version"] = "gemini-2.5-flash"
        saved = llm.make
        llm.make = lambda spec, env=None: VersionedClient()
        try:
            experiment.run_all(cfg, log=lambda *_: None)
        finally:
            llm.make = saved
        self.assertEqual(len(glob.glob(os.path.join(cfg["_out"], "raw", "*.json"))), 1)


class ScoringUnchanged(unittest.TestCase):
    def test_retrieval_fields_do_not_change_scores(self):
        key = experiment.answer_key()["RT-012"]
        u = {"input_tokens": 1, "output_tokens": 1, "cost_usd": 0.0}
        plain = scoring.score_replay(OUT, key, "B", u)
        extra = scoring.score_replay(dict(OUT, research_question="q", retrieval_summary={}, evidence_use="e"), key, "B", u)
        self.assertEqual(plain, extra)

    def test_pilot2_config_matches_pilot1(self):
        p1 = json.load(open(os.path.join(common.HB, "configs", "pilot.json"), encoding="utf-8"))
        p2 = json.load(open(os.path.join(common.HB, "configs", "pilot2.json"), encoding="utf-8"))
        for k in ("models", "tasks", "conditions", "seeds", "order_seed", "budgets", "max_cost_usd", "equivalence_margin", "env_path"):
            self.assertEqual(p1[k], p2[k], k)
        self.assertNotEqual(p1["experiment_id"], p2["experiment_id"])


if __name__ == "__main__":
    unittest.main()
