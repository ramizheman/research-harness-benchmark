r"""Generate the replay task pool, answer key, frozen task definitions and the pilot memory snapshots.

Inputs: automated_adjudication.csv, research_question_clusters.csv, audit\overlap_candidates.csv,
        audit\duplicate_candidates_raw.tsv, audit\cluster_calibration.json (all from 10_prepare_history.py)
Outputs: replay_task_pool.csv, benchmark_answer_key.jsonl, tasks\replay\<task_id>.json,
         memory_v2\snapshots\<task_id>\ (pilot tasks only; other snapshots are built on demand by the runner)
"""
import collections
import csv
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bench import common, memory_v2, tasks  # noqa: E402

HB = common.HB
records = common.load_records()
by_id = {r["id"]: r for r in records}
family_of, members, kind, note = common.load_families(records)
inv = common.load_inventory()
adj = list(csv.DictReader(open(os.path.join(HB, "automated_adjudication.csv"), encoding="utf-8-sig")))
for a in adj:
    a["confidence"] = float(a["confidence"])
clr = list(csv.DictReader(open(os.path.join(HB, "research_question_clusters.csv"), encoding="utf-8-sig")))
ov = list(csv.DictReader(open(os.path.join(HB, "audit", "overlap_candidates.csv"), encoding="utf-8-sig")))
dup = list(csv.DictReader(open(os.path.join(HB, "audit", "duplicate_candidates_raw.tsv"), encoding="utf-8"), delimiter="\t"))
cal = json.load(open(os.path.join(HB, "audit", "cluster_calibration.json"), encoding="utf-8"))

pool, keys, frozen = tasks.generate(records, family_of, members, kind, adj, clr, ov, dup, cal)
common.write_csv(common.safe_path(os.path.join(HB, "replay_task_pool.csv")), pool)
common.write_jsonl(common.safe_path(os.path.join(HB, "benchmark_answer_key.jsonl")), keys)
tdir = os.path.join(HB, "tasks", "replay")
os.makedirs(tdir, exist_ok=True)
for t in frozen.values():
    json.dump(t, open(os.path.join(tdir, t["task_id"] + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)

pilot = [r for r in pool if r["selected_pilot"] == "yes"]
snap_root = os.path.join(HB, "memory_v2", "snapshots")
common.rmtree_retry(snap_root)
snap_rows = []
for r in pilot:
    t = frozen[r["task_id"]]
    recs = [by_id[i] for i in t["permitted_records"]]
    man, F, meta, nodes, edges = memory_v2.snapshot(recs, os.path.join(HB, "memory_v2", "snapshots", r["task_id"]), inv=inv,
                                                    label=f"{r['task_id']} cutoff {t['task_date']}")
    leak = sorted(set(man["records"]) & set(t["excluded_records"]))
    snap_rows.append({"task_id": r["task_id"], "stratum": r["stratum"], "records": man["n_records"], "facts": man["n_facts"],
                      "equivalent": man["equivalent"], "excluded_records_present": len(leak), "fact_hash": man["fact_hash"]})
common.write_csv(os.path.join(HB, "audit", "pilot_snapshots.csv"), snap_rows or [{"task_id": ""}])

reasons = collections.Counter()
for r in pool:
    for x in filter(None, r["exclusion_reasons"].split(" | ")):
        reasons[x.split(":")[0].split(" (")[0]] += 1
print("families", len(pool), "eligible", sum(r["eligible"] == "yes" for r in pool))
print("eligible by stratum", dict(collections.Counter(r["stratum"] for r in pool if r["eligible"] == "yes")))
print("eligible by tier", dict(collections.Counter((r["stratum"], r["date_tier"]) for r in pool if r["eligible"] == "yes")))
print("main by stratum", dict(collections.Counter(r["stratum"] for r in pool if r["selected_main"] == "yes")))
print("main adaptation", sum(1 for r in pool if r["selected_main"] == "yes" and r["adaptation_group"] == "yes"))
print("pilot", [(r["task_id"], r["stratum"], r["topic"][:25], r["permitted_records"]) for r in pilot])
print("exclusion reasons", reasons.most_common())
print("not selected", collections.Counter(r["selection_reason"] for r in pool if r["eligible"] == "yes" and r["selected_main"] == "no"))
print("snapshots", snap_rows)
