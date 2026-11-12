"""Revised research memory (version 2): one canonical fact list rendered as documents (condition B) and as a graph (C).

A fact is (subject, predicate, object, qualifiers). Relation facts (object is an entity id) become graph edges whose
provenance is the qualifiers; attribute facts become node properties. Documents list the same facts as text lines.
equivalence() parses both renderings back into fact sets and compares them.

build_facts() is a pure function of the records it is given. A task snapshot passes only the permitted records, so
clusters, adjudication, knowability, consolidated findings and relation directions are recomputed without any
excluded record.
"""
import collections
import hashlib
import json
import os
import re
import shutil

from . import adjudicate, clusters, common

ENTITY_RE = re.compile(r"^(?:EXP|RES|FAM|HYP|FIND|RQC|FG|DS|METH|LIM|VAR|PAPER|FOLLOW):")
TYPES = {"EXP": "Experiment", "RES": "Result", "FAM": "StudyFamily", "HYP": "Hypothesis", "FIND": "Finding",
         "RQC": "ResearchQuestion", "FG": "ConsolidatedFinding", "DS": "Dataset", "METH": "Method",
         "LIM": "StatisticalLimitation", "VAR": "Variable", "PAPER": "Paper", "FOLLOW": "FollowOnHypothesis"}
PAPERS = {"Structural Influence (Paper 1)": "Structural Influence (published)",
          "When a Hub Sits (Paper 2)": "When a Hub Sits (manuscript)",
          "Defensive Suppression": "Detecting Defensive Suppression (published)",
          "Halftime Minutes": "Halftime Minutes (manuscript)"}
FINDING_REL = {"supported": "supported_by", "rejected": "contradicted_by", "artifact": "invalidated_by",
               "untestable": "found_untestable_by", "uncertain": "left_open_by"}
CALIBRATION = os.path.join(common.HB, "audit", "cluster_calibration.json")


def full_history_thresholds():
    """Cluster thresholds calibrated on the full history (family structure only, no outcomes), reused by snapshots."""
    if os.path.exists(CALIBRATION):
        c = json.load(open(CALIBRATION, encoding="utf-8"))
        return c["merge_similarity"], c["repeat_similarity"]
    return None, None


def clean(v):
    return re.sub(r"\s+", " ", str(v)).strip()


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


class Facts:
    def __init__(self):
        self.items = []
        self.titles = {}

    def add(self, s, p, o, **q):
        o = clean(o)
        if o == "":
            return
        if not q:
            o = re.sub(r" \{(?=[a-z_]+=)", " (", o)
        quals = tuple(sorted((k, re.sub(r"[;{}]", ",", clean(v))) for k, v in q.items() if clean(v) != ""))
        self.items.append((s, p, o, quals))

    def rel(self, s, p, o, rule, **q):
        assert ENTITY_RE.match(o), o
        self.add(s, p, o, rule=rule, **q)

    def unique(self):
        return sorted(set(self.items))


def record_link_relations(records, family_of, members, kind):
    """Directed links between records, from related-field id references and within repeat-run families.

    Direction rule: the later record extends the earlier one. Order is decided by date intervals; when it cannot be
    decided the link is kept as related_to with direction unknown. Returns list of dicts with the original reading.
    """
    by_id = {r["id"]: r for r in records}
    links = {}
    for r in records:
        for ref in dict.fromkeys(common.ID_RE.findall(str(r.get("related") or ""))):
            if ref in by_id and ref != r["id"]:
                links.setdefault(tuple(sorted((r["id"], ref))), {"origin": "related field", "cited_by": r["id"], "cited": ref})
    for f, ms in members.items():
        ms = [m for m in ms if m in by_id]
        if kind.get(f) == "repeat_runs_or_robustness":
            for i, a in enumerate(ms):
                for b in ms[i + 1:]:
                    links.setdefault(tuple(sorted((a, b))), {"origin": f"repeat-run family {f}", "cited_by": a, "cited": b})
    out = []
    for (a, b), info in sorted(links.items()):
        o = common.order(by_id[a], by_id[b])
        if o == "unknown":
            rel, src, dst, direction = "related_to", info["cited_by"], info["cited"], "unknown (date intervals overlap)"
        else:
            later, earlier = (a, b) if o == "after" else (b, a)
            rel, src, dst = "extends", later, earlier
            v1_src = info["cited_by"]
            direction = "verified by dates" if v1_src == later else "corrected (citing record is the earlier one)"
        same_fam = family_of[a] == family_of[b]
        if rel == "extends" and adjudicate.record_stratum(by_id[src])[0] == "artifact" and \
                adjudicate.record_stratum(by_id[dst])[0] == "supported" and (same_fam or info["origin"] == "related field"):
            rel = "invalidates"
        out.append({"src": src, "dst": dst, "rel": rel, "direction": direction, "origin": info["origin"],
                    "same_family": same_fam, "needs_review": rel == "related_to" or direction.startswith("corrected")})
    return out


def build_facts(records, family_review_path=common.FAMILY_REVIEW, inv=None, thresholds=None):
    """All memory facts for the given records (any subset of the merged ledger)."""
    inv = inv or {}
    merge_sim, repeat_sim = thresholds or full_history_thresholds()
    by_id = {r["id"]: r for r in records}
    family_of, members, kind, note = common.load_families(records, family_review_path)
    members = {f: [m for m in ms if m in by_id] for f, ms in members.items()}
    members = {f: ms for f, ms in members.items() if ms}
    family_of = {m: f for f, ms in members.items() for m in ms}
    F = Facts()
    if not records:
        return F, {}
    fam_rows, cl_rows, cal = clusters.build(records, family_of, members, merge_sim, repeat_sim) if len(members) > 1 else ([], [], {})
    cluster_of = {r["study_family_id"]: r["cluster_id"] for r in fam_rows}
    adj = {a["study_family_id"]: a for a in adjudicate.adjudicate_all(records, family_of, members, kind, inv)}
    know = adjudicate.knowability(list(adj.values()), records, family_of, members, cluster_of)
    dates = {d["experiment_id"]: d for d in adjudicate.date_audit(records)}

    # ---------------------------------------------------------- experiments and results
    for r in records:
        x, res = "EXP:" + r["id"], "RES:" + r["id"]
        F.titles[x] = r.get("title", "")
        for p in ("title", "project", "date", "date_basis", "prespecified", "knowable_in_advance", "hypothesis", "design", "notes"):
            F.add(x, p, r.get(p) or "")
        F.add(x, "date_reliable", dates[r["id"]]["reliable"])
        F.add(x, "date_issues", dates[r["id"]]["issues"])
        F.add(x, "n_runs", r.get("n_runs") or 1)
        F.add(x, "related_as_recorded", r.get("related") or "")
        for s in r.get("sources") or []:
            F.add(x, "source", s)
        for a in r.get("also_recorded_as") or []:
            F.add(x, "also_recorded_as", a)
        st, sub = adjudicate.record_stratum(r)
        F.titles[res] = "Result of " + r["id"]
        for p in ("verdict", "failure_type", "primary_result", "failure_evidence", "power_info"):
            F.add(res, p, r.get(p) or "")
        F.add(res, "record_stratum", st)
        F.add(res, "record_substatus", sub)
        prov = {"record": r["id"]}
        F.rel(x, "produced", res, "record fields", **prov)
        F.rel(x, "member_of", "FAM:" + family_of[r["id"]], "audit/study_family_review.csv or singleton", **prov)
        F.rel("HYP:" + family_of[r["id"]], "tested_by", x, "family hypothesis tested by member record", **prov)
        for d in common.tags(common.DATASET_RULES, common.text(r, "title", "hypothesis", "design", "project")):
            F.rel(x, "uses_dataset", "DS:" + slug(d), "keyword rule DATASET_RULES", **prov)
            F.titles["DS:" + slug(d)] = d
        for m in common.tags(common.METHOD_RULES, common.text(r, "title", "hypothesis", "design", "primary_result")):
            F.rel(x, "uses_method", "METH:" + slug(m), "keyword rule METHOD_RULES", **prov)
            F.titles["METH:" + slug(m)] = m
        for v in common.tags(common.VARIABLE_RULES, common.text(r, "title", "hypothesis", "design", "primary_result")):
            F.rel(x, "measures", "VAR:" + slug(v), "keyword rule VARIABLE_RULES", **prov)
            F.titles["VAR:" + slug(v)] = v
        if r.get("project") in PAPERS:
            pid = "PAPER:" + slug(PAPERS[r["project"]])
            F.titles[pid] = PAPERS[r["project"]]
            F.rel(x, "reported_in", pid, "project field", **prov)
        rel_text = common.text(r, "notes", "related", "failure_evidence")
        if re.search(r"motivat|follow-?up|next step|led to", rel_text):
            fo = "FOLLOW:" + r["id"]
            F.titles[fo] = "Follow-on candidate from " + r["id"]
            F.add(fo, "text", r.get("notes") or "")
            F.add(fo, "status", "candidate from text pattern; not curated")
            F.rel(x, "motivates", fo, "text pattern motivate/follow-up/next step", needs_review="yes", **prov)

    # ---------------------------------------------------------- record links with corrected direction
    for l in record_link_relations(records, family_of, members, kind):
        F.rel("EXP:" + l["src"], l["rel"], "EXP:" + l["dst"], "date-ordered record link", direction=l["direction"],
              origin=l["origin"], needs_review="yes" if l["needs_review"] else "no", record=l["src"])

    # ---------------------------------------------------------- families, hypotheses, findings
    for f, ms in sorted(members.items()):
        a, k = adj[f], know[f]
        fam, hyp, fin = "FAM:" + f, "HYP:" + f, "FIND:" + f
        rep = a["representative"]
        F.titles[fam] = f"Study family {f} ({a['family_kind']})"
        F.titles[hyp] = "Hypothesis of " + f
        F.add(hyp, "text", by_id[rep].get("hypothesis") or "")
        F.add(hyp, "source_record", rep)
        for p in ("family_kind", "automated_stratum", "automated_substatus", "outcome_status", "failure_mechanism",
                  "mechanism_votes", "decision_rule", "deciding_record", "confidence", "confidence_level",
                  "leave_one_out_stability", "members_disagree", "conflicting_evidence", "validation_status",
                  "validation_evidence", "adjudication_type"):
            F.add(fam, p, a[p])
        F.add(fam, "knowable_before_outcome_auto", k["knowable_auto"])
        F.add(fam, "knowable_basis", k["knowable_basis"])
        if f in note and note[f]:
            F.add(fam, "family_review_evidence", note[f])
        for pf in filter(None, k["precedent_families"].split("; ")):
            if pf in members:
                F.rel(fam, "limitation_precedent", "FAM:" + pf, "knowability: earlier family with overlapping limitation", family=f)
        if f in cluster_of:
            F.rel(hyp, "addresses", "RQC:" + cluster_of[f], "TF-IDF question clustering", family=f,
                  similarity_threshold=cal.get("merge_similarity", ""))
            fr = next(x for x in fam_rows if x["study_family_id"] == f)
            if fr["nearest_family_in_cluster"] and fr["relation"] != "related_question":
                F.rel(fam, fr["relation"], "FAM:" + fr["nearest_family_in_cluster"], "lexical similarity >= repeat threshold",
                      similarity=fr["nearest_similarity"], order=fr["nearest_order"] or "unknown", family=f)
        for lvl, field in (("data", "data_level_limitations"), ("design", "design_level_limitations"),
                           ("unclear (sample size or power; data scarcity not stated)", "level_unclear_limitations")):
            for lim in filter(None, a[field].split("; ")):
                F.rel(fam, "limited_by", "LIM:" + slug(lim), "LIMIT_RULES on power_info, failure_evidence, notes", level=lvl, family=f)
                F.titles["LIM:" + slug(lim)] = lim
        for rc in filter(None, a["risk_codes"].split("; ")):
            F.add(fam, "risk_code", rc)
        st = a["automated_stratum"]
        if st in FINDING_REL:
            dec = a["deciding_record"] or rep
            F.titles[fin] = f"Finding of {f}: {st}"
            F.add(fin, "status", st)
            F.add(fin, "statement", by_id[dec].get("primary_result") or "")
            F.add(fin, "validation_status", a["validation_status"])
            F.add(fin, "confidence", a["confidence"])
            F.rel(hyp, FINDING_REL[st], fin, "automated adjudication stratum", family=f, decided_by=dec)
            for m in ms:
                F.rel(fin, "derived_from", "EXP:" + m, "family member", family=f)
            if st in ("rejected", "artifact"):
                F.rel(fin, "rules_out", hyp, f"stratum {st}: hypothesis ruled out as specified (scope: this design and data)", family=f)

    # ---------------------------------------------------------- clusters and consolidated findings
    for c in cl_rows:
        q = "RQC:" + c["cluster_id"]
        F.titles[q] = "Research question cluster " + c["cluster_id"]
        F.add(q, "label_terms", c["label_terms"])
        F.add(q, "main_topic", c["main_topic"])
        F.add(q, "mean_within_similarity", c["mean_within_similarity"])
        by_st = collections.defaultdict(list)
        for f in c["families"].split("; "):
            if adj[f]["automated_stratum"] in FINDING_REL:
                by_st[adj[f]["automated_stratum"]].append(f)
        for st, fs in sorted(by_st.items()):
            if len(fs) < 2:
                continue
            g = f"FG:{c['cluster_id']}_{st}"
            F.titles[g] = f"Consolidated {st} findings in {c['cluster_id']}"
            F.add(g, "status", st)
            F.add(g, "n_families", len(fs))
            F.add(g, "summary", f"{len(fs)} families asking this question reached stratum {st}")
            F.rel(g, "about", q, "consolidation of findings with one stratum in one question cluster")
            for f in fs:
                F.rel(g, "consolidates", "FIND:" + f, "consolidation of findings with one stratum in one question cluster", family=f)
    for e, t in list(F.titles.items()):
        if e.split(":")[0] in ("DS", "METH", "VAR", "LIM", "PAPER"):
            F.add(e, "label", t)
    return F, {"calibration": cal, "adjudication": adj, "clusters": cl_rows, "family_rows": fam_rows}


# ---------------------------------------------------------------- rendering
def doc_key(subject):
    pre, rest = subject.split(":", 1)
    if pre in ("EXP", "RES", "FOLLOW"):
        return "records/" + rest
    if pre in ("FAM", "HYP", "FIND"):
        return "families/" + rest
    if pre == "RQC":
        return "questions/" + rest
    if pre == "FG":
        return "questions/" + rest.split("_")[0]
    return "vocabulary"


def qual_str(q):
    return " {" + "; ".join(f"{k}={v}" for k, v in q) + "}" if q else ""


def render_documents(F, out_dir):
    """Write condition B: markdown documents grouped by record, family, question cluster and vocabulary."""
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
            lines.append(f"# {s} | {clean(F.titles.get(s, ''))}")
            for p, o, q in subjects[s]:
                lines.append(f"- {p}: {o}{qual_str(q)}")
            lines.append("")
        open(path, "w", encoding="utf-8").write("\n".join(lines))


def build_graph(F):
    nodes, edges = {}, []
    for s in set(F.titles) | {x[0] for x in F.items} | {x[2] for x in F.items if ENTITY_RE.match(x[2])}:
        nodes[s] = {"id": s, "type": TYPES[s.split(":")[0]], "_label": clean(F.titles.get(s, ""))}
    for s, p, o, q in F.unique():
        if q and ENTITY_RE.match(o):
            edges.append({"src": s, "rel": p, "dst": o, "provenance": dict(q)})
        else:
            v = nodes[s].get(p)
            nodes[s][p] = o if v is None else (v + [o] if isinstance(v, list) else [v, o])
    return nodes, edges


def write_graph(F, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    nodes, edges = build_graph(F)
    common.write_jsonl(os.path.join(out_dir, "graph_nodes.jsonl"), sorted(nodes.values(), key=lambda n: n["id"]))
    common.write_jsonl(os.path.join(out_dir, "graph_edges.jsonl"), edges)
    return nodes, edges


# ---------------------------------------------------------------- parsing back and equivalence
LINE_RE = re.compile(r"^- ([A-Za-z_]+): (.*?)(?: \{((?:[a-z_]+=[^;{}]*)(?:; [a-z_]+=[^;{}]*)*)\})?$")


def facts_from_documents(doc_dir):
    facts, titles = set(), {}
    for root, _, files in os.walk(doc_dir):
        for fn in files:
            subject = None
            for line in open(os.path.join(root, fn), encoding="utf-8"):
                line = line.rstrip("\n")
                if line.startswith("# "):
                    subject, _, title = line[2:].partition(" | ")
                    titles[subject] = title
                elif line.startswith("- ") and subject:
                    m = LINE_RE.match(line)
                    if not m:
                        raise ValueError(f"unparseable line in {fn}: {line[:80]}")
                    p, o, qs = m.group(1), m.group(2), m.group(3)
                    q = tuple(tuple(x.split("=", 1)) for x in qs.split("; ")) if qs else ()
                    facts.add((subject, p, o, q))
    return facts, titles


def facts_from_graph(nodes, edges):
    facts, titles = set(), {}
    for n in nodes.values():
        titles[n["id"]] = n.get("_label", "")
        for k, v in n.items():
            if k in ("id", "type", "_label"):
                continue
            for x in (v if isinstance(v, list) else [v]):
                facts.add((n["id"], k, x, ()))
    for e in edges:
        facts.add((e["src"], e["rel"], e["dst"], tuple(sorted(e["provenance"].items()))))
    return facts, titles


def equivalence(F, doc_dir, nodes, edges):
    canon = set(F.unique())
    fd, td = facts_from_documents(doc_dir)
    fg, tg = facts_from_graph(nodes, edges)
    t_canon = {k: clean(v) for k, v in F.titles.items()}
    return {"canonical_facts": len(canon), "document_facts": len(fd), "graph_facts": len(fg),
            "missing_from_documents": sorted(canon - fd)[:20], "missing_from_graph": sorted(canon - fg)[:20],
            "extra_in_documents": sorted(fd - canon)[:20], "extra_in_graph": sorted(fg - canon)[:20],
            "n_missing_from_documents": len(canon - fd), "n_missing_from_graph": len(canon - fg),
            "n_extra_in_documents": len(fd - canon), "n_extra_in_graph": len(fg - canon),
            "title_mismatches": sum(1 for k in t_canon if td.get(k, "") != t_canon[k] or tg.get(k, "") != t_canon[k]),
            "equivalent": canon == fd == fg and all(td.get(k, "") == t_canon[k] == tg.get(k, "") for k in t_canon)}


def snapshot(records, out_dir, inv=None, label="", thresholds=None):
    """Build and write a complete memory snapshot (documents and graph) for the given records; return manifest."""
    F, meta = build_facts(records, inv=inv, thresholds=thresholds)
    render_documents(F, os.path.join(out_dir, "documents"))
    nodes, edges = write_graph(F, os.path.join(out_dir, "graph"))
    eq = equivalence(F, os.path.join(out_dir, "documents"), nodes, edges)
    h = hashlib.sha256(json.dumps(F.unique(), ensure_ascii=False).encode("utf-8")).hexdigest()
    manifest = {"label": label, "records": sorted(r["id"] for r in records), "n_records": len(records),
                "n_facts": len(F.unique()), "n_nodes": len(nodes), "n_edges": len(edges), "fact_hash": h,
                "equivalent": eq["equivalent"], "equivalence": {k: v for k, v in eq.items() if not isinstance(v, list)}}
    json.dump(manifest, open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8"), indent=1)
    return manifest, F, meta, nodes, edges
