"""The committed Study 1b gold-family rule (study1b/gold_rule.md) as a function, for Study 2.

Same steps as study1b/propose_gold.py, which stays untouched. Deterministic: TF-IDF similarity, cluster ids, answer-key
fields and risk-code tags only; no model calls and no manual additions.
"""
import json
import os
import sys

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import retrieval_audit as ra  # noqa: E402


def gold_for(task, k, snap, ctx):
    strata, risks, _, _ = ra.snapshot_info(snap, with_risks=True)
    nodes = {n["id"]: n for n in (json.loads(l) for l in open(os.path.join(snap, "graph", "graph_nodes.jsonl"), encoding="utf-8"))}
    snap_fams = set(strata) | {ctx.family_of[p] for p in task["permitted_records"] if p in ctx.family_of}
    Q = ra.relevant_families(task, k, ctx, snap_fams)
    L = ra.lesson_families(k, risks, strata) - Q
    want = set(ra._list(k.get("expected_risk_codes")))
    named = {x.strip() for x in str(k.get("knowable_precedents") or "").split(";") if x.strip()} | set(ra._list(k.get("prior_same_question_families_in_memory")))
    own = [ctx.row[m] for m in ctx.members.get(task["study_family_id"], []) if m in ctx.row]
    perm = set(task["permitted_records"])

    def sim(f):
        rows = [ctx.row[m] for m in ctx.members.get(f, []) if m in ctx.row and m in perm]
        return float((ctx.X[own] @ ctx.X[rows].T).toarray().max()) if own and rows else 0.0

    qo = sorted(Q, key=lambda f: (f not in named, -sim(f), f))
    lo = sorted(L, key=lambda f: (-len(risks.get(f, set()) & want), -sim(f), f))
    pick = qo[:2] + lo[:2]
    rest = qo[2:] + lo[2:] if len(qo) < 2 or len(lo) < 2 else []
    pick += rest[:4 - len(pick)]

    def info(f, tier):
        n = nodes.get("FAM:" + f, {})
        return {"family": f, "tier": tier, "named_in_key": f in named, "stratum": strata.get(f),
                "shared_risk_codes": sorted(risks.get(f, set()) & want), "sim": round(sim(f), 3),
                "research_question": str(n.get("observed_research_question", ""))[:160]}
    return {"task_family": task["study_family_id"], "expected_risk_codes": sorted(want), "n_question_tier": len(Q),
            "n_lesson_tier": len(L), "gold": [info(f, "Q" if f in Q else "L") for f in pick],
            "next_candidates": [info(f, "Q") for f in qo if f not in pick][:3] + [info(f, "L") for f in lo if f not in pick][:3]}
