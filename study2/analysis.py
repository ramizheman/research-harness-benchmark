"""The one analysis script for Study 2. Reads saved runs only; no model calls.

  python study2/analysis.py reproduce   Recomputes the published Study 1 and Study 1b numbers from the raw run files with
                                        the functions below and compares each with the paper (exit 1 on any mismatch).
  python study2/analysis.py power       Minimum detectable effects for Study 2 from the Study 1 and 1b seed-1 runs.
  python study2/analysis.py study2      The preregistered Study 2 analysis (study2/prereg.md) of runs/study2_v1.

Method, identical to paper 1 and Study 1b: every raw run is rescored with bench.scoring.score_replay; correct rate per
task = mean over the runs in the cell; balanced accuracy = mean of the flag-task mean and the no-flag-task mean;
contrast = mean of per-task differences weighted by 1/(2 p) for flag tasks and 1/(2 (1 - p)) for no-flag tasks, where p
is the share of flag tasks (this mean equals the balanced-accuracy difference); 95% CI = bench.stats.bootstrap_ci
(10,000 resamples, seed 0) over tasks; p = bench.stats.sign_flip_p (exact up to 16 tasks, else 20,000 sign draws);
Holm within each contrast family. Rules: primary (no scorable flag counts as wrong), strict (invalid counts as wrong),
valid_only (invalid or unscorable dropped).
"""
import csv
import glob
import json
import os
import random
import sys
from collections import Counter

import numpy as np

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import retrieval_audit as ra, scoring  # noqa: E402
from bench.stats import bootstrap_ci, holm, sign_flip_p  # noqa: E402
from runner import experiment  # noqa: E402

S1_TASKS = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]
S1_SOURCES = ["runs/pilot3_v1", "runs/cross_model_v1", "runs/reasoning_models_v1"]
S1B_SOURCE = "runs/study1b_v1"
S2_MODELS = ["Gemini", "DeepSeek", "Haiku", "gpt-oss"]
RULES = ("primary", "strict", "valid_only")
DECISION_FIELDS = "risks[].text, testability.blocking_constraints[].text, historical_effect.explanation"


def short(name):
    n = name.lower()
    return next(m for k, m in (("gemini", "Gemini"), ("haiku", "Haiku"), ("gpt-oss", "gpt-oss"), ("sonnet", "Sonnet"),
                               ("deepseek", "DeepSeek")) if k in n)


# ------------------------------------------------------------------ rows and scoring
def load_rows(dirs, keys, keep_raw=False):
    rows = []
    for d in dirs:
        for p in sorted(glob.glob(os.path.join(HB, d, "raw", "*.json"))):
            r = json.load(open(p, encoding="utf-8"))
            s = scoring.score_replay(r.get("final"), keys[r["task_id"]], r["condition"], {})
            u = r.get("usage") or {}
            row = {"src": os.path.basename(d), "run_id": r["run_id"], "m": short(r["model_name"]), "t": r["task_id"],
                   "c": r["condition"], "seed": r["seed"], "valid": bool(s.get("valid_output")), "fc": s.get("flag_correct"),
                   "flagged": s.get("flagged"), "cost": u.get("cost_usd") or 0.0, "cost_known": u.get("cost_known", True),
                   "stop": r.get("stop_reason"), "wall": r.get("wall_seconds")}
            if keep_raw:
                row["_raw"] = r
            rows.append(row)
    return rows


def fc(r, rule):
    if rule == "strict":
        return float(r["fc"] or 0) if r["valid"] else 0.0
    if rule == "valid_only":
        return float(r["fc"]) if r["valid"] and r["fc"] is not None else None
    return float(r["fc"]) if r["fc"] is not None else 0.0


def weights(tasks, sf):
    p = np.mean([sf[t] for t in tasks])
    return {t: (1 / (2 * p) if sf[t] else 1 / (2 * (1 - p))) for t in tasks}


def cells(rows, tasks, m, c, rule):
    """Correct rate per task for one model (None pools all models) and condition."""
    out = {}
    for t in tasks:
        xs = [fc(r, rule) for r in rows if (m is None or r["m"] == m) and r["t"] == t and r["c"] == c]
        xs = [x for x in xs if x is not None]
        out[t] = float(np.mean(xs)) if xs else float("nan")
    return out


def ba(cm, tasks, sf):
    return float((np.nanmean([cm[t] for t in tasks if sf[t]]) + np.nanmean([cm[t] for t in tasks if not sf[t]])) / 2)


def task_diffs(rows, tasks, sf, m, a, b, rule):
    """Weighted per-task differences b minus a. m=None pools: the per-task difference is the mean over models."""
    W = weights(tasks, sf)
    models = sorted({r["m"] for r in rows}) if m is None else [m]
    out = {}
    for t in tasks:
        ds = []
        for mm in models:
            ca, cb = cells(rows, [t], mm, a, rule)[t], cells(rows, [t], mm, b, rule)[t]
            if not (np.isnan(ca) or np.isnan(cb)):
                ds.append(cb - ca)
        if ds:
            out[t] = float(np.mean(ds)) * W[t]
    return out


def contrast(rows, tasks, sf, m, a, b, rule):
    d = task_diffs(rows, tasks, sf, m, a, b, rule)
    arr = np.array([d[t] for t in tasks if t in d])
    lo, hi = bootstrap_ci(arr)
    if m is None:
        models = sorted({r["m"] for r in rows})
        diff = float(np.mean([ba(cells(rows, tasks, mm, b, rule), tasks, sf) - ba(cells(rows, tasks, mm, a, rule), tasks, sf) for mm in models]))
    else:
        diff = ba(cells(rows, tasks, m, b, rule), tasks, sf) - ba(cells(rows, tasks, m, a, rule), tasks, sf)
    return {"diff": diff, "lo": lo, "hi": hi, "p": sign_flip_p(arr), "n_tasks": len(arr)}


def with_holm(cs):
    ks = list(cs)
    for k, adj in zip(ks, holm([cs[k]["p"] for k in ks])):
        cs[k]["p_holm"] = adj
    return cs


def tally(rows, m, a, b, rule="primary"):
    """Same-model, same-task, same-seed pairs: b fixed a wrong decision, broke a correct one, or left it."""
    idx = {(r["m"], r["t"], r["seed"], r["c"]): r for r in rows}
    cnt = Counter()
    for (mm, t, s, c), r in idx.items():
        if c != b or (m is not None and mm != m) or (mm, t, s, a) not in idx:
            continue
        fa, fb = fc(idx[(mm, t, s, a)], rule), fc(r, rule)
        cnt["fixed" if (fa, fb) == (0, 1) else "broke" if (fa, fb) == (1, 0) else "same_correct" if fa == 1 else "same_wrong"] += 1
    return dict(cnt)


# ------------------------------------------------------------------ retrieval audit and decision-linked use
def decision_linked_use(run, task, key, snap, ctx):
    """Stronger 'used' (Study 2, secondary): a relevant family that appeared in the run's memory tool results is named
    in a decision-bearing field (risks, blocking constraints, or the explanation of how history changed the decision),
    and no status the output gives that family contradicts the family's recorded stratum."""
    final = run.get("final") if isinstance(run.get("final"), dict) else {}
    strata, risks, fg, rqc = ra.snapshot_info(snap, with_risks=True)
    snap_fams = set(strata) | {ctx.family_of[p] for p in task["permitted_records"] if p in ctx.family_of}
    relevant = ra.relevant_families(task, key, ctx, snap_fams) | ra.lesson_families(key, risks, strata)
    seen_text = "\n".join(m["content"] for m in run.get("messages", []) if m["role"] == "user" and m["content"].startswith("TOOL_RESULT")
                          and m["content"].split(":", 1)[0].split()[-1] in ra.MEMORY_TOOLS)
    seen = set().union(*[ra.families_of_id(i, ctx, fg, rqc) for i in ra.ids_in(seen_text)]) if seen_text else set()
    texts = [str(x.get("text", "")) for x in final.get("risks") or [] if isinstance(x, dict)]
    tb = final.get("testability") if isinstance(final.get("testability"), dict) else {}
    texts += [str(x.get("text", "")) for x in tb.get("blocking_constraints") or [] if isinstance(x, dict)]
    he = final.get("historical_effect") if isinstance(final.get("historical_effect"), dict) else {}
    texts.append(str(he.get("explanation") or ""))
    named = set().union(*[ra.families_of_id(i, ctx, fg, rqc) for i in ra.ids_in("\n".join(texts))]) & relevant & seen
    contradicted = set()
    for x in final.get("historical_evidence") or []:
        if not isinstance(x, dict):
            continue
        st = ra.V3_STATUS.get(str(x.get("status_as_recorded", "")).strip().lower(), str(x.get("status_as_recorded", "")).strip().lower())
        for f in ra.families_of_id(next(iter(ra.ids_in(str(x.get("id", "")))), str(x.get("id", ""))), ctx, fg, rqc):
            if st in ra.STRATA and strata.get(f) in ra.STRATA and strata[f] != st:
                contradicted.add(f)
    linked = named - contradicted
    return {"decision_linked_use": bool(linked), "decision_linked_families": "; ".join(sorted(linked)),
            "decision_named_contradicted": "; ".join(sorted(named & contradicted))}


def audit_rows(rows, keys, conditions):
    ctx = ra.Context()
    for r in rows:
        if r["c"] not in conditions:
            continue
        task = experiment.load_task(r["t"])
        snap, _ = experiment.ensure_snapshot_v3(task)
        r.update(ra.audit(r["_raw"], task, keys[r["t"]], snap, ctx, None))
        r.update(decision_linked_use(r["_raw"], task, keys[r["t"]], snap, ctx))
    return rows


# ------------------------------------------------------------------ reproduce the published numbers
CHECKS = []


def check(name, got, want, tol=0.0005):
    exact = isinstance(want, int) and not isinstance(want, bool) and tol == 0
    ok = (got == want) if exact else (got is not None and abs(float(got) - float(want)) <= tol + 1e-9)
    CHECKS.append((name, ok))
    print(f"  {'MATCH' if ok else 'MISMATCH'}  {name}: recomputed {round(got, 3) if isinstance(got, float) else got} published {want}")


S1_PRIMARY = {  # A, B, C, (B-A, lo, hi, p), (C-A, lo, hi, p)
    "Gemini": (.639, .681, .583, (.042, -.264, .389, .91), (-.056, -.361, .292, .84)),
    "Haiku": (.625, .583, .639, (-.042, -.333, .319, .88), (.014, -.333, .389, 1.00)),
    "gpt-oss": (.542, .528, .528, (-.014, -.250, .250, 1.00), (-.014, -.333, .347, 1.00)),
    "Sonnet": (.736, .653, .722, (-.083, -.319, .111, .56), (-.014, -.125, .083, 1.00)),
    "DeepSeek": (.514, .681, .722, (.167, -.097, .486, .44), (.208, .069, .389, .06)),
}
S1_STRICT = {"Gemini": (0, -.083), "Haiku": (-.042, -.014), "gpt-oss": (.111, .056), "Sonnet": (-.194, -.069), "DeepSeek": (.139, .167)}
S1_VALID_ONLY = {"Gemini": (.042, -.069), "Haiku": (-.056, .035), "gpt-oss": (.042, .125), "Sonnet": (0, .014), "DeepSeek": (.167, .208)}
S1_INVALID = {"Gemini": (0, 1, 1), "Haiku": (3, 1, 4), "gpt-oss": (4, 1, 6), "Sonnet": (0, 6, 3), "DeepSeek": (0, 1, 1)}
S1_TALLY = {"fixed": 47, "broke": 46, "same_correct": 136, "same_wrong": 71}
S1_TALLY_MODEL = {"Gemini": (10, 12), "Haiku": (8, 11), "gpt-oss": (10, 13), "Sonnet": (5, 6), "DeepSeek": (14, 4)}
S1_POOLED = {"B": (65, 50, 47), "C": (47, 38, 35)}
S1_ACC_RETURNED = {"B": (.82, .60), "C": (.66, .76)}
S1B_TABLE = {  # O, OS, (O-A, lo, hi)
    "Gemini": (.861, .847, (.222, -.056, .597)), "Haiku": (.639, .667, (.014, -.250, .347)),
    "gpt-oss": (.625, .750, (.083, -.208, .431)), "Sonnet": (.722, None, (-.014, -.125, .083)),
    "DeepSeek": (.778, .806, (.264, 0.000, .556)),
}
S1B_POOLED_TASK = {"RT-012": (.33, .67, .60, 1.00), "RT-147": (.80, .47, .60, .67), "RT-179": (.20, .73, .53, .80)}


def reproduce():
    keys = experiment.answer_key()
    sf = {t: int(bool(keys[t]["should_flag_before_running"])) for t in S1_TASKS}
    rows = load_rows(S1_SOURCES, keys, keep_raw=True)
    T, M = S1_TASKS, list(S1_PRIMARY)
    print("STUDY 1 (paper 1, Tables 3 and 4, tally, Appendix C)")
    check("Study 1 runs", len(rows), 450, 0)
    pv = {}
    for m in M:
        A, B, C, pb, pc = S1_PRIMARY[m]
        for c, want in (("A", A), ("B", B), ("C", C)):
            check(f"{m} BA {c}", ba(cells(rows, T, m, c, "primary"), T, sf), want)
        for c, want in (("B", pb), ("C", pc)):
            x = contrast(rows, T, sf, m, "A", c, "primary")
            pv[(m, c)] = x["p"]
            check(f"{m} {c}-A", x["diff"], want[0]); check(f"{m} {c}-A CI low", x["lo"], want[1])
            check(f"{m} {c}-A CI high", x["hi"], want[2]); check(f"{m} {c}-A p", x["p"], want[3], 0.005)
    ks = list(pv)
    check("Holm DeepSeek C-A (ten contrasts)", dict(zip(ks, holm([pv[k] for k in ks])))[("DeepSeek", "C")], .62, 0.005)
    for rule, pub in (("strict", S1_STRICT), ("valid_only", S1_VALID_ONLY)):
        for m in M:
            for c, want in zip("BC", pub[m]):
                check(f"{rule} {m} {c}-A", contrast(rows, T, sf, m, "A", c, rule)["diff"], want)
    x = contrast(rows, T, sf, "Sonnet", "A", "B", "strict")
    check("strict Sonnet B-A CI low", x["lo"], -.389); check("strict Sonnet B-A CI high", x["hi"], -.014)
    for m in M:
        for c, want in zip("ABC", S1_INVALID[m]):
            check(f"invalid outputs {m} {c}", sum(1 for r in rows if r["m"] == m and r["c"] == c and not r["valid"]), want, 0)
    tot = Counter()
    for m in M:
        cnt = Counter(tally(rows, m, "A", "B")) + Counter(tally(rows, m, "A", "C"))
        tot += cnt
        check(f"tally {m} fixed", cnt["fixed"], S1_TALLY_MODEL[m][0], 0); check(f"tally {m} broke", cnt["broke"], S1_TALLY_MODEL[m][1], 0)
    for k, want in S1_TALLY.items():
        check(f"tally all {k}", tot[k], want, 0)
    audit_rows(rows, keys, ("B", "C"))
    for c in "BC":
        g = [r for r in rows if r["c"] == c]
        men, ret, use = (sum(bool(r[x]) for r in g) for x in ("relevant_surfaced", "retrieval_successful", "meaningfully_used"))
        check(f"pooled {c} mentioned", men, S1_POOLED[c][0], 0); check(f"pooled {c} returned", ret, S1_POOLED[c][1], 0)
        check(f"pooled {c} used", use, S1_POOLED[c][2], 0)
        rel = [r for r in g if r["relevant_families_in_memory"] > 0]
        check(f"accuracy {c} returned", float(np.mean([fc(r, "primary") for r in rel if r["retrieval_successful"]])), S1_ACC_RETURNED[c][0], 0.005)
        check(f"accuracy {c} not returned", float(np.mean([fc(r, "primary") for r in rel if not r["retrieval_successful"]])), S1_ACC_RETURNED[c][1], 0.005)
        check(f"question tier returned {c}", sum(1 for r in g if r["question_relevant_returned"] > 0), 2, 0)
    dl = {c: sum(r["decision_linked_use"] for r in rows if r["c"] == c) for c in "BC"}
    print(f"  (new, not published) decision-linked use: B {dl['B']} of {S1_POOLED['B'][2]} 'used' runs; C {dl['C']} of {S1_POOLED['C'][2]}")

    print("\nSTUDY 1b (paper 1, Table tab:study1b and Section 6 text)")
    rows_b = load_rows([S1B_SOURCE], keys)
    check("Study 1b runs", len(rows_b), 270, 0)
    allr = rows + rows_b
    for m, (o, os_, oa) in S1B_TABLE.items():
        check(f"{m} BA O", ba(cells(allr, T, m, "O", "primary"), T, sf), o)
        if os_ is not None:
            check(f"{m} BA OS", ba(cells(allr, T, m, "OS", "primary"), T, sf), os_)
        x = contrast(allr, T, sf, m, "A", "O", "primary")
        check(f"{m} O-A", x["diff"], oa[0]); check(f"{m} O-A CI low", x["lo"], oa[1]); check(f"{m} O-A CI high", x["hi"], oa[2])
    oa = with_holm({m: contrast(allr, T, sf, m, "A", "O", "primary") for m in S1B_TABLE})
    check("smallest Holm-adjusted O-A p (published: 0.94 or higher)", min(v["p_holm"] for v in oa.values()), 0.94, 0.005)
    for t, want in S1B_POOLED_TASK.items():
        for c, w in zip("ABCO", want):
            check(f"pooled {t} {c}", cells(allr, [t], None, c, "primary")[t], w, 0.005)
    check("Study 1b invalid runs", sum(1 for r in rows_b if not r["valid"]), 15, 0)
    check("Study 1b no scorable flag (all within the 15 invalid runs)", sum(1 for r in rows_b if r["fc"] is None), 2, 0)
    check("Study 1b cost", sum(r["cost"] for r in rows_b), 4.19, 0.005)
    n_ok = sum(ok for _, ok in CHECKS)
    print(f"\n{n_ok} of {len(CHECKS)} published numbers match")
    out = os.path.join(HB, "study2", "phase0")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "reproduce_checks.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["check", "match"])
        w.writerows(CHECKS)
    return 0 if n_ok == len(CHECKS) else 1


# ------------------------------------------------------------------ power
def power():
    """MDE for a Study 2 task-level contrast, from the spread of seed-1 per-task differences in Study 1 and 1b."""
    from statistics import NormalDist
    keys = experiment.answer_key()
    sf = {t: int(bool(keys[t]["should_flag_before_running"])) for t in S1_TASKS}
    rows = [r for r in load_rows(S1_SOURCES + [S1B_SOURCE], keys) if r["seed"] == 1 and r["m"] in S2_MODELS]
    man = json.load(open(os.path.join(HB, "study2", "task_manifest.json"), encoding="utf-8"))["tasks"]
    n, p2 = len(man), np.mean([m["should_flag_before_running"] for m in man])
    w2 = {1: 1 / (2 * p2), 0: 1 / (2 * (1 - p2))}
    z = NormalDist().inv_cdf
    res = {"n_tasks": n, "share_flag_tasks": round(float(p2), 3), "source": "Study 1 A/B and Study 1b O runs, seed 1, the four Study 2 models, ten tasks",
           "contrasts": {}}
    for a, b in (("A", "O"), ("B", "O")):
        per_model = {}
        for m in S2_MODELS:
            ca, cb = cells(rows, S1_TASKS, m, a, "primary"), cells(rows, S1_TASKS, m, b, "primary")
            per_model[m] = np.array([(cb[t] - ca[t]) * w2[sf[t]] for t in S1_TASKS])
        pooled = np.mean(np.vstack(list(per_model.values())), axis=0)
        sd = {m: float(np.std(v, ddof=1)) for m, v in per_model.items()}
        mde = lambda s, alpha: (z(1 - alpha / 2) + z(0.8)) * s / np.sqrt(n)  # noqa: E731
        res["contrasts"][f"{b}-{a}"] = {
            "sd_per_task_by_model": {m: round(s, 3) for m, s in sd.items()},
            "mde_per_model_80pct_alpha_0.0125": {m: round(float(mde(s, 0.05 / 4)), 3) for m, s in sd.items()},
            "mde_per_model_80pct_alpha_0.05": {m: round(float(mde(s, 0.05)), 3) for m, s in sd.items()},
            "sd_per_task_pooled": round(float(np.std(pooled, ddof=1)), 3),
            "mde_pooled_80pct_alpha_0.025": round(float(mde(np.std(pooled, ddof=1), 0.025)), 3)}
    json.dump(res, open(os.path.join(HB, "study2", "power.json"), "w", encoding="utf-8"), indent=1)
    print(json.dumps(res, indent=1))
    return 0


# ------------------------------------------------------------------ Study 2
def study2(run_dir="runs/study2_v1"):
    man = json.load(open(os.path.join(HB, "study2", "task_manifest.json"), encoding="utf-8"))["tasks"]
    T = [m["task_id"] for m in man]
    uncertain = {m["task_id"] for m in man if m["stratum"] == "uncertain"}
    gold = {m["task_id"]: m["gold_families"] for m in man}
    keys = experiment.answer_key()
    sf = {t: int(bool(keys[t]["should_flag_before_running"])) for t in T}
    experiment.load_config(os.path.join(HB, "configs", "study2.json"))
    rows = load_rows([run_dir], keys, keep_raw=True)
    M = [m for m in S2_MODELS if any(r["m"] == m for r in rows)]
    res = {"n_runs": len(rows), "models": M, "ba": {}, "contrasts": {}, "sensitivity": {}}
    for rule in RULES:
        res["ba"][rule] = {m: {c: ba(cells(rows, T, m, c, rule), T, sf) for c in "ABO"} for m in M}
        res["contrasts"][rule] = {}
        for a, b in (("A", "O"), ("B", "O")):
            res["contrasts"][rule][f"{b}-{a}"] = with_holm({m: contrast(rows, T, sf, m, a, b, rule) for m in M})
        pooled = with_holm({f"{b}-{a}": contrast(rows, T, sf, None, a, b, rule) for a, b in (("A", "O"), ("B", "O"))})
        res["contrasts"][rule]["pooled"] = pooled
    subsets = {"without the 12 uncertain tasks": [t for t in T if t not in uncertain],
               "tasks with gold families": [t for t in T if gold[t]],
               "tasks without gold families (noise reference: O is A there)": [t for t in T if not gold[t]]}
    for name, ts in subsets.items():
        res["sensitivity"][name] = {"n_tasks": len(ts), **{f"{b}-{a}": {**{m: contrast(rows, ts, sf, m, a, b, "primary") for m in M},
                                                                      "pooled": contrast(rows, ts, sf, None, a, b, "primary")}
                                                           for a, b in (("A", "O"), ("B", "O"))}}
    res["tally"] = {f"{b} vs {a}": {m: tally(rows, m, a, b) for m in M + [None]} for a, b in (("A", "O"), ("A", "B"), ("B", "O"))}
    audit_rows(rows, keys, ("B", "O"))
    res["retrieval"] = {c: {m: {k: int(sum(bool(r.get(k)) for r in rows if r["m"] == m and r["c"] == c))
                                for k in ("relevant_surfaced", "retrieval_successful", "meaningfully_used", "decision_linked_use")}
                            | {"runs": sum(1 for r in rows if r["m"] == m and r["c"] == c)} for m in M} for c in ("B", "O")}
    res["validity"] = {m: {c: {"runs": sum(1 for r in rows if r["m"] == m and r["c"] == c),
                               "invalid": sum(1 for r in rows if r["m"] == m and r["c"] == c and not r["valid"]),
                               "no_scorable_flag": sum(1 for r in rows if r["m"] == m and r["c"] == c and r["fc"] is None)}
                           for c in "ABO"} for m in M}
    res["cost_usd"] = {m: round(sum(r["cost"] for r in rows if r["m"] == m), 4) for m in M}
    res["stop_reasons"] = dict(Counter(r["stop"] for r in rows))
    out = os.path.join(HB, "study2", "analysis")
    os.makedirs(out, exist_ok=True)
    used = [r for r in rows if r.get("meaningfully_used") or r.get("decision_linked_use")]
    sample = sorted(random.Random(20261112).sample(used, min(30, len(used))), key=lambda r: r["run_id"])
    with open(os.path.join(out, "used_hand_check.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["run_id", "condition", "meaningfully_used", "decision_linked_use", "decision_linked_families", "cited_ids",
                    "hand_check_used (fill in: yes/no)", "note"])
        for r in sample:
            w.writerow([r["run_id"], r["c"], r.get("meaningfully_used"), r.get("decision_linked_use"), r.get("decision_linked_families"),
                        r.get("cited_ids"), "", ""])
    with open(os.path.join(out, "per_run.csv"), "w", newline="", encoding="utf-8") as f:
        cols = [k for k in rows[0] if not k.startswith("_")] if rows else []
        w = csv.DictWriter(f, fieldnames=sorted({k for r in rows for k in r if not k.startswith("_")}), extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    saved = os.path.join(HB, run_dir, "scores.csv")
    if os.path.exists(saved):
        sv = {r["run_id"]: r for r in csv.DictReader(open(saved, encoding="utf-8-sig"))}
        res["recompute_vs_scores_csv_mismatches"] = sum(1 for r in rows if r["run_id"] in sv and
                                                        str(sv[r["run_id"]].get("flag_correct", "")) not in (str(r["fc"]) if r["fc"] is not None else "", str(float(r["fc"])) if r["fc"] is not None else ""))
    json.dump(res, open(os.path.join(out, "results.json"), "w", encoding="utf-8"), indent=1, default=lambda x: None if x is None else float(x))
    print(json.dumps({k: res[k] for k in ("n_runs", "models", "cost_usd", "stop_reasons")}, indent=1))
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "reproduce"
    sys.exit({"reproduce": reproduce, "power": power, "study2": lambda: study2(*sys.argv[2:3])}[mode]())
