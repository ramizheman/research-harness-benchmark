"""Revised Study 1b full-run cost estimate from the smoke test. Reads saved runs only; no model calls.
Ratio = Haiku smoke cost per run / Haiku Study 1 memory-condition (B, C) cost per run on the same tasks (RT-012, RT-147).
That one ratio replaces the 1.4x guess for every model (an assumption: other models are not measured)."""
import csv, json, os
from collections import defaultdict

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rows(exp):
    return list(csv.DictReader(open(os.path.join(HB, "runs", exp, "scores.csv"), encoding="utf-8-sig")))
smoke = rows("study1b_smoke_v1")
m_smoke = sum(float(r["cost_usd"]) for r in smoke) / len(smoke)
hk = [r for r in rows("cross_model_v1") if "haiku" in r["model"] and r["task_id"] in ("RT-012", "RT-147") and r["condition"] in ("B", "C")]
m_s1 = sum(float(r["cost_usd"]) for r in hk) / len(hk)
ratio = m_smoke / m_s1
print(f"Haiku smoke mean {m_smoke:.6f} USD/run; Haiku Study 1 B+C mean on RT-012, RT-147 {m_s1:.6f} USD/run (n={len(hk)}); ratio {ratio:.2f}")
src = {"gemini-2.5-flash": ("pilot3_v1", 60), "anthropic/claude-haiku-5.5": ("cross_model_v1", 60), "openai/gpt-oss-20b": ("cross_model_v1", 60),
       "deepseek/deepseek-v4-pro": ("reasoning_models_v1", 60), "anthropic/claude-sonnet-5.5": ("reasoning_models_v1", 30)}
cost = defaultdict(list)
for exp in {e for e, _ in src.values()}:
    for r in rows(exp):
        if r["condition"] in ("B", "C") and r["cost_usd"] not in ("", None):
            cost[r["model"].split(":", 1)[1]].append(float(r["cost_usd"]))
tot = [0.0, 0.0, 0.0]
print(f"{'model':30s} {'runs':>4s} {'S1 mean':>9s} {'S1 max':>9s} {'low':>7s} {'expected':>9s} {'high':>7s}")
for m, (exp, n) in src.items():
    c = cost[m]; mean, mx = sum(c) / len(c), max(c)
    low, exp_, high = n * mean, n * mean * ratio, n * mx * max(ratio, 1.0)
    tot = [tot[0] + low, tot[1] + exp_, tot[2] + high]
    print(f"{m:30s} {n:4d} {mean:9.4f} {mx:9.4f} {low:7.2f} {exp_:9.2f} {high:7.2f}")
print(f"{'total':30s} {270:4d} {'':9s} {'':9s} {tot[0]:7.2f} {tot[1]:9.2f} {tot[2]:7.2f}")
