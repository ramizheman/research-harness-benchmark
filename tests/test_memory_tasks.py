"""Memory v2 equivalence, snapshot isolation, replay task leakage checks and challenge screening."""
import csv
import json
import os
import shutil
import tempfile
import unittest

from bench import challenges, common, memory_v2, tasks

HB = common.HB


def pool():
    return list(csv.DictReader(open(os.path.join(HB, "replay_task_pool.csv"), encoding="utf-8-sig")))


class Memory(unittest.TestCase):
    def test_round_trip_special_characters(self):
        F = memory_v2.Facts()
        F.titles["EXP:APPA-001"] = "Title with {braces}"
        F.add("EXP:APPA-001", "notes", "odd {k=v; x} text: a - b")
        F.rel("EXP:APPA-001", "member_of", "FAM:SF1", "rule with; semicolon {x}", family="SF1")
        d = tempfile.mkdtemp()
        try:
            memory_v2.render_documents(F, os.path.join(d, "documents"))
            nodes, edges = memory_v2.write_graph(F, os.path.join(d, "graph"))
            eq = memory_v2.equivalence(F, os.path.join(d, "documents"), nodes, edges)
            self.assertTrue(eq["equivalent"], eq)
        finally:
            shutil.rmtree(d, ignore_errors=True)

    def test_snapshot_contains_only_permitted_records(self):
        records = common.load_records()
        keep = records[:30]
        d = tempfile.mkdtemp()
        try:
            man, F, _, nodes, _ = memory_v2.snapshot(keep, d, inv=common.load_inventory(), thresholds=memory_v2.full_history_thresholds())
            self.assertTrue(man["equivalent"])
            ids = {r["id"] for r in keep}
            seen = {n.split(":", 1)[1] for n in nodes if n.startswith(("EXP:", "RES:"))}
            self.assertTrue(seen <= ids)
            others = {r["id"] for r in records[30:]}
            blob = open(os.path.join(d, "graph", "graph_nodes.jsonl"), encoding="utf-8").read()
            self.assertFalse(any(f'"EXP:{i}"' in blob for i in others))
        finally:
            shutil.rmtree(d, ignore_errors=True)

    def test_full_memory_equivalent(self):
        a = json.load(open(os.path.join(HB, "audit", "memory_v2_audit.json"), encoding="utf-8"))
        self.assertTrue(a["manifest"]["equivalent"])
        self.assertEqual(a["edges_without_rule"], 0)


class Replay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = {r["id"]: r for r in common.load_records()}
        cls.family_of, cls.members, _, _ = common.load_families(list(cls.records.values()))
        cls.pool = pool()
        cls.keys = {k["task_id"]: k for k in map(json.loads, open(os.path.join(HB, "benchmark_answer_key.jsonl"), encoding="utf-8"))}

    def test_jargon_and_numbers(self):
        self.assertEqual(tasks.jargon_terms("PNR PPP rises after a DRIVE"), [])
        self.assertIn("absorption", tasks.jargon_terms("Hub absorption predicts W3 shift"))
        self.assertEqual(tasks.distinctive_numbers("PPP rose by +0.045 (n=1200) in 2024"), {"0.045", "1200", "2024"})

    def test_every_row_has_reason(self):
        for r in self.pool:
            if r["eligible"] == "yes":
                if r["selected_main"] == "yes":
                    self.assertTrue(r["selection_reason"])
            else:
                self.assertTrue(r["exclusion_reasons"], r["study_family_id"])

    def test_selection_balance(self):
        main = [r for r in self.pool if r["selected_main"] == "yes"]
        by = {s: sum(1 for r in main if r["stratum"] == s) for s in tasks.STRATA_QUOTA}
        self.assertEqual(by, tasks.STRATA_QUOTA)
        self.assertLessEqual(sum(r["adaptation_group"] == "yes" for r in main) / len(main), tasks.MAX_ADAPTATION_SHARE + 1e-9)
        pilot = [r for r in self.pool if r["selected_pilot"] == "yes"]
        self.assertEqual(len(pilot), 10)
        self.assertEqual({s: sum(r["stratum"] == s for r in pilot) for s in tasks.STRATA_QUOTA}, {s: 2 for s in tasks.STRATA_QUOTA})

    def test_no_leakage_in_frozen_tasks(self):
        for r in self.pool:
            if r["selected_main"] != "yes":
                continue
            t = json.load(open(os.path.join(HB, "tasks", "replay", r["task_id"] + ".json"), encoding="utf-8"))
            fam = t["study_family_id"]
            own = set(self.members[fam])
            perm = set(t["permitted_records"])
            self.assertFalse(perm & own, r["task_id"])
            first = min((self.records[m] for m in own), key=lambda x: common.date_interval(x)[0])
            for p in perm:
                self.assertTrue(common.date_interval(self.records[p])[1] < t["task_date"], (r["task_id"], p))
            self.assertIsNone(common.ID_RE.search(t["statement"]))
            for m in own:
                res = self.records[m].get("primary_result") or ""
                leaked = tasks.distinctive_numbers(res) & tasks.distinctive_numbers(t["statement"].split("Data available")[0])
                self.assertFalse(leaked - {"2022", "2023", "2024", "2025", "2026"}, (r["task_id"], leaked))
            k = self.keys[r["task_id"]]
            self.assertEqual(k["stratum"], r["stratum"])
            self.assertIn("not independent human adjudication", k["answer_key_type"])
            del first

    def test_lineup_adaptation_has_no_2025_26(self):
        for r in self.pool:
            if r["selected_main"] == "yes" and r["adaptation_group"] == "yes":
                t = json.load(open(os.path.join(HB, "tasks", "replay", r["task_id"] + ".json"), encoding="utf-8"))
                proj = {self.records[m].get("project") for m in self.members[t["study_family_id"]]}
                if proj & tasks.LINEUP_ADAPTATION_PROJECTS:
                    self.assertNotIn("2025-26", t["statement"], r["task_id"])


class Challenges(unittest.TestCase):
    def test_pool_balanced_and_explained(self):
        rows = list(csv.DictReader(open(os.path.join(HB, "prospective_challenge_pool.csv"), encoding="utf-8-sig")))
        self.assertGreaterEqual(len(rows), 30)
        sel = [r for r in rows if r["selected"] == "yes"]
        self.assertEqual(sum(r["selection_class"] == "history-relevant" for r in sel), 6)
        self.assertEqual(sum(r["selection_class"] == "history-irrelevant" for r in sel), 6)
        for r in sel:
            self.assertNotIn("adaptation", r["exclusion_reasons"])
            self.assertNotEqual(r["history_relation"], "redundant")
        for r in rows:
            self.assertTrue(r["selection_rationale"] or r["exclusion_reasons"], r["challenge_id"])

    def test_validation_period_locked(self):
        import datetime as dt
        import importlib.util
        spec = importlib.util.spec_from_file_location("fetch", os.path.join(HB, "scripts", "14_fetch_2026_27.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        with self.assertRaises(PermissionError):
            m.window("validation", dt.date(2027, 6, 1), registry=os.path.join(tempfile.gettempdir(), "no_such_registry.jsonl"))
        lo, hi = m.window("development", dt.date(2027, 6, 1))
        self.assertEqual(hi.isoformat(), "2027-01-30")
        lo, hi = m.window("development", dt.date(2026, 11, 10))
        self.assertEqual(hi.isoformat(), "2026-11-09")
        self.assertFalse(m.in_window("2027-01-31", lo, dt.date(2027, 1, 30)))


if __name__ == "__main__":
    unittest.main()
