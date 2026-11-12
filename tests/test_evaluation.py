"""Scoring, statistics, claim registry and redaction."""
import json
import os
import tempfile
import unittest

import numpy as np

from bench import claims, redact, scoring, stats

KEY = {"stratum": "artifact", "testable": True, "should_flag_before_running": True,
       "expected_risk_codes": ["RTM_SELECTION", "LABEL_ERROR"], "prior_same_question_families_in_memory": ["SF1"]}


def output(**kw):
    o = {"testability": {"p_testable": 0.3, "blocking_constraints": [{"code": "LABEL_ERROR", "text": "x"}]},
         "prior_work": {"already_answered": "partly", "cited": [], "summary": ""},
         "risks": [{"code": "RTM_SELECTION", "text": "x"}, {"code": "BASE_RATE", "text": "y"}],
         "predicted_outcome": {"supported": 0.1, "rejected": 0.1, "untestable": 0.1, "artifact": 0.6, "uncertain": 0.1},
         "decision": "do_not_proceed",
         "design": {f: "" for f in scoring.DESIGN_FIELDS}}
    o.update(kw)
    return o


class Scoring(unittest.TestCase):
    def test_replay_scores(self):
        s = scoring.score_replay(output(), KEY, "B")
        self.assertTrue(s["valid_output"])
        self.assertEqual(s["flag_correct"], 1)
        self.assertAlmostEqual(s["testability_brier"], 0.49)
        self.assertEqual(s["risk_recall"], 1.0)
        self.assertEqual(s["risk_codes_not_in_key"], 1)
        self.assertTrue(s["prior_work_recognized"])
        self.assertAlmostEqual(s["outcome_log_loss"], -np.log(0.6))

    def test_invalid_and_missing(self):
        self.assertFalse(scoring.score_replay(None, KEY, "A")["valid_output"])
        bad = output(decision="maybe", risks=[{"code": "NOT_A_CODE"}])
        self.assertTrue(scoring.validate_output(bad))

    def test_prereg_rubric(self):
        d = {"estimand": "difference in PPP between triggered and matched possessions", "unit": "possession clustered by game",
             "sample": "about 1,200 games from 2022-23 to 2024-25", "power": "power 0.8 for a minimum detectable effect of 0.03",
             "controls": "opponent fixed effects and matched baseline", "falsification": "placebo permutation of trigger timing",
             "multiplicity": "single primary test; Holm for the two secondary tests", "decision_rule": "support if the 95% CI excludes 0 and effect > 0.02",
             "data_version": "frozen snapshot of seasons 2022-23 to 2024-25"}
        items, q = scoring.prereg_score(d)
        self.assertEqual(q, 1.0)
        self.assertEqual(scoring.prereg_score({})[1], 0.0)
        items, q = scoring.prereg_score({"estimand": "something vague about basketball"})
        self.assertEqual(items["estimand"], 1)


class Stats(unittest.TestCase):
    def test_auc_balanced(self):
        self.assertEqual(stats.auc([0.9, 0.8, 0.1], [1, 1, 0]), 1.0)
        self.assertEqual(stats.auc([0.5, 0.5], [1, 0]), 0.5)
        self.assertIsNone(stats.auc([0.5], [1]))
        self.assertEqual(stats.balanced_accuracy([1, 0, 0, 0], [1, 1, 0, 0]), 0.75)

    def test_holm(self):
        self.assertEqual(stats.holm([0.01, 0.04, 0.03]), [0.03, 0.06, 0.06])

    def test_sign_flip_and_bootstrap(self):
        d = np.array([1.0] * 10)
        self.assertAlmostEqual(stats.sign_flip_p(d), 2 / 1024)
        lo, hi = stats.bootstrap_ci(d)
        self.assertEqual((lo, hi), (1.0, 1.0))
        self.assertTrue(stats.tost(np.zeros(10), 0.1)["equivalent"])
        self.assertFalse(stats.tost(np.array([0.5, -0.5] * 5), 0.1)["equivalent"])

    def test_paired_contrast(self):
        rows = [{"task_id": t, "condition": c, "m": v} for t, c, v in
                [("t1", "A", 0), ("t1", "B", 1), ("t2", "A", 0), ("t2", "B", 1), ("t3", "A", 1)]]
        tasks, d = stats.paired(rows, "m", "A", "B")
        self.assertEqual(tasks, ["t1", "t2"])
        self.assertEqual(list(d), [1.0, 1.0])


class Claims(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.reg = os.path.join(self.d, "claims.jsonl")
        self.script = os.path.join(self.d, "analysis.py")
        open(self.script, "w").write("import json, sys\nprint(json.dumps({'estimate': 0.05, 'ci_low': 0.01, 'ci_high': 0.09}))\n")
        self.claim = {"estimand": "x", "direction": "positive", "test": "t", "pass_rule": {"direction": "positive", "min_abs_effect": 0.02},
                      "script": self.script}

    def test_chain_and_tamper(self):
        claims.register(self.reg, "R1", self.claim)
        claims.register(self.reg, "R2", self.claim)
        self.assertTrue(claims.verify(self.reg)[0])
        lines = open(self.reg, encoding="utf-8").read().splitlines()
        e = json.loads(lines[0])
        e["claim"]["estimand"] = "changed"
        open(self.reg, "w", encoding="utf-8").write(json.dumps(e) + "\n" + lines[1] + "\n")
        ok, problems = claims.verify(self.reg)
        self.assertFalse(ok)

    def test_script_change_detected(self):
        claims.register(self.reg, "R1", self.claim)
        open(self.script, "a").write("# edited\n")
        self.assertFalse(claims.verify(self.reg)[0])

    def test_close_and_gate(self):
        with self.assertRaises(ValueError):
            claims.register(self.reg, "R1", {"estimand": "x"})
        claims.register(self.reg, "R1", self.claim)
        self.assertFalse(claims.release_allowed(self.reg, "2027-04-12", "2027-05-01")[0])
        claims.close(self.reg)
        with self.assertRaises(PermissionError):
            claims.register(self.reg, "R2", self.claim)
        self.assertFalse(claims.release_allowed(self.reg, "2027-04-12", "2027-04-12")[0])
        self.assertTrue(claims.release_allowed(self.reg, "2027-04-12", "2027-05-01")[0])
        with self.assertRaises(PermissionError):
            claims.validate(self.reg, self.d, self.d, "2027-04-12", "2027-04-01")
        res = claims.validate(self.reg, self.d, self.d, "2027-04-12", "2027-05-01")
        self.assertTrue(res[0]["survives_validation"])

    def test_evaluate(self):
        self.assertTrue(claims.evaluate({"estimate": 0.05, "ci_low": 0.01, "ci_high": 0.09}, {"direction": "positive", "min_abs_effect": 0.02}))
        self.assertFalse(claims.evaluate({"estimate": 0.05, "ci_low": -0.01, "ci_high": 0.09}, {"direction": "positive"}))
        self.assertTrue(claims.evaluate({"estimate": -0.05, "ci_low": -0.09, "ci_high": -0.01}, {"direction": "negative"}))


class Redaction(unittest.TestCase):
    def test_redact(self):
        s = ("According to the research history (APPA-012, SF-APPA-001, FAM:SF12), query_graph showed the graph node "
             "C:\\Users\\x\\file.md was relevant.")
        out, n = redact.redact(s)
        for bad in ("APPA-012", "SF-APPA-001", "SF12", "query_graph", "graph node", "C:\\Users", "research history"):
            self.assertNotIn(bad, out)
        self.assertGreaterEqual(n, 6)
        o, n = redact.redact_obj({"a": ["see APPS-003"], "b": 1})
        self.assertEqual(o, {"a": ["see [prior work]"], "b": 1})

    def test_blind_ids(self):
        a, b = redact.blind_id("s", "run1"), redact.blind_id("s", "run2")
        self.assertNotEqual(a, b)
        self.assertEqual(a, redact.blind_id("s", "run1"))
        self.assertNotIn("run1", a)


if __name__ == "__main__":
    unittest.main()
