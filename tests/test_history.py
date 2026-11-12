"""Rules, dates, record strata, family resolution, negation and validation classification."""
import ast
import os
import unittest

from bench import adjudicate as A
from bench import common


def rec(id, verdict="null", ft="B_powered_null", result="effect 0.01", power="n=400", date="2026-05-01", basis="doc", **kw):
    return {"id": id, "verdict": verdict, "failure_type": ft, "primary_result": result, "power_info": power,
            "date": date, "date_basis": basis, **kw}


class Rules(unittest.TestCase):
    def test_rules_match_inventory_script(self):
        src = open(os.path.join(common.HB, "scripts", "01_build_inventory_and_memory.py"), encoding="utf-8").read()
        found = {}
        for node in ast.parse(src).body:
            if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id.endswith("_RULES"):
                found[node.targets[0].id] = ast.literal_eval(node.value)
        for name in ("TOPIC_RULES", "DATASET_RULES", "METHOD_RULES", "LIMIT_RULES", "VARIABLE_RULES"):
            self.assertEqual([tuple(x) for x in found[name]], [tuple(x) for x in getattr(common, name)], name)

    def test_norm_text_drops_ids_and_numbers(self):
        s = common.norm_text("APPA-012 found pick-and-roll PPP of 0.95 in 2024")
        self.assertNotIn("appa", s)
        self.assertNotIn("0.95", s)
        self.assertIn("pnr", s)


class Dates(unittest.TestCase):
    def test_exact_and_upper_bound(self):
        self.assertEqual(common.date_interval(rec("X", date="2026-05-01")), ("2026-05-01", "2026-05-01", True))
        self.assertEqual(common.date_interval(rec("X", date="2026-05-01", basis="mtime")), ("2026-03-01", "2026-05-01", False))
        self.assertFalse(common.date_interval(rec("X", date=""))[2])

    def test_order(self):
        a, b = rec("A", date="2026-04-01"), rec("B", date="2026-05-01")
        self.assertEqual(common.order(a, b), "before")
        self.assertEqual(common.order(b, a), "after")
        m = rec("M", date="2026-06-01", basis="mtime")
        self.assertEqual(common.order(a, m), "unknown")
        self.assertEqual(common.order(m, rec("L", date="2026-07-01")), "before")


class Strata(unittest.TestCase):
    def test_record_stratum(self):
        self.assertEqual(A.record_stratum(rec("X", result=""))[0], "no_result")
        self.assertEqual(A.record_stratum(rec("X", verdict="descriptive"))[0], "not_a_test")
        self.assertEqual(A.record_stratum(rec("X", verdict="artifact_found", ft="C_artifact"))[0], "artifact")
        self.assertEqual(A.record_stratum(rec("X", verdict="failed_gate", ft="C_artifact", failure_evidence="the gap vanishes after matching"))[0], "artifact")
        self.assertEqual(A.record_stratum(rec("X", verdict="failed_gate", ft="C_artifact", failure_evidence="small effect"))[0], "uncertain")
        self.assertEqual(A.record_stratum(rec("X", ft="A_unanswerable"))[0], "untestable")
        self.assertEqual(A.record_stratum(rec("X", verdict="supported", ft="D_positive"))[0], "supported")
        self.assertEqual(A.record_stratum(rec("X"))[0], "rejected")
        self.assertEqual(A.record_stratum(rec("X", power=""))[0], "uncertain")
        self.assertEqual(A.record_stratum(rec("X", verdict="inconclusive", ft="E_unclear"))[0], "uncertain")

    def test_resolution_rules(self):
        sup = rec("APPA-001", verdict="supported", ft="D_positive", date="2026-04-01")
        rej = rec("APPA-002", date="2026-05-01")
        art = rec("APPA-003", verdict="artifact_found", ft="C_artifact", date="2026-05-10")
        self.assertEqual(A.resolve([sup], "single")["rule"][:2], "R0")
        self.assertEqual(A.resolve([sup, dict(sup, id="APPA-009")], "x")["rule"][:2], "R1")
        self.assertEqual(A.resolve([sup, rej], "bundle")["stratum"], "mixed")
        r2 = A.resolve([sup, art], "x")
        self.assertEqual((r2["stratum"], r2["rule"][:2]), ("artifact", "R2"))
        fixed = rec("APPA-004", verdict="supported", ft="D_positive", date="2026-06-01", design="corrected after the fix")
        self.assertNotEqual(A.resolve([art, fixed], "x")["rule"][:2], "R2")
        r3 = A.resolve([sup, rej], "x")
        self.assertEqual((r3["stratum"], r3["decider"]), ("rejected", "APPA-002"))
        u1, u2 = dict(sup, date_basis="mtime", date="2026-06-01"), dict(rej, date_basis="mtime", date="2026-06-01")
        self.assertEqual(A.resolve([u1, u2], "x")["rule"][:2], "R5")
        p = dict(u2, id="PAP-001")
        self.assertEqual(A.resolve([u1, p], "x")["decider"], "PAP-001")

    def test_negation_and_validation(self):
        r = rec("X", notes="This is not an independent replication; holdout season 2024-25 used.")
        st, ev = A.validation_status([r], "single", True)
        self.assertEqual(st, "same_pipeline_validation")
        r2 = rec("X", notes="An independent replication on external data confirmed it.")
        self.assertEqual(A.validation_status([r2], "single", True)[0], "independent_validation_claimed")
        self.assertEqual(A.validation_status([rec("X")], "single", True)[0], "no_validation_recorded")

    def test_confidence_penalties(self):
        c, why = A.record_confidence(rec("X", ft="E_unclear", basis="mtime"))
        self.assertAlmostEqual(c, 0.65)
        self.assertEqual(A.level(0.75), "high")
        self.assertEqual(A.level(0.5), "medium")
        self.assertEqual(A.level(0.49), "low")


class Outputs(unittest.TestCase):
    def test_adjudication_file_consistent(self):
        import csv
        rows = list(csv.DictReader(open(os.path.join(common.HB, "automated_adjudication.csv"), encoding="utf-8-sig")))
        records = common.load_records()
        fam = {r["study_family_id"] for r in rows}
        family_of, members, _, _ = common.load_families(records)
        self.assertEqual(fam, set(members))
        self.assertEqual(sum(len(r["members"].split("; ")) for r in rows), len(records))
        for r in rows:
            self.assertIn("not independent human adjudication", r["adjudication_type"])
            self.assertTrue(r["decision_rule"])
            if r["members_disagree"] == "yes":
                self.assertTrue(r["conflicting_evidence"], r["study_family_id"])


if __name__ == "__main__":
    unittest.main()
