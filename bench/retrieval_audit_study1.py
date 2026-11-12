"""FROZEN COPY of bench/retrieval_audit.py as used for Study 1 (paper 1). Do not edit; it reproduces the 300 saved
Study 1 audit rows. Known defect: _list drops plain-string risk codes, and runs are audited against memory_v2.

Retrieval audit for protocol-2 runs: attempted, successful and meaningfully used retrieval, and whether retrieved
evidence was represented correctly. All rules are automated; relevance is defined from data, not by judgment.

Relevant families for a task (restricted to families present in the task's memory snapshot), in two tiers:
  question-relevant  same question cluster as the task family (research_question_clusters.csv), knowability
                     precedents and same-question families from the answer key, and families with any record whose
                     TF-IDF similarity to a task-family record reaches the calibrated merge threshold (0.231)
  lesson-relevant    untestable, artifact or uncertain families in the snapshot that carry one of the task's expected
                     risk codes (the lesson rule of the challenge pool, applied per task)
retrieval_attempted   retrieve_history was called
retrieval_successful  some returned item (retrieve_history or follow-up tool) belongs to a relevant family
meaningfully_used     successful, and the final output cites a relevant family whose identifier appeared in tool
                      results, and evidence_use is a substantive statement (at least 30 characters)
representation        for cited prior findings or failed experiments with a status, whether the status equals the
                      family's stratum in the snapshot the agent saw (only strata the schema allows; split by whether
                      the family's own record, which states the stratum, was returned or the status was inferred)
fabricated citation   a cited identifier that never appeared in any tool result of the run
relevant_surfaced     (any protocol) some memory tool result mentioned a relevant family
cites_relevant_seen   (any protocol) the output cites a relevant family that appeared in tool results
"""
import ast
import csv
import json
import os
import re

from . import clusters, common, memory_v2

NODE_ID_RE = re.compile(r"\b(?:EXP|RES|FAM|HYP|FIND|RQC|FG|DS|METH|LIM|VAR|PAPER|FOLLOW):[A-Za-z0-9_\-]+")
SF_RE = re.compile(r"\bSF(?:-[A-Z]+-\d{3}|\d+)\b")
MEMORY_TOOLS = ("retrieve_history", "read_document", "query_graph", "search_documents", "explore_graph", "read_family")
V3_STATUS = {"inconclusive": "uncertain", "not a hypothesis test": "not_a_test", "no result recorded": "no_result"}


def v3_as_v2(final):
    """Protocol-3 evidence fields expressed in the protocol-2 audit fields (statuses mapped to strata)."""
    if not isinstance(final, dict) or "historical_evidence" not in final:
        return final
    he = [x for x in final.get("historical_evidence") or [] if isinstance(x, dict)] if isinstance(final.get("historical_evidence"), list) else []
    fa = [x for x in final.get("failed_approaches") or [] if isinstance(x, dict)] if isinstance(final.get("failed_approaches"), list) else []
    st = lambda s: V3_STATUS.get(str(s).strip().lower(), str(s).strip().lower())  # noqa: E731
    eff = final.get("historical_effect") if isinstance(final.get("historical_effect"), dict) else {}
    return {**final, "retrieval_summary": {"prior_findings": [{"id": x.get("id", ""), "status": st(x.get("status_as_recorded", ""))} for x in he],
                                           "failed_experiments": [{"id": x.get("id", "")} for x in fa], "limitations": [], "unresolved": []},
            "evidence_use": str(eff.get("explanation") or "")}
PLACEHOLDER_RE = re.compile(r"^(?:|n/?a|none|null|-+|unknown|no id|not applicable)$", re.I)
STRATA = ("supported", "rejected", "untestable", "artifact", "uncertain")


class Context:
    """Shared lookups: family of each record, question clusters, record texts and vectoriser."""

    def __init__(self):
        self.records = {r["id"]: r for r in common.load_records()}
        self.family_of, self.members, _, _ = common.load_families(list(self.records.values()))
        self.cluster = {r["study_family_id"]: r["cluster_id"] for r in
                        csv.DictReader(open(os.path.join(common.HB, "research_question_clusters.csv"), encoding="utf-8-sig"))}
        self.merge_sim = memory_v2.full_history_thresholds()[0]
        ids = sorted(self.records)
        self.vec, X = clusters.vectorizer(clusters.record_texts([self.records[i] for i in ids]))
        self.X, self.row = X, {i: k for k, i in enumerate(ids)}


def snapshot_info(snap_dir, with_risks=False):
    """Family strata, risk codes and FG/RQC membership from the snapshot graph the agent saw."""
    strata, risks, fg, rqc = {}, {}, {}, {}
    for l in open(os.path.join(snap_dir, "graph", "graph_nodes.jsonl"), encoding="utf-8"):
        n = json.loads(l)
        if n["id"].startswith("FAM:") and n.get("automated_stratum"):
            strata[n["id"][4:]] = n["automated_stratum"]
            risks[n["id"][4:]] = set(_list(n.get("risk_code")))
    for l in open(os.path.join(snap_dir, "graph", "graph_edges.jsonl"), encoding="utf-8"):
        e = json.loads(l)
        if e["rel"] == "consolidates":
            fg.setdefault(e["src"], set()).add(e["dst"][4:])
        if e["rel"] == "addresses" and e["src"].startswith("HYP:"):
            rqc.setdefault(e["dst"], set()).add(e["src"][4:])
    return (strata, risks, fg, rqc) if with_risks else (strata, fg, rqc)


def families_of_id(i, ctx, fg, rqc):
    """Families an identifier refers to (empty for vocabulary nodes such as LIM:, DS:, METH:)."""
    if ":" in i:
        p, v = i.split(":", 1)
        if p in ("FAM", "HYP", "FIND"):
            return {v}
        if p in ("EXP", "RES"):
            return {ctx.family_of[v]} if v in ctx.family_of else set()
        if p == "FG":
            return set(fg.get(i, ()))
        if p == "RQC":
            return set(rqc.get(i, ()))
        return set()
    if SF_RE.fullmatch(i):
        return {i}
    if common.ID_RE.fullmatch(i):
        return {ctx.family_of[i]} if i in ctx.family_of else set()
    return set()


def ids_in(text):
    """Identifiers in a text, each in its most specific form (FAM:SF-APPA-001 is not also counted as SF-APPA-001)."""
    out = set(NODE_ID_RE.findall(text))
    rest = NODE_ID_RE.sub(" ", text)
    out |= set(SF_RE.findall(rest))
    out |= set(common.ID_RE.findall(SF_RE.sub(" ", rest)))
    return out


def _list(v):
    if isinstance(v, list):
        return v
    try:
        x = ast.literal_eval(str(v)) if v not in (None, "") else []
    except (ValueError, SyntaxError):
        return []
    return x if isinstance(x, list) else []


def lesson_families(key, risk_codes, strata):
    """Prior failed or uncertain families (untestable, artifact, uncertain in the snapshot) sharing a risk code with
    the task's expected risk codes; the same lesson rule as the challenge pool, applied per task."""
    want = set(_list(key.get("expected_risk_codes")))
    return {f for f, codes in risk_codes.items() if codes & want and strata.get(f) in ("untestable", "artifact", "uncertain")}


def relevant_families(task, key, ctx, snapshot_families):
    """Question-relevant families: same question cluster, knowability precedents, same-question families in memory,
    or a record at or above the calibrated merge similarity."""
    fam = task["study_family_id"]
    rel = {f for f, c in ctx.cluster.items() if c == ctx.cluster.get(fam) and f != fam}
    rel |= {x.strip() for x in str(key.get("knowable_precedents") or "").split(";") if x.strip()}
    rel |= set(_list(key.get("prior_same_question_families_in_memory")))
    own = [ctx.row[m] for m in ctx.members.get(fam, []) if m in ctx.row]
    perm = [p for p in task["permitted_records"] if p in ctx.row]
    if own and perm:
        S = (ctx.X[own] @ ctx.X[[ctx.row[p] for p in perm]].T).toarray().max(axis=0)
        rel |= {ctx.family_of[p] for p, s in zip(perm, S) if s >= ctx.merge_sim}
    return rel & snapshot_families


def _items(final, field):
    rs = (final or {}).get("retrieval_summary") or {}
    v = rs.get(field) if isinstance(rs, dict) else None
    return [x for x in v if isinstance(x, dict)] if isinstance(v, list) else []


def audit(run, task, key, snap_dir, ctx, input_price_per_million=None):
    strata, risks, fg, rqc = snapshot_info(snap_dir, with_risks=True)
    snap_fams = set(strata) | {ctx.family_of[p] for p in task["permitted_records"] if p in ctx.family_of}
    question_rel = relevant_families(task, key, ctx, snap_fams)
    lesson_rel = lesson_families(key, risks, strata)
    relevant = question_rel | lesson_rel
    log, msgs = run.get("log", []), run.get("messages", [])
    calls = [l["tool"] for l in log if "tool" in l]
    retr = [c for c in calls if c["name"] == "retrieve_history"]
    mem = [c for c in calls if c["name"] in MEMORY_TOOLS]
    returned = [i for c in mem for i in c.get("returned_ids", [])]
    seen_text = "\n".join(m["content"] for m in msgs if m["role"] == "user" and m["content"].startswith("TOOL_RESULT")
                          and m["content"].split(":", 1)[0].split()[-1] in MEMORY_TOOLS)
    seen = ids_in(seen_text)
    ret_fams = set().union(*[families_of_id(i, ctx, fg, rqc) for i in returned]) if returned else set()
    final = v3_as_v2(run.get("final")) if isinstance(run.get("final"), dict) else {}
    cited_raw = [str(x.get("id", "")) for f in ("prior_findings", "failed_experiments", "limitations", "unresolved") for x in _items(final, f)]
    cited_raw += [str(x) for x in ((final.get("prior_work") or {}).get("cited") or []) if isinstance(x, (str, int))]
    cited = set()
    for c in cited_raw:
        if PLACEHOLDER_RE.match(c.strip()):
            continue
        cited |= ids_in(c) or {c.strip()}
    def was_seen(c):
        bare = c.split(":", 1)[1] if ":" in c else c
        forms = {c, bare} | {f"{p}:{bare}" for p in ("FAM", "HYP", "FIND", "EXP", "RES")}
        return bool(forms & seen)
    fabricated = sorted(c for c in cited if not was_seen(c))
    cited_fams = set().union(*[families_of_id(c, ctx, fg, rqc) for c in cited if c not in fabricated]) if cited else set()
    # A status claim is checkable when the family's stratum is one the schema allows. It is 'shown' when the family's
    # own section or node (which carries automated_stratum) was returned; otherwise the agent inferred the status
    # from an experiment, result or hypothesis record that does not state the family stratum.
    shown_fams = {i[4:] for i in returned if i.startswith("FAM:")}
    tally = {"shown": [0, 0], "inferred": [0, 0]}
    wrong = []
    for f in ("prior_findings", "failed_experiments"):
        for x in _items(final, f):
            st = str(x.get("status", "")).strip().lower()
            fams = families_of_id(next(iter(ids_in(str(x.get("id", "")))), str(x.get("id", ""))), ctx, fg, rqc)
            if st in STRATA and len(fams) == 1:
                fam = next(iter(fams))
                if strata.get(fam) in STRATA:
                    kind = "shown" if fam in shown_fams else "inferred"
                    tally[kind][0] += 1
                    if strata[fam] == st:
                        tally[kind][1] += 1
                    else:
                        wrong.append(f"{x.get('id')} ({kind}): said {st}, memory says {strata[fam]}")
    checked, correct = tally["shown"][0] + tally["inferred"][0], tally["shown"][1] + tally["inferred"][1]
    evidence_use = str(final.get("evidence_use") or "").strip()
    seen_fams = set().union(*[families_of_id(i, ctx, fg, rqc) for i in seen]) if seen else set()
    successful = bool(ret_fams & relevant)
    used = successful and bool(cited_fams & relevant) and len(evidence_use) >= 30
    # token cost of memory results: each result stays in the context for every later model call
    mem_turns = [l["turn"] for l in log if "tool" in l and l["tool"]["name"] in MEMORY_TOOLS]
    n_calls = len(log)
    mem_tokens = sum(l["tool"]["result_chars"] / 4 for l in log if "tool" in l and l["tool"]["name"] in MEMORY_TOOLS)
    carried = sum(l["tool"]["result_chars"] / 4 * (n_calls - 1 - l["turn"]) for l in log if "tool" in l and l["tool"]["name"] in MEMORY_TOOLS)
    return {
        "retrieval_attempted": bool(retr), "retrieval_first": bool(calls) and calls[0]["name"] == "retrieve_history",
        "n_retrieve_calls": len(retr), "n_memory_calls": len(mem),
        "queries": " || ".join(" | ".join(str(c["args"].get(k, "")) for k in ("research_question", "query", "text", "key", "id") if c["args"].get(k)) for c in mem),
        "n_items_returned": len(returned), "n_families_returned": len(ret_fams),
        "relevant_families_in_memory": len(relevant), "relevant_families_returned": len(ret_fams & relevant),
        "question_relevant_in_memory": len(question_rel), "question_relevant_returned": len(ret_fams & question_rel),
        "lesson_relevant_in_memory": len(lesson_rel), "lesson_relevant_returned": len(ret_fams & lesson_rel),
        "relevant_available": bool(relevant), "retrieval_successful": successful,
        # protocol-independent: any memory tool result mentioned a relevant family; the output cites one it saw
        "relevant_surfaced": bool(seen_fams & relevant), "cites_relevant_seen": bool(cited_fams & relevant & seen_fams),
        "cited_ids": "; ".join(sorted(cited)), "n_cited": len(cited), "n_fabricated_citations": len(fabricated),
        "fabricated_citations": "; ".join(fabricated), "cited_relevant_families": len(cited_fams & relevant),
        "meaningfully_used": used, "evidence_use_chars": len(evidence_use),
        "status_claims_checked": checked, "status_claims_correct": correct,
        "representation_accuracy": (correct / checked) if checked else None, "misrepresentations": "; ".join(wrong),
        "status_shown_checked": tally["shown"][0], "status_shown_correct": tally["shown"][1],
        "status_inferred_checked": tally["inferred"][0], "status_inferred_correct": tally["inferred"][1],
        "retrieval_latency_seconds": round(sum(c.get("latency_seconds", 0) for c in mem), 3),
        "memory_result_tokens_est": round(mem_tokens), "memory_tokens_carried_est": round(carried),
        "memory_cost_usd_est": carried * input_price_per_million / 1e6 if input_price_per_million else None,
        "first_memory_turn": mem_turns[0] if mem_turns else None,
    }
