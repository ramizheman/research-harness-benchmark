"""Research memory version 3: one consolidated record per study family, rendered as family documents (condition B) and
as a family graph (condition C) from a single canonical fact list.

Every family record states the research question, hypothesis, data and sample, method and measures, the actual result,
the outcome status, the failure mechanism, limitations, validation, related families and sources. Field names mark the
basis of each fact:
  observed_*  copied from the research records (text as recorded)
  auto_*      automated interpretation (rule-based adjudication or keyword rules; not human adjudication)
Missing information is written as NOT_RECORDED; nothing is inferred to fill it.

Graph: StudyFamily nodes carry the attribute facts; relation facts become edges from the family to shared concept
nodes (question cluster, method, dataset, measure, limitation, risk code) and to other families (limitation
precedent, repeat relations, links between member records). Documents list the same facts as lines. equivalence()
(from memory_v2) parses both renderings back and compares them with the canonical facts.

The build is a pure function of the permitted records, through memory_v2.build_facts (adjudication, clusters,
knowability and record links are recomputed without excluded records).
"""
import ast
import collections
import hashlib
import json
import os
import re

from . import common, memory_v2

ENTITY_RE = re.compile(r"^(?:FAM|RQC|METH|DS|VAR|LIM|RISK):")
TYPES = {"FAM": "StudyFamily", "RQC": "ResearchQuestion", "METH": "Method", "DS": "Dataset", "VAR": "Measure",
         "LIM": "Limitation", "RISK": "RiskCode"}
NOT_RECORDED = "NOT_RECORDED"
STATUS_WORDS = {"supported": "supported", "rejected": "rejected", "uncertain": "inconclusive", "untestable": "untestable",
                "artifact": "artifact", "not_a_test": "not a hypothesis test", "no_result": "no result recorded"}
MECHANISMS = {"A_unanswerable": "question not answerable with the data or design",
              "B_powered_null": "adequately powered null result",
              "C_artifact": "apparent effect produced by a construction, selection or labelling flaw",
              "D_positive": "no failure: positive result", "E_unclear": "mechanism unclear from the records"}
FAMILY_REL = ("limitation_precedent", "repeat_order_unknown", "repeat_of_earlier_family", "repeated_by_later_family")
ATTR_ORDER = ("observed_research_question", "auto_outcome_status", "observed_hypothesis", "observed_result",
              "auto_failure_mechanism", "observed_failure_evidence", "observed_sample_and_power", "observed_method",
              "observed_verdict", "observed_failure_type", "auto_validation_status", "observed_notes", "auto_confidence", "auto_members_disagree",
              "auto_knowable_before_outcome", "observed_project", "observed_dates", "observed_member_records",
              "observed_sources", "auto_adjudication_basis")
REL_ORDER = ("auto_limited_by", "auto_has_risk", "auto_related_family", "auto_addresses_question", "auto_uses_method",
             "auto_uses_dataset", "auto_measures")


def _list(v):
    if isinstance(v, list):
        return v
    try:
        x = ast.literal_eval(str(v)) if v not in (None, "") else []
    except (ValueError, SyntaxError):
        return [v]
    return x if isinstance(x, list) else [x]


def _val(v):
    v = memory_v2.clean(v or "")
    return v if v else NOT_RECORDED


def family_facts(records, inv=None, thresholds=None):
    """Canonical facts of the consolidated family memory for the given records."""
    base, meta = memory_v2.build_facts(records, inv=inv, thresholds=thresholds)
    by_id = {r["id"]: r for r in records}
    adj = meta["adjudication"]
    cluster_of = {r["study_family_id"]: r["cluster_id"] for r in meta["family_rows"]}
    fam_of = {}
    for s, p, o, q in base.unique():
        if p == "member_of":
            fam_of[s[4:]] = o[4:]
    edges_by = collections.defaultdict(set)
    for s, p, o, q in base.unique():
        if s.startswith("EXP:") and p in ("uses_method", "uses_dataset", "measures"):
            edges_by[(fam_of[s[4:]], p)].add(o)
        if s.startswith("FAM:") and o.startswith("FAM:") and p in FAMILY_REL:
            edges_by[(s[4:], "fam:" + p)].add(o)
        if s.startswith("EXP:") and o.startswith("EXP:"):
            a, b = fam_of.get(s[4:]), fam_of.get(o[4:])
            if a and b and a != b:
                edges_by[(a, "fam:record_link_" + p)].add("FAM:" + b)
    F = memory_v2.Facts()
    for f, a in sorted(adj.items()):
        fam = "FAM:" + f
        raw = a["members"] if isinstance(a["members"], list) else re.split(r"[;,]\s*", str(a["members"]))
        ms = [m for m in raw if m in by_id]
        rep = by_id[a["representative"]]
        F.titles[fam] = f"Study family {f}: {memory_v2.clean(rep.get('title', ''))}"
        many = len(ms) > 1
        tag = (lambda m: f"[{m}] ") if many else (lambda m: "")
        F.add(fam, "observed_research_question", _val(rep.get("title")))
        F.add(fam, "observed_hypothesis", _val(rep.get("hypothesis")))
        for m in ms:
            r = by_id[m]
            F.add(fam, "observed_result", tag(m) + _val(r.get("primary_result")))
            F.add(fam, "observed_verdict", tag(m) + _val(r.get("verdict")))
            F.add(fam, "observed_failure_type", tag(m) + _val(r.get("failure_type")))
            F.add(fam, "observed_failure_evidence", tag(m) + _val(r.get("failure_evidence")))
            F.add(fam, "observed_sample_and_power", tag(m) + _val(r.get("power_info")))
            F.add(fam, "observed_method", tag(m) + _val(r.get("design")))
            F.add(fam, "observed_notes", tag(m) + _val(r.get("notes")))
            F.add(fam, "observed_dates", f"{m}: {_val(r.get('date'))} ({_val(r.get('date_basis'))})")
            for s in _list(r.get("sources")):
                F.add(fam, "observed_sources", f"{m}: {memory_v2.clean(s)}")
        F.add(fam, "observed_project", "; ".join(sorted({_val(by_id[m].get("project")) for m in ms})))
        F.add(fam, "observed_member_records", "; ".join(ms))
        st = a["automated_stratum"]
        F.add(fam, "auto_outcome_status", STATUS_WORDS.get(st, st))
        mech = a.get("failure_mechanism") or ""
        F.add(fam, "auto_failure_mechanism", f"{mech} ({MECHANISMS[mech]})" if mech in MECHANISMS else (mech or "none (no failure recorded)"))
        F.add(fam, "auto_validation_status", f"{_val(a.get('validation_status'))}; evidence: {_val(a.get('validation_evidence'))}")
        F.add(fam, "auto_confidence", f"{_val(a.get('confidence_level'))} ({_val(a.get('confidence'))})")
        F.add(fam, "auto_members_disagree", _val(a.get("members_disagree")))
        F.add(fam, "auto_adjudication_basis", f"{_val(a.get('decision_rule'))}; automated rule-based adjudication, not human adjudication")
        k = next((o for s, p, o, q in base.unique() if s == fam and p == "knowable_before_outcome_auto"), "")
        F.add(fam, "auto_knowable_before_outcome", _val(k))
        rule = {"rule": "automated"}
        for lvl, field in (("data", "data_level_limitations"), ("design", "design_level_limitations"), ("unclear", "level_unclear_limitations")):
            for lim in filter(None, (a.get(field) or "").split("; ")):
                lid = "LIM:" + memory_v2.slug(lim)
                F.titles[lid] = lim
                F.add(fam, "auto_limited_by", lid, basis="LIMIT_RULES on recorded power, failure evidence and notes", level=lvl)
        for rc in filter(None, (a.get("risk_codes") or "").split("; ")):
            F.titles["RISK:" + rc] = rc
            F.add(fam, "auto_has_risk", "RISK:" + rc, basis="risk taxonomy rules")
        if f in cluster_of:
            q = "RQC:" + cluster_of[f]
            F.add(fam, "auto_addresses_question", q, basis="TF-IDF question clustering")
        for p, rel in (("uses_method", "auto_uses_method"), ("uses_dataset", "auto_uses_dataset"), ("measures", "auto_measures")):
            for o in sorted(edges_by.get((f, p), ())):
                F.add(fam, rel, o, basis="keyword rules on member records")
        for (ff, p), dsts in edges_by.items():
            if ff == f and p.startswith("fam:"):
                for o in sorted(dsts):
                    if o[4:] in adj and o != fam:
                        F.add(fam, "auto_related_family", o, relation=p[4:], basis="family structure, similarity or record links")
    for s, p, o, q in base.unique():
        if s.startswith("RQC:") and p in ("label_terms", "main_topic"):
            F.titles.setdefault(s, base.titles.get(s, s))
            F.add(s, p, o)
    for s, t in base.titles.items():
        if s.startswith(("METH:", "DS:", "VAR:")) and any(o == s for _, _, o, _ in F.items):
            F.titles[s] = t
    for e, t in list(F.titles.items()):
        if e.split(":")[0] in ("METH", "DS", "VAR", "LIM", "RISK"):
            F.add(e, "label", t)
    for s in {x[2] for x in F.items if ENTITY_RE.match(x[2])} - set(F.titles):
        F.titles[s] = base.titles.get(s, s)
    return F, meta


def render_documents(F, out_dir):
    """Condition B: one document per study family, plus question and vocabulary documents."""
    common.rmtree_retry(out_dir)
    by_doc = collections.defaultdict(lambda: collections.defaultdict(list))
    for s, p, o, q in F.unique():
        by_doc[doc_key(s)][s].append((p, o, q))
    for s in F.titles:
        by_doc[doc_key(s)].setdefault(s, [])
    for key, subjects in by_doc.items():
        path = os.path.join(out_dir, key + ".md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        lines = []
        for s in sorted(subjects):
            lines.append(f"# {s} | {memory_v2.clean(F.titles.get(s, ''))}")
            for p, o, q in sorted(subjects[s], key=lambda x: (_order(x[0]), x[1])):
                lines.append(f"- {p}: {o}{memory_v2.qual_str(q)}")
            lines.append("")
        open(path, "w", encoding="utf-8").write("\n".join(lines))


def doc_key(s):
    pre, rest = s.split(":", 1)
    return {"FAM": "families/" + rest, "RQC": "questions/" + rest}.get(pre, "vocabulary")


def _order(p):
    o = ATTR_ORDER + REL_ORDER
    return o.index(p) if p in o else len(o)


def build_graph(F):
    nodes, edges = {}, []
    for s in set(F.titles) | {x[0] for x in F.items} | {x[2] for x in F.items if ENTITY_RE.match(x[2])}:
        nodes[s] = {"id": s, "type": TYPES[s.split(":")[0]], "_label": memory_v2.clean(F.titles.get(s, ""))}
    for s, p, o, q in F.unique():
        if q and ENTITY_RE.match(o):
            edges.append({"src": s, "rel": p, "dst": o, "provenance": dict(q)})
        else:
            v = nodes[s].get(p)
            nodes[s][p] = o if v is None else (v + [o] if isinstance(v, list) else [v, o])
    return nodes, edges


def snapshot(records, out_dir, inv=None, label="", thresholds=None):
    F, meta = family_facts(records, inv=inv, thresholds=thresholds)
    render_documents(F, os.path.join(out_dir, "documents"))
    os.makedirs(os.path.join(out_dir, "graph"), exist_ok=True)
    nodes, edges = build_graph(F)
    common.write_jsonl(os.path.join(out_dir, "graph", "graph_nodes.jsonl"), sorted(nodes.values(), key=lambda n: n["id"]))
    common.write_jsonl(os.path.join(out_dir, "graph", "graph_edges.jsonl"), edges)
    eq = memory_v2.equivalence(F, os.path.join(out_dir, "documents"), nodes, edges)
    fams = [n for n in nodes if n.startswith("FAM:")]
    missing = collections.Counter(p for s, p, o, q in F.unique() if s.startswith("FAM:") and NOT_RECORDED in o)
    h = hashlib.sha256(json.dumps(F.unique(), ensure_ascii=False).encode("utf-8")).hexdigest()
    manifest = {"label": label, "version": 3, "records": sorted(r["id"] for r in records), "n_records": len(records),
                "n_families": len(fams), "n_facts": len(F.unique()), "n_nodes": len(nodes), "n_edges": len(edges),
                "fact_hash": h, "equivalent": eq["equivalent"],
                "equivalence": {k: v for k, v in eq.items() if not isinstance(v, list)},
                "not_recorded_counts": dict(missing),
                "every_family_has_all_fields": all(
                    {p for s, p, o, q in F.unique() if s == fam} >= set(ATTR_ORDER) for fam in fams)}
    json.dump(manifest, open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8"), indent=1)
    return manifest, F, nodes, edges
