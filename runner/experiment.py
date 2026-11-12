"""Plan, execute, blind, score and analyse an experiment defined by a JSON config.

Phases (each resumable; existing run files are never overwritten):
  run      execute every (model, task, condition, seed) and save raw/<run>.json
  blind    write blinded/<blind id>.json (redacted outputs) and the sealed blinding key
  score    automated scores against the answer key -> scores.csv
  analyze  condition contrasts with intervals -> analysis.json, report.md
"""
import datetime as _dt
import glob
import hashlib
import json
import os
import random
import re
import secrets

import numpy as np

from bench import clusters, common, memory_v2, redact, retrieval_audit, scoring, stats
from . import agent, llm, tools, tools_v3

HB = common.HB
CODE_DIRS = ("bench", "runner")


def code_hash():
    h = hashlib.sha256()
    for d in CODE_DIRS:
        for p in sorted(glob.glob(os.path.join(HB, d, "*.py"))):
            h.update(open(p, "rb").read())
    return h.hexdigest()


def load_config(path):
    c = json.load(open(path, encoding="utf-8"))
    c["_config_hash"] = hashlib.sha256(json.dumps(c, sort_keys=True).encode()).hexdigest()
    c["_out"] = os.path.join(HB, "runs", c["experiment_id"])
    return c


def load_task(task_id):
    t = json.load(open(os.path.join(HB, "tasks", "replay", f"{task_id}.json"), encoding="utf-8"))
    body = json.dumps({k: t[k] for k in ("task_id", "statement", "permitted_records")}, sort_keys=True, ensure_ascii=False)
    if hashlib.sha256(body.encode("utf-8")).hexdigest() != t["task_hash"]:
        raise ValueError(f"{task_id}: frozen task file changed (hash mismatch)")
    return t


def answer_key():
    return {k["task_id"]: k for k in (json.loads(l) for l in open(os.path.join(HB, "benchmark_answer_key.jsonl"), encoding="utf-8")) if k.get("task_id")}


def ensure_snapshot(task, records=None, inv=None):
    """Return the task's snapshot dir, building it if absent; refuse a snapshot whose records differ from the task's."""
    d = os.path.join(HB, "memory_v2", "snapshots", task["task_id"])
    man = os.path.join(d, "manifest.json")
    if not os.path.exists(man):
        records = records or common.load_records()
        keep = set(task["permitted_records"])
        memory_v2.snapshot([r for r in records if r["id"] in keep], d, inv=inv or common.load_inventory(),
                           label=f"{task['task_id']} cutoff {task['task_date']}", thresholds=memory_v2.full_history_thresholds())
    m = json.load(open(man, encoding="utf-8"))
    if sorted(m["records"]) != sorted(task["permitted_records"]) or not m["equivalent"]:
        raise ValueError(f"{task['task_id']}: snapshot does not match the frozen permitted records or is not equivalent")
    if set(m["records"]) & set(task.get("excluded_records", [])):
        raise ValueError(f"{task['task_id']}: snapshot contains excluded records")
    return d, m


def ensure_snapshot_v3(task, records=None, inv=None):
    """Consolidated family memory (memory_v3) for a task: built from exactly the task's permitted records."""
    from bench import memory_v3
    d = os.path.join(HB, "memory_v3", "snapshots", task["task_id"])
    man = os.path.join(d, "manifest.json")
    if not os.path.exists(man):
        records = records or common.load_records()
        keep = set(task["permitted_records"])
        memory_v3.snapshot([r for r in records if r["id"] in keep], d, inv=inv or common.load_inventory(),
                           label=f"{task['task_id']} cutoff {task['task_date']} (family memory v3)", thresholds=memory_v2.full_history_thresholds())
    m = json.load(open(man, encoding="utf-8"))
    if sorted(m["records"]) != sorted(task["permitted_records"]) or not m["equivalent"] or not m["every_family_has_all_fields"]:
        raise ValueError(f"{task['task_id']}: v3 snapshot does not match the permitted records, is not equivalent, or lacks fields")
    if set(m["records"]) & set(task.get("excluded_records", [])):
        raise ValueError(f"{task['task_id']}: v3 snapshot contains excluded records")
    return d, m


def plan(cfg):
    """All runs, shuffled by order_seed. A model may list its own conditions. With run_order 'model_then_seed', models
    run in config order and seeds in ascending order (shuffled within each model and seed), so a budget stop cuts the
    last-listed model first and the highest seed next."""
    runs = []
    for spec in cfg["models"]:
        for t in cfg["tasks"]:
            for c in spec.get("conditions", cfg["conditions"]):
                for s in cfg["seeds"]:
                    runs.append({"model": spec, "task_id": t, "condition": c, "seed": s,
                                 "run_id": f"{cfg['experiment_id']}|{spec['provider']}:{spec['model']}|{t}|{c}|s{s}"})
    random.Random(cfg.get("order_seed", 0)).shuffle(runs)
    if cfg.get("run_order") == "model_then_seed":
        rank = {id(m): i for i, m in enumerate(cfg["models"])}
        runs.sort(key=lambda r: (rank[id(r["model"])], r["seed"]))
    return runs


def spend_cap(cfg):
    """The cap checked before every run: max_cost_usd, lowered to stop_fraction x budget_usd when a study budget is set."""
    caps = [c for c in (cfg.get("max_cost_usd"),) if c is not None]
    if cfg.get("budget_usd") is not None:
        caps.append(cfg["budget_usd"] * cfg.get("stop_fraction", 0.8))
    return min(caps) if caps else None


def oracle_inputs(cfg):
    """Frozen gold families and scope annotations for conditions O and OS, with file hashes for the run record."""
    o = cfg.get("oracle")
    if not o:
        return None
    paths = {k: os.path.join(HB, o[k]) for k in ("gold_file", "annotation_file")}
    return {"gold": json.load(open(paths["gold_file"], encoding="utf-8"))["tasks"],
            "annotations": json.load(open(paths["annotation_file"], encoding="utf-8"))["annotations"],
            "hashes": {k + "_sha256": hashlib.sha256(open(p, "rb").read()).hexdigest() for k, p in paths.items()}}


def _fname(run_id):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", run_id) + ".json"


def run_all(cfg, limit=None, log=print):
    out = cfg["_out"]
    os.makedirs(os.path.join(out, "raw"), exist_ok=True)
    manifest = os.path.join(out, "manifest.json")
    if not os.path.exists(manifest):
        json.dump({"config": {k: v for k, v in cfg.items() if not k.startswith("_")}, "config_hash": cfg["_config_hash"],
                   "code_hash": code_hash(), "created": _dt.datetime.now().isoformat(timespec="seconds")},
                  open(manifest, "w", encoding="utf-8"), indent=1)
    done, cap, consecutive_errors = 0, spend_cap(cfg), 0
    oracle = oracle_inputs(cfg)
    for r in plan(cfg):
        if consecutive_errors >= cfg.get("max_consecutive_errors", 3):
            log(f"stopping: {consecutive_errors} consecutive API errors")
            break
        path = os.path.join(out, "raw", _fname(r["run_id"]))
        if os.path.exists(path):
            continue
        if limit is not None and done >= limit:
            break
        if cap is not None:
            done_runs = raw_runs(cfg)
            spent = sum((x.get("usage") or {}).get("cost_usd") or 0.0 for x in done_runs)
            if spent >= cap:
                log(f"stopping: spent {spent:.4f} USD reaches the cap {cap} USD")
                break
            if cfg.get("budget_usd") is not None and any((x.get("usage") or {}).get("cost_known") is False for x in done_runs):
                log("stopping: a finished run has unknown cost, so spend against the study budget cannot be tracked")
                break
        task = load_task(r["task_id"])
        protocol = cfg.get("protocol", 1)
        chars = cfg["budgets"].get("max_tool_result_chars", 6000)
        if protocol >= 3 and r["condition"] in tools_v3.ORACLE_CONDITIONS:
            snap, man = ensure_snapshot_v3(task)
            if oracle is None:
                raise ValueError("conditions O and OS need an 'oracle' entry in the config")
            tb = tools_v3.Toolbox3(r["condition"], snap, chars, gold=oracle["gold"][r["task_id"]], annotations=oracle["annotations"])
        elif protocol >= 3:
            snap, man = ensure_snapshot_v3(task)
            tb = tools_v3.Toolbox3(r["condition"], snap if r["condition"] != "A" else None, chars)
        else:
            snap, man = ensure_snapshot(task)
            tb = tools.Toolbox(r["condition"], snap if r["condition"] != "A" else None, chars, protocol)
        client = llm.make(r["model"], cfg.get("env_path", llm.DEFAULT_ENV))
        try:
            if protocol >= 3:
                res = agent.run_v3(client, tb, task["statement"], r["seed"], cfg["budgets"])
            else:
                res = agent.run(client, tb, task["statement"], r["seed"], cfg["budgets"], protocol)
            err = ""
        except Exception as e:
            res, err = {"final": None, "stop_reason": "error", "usage": {}, "tool_calls": [], "n_tool_calls": 0, "memory_tool_calls": 0}, repr(e)[:1000]
        rec = {**r, "model_name": client.name, "task_hash": task["task_hash"], "snapshot_fact_hash": man["fact_hash"],
               "config_hash": cfg["_config_hash"], "code_hash": code_hash(), "error": err,
               "finished": _dt.datetime.now().isoformat(timespec="seconds"), **res}
        if r["condition"] in tools_v3.ORACLE_CONDITIONS:
            rec["oracle"] = {"gold": oracle["gold"][r["task_id"]], **oracle["hashes"]}
        json.dump(rec, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        done += 1
        consecutive_errors = consecutive_errors + 1 if res["stop_reason"] in ("api_error", "error") else 0
        want = r["model"].get("expected_response_model_version", cfg.get("expected_response_model_version"))
        if want and any(v != want for v in res.get("model_versions", [])):
            log(f"stopping: response model version {res.get('model_versions')} differs from the expected {want}")
            break
        u = res.get("usage") or {}
        log(f"{r['run_id']}: {res['stop_reason']} tools={res.get('n_tool_calls')} tokens={u.get('input_tokens', 0)}+{u.get('output_tokens', 0)} "
            f"cost={u.get('cost_usd') or 0:.4f} versions={res.get('model_versions')} {err}{res.get('api_error', '')}"[:600])
    return done


def raw_runs(cfg):
    return [json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(cfg["_out"], "raw", "*.json")))]


def blind(cfg):
    """Redacted outputs under blinded IDs. The key file maps blinded IDs back and must not be given to reviewers."""
    out = cfg["_out"]
    keyp = os.path.join(out, "sealed", "blinding_key.json")
    os.makedirs(os.path.dirname(keyp), exist_ok=True)
    os.makedirs(os.path.join(out, "blinded"), exist_ok=True)
    key = json.load(open(keyp, encoding="utf-8")) if os.path.exists(keyp) else {"secret": secrets.token_hex(16), "map": {}}
    n_red = 0
    for r in raw_runs(cfg):
        bid = redact.blind_id(key["secret"], r["run_id"])
        key["map"][bid] = r["run_id"]
        body, n = redact.redact_obj(r.get("final"))
        n_red += n
        p = os.path.join(out, "blinded", bid + ".json")
        if not os.path.exists(p):
            json.dump({"blind_id": bid, "task_statement": load_task(r["task_id"])["statement"], "output": body, "redactions": n},
                      open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(key, open(keyp, "w", encoding="utf-8"), indent=1)
    return len(key["map"]), n_red


def score(cfg):
    keys = answer_key()
    records = {r["id"]: r for r in common.load_records()}
    repeat_sim = memory_v2.full_history_thresholds()[1]
    vec, _ = clusters.vectorizer(clusters.record_texts(list(records.values())))
    rows, ctx = [], None
    for r in raw_runs(cfg):
        k = keys[r["task_id"]]
        task = load_task(r["task_id"])
        usage = r.get("usage") or {}
        u = {"input_tokens": usage.get("input_tokens", 0), "output_tokens": usage.get("output_tokens", 0),
             "cost_usd": usage.get("cost_usd") if usage.get("cost_known", True) else None,
             "n_tool_calls": r.get("n_tool_calls", 0), "memory_tool_calls": r.get("memory_tool_calls", 0),
             "wall_seconds": r.get("wall_seconds"), "stop_reason": r.get("stop_reason"), "error": r.get("error", "")}
        row = {"run_id": r["run_id"], "model": r["model_name"], "task_id": r["task_id"], "condition": r["condition"], "seed": r["seed"]}
        row.update(scoring.score_replay(r.get("final"), k, r["condition"], u))
        if isinstance(r.get("final"), dict):
            permitted = clusters.record_texts([records[i] for i in task["permitted_records"] if i in records])
            row.update(scoring.proposal_overlap(r["final"], permitted, vec, repeat_sim))
        if r.get("protocol", 1) >= 2:
            if ctx is None:
                ctx = retrieval_audit.Context()
            price = (r["model"].get("price_per_million") or {}).get("input")
            snap, _ = ensure_snapshot_v3(task) if r.get("protocol", 1) >= 3 else ensure_snapshot(task)
            row.update(retrieval_audit.audit(r, task, k, snap, ctx, price))
            row.update({"repair_turns": r.get("repair_turns"), "gate_turns": r.get("gate_turns"),
                        "parse_recoveries": "; ".join(r.get("parse_recoveries", []))})
            if r.get("protocol", 1) >= 3:
                row.update({"preliminary_answers": r.get("preliminary_answers", 0), "correction_turns": r.get("correction_turns", 0),
                            "initial_citation_problems": len(r.get("initial_citation_problems") or [])})
                if isinstance(r.get("final_precorrection"), dict):
                    pre = retrieval_audit.audit(dict(r, final=r["final_precorrection"]), task, k, snap, ctx, price)
                    row.update({"pre_" + m: pre[m] for m in ("n_fabricated_citations", "status_claims_checked", "status_claims_correct")})
                    row["pre_flag_correct"] = scoring.score_replay(r["final_precorrection"], k, r["condition"], {}).get("flag_correct")
                else:
                    row.update({"pre_" + m: row.get(m) for m in ("n_fabricated_citations", "status_claims_checked", "status_claims_correct")})
                    row["pre_flag_correct"] = row.get("flag_correct")
        rows.append(row)
    if rows:
        fields = sorted({k for r in rows for k in r}, key=lambda k: (k not in ("run_id", "model", "task_id", "condition", "seed"), k))
        common.write_csv(os.path.join(cfg["_out"], "scores.csv"), rows, fields)
    return rows


def _p1_weights(rows):
    """Weight per task so that the mean of weighted correctness equals balanced accuracy over flag classes."""
    cls = {r["task_id"]: r.get("should_flag") for r in rows if r.get("should_flag") is not None}
    n = len(cls)
    npos = sum(1 for v in cls.values() if v == 1)
    nneg = n - npos
    return {t: (n / (2 * npos) if v == 1 else n / (2 * nneg)) if npos and nneg else 1.0 for t, v in cls.items()}


def analyze(cfg, rows=None):
    rows = rows if rows is not None else score(cfg)
    w = _p1_weights(rows)
    for r in rows:
        r["p1_weighted"] = r["flag_correct"] * w[r["task_id"]] if r.get("flag_correct") is not None and r["task_id"] in w else None
    conds = cfg["conditions"]
    summary = {}
    for c in conds:
        rc = [r for r in rows if r["condition"] == c]
        valid = [r for r in rc if r.get("valid_output")]
        pts = [r["p_testable"] for r in valid if r.get("p_testable") is not None]
        summary[c] = {
            "runs": len(rc), "valid_outputs": len(valid),
            "P1_balanced_flag_accuracy": stats.balanced_accuracy([r["flagged"] for r in valid], [r["should_flag"] for r in valid]),
            "testability_auc": stats.auc(pts, [r["testable_truth"] for r in valid if r.get("p_testable") is not None]),
            **{m: (float(np.mean([r[m] for r in valid if r.get(m) is not None])) if any(r.get(m) is not None for r in valid) else None)
               for m in ("testability_brier", "outcome_log_loss", "risk_recall", "prereg_quality", "prior_work_recognized",
                         "false_prior_claim", "proposal_max_similarity", "input_tokens", "output_tokens", "n_tool_calls", "memory_tool_calls")},
            "cost_usd_total": (sum(r["cost_usd"] for r in rc if r.get("cost_usd") is not None) if all(r.get("cost_usd") is not None for r in rc) else None),
        }
        if cfg.get("protocol", 1) >= 2:
            def rate(m):
                return float(np.mean([bool(r.get(m)) for r in rc])) if rc else None
            chk = sum(r.get("status_claims_checked") or 0 for r in rc)
            summary[c].update({
                "retrieval_attempted_rate": rate("retrieval_attempted"), "retrieval_first_rate": rate("retrieval_first"),
                "retrieval_successful_rate": rate("retrieval_successful"), "meaningfully_used_rate": rate("meaningfully_used"),
                "fabricated_citations_total": sum(r.get("n_fabricated_citations") or 0 for r in rc),
                "status_claims_checked_total": chk,
                "representation_accuracy": (sum(r.get("status_claims_correct") or 0 for r in rc) / chk) if chk else None,
                "retrieval_latency_mean_s": float(np.mean([r.get("retrieval_latency_seconds") or 0 for r in rc])) if rc else None,
                "memory_tokens_carried_mean": float(np.mean([r.get("memory_tokens_carried_est") or 0 for r in rc])) if rc else None,
                "repair_turns_total": sum(r.get("repair_turns") or 0 for r in rc),
                "gate_turns_total": sum(r.get("gate_turns") or 0 for r in rc),
                "parse_recoveries_total": sum(len([x for x in str(r.get("parse_recoveries") or "").split("; ") if x]) for r in rc),
                "stop_reasons": "; ".join(sorted({str(r.get("stop_reason")) for r in rc})),
            })
        if cfg.get("protocol", 1) >= 3:
            summary[c].update({k + "_total": sum(r.get(k) or 0 for r in rc) for k in
                               ("preliminary_answers", "correction_turns", "initial_citation_problems", "pre_n_fabricated_citations")})
    primary, secondary = [], []
    pairs = [(a, b) for a, b in (("A", "B"), ("A", "C"), ("B", "C")) if a in conds and b in conds]
    for a, b in pairs:
        primary.append(stats.contrast(rows, "p1_weighted", a, b))
        for m, hib in (("testability_brier", False), ("outcome_log_loss", False), ("risk_recall", True), ("prereg_quality", True)):
            secondary.append(stats.contrast(rows, m, a, b, higher_is_better=hib))
    ps = [x["p_sign_flip"] for x in primary if x["p_sign_flip"] is not None]
    for x, adj in zip([x for x in primary if x["p_sign_flip"] is not None], stats.holm(ps) if ps else []):
        x["p_holm"] = adj
    equiv = None
    if "B" in conds and "C" in conds:
        _, d = stats.paired(rows, "p1_weighted", "B", "C")
        equiv = stats.tost(d, cfg.get("equivalence_margin", 0.10))
    res = {"experiment_id": cfg["experiment_id"], "mock": all(m["provider"] == "mock" for m in cfg["models"]),
           "n_tasks": len({r["task_id"] for r in rows}), "summary_by_condition": summary,
           "primary_P1_contrasts": primary, "secondary_contrasts": secondary, "C_vs_B_equivalence_P1": equiv,
           "note": cfg.get("note", "")}
    json.dump(res, open(os.path.join(cfg["_out"], "analysis.json"), "w", encoding="utf-8"), indent=1, default=str)
    write_report(cfg, res)
    return res


def _f(x, nd=3):
    if x is None:
        return "n/a"
    if isinstance(x, (tuple, list)):
        return "(" + ", ".join(_f(v, nd) for v in x) + ")"
    return f"{x:.{nd}f}" if isinstance(x, float) else str(x)


def write_report(cfg, res):
    L = [f"# Experiment {res['experiment_id']}", ""]
    if res["mock"]:
        L += ["**MOCK RUN.** Every output was produced by the scripted mock client. The numbers test the pipeline only and "
              "carry no information about memory or models.", ""]
    L += [f"Tasks: {res['n_tasks']}. Conditions: {', '.join(cfg['conditions'])}. Seeds: {cfg['seeds']}. "
          f"Models: {', '.join(m['provider'] + ':' + m['model'] for m in cfg['models'])}.", "",
          "## Summary by condition", "",
          "| metric | " + " | ".join(cfg["conditions"]) + " |", "|---|" + "---|" * len(cfg["conditions"])]
    metrics = list(next(iter(res["summary_by_condition"].values())).keys())
    for m in metrics:
        L.append(f"| {m} | " + " | ".join(_f(res["summary_by_condition"][c][m]) for c in cfg["conditions"]) + " |")
    L += ["", "## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)", "",
          "| contrast | tasks | mean difference | 95% interval | p | p (Holm) |", "|---|---|---|---|---|---|"]
    for x in res["primary_P1_contrasts"]:
        L.append(f"| {x['contrast']} | {x['n_tasks']} | {_f(x['mean_difference'])} | {_f(x['ci95'])} | {_f(x['p_sign_flip'])} | {_f(x.get('p_holm'))} |")
    L += ["", "## Secondary contrasts (not corrected; descriptive)", "", "| metric | contrast | mean difference | 95% interval | p |", "|---|---|---|---|---|"]
    for x in res["secondary_contrasts"]:
        L.append(f"| {x['metric']} | {x['contrast']} | {_f(x['mean_difference'])} | {_f(x['ci95'])} | {_f(x['p_sign_flip'])} |")
    if res["C_vs_B_equivalence_P1"]:
        e = res["C_vs_B_equivalence_P1"]
        L += ["", f"C versus B equivalence on P1 (margin {cfg.get('equivalence_margin', 0.10)}): 90% interval {_f(e['ci90'])}, equivalent: {e['equivalent']}."]
    L += ["", "Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are "
          "wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test."]
    open(os.path.join(cfg["_out"], "report.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
