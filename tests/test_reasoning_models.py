"""Reasoning-models experiment tests: config structure, reasoning_details passthrough,
mock dry run, and (when --live is passed) a paid single-call smoke test per model."""
import json
import os
import sys
import unittest
import unittest.mock as mock

from bench import common
from runner import experiment, llm, tools_v3

HB = common.HB
LIVE = "--live" in sys.argv


def load_cfg(name):
    return experiment.load_config(os.path.join(HB, "configs", name))


class Config(unittest.TestCase):

    def test_config_exists(self):
        cfg = load_cfg("reasoning_models_v1.json")
        self.assertEqual(cfg["experiment_id"], "reasoning_models_v1")
        self.assertEqual(cfg["protocol"], 3)
        self.assertEqual(cfg["seeds"], [1, 2, 3])
        self.assertEqual(sorted(cfg["conditions"]), ["A", "B", "C"])

    def test_same_tasks_as_pilot3(self):
        cfg = load_cfg("reasoning_models_v1.json")
        p3 = load_cfg("pilot3.json")
        self.assertEqual(cfg["tasks"], p3["tasks"])
        self.assertEqual(cfg["order_seed"], p3["order_seed"])
        self.assertEqual(cfg["budgets"], p3["budgets"])
        self.assertEqual(cfg["equivalence_margin"], p3["equivalence_margin"])

    def test_expected_models(self):
        cfg = load_cfg("reasoning_models_v1.json")
        ids = {m["model"] for m in cfg["models"]}
        self.assertIn("anthropic/claude-sonnet-5.5", ids)
        self.assertIn("deepseek/deepseek-v4-pro", ids)
        for m in cfg["models"]:
            self.assertEqual(m["provider"], "openrouter")

    def test_both_models_have_reasoning_in_extra(self):
        cfg = load_cfg("reasoning_models_v1.json")
        for m in cfg["models"]:
            self.assertIn("reasoning", m["extra"],
                          f"{m['model']} missing reasoning in extra")
            self.assertTrue(m["extra"]["reasoning"].get("enabled"),
                            f"{m['model']} reasoning not enabled")

    def test_both_models_have_provider_routing(self):
        cfg = load_cfg("reasoning_models_v1.json")
        for m in cfg["models"]:
            self.assertIn("provider", m["extra"],
                          f"{m['model']} missing provider routing in extra")
            self.assertFalse(m["extra"]["provider"].get("allow_fallbacks", True),
                             f"{m['model']} allow_fallbacks should be False")

    def test_sonnet_routes_to_anthropic(self):
        cfg = load_cfg("reasoning_models_v1.json")
        sonnet = next(m for m in cfg["models"] if "sonnet" in m["model"])
        self.assertIn("anthropic", sonnet["extra"]["provider"]["only"])

    def test_deepseek_routes_to_streamlake(self):
        cfg = load_cfg("reasoning_models_v1.json")
        ds = next(m for m in cfg["models"] if "deepseek" in m["model"])
        self.assertTrue(any("streamlake" in p for p in ds["extra"]["provider"]["only"]),
                        f"expected streamlake provider, got {ds['extra']['provider']['only']}")

    def test_temperature_is_one(self):
        """Both reasoning models require temperature=1."""
        cfg = load_cfg("reasoning_models_v1.json")
        for m in cfg["models"]:
            self.assertEqual(m["temperature"], 1.0,
                             f"{m['model']} temperature should be 1.0 for reasoning")

    def test_run_count(self):
        cfg = load_cfg("reasoning_models_v1.json")
        runs = experiment.plan(cfg)
        # 2 models x 10 tasks x 3 conditions x 3 seeds = 180
        self.assertEqual(len(runs), 180)

    def test_cost_cap(self):
        cfg = load_cfg("reasoning_models_v1.json")
        self.assertGreaterEqual(cfg["max_cost_usd"], 15.0)

    def test_no_mock_in_real_config(self):
        cfg = load_cfg("reasoning_models_v1.json")
        for m in cfg["models"]:
            self.assertNotEqual(m["provider"], "mock")

    def test_mock_config_exists(self):
        cfg = load_cfg("reasoning_models_mock.json")
        self.assertEqual(cfg["protocol"], 3)
        for m in cfg["models"]:
            self.assertEqual(m["provider"], "mock")

    def test_mock_run_count(self):
        cfg = load_cfg("reasoning_models_mock.json")
        self.assertEqual(len(experiment.plan(cfg)), 180)


class ReasoningDetailsPassthrough(unittest.TestCase):
    """reasoning_details returned by the API must survive into the usage dict and be
    forwarded in subsequent assistant messages so the model can continue reasoning."""

    def test_reasoning_details_returned_in_usage(self):
        """OpenAICompatible.chat() must include reasoning_details from the API response."""
        spec = {"provider": "openrouter", "model": "anthropic/claude-sonnet-5.5",
                "temperature": 1.0, "max_tokens": 16000,
                "extra": {"reasoning": {"enabled": True},
                          "provider": {"only": ["anthropic"], "allow_fallbacks": False}}}
        c = llm.make(spec, llm.DEFAULT_ENV)
        fake_response = {
            "model": "anthropic/claude-sonnet-5.5:thinking",
            "choices": [{
                "message": {
                    "role": "assistant",
                    "content": '{"action": "tool", "tool": "retrieve_history", "args": {"query": "test"}}',
                    "reasoning_details": [{"type": "thinking", "thinking": "Let me think..."}],
                }
            }],
            "usage": {"prompt_tokens": 100, "completion_tokens": 50, "cost": 0.002},
        }
        with mock.patch("runner.llm._post", return_value=fake_response):
            text, u = c.chat("sys", [{"role": "user", "content": "hi"}], seed=1)
        self.assertIsNotNone(u.get("reasoning_details"),
                             "reasoning_details should be in usage")
        self.assertEqual(u["reasoning_details"][0]["type"], "thinking")
        self.assertEqual(u["model_version"], "anthropic/claude-sonnet-5.5:thinking")

    def test_reasoning_details_absent_for_non_reasoning_model(self):
        """Non-reasoning OpenRouter models must not inject spurious reasoning_details."""
        spec = {"provider": "openrouter", "model": "openai/gpt-oss-20b",
                "temperature": 0.7, "max_tokens": 8192,
                "extra": {"response_format": {"type": "json_object"}}}
        c = llm.make(spec, llm.DEFAULT_ENV)
        fake_response = {
            "model": "openai/gpt-oss-20b",
            "choices": [{"message": {"role": "assistant", "content": '{"ok": true}'}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "cost": 0.0001},
        }
        with mock.patch("runner.llm._post", return_value=fake_response):
            _, u = c.chat("sys", [{"role": "user", "content": "hi"}], seed=1)
        self.assertIsNone(u.get("reasoning_details"))

    def test_agent_preserves_reasoning_details_in_messages(self):
        """run_v3 must include reasoning_details in the assistant message when the client returns them."""
        from runner import agent
        cfg = load_cfg("reasoning_models_mock.json")
        task = experiment.load_task(cfg["tasks"][0])
        snap, _ = experiment.ensure_snapshot_v3(task)
        tb = tools_v3.Toolbox3("A", None)

        # Patch Mock.chat to return reasoning_details in the final call
        original_chat = llm.Mock.chat
        call_count = [0]

        def patched_chat(self, system, messages, seed=None):
            call_count[0] += 1
            text, u = original_chat(self, system, messages, seed=seed)
            # Inject fake reasoning_details on the first non-repair call
            if call_count[0] == 1:
                u["reasoning_details"] = [{"type": "thinking", "thinking": "scripted thinking"}]
            return text, u

        with mock.patch.object(llm.Mock, "chat", patched_chat):
            result = agent.run_v3(llm.Mock(), tb, task["statement"], seed=1,
                                  budgets=cfg["budgets"])

        # Find the first assistant message in the result
        asst_msgs = [m for m in result["messages"] if m["role"] == "assistant"]
        self.assertTrue(len(asst_msgs) > 0)
        # The first assistant message should have carried the injected reasoning_details
        self.assertIn("reasoning_details", asst_msgs[0],
                      "reasoning_details should be preserved in assistant message")


class MockDryRun(unittest.TestCase):
    """Protocol-3 mock run with reasoning_models_mock config."""

    @classmethod
    def setUpClass(cls):
        from runner import agent
        cls.agent = agent
        cls.cfg = load_cfg("reasoning_models_mock.json")
        task = experiment.load_task(cls.cfg["tasks"][0])
        snap, _ = experiment.ensure_snapshot_v3(task)
        cls.statement = task["statement"]
        cls.snap = snap

    def _run(self, condition):
        tb = tools_v3.Toolbox3(condition, self.snap if condition != "A" else None)
        client = llm.Mock()
        return self.agent.run_v3(client, tb, self.statement, seed=1,
                                 budgets=self.cfg["budgets"])

    def test_mock_condition_a_stops_at_final(self):
        r = self._run("A")
        self.assertEqual(r["stop_reason"], "final", r.get("api_error"))
        self.assertIsInstance(r["final"], dict)

    def test_mock_condition_b_stops_at_final(self):
        r = self._run("B")
        self.assertEqual(r["stop_reason"], "final", r.get("api_error"))

    def test_mock_condition_c_stops_at_final(self):
        r = self._run("C")
        self.assertEqual(r["stop_reason"], "final", r.get("api_error"))


@unittest.skipUnless(LIVE, "pass --live to run paid API smoke tests")
class LiveSmoke(unittest.TestCase):
    """Single paid call per model. Run manually:
    python -m unittest tests.test_reasoning_models -- --live"""

    def _smoke(self, model_id):
        cfg = load_cfg("reasoning_models_v1.json")
        spec = next(m for m in cfg["models"] if m["model"] == model_id)
        client = llm.make(spec, llm.DEFAULT_ENV)
        # Ask for a simple JSON object; reasoning will think about it
        text, u = client.chat(
            'Reply with the JSON object {"ok": true} and nothing else.',
            [{"role": "user", "content": "ping"}], seed=1)
        # Accept content possibly wrapped in markdown due to no response_format enforcement
        import re
        cleaned = re.sub(r"^```(?:json)?|```$", "", (text or "").strip(), flags=re.M).strip()
        try:
            parsed = json.loads(cleaned or "{}")
        except json.JSONDecodeError:
            parsed = {}
        self.assertTrue(parsed.get("ok"), f"bad reply from {model_id}: {text!r}")
        self.assertIsNotNone(u.get("model_version"), "model_version missing from usage")
        self.assertGreater(u.get("input_tokens", 0), 0)
        rd = u.get("reasoning_details")
        print(f"\n  {model_id}: tokens {u['input_tokens']}+{u['output_tokens']} "
              f"cost=${u['cost_usd']} version={u['model_version']} "
              f"has_reasoning={'yes' if rd else 'no'}")

    def test_claude_sonnet_5_5(self):
        self._smoke("anthropic/claude-sonnet-5.5")

    def test_deepseek_v4_pro(self):
        self._smoke("deepseek/deepseek-v4-pro")
