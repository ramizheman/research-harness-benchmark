r"""Cross-model replication analysis: gpt-oss-20b and claude-haiku-5.5 versus Gemini 2.5 Flash (Pilot 3).

Results are never pooled across models. Each model is analysed on its own 10 tasks (3 seeds averaged within task).
Cross-model comparisons are task-paired within the same condition. Gemini results come from the Pilot 3 per-run CSV;
earlier pilot files are only read.

Usage: python scripts\25_cross_model_analysis.py [configs\cross_model.json]
Writes <run>\analysis_cross\ per_run.csv, per_task.csv, contrasts.csv, citations.csv, summary.json, cross_model_report.md
"""
import csv
import itertools
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bench import common, stats  # noqa: E402
from runner import agent, experiment  # noqa: E402

HB = common.HB
cfg = experiment.load_config(os.path.join(HB, sys.argv[1] if len(sys.argv) > 1 else os.path.join("configs", "cross_model.json")))
OUT = os.path.join(cfg["_out"], "analysis_cross")
os.makedirs(OUT, exist_ok=True)
keys = experiment.answer_key()
TASKS = cfg["tasks"]
SEEDS = cfg["seeds"]

MODEL_SHORT = {
    "openai/gpt-oss-20b": "gpt-oss-20b",
    "anthropic/claude-haiku-5.5": "haiku-5.5",
    "gemini:gemini-2.5-flash": "gemini-2.5-flash",
    "mock:mock-gpt-oss-20b": "mock-gpt",
    "mock:mock-haiku-5.5": "mock-haiku",
}


def num(v):
    if v in ("", None):
        return None
    if v in ("True", "False"):
        return float(v == "True")
    try:
        return float(v)
    except ValueError:
        return v


def read_rows(path):
    return [{k: num(v) for k, v in r.items()} for r in csv.DictReader(open(path, encoding="utf-8-sig"))]


def derive(rs):
    w = experiment._p1_weights(rs)
    for x in rs:
        x["p1_weighted"] = x["flag_correct"] * w[x["task_id"]] if x.get("flag_correct") is not None else None
        for m in ("relevant_surfaced", "cites_relevant_seen", "retrieval_successful", "meaningfully_used"):
            x[m + "_num"] = float(bool(x.get(m)))
        x["any_fabrication_num"] = float((x.get("n_fabricated_citations") or 0) > 0)
    return rs


# ------------------------------------------------------------------ load current experiment rows
cm_rows_all = derive(read_rows(os.path.join(cfg["_out"], "scores.csv")))
model_names = sorted({r["model"] for r in cm_rows_all})

# ------------------------------------------------------------------ load Pilot 3 for cross-model comparison
p3_path = os.path.join(HB, "runs", "pilot3_v1", "scores.csv")
p3_rows = derive(read_rows(p3_path)) if os.path.exists(p3_path) else []
if p3_rows:
    p3_model = next((r["model"] for r in p3_rows), "gemini:gemini-2.5-flash")
    model_names_all = [p3_model] + model_names
else:
    model_names_all = model_names

raw_idx = {r["run_id"]: r for r in experiment.raw_runs(cfg)}
facts_cache = {}


def facts_for(task_id):
    if task_id not in facts_cache:
        d, _ = experiment.ensure_snapshot_v3(experiment.load_task(task_id))
        fs, _ = __import__("bench.memory_v2", fromlist=["x"]).facts_from_documents(os.path.join(d, "documents"))
        acc = {}
        for s, p, o, q in fs:
            acc.setdefault(s, []).append((p, o, q))
        facts_cache[task_id] = acc
    return facts_cache[task_id]


class _FakeSeen:
    def __init__(self, returned, facts):
        self.returned = returned
        self.facts = facts


def citation_check(final, run):
    if not isinstance(final, dict):
        return {"ids": 0, "unreturned": 0, "status_checked": 0, "status_wrong": 0}
    seen = _FakeSeen([i for c in run.get("tool_calls", []) for i in c.get("returned_ids", [])],
                     facts_for(run["task_id"]))
    ids = [i for i in agent.cited_ids(final) if not agent.PLACEHOLDER.match(i)]
    probs = agent.citation_problems(final, seen)
    he = [x for x in (final.get("historical_evidence") or []) if isinstance(x, dict)]
    checked = sum(1 for x in he if ("FAM:" + str(x.get("id", "")).strip().removeprefix("FAM:")) in set(seen.returned))
    return {"ids": len(ids), "unreturned": sum(1 for p in probs if "not returned" in p),
            "status_checked": checked, "status_wrong": sum(1 for p in probs if "status is recorded" in p)}


# ------------------------------------------------------------------ citation log for current experiment
cit = []
for row in cm_rows_all:
    r = raw_idx.get(row["run_id"], {})
    fin, pre = r.get("final"), r.get("final_precorrection") or r.get("final")
    he = fin.get("historical_effect") if isinstance(fin, dict) and isinstance(fin.get("historical_effect"), dict) else {}
    cd = str(he.get("changed_decision", "")).strip().lower()
    a_pre, a_post = citation_check(pre, r), citation_check(fin, r)
    first = next((c for c in r.get("tool_calls", []) if c["name"] == "retrieve_history"), None)
    cit.append({"run_id": row["run_id"], "model": row["model"], "task_id": row["task_id"],
                "condition": row["condition"], "seed": row["seed"],
                **{"pre_" + k: v for k, v in a_pre.items()}, **{"post_" + k: v for k, v in a_post.items()},
                "changed_decision": cd,
                "edges_traversed": sum((c.get("trace") or {}).get("edges_traversed", 0) for c in r.get("tool_calls", [])),
                "first_retrieval_chars": first["result_chars"] if first else None,
                "first_retrieval_ids": "; ".join(first.get("returned_ids", [])) if first else ""})
    row["claimed_changed_decision_num"] = float(cd == "yes") if cd else None
common.write_csv(os.path.join(OUT, "citations.csv"), cit, list(cit[0].keys()) if cit else None)
common.write_csv(os.path.join(OUT, "per_run.csv"), cm_rows_all,
                 sorted({k for r in cm_rows_all for k in r}, key=lambda k: (k not in ("model", "task_id", "condition", "seed"), k)))


def mean(rs, m):
    v = [r[m] for r in rs if r.get(m) is not None]
    return float(np.mean(v)) if v else None


def summarize(rs):
    valid = [r for r in rs if r.get("valid_output")]
    pts = [(r["p_testable"], r["testable_truth"]) for r in valid if r.get("p_testable") is not None]
    s = {"runs": len(rs), "valid": len(valid),
         "P1_balanced_flag_accuracy_task_level": stats.balanced_accuracy(
             [r["flagged"] for r in valid], [r["should_flag"] for r in valid]),
         "testability_auc": stats.auc([p for p, _ in pts], [t for _, t in pts]),
         **{m: mean(valid, m) for m in ("testability_brier", "outcome_log_loss", "risk_recall",
                                        "prior_work_recognized", "false_prior_claim", "prereg_quality")},
         "relevant_surfaced_rate": mean(rs, "relevant_surfaced_num"),
         "cites_relevant_seen_rate": mean(rs, "cites_relevant_seen_num"),
         "meaningfully_used_rate": mean(rs, "meaningfully_used_num"),
         "fabricated_citations_total": sum(r.get("n_fabricated_citations") or 0 for r in rs),
         "status_claims_checked": sum(r.get("status_claims_checked") or 0 for r in rs),
         "status_claims_correct": sum(r.get("status_claims_correct") or 0 for r in rs),
         "correction_turns_total": sum(r.get("correction_turns") or 0 for r in rs),
         "preliminary_answers_total": sum(r.get("preliminary_answers") or 0 for r in rs),
         "repair_turns_total": sum(r.get("repair_turns") or 0 for r in rs),
         "input_tokens_total": sum(r.get("input_tokens") or 0 for r in rs),
         "output_tokens_total": sum(r.get("output_tokens") or 0 for r in rs),
         "cost_usd_total": sum(r.get("cost_usd") or 0 for r in rs),
         "wall_seconds_mean": mean(rs, "wall_seconds"),
         "stop_reasons": {s: sum(1 for r in rs if r.get("stop_reason") == s) for s in sorted({str(r.get("stop_reason")) for r in rs})},
         "P1_balanced_accuracy_by_seed": {int(k): stats.balanced_accuracy([r["flagged"] for r in g if r.get("valid_output")],
                                                                          [r["should_flag"] for r in g if r.get("valid_output")])
                                          for k in sorted({r["seed"] for r in rs})
                                          for g in [[r for r in rs if r["seed"] == k]]}}
    cc = [x for x in cit if any(r["run_id"] == x["run_id"] for r in rs)]
    s.update({"changed_decision_claims": {v: sum(1 for x in cc if x["changed_decision"] == v)
                                          for v in sorted({x["changed_decision"] for x in cc})},
              "pre_unreturned_ids": sum(x["pre_unreturned"] for x in cc),
              "post_unreturned_ids": sum(x["post_unreturned"] for x in cc),
              "edges_traversed_mean": mean(cc, "edges_traversed"),
              "first_retrieval_chars_mean": mean(cc, "first_retrieval_chars")})
    return s


# per-model per-condition summary
summary = {}
for mn in model_names:
    model_rows = [r for r in cm_rows_all if r["model"] == mn]
    summary[MODEL_SHORT.get(mn, mn)] = {c: summarize([r for r in model_rows if r["condition"] == c]) for c in "ABC"}

# ------------------------------------------------------------------ contrasts within each model
contrasts = []
for mn in model_names:
    short = MODEL_SHORT.get(mn, mn)
    model_rows = [r for r in cm_rows_all if r["model"] == mn]
    for a_cond, b_cond in (("A", "B"), ("A", "C"), ("B", "C")):
        contrasts.append({"model": short, "family": "primary",
                          **stats.contrast(model_rows, "p1_weighted", a_cond, b_cond)})
    for a_cond, b_cond in (("A", "B"), ("A", "C"), ("B", "C")):
        for m, hib in (("testability_brier", False), ("outcome_log_loss", False),
                       ("risk_recall", True), ("prior_work_recognized", True), ("false_prior_claim", False)):
            contrasts.append({"model": short, "family": "secondary",
                               **stats.contrast(model_rows, m, a_cond, b_cond, higher_is_better=hib)})

# Holm within each model's primary contrasts
for mn in model_names:
    short = MODEL_SHORT.get(mn, mn)
    prim = [x for x in contrasts if x["model"] == short and x["family"] == "primary" and x.get("p_sign_flip") is not None]
    for x, adj in zip(prim, stats.holm([x["p_sign_flip"] for x in prim])):
        x["p_holm"] = adj


# ------------------------------------------------------------------ cross-model comparison (task-paired)
def _rows_for(model_id_or_short, all_rows):
    for rs in [all_rows]:
        m = [r for r in rs if r["model"] == model_id_or_short or MODEL_SHORT.get(r["model"]) == model_id_or_short]
        if m:
            return m
    return []


# gather per-model per-condition task means for the primary metric
tm = {}
for mn in model_names:
    short = MODEL_SHORT.get(mn, mn)
    model_rows = [r for r in cm_rows_all if r["model"] == mn]
    for c in "ABC":
        tm[(short, c)] = stats.task_means(model_rows, "p1_weighted", c)

if p3_rows:
    p3_short = MODEL_SHORT.get(p3_model, "gemini-2.5-flash")
    for c in "ABC":
        tm[(p3_short, c)] = stats.task_means(p3_rows, "p1_weighted", c)

cross = []
# memory effect B-A and C-A per model
all_shorts = ([p3_short] if p3_rows else []) + [MODEL_SHORT.get(mn, mn) for mn in model_names]
for short in all_shorts:
    for c in "BC":
        if (short, "A") in tm and (short, c) in tm:
            common_t = sorted(set(tm[(short, "A")]) & set(tm[(short, c)]))
            d = np.array([tm[(short, c)][t] - tm[(short, "A")][t] for t in common_t])
            cross.append({"family": f"memory effect {c}-A", "model": short, "metric": "p1_weighted",
                          "contrast": f"{c} - A", "n_tasks": len(d),
                          "mean_difference": float(d.mean()) if len(d) else None,
                          "ci95": stats.bootstrap_ci(d), "p_sign_flip": stats.sign_flip_p(d)})

# pairwise model comparison: same condition, same task
for short_a, short_b in itertools.combinations(all_shorts, 2):
    for c in "ABC":
        if (short_a, c) in tm and (short_b, c) in tm:
            common_t = sorted(set(tm[(short_a, c)]) & set(tm[(short_b, c)]))
            d = np.array([tm[(short_b, c)][t] - tm[(short_a, c)][t] for t in common_t])
            cross.append({"family": "cross-model comparison", "model": f"{short_b} vs {short_a}", "metric": "p1_weighted",
                          "contrast": f"cond={c}", "n_tasks": len(d),
                          "mean_difference": float(d.mean()) if len(d) else None,
                          "ci95": stats.bootstrap_ci(d), "p_sign_flip": stats.sign_flip_p(d)})

all_contrasts = contrasts + cross
common.write_csv(os.path.join(OUT, "contrasts.csv"),
                 [dict(x, ci95=json.dumps(x.get("ci95"))) for x in all_contrasts],
                 ["model", "family", "metric", "contrast", "n_tasks", "mean_difference", "ci95", "p_sign_flip", "p_holm"])

# ------------------------------------------------------------------ per-task table
per_task = []
for t in TASKS:
    k = keys[t]
    row = {"task_id": t, "stratum": k["stratum"], "should_flag": k["should_flag_before_running"]}
    for short in all_shorts:
        src = p3_rows if short == (p3_short if p3_rows else None) else cm_rows_all
        for c in "ABC":
            v = tm.get((short, c), {}).get(t)
            row[f"{short}_{c}_flag"] = round(v, 3) if v is not None else None
    per_task.append(row)
common.write_csv(os.path.join(OUT, "per_task.csv"), per_task, list(per_task[0].keys()))

# ------------------------------------------------------------------ write summary.json
p3_summary = {}
if p3_rows:
    for c in "ABC":
        p3_summary[c] = summarize([r for r in p3_rows if r["condition"] == c])
        p3_summary[c]["cit_data"] = "from pilot3_v1/analysis_p3"

res = {"experiment_id": cfg["experiment_id"], "mock": all(m["provider"] == "mock" for m in cfg["models"]),
       "n_tasks": len(TASKS), "seeds": SEEDS, "model_names": model_names,
       "summary_by_model_condition": summary,
       "pilot3_summary_by_condition": p3_summary,
       "within_model_contrasts": contrasts, "cross_model_analysis": cross,
       "earlier_pilot_files_modified": False}
json.dump(res, open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8"), indent=1, default=str)


# ------------------------------------------------------------------ report
def r3(v):
    return round(v, 3) if isinstance(v, float) else v


def fmt_ci(x):
    lo, hi = x.get("ci95", (None, None))
    return f"({r3(lo)}, {r3(hi)})"


lines = [
    "# Cross-model replication: gpt-oss-20b and Claude Haiku 5.5 versus Gemini 2.5 Flash",
    "",
    f"Experiment `{cfg['experiment_id']}`. "
    f"{'Mock run — no API calls.' if res['mock'] else f'Real API run via OpenRouter.'}",
    f"10 tasks, conditions A/B/C, seeds {SEEDS}. {len(model_names)} model(s) x 30 runs = {len(cm_rows_all)} runs.",
    "",
    "## Models",
    "",
]
for m in cfg["models"]:
    p = m.get("price_per_million", {})
    lines.append(f"- **{MODEL_SHORT.get(m['model'], m['model'])}** (`{m['model']}` via {m['provider']}, "
                 f"temperature {m.get('temperature', '?')}, max_tokens {m.get('max_tokens', '?')}, "
                 f"input ${p.get('input', '?')}/1M out ${p.get('output', '?')}/1M)")
lines += ["", "## Primary outcome: balanced flag accuracy (task level)", "", "Seeds averaged within task.", ""]
header = "| condition |" + "".join(f" {MODEL_SHORT.get(mn, mn)} |" for mn in model_names)
if p3_rows:
    header += f" {p3_short} (P3) |"
lines += [header, "|---|" + "---|" * (len(model_names) + (1 if p3_rows else 0))]
for c in "ABC":
    row_str = f"| {c} |"
    for mn in model_names:
        short = MODEL_SHORT.get(mn, mn)
        v = summary[short][c].get("P1_balanced_flag_accuracy_task_level")
        row_str += f" {r3(v)} |"
    if p3_rows:
        v = p3_summary[c].get("P1_balanced_flag_accuracy_task_level")
        row_str += f" {r3(v)} |"
    lines.append(row_str)
lines += ["", "### Primary contrasts (task-paired, 10 tasks, 95% CI from cluster bootstrap)", ""]
lines.append("| model | contrast | difference | 95% CI | sign-flip p | Holm p |")
lines.append("|---|---|---|---|---|---|")
for x in contrasts:
    if x["family"] == "primary":
        lines.append(f"| {x['model']} | {x['contrast']} | {r3(x['mean_difference'])} | {fmt_ci(x)} | {x['p_sign_flip']} | {r3(x.get('p_holm'))} |")
lines += ["", "## Secondary outcomes", ""]
lines.append("| model | condition | testability AUC | Brier | log loss | risk recall | prior_work_recog | false_prior | citations correct | cost USD |")
lines.append("|---|---|---|---|---|---|---|---|---|---|")
for mn in model_names:
    short = MODEL_SHORT.get(mn, mn)
    for c in "ABC":
        s = summary[short][c]
        chk = s.get("status_claims_checked") or 0
        cor = s.get("status_claims_correct") or 0
        acc = f"{cor}/{chk}" if chk else "n/a"
        lines.append(f"| {short} | {c} | {r3(s.get('testability_auc'))} | {r3(s.get('testability_brier'))} "
                     f"| {r3(s.get('outcome_log_loss'))} | {r3(s.get('risk_recall'))} "
                     f"| {r3(s.get('prior_work_recognized'))} | {r3(s.get('false_prior_claim'))} "
                     f"| {acc} | {r3(s.get('cost_usd_total'))} |")
lines += ["", "## Cross-model comparison (memory effect, task-paired)", ""]
lines.append("| models | condition | B-A difference | 95% CI | sign-flip p |")
lines.append("|---|---|---|---|---|")
for x in cross:
    if x["family"].startswith("memory effect"):
        lines.append(f"| {x['model']} | {x['contrast']} | {r3(x['mean_difference'])} | {fmt_ci(x)} | {x['p_sign_flip']} |")
lines += ["", "## Protocol compliance", ""]
lines.append("| model | condition | valid | prelim answers | gate turns | repairs | correction turns | fabricated citations |")
lines.append("|---|---|---|---|---|---|---|---|")
for mn in model_names:
    short = MODEL_SHORT.get(mn, mn)
    for c in "ABC":
        s = summary[short][c]
        lines.append(f"| {short} | {c} | {s['valid']}/{s['runs']} | {s['preliminary_answers_total']} "
                     f"| {s['repair_turns_total']} | {s['repair_turns_total']} | {s['correction_turns_total']} "
                     f"| {s['fabricated_citations_total']} |")
lines += ["", "## Cost", ""]
for mn in model_names:
    short = MODEL_SHORT.get(mn, mn)
    total = sum(summary[short][c]["cost_usd_total"] for c in "ABC")
    lines.append(f"- **{short}**: ${r3(total)} (A ${r3(summary[short]['A']['cost_usd_total'])}, "
                 f"B ${r3(summary[short]['B']['cost_usd_total'])}, C ${r3(summary[short]['C']['cost_usd_total'])})")
lines += ["", "## Limitations", "",
          "- Ten tasks. Three seeds reduce per-task noise but do not add tasks; intervals span roughly plus or minus 0.3.",
          "- The answer key is automated adjudication, unchanged from the Gemini pilots.",
          "- Pricing sourced from openrouter.ai/models on 2026-11-11; OpenRouter adds a small markup over provider list prices.",
          "- Temperature and max_tokens are sent identically to both models; identical numeric settings do not guarantee",
          "  identical sampling behaviour across different tokenizers and training regimes.",
          "- Seed reproducibility is not guaranteed across providers.",
          ""]
open(os.path.join(OUT, "cross_model_report.md"), "w", encoding="utf-8").write("\n".join(lines))
print(f"report: {os.path.join(OUT, 'cross_model_report.md')}")
print()
for short in all_shorts:
    src = p3_rows if (p3_rows and short == p3_short) else cm_rows_all
    for c in "ABC":
        rows_c = [r for r in src if r["condition"] == c and (MODEL_SHORT.get(r.get("model"), r.get("model")) == short or r.get("model") == short)]
        if not rows_c:
            continue
        valid = [r for r in rows_c if r.get("valid_output")]
        ba = stats.balanced_accuracy([r["flagged"] for r in valid], [r["should_flag"] for r in valid])
        print(f"{short:25s} {c}  BA={r3(ba)}  n={len(rows_c)}  valid={len(valid)}")
print()
for x in contrasts:
    if x["family"] == "primary":
        print(f"  {x['model']:25s} {x['contrast']:8s} d={r3(x['mean_difference'])} ci={fmt_ci(x)} p={x['p_sign_flip']} holm={r3(x.get('p_holm'))}")
