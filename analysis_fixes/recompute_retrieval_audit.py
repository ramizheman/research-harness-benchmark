"""Recompute the retrieval audit with the risk-code parsing fixed, from the saved raw runs. Read-only on runs and
snapshots; writes only to analysis_fixes/.

Bug: bench.retrieval_audit._list() parses a node's risk_code with ast.literal_eval, which fails on a plain string
such as 'MEASURE_RELIABILITY' and returns []. Families tagged with a single risk code (stored as a string) therefore
never enter the lesson tier. The fix splits a plain string into codes. Nothing else in the audit is changed.

Question-tier relevance normally also uses TF-IDF similarity (scikit-learn, not installed here). The script rebuilds
the question tier without it and checks that the tier sizes equal the saved per-run columns; it stops if they differ.
"""
import ast, csv, glob, json, os, sys
from collections import defaultdict
import numpy as np
HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import common, retrieval_audit as ra
from runner.experiment import load_task, answer_key

OUT = os.path.join(HB, "analysis_fixes")
T = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]
K = answer_key()
ORIG_LIST = ra._list


def fixed_list(v):
    x = ORIG_LIST(v)
    if x or v in (None, ""):
        return x
    s = str(v).strip()
    return [] if s.startswith("[") else [c.strip() for c in s.replace(";", ",").split(",") if c.strip()]


records = {r["id"]: r for r in common.load_records()}
ctx = object.__new__(ra.Context)
ctx.records = records
ctx.family_of, ctx.members, _, _ = common.load_families(list(records.values()))
ctx.cluster = {r["study_family_id"]: r["cluster_id"] for r in
               csv.DictReader(open(os.path.join(HB, "research_question_clusters.csv"), encoding="utf-8-sig"))}


def q_no_tfidf(task, key, ctx, snapshot_families):
    fam = task["study_family_id"]
    rel = {f for f, c in ctx.cluster.items() if c == ctx.cluster.get(fam) and f != fam}
    rel |= {x.strip() for x in str(key.get("knowable_precedents") or "").split(";") if x.strip()}
    rel |= set(ORIG_LIST(key.get("prior_same_question_families_in_memory")))
    return rel & snapshot_families
ra.relevant_families = q_no_tfidf

saved = {}
for p in ("runs/pilot3_v1/analysis_p3/per_run.csv", "runs/cross_model_v1/analysis_cross/per_run.csv", "runs/reasoning_models_v1/analysis_rm/per_run.csv"):
    for r in csv.DictReader(open(os.path.join(HB, p), encoding="utf-8-sig")):
        saved[r["run_id"]] = r

raws = []
for d in ("runs/pilot3_v1/raw", "runs/cross_model_v1/raw", "runs/reasoning_models_v1/raw"):
    raws += sorted(glob.glob(os.path.join(HB, d, "*.json")))
B = lambda x: str(x) in ("True", "1", "1.0")
rows, mismatch = [], defaultdict(int)
for p in raws:
    r = json.load(open(p, encoding="utf-8"))
    if r["run_id"] not in saved or r["condition"] not in "BC":
        continue
    s = saved[r["run_id"]]
    task, key = load_task(r["task_id"]), K[r["task_id"]]
    snap = os.path.join(HB, "memory_v2", "snapshots", r["task_id"])
    ra._list = ORIG_LIST
    old = ra.audit(r, task, key, snap, ctx)
    for col in ("question_relevant_in_memory", "lesson_relevant_in_memory", "relevant_surfaced", "retrieval_successful", "meaningfully_used"):
        if str(old[col]) != str(s[col]) and not (B(old[col]) == B(s[col]) and col not in ("question_relevant_in_memory", "lesson_relevant_in_memory")):
            if str(int(float(old[col]))) != str(int(float(s[col]))):
                mismatch[col] += 1
    ra._list = fixed_list
    new = ra.audit(r, task, key, snap, ctx)
    fc = float(s["flag_correct"]) if s["flag_correct"] not in ("", None) else 0.0
    rows.append({"run_id": r["run_id"], "model": r["model_name"], "task_id": r["task_id"], "condition": r["condition"], "seed": r["seed"],
                 "flag_correct_primary": fc, "n_families_returned": new["n_families_returned"],
                 "Q": new["question_relevant_in_memory"], "L_old": old["lesson_relevant_in_memory"], "L_fixed": new["lesson_relevant_in_memory"],
                 "mentioned_old": int(old["relevant_surfaced"]), "returned_old": int(old["retrieval_successful"]), "used_old": int(old["meaningfully_used"]),
                 "mentioned": int(new["relevant_surfaced"]), "returned": int(new["retrieval_successful"]), "used": int(new["meaningfully_used"]),
                 "Q_returned": int(new["question_relevant_returned"] > 0), "L_returned": int(new["lesson_relevant_returned"] > 0)})
ra._list = ORIG_LIST
print("runs", len(rows), "| harness vs saved CSV mismatches (original parser):", dict(mismatch) or "none")
if mismatch:
    sys.exit("Harness does not reproduce the saved audit; not writing corrected values.")

with open(os.path.join(OUT, "retrieval_audit_fixed_per_run.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

lines = ["task cond | Q L_old L_fixed | Fam | mentioned returned used (fixed) | old: mentioned returned used"]
for t in T:
    for c in "BC":
        g = [x for x in rows if x["task_id"] == t and x["condition"] == c]
        m = lambda k: np.mean([x[k] for x in g])
        lines.append(f"{t} {c} | {g[0]['Q']} {g[0]['L_old']} {g[0]['L_fixed']} | {m('n_families_returned'):.1f} | "
                     f"{m('mentioned'):.2f} {m('returned'):.2f} {m('used'):.2f} | {m('mentioned_old'):.2f} {m('returned_old'):.2f} {m('used_old'):.2f}  n={len(g)}")
for c in "BC":
    g = [x for x in rows if x["condition"] == c and (x["Q"] + x["L_fixed"]) > 0]
    tasks = sorted({x["task_id"] for x in g})
    men, ret, use = sum(x["mentioned"] for x in g), sum(x["returned"] for x in g), sum(x["used"] for x in g)
    acc = lambda k, v: np.mean([x["flag_correct_primary"] for x in g if x[k] == v])
    lines.append(f"POOLED {c}: tasks={len(tasks)} n={len(g)} mentioned={men} returned={ret} used={use} used/returned={use / ret:.2f} used/mentioned={use / men:.2f} "
                 f"| acc returned={acc('returned', 1):.2f} (n={ret}) not={acc('returned', 0):.2f} (n={len(g) - ret}) | acc used={acc('used', 1):.2f} not={acc('used', 0):.2f}")
for t in ("RT-179", "RT-112"):
    for c in "BC":
        g = [x for x in rows if x["task_id"] == t and x["condition"] == c]
        lines.append(f"{t} {c} accuracy: returned {np.mean([x['flag_correct_primary'] for x in g if x['returned']]) if any(x['returned'] for x in g) else float('nan'):.2f} "
                     f"(n={sum(x['returned'] for x in g)}) | not returned {np.mean([x['flag_correct_primary'] for x in g if not x['returned']]) if any(not x['returned'] for x in g) else float('nan'):.2f} (n={sum(1 - x['returned'] for x in g)})")
open(os.path.join(OUT, "retrieval_audit_fixed_summary.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines))
