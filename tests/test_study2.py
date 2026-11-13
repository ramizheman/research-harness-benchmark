"""Study 2 freeze: task copies, exclusion rules, snapshots, gold families, configs and the runner's task/snapshot dirs."""
import hashlib
import json
import os
import sys
import unittest

from bench import common, retrieval_audit as ra
from runner import experiment

HB = common.HB
sys.path.insert(0, os.path.join(HB, "study2"))
import gold as gold_rule  # noqa: E402
import leakage_check  # noqa: E402

MANIFEST = json.load(open(os.path.join(HB, "study2", "task_manifest.json"), encoding="utf-8"))
TASKS = [m["task_id"] for m in MANIFEST["tasks"]]


def task_hash(t):
    body = json.dumps({k: t[k] for k in ("task_id", "statement", "permitted_records")}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


class Study2Dirs(unittest.TestCase):
    def setUp(self):
        self.saved = experiment.TASK_DIR, experiment.SNAPSHOT_DIR

    def tearDown(self):
        experiment.TASK_DIR, experiment.SNAPSHOT_DIR = self.saved

    def test_default_config_keeps_study1_paths(self):
        experiment.load_config(os.path.join(HB, "configs", "study1b.json"))
        self.assertEqual(experiment.TASK_DIR, os.path.join(HB, "tasks", "replay"))
        self.assertEqual(experiment.SNAPSHOT_DIR, os.path.normpath(HB))
        self.assertEqual(experiment.load_task("RT-012")["task_hash"],
                         json.load(open(os.path.join(HB, "tasks", "replay", "RT-012.json"), encoding="utf-8"))["task_hash"])

    def test_study2_config_uses_study2_paths(self):
        experiment.load_config(os.path.join(HB, "configs", "study2.json"))
        self.assertEqual(experiment.TASK_DIR, os.path.join(HB, "study2", "tasks"))
        self.assertEqual(experiment.SNAPSHOT_DIR, os.path.join(HB, "study2"))
        d, _ = experiment.ensure_snapshot_v3(experiment.load_task(TASKS[0]))
        self.assertTrue(d.startswith(os.path.join(HB, "study2", "memory_v3", "snapshots")))


class Study2Freeze(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = experiment.TASK_DIR, experiment.SNAPSHOT_DIR
        experiment.load_config(os.path.join(HB, "configs", "study2.json"))
        cls.tasks = {t: experiment.load_task(t) for t in TASKS}
        cls.keys = experiment.answer_key()

    @classmethod
    def tearDownClass(cls):
        experiment.TASK_DIR, experiment.SNAPSHOT_DIR = cls.saved

    def test_68_tasks_none_from_study1(self):
        self.assertEqual(len(TASKS), 68)
        self.assertFalse(set(TASKS) & leakage_check.STUDY1_TASKS)
        self.assertEqual(sorted(TASKS), leakage_check.study2_task_ids())

    def test_hashes_match_manifest_and_originals_untouched(self):
        for m in MANIFEST["tasks"]:
            t = self.tasks[m["task_id"]]
            self.assertEqual(t["task_hash"], m["task_hash"])
            orig = json.load(open(os.path.join(HB, "tasks", "replay", f"{m['task_id']}.json"), encoding="utf-8"))
            self.assertEqual(task_hash(orig), orig["task_hash"])
            self.assertEqual(orig["task_hash"], m["source_task_hash"])
            self.assertEqual(t["statement"], orig["statement"])
            self.assertEqual(set(orig["permitted_records"]) - set(t["permitted_records"]), set(t["study2_removed_records"]))

    def test_every_exclusion_rule_passes(self):
        ck = leakage_check.Checker()
        for tid, t in self.tasks.items():
            self.assertEqual(ck.check(t), {}, tid)

    def test_snapshots_hold_exactly_the_permitted_records(self):
        for m in MANIFEST["tasks"]:
            t = self.tasks[m["task_id"]]
            _, man = experiment.ensure_snapshot_v3(t)
            self.assertEqual(sorted(man["records"]), sorted(t["permitted_records"]))
            self.assertEqual(man["fact_hash"], m["snapshot_fact_hash"])
            self.assertFalse(set(man["records"]) & set(t["excluded_records"]))

    def test_gold_is_the_study1b_rule_and_inside_memory(self):
        gold = json.load(open(os.path.join(HB, "study2", "gold_families_frozen.json"), encoding="utf-8"))["tasks"]
        ctx = ra.Context()
        for m in MANIFEST["tasks"]:
            t = self.tasks[m["task_id"]]
            self.assertEqual(gold[m["task_id"]], m["gold_families"])
            snap, _ = experiment.ensure_snapshot_v3(t)
            g = gold_rule.gold_for(t, self.keys[m["task_id"]], snap, ctx)
            self.assertEqual([x["family"] for x in g["gold"]], gold[m["task_id"]])
            fams = {ctx.family_of[r] for r in t["permitted_records"]}
            for f in gold[m["task_id"]]:
                self.assertIn(f, fams)
                self.assertNotEqual(f, t["study_family_id"])

    def test_manifest_file_hashes(self):
        for p, h in MANIFEST["file_sha256"].items():
            self.assertEqual(hashlib.sha256(open(os.path.join(HB, p), "rb").read()).hexdigest(), h, p)


class Study2Config(unittest.TestCase):
    def setUp(self):
        self.saved = experiment.TASK_DIR, experiment.SNAPSHOT_DIR
        self.cfg = experiment.load_config(os.path.join(HB, "configs", "study2.json"))
        self.src = json.load(open(os.path.join(HB, "configs", "study1b.json"), encoding="utf-8"))

    def tearDown(self):
        experiment.TASK_DIR, experiment.SNAPSHOT_DIR = self.saved

    def test_models_copied_unchanged_and_no_sonnet(self):
        by = {m["model"]: {k: v for k, v in m.items() if k != "conditions"} for m in self.src["models"]}
        self.assertEqual([m["model"] for m in self.cfg["models"]],
                         ["gemini-2.5-flash", "deepseek/deepseek-v4-pro", "anthropic/claude-haiku-5.5", "openai/gpt-oss-20b"])
        for m in self.cfg["models"]:
            self.assertEqual(m, by[m["model"]])

    def test_design(self):
        self.assertEqual(self.cfg["conditions"], ["A", "B", "O"])
        self.assertEqual(self.cfg["seeds"], [1])
        self.assertEqual(self.cfg["tasks"], TASKS)
        self.assertEqual(self.cfg["budgets"], self.src["budgets"])
        self.assertEqual(experiment.spend_cap(self.cfg), 8.0)
        self.assertEqual(len(experiment.plan(self.cfg)), 68 * 3 * 4)

    def test_budget_stop_cuts_gpt_oss_then_haiku(self):
        order = [r["model"]["model"] for r in experiment.plan(self.cfg)]
        self.assertEqual(order[-1], "openai/gpt-oss-20b")
        self.assertEqual(order[0], "gemini-2.5-flash")

    def test_smoke_config(self):
        s = experiment.load_config(os.path.join(HB, "configs", "study2_smoke.json"))
        self.assertEqual([m["model"] for m in s["models"]], ["anthropic/claude-haiku-5.5"])
        self.assertEqual(len(experiment.plan(s)), 6)
        self.assertEqual(experiment.spend_cap(s), 0.5)
        self.assertTrue(set(s["tasks"]) <= set(TASKS))


if __name__ == "__main__":
    unittest.main()
