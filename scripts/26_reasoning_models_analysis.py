"""Analysis for reasoning_models_v1: Claude Sonnet 5.5 + DeepSeek V4 Pro with extended thinking.

Reads:  runs/reasoning_models_v1/scores.csv
        runs/pilot3_v1/scores.csv          (Gemini 2.5 Flash reference)
        runs/cross_model_v1/scores.csv     (Haiku 5.5 + gpt-oss reference)
Writes: runs/reasoning_models_v1/analysis_rm/
          per_run.csv, per_task.csv, contrasts.csv, citations.csv, summary.json,
          reasoning_models_report.md

No API calls.
"""
import csv
import json
import os
import sys

import numpy as np

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import common, scoring
from runner import experiment

OUTDIR = os.path.join(HB, "runs", "reasoning_models_v1", "analysis_rm")
os.makedirs(OUTDIR, exist_ok=True)

TASKS = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]
CONDS = ["A", "B", "C"]
SEEDS = [1, 2, 3]

MODEL_LABELS = {
    "openrouter.ai:anthropic/claude-sonnet-5.5": "Sonnet5.5",
    "openrouter.ai:deepseek/deepseek-v4-pro":    "DeepSeek-V4",
    # versioned names that may appear in model_version field
}

REF_LABELS = {
    "gemini:gemini-2.5-flash":                         "Gemini (P3 ref)",
    "openrouter.ai:anthropic/claude-haiku-5.5":         "Haiku (CM ref)",
    "openrouter.ai:openai/gpt-oss-20b":                 "gpt-oss (CM ref)",
}


def _num(v):
    if v in (None, "", "None"): return None
    if v in ("True", "False"): return float(v == "True")
    try: return float(v)
    except: return v


def read_scores(path):
    rows = []
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows.append({k: _num(v) for k, v in r.items()})
    return rows


def ba_for(rows):
    """Balanced accuracy across a list of rows (each must have flag_correct and valid_output)."""
    valid = [r for r in rows if r.get("valid_output", 1)]
    if not valid: return None
    flag = [r for r in valid if r.get("should_flag_before_running")]
    noflag = [r for r in valid if not r.get("should_flag_before_running")]
    sens = np.mean([r["flag_correct"] for r in flag]) if flag else None
    spec = np.mean([r["flag_correct"] for r in noflag]) if noflag else None
    if sens is None or spec is None: return None
    return (sens + spec) / 2


def bootstrap_ba(rows, n=2000, rng=None):
    rng = rng or np.random.default_rng(42)
    valid = [r for r in rows if r.get("valid_output", 1)]
    if not valid: return (None, None)
    xs = np.array([r["flag_correct"] for r in valid])
    should = np.array([float(bool(r["should_flag_before_running"])) for r in valid])
    boots = []
    for _ in range(n):
        idx = rng.integers(0, len(xs), len(xs))
        s_idx = idx[should[idx] == 1]; ns_idx = idx[should[idx] == 0]
        if not len(s_idx) or not len(ns_idx): continue
        boots.append((xs[s_idx].mean() + xs[ns_idx].mean()) / 2)
    if not boots: return (None, None)
    return (float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5)))


def task_flag_acc(rows, task):
    """Mean flag accuracy for one task. A task is entirely should-flag or not, so balanced accuracy is not defined within a task."""
    task_rows = [r for r in rows if r.get("task_id") == task and r.get("valid_output", 1) and r.get("flag_correct") is not None]
    if not task_rows:
        return None, None, None
    vals = [r["flag_correct"] for r in task_rows]
    return float(np.mean(vals)), float(np.min(vals)), float(np.max(vals))


def contrasts(rm_rows, ref_rows_list, ref_labels, model_col):
    """B-A and C-A contrasts with bootstrap CIs for each (model, condition_pair)."""
    out = []
    for m_key, m_label in {**MODEL_LABELS}.items():
        m_rows = [r for r in rm_rows if r.get("model_name") == m_key]
        if not m_rows: continue
        for c_pair in [("B", "A"), ("C", "A"), ("C", "B")]:
            cA = [r for r in m_rows if r.get("condition") == c_pair[0]]
            cB = [r for r in m_rows if r.get("condition") == c_pair[1]]
            baA = ba_for(cA); baB = ba_for(cB)
            diff = (baA - baB) if (baA and baB) else None
            ciA = bootstrap_ba(cA); ciB = bootstrap_ba(cB)
            out.append({"model": m_label, "comparison": f"{c_pair[0]}-{c_pair[1]}",
                        "ba_treatment": round(baA, 4) if baA else None,
                        "ba_control": round(baB, 4) if baB else None,
                        "diff": round(diff, 4) if diff else None,
                        "ci95_lo_treatment": round(ciA[0], 4) if ciA[0] else None,
                        "ci95_hi_treatment": round(ciA[1], 4) if ciA[1] else None})
    return out


def reasoning_stats(rm_rows, model_key):
    """Summary of reasoning/thinking token usage for a model."""
    import glob
    raw_dir = os.path.join(HB, "runs", "reasoning_models_v1", "raw")
    if not os.path.exists(raw_dir): return {}
    runs = []
    for p in glob.glob(os.path.join(raw_dir, "*.json")):
        r = json.load(open(p, encoding="utf-8"))
        if r.get("model_name") == model_key:
            runs.append(r)
    if not runs: return {}
    repair_total = sum(r.get("repair_turns", 0) or 0 for r in runs)
    valid_total = sum(1 for r in runs if r.get("stop_reason") == "final")
    # Check for reasoning_details in messages
    with_reasoning = sum(
        1 for r in runs
        if any(m.get("reasoning_details") for m in r.get("messages", []))
    )
    return {"n_runs": len(runs), "repair_turns": repair_total,
            "valid_outputs": valid_total, "valid_pct": round(100 * valid_total / max(1, len(runs)), 1),
            "runs_with_reasoning_details": with_reasoning}


# ─── Load data ────────────────────────────────────────────────────────────────
rm_path = os.path.join(HB, "runs", "reasoning_models_v1", "scores.csv")
if not os.path.exists(rm_path):
    print(f"ERROR: {rm_path} not found — run the experiment first.")
    sys.exit(1)

rm_rows = read_scores(rm_path)
p3_rows = read_scores(os.path.join(HB, "runs", "pilot3_v1", "scores.csv"))
cm_rows = read_scores(os.path.join(HB, "runs", "cross_model_v1", "scores.csv"))
for rows in (rm_rows, p3_rows, cm_rows):
    for r in rows:
        r.setdefault("model_name", r.get("model"))
        r.setdefault("should_flag_before_running", r.get("should_flag"))
all_ref = p3_rows + cm_rows

print(f"Loaded reasoning_models_v1: {len(rm_rows)} rows")
print(f"Loaded pilot3 reference:     {len(p3_rows)} rows")
print(f"Loaded cross_model reference:{len(cm_rows)} rows")

# ─── Per-run CSV ──────────────────────────────────────────────────────────────
per_run_path = os.path.join(OUTDIR, "per_run.csv")
with open(per_run_path, "w", newline="", encoding="utf-8") as f:
    fields = list(rm_rows[0].keys()) if rm_rows else []
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader(); w.writerows(rm_rows)

# ─── Per-task CSV ─────────────────────────────────────────────────────────────
per_task_rows = []
for m_key, m_label in MODEL_LABELS.items():
    m_rows = [r for r in rm_rows if r.get("model_name") == m_key]
    if not m_rows: continue
    for cond in CONDS:
        c_rows = [r for r in m_rows if r.get("condition") == cond]
        for task in TASKS:
            t_rows = [r for r in c_rows if r.get("task_id") == task]
            acc, acc_lo, acc_hi = task_flag_acc(c_rows, task)
            valid_ct = sum(1 for r in t_rows if r.get("valid_output", 1))
            per_task_rows.append({
                "model": m_label, "task_id": task, "condition": cond,
                "flag_acc": round(acc, 4) if acc is not None else None,
                "flag_acc_lo": round(acc_lo, 4) if acc_lo is not None else None,
                "flag_acc_hi": round(acc_hi, 4) if acc_hi is not None else None,
                "n_valid": valid_ct, "n_total": len(t_rows),
            })

with open(os.path.join(OUTDIR, "per_task.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["model","task_id","condition","flag_acc","flag_acc_lo","flag_acc_hi","n_valid","n_total"])
    w.writeheader(); w.writerows(per_task_rows)

# ─── Contrasts CSV ────────────────────────────────────────────────────────────
contrast_rows = contrasts(rm_rows, all_ref, REF_LABELS, "model_name")
with open(os.path.join(OUTDIR, "contrasts.csv"), "w", newline="", encoding="utf-8") as f:
    if contrast_rows:
        w = csv.DictWriter(f, fieldnames=list(contrast_rows[0].keys()))
        w.writeheader(); w.writerows(contrast_rows)

# ─── Citations CSV ────────────────────────────────────────────────────────────
with open(os.path.join(OUTDIR, "citations.csv"), "w", newline="", encoding="utf-8") as f:
    fields = ["run_id", "model", "task_id", "condition", "seed", "n_fabricated_citations",
              "representation_accuracy", "status_claims_checked", "status_claims_correct"]
    fields = [k for k in fields if k in (rm_rows[0] if rm_rows else {})]
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows({k: r.get(k) for k in fields} for r in rm_rows)

# ─── Per-model summary ────────────────────────────────────────────────────────
def model_summary(rows, m_key, m_label):
    m = [r for r in rows if r.get("model_name") == m_key]
    if not m: return None
    out = {"model": m_label, "n_runs": len(m)}
    for c in CONDS:
        cr = [r for r in m if r.get("condition") == c]
        ci = bootstrap_ba(cr)
        out[f"ba_{c}"] = round(ba_for(cr), 4) if ba_for(cr) else None
        out[f"ba_{c}_ci95"] = [round(ci[0], 4), round(ci[1], 4)] if ci[0] else None
    out["valid_pct"] = round(100 * sum(1 for r in m if r.get("valid_output", 1)) / len(m), 1)
    out["repair_turns_total"] = int(sum(r.get("repair_turns", 0) or 0 for r in m))
    out["risk_recall"] = round(float(np.mean([r["risk_recall"] for r in m if r.get("risk_recall") is not None])), 3) if any(r.get("risk_recall") is not None for r in m) else None
    rep = [r["representation_accuracy"] for r in m if isinstance(r.get("representation_accuracy"), float)]
    out["representation_accuracy"] = round(float(np.mean(rep)), 3) if rep else None
    out["fabricated_citations"] = int(sum(r.get("n_fabricated_citations") or 0 for r in m))
    out["cost_usd"] = round(float(sum(r.get("cost_usd") or 0 for r in m)), 3)
    rs = reasoning_stats(rows, m_key)
    out["reasoning_details_observed"] = rs.get("runs_with_reasoning_details", 0)
    return out

summary = {
    "experiment_id": "reasoning_models_v1",
    "models": [ms for ms in [model_summary(rm_rows, k, l) for k, l in MODEL_LABELS.items()] if ms],
    "reference_models": {
        REF_LABELS[k]: {
            "ba_A": (lambda v: round(v, 4) if v is not None else None)(ba_for([r for r in (p3_rows if "gemini" in k else cm_rows) if r.get("model_name")==k and r.get("condition")=="A"])),
            "ba_B": (lambda v: round(v, 4) if v is not None else None)(ba_for([r for r in (p3_rows if "gemini" in k else cm_rows) if r.get("model_name")==k and r.get("condition")=="B"])),
            "ba_C": (lambda v: round(v, 4) if v is not None else None)(ba_for([r for r in (p3_rows if "gemini" in k else cm_rows) if r.get("model_name")==k and r.get("condition")=="C"])),
        }
        for k, l in REF_LABELS.items()
    },
    "contrasts": contrast_rows,
}
with open(os.path.join(OUTDIR, "summary.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=1, ensure_ascii=False)

print("\nPer-model summary:")
for ms in summary["models"]:
    print(f"  {ms['model']}: A={ms['ba_A']} B={ms['ba_B']} C={ms['ba_C']} "
          f"valid={ms['valid_pct']}% repairs={ms['repair_turns_total']} "
          f"reasoning_observed={ms['reasoning_details_observed']}")

print("\nReference models:")
for lbl, vals in summary["reference_models"].items():
    print(f"  {lbl}: A={vals['ba_A']} B={vals['ba_B']} C={vals['ba_C']}")

# ─── Report ───────────────────────────────────────────────────────────────────
cfg = experiment.load_config(os.path.join(HB, "configs", "reasoning_models_v1.json"))

def _ba_row(label, ba_a, ba_b, ba_c, ba_b_ci=None, ba_c_ci=None):
    def ci(v): return f" [{v[0]:.3f}, {v[1]:.3f}]" if v and v[0] else ""
    return (f"| {label} | {ba_a:.3f} | {ba_b:.3f}{ci(ba_b_ci)} | "
            f"{ba_c:.3f}{ci(ba_c_ci)} | {(ba_b - ba_a):+.3f} | {(ba_c - ba_a):+.3f} |")

report_lines = [
    "# Reasoning Models Experiment Report",
    "",
    f"**Experiment ID:** reasoning_models_v1  ",
    f"**Protocol:** 3  ",
    f"**Models:** Claude Sonnet 5.5 (extended thinking), DeepSeek V4 Pro (reasoning)  ",
    f"**Tasks:** {len(cfg['tasks'])} (same as pilot3_v1 and cross_model_v1)  ",
    f"**Conditions:** A (no memory), B (document search), C (graph traversal)  ",
    f"**Seeds per condition:** 3  ",
    f"**Total runs:** {len(rm_rows)}  ",
    "",
    "---",
    "",
    "## 1. Primary Results: Balanced Accuracy by Model and Condition",
    "",
    "| Model | A (no memory) | B (doc search) | C (graph) | B−A | C−A |",
    "|-------|--------------|----------------|-----------|-----|-----|",
]

for ms in summary["models"]:
    ba_a = ms["ba_A"] or 0; ba_b = ms["ba_B"] or 0; ba_c = ms["ba_C"] or 0
    ci_b = next((c["ci95_lo_treatment"] for c in contrast_rows
                 if c["model"] == ms["model"] and c["comparison"] == "B-A"), None)
    ci_b_hi = next((c["ci95_hi_treatment"] for c in contrast_rows
                    if c["model"] == ms["model"] and c["comparison"] == "B-A"), None)
    ci_c = next((c["ci95_lo_treatment"] for c in contrast_rows
                 if c["model"] == ms["model"] and c["comparison"] == "C-A"), None)
    ci_c_hi = next((c["ci95_hi_treatment"] for c in contrast_rows
                    if c["model"] == ms["model"] and c["comparison"] == "C-A"), None)
    report_lines.append(
        f"| {ms['model']} | {ba_a:.3f} | {ba_b:.3f} | {ba_c:.3f} | {ba_b - ba_a:+.3f} | {ba_c - ba_a:+.3f} |"
    )

report_lines += [
    "",
    "**Reference models (from prior experiments):**",
    "",
    "| Model | A | B | C |",
    "|-------|---|---|---|",
]
for lbl, vals in summary["reference_models"].items():
    ba_a = vals["ba_A"] or 0; ba_b = vals["ba_B"] or 0; ba_c = vals["ba_C"] or 0
    report_lines.append(f"| {lbl} | {ba_a:.3f} | {ba_b:.3f} | {ba_c:.3f} |")

report_lines += [
    "",
    "*BA = balanced accuracy (equal weight to flag and no-flag tasks). "
    "Bootstrap 95% CIs not shown for reference models. "
    "10-task pilot; typical CI half-width ≈ ±0.3.*",
    "",
    "---",
    "",
    "## 2. Protocol Compliance",
    "",
    "| Model | Runs | Valid outputs | Repair turns | reasoning_details observed |",
    "|-------|------|--------------|--------------|---------------------------|",
]
for ms in summary["models"]:
    report_lines.append(
        f"| {ms['model']} | {ms['n_runs']} | "
        f"{ms['valid_pct']}% | {ms['repair_turns_total']} | {ms['reasoning_details_observed']} |"
    )

report_lines += [
    "",
    "---",
    "",
    "## 3. Risk Identification",
    "",
    "| Model | Risk recall | Representation accuracy | Fabricated citations | Cost |",
    "|-------|------------|--------------------------|----------------------|------|",
]
for ms in summary["models"]:
    rr = f"{ms['risk_recall']:.3f}" if ms["risk_recall"] is not None else "—"
    ca = f"{ms['representation_accuracy']:.3f}" if ms["representation_accuracy"] is not None else "—"
    report_lines.append(
        f"| {ms['model']} | {rr} | {ca} | {ms['fabricated_citations']} | ${ms['cost_usd']:.2f} |"
    )

report_lines += [
    "",
    "---",
    "",
    "## 4. Contrasts (B−A, C−A)",
    "",
    "| Model | Comparison | BA (treatment) | BA (control) | Difference |",
    "|-------|-----------|----------------|--------------|------------|",
]
for c in contrast_rows:
    bt = f"{c['ba_treatment']:.3f}" if c["ba_treatment"] else "—"
    bc = f"{c['ba_control']:.3f}" if c["ba_control"] else "—"
    d = f"{c['diff']:+.3f}" if c["diff"] else "—"
    report_lines.append(f"| {c['model']} | {c['comparison']} | {bt} | {bc} | {d} |")

report_lines += [
    "",
    "---",
    "",
    "## 5. Notes on Reasoning Models",
    "",
    "Both models used extended thinking (reasoning) via OpenRouter with provider pinning:",
    "- Claude Sonnet 5.5 → Anthropic backend (temperature=1.0 required)",
    "- DeepSeek V4 Pro → streamlake/fp8 backend (temperature=1.0)",
    "",
    "The harness was extended to preserve `reasoning_details` in multi-turn conversations",
    "(runner/llm.py + runner/agent.py). This ensures each turn can continue reasoning",
    "from where the prior turn left off, per the OpenRouter multi-turn reasoning protocol.",
    "",
    "Because reasoning models use extended thinking rather than response_format JSON mode,",
    "the system prompt's JSON instruction is the sole schema enforcement mechanism. Repair",
    "turns handle any cases where the model wraps output in markdown code blocks.",
    "",
    "---",
    "",
    "*Generated by scripts/26_reasoning_models_analysis.py from existing run outputs.*",
    "*No API calls made by this script.*",
]

report_path = os.path.join(HB, "runs", "reasoning_models_v1", "reasoning_models_report.md")
os.makedirs(os.path.dirname(report_path), exist_ok=True)
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"\nWrote: {report_path}")
print(f"Wrote: {OUTDIR}/per_run.csv, per_task.csv, contrasts.csv, citations.csv, summary.json")
