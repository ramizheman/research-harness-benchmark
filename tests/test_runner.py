"""Agent protocol, tool access per condition, prompt identity, budgets and the mock end-to-end path."""
import json
import os
import unittest

from bench import common
from runner import agent, experiment, llm, tools

SNAP = os.path.join(common.HB, "memory_v2", "snapshots", "RT-012")


class Protocol(unittest.TestCase):
    def test_parse_action(self):
        a, e = agent.parse_action('```json\n{"action": "tool", "tool": "glossary", "args": {}}\n```')
        self.assertEqual(a["tool"], "glossary")
        a, e = agent.parse_action('Sure. {"action": "final", "output": {"note": "a \\"quoted\\" } brace"}} trailing')
        self.assertEqual(a["output"]["note"], 'a "quoted" } brace')
        self.assertIsNone(agent.parse_action("no json here")[0])
        self.assertIsNone(agent.parse_action('{"action": "final"}')[0])


class Conditions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tb = {c: tools.Toolbox(c, SNAP if c != "A" else None) for c in "ABC"}

    def test_tool_access(self):
        self.assertIn("error", self.tb["A"].call("search_documents", {"query": "x"}))
        self.assertIn("error", self.tb["B"].call("query_graph", {"op": "find"}))
        self.assertIn("error", self.tb["C"].call("search_documents", {"query": "x"}))
        self.assertTrue(json.loads(self.tb["B"].call("search_documents", {"query": "drive before pick and roll", "k": 3})))
        self.assertTrue(json.loads(self.tb["C"].call("query_graph", {"op": "find", "text": "drive before pick and roll", "limit": 3})))

    def test_prompts_identical_except_tools(self):
        p = {c: agent.system_prompt(self.tb[c], 12) for c in "ABC"}
        strip = {c: p[c].replace(self.tb[c].describe(), "<TOOLS>") for c in "ABC"}
        self.assertEqual(strip["A"], strip["B"])
        self.assertEqual(strip["B"], strip["C"])

    def test_same_facts_reachable(self):
        sec = self.tb["B"].call("read_document", {"key": "FAM:SF-APPA-001"})
        node = json.loads(self.tb["C"].call("query_graph", {"op": "node", "id": "FAM:SF-APPA-001"}))
        self.assertIn("automated_stratum: artifact", sec)
        self.assertEqual(node["automated_stratum"], "artifact")

    def test_truncation(self):
        self.assertLessEqual(len(tools.Toolbox("A", max_chars=100).call("glossary", {})), 100 + len(" ...[truncated]"))


class ToolHog:
    name = "test:toolhog"

    def chat(self, system, messages, seed=None):
        if messages[-1]["content"].startswith("TOOL_RESULT") and agent.FINISH in messages[-1]["content"] or messages[-1]["content"] == agent.FINISH:
            return json.dumps({"action": "final", "output": {"decision": "proceed"}}), {"input_tokens": 10, "output_tokens": 5, "cost_usd": 0.001}
        return json.dumps({"action": "tool", "tool": "glossary", "args": {}}), {"input_tokens": 10, "output_tokens": 5, "cost_usd": 0.001}


class Loop(unittest.TestCase):
    def test_budget_forces_finish(self):
        r = agent.run(ToolHog(), tools.Toolbox("A"), "Research question:\nX\n\nData available", 1, {"max_tool_calls": 3})
        self.assertEqual(r["stop_reason"], "final")
        self.assertEqual(r["n_tool_calls"], 3)
        self.assertAlmostEqual(r["usage"]["cost_usd"], 0.004)

    def test_mock_all_conditions(self):
        task = experiment.load_task("RT-012")
        for c in "ABC":
            r = agent.run(llm.Mock(), tools.Toolbox(c, SNAP if c != "A" else None), task["statement"], 1, {"max_tool_calls": 12})
            self.assertEqual(r["stop_reason"], "final")
            self.assertEqual(r["memory_tool_calls"], 0 if c == "A" else 1)

    def test_frozen_task_and_snapshot_checks(self):
        t = experiment.load_task("RT-012")
        experiment.ensure_snapshot(t)
        bad = dict(t, permitted_records=t["permitted_records"][:-1])
        with self.assertRaises(ValueError):
            experiment.ensure_snapshot(bad)

    def test_plan_counts(self):
        cfg = experiment.load_config(os.path.join(common.HB, "configs", "pilot_mock.json"))
        runs = experiment.plan(cfg)
        self.assertEqual(len(runs), 30)
        self.assertEqual(len({r["run_id"] for r in runs}), 30)


class GeminiClient(unittest.TestCase):
    def setUp(self):
        self.spec = {"provider": "gemini", "model": "gemini-2.5-flash", "temperature": 0.7, "max_tokens": 8192,
                     "thinking_budget": 2048, "price_per_million": {"input": 0.30, "output": 2.50}}

    def test_request_body(self):
        c = llm.make(self.spec, env_path=None)
        b = c.body("SYS", [{"role": "user", "content": "q"}, {"role": "assistant", "content": "a"}, {"role": "user", "content": "r"}], seed=1)
        self.assertEqual(b["systemInstruction"]["parts"][0]["text"], "SYS")
        self.assertEqual([x["role"] for x in b["contents"]], ["user", "model", "user"])
        self.assertEqual(b["generationConfig"], {"temperature": 0.7, "maxOutputTokens": 8192, "responseMimeType": "application/json",
                                                 "thinkingConfig": {"thinkingBudget": 2048}, "seed": 1})

    def test_same_settings_every_condition(self):
        cfg = experiment.load_config(os.path.join(common.HB, "configs", "pilot.json"))
        runs = experiment.plan(cfg)
        self.assertEqual(len(runs), 30)
        self.assertEqual(len({json.dumps(r["model"], sort_keys=True) for r in runs}), 1)
        self.assertEqual({r["model"]["provider"] for r in runs}, {"gemini"})
        bodies = {c: llm.make(runs[0]["model"], None).body("S", [{"role": "user", "content": "x"}], 1)["generationConfig"] for c in "ABC"}
        self.assertEqual(bodies["A"], bodies["B"])
        self.assertEqual(bodies["B"], bodies["C"])

    def test_parse_and_cost(self):
        c = llm.make(self.spec, env_path=None)
        j = {"candidates": [{"content": {"parts": [{"text": "hidden", "thought": True}, {"text": '{"action": "final"'}, {"text": ', "output": {}}'}]},
                             "finishReason": "STOP"}],
             "usageMetadata": {"promptTokenCount": 1000, "candidatesTokenCount": 200, "thoughtsTokenCount": 300},
             "modelVersion": "gemini-2.5-flash"}
        text, u = c.parse(j)
        self.assertEqual(text, '{"action": "final", "output": {}}')
        self.assertEqual(u["output_tokens"], 500)
        self.assertAlmostEqual(u["cost_usd"], (1000 * 0.30 + 500 * 2.50) / 1e6)
        self.assertEqual(u["model_version"], "gemini-2.5-flash")
        text, u = c.parse({"candidates": [{"finishReason": "SAFETY"}]})
        self.assertEqual(text, "")
        self.assertEqual(u["finish_reason"], "SAFETY")

    def test_key_lookup_order(self):
        import tempfile
        p = os.path.join(tempfile.mkdtemp(), ".env")
        open(p, "w").write("OTHER=1\nGOOGLE_API_KEY=abc\n")
        saved = {n: os.environ.pop(n, None) for n in llm.GEMINI_KEY_NAMES}
        try:
            self.assertEqual(llm.load_key(llm.GEMINI_KEY_NAMES, p), "abc")
            open(p, "a").write("GEMINI_API_KEY=def\n")
            self.assertEqual(llm.load_key(llm.GEMINI_KEY_NAMES, p), "def")
            with self.assertRaises(KeyError):
                llm.load_key(("MISSING_KEY",), p)
        finally:
            for n, v in saved.items():
                if v is not None:
                    os.environ[n] = v


class Failing:
    name = "test:failing"

    def chat(self, system, messages, seed=None):
        raise RuntimeError("HTTP 503: unavailable")


class Errors(unittest.TestCase):
    def test_api_error_recorded(self):
        r = agent.run(Failing(), tools.Toolbox("A"), "Research question:\nX\n\nData available", 1, {"max_tool_calls": 3})
        self.assertEqual(r["stop_reason"], "api_error")
        self.assertIn("503", r["api_error"])
        self.assertIsNone(r["final"])


if __name__ == "__main__":
    unittest.main()
