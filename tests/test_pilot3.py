"""Protocol 3: consolidated family memory (equivalence, fields, no invented outcomes), condition-specific retrieval
(document search in B, relationship traversal in C, equal budgets, identical facts per family), retrieval before any
assessment, the citation check and correction turn, and an unchanged configuration apart from protocol and seeds."""
import json
import os
import unittest

from bench import common, memory_v3, retrieval_audit, scoring
from runner import agent, experiment, llm, tools_v3

HB = common.HB
TASK = "RT-012"


def snap():
    return experiment.ensure_snapshot_v3(experiment.load_task(TASK))


class FamilyMemory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir, cls.man = snap()
        cls.b, cls.c = tools_v3.Toolbox3("B", cls.dir), tools_v3.Toolbox3("C", cls.dir)

    def test_equivalent_and_complete(self):
        self.assertTrue(self.man["equivalent"])
        self.assertTrue(self.man["every_family_has_all_fields"])
        e = self.man["equivalence"]
        self.assertEqual(e["canonical_facts"], e["document_facts"])
        self.assertEqual(e["canonical_facts"], e["graph_facts"])

    def test_same_facts_per_family_in_b_and_c(self):
        self.assertEqual(set(self.b.families), set(self.c.families))
        for f in self.b.families[:40]:
            self.assertEqual(sorted(self.b.facts[f]), sorted(self.c.facts[f]), f)

    def test_observed_and_automated_fields_marked(self):
        f = self.b.families[0]
        ps = {p for p, _, _ in self.b.facts[f]}
        self.assertTrue(all(p.startswith(("observed_", "auto_")) for p in ps), ps)
        self.assertIn("auto_outcome_status", ps)
        self.assertIn("observed_result", ps)

    def test_missing_information_marked_not_invented(self):
        recs = {r["id"]: r for r in common.load_records()}
        for f in self.b.families:
            for p, o, _ in self.b.facts[f]:
                if p == "observed_sample_and_power" and "[" not in o:
                    m = next(x for q, x, _ in self.b.facts[f] if q == "observed_member_records")
                    want = (recs[m].get("power_info") or "").strip()
                    self.assertEqual(o == memory_v3.NOT_RECORDED, want == "", f)

    def test_statuses_from_adjudication_of_permitted_records(self):
        strata, _, _ = retrieval_audit.snapshot_info(os.path.join(HB, "memory_v2", "snapshots", TASK))
        for f in self.b.families:
            st = next(o for p, o, _ in self.b.facts[f] if p == "auto_outcome_status")
            if f[4:] in strata:
                self.assertEqual(st, memory_v3.STATUS_WORDS[strata[f[4:]]], f)

    def test_excluded_family_absent(self):
        t = experiment.load_task(TASK)
        self.assertNotIn("FAM:" + t["study_family_id"], self.b.families)


class Retrieval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        d, _ = snap()
        cls.tb = {c: tools_v3.Toolbox3(c, d if c != "A" else None) for c in "ABC"}
        cls.args = {"research_concepts": ["teammate drive before pick and roll"], "methodological_questions": ["are play-type labels reliable"],
                    "query": "drive preceding PNR raises PNR points per possession"}

    def test_a_returns_nothing(self):
        self.assertEqual(json.loads(self.tb["A"].call("retrieve_history", self.args)), {"results": [], "n_results": 0})
        for t in ("read_family", "search_documents", "explore_graph"):
            self.assertIn("error", self.tb["A"].call(t, {"id": "FAM:SF07"}))

    def test_equal_budget_and_identical_views(self):
        rb = json.loads(self.tb["B"].call("retrieve_history", self.args))["results"]
        rc = json.loads(self.tb["C"].call("retrieve_history", self.args))["results"]
        self.assertEqual(len(rb), tools_v3.RETRIEVE_K)
        self.assertEqual(len(rc), tools_v3.RETRIEVE_K)
        for f in {x["id"] for x in rb} | {x["id"] for x in rc}:
            self.assertEqual(tools_v3.family_view(self.tb["B"].facts[f]), tools_v3.family_view(self.tb["C"].facts[f]))

    def test_graph_traverses_relationships(self):
        self.tb["C"].call("retrieve_history", self.args)
        tr = self.tb["C"].last_trace
        self.assertGreater(tr["edges_traversed"], 0)
        self.assertTrue(tr["concept_seeds"])
        paths = [p for ps in tr["paths"].values() for p in ps]
        self.assertTrue(any(" auto_" in p and "request matches RQC" in p or "auto_related_family" in p or "request matches LIM" in p
                            or "request matches METH" in p for p in paths), paths)

    def test_selection_differs_somewhere(self):
        cfg = experiment.load_config(os.path.join(HB, "configs", "pilot3.json"))
        differ = 0
        for t in cfg["tasks"]:
            d, _ = experiment.ensure_snapshot_v3(experiment.load_task(t))
            q = {"query": experiment.load_task(t)["statement"].split("\n")[1], "research_concepts": [], "methodological_questions": []}
            ib = [x["id"] for x in json.loads(tools_v3.Toolbox3("B", d).call("retrieve_history", q))["results"]]
            ic = [x["id"] for x in json.loads(tools_v3.Toolbox3("C", d).call("retrieve_history", q))["results"]]
            differ += ib != ic
        self.assertGreater(differ, 0)

    def test_results_fit_without_truncation(self):
        for c in "BC":
            s = self.tb[c].call("retrieve_history", {"query": "lineup defense adaptation reliability sample size regression to the mean " * 3})
            self.assertFalse(s.endswith("[truncated]"))
            json.loads(s)


class Scripted:
    name = "test:scripted"

    def __init__(self, replies):
        self.replies = list(replies)

    def chat(self, system, messages, seed=None):
        r = self.replies.pop(0)
        return (r(messages) if callable(r) else r), {"input_tokens": 10, "output_tokens": 5, "cost_usd": 0.0, "model_version": "gemini-2.5-flash"}


OUT = {"testability": {"p_testable": 0.5, "blocking_constraints": []}, "decision": "proceed",
       "predicted_outcome": {"supported": 0.2, "rejected": 0.2, "untestable": 0.2, "artifact": 0.2, "uncertain": 0.2},
       "prior_work": {"already_answered": "unknown", "cited": [], "summary": ""}}
RETRIEVE = json.dumps({"action": "tool", "tool": "retrieve_history", "args": {"research_concepts": ["drive"], "methodological_questions": ["labels"], "query": "drive PNR"}})


def final(evidence=None):
    return json.dumps({"action": "final", "output": dict(OUT, historical_evidence=evidence or [], failed_approaches=[],
                                                          historical_effect={"changed_decision": "no", "explanation": "x"})})


class Sequence(unittest.TestCase):
    def test_schema_hidden_until_retrieval(self):
        tb = tools_v3.Toolbox3("A")
        sysp = agent.system_prompt_v3(tb, 12)
        self.assertNotIn("p_testable", sysp)
        self.assertNotIn("predicted_outcome", sysp)
        self.assertNotIn("p_testable", agent.STAGE1)
        self.assertIn("p_testable", agent.stage2_text())

    def test_preliminary_answer_rejected_and_counted(self):
        r = agent.run_v3(Scripted([final(), RETRIEVE, final()]), tools_v3.Toolbox3("A"), "Q", 1, {"max_tool_calls": 12})
        self.assertEqual((r["stop_reason"], r["preliminary_answers"], r["gate_turns"]), ("final", 1, 1))
        self.assertEqual(r["tool_calls"][0]["name"], "retrieve_history")
        stage2 = [m for m in r["messages"] if m["content"].startswith("TOOL_RESULT retrieve_history")][0]["content"]
        self.assertIn("Stage 2", stage2)

    def test_assessment_inside_retrieval_args_rejected(self):
        bad = json.dumps({"action": "tool", "tool": "retrieve_history", "args": {"query": "x", "decision": "proceed"}})
        r = agent.run_v3(Scripted([bad, RETRIEVE, final()]), tools_v3.Toolbox3("A"), "Q", 1, {"max_tool_calls": 12})
        self.assertEqual(r["preliminary_answers"], 1)

    def test_unwrapped_retrieval_arguments_accepted(self):
        r = agent.run_v3(Scripted(['{"research_concepts": ["a"], "methodological_questions": [], "query": "drive"}', final()]),
                         tools_v3.Toolbox3("A"), "Q", 1, {"max_tool_calls": 12})
        self.assertEqual((r["stop_reason"], r["repair_turns"], r["gate_turns"]), ("final", 0, 0))

    def test_no_retrieval_stops(self):
        r = agent.run_v3(Scripted([final()] * 3), tools_v3.Toolbox3("A"), "Q", 1, {"max_tool_calls": 12})
        self.assertEqual((r["stop_reason"], r["final"]), ("no_retrieval", None))


class Citations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir, _ = snap()

    def test_invented_citation_corrected_once(self):
        r = agent.run_v3(Scripted([RETRIEVE, final([{"id": "FAM:SF999", "status_as_recorded": "supported", "finding": "x"}]), final()]),
                         tools_v3.Toolbox3("A"), "Q", 1, {"max_tool_calls": 12})
        self.assertEqual((r["stop_reason"], r["correction_turns"]), ("final", 1))
        self.assertIn("not returned", r["initial_citation_problems"][0])
        self.assertEqual(r["final_precorrection"]["historical_evidence"][0]["id"], "FAM:SF999")

    def test_wrong_status_flagged_and_right_status_accepted(self):
        def first_result(messages):
            res = [m["content"] for m in messages if m["content"].startswith("TOOL_RESULT retrieve_history")][0]
            item = json.loads(res.split("\n", 1)[1].split("\n\nStage 2")[0])["results"][0]
            return item["id"], item["document"].split("auto_outcome_status: ")[1].split("\n")[0]

        def wrong(messages):
            f, st = first_result(messages)
            return final([{"id": f, "status_as_recorded": "artifact" if st != "artifact" else "supported", "finding": "x"}])

        def right(messages):
            f, st = first_result(messages)
            return final([{"id": f, "status_as_recorded": st, "finding": "x"}])
        r = agent.run_v3(Scripted([RETRIEVE, wrong, right]), tools_v3.Toolbox3("B", self.dir), "Q", 1, {"max_tool_calls": 12})
        self.assertEqual((r["stop_reason"], r["correction_turns"]), ("final", 1))
        self.assertIn("status is recorded", r["initial_citation_problems"][0])
        self.assertEqual(r["log"][-1]["citation_problems"], [])

    def test_audit_maps_v3_fields(self):
        f = {"historical_evidence": [{"id": "FAM:SF07", "status_as_recorded": "inconclusive"}], "historical_effect": {"explanation": "e" * 40}}
        v = retrieval_audit.v3_as_v2(f)
        self.assertEqual(v["retrieval_summary"]["prior_findings"][0]["status"], "uncertain")
        self.assertEqual(len(v["evidence_use"]), 40)


class Mock(unittest.TestCase):
    def test_mock_all_conditions(self):
        d, _ = snap()
        task = experiment.load_task(TASK)
        for c in "ABC":
            r = agent.run_v3(llm.Mock(), tools_v3.Toolbox3(c, d if c != "A" else None), task["statement"], 1, {"max_tool_calls": 12})
            self.assertEqual(r["stop_reason"], "final", c)
            self.assertEqual(r["preliminary_answers"], 0)
            self.assertEqual(scoring.validate_output(r["final"]), [])


class Config(unittest.TestCase):
    def test_pilot3_matches_pilot1_except_protocol_and_seeds(self):
        p1 = json.load(open(os.path.join(HB, "configs", "pilot.json"), encoding="utf-8"))
        p3 = json.load(open(os.path.join(HB, "configs", "pilot3.json"), encoding="utf-8"))
        for k in ("models", "tasks", "conditions", "order_seed", "budgets", "max_cost_usd", "equivalence_margin", "env_path"):
            self.assertEqual(p1[k], p3[k], k)
        self.assertEqual(p3["seeds"], [1, 2, 3])
        self.assertEqual(len(experiment.plan(experiment.load_config(os.path.join(HB, "configs", "pilot3.json")))), 90)


if __name__ == "__main__":
    unittest.main()
