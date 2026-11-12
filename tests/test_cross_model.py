"""Cross-model replication tests: config structure, OpenRouter client, model_version in usage, mock dry run,
and (when --live is passed) a paid single-call smoke test per model."""
import json
import os
import sys
import unittest

from bench import common
from runner import experiment, llm, tools_v3

HB = common.HB
LIVE = "--live" in sys.argv  # python -m unittest tests.test_cross_model -- --live


def load_cfg(name):
    return experiment.load_config(os.path.join(HB, "configs", name))


class Config(unittest.TestCase):
    def test_cross_model_config_exists(self):
        cfg = load_cfg("cross_model.json")
        self.assertEqual(cfg["experiment_id"], "cross_model_v1")
        self.assertEqual(cfg["protocol"], 3)
        self.assertEqual(cfg["seeds"], [1, 2, 3])
        self.assertEqual(sorted(cfg["conditions"]), ["A", "B", "C"])
        self.assertEqual(cfg["tasks"], experiment.load_config(os.path.join(HB, "configs", "pilot3.json"))["tasks"])

    def test_expected_models(self):
        cfg = load_cfg("cross_model.json")
        ids = {m["model"] for m in cfg["models"]}
        self.assertIn("openai/gpt-oss-20b", ids)
        self.assertIn("anthropic/claude-haiku-5.5", ids)
        for m in cfg["models"]:
            self.assertEqual(m["provider"], "openrouter")
            self.assertIn("price_per_million", m)

    def test_run_count(self):
        cfg = load_cfg("cross_model.json")
        runs = experiment.plan(cfg)
        # 2 models x 10 tasks x 3 conditions x 3 seeds = 180
        self.assertEqual(len(runs), 180)

    def test_cap_five_dollars(self):
        cfg = load_cfg("cross_model.json")
        self.assertEqual(cfg["max_cost_usd"], 5.0)

    def test_no_mock_in_real_config(self):
        cfg = load_cfg("cross_model.json")
        for m in cfg["models"]:
            self.assertNotEqual(m["provider"], "mock")

    def test_same_tasks_and_order_seed_as_pilot3(self):
        cfg = load_cfg("cross_model.json")
        p3 = load_cfg("pilot3.json")
        self.assertEqual(cfg["tasks"], p3["tasks"])
        self.assertEqual(cfg["order_seed"], p3["order_seed"])
        self.assertEqual(cfg["budgets"], p3["budgets"])
        self.assertEqual(cfg["equivalence_margin"], p3["equivalence_margin"])

    def test_mock_config_exists(self):
        cfg = load_cfg("cross_model_mock.json")
        self.assertEqual(cfg["protocol"], 3)
        for m in cfg["models"]:
            self.assertEqual(m["provider"], "mock")

    def test_mock_run_count(self):
        cfg = load_cfg("cross_model_mock.json")
        self.assertEqual(len(experiment.plan(cfg)), 180)


class OpenRouterClient(unittest.TestCase):
    def test_make_returns_openai_compatible(self):
        spec = {"provider": "openrouter", "model": "openai/gpt-oss-20b",
                "temperature": 0.7, "max_tokens": 512,
                "extra": {"response_format": {"type": "json_object"}}}
        c = llm.make(spec, llm.DEFAULT_ENV)
        self.assertIsInstance(c, llm.OpenAICompatible)
        self.assertIn("openrouter", c.base_url)
        self.assertEqual(c.model, "openai/gpt-oss-20b")

    def test_extra_forwarded_to_body(self):
        """response_format must survive into the request body."""
        spec = {"provider": "openrouter", "model": "openai/gpt-oss-20b",
                "temperature": 0.7, "max_tokens": 16,
                "extra": {"response_format": {"type": "json_object"}}}
        c = llm.make(spec, llm.DEFAULT_ENV)
        body = {"model": c.model, "messages": [{"role": "system", "content": "s"}, {"role": "user", "content": "u"}],
                "temperature": c.temperature, "max_tokens": c.max_tokens, **c.extra}
        self.assertEqual(body["response_format"], {"type": "json_object"})

    def test_model_version_in_usage(self):
        """OpenAICompatible must return model_version in usage when using openrouter base URL."""
        import unittest.mock as mock
        spec = {"provider": "openrouter", "model": "openai/gpt-oss-20b",
                "temperature": 0.7, "max_tokens": 16,
                "extra": {"response_format": {"type": "json_object"}}}
        c = llm.make(spec, llm.DEFAULT_ENV)
        fake_response = {
            "model": "openai/gpt-oss-20b",
            "choices": [{"message": {"content": '{"ok": true}'}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "cost": 0.0001},
        }
        with mock.patch("runner.llm._post", return_value=fake_response):
            _, u = c.chat("sys", [{"role": "user", "content": "hi"}], seed=1)
        self.assertEqual(u["model_version"], "openai/gpt-oss-20b")
        self.assertEqual(u["input_tokens"], 10)
        self.assertIsNotNone(u["cost_usd"])

    def test_key_name_is_openrouter(self):
        spec = {"provider": "openrouter", "model": "anthropic/claude-haiku-5.5",
                "temperature": 0.7, "max_tokens": 512}
        c = llm.make(spec, llm.DEFAULT_ENV)
        self.assertEqual(c.key_name, "OPENROUTER_API_KEY")


class MockDryRun(unittest.TestCase):
    """Protocol-3 mock run with cross_model_mock config: both mock models, all conditions."""

    @classmethod
    def setUpClass(cls):
        from runner import agent
        cls.agent = agent
        cls.cfg = load_cfg("cross_model_mock.json")
        task = experiment.load_task(cls.cfg["tasks"][0])
        snap, _ = experiment.ensure_snapshot_v3(task)
        cls.statement = task["statement"]
        cls.snap = snap

    def _run(self, condition):
        tb = tools_v3.Toolbox3(condition, self.snap if condition != "A" else None)
        client = llm.Mock()
        r = self.agent.run_v3(client, tb, self.statement, seed=1,
                              budgets=self.cfg["budgets"])
        return r

    def test_mock_condition_a(self):
        r = self._run("A")
        self.assertEqual(r["stop_reason"], "final", r.get("api_error"))
        self.assertIsInstance(r["final"], dict)
        self.assertEqual(r["preliminary_answers"], 0)
        self.assertEqual(r["gate_turns"], 0)

    def test_mock_condition_b(self):
        r = self._run("B")
        self.assertEqual(r["stop_reason"], "final", r.get("api_error"))
        self.assertEqual(len(r["tool_calls"]), r["n_tool_calls"])

    def test_mock_condition_c(self):
        r = self._run("C")
        self.assertEqual(r["stop_reason"], "final", r.get("api_error"))
        self.assertGreater(r["tool_calls"][0].get("trace", {}).get("edges_traversed", 0), 0)


@unittest.skipUnless(LIVE, "pass --live to run paid API smoke tests")
class LiveSmoke(unittest.TestCase):
    """Single paid call per model. Run manually: python -m unittest tests.test_cross_model -- --live"""

    def _smoke(self, model_id):
        spec = next(m for m in load_cfg("cross_model.json")["models"] if m["model"] == model_id)
        client = llm.make(spec, llm.DEFAULT_ENV)
        text, u = client.chat(
            'Reply with the JSON object {"ok": true} and nothing else.',
            [{"role": "user", "content": "ping"}], seed=1)
        parsed = json.loads(text or "{}")
        self.assertTrue(parsed.get("ok"), f"bad reply: {text!r}")
        self.assertIsNotNone(u.get("model_version"), "model_version missing from usage")
        self.assertGreater(u.get("input_tokens", 0), 0)
        print(f"\n  {model_id}: tokens {u['input_tokens']}+{u['output_tokens']} cost=${u['cost_usd']} version={u['model_version']}")

    def test_gpt_oss_20b(self):
        self._smoke("openai/gpt-oss-20b")

    def test_claude_haiku_5_5(self):
        self._smoke("anthropic/claude-haiku-5.5")
