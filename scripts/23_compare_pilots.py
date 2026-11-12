r"""Compare Pilot 2 (required retrieval, protocol 2) with Pilot 1 without pooling them. Pilot 1 files are only read.

Pilot 1 comparator: the Pilot 1 raw runs, with the final output of runs that ended 'unparseable' recovered from their
last reply by the Pilot 2 lenient parser (the same outputs as the Pilot 1 'recovered' sensitivity analysis). Both
pilots are scored here with the same answer key, the same scoring code and the same retrieval audit.

Effects separated (task-paired; 10 tasks; bootstrap intervals and exact sign-flip tests; no pooling across pilots):
  availability          Pilot 1: B - A, C - A (memory available, use optional)
  retrieved information Pilot 2: B - A, C - A (same required procedure in every condition; only content differs)
  required retrieval    Pilot 2 - Pilot 1 within each condition; A2 - A1 is the effect of the procedure, parser and
                        gate with no memory content; (X2 - A2) - (X1 - A1) is the change in the memory effect

Usage: python scripts\23_compare_pilots.py
Writes runs\pilot2_v1\comparison\ (per_run.csv, per_task.csv, contrasts.csv, summary.json).
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bench import common, retrieval_audit, scoring, stats  # noqa: E402
from runner import agent, experiment  # noqa: E402

HB = common.HB
cfg1 = experiment.load_config(os.path.join(HB, "configs", "pilot.json"))
cfg2 = experiment.load_config(os.path.join(HB, "configs", "pilot2.json"))
OUT = os.path.join(cfg2["_out"], "comparison")
os.makedirs(OUT, exist_ok=True)
keys = experiment.answer_key()
ctx = retrieval_audit.Context()
TAG = {cfg1["experiment_id"]: "P1", cfg2["experiment_id"]: "P2"}


def recovered_final(run):
    if isinstance(run.get("final"), dict):
        return run["final"], ""
    for l in reversed(run.get("log", [])):
        act, _, note = agent.parse_action_lenient(l.get("reply", ""))
        if act and act["action"] == "final":
            return act["output"], note or "recovered"
    return None, "not recoverable"


def rows_for(cfg):
    rs = []
    for r in experiment.raw_runs(cfg):
        final, note = recovered_final(r)
        task, k = experiment.load_task(r["task_id"]), keys[r["task_id"]]
        usage = r.get("usage") or {}
        u = {"input_tokens": usage.get("input_tokens", 0), "output_tokens": usage.get("output_tokens", 0),
             "cost_usd": usage.get("cost_usd"), "n_tool_calls": r.get("n_tool_calls", 0),
             "memory_tool_calls": r.get("memory_tool_calls", 0), "wall_seconds": r.get("wall_seconds"),
             "stop_reason": r.get("stop_reason"), "error": r.get("error", "")}
        row = {"pilot": TAG[cfg["experiment_id"]], "run_id": r["run_id"], "task_id": r["task_id"], "condition": r["condition"]}
        row.update(scoring.score_replay(final, k, r["condition"], u))
        snap, _ = experiment.ensure_snapshot(task)
        row.update(retrieval_audit.audit(dict(r, final=final), task, k, snap, ctx, cfg["models"][0]["price_per_million"]["input"]))
        row.update({"recovery": note, "turns": r.get("turns", len(r.get("log", []))),
                    "repair_turns": sum(1 for l in r.get("log", []) if l.get("parse_error")),
                    "gate_turns": r.get("gate_turns", 0), "model_versions": "; ".join(r.get("model_versions", [])),
                    "stratum": k["stratum"]})
        rs.append(row)
    w = experiment._p1_weights(rs)
    for x in rs:
        x["p1_weighted"] = x["flag_correct"] * w[x["task_id"]] if x.get("flag_correct") is not None else None
        for m in ("relevant_surfaced", "cites_relevant_seen", "retrieval_successful", "meaningfully_used"):
            x[m + "_num"] = float(bool(x.get(m)))
        x["any_fabrication_num"] = float((x.get("n_fabricated_citations") or 0) > 0)
    return rs


rows = rows_for(cfg1) + rows_for(cfg2)
common.write_csv(os.path.join(OUT, "per_run.csv"), rows, sorted({k for r in rows for k in r}, key=lambda k: (k not in ("pilot", "task_id", "condition"), k)))


def summarize(rs):
    valid = [r for r in rs if r.get("valid_output")]
    mean = lambda m, pool=rs: float(np.mean([r[m] for r in pool if r.get(m) is not None])) if any(r.get(m) is not None for r in pool) else None  # noqa: E731
    chk = sum(r.get("status_claims_checked") or 0 for r in rs)
    pts = [(r["p_testable"], r["testable_truth"]) for r in valid if r.get("p_testable") is not None]
    return {
        "runs": len(rs), "completed_valid": len(valid), "ended_final": sum(1 for r in rs if r["stop_reason"] in ("final", "final_without_retrieval")),
        "recovered_by_parser": sum(1 for r in rs if r["recovery"] and r["stop_reason"] == "unparseable"),
        "P1_balanced_flag_accuracy": stats.balanced_accuracy([r["flagged"] for r in valid], [r["should_flag"] for r in valid]),
        "testability_auc": stats.auc([p for p, _ in pts], [t for _, t in pts]),
        "outcome_log_loss": mean("outcome_log_loss", valid), "risk_recall": mean("risk_recall", valid),
        "false_prior_claim": mean("false_prior_claim", valid), "prior_work_recognized": mean("prior_work_recognized", valid),
        "memory_tool_calls_mean": mean("memory_tool_calls"),
        "relevant_available_tasks": sum(1 for r in rs if r.get("relevant_available")),
        "relevant_surfaced_rate": mean("relevant_surfaced_num"), "cites_relevant_seen_rate": mean("cites_relevant_seen_num"),
        "retrieval_attempted_rate": mean("retrieval_attempted"), "retrieval_successful_rate": mean("retrieval_successful_num"),
        "meaningfully_used_rate": mean("meaningfully_used_num"),
        "fabricated_citations_total": sum(r.get("n_fabricated_citations") or 0 for r in rs),
        "runs_with_fabrication": sum(1 for r in rs if (r.get("n_fabricated_citations") or 0) > 0),
        "status_claims_checked": chk,
        "status_claims_correct": sum(r.get("status_claims_correct") or 0 for r in rs),
        **{k: sum(r.get(k) or 0 for r in rs) for k in ("status_shown_checked", "status_shown_correct", "status_inferred_checked", "status_inferred_correct")},
        "repair_turns_total": sum(r["repair_turns"] for r in rs), "gate_turns_total": sum(r.get("gate_turns") or 0 for r in rs),
        "input_tokens_total": sum(r.get("input_tokens") or 0 for r in rs), "output_tokens_total": sum(r.get("output_tokens") or 0 for r in rs),
        "memory_tokens_carried_mean": mean("memory_tokens_carried_est"),
        "cost_usd_total": sum(r.get("cost_usd") or 0 for r in rs),
        "stop_reasons": {s: sum(1 for r in rs if r["stop_reason"] == s) for s in sorted({r["stop_reason"] for r in rs})},
    }


summary = {p: {c: summarize([r for r in rows if r["pilot"] == p and r["condition"] == c]) for c in "ABC"} for p in ("P1", "P2")}


def label(rs, fn):
    return [dict(r, condition=fn(r)) for r in rs]


contrasts = []
for p in ("P1", "P2"):
    sub = [r for r in rows if r["pilot"] == p]
    for a, b in (("A", "B"), ("A", "C"), ("B", "C")):
        for m in ("p1_weighted", "cites_relevant_seen_num", "any_fabrication_num"):
            contrasts.append({"family": f"within {p}", **stats.contrast(sub, m, a, b)})
for c in "ABC":
    sub = label([r for r in rows if r["condition"] == c], lambda r: r["pilot"])
    for m in ("p1_weighted", "relevant_surfaced_num", "cites_relevant_seen_num", "any_fabrication_num"):
        contrasts.append({"family": f"across pilots, condition {c}", **stats.contrast(sub, m, "P1", "P2")})
for c in "BC":
    for m in ("p1_weighted", "cites_relevant_seen_num"):
        sub1 = [r for r in rows if r["pilot"] == "P1"]
        sub2 = [r for r in rows if r["pilot"] == "P2"]
        t1, d1 = stats.paired(sub1, m, "A", c)
        t2, d2 = stats.paired(sub2, m, "A", c)
        common_t = sorted(set(t1) & set(t2))
        d = np.array([d2[list(t2).index(t)] - d1[list(t1).index(t)] for t in common_t])
        contrasts.append({"family": "difference in differences", "metric": m, "contrast": f"({c}2 - A2) - ({c}1 - A1)",
                          "n_tasks": len(d), "mean_difference": float(d.mean()) if len(d) else None,
                          "ci95": stats.bootstrap_ci(d), "p_sign_flip": stats.sign_flip_p(d)})
p_primary = [x for x in contrasts if x["family"] == "within P2" and x["metric"] == "p1_weighted" and x["p_sign_flip"] is not None]
for x, adj in zip(p_primary, stats.holm([x["p_sign_flip"] for x in p_primary])):
    x["p_holm"] = adj
_, dbc = stats.paired([r for r in rows if r["pilot"] == "P2"], "p1_weighted", "B", "C")
equiv = stats.tost(dbc, cfg2.get("equivalence_margin", 0.10))
common.write_csv(os.path.join(OUT, "contrasts.csv"), [dict(x, ci95=json.dumps(x.get("ci95"))) for x in contrasts],
                 ["family", "metric", "contrast", "n_tasks", "mean_difference", "ci95", "p_sign_flip", "p_holm"])

per_task = []
for t in cfg2["tasks"]:
    k = keys[t]
    row = {"task_id": t, "stratum": k["stratum"], "should_flag": k["should_flag_before_running"], "expected_risk_codes": k["expected_risk_codes"]}
    for r in rows:
        if r["task_id"] == t:
            tag = f"{r['pilot']}{r['condition']}"
            row[f"{tag}_flag_correct"] = r.get("flag_correct")
            row[f"{tag}_decision"] = r.get("decision")
            row[f"{tag}_surfaced"] = int(bool(r.get("relevant_surfaced")))
            row[f"{tag}_cites_relevant"] = int(bool(r.get("cites_relevant_seen")))
            row["relevant_in_memory"] = r.get("relevant_families_in_memory")
    per_task.append(row)
common.write_csv(os.path.join(OUT, "per_task.csv"), per_task, list(per_task[0].keys()) + sorted({k for r in per_task for k in r} - set(per_task[0])))

# Pilot 2 within-run effect: answers the agent drafted before retrieval (rejected by the gate) versus its final answer.
# In A the change reflects re-answering with no content; in B and C it also reflects the retrieved content.
drafts = []
for r in experiment.raw_runs(cfg2):
    pre = next((l for l in r.get("log", []) if l.get("gate")), None)
    if not pre:
        continue
    act, _, _ = agent.parse_action_lenient(pre["reply"])
    if not act or act["action"] != "final":
        continue
    k = keys[r["task_id"]]
    sd = scoring.score_replay(act["output"], k, r["condition"], {})
    sf = scoring.score_replay(r.get("final"), k, r["condition"], {}) if isinstance(r.get("final"), dict) else {}
    drafts.append({"task_id": r["task_id"], "condition": r["condition"], "draft_flagged": sd.get("flagged"), "final_flagged": sf.get("flagged"),
                   "draft_correct": sd.get("flag_correct"), "final_correct": sf.get("flag_correct"),
                   "draft_decision": sd.get("decision"), "final_decision": sf.get("decision"),
                   "draft_p_testable": sd.get("p_testable"), "final_p_testable": sf.get("p_testable"),
                   "draft_log_loss": sd.get("outcome_log_loss"), "final_log_loss": sf.get("outcome_log_loss")})
if drafts:
    common.write_csv(os.path.join(OUT, "draft_vs_final.csv"), drafts, list(drafts[0].keys()))
draft_summary = {}
for c in "ABC":
    d = [x for x in drafts if x["condition"] == c and x["draft_correct"] is not None and x["final_correct"] is not None]
    draft_summary[c] = {"runs_with_draft": len(d), "flag_changed": sum(1 for x in d if x["draft_flagged"] != x["final_flagged"]),
                        "decision_changed": sum(1 for x in d if x["draft_decision"] != x["final_decision"]),
                        "wrong_to_right": sum(1 for x in d if x["draft_correct"] == 0 and x["final_correct"] == 1),
                        "right_to_wrong": sum(1 for x in d if x["draft_correct"] == 1 and x["final_correct"] == 0),
                        "mean_abs_p_testable_change": float(np.mean([abs(x["final_p_testable"] - x["draft_p_testable"]) for x in d
                                                                     if x["final_p_testable"] is not None and x["draft_p_testable"] is not None])) if d else None}

# association between citing relevant evidence and a correct flag, Pilot 2 memory conditions (descriptive only)
assoc = {}
for p in ("P1", "P2"):
    mem = [r for r in rows if r["pilot"] == p and r["condition"] in "BC" and r.get("flag_correct") is not None]
    for used in (True, False):
        g = [r["flag_correct"] for r in mem if bool(r.get("cites_relevant_seen")) == used]
        assoc[f"{p} B/C runs {'citing' if used else 'not citing'} relevant retrieved evidence"] = {"runs": len(g), "flag_correct_rate": float(np.mean(g)) if g else None}
json.dump({"summary": summary, "contrasts": contrasts, "C_vs_B_equivalence_P2": equiv, "use_vs_correct": assoc, "draft_vs_final": draft_summary,
           "pilot1_files_modified": False}, open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8"), indent=1, default=str)

for p in ("P1", "P2"):
    print(p)
    for c in "ABC":
        s = summary[p][c]
        print(f"  {c}", {k: (round(v, 3) if isinstance(v, float) else v) for k, v in s.items()})
print("contrasts")
for x in contrasts:
    print(f"  {x['family']:32s} {x['metric']:26s} {x['contrast']:22s} n={x['n_tasks']} d={x['mean_difference'] if x['mean_difference'] is None else round(x['mean_difference'], 3)} "
          f"ci={tuple(round(v, 3) if v is not None else None for v in x['ci95'])} p={x['p_sign_flip']} holm={x.get('p_holm')}")
print("C vs B equivalence (P2)", equiv)
print("use vs correct", assoc)
print("draft vs final", draft_summary)
