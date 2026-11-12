"""Study 1b: oracle conditions O and OS, the study budget stop, the run plan, and that A, B and C are unchanged.
No model or API calls: every run uses the scripted mock client or a scripted test client."""
import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from runner import agent, experiment, llm, tools_v3  # noqa: E402
from runner.experiment import ensure_snapshot_v3, load_task  # noqa: E402

T = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]
GOLD = json.load(open(os.path.join(HB, "study1b", "gold_families_frozen.json"), encoding="utf-8"))["tasks"]
ANN = json.load(open(os.path.join(HB, "study1b", "scope_annotations_frozen.json"), encoding="utf-8"))["annotations"]
REQ = {"research_concepts": ["play-type labels"], "methodological_questions": ["is the sample large enough"], "query": "defensive adjustment"}
REQ2 = {"query": "connector portability after a trade"}
_TB = {}


def toolbox(cond, t):
    if (cond, t) not in _TB:
        snap, _ = ensure_snapshot_v3(load_task(t))
        _TB[(cond, t)] = tools_v3.Toolbox3(cond, snap, 6000, gold=GOLD[t], annotations=ANN) if cond in ("O", "OS") \
            else tools_v3.Toolbox3(cond, snap if cond != "A" else None, 6000)
    return _TB[(cond, t)]


def fresh(cond, t, max_chars=10 ** 6):
    """O or OS toolbox. Behaviour tests use no effective cap; the limit test passes the configured 6,000 explicitly."""
    snap, _ = ensure_snapshot_v3(load_task(t))
    return tools_v3.Toolbox3(cond, snap, max_chars, gold=GOLD[t], annotations=ANN)


def without_annotation_fields(s, t):
    for f in GOLD[t]:
        s = s.replace('"scope_annotation": ' + json.dumps(ANN[f], ensure_ascii=False) + ", ", "")
    return s


class Oracle(unittest.TestCase):
    def test_tool_lists(self):
        for c in ("O", "OS"):
            self.assertEqual(tools_v3.CONDITION_TOOLS[c], ["retrieve_history", "glossary", "data_catalog", "read_family"])

    def test_retrieval_returns_frozen_gold_in_order_for_any_request(self):
        for t in T:
            for c in ("O", "OS"):
                for req in (REQ, REQ2):
                    tb = fresh(c, t)
                    out = json.loads(tb.call("retrieve_history", req))
                    self.assertEqual([x["id"] for x in out["results"]], ["FAM:" + f for f in GOLD[t]], (t, c))
                    self.assertEqual(tb.last_ids, ["FAM:" + f for f in GOLD[t]])

    def test_tasks_without_gold_return_empty(self):
        for t in ("RT-065", "RT-101", "RT-146"):
            self.assertEqual(GOLD[t], [])
            for c in ("O", "OS"):
                self.assertEqual(json.loads(fresh(c, t).call("retrieve_history", REQ)), {"results": [], "n_results": 0})

    def test_o_document_identical_to_b(self):
        for t in T:
            if not GOLD[t]:
                continue
            b = toolbox("B", t)
            for x in json.loads(fresh("O", t).call("retrieve_history", REQ))["results"]:
                self.assertEqual(x["document"], b._render(x["id"], None, {})["document"], (t, x["id"]))
                self.assertNotIn("scope_annotation", x)

    def test_os_is_o_plus_frozen_annotation(self):
        for t in T:
            o = json.loads(fresh("O", t).call("retrieve_history", REQ))["results"]
            s = json.loads(fresh("OS", t).call("retrieve_history", REQ))["results"]
            self.assertEqual(len(o), len(s))
            for xo, xs in zip(o, s):
                self.assertEqual({k: v for k, v in xs.items() if k != "scope_annotation"}, xo)
                self.assertEqual(xs["scope_annotation"], ANN[xs["id"][4:]])

    def test_same_annotation_text_across_tasks(self):
        shared = {f: [t for t in T if f in GOLD[t]] for f in ANN}
        shared = {f: ts for f, ts in shared.items() if len(ts) > 1}
        self.assertEqual(sorted(shared), ["SF-APPS-018", "SF-APPS-068", "SF-CHT-025"])
        for f, ts in shared.items():
            texts = {next(x["scope_annotation"] for x in json.loads(fresh("OS", t).call("retrieve_history", REQ))["results"]
                          if x["id"] == "FAM:" + f) for t in ts}
            self.assertEqual(len(texts), 1, f)

    def test_first_retrieval_within_tool_result_limit(self):
        """Fix 1: O's first retrieval fits the 6,000-character cap; OS is never cut because annotation characters do
        not count; OS with its annotation fields removed equals O byte for byte, for the first retrieval and for every
        read_family (including SF20, where O and OS are both cut at the same place)."""
        over = []
        for t in T:
            o, s = fresh("O", t, 6000), fresh("OS", t, 6000)
            first_o, first_s = o.call("retrieve_history", REQ), s.call("retrieve_history", REQ)
            if len(first_o) > 6000 or first_o.endswith("...[truncated]") or first_s.endswith("...[truncated]"):
                over.append((t, len(first_o), len(first_s)))
            self.assertEqual(without_annotation_fields(first_s, t), first_o, t)
            for f in GOLD[t]:
                self.assertEqual(without_annotation_fields(s.call("read_family", {"id": f}), t), o.call("read_family", {"id": f}), (t, f))
        self.assertEqual(over, [], "first retrieval cut at the 6,000-character tool-result limit (task, O chars, OS chars)")

    def test_o_outputs_unchanged_by_fix_1(self):
        fx = json.load(open(os.path.join(HB, "tests", "fixtures", "study1b_o_tool_outputs.json"), encoding="utf-8"))
        sys.path.insert(0, os.path.join(HB, "study1b"))
        import make_o_fixture as m  # noqa: E402
        for t in T:
            self.assertEqual([hashlib.sha256(x.encode()).hexdigest() for x in m.o_calls(t)], fx[t], t)

    def test_read_family_limited_to_gold(self):
        tb = fresh("O", "RT-012")
        self.assertIn("error", json.loads(tb.call("read_family", {"id": "SF02"})))
        self.assertIn("error", json.loads(tb.call("read_family", {"id": load_task("RT-012")["study_family_id"]})))
        ok = json.loads(tb.call("read_family", {"id": "SF-CHT-025"}))
        self.assertEqual(ok["id"], "FAM:SF-CHT-025")
        self.assertNotIn("scope_annotation", ok)
        self.assertEqual(json.loads(fresh("OS", "RT-012").call("read_family", {"id": "FAM:SF-CHT-025"}))["scope_annotation"], ANN["SF-CHT-025"])
        self.assertIn("error", json.loads(fresh("O", "RT-065").call("read_family", {"id": "SF-CHT-025"})))

    def test_read_family_shows_field_cut_from_retrieval_view(self):
        """SF-APPS-085 (RT-179): retrieval cuts observed_result before 'attenuates to 0.179'; read_family returns it
        in full, in O and OS alike; the frozen OS annotation does not contain it."""
        for c in ("O", "OS"):
            tb = fresh(c, "RT-179")
            first = tb.call("retrieve_history", REQ)
            self.assertNotIn("0.179", first)
            full = tb.call("read_family", {"id": "SF-APPS-085"})
            self.assertFalse(full.endswith("...[truncated]"))
            self.assertIn("0.179", json.loads(full)["document"])
        self.assertNotIn("0.179", ANN["SF-APPS-085"])

    def test_gold_respects_own_family_and_exclusion_rules(self):
        for t in T:
            task = load_task(t)
            snap, man = ensure_snapshot_v3(task)
            self.assertEqual(sorted(man["records"]), sorted(task["permitted_records"]))
            self.assertTrue(man["fact_hash"])
            self.assertNotIn(task["study_family_id"], GOLD[t])
            tb = toolbox("O", t)
            for f in GOLD[t]:
                members = [m.strip() for p, o, _ in tb.facts["FAM:" + f] if p == "observed_member_records" for m in o.split(";")]
                self.assertTrue(members, f)
                self.assertTrue(set(members) <= set(task["permitted_records"]), (t, f))
                self.assertFalse(set(members) & set(task.get("excluded_records", [])), (t, f))

    def test_unknown_gold_family_is_refused(self):
        snap, _ = ensure_snapshot_v3(load_task("RT-012"))
        with self.assertRaises(ValueError):
            tools_v3.Toolbox3("O", snap, 6000, gold=["SF-NOT-000"])


class Script:
    """Test client that replies with a fixed sequence of actions."""
    name = "test:script"

    def __init__(self, replies):
        self.replies = list(replies)

    def chat(self, system, messages, seed=None):
        return json.dumps(self.replies.pop(0)), {"input_tokens": 10, "output_tokens": 10, "cost_usd": 0.0}


FINAL = {"action": "final", "output": {"testability": {"p_testable": 0.3, "blocking_constraints": []}, "decision": "do_not_proceed",
                                       "predicted_outcome": {"supported": 0.2, "rejected": 0.2, "untestable": 0.2, "artifact": 0.2, "uncertain": 0.2}}}


class TwoStage(unittest.TestCase):
    def test_retrieval_precedes_assessment_and_stage1_rejects_preliminary(self):
        retrieve_with_assessment = {"action": "tool", "tool": "retrieve_history", "args": {**REQ, "testability": {"p_testable": 0.2}}}
        retrieve = {"action": "tool", "tool": "retrieve_history", "args": REQ}
        res = agent.run_v3(Script([FINAL, retrieve_with_assessment, retrieve, FINAL]), fresh("O", "RT-012"), load_task("RT-012")["statement"], 1,
                           {"max_tool_calls": 12})
        log = res["log"]
        self.assertTrue(log[0].get("preliminary_answer") and log[0].get("gate"))
        self.assertTrue(log[1].get("preliminary_answer") and log[1].get("gate"))
        self.assertEqual(res["tool_calls"][0]["name"], "retrieve_history")
        self.assertEqual(res["tool_calls"][0]["returned_ids"], ["FAM:" + f for f in GOLD["RT-012"]])
        self.assertEqual((res["preliminary_answers"], res["gate_turns"], res["stop_reason"]), (2, 2, "final"))
        self.assertIn(agent.stage2_text(), next(m["content"] for m in res["messages"] if m["content"].startswith("TOOL_RESULT retrieve_history")))

    def test_no_retrieval_stops_the_run(self):
        res = agent.run_v3(Script([FINAL, FINAL, FINAL]), fresh("O", "RT-012"), load_task("RT-012")["statement"], 1, {"max_tool_calls": 12})
        self.assertEqual(res["stop_reason"], "no_retrieval")
        self.assertIsNone(res["final"])


class StudyOneUnchanged(unittest.TestCase):
    def test_abc_tool_outputs_and_prompts_match_pre_change_fixture(self):
        fx = json.load(open(os.path.join(HB, "tests", "fixtures", "study1_abc_tool_outputs.json"), encoding="utf-8"))
        sys.path.insert(0, os.path.join(HB, "study1b"))
        import make_abc_fixture as m  # noqa: E402
        for t in T:
            snap, _ = ensure_snapshot_v3(load_task(t))
            for c in "ABC":
                out, prompt = m.calls(c, snap)
                self.assertEqual([hashlib.sha256(s.encode()).hexdigest() for s in out], fx[f"{t}|{c}"]["calls_sha256"], (t, c))
                self.assertEqual(hashlib.sha256(prompt.encode()).hexdigest(), fx[f"{t}|{c}"]["prompt_sha256"], (t, c))
        self.assertEqual(hashlib.sha256(agent.STAGE1.encode()).hexdigest(), fx["_stage"]["STAGE1"])
        self.assertEqual(hashlib.sha256(agent.stage2_text().encode()).hexdigest(), fx["_stage"]["STAGE2"])

    def test_study1_configs_keep_their_plan_and_cap(self):
        for name, n, cap in (("pilot3.json", 90, 5.0), ("cross_model.json", 180, 5.0), ("reasoning_models_v1.json", 180, 12.0)):
            cfg = experiment.load_config(os.path.join(HB, "configs", name))
            self.assertEqual(len(experiment.plan(cfg)), n)
            self.assertEqual(experiment.spend_cap(cfg), cap)


class Plan(unittest.TestCase):
    def setUp(self):
        self.cfg = experiment.load_config(os.path.join(HB, "configs", "study1b.json"))

    def test_run_matrix(self):
        runs = experiment.plan(self.cfg)
        self.assertEqual(len(runs), 270)
        self.assertEqual(len({r["run_id"] for r in runs}), 270)
        by = {}
        for r in runs:
            by.setdefault(r["model"]["model"], []).append(r)
        for m, rs in by.items():
            conds = {r["condition"] for r in rs}
            self.assertEqual(conds, {"O"} if "sonnet" in m else {"O", "OS"}, m)
            self.assertEqual(len(rs), 30 if "sonnet" in m else 60, m)

    def test_order_cuts_sonnet_then_deepseek_then_seeds(self):
        runs = experiment.plan(self.cfg)
        names = [r["model"]["model"] for r in runs]
        self.assertEqual(list(dict.fromkeys(names)), [m["model"] for m in self.cfg["models"]])
        self.assertEqual(names[-1], "anthropic/claude-sonnet-5.5")
        self.assertEqual(names[-31], "deepseek/deepseek-v4-pro")
        for m in self.cfg["models"]:
            seeds = [r["seed"] for r in runs if r["model"] is m]
            self.assertEqual(seeds, sorted(seeds))

    def test_model_settings_copied_from_study1(self):
        src = {}
        for name in ("pilot3.json", "cross_model.json", "reasoning_models_v1.json"):
            for m in json.load(open(os.path.join(HB, "configs", name), encoding="utf-8"))["models"]:
                src[m["model"]] = m
        added = ("conditions", "expected_response_model_version", "price_per_million")
        for m in self.cfg["models"]:
            s = src[m["model"]]
            self.assertEqual({k: v for k, v in m.items() if k not in added}, {k: v for k, v in s.items() if k not in added}, m["model"])
            self.assertEqual({k: m["price_per_million"][k] for k in ("input", "output")}, {k: s["price_per_million"][k] for k in ("input", "output")})

    def test_study_cap_is_80_percent_of_budget(self):
        self.assertEqual(experiment.spend_cap(self.cfg), 8.0)
        self.assertEqual(self.cfg["budget_usd"], 10.0)


class CostlyMock(llm.Mock):
    """Scripted mock that reports a fixed cost per call, to exercise the budget stop without any API call."""
    cost = 0.30

    def chat(self, system, messages, seed=None):
        text, u = super().chat(system, messages, seed)
        return text, {**u, "cost_usd": self.cost}


class UnknownCostMock(llm.Mock):
    def chat(self, system, messages, seed=None):
        text, u = super().chat(system, messages, seed)
        return text, {**u, "cost_usd": None}


class BudgetStop(unittest.TestCase):
    def setUp(self):
        self.cfg = experiment.load_config(os.path.join(HB, "configs", "study1b_mock.json"))
        self.tmp = tempfile.mkdtemp()
        self.cfg["_out"] = self.tmp
        self.make = experiment.llm.make

    def tearDown(self):
        experiment.llm.make = self.make
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_halts_all_runs_at_80_percent_of_budget(self):
        experiment.llm.make = lambda spec, env=None: CostlyMock()
        msgs = []
        done = experiment.run_all(self.cfg, log=msgs.append)
        costs = [r["usage"]["cost_usd"] for r in experiment.raw_runs(self.cfg)]
        self.assertLess(done, 270)
        self.assertGreaterEqual(sum(costs), 8.0)
        self.assertLess(sum(costs) - max(costs), 8.0 + 1e-9)
        self.assertTrue(any(m.startswith("stopping: spent") for m in msgs), msgs[-3:])
        self.assertEqual(experiment.run_all(self.cfg, log=msgs.append), 0)

    def test_unknown_cost_halts(self):
        experiment.llm.make = lambda spec, env=None: UnknownCostMock()
        msgs = []
        self.assertEqual(experiment.run_all(self.cfg, log=msgs.append), 1)
        self.assertTrue(any("unknown cost" in m for m in msgs))

    def test_run_record_fields(self):
        experiment.run_all(self.cfg, limit=3, log=lambda *_: None)
        recs = experiment.raw_runs(self.cfg)
        self.assertEqual(len(recs), 3)
        hashes = {k + "_sha256": hashlib.sha256(open(os.path.join(HB, self.cfg["oracle"][k]), "rb").read()).hexdigest()
                  for k in ("gold_file", "annotation_file")}
        for r in recs:
            self.assertTrue(r["snapshot_fact_hash"])
            self.assertEqual(r["oracle"], {"gold": GOLD[r["task_id"]], **hashes})
            self.assertEqual(r["tool_calls"][0]["name"], "retrieve_history")
            self.assertEqual(r["tool_calls"][0]["returned_ids"], ["FAM:" + f for f in GOLD[r["task_id"]]])
            self.assertIn("final", r)
            self.assertIn("cost_usd", r["usage"])


if __name__ == "__main__":
    unittest.main()
