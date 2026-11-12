"""Phase 0 check of the retrieval-audit fix (Study 1b). Read-only on runs, snapshots and saved analyses; no model calls.

1. The frozen Study 1 audit (bench/retrieval_audit_study1.py) on the memory_v2 snapshot reproduces every audit column
   of the 450 saved Study 1 rows (300 memory runs, 150 no-memory runs).
2. The fixed audit (bench/retrieval_audit.py) on the memory_v3 snapshot the agents searched equals the fixed audit on
   memory_v2 in every column (the v3 field mapping is exact).
3. Fixed vs frozen: which columns and rows change. Only the risk-code parser changed, so only lesson-tier columns
   and columns derived from them may differ.
Run with the venv that has scikit-learn: %TEMP%\\supp_audit_venv\\Scripts\\python.exe analysis_fixes\\verify_audit_fix.py
"""
import csv, glob, json, os, sys
from collections import Counter, defaultdict

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import retrieval_audit as new, retrieval_audit_study1 as old
from runner.experiment import load_task, answer_key, ensure_snapshot, ensure_snapshot_v3

EXPS = [("runs/pilot3_v1", "analysis_p3"), ("runs/cross_model_v1", "analysis_cross"), ("runs/reasoning_models_v1", "analysis_rm")]
OUT = os.path.join(HB, "analysis_fixes")
LESSON_DERIVED = {"lesson_relevant_in_memory", "lesson_relevant_returned", "relevant_families_in_memory",
                  "relevant_families_returned", "relevant_available", "retrieval_successful", "relevant_surfaced",
                  "cites_relevant_seen", "cited_relevant_families", "meaningfully_used"}


def norm(v):
    if v is None or v == "":
        return ""
    if isinstance(v, bool) or str(v) in ("True", "False"):
        return "1" if str(v) == "True" else "0"
    try:
        return f"{float(v):.6g}"
    except (TypeError, ValueError):
        return str(v)


saved = {}
for d, a in EXPS:
    for row in csv.DictReader(open(os.path.join(HB, d, a, "per_run.csv"), encoding="utf-8")):
        saved[row["run_id"]] = row
keys = answer_key()
ctx = new.Context()
octx = old.Context()

repro_bad, map_bad, changes, n = Counter(), Counter(), defaultdict(list), 0
for d, _ in EXPS:
    for p in sorted(glob.glob(os.path.join(HB, d, "raw", "*.json"))):
        r = json.load(open(p, encoding="utf-8"))
        if r["run_id"] not in saved:
            continue
        n += 1
        task, k = load_task(r["task_id"]), keys[r["task_id"]]
        price = (r["model"].get("price_per_million") or {}).get("input")
        v2, _ = ensure_snapshot(task)
        v3, _ = ensure_snapshot_v3(task)
        a_old = old.audit(r, task, k, v2, octx, price)
        a_new3 = new.audit(r, task, k, v3, ctx, price)
        a_new2 = new.audit(r, task, k, v2, ctx, price)
        s = saved[r["run_id"]]
        for c, v in a_old.items():
            if c in s and norm(v) != norm(s[c]):
                repro_bad[c] += 1
        for c in a_new3:
            if norm(a_new3[c]) != norm(a_new2[c]):
                map_bad[c] += 1
            if norm(a_new3[c]) != norm(a_old[c]):
                changes[c].append((r["run_id"], r["condition"], a_old[c], a_new3[c]))

lines = [f"runs audited: {n}",
         f"1. frozen audit vs saved per_run.csv: {sum(repro_bad.values())} mismatched cells" + (f" {dict(repro_bad)}" if repro_bad else ""),
         f"2. fixed audit, v3 vs v2 snapshot: {sum(map_bad.values())} mismatched cells" + (f" {dict(map_bad)}" if map_bad else ""),
         "3. fixed (v3) vs frozen (v2), changed cells by column:"]
for c in sorted(changes):
    conds = Counter(x[1] for x in changes[c])
    lines.append(f"   {c}: {len(changes[c])} rows (by condition {dict(conds)})" + ("" if c in LESSON_DERIVED else "   <-- NOT lesson-derived"))
rows_changed = {x[0] for c in changes for x in changes[c]}
behaviour = {x[0] for c in ("retrieval_successful", "relevant_surfaced", "meaningfully_used") for x in changes.get(c, [])}
lines.append(f"   rows with any change: {len(rows_changed)}; rows where mentioned/returned/used changed: {len(behaviour)}")
lines.append(f"   unexpected columns changed: {sorted(set(changes) - LESSON_DERIVED) or 'none'}")
for c in ("relevant_surfaced", "retrieval_successful", "meaningfully_used"):
    for rid, cond, a, b in sorted(changes.get(c, [])):
        lines.append(f"   {c}: {rid} {a} -> {b}")
txt = "\n".join(lines)
print(txt)
open(os.path.join(OUT, "verify_audit_fix.txt"), "w", encoding="utf-8").write(txt + "\n")
