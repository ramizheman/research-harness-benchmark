r"""Pilot 3 analysis (protocol 3, family memory, three seeds), reported on its own, plus task-level comparisons with
Pilots 1 and 2 that are never pooled. Earlier pilot files are only read.

Unit of analysis: the task. Seeds are averaged within task before any contrast, so ten tasks remain ten observations.
Seed noise baseline: how often the same condition gives a different flag on the same task under another seed, compared
with how often B or C differ from A under the same seed.

Usage: python scripts\24_pilot3_analysis.py [configs\pilot3.json]
Writes <run>\analysis_p3\ (per_run.csv, per_task.csv, contrasts.csv, citations.csv, retrieval_pairs.csv, summary.json).
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
cfg = experiment.load_config(os.path.join(HB, sys.argv[1] if len(sys.argv) > 1 else os.path.join("configs", "pilot3.json")))
OUT = os.path.join(cfg["_out"], "analysis_p3")
os.makedirs(OUT, exist_ok=True)
keys = experiment.answer_key()
TASKS = cfg["tasks"]


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


p3 = derive(read_rows(os.path.join(cfg["_out"], "scores.csv")))
raw = {r["run_id"]: r for r in experiment.raw_runs(cfg)}
prev_path = os.path.join(HB, "runs", "pilot2_v1", "comparison", "per_run.csv")
prev = read_rows(prev_path)
p1 = derive([r for r in prev if r["pilot"] == "P1"])
p2 = derive([r for r in prev if r["pilot"] == "P2"])


# ------------------------------------------------------------------ direct citation check against the v3 memory
class Seen:
    def __init__(self, run, toolbox_facts):
        self.returned = [i for c in run.get("tool_calls", []) for i in c.get("returned_ids", [])]
        self.facts = toolbox_facts


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


def citation_check(final, run):
    if not isinstance(final, dict):
        return {"items": 0, "ids": 0, "unreturned": 0, "status_checked": 0, "status_wrong": 0}
    seen = Seen(run, facts_for(run["task_id"]))
    ids = [i for i in agent.cited_ids(final) if not agent.PLACEHOLDER.match(i)]
    probs = agent.citation_problems(final, seen)
    he = [x for x in final.get("historical_evidence") or [] if isinstance(x, dict)] if isinstance(final.get("historical_evidence"), list) else []
    checked = sum(1 for x in he if ("FAM:" + str(x.get("id", "")).strip().removeprefix("FAM:")) in set(seen.returned))
    fa = final.get("failed_approaches") if isinstance(final.get("failed_approaches"), list) else []
    return {"items": len(he) + len(fa), "ids": len(ids), "unreturned": sum(1 for p in probs if "not returned" in p),
            "status_checked": checked, "status_wrong": sum(1 for p in probs if "status is recorded" in p)}


cit = []
for row in p3:
    r = raw[row["run_id"]]
    fin, pre = r.get("final"), r.get("final_precorrection") or r.get("final")
    a, b = citation_check(pre, r), citation_check(fin, r)
    he = fin.get("historical_effect") if isinstance(fin, dict) and isinstance(fin.get("historical_effect"), dict) else {}
    cd = str(he.get("changed_decision", "")).strip().lower()
    returned = [i for c in r.get("tool_calls", []) if c["name"] == "retrieve_history" for i in c.get("returned_ids", [])]
    first = next((c for c in r.get("tool_calls", []) if c["name"] == "retrieve_history"), None)
    x = {"run_id": row["run_id"], "task_id": row["task_id"], "condition": row["condition"], "seed": row["seed"],
         **{"pre_" + k: v for k, v in a.items()}, **{"post_" + k: v for k, v in b.items()},
         "changed_decision": cd, "n_historical_evidence": len(fin.get("historical_evidence") or []) if isinstance(fin, dict) else None,
         "n_failed_approaches": len(fin.get("failed_approaches") or []) if isinstance(fin, dict) else None,
         "n_own_inferences": len(fin.get("own_inferences") or []) if isinstance(fin, dict) else None,
         "n_uncertainties": len(fin.get("uncertainties") or []) if isinstance(fin, dict) else None,
         "retrieve_calls": sum(1 for c in r.get("tool_calls", []) if c["name"] == "retrieve_history"),
         "followup_calls": sum(1 for c in r.get("tool_calls", []) if c["name"] in ("search_documents", "explore_graph", "read_family")),
         "families_returned": len(set(i for c in r.get("tool_calls", []) for i in c.get("returned_ids", []))),
         "first_retrieval_ids": "; ".join(first.get("returned_ids", [])) if first else "",
         "first_retrieval_chars": first.get("result_chars") if first else None,
         "edges_traversed": sum((c.get("trace") or {}).get("edges_traversed", 0) for c in r.get("tool_calls", [])),
         "first_query": json.dumps(first.get("args"), ensure_ascii=False)[:600] if first else "",
         "stage1_turns_before_retrieval": sum(1 for l in r.get("log", []) if l.get("stage") == 1)}
    row.update({k: v for k, v in x.items() if k not in row})
    row["claimed_changed_decision_num"] = float(cd == "yes") if cd else None
    cit.append(x)
common.write_csv(os.path.join(OUT, "citations.csv"), cit, list(cit[0].keys()))
common.write_csv(os.path.join(OUT, "per_run.csv"), p3, sorted({k for r in p3 for k in r}, key=lambda k: (k not in ("task_id", "condition", "seed"), k)))


# ------------------------------------------------------------------ Pilot 3 on its own
def mean(rs, m):
    v = [r[m] for r in rs if r.get(m) is not None]
    return float(np.mean(v)) if v else None


def task_ba(rs):
    """Balanced flag accuracy over tasks with seeds averaged within task (mean of p1-weighted task means)."""
    tm = stats.task_means(rs, "p1_weighted", rs[0]["condition"]) if rs else {}
    return float(np.mean(list(tm.values()))) if tm else None


def summarize(rs, with_seeds=True):
    valid = [r for r in rs if r.get("valid_output")]
    pts = [(r["p_testable"], r["testable_truth"]) for r in valid if r.get("p_testable") is not None]
    s = {"runs": len(rs), "valid": len(valid),
         "P1_balanced_flag_accuracy_task_level": task_ba(rs),
         "P1_balanced_flag_accuracy_valid_runs": stats.balanced_accuracy([r["flagged"] for r in valid], [r["should_flag"] for r in valid]),
         "testability_auc_runs": stats.auc([p for p, _ in pts], [t for _, t in pts]),
         **{m: mean(valid, m) for m in ("testability_brier", "outcome_log_loss", "risk_recall", "prior_work_recognized", "false_prior_claim", "prereg_quality")},
         "relevant_surfaced_rate": mean(rs, "relevant_surfaced_num"), "cites_relevant_seen_rate": mean(rs, "cites_relevant_seen_num"),
         "meaningfully_used_rate": mean(rs, "meaningfully_used_num"),
         "fabricated_citations_total": sum(r.get("n_fabricated_citations") or 0 for r in rs),
         "status_claims_checked": sum(r.get("status_claims_checked") or 0 for r in rs),
         "status_claims_correct": sum(r.get("status_claims_correct") or 0 for r in rs),
         "input_tokens_total": sum(r.get("input_tokens") or 0 for r in rs), "output_tokens_total": sum(r.get("output_tokens") or 0 for r in rs),
         "cost_usd_total": sum(r.get("cost_usd") or 0 for r in rs), "wall_seconds_mean": mean(rs, "wall_seconds"),
         "stop_reasons": {s: sum(1 for r in rs if r.get("stop_reason") == s) for s in sorted({str(r.get("stop_reason")) for r in rs})}}
    if with_seeds and rs and rs[0].get("seed") is not None:
        s["P1_balanced_accuracy_by_seed"] = {int(k): stats.balanced_accuracy([r["flagged"] for r in g if r.get("valid_output")],
                                                                             [r["should_flag"] for r in g if r.get("valid_output")])
                                             for k in sorted({r["seed"] for r in rs}) for g in [[r for r in rs if r["seed"] == k]]}
        s["testability_auc_by_seed"] = {int(k): stats.auc([r["p_testable"] for r in g], [r["testable_truth"] for r in g])
                                        for k in sorted({r["seed"] for r in rs})
                                        for g in [[r for r in rs if r["seed"] == k and r.get("valid_output") and r.get("p_testable") is not None]]}
    return s


summary3 = {c: summarize([r for r in p3 if r["condition"] == c]) for c in "ABC"}
for c in "ABC":
    cc = [x for x in cit if x["condition"] == c]
    summary3[c].update({
        "preliminary_answers_total": sum(r.get("preliminary_answers") or 0 for r in p3 if r["condition"] == c),
        "gate_turns_total": sum(r.get("gate_turns") or 0 for r in p3 if r["condition"] == c),
        "repair_turns_total": sum(r.get("repair_turns") or 0 for r in p3 if r["condition"] == c),
        "correction_turns_total": sum(r.get("correction_turns") or 0 for r in p3 if r["condition"] == c),
        "retrieval_first_rate": mean([r for r in p3 if r["condition"] == c], "retrieval_first"),
        "pre_ids_cited": sum(x["pre_ids"] for x in cc), "pre_unreturned_ids": sum(x["pre_unreturned"] for x in cc),
        "pre_status_checked": sum(x["pre_status_checked"] for x in cc), "pre_status_wrong": sum(x["pre_status_wrong"] for x in cc),
        "post_ids_cited": sum(x["post_ids"] for x in cc), "post_unreturned_ids": sum(x["post_unreturned"] for x in cc),
        "post_status_checked": sum(x["post_status_checked"] for x in cc), "post_status_wrong": sum(x["post_status_wrong"] for x in cc),
        "changed_decision_claims": {v: sum(1 for x in cc if x["changed_decision"] == v) for v in sorted({x["changed_decision"] for x in cc})},
        "historical_evidence_items_mean": mean(cc, "n_historical_evidence"), "failed_approaches_mean": mean(cc, "n_failed_approaches"),
        "own_inferences_mean": mean(cc, "n_own_inferences"), "followup_memory_calls_mean": mean(cc, "followup_calls"),
        "retrieve_calls_mean": mean(cc, "retrieve_calls"), "families_returned_mean": mean(cc, "families_returned"),
        "edges_traversed_mean": mean(cc, "edges_traversed"), "first_retrieval_chars_mean": mean(cc, "first_retrieval_chars"),
    })

contrasts = []
for a, b in (("A", "B"), ("A", "C"), ("B", "C")):
    contrasts.append({"family": "primary", **stats.contrast(p3, "p1_weighted", a, b)})
for a, b in (("A", "B"), ("A", "C"), ("B", "C")):
    for m, hib in (("testability_brier", False), ("outcome_log_loss", False), ("risk_recall", True), ("prior_work_recognized", True),
                   ("false_prior_claim", False), ("prereg_quality", True)):
        contrasts.append({"family": "secondary", **stats.contrast(p3, m, a, b, higher_is_better=hib)})
for m in ("relevant_surfaced_num", "cites_relevant_seen_num", "meaningfully_used_num"):
    contrasts.append({"family": "retrieval B vs C", **stats.contrast(p3, m, "B", "C")})
prim = [x for x in contrasts if x["family"] == "primary"]
for x, adj in zip(prim, stats.holm([x["p_sign_flip"] for x in prim])):
    x["p_holm"] = adj
_, dbc = stats.paired(p3, "p1_weighted", "B", "C")
equiv_bc = stats.tost(dbc, cfg.get("equivalence_margin", 0.10))


# ------------------------------------------------------------------ seed noise versus condition differences (flag level)
def flag(t, c, s):
    r = next((r for r in p3 if r["task_id"] == t and r["condition"] == c and r["seed"] == s and r.get("valid_output")), None)
    return None if r is None else r["flagged"]


seeds = sorted({int(r["seed"]) for r in p3})
noise = {}
for c in "ABC":
    pairs = [(flag(t, c, s1), flag(t, c, s2)) for t in TASKS for s1, s2 in itertools.combinations(seeds, 2)]
    pairs = [p for p in pairs if None not in p]
    noise[f"{c} vs {c}, different seeds"] = {"pairs": len(pairs), "flag_disagreement": float(np.mean([a != b for a, b in pairs])) if pairs else None}
for c in "BC":
    pairs = [(flag(t, "A", s), flag(t, c, s)) for t in TASKS for s in seeds]
    pairs = [p for p in pairs if None not in p]
    noise[f"A vs {c}, same seed"] = {"pairs": len(pairs), "flag_disagreement": float(np.mean([a != b for a, b in pairs])) if pairs else None}
dec = {}
for c in "ABC":
    for t in TASKS:
        ds = [r.get("decision") for r in p3 if r["task_id"] == t and r["condition"] == c]
        dec.setdefault(c, []).append(len(set(ds)))
noise["distinct decisions across 3 seeds, mean per task"] = {c: float(np.mean(v)) for c, v in dec.items()}


# ------------------------------------------------------------------ document versus graph retrieval
pairs = []
for t in TASKS:
    for s in seeds:
        xb = next((x for x in cit if x["task_id"] == t and x["condition"] == "B" and x["seed"] == s), None)
        xc = next((x for x in cit if x["task_id"] == t and x["condition"] == "C" and x["seed"] == s), None)
        rb = next((r for r in p3 if r["task_id"] == t and r["condition"] == "B" and r["seed"] == s), {})
        rc = next((r for r in p3 if r["task_id"] == t and r["condition"] == "C" and r["seed"] == s), {})
        if xb and xc:
            ib, ic = set(filter(None, xb["first_retrieval_ids"].split("; "))), set(filter(None, xc["first_retrieval_ids"].split("; ")))
            pairs.append({"task_id": t, "seed": s, "first_retrieval_shared": len(ib & ic), "B_first": len(ib), "C_first": len(ic),
                          "B_chars": xb["first_retrieval_chars"], "C_chars": xc["first_retrieval_chars"], "C_edges": xc["edges_traversed"],
                          "B_relevant_surfaced": rb.get("relevant_surfaced_num"), "C_relevant_surfaced": rc.get("relevant_surfaced_num"),
                          "B_flag_correct": rb.get("flag_correct"), "C_flag_correct": rc.get("flag_correct"),
                          "B_decision": rb.get("decision"), "C_decision": rc.get("decision")})
common.write_csv(os.path.join(OUT, "retrieval_pairs.csv"), pairs, list(pairs[0].keys()) if pairs else None)
bc = {"pairs": len(pairs), "first_retrieval_shared_mean": float(np.mean([p["first_retrieval_shared"] for p in pairs])) if pairs else None,
      "identical_first_retrieval": sum(1 for p in pairs if p["first_retrieval_shared"] == p["B_first"] == p["C_first"]),
      "B_chars_mean": float(np.mean([p["B_chars"] for p in pairs if p["B_chars"]])) if pairs else None,
      "C_chars_mean": float(np.mean([p["C_chars"] for p in pairs if p["C_chars"]])) if pairs else None,
      "flag_disagreement_same_seed": float(np.mean([p["B_flag_correct"] != p["C_flag_correct"] for p in pairs])) if pairs else None,
      "decision_disagreement_same_seed": float(np.mean([p["B_decision"] != p["C_decision"] for p in pairs])) if pairs else None}

# association, descriptive only: runs citing relevant retrieved evidence versus not
assoc = {}
for c in "BC":
    mem = [r for r in p3 if r["condition"] == c and r.get("flag_correct") is not None]
    for used in (True, False):
        g = [r["flag_correct"] for r in mem if bool(r.get("cites_relevant_seen")) == used]
        assoc[f"{c} runs {'citing' if used else 'not citing'} relevant retrieved evidence"] = {"runs": len(g), "flag_correct_rate": float(np.mean(g)) if g else None}
for c in "BC":
    for v in ("yes", "no"):
        g = [r["flag_correct"] for r in p3 if r["condition"] == c and r.get("flag_correct") is not None and str(r.get("changed_decision")) == v]
        assoc[f"{c} runs claiming changed_decision={v}"] = {"runs": len(g), "flag_correct_rate": float(np.mean(g)) if g else None}


# ------------------------------------------------------------------ task-level comparison with Pilots 1 and 2 (not pooled)
per_task = []
tm = {}
for tag, rs in (("P1", p1), ("P2", p2), ("P3", p3)):
    for c in "ABC":
        for m in ("flag_correct", "p_testable", "outcome_log_loss", "risk_recall", "relevant_surfaced_num", "cites_relevant_seen_num", "any_fabrication_num"):
            tm[(tag, c, m)] = stats.task_means(rs, m, c)
for t in TASKS:
    k = keys[t]
    row = {"task_id": t, "stratum": k["stratum"], "should_flag": k["should_flag_before_running"], "testable": k.get("testable_from_permitted_data", ""),
           "expected_risk_codes": k["expected_risk_codes"], "relevant_in_memory": next((r.get("relevant_families_in_memory") for r in p3 if r["task_id"] == t), None)}
    for tag in ("P1", "P2", "P3"):
        for c in "ABC":
            for m, short in (("flag_correct", "flag"), ("p_testable", "pt"), ("cites_relevant_seen_num", "cites_rel")):
                v = tm[(tag, c, m)].get(t)
                row[f"{tag}{c}_{short}"] = None if v is None else round(v, 3)
    for c in "ABC":
        row[f"P3{c}_decisions"] = "/".join(str(r.get("decision")) for r in sorted([r for r in p3 if r["task_id"] == t and r["condition"] == c], key=lambda r: r["seed"]))
    per_task.append(row)
common.write_csv(os.path.join(OUT, "per_task.csv"), per_task, list(per_task[0].keys()))

across = {}
for tag, rs in (("P1", p1), ("P2", p2)):
    across[tag] = {c: summarize([r for r in rs if r["condition"] == c], with_seeds=False) for c in "ABC"}
memory_effect = []
for c in "BC":
    for m, hib in (("flag_correct", True), ("p1_weighted", True), ("outcome_log_loss", False), ("risk_recall", True), ("cites_relevant_seen_num", True)):
        effs = {}
        for tag, rs in (("P1", p1), ("P2", p2), ("P3", p3)):
            ts, d = stats.paired(rs, m, "A", c)
            effs[tag] = dict(zip(ts, d if hib else -d))
        for t1, t2 in (("P1", "P3"), ("P2", "P3")):
            common_t = sorted(set(effs[t1]) & set(effs[t2]))
            d = np.array([effs[t2][t] - effs[t1][t] for t in common_t])
            memory_effect.append({"family": "change in memory effect across pilots (task-paired, not pooled)", "metric": m,
                                  "contrast": f"({c}-A in {t2}) - ({c}-A in {t1})" + ("" if hib else " (sign flipped: positive = better)"),
                                  "n_tasks": len(d), "mean_difference": float(d.mean()) if len(d) else None,
                                  "ci95": stats.bootstrap_ci(d), "p_sign_flip": stats.sign_flip_p(d)})
        memory_effect.append({"family": "memory effect within each pilot", "metric": m, "contrast": f"{c} - A",
                              **{f"{tag}_mean": float(np.mean(list(effs[tag].values()))) if effs[tag] else None for tag in ("P1", "P2", "P3")}})

common.write_csv(os.path.join(OUT, "contrasts.csv"), [dict(x, ci95=json.dumps(x.get("ci95"))) for x in contrasts + memory_effect],
                 ["family", "metric", "contrast", "n_tasks", "mean_difference", "ci95", "p_sign_flip", "p_holm", "P1_mean", "P2_mean", "P3_mean"])
res = {"experiment_id": cfg["experiment_id"], "mock": all(m["provider"] == "mock" for m in cfg["models"]), "n_tasks": len(TASKS), "seeds": seeds,
       "pilot3_by_condition": summary3, "pilot3_contrasts": contrasts, "C_vs_B_equivalence": equiv_bc, "seed_noise": noise,
       "document_vs_graph": bc, "associations_descriptive": assoc, "earlier_pilots_by_condition": across, "memory_effect_across_pilots": memory_effect,
       "earlier_pilot_files_modified": False}
json.dump(res, open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8"), indent=1, default=str)


def r3(v):
    return round(v, 3) if isinstance(v, float) else v


for c in "ABC":
    print(c, {k: r3(v) if not isinstance(v, dict) else {kk: r3(vv) for kk, vv in v.items()} for k, v in summary3[c].items()})
for x in contrasts:
    print(f"  {x['family']:18s} {x['metric']:24s} {x['contrast']:46s} d={r3(x['mean_difference'])} ci={tuple(r3(v) for v in x['ci95'])} p={x['p_sign_flip']} holm={r3(x.get('p_holm'))}")
print("B vs C equivalence", equiv_bc)
print("seed noise", noise)
print("document vs graph", bc)
print("associations", assoc)
for x in memory_effect:
    print("  ", {k: r3(v) if not isinstance(v, (tuple, list)) else tuple(r3(u) for u in v) for k, v in x.items() if k != "family"})
for tag in ("P1", "P2"):
    print(tag, {c: {k: r3(across[tag][c][k]) for k in ("P1_balanced_flag_accuracy_task_level", "P1_balanced_flag_accuracy_valid_runs", "testability_auc_runs", "outcome_log_loss", "risk_recall", "cost_usd_total")} for c in "ABC"})
