"""Audit the mock dry run (runs/study1b_mock): run matrix, output paths and logging fields. No model calls.
Writes study1b/dry_run_report.txt."""
import csv, glob, json, os, sys
from collections import Counter

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HB, "runs", "study1b_mock")
GOLD = json.load(open(os.path.join(HB, "study1b", "gold_families_frozen.json"), encoding="utf-8"))["tasks"]
raw = [json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(OUT, "raw", "*.json")))]
scores = {r["run_id"]: r for r in csv.DictReader(open(os.path.join(OUT, "scores.csv"), encoding="utf-8"))}
L = [f"output directory: {OUT}", f"files: {sorted(os.listdir(OUT))}", f"raw run files: {len(raw)}; scored rows: {len(scores)}", ""]
cells = Counter((r["model"]["model"], r["condition"]) for r in raw)
L.append("runs per model and condition (expected 30 each; Sonnet O only):")
L += [f"  {m:26s} {c:2s} {n}" for (m, c), n in sorted(cells.items())]
L.append(f"  seeds per cell: {sorted(Counter((r['model']['model'], r['condition'], r['task_id']) for r in raw).values()) == [3] * (len(raw) // 3)}")
checks = {
    "snapshot_fact_hash present": all(r.get("snapshot_fact_hash") for r in raw),
    "one snapshot hash per task": all(len({r["snapshot_fact_hash"] for r in raw if r["task_id"] == t}) == 1 for t in GOLD),
    "oracle gold and file hashes recorded": all(r.get("oracle", {}).get("gold") == GOLD[r["task_id"]] and r["oracle"].get("gold_file_sha256")
                                                 and r["oracle"].get("annotation_file_sha256") for r in raw),
    "first tool call is retrieve_history": all(r["tool_calls"] and r["tool_calls"][0]["name"] == "retrieve_history" for r in raw),
    "families returned equal frozen gold": all(r["tool_calls"][0]["returned_ids"] == ["FAM:" + f for f in GOLD[r["task_id"]]] for r in raw),
    "raw output (final) stored": all("final" in r for r in raw),
    "full message transcript stored": all(r.get("messages") for r in raw),
    "cost_usd in usage": all("cost_usd" in (r.get("usage") or {}) for r in raw),
    "scored: valid_output column": all("valid_output" in s for s in scores.values()),
    "scored: cited_ids column": all("cited_ids" in s for s in scores.values()),
    "scored: cost_usd column": all("cost_usd" in s for s in scores.values()),
    "every raw run scored": set(scores) == {r["run_id"] for r in raw},
}
L += ["", "logging fields:"] + [f"  {'ok  ' if v else 'FAIL'} {k}" for k, v in checks.items()]
trunc = Counter()
for r in raw:
    first = next(m["content"] for m in r["messages"] if m["content"].startswith("TOOL_RESULT retrieve_history"))
    if "...[truncated]" in first.split("\n\n")[0]:
        trunc[(r["condition"], r["task_id"])] += 1
L += ["", "runs whose first retrieval result was cut at 6,000 characters:"]
L += [f"  {c} {t}: {n} runs" for (c, t), n in sorted(trunc.items())] or ["  none"]
txt = "\n".join(L)
print(txt)
open(os.path.join(HB, "study1b", "dry_run_report.txt"), "w", encoding="utf-8").write(txt + "\n")
sys.exit(0 if all(checks.values()) else 1)
