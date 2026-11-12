"""Recompute-and-match for Study 1 (paper 1) from the raw run files. Read-only; no model calls.

Rescores every raw run with bench.scoring.score_replay, re-audits it with the fixed bench.retrieval_audit on the
memory_v3 snapshot the agent searched, and regenerates the primary table, the sensitivity table, the invalid-output
counts, the 300-pair tally and the Appendix C counts. Each number is compared with the value published in
paper/ssrn_research_memory_basketball.tex (3-decimal rounding; p-values to 2 decimals).
Run with the venv that has scikit-learn: %TEMP%\\supp_audit_venv\\Scripts\\python.exe analysis_fixes\\recompute_and_match_study1.py
"""
import csv, glob, json, os, sys
from collections import Counter
import numpy as np

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import scoring, retrieval_audit as ra
from bench.stats import bootstrap_ci, sign_flip_p
from runner.experiment import load_task, answer_key, ensure_snapshot_v3

EXPS = [("runs/pilot3_v1", "analysis_p3"), ("runs/cross_model_v1", "analysis_cross"), ("runs/reasoning_models_v1", "analysis_rm")]
M = ["Gemini", "Haiku", "gpt-oss", "Sonnet", "DeepSeek"]
T = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]

# ---- published values (paper 1) ----
PRIMARY = {  # A, B, C, (B-A, lo, hi, p), (C-A, lo, hi, p)
    "Gemini": (.639, .681, .583, (.042, -.264, .389, .91), (-.056, -.361, .292, .84)),
    "Haiku": (.625, .583, .639, (-.042, -.333, .319, .88), (.014, -.333, .389, 1.00)),
    "gpt-oss": (.542, .528, .528, (-.014, -.250, .250, 1.00), (-.014, -.333, .347, 1.00)),
    "Sonnet": (.736, .653, .722, (-.083, -.319, .111, .56), (-.014, -.125, .083, 1.00)),
    "DeepSeek": (.514, .681, .722, (.167, -.097, .486, .44), (.208, .069, .389, .06)),
}
HOLM_DEEPSEEK_C = .62
STRICT = {"Gemini": (0, -.083), "Haiku": (-.042, -.014), "gpt-oss": (.111, .056), "Sonnet": (-.194, -.069), "DeepSeek": (.139, .167)}
STRICT_SONNET_B_CI = (-.389, -.014)
VALID_ONLY = {"Gemini": (.042, -.069), "Haiku": (-.056, .035), "gpt-oss": (.042, .125), "Sonnet": (0, .014), "DeepSeek": (.167, .208)}
INVALID = {"Gemini": (0, 1, 1), "Haiku": (3, 1, 4), "gpt-oss": (4, 1, 6), "Sonnet": (0, 6, 3), "DeepSeek": (0, 1, 1)}
TALLY = {"fixed": 47, "broke": 46, "same_correct": 136, "same_wrong": 71}
TALLY_MODEL = {"Gemini": (10, 12), "Haiku": (8, 11), "gpt-oss": (10, 13), "Sonnet": (5, 6), "DeepSeek": (14, 4)}
L_TIER = {"RT-012": 5, "RT-014": 8, "RT-066": 49, "RT-112": 9, "RT-179": 7, "RT-183": 43}
RT179 = {"B": (1.00, .93), "C": (1.00, .87)}
POOLED = {"B": (65, 50, 47), "C": (47, 38, 35)}
USED_PER_RETURNED = {"B": .94, "C": .92}
ACC_RETURNED = {"B": (.82, .60), "C": (.66, .76)}
Q_RETURNED = {"B": 2, "C": 2}

checks = []


def check(name, got, want, tol=0.0005):
    ok = (got == want) if isinstance(want, (int, str)) and not isinstance(want, float) and tol == 0 else abs(float(got) - float(want)) <= tol + 1e-9
    checks.append(ok)
    print(f"  {'MATCH' if ok else 'MISMATCH'}  {name}: recomputed {got if not isinstance(got, float) else round(got, 3)} published {want}")


def short(name):
    n = name.lower()
    return next(m for k, m in (("gemini", "Gemini"), ("haiku", "Haiku"), ("gpt-oss", "gpt-oss"), ("sonnet", "Sonnet"), ("deepseek", "DeepSeek")) if k in n)


keys = answer_key()
SF = {t: int(bool(keys[t]["should_flag_before_running"])) for t in T}
saved = {}
for d, a in EXPS:
    for row in csv.DictReader(open(os.path.join(HB, d, a, "per_run.csv"), encoding="utf-8")):
        saved[row["run_id"]] = row
ctx = ra.Context()
rows, score_mismatch = [], 0
for d, _ in EXPS:
    for p in sorted(glob.glob(os.path.join(HB, d, "raw", "*.json"))):
        r = json.load(open(p, encoding="utf-8"))
        if r["run_id"] not in saved:
            continue
        k, task = keys[r["task_id"]], load_task(r["task_id"])
        s = scoring.score_replay(r.get("final"), k, r["condition"], {})
        sv = saved[r["run_id"]]
        same = str(bool(s.get("valid_output"))) == str(sv["valid_output"] in ("True", "1", "1.0")) and \
            (str(s.get("flag_correct", "")) == "" and sv["flag_correct"] == "" or
             sv["flag_correct"] != "" and s.get("flag_correct") is not None and float(sv["flag_correct"]) == s["flag_correct"])
        score_mismatch += not same
        snap, _ = ensure_snapshot_v3(task)
        a = ra.audit(r, task, k, snap, ctx, None)
        rows.append({"run_id": r["run_id"], "m": short(r["model_name"]), "t": r["task_id"], "c": r["condition"], "seed": r["seed"],
                     "valid": bool(s.get("valid_output")), "fc": s.get("flag_correct"), **a})
print(f"raw runs: {len(rows)}; rescoring differs from saved per_run.csv in {score_mismatch} runs")
check("runs", len(rows), 450, 0)


def fc(r, rule):
    if rule == "strict":
        return float(r["fc"] or 0) if r["valid"] else 0.0
    if rule == "valid_only":
        return float(r["fc"]) if r["valid"] else None
    return float(r["fc"]) if r["fc"] is not None else 0.0


def cells(m, c, rule):
    out = {}
    for t in T:
        xs = [fc(r, rule) for r in rows if r["m"] == m and r["t"] == t and r["c"] == c]
        xs = [x for x in xs if x is not None]
        out[t] = np.mean(xs) if xs else np.nan
    return out


def ba(cm):
    return (np.nanmean([cm[t] for t in T if SF[t]]) + np.nanmean([cm[t] for t in T if not SF[t]])) / 2


W = {t: (1 / 0.8 if SF[t] else 1 / 1.2) for t in T}


def contrast(m, c, rule):
    ca, cb = cells(m, "A", rule), cells(m, c, rule)
    d = np.array([(cb[t] - ca[t]) * W[t] for t in T if not (np.isnan(cb[t]) or np.isnan(ca[t]))])
    lo, hi = bootstrap_ci(d)
    return ba(cb) - ba(ca), lo, hi, sign_flip_p(d)


print("\nPRIMARY TABLE (scored where possible)")
pvals = []
for m in M:
    A, B, C, pb, pc = PRIMARY[m]
    for c, want in (("A", A), ("B", B), ("C", C)):
        check(f"{m} BA {c}", ba(cells(m, c, "primary")), want)
    for c, want in (("B", pb), ("C", pc)):
        d, lo, hi, p = contrast(m, c, "primary")
        pvals.append((m, c, p))
        check(f"{m} {c}-A", d, want[0]); check(f"{m} {c}-A CI low", lo, want[1]); check(f"{m} {c}-A CI high", hi, want[2])
        check(f"{m} {c}-A p", p, want[3], 0.005)
ps, prev, holm = sorted(pvals, key=lambda x: x[2]), 0, {}
for i, (m, c, p) in enumerate(ps):
    prev = max(prev, min(1, (len(ps) - i) * p)); holm[(m, c)] = prev
check("Holm DeepSeek C-A", holm[("DeepSeek", "C")], HOLM_DEEPSEEK_C, 0.005)

print("\nSENSITIVITY TABLE")
for rule, pub in (("strict", STRICT), ("valid_only", VALID_ONLY)):
    for m in M:
        for c, want in zip("BC", pub[m]):
            check(f"{rule} {m} {c}-A", contrast(m, c, rule)[0], want)
_, lo, hi, _ = contrast("Sonnet", "B", "strict")
check("strict Sonnet B-A CI low", lo, STRICT_SONNET_B_CI[0]); check("strict Sonnet B-A CI high", hi, STRICT_SONNET_B_CI[1])
for m in M:
    for c, want in zip("ABC", INVALID[m]):
        check(f"invalid outputs {m} {c}", sum(1 for r in rows if r["m"] == m and r["c"] == c and not r["valid"]), want, 0)

print("\nTALLY (memory run vs same-seed no-memory run, primary rule)")
tot = Counter()
for m in M:
    cnt = Counter()
    for r in rows:
        if r["m"] == m and r["c"] in "BC":
            a = next(x for x in rows if x["m"] == m and x["t"] == r["t"] and x["seed"] == r["seed"] and x["c"] == "A")
            fa, fb = fc(a, "primary"), fc(r, "primary")
            cnt["fixed" if (fa, fb) == (0, 1) else "broke" if (fa, fb) == (1, 0) else "same_correct" if fa == 1 else "same_wrong"] += 1
    tot += cnt
    check(f"tally {m} fixed", cnt["fixed"], TALLY_MODEL[m][0], 0); check(f"tally {m} broke", cnt["broke"], TALLY_MODEL[m][1], 0)
for k2, want in TALLY.items():
    check(f"tally all {k2}", tot[k2], want, 0)

print("\nAPPENDIX C (fixed audit, memory_v3 snapshot)")
for t, want in L_TIER.items():
    check(f"lesson-tier families {t}", next(r for r in rows if r["t"] == t)["lesson_relevant_in_memory"], want, 0)
for c in "BC":
    g = [r for r in rows if r["t"] == "RT-179" and r["c"] == c]
    check(f"RT-179 {c} returned rate", np.mean([r["retrieval_successful"] for r in g]), RT179[c][0], 0.005)
    check(f"RT-179 {c} used rate", np.mean([r["meaningfully_used"] for r in g]), RT179[c][1], 0.005)
    g = [r for r in rows if r["c"] == c]
    men, ret, use = (sum(bool(r[x]) for r in g) for x in ("relevant_surfaced", "retrieval_successful", "meaningfully_used"))
    check(f"pooled {c} mentioned", men, POOLED[c][0], 0); check(f"pooled {c} returned", ret, POOLED[c][1], 0)
    check(f"pooled {c} used", use, POOLED[c][2], 0); check(f"pooled {c} used/returned", use / ret, USED_PER_RETURNED[c], 0.005)
    rel = [r for r in g if r["relevant_families_in_memory"] > 0]
    y = [fc(r, "primary") for r in rel if r["retrieval_successful"]]; n = [fc(r, "primary") for r in rel if not r["retrieval_successful"]]
    check(f"accuracy {c} returned", np.mean(y), ACC_RETURNED[c][0], 0.005); check(f"accuracy {c} not returned", np.mean(n), ACC_RETURNED[c][1], 0.005)
    q = [r for r in g if r["question_relevant_returned"] > 0]
    check(f"question tier returned {c}", len(q), Q_RETURNED[c], 0)
    print("     question-tier returns:", [f"{r['t']} {r['m']} s{r['seed']}" for r in q])

print(f"\n{sum(checks)} of {len(checks)} published numbers match")
