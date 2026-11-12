"""Study 1b analysis exactly as specified in study1b/prereg_1b.md. Reads saved runs only; no model calls.

Method (identical to paper 1, analysis_fixes/recompute_and_match_study1.py): every raw run is rescored with
bench.scoring.score_replay; correct rate per task = mean over seeds; balanced accuracy = mean of the flag-task mean and the
no-flag-task mean; contrast CI = bench.stats.bootstrap_ci (10,000 resamples, seed 0) over the ten per-task differences
weighted by Study 1's task weights; p = bench.stats.sign_flip_p; Holm across models within each contrast family.
Three scoring rules: primary (scored where possible; no scorable flag counts as wrong), strict (invalid counts as wrong),
valid-only (invalid dropped).
Comparators A, B, C come from the three Study 1 experiments (not rerun). O and OS come from runs/study1b_v1.
Writes study1b/analysis/results.json, per_task.csv, and study1b/analysis/report.md.
Run with %TEMP%\\supp_audit_venv\\Scripts\\python.exe study1b\\analyze_study1b.py
"""
import csv, glob, json, os, sys
from collections import Counter

import numpy as np

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import scoring
from bench.stats import bootstrap_ci, holm, sign_flip_p
from runner.experiment import answer_key

OUT = os.path.join(HB, "study1b", "analysis")
os.makedirs(OUT, exist_ok=True)
T = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]
M = ["Gemini", "Haiku", "gpt-oss", "DeepSeek", "Sonnet"]
GOLD = json.load(open(os.path.join(HB, "study1b", "gold_families_frozen.json"), encoding="utf-8"))["tasks"]
GOLD_TASKS = [t for t in T if GOLD[t]]
NOGOLD_TASKS = [t for t in T if not GOLD[t]]
KEYS = answer_key()
SF = {t: int(bool(KEYS[t]["should_flag_before_running"])) for t in T}
W = {t: (1 / 0.8 if SF[t] else 1 / 1.2) for t in T}  # Study 1 task weights
SOURCES = ["runs/pilot3_v1", "runs/cross_model_v1", "runs/reasoning_models_v1", "runs/study1b_v1"]


def short(name):
    n = name.lower()
    return next(m for k, m in (("gemini", "Gemini"), ("haiku", "Haiku"), ("gpt-oss", "gpt-oss"), ("sonnet", "Sonnet"), ("deepseek", "DeepSeek")) if k in n)


rows = []
for d in SOURCES:
    for p in sorted(glob.glob(os.path.join(HB, d, "raw", "*.json"))):
        r = json.load(open(p, encoding="utf-8"))
        s = scoring.score_replay(r.get("final"), KEYS[r["task_id"]], r["condition"], {})
        rows.append({"src": d.split("/")[1], "m": short(r["model_name"]), "t": r["task_id"], "c": r["condition"], "seed": r["seed"],
                     "valid": bool(s.get("valid_output")), "fc": s.get("flag_correct"), "flagged": s.get("flagged"),
                     "cost": (r.get("usage") or {}).get("cost_usd") or 0.0, "stop": r.get("stop_reason")})
cnt = Counter((r["src"], r["c"]) for r in rows)
assert all(cnt[("study1b_v1", c)] == n for c, n in (("O", 150), ("OS", 120))), cnt
assert all(cnt[(s, c)] == n for s, n in (("pilot3_v1", 30), ("cross_model_v1", 60), ("reasoning_models_v1", 60)) for c in "ABC"), cnt


def fc(r, rule):
    if rule == "strict":
        return float(r["fc"] or 0) if r["valid"] else 0.0
    if rule == "valid_only":
        return float(r["fc"]) if r["valid"] and r["fc"] is not None else None
    return float(r["fc"]) if r["fc"] is not None else 0.0


def cells(m, c, rule, pool=False):
    """Correct rate per task for one condition (seeds averaged); m=None pools all models."""
    out = {}
    for t in T:
        xs = [fc(r, rule) for r in rows if (m is None or r["m"] == m) and r["t"] == t and r["c"] == c]
        xs = [x for x in xs if x is not None]
        out[t] = float(np.mean(xs)) if xs else float("nan")
    return out


def ba(cm):
    return (np.nanmean([cm[t] for t in T if SF[t]]) + np.nanmean([cm[t] for t in T if not SF[t]])) / 2


def contrast(m, a, b, rule):
    """b minus a, task-level, weighted as in paper 1."""
    ca, cb = cells(m, a, rule), cells(m, b, rule)
    d = np.array([(cb[t] - ca[t]) * W[t] for t in T if not (np.isnan(cb[t]) or np.isnan(ca[t]))])
    lo, hi = bootstrap_ci(d)
    return {"diff": float(ba(cb) - ba(ca)), "lo": lo, "hi": hi, "p": sign_flip_p(d), "n_tasks": len(d)}


FAMILIES = {"O-A": ("A", "O"), "O-B": ("B", "O"), "O-C": ("C", "O"), "OS-O": ("O", "OS")}
res = {"ba": {}, "contrasts": {}, "per_task": {}}
for rule in ("primary", "strict", "valid_only"):
    res["ba"][rule] = {m: {c: float(ba(cells(m, c, rule))) for c in ("A", "B", "C", "O", "OS") if not (m == "Sonnet" and c == "OS")} for m in M}
    res["contrasts"][rule] = {}
    for fam, (a, b) in FAMILIES.items():
        models = [m for m in M if not (m == "Sonnet" and "OS" in (a, b))]
        cs = {m: contrast(m, a, b, rule) for m in models}
        for m, adj in zip(models, holm([cs[m]["p"] for m in models])):
            cs[m]["p_holm"] = adj
        res["contrasts"][rule][fam] = cs

# per-task correct rates (primary), pooled over models and per model
with open(os.path.join(OUT, "per_task.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["model", "task_id", "gold_families", "should_flag", "A", "B", "C", "O", "OS"])
    for m in M + ["ALL"]:
        cs = {c: cells(None if m == "ALL" else m, c, "primary") for c in ("A", "B", "C", "O", "OS")}
        for t in T:
            w.writerow([m, t, len(GOLD[t]), SF[t]] + [("" if np.isnan(cs[c][t]) else round(cs[c][t], 3)) for c in ("A", "B", "C", "O", "OS")])
        res["per_task"][m] = {t: {c: (None if np.isnan(cs[c][t]) else round(cs[c][t], 3)) for c in cs} for t in T}

# operational definitions (primary, per model)
defs = {}
for m in M:
    c = res["contrasts"]["primary"]["O-A"][m]
    helps = c["diff"] > 0 and c["lo"] > 0
    harmed = c["hi"] < 0
    d = {"oracle_helps": bool(helps), "oracle_harmed": bool(harmed), "O-A": [round(c["diff"], 3), round(c["lo"], 3), round(c["hi"], 3)]}
    if m != "Sonnet":
        os_ = res["contrasts"]["primary"]["OS-O"][m]
        a_excl = os_["lo"] > 0 or os_["hi"] < 0

        def share(cond, t):
            xs = [1.0 if r["flagged"] else 0.0 for r in rows if r["m"] == m and r["t"] == t and r["c"] == cond and r["flagged"] is not None]
            return (float(np.mean(xs)) if xs else float("nan")), len(xs)
        gold_diffs = {t: abs(share("OS", t)[0] - share("O", t)[0]) for t in GOLD_TASKS}
        nogold_diffs = {t: abs(share("OS", t)[0] - share("O", t)[0]) for t in NOGOLD_TASKS}
        n_b = sum(1 for v in gold_diffs.values() if v >= 2 / 3 - 1e-9)
        d.update({"OS-O": [round(os_["diff"], 3), round(os_["lo"], 3), round(os_["hi"], 3)], "criterion_a_ci_excludes_0": bool(a_excl),
                  "criterion_b_tasks_with_flag_share_diff_ge_2_3": n_b, "criterion_b": n_b >= 2,
                  "changes_decisions_descriptive": bool(a_excl or n_b >= 2),
                  "flag_share_diff_gold_tasks": {t: round(v, 3) for t, v in gold_diffs.items()},
                  "flag_share_diff_nogold_tasks_noise_reference": {t: round(v, 3) for t, v in nogold_diffs.items()}})
    defs[m] = d
res["definitions"] = defs

# drift check: no-gold tasks, O correct rate versus Study 1 A rate
res["drift_check"] = {m: {t: {"A_study1": round(cells(m, "A", "primary")[t], 3), "O_study1b": round(cells(m, "O", "primary")[t], 3)} for t in NOGOLD_TASKS} for m in M}

# validity and cost
res["validity"] = {m: {c: {"runs": sum(1 for r in rows if r["src"] == "study1b_v1" and r["m"] == m and r["c"] == c),
                          "invalid": sum(1 for r in rows if r["src"] == "study1b_v1" and r["m"] == m and r["c"] == c and not r["valid"]),
                          "no_scorable_flag": sum(1 for r in rows if r["src"] == "study1b_v1" and r["m"] == m and r["c"] == c and r["fc"] is None)}
                      for c in ("O", "OS") if not (m == "Sonnet" and c == "OS")} for m in M}
res["cost_usd"] = {m: round(sum(r["cost"] for r in rows if r["src"] == "study1b_v1" and r["m"] == m), 3) for m in M}
res["stop_reasons"] = dict(Counter(r["stop"] for r in rows if r["src"] == "study1b_v1"))
json.dump(res, open(os.path.join(OUT, "results.json"), "w", encoding="utf-8"), indent=1, default=float)


# ------------------------------------------------------------------ report
def f3(x):
    return "n/a" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.3f}"


def cell(c):
    return f"{c['diff']:+.3f} [{c['lo']:+.3f}, {c['hi']:+.3f}] p={c['p']:.2f} (Holm {c['p_holm']:.2f})"


L = ["# Study 1b results (descriptive)", "",
     "Generated by study1b/analyze_study1b.py from saved runs; no model calls. Method as specified in study1b/prereg_1b.md and identical to paper 1. "
     "Ten tasks cannot detect effects below about 0.3 in balanced accuracy; every result is descriptive, and a CI that includes 0 is not evidence of no effect. "
     "OS also delivers more text than O, so an OS - O difference is annotation plus extra length.", "",
     "## 1. Balanced accuracy by model and condition (primary rule)", "", "| Model | A | B | C | O | OS |", "|---|---|---|---|---|---|"]
for m in M:
    b = res["ba"]["primary"][m]
    L.append(f"| {m} | " + " | ".join(f3(b.get(c)) for c in ("A", "B", "C", "O", "OS")) + " |")
L += ["", "A, B, C are Study 1 (not rerun); O and OS are Study 1b. 3 seeds per task and condition.", "", "## 2. Contrasts, primary rule (difference [95% bootstrap CI], sign-flip p, Holm within contrast family)", ""]
L += ["| Model | O - A (Q1) | O - B | O - C | OS - O (Q2) |", "|---|---|---|---|---|"]
for m in M:
    r = [cell(res["contrasts"]["primary"][f][m]) if m in res["contrasts"]["primary"][f] else "not run" for f in FAMILIES]
    L.append(f"| {m} | " + " | ".join(r) + " |")
L += ["", "## 3. Operational definitions (primary rule, per model)", "",
      "| Model | Oracle helps (O - A > 0, CI low > 0) | Oracle harmed (CI high < 0) | Scope annotation changes decisions (descriptive) | (a) OS - O CI excludes 0 | (b) tasks with flag-share change >= 2/3 (of 7) |", "|---|---|---|---|---|---|"]
for m in M:
    d = defs[m]
    L.append(f"| {m} | {d['oracle_helps']} | {d['oracle_harmed']} | " + (f"{d['changes_decisions_descriptive']} | {d['criterion_a_ci_excludes_0']} | {d['criterion_b_tasks_with_flag_share_diff_ge_2_3']} |" if m != "Sonnet" else "not run (O only) | | |"))
L += ["", "Flag-share change between OS and O per task (noise reference: the three no-gold tasks, where OS and O are identical):", ""]
L += ["| Model | " + " | ".join(f"{t}{'*' if t in NOGOLD_TASKS else ''}" for t in T) + " |", "|---|" + "---|" * len(T)]
for m in M:
    if m == "Sonnet":
        continue
    g = {**defs[m]["flag_share_diff_gold_tasks"], **defs[m]["flag_share_diff_nogold_tasks_noise_reference"]}
    L.append(f"| {m} | " + " | ".join(f3(g[t]) for t in T) + " |")
L += ["", "\\* no gold families.", "", "## 4. Sensitivity (O - A and OS - O under the strict and valid-only rules)", "", "| Rule | Model | O - A | OS - O |", "|---|---|---|---|"]
for rule in ("strict", "valid_only"):
    for m in M:
        oa = res["contrasts"][rule]["O-A"][m]
        oso = res["contrasts"][rule]["OS-O"].get(m)
        L.append(f"| {rule} | {m} | {oa['diff']:+.3f} [{oa['lo']:+.3f}, {oa['hi']:+.3f}] | " + (f"{oso['diff']:+.3f} [{oso['lo']:+.3f}, {oso['hi']:+.3f}]" if oso else "not run") + " |")
L += ["", "## 5. Drift check: no-gold tasks (O is A plus the read_family tool); Study 1 A versus Study 1b O correct rate", "",
      "| Model | " + " | ".join(f"{t} A / O" for t in NOGOLD_TASKS) + " |", "|---|" + "---|" * len(NOGOLD_TASKS)]
for m in M:
    L.append(f"| {m} | " + " | ".join(f"{res['drift_check'][m][t]['A_study1']:.2f} / {res['drift_check'][m][t]['O_study1b']:.2f}" for t in NOGOLD_TASKS) + " |")
L += ["", "## 6. Per-task correct rate, all five models pooled (primary rule), for the three tasks named in the predictions", "",
      "| Task | Should flag | Gold families | A | B | C | O | OS |", "|---|---|---|---|---|---|---|---|"]
for t in ("RT-012", "RT-147", "RT-179"):
    p = res["per_task"]["ALL"][t]
    L.append(f"| {t} | {SF[t]} | {len(GOLD[t])} | " + " | ".join(f3(p[c]) for c in ("A", "B", "C", "O", "OS")) + " |")
def pooled4(c, t):
    xs = [fc(r, "primary") for r in rows if r["m"] != "Sonnet" and r["t"] == t and r["c"] == c]
    return float(np.mean(xs))


L += ["", "Pooled over models (n = 15 per cell for A, B, C and O; 12 for OS, which excludes Sonnet). The prereg sets no numeric threshold for the three per-task predictions; direction is read from these rates only.", "",
      "Same table restricted to the four models that ran OS (Gemini, Haiku, gpt-oss, DeepSeek; n = 12 per cell), so that O and OS are directly comparable:", "",
      "| Task | A | B | C | O | OS | OS - O |", "|---|---|---|---|---|---|---|"]
for t in ("RT-012", "RT-147", "RT-179"):
    v = {c: pooled4(c, t) for c in ("A", "B", "C", "O", "OS")}
    L.append(f"| {t} | " + " | ".join(f3(v[c]) for c in ("A", "B", "C", "O", "OS")) + f" | {v['OS'] - v['O']:+.3f} |")
L += ["",
      "## 7. Run validity and cost (Study 1b)", "", "| Model | O runs / invalid / no scorable flag | OS runs / invalid / no scorable flag | Cost (USD) |", "|---|---|---|---|"]
for m in M:
    v = res["validity"][m]
    fmt = lambda x: f"{x['runs']} / {x['invalid']} / {x['no_scorable_flag']}"
    L.append(f"| {m} | {fmt(v['O'])} | {fmt(v['OS']) if 'OS' in v else 'not run'} | {res['cost_usd'][m]:.3f} |")
L += ["", f"Stop reasons: {res['stop_reasons']}. Total cost {sum(res['cost_usd'].values()):.2f} USD.", ""]
open(os.path.join(OUT, "report.md"), "w", encoding="utf-8").write("\n".join(L))
print("\n".join(L))
