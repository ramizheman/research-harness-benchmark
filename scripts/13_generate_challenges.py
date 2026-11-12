r"""Screen, rank and select prospective 2026-27 challenges; write the pool and frozen challenge definitions.

No 2026-27 game data is read. Inputs: memory\ledger_merged.jsonl, automated_adjudication.csv, audit\cluster_calibration.json
Outputs: prospective_challenge_pool.csv, tasks\prospective\<challenge_id>.json (selected challenges)
"""
import collections
import csv
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bench import challenges, common  # noqa: E402

HB = common.HB
records = common.load_records()
family_of, members, kind, note = common.load_families(records)
adj = list(csv.DictReader(open(os.path.join(HB, "automated_adjudication.csv"), encoding="utf-8-sig")))
cal = json.load(open(os.path.join(HB, "audit", "cluster_calibration.json"), encoding="utf-8"))
rows = challenges.select(challenges.screen(records, family_of, members, adj, cal))
common.write_csv(common.safe_path(os.path.join(HB, "prospective_challenge_pool.csv")), rows)
pdir = os.path.join(HB, "tasks", "prospective")
common.rmtree_retry(pdir)
os.makedirs(pdir)
for r in rows:
    if r["selected"] != "yes":
        continue
    statement = "\n".join([
        f"Research objective: {r['objective']}", "",
        f"Data: 2026-27 NBA regular season from {challenges.D0} to {challenges.D1} (development period), plus 2022-23 to 2024-25 "
        "seasons. The 2025-26 season is not provided. Fields: " + r["data"] + ".",
        f"Unit of analysis to consider: {r['unit']} (about {r['expected_dev_units']} expected in the development period).",
        f"What would count as a meaningful finding: {r['meaningful_finding']}",
        f"Validation: claims are tested on games from {challenges.D1} to {challenges.D2}, which are sealed until every claim is registered. "
        f"Planned approach: {r['validation_approach']}",
        "", "Register at most three claims. Each claim needs an estimand, a direction, a pre-specified test with a pass rule, and "
        "an analysis script that runs unchanged on the validation data."])
    t = {"challenge_id": r["challenge_id"], "selection_class": r["selection_class"], "statement": statement,
         "development_period": [challenges.D0, challenges.D1], "validation_period": [challenges.D1, challenges.D2],
         "permitted_memory": "full history (all 384 records); no record uses 2026-27 data"}
    t["task_hash"] = hashlib.sha256(json.dumps(t, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    json.dump(t, open(os.path.join(pdir, r["challenge_id"] + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("candidates", len(rows), collections.Counter(r["history_relation"] for r in rows))
print("eligible", sum(r["eligible"] == "yes" for r in rows))
for r in rows:
    print(r["challenge_id"], r["history_relation"], r["max_history_similarity"], r["feasibility"], r["score"], r["selected"], r["selection_class"], "|", r["exclusion_reasons"][:100])
