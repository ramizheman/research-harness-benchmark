"""Study 2 cost and time estimate from measured runs (Study 1 A and B, Study 1b O). No model calls.

Expected = measured mean cost per run x 68 tasks x 1 seed, per model and condition. High = the most expensive task's
mean cost per run (over the ten measured tasks) x 68, per model and condition. Writes study2/cost_estimate.txt.
"""
import glob
import json
import os
import sys

import numpy as np

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HB, "study2"))
from analysis import S1_SOURCES, S1B_SOURCE, S2_MODELS, short  # noqa: E402

BUDGET, STOP = 10.0, 0.8
runs = []
for d in S1_SOURCES + [S1B_SOURCE]:
    for p in glob.glob(os.path.join(HB, d, "raw", "*.json")):
        r = json.load(open(p, encoding="utf-8"))
        runs.append((short(r["model_name"]), r["condition"], r["task_id"], (r.get("usage") or {}).get("cost_usd") or 0.0, r.get("wall_seconds") or 0.0))
n = len(json.load(open(os.path.join(HB, "study2", "task_manifest.json"), encoding="utf-8"))["tasks"])
L = [f"Study 2 cost estimate: {n} tasks x 3 conditions (A, B, O) x 1 seed x {len(S2_MODELS)} models = {n * 3 * len(S2_MODELS)} runs", "",
     f"{'model':9s} {'cond':4s} {'mean $/run':>10s} {'max task $/run':>14s} {'expected $':>10s} {'high $':>8s} {'mean s/run':>10s}"]
tot_e = tot_h = tot_s = 0.0
for m in S2_MODELS:
    for c in "ABO":
        xs = [x for x in runs if x[0] == m and x[1] == c]
        per_task = {t: np.mean([x[3] for x in xs if x[2] == t]) for t in {x[2] for x in xs}}
        mean, hi, sec = float(np.mean([x[3] for x in xs])), float(max(per_task.values())), float(np.mean([x[4] for x in xs]))
        e, h = mean * n, hi * n
        tot_e, tot_h, tot_s = tot_e + e, tot_h + h, tot_s + sec * n
        L.append(f"{m:9s} {c:4s} {mean:10.4f} {hi:14.4f} {e:10.2f} {h:8.2f} {sec:10.0f}")
L += ["", f"Expected total: ${tot_e:.2f} = {tot_e / BUDGET:.0%} of the ${BUDGET:.0f} budget (target: under 70%).",
      f"High total: ${tot_h:.2f} = {tot_h / BUDGET:.0%} of the budget. The runner stops at ${BUDGET * STOP:.2f} (80%).",
      f"Per task-condition (four models, expected): ${tot_e / (n * 3):.4f}.",
      f"Run time if sequential: about {tot_s / 3600:.1f} hours (measured mean wall time per run)."]
open(os.path.join(HB, "study2", "cost_estimate.txt"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L))
