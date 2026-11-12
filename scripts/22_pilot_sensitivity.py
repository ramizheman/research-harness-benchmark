r"""Post-hoc sensitivity analyses for a finished experiment (not part of the pre-specified analysis).

  python scripts\22_pilot_sensitivity.py configs\pilot.json

1. recovered: for runs that ended 'unparseable', take the last reply that is a complete output object, either bare
   (all of testability, decision and predicted_outcome at top level) or wrapped as action 'final' after appending
   at most three missing closing braces. Scored with the unchanged scoring rules.
2. itt (intention to treat): unparseable runs count as an incorrect flag decision on P1.
Writes runs\<experiment>\sensitivity_recovered\ and sensitivity_itt\ plus per_task.csv; the primary scores.csv,
analysis.json and report.md are not touched.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bench import clusters, common, memory_v2, scoring  # noqa: E402
from runner import experiment  # noqa: E402

KEYS_REQUIRED = ("testability", "decision", "predicted_outcome")


def recover(run):
    for l in reversed(run["log"]):
        t = l["reply"].strip()
        for extra in range(4):
            try:
                o = json.loads(t + "}" * extra)
            except ValueError:
                continue
            if isinstance(o, dict) and o.get("action") == "final" and isinstance(o.get("output"), dict):
                return o["output"], f"wrapped final, {extra} closing brace(s) appended"
            if isinstance(o, dict) and all(k in o for k in KEYS_REQUIRED):
                return o, f"bare output object, {extra} closing brace(s) appended"
            break
    return None, "nothing recoverable"


def rows_for(cfg, runs, finals):
    keys = experiment.answer_key()
    records = {r["id"]: r for r in common.load_records()}
    repeat_sim = memory_v2.full_history_thresholds()[1]
    vec, _ = clusters.vectorizer(clusters.record_texts(list(records.values())))
    rows = []
    for r in runs:
        k, task = keys[r["task_id"]], experiment.load_task(r["task_id"])
        u = r.get("usage") or {}
        usage = {"input_tokens": u.get("input_tokens", 0), "output_tokens": u.get("output_tokens", 0), "cost_usd": u.get("cost_usd"),
                 "n_tool_calls": r.get("n_tool_calls", 0), "memory_tool_calls": r.get("memory_tool_calls", 0),
                 "wall_seconds": r.get("wall_seconds"), "stop_reason": r.get("stop_reason"), "error": r.get("error", "")}
        row = {"run_id": r["run_id"], "model": r["model_name"], "task_id": r["task_id"], "condition": r["condition"], "seed": r["seed"]}
        f = finals[r["run_id"]]
        row.update(scoring.score_replay(f, k, r["condition"], usage))
        if isinstance(f, dict):
            row.update(scoring.proposal_overlap(f, clusters.record_texts([records[i] for i in task["permitted_records"]]), vec, repeat_sim))
        rows.append(row)
    return rows


cfg = experiment.load_config(sys.argv[1] if os.path.isabs(sys.argv[1]) else os.path.join(experiment.HB, sys.argv[1]))
runs = experiment.raw_runs(cfg)
base = cfg["_out"]

finals, notes = {}, []
for r in runs:
    if r["stop_reason"] == "final":
        finals[r["run_id"]] = r["final"]
    else:
        o, how = recover(r)
        finals[r["run_id"]] = o
        notes.append({"run": r["run_id"], "stop_reason": r["stop_reason"], "recovery": how})

cfg_rec = dict(cfg, _out=os.path.join(base, "sensitivity_recovered"), note="POST-HOC SENSITIVITY: outputs of unparseable runs recovered")
os.makedirs(cfg_rec["_out"], exist_ok=True)
rec_rows = rows_for(cfg, runs, finals)
res_rec = experiment.analyze(cfg_rec, rec_rows)
json.dump(notes, open(os.path.join(cfg_rec["_out"], "recovery_log.json"), "w", encoding="utf-8"), indent=1)

itt_rows = rows_for(cfg, runs, {r["run_id"]: (r["final"] if r["stop_reason"] == "final" else None) for r in runs})
keys = experiment.answer_key()
for row in itt_rows:
    if not row.get("valid_output") and row.get("flag_correct") is None:
        sf = int(keys[row["task_id"]]["should_flag_before_running"])
        row.update({"flag_correct": 0, "flagged": 1 - sf, "should_flag": sf, "valid_output": True, "schema_problems": "ITT: counted as incorrect"})
cfg_itt = dict(cfg, _out=os.path.join(base, "sensitivity_itt"), note="POST-HOC SENSITIVITY: unparseable runs counted as incorrect on P1")
os.makedirs(cfg_itt["_out"], exist_ok=True)
res_itt = experiment.analyze(cfg_itt, itt_rows)

by = {(r["task_id"], r["condition"]): r for r in rec_rows}
raw = {(r["task_id"], r["condition"]): r for r in runs}
table = []
for t in cfg["tasks"]:
    k = keys[t]
    row = {"task_id": t, "stratum": k["stratum"], "should_flag": int(k["should_flag_before_running"]),
           "redundancy_subset": bool(k["prior_same_question_families_in_memory"])}
    for c in cfg["conditions"]:
        s = by[(t, c)]
        row[f"{c}_status"] = raw[(t, c)]["stop_reason"]
        row[f"{c}_flagged"] = s.get("flagged")
        row[f"{c}_p_testable"] = s.get("p_testable")
        row[f"{c}_decision"] = s.get("decision")
        row[f"{c}_predicted"] = s.get("predicted_stratum")
        row[f"{c}_memory_calls"] = raw[(t, c)]["memory_tool_calls"]
    table.append(row)
common.write_csv(os.path.join(base, "per_task.csv"), table)
for name, res in (("recovered", res_rec), ("itt", res_itt)):
    print("==", name)
    for c, s in res["summary_by_condition"].items():
        print(" ", c, {k: round(v, 3) if isinstance(v, float) else v for k, v in s.items() if k in ("valid_outputs", "P1_balanced_flag_accuracy", "testability_auc", "testability_brier", "outcome_log_loss", "risk_recall")})
    for x in res["primary_P1_contrasts"]:
        print("  ", x["contrast"], x["n_tasks"], round(x["mean_difference"], 3), tuple(round(v, 3) for v in x["ci95"]), x["p_sign_flip"], round(x.get("p_holm", 1), 3))
    print("   equivalence C vs B", res["C_vs_B_equivalence_P1"])
print(json.dumps(notes, indent=1))
for row in table:
    print(row)
