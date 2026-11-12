"""Protocol-3 tools over the consolidated family memory (bench/memory_v3).

retrieve_history has one name and one description in every condition. A executes it and returns nothing. B ranks the
study-family documents by TF-IDF text similarity to the request. C links the request to graph nodes (research-question
clusters, methods, datasets, measures, limitations, risk codes, and family entry points matched on question and
hypothesis only) and scores families by following relationships from those nodes; each returned family lists the
paths that reached it. Selection therefore differs between B and C, while the budget is the same: RETRIEVE_K families
per call, each shown through the same field selection under the same character budget (family_view), so a family
retrieved in B and in C shows identical facts. Follow-up tools have the same call and size limits in B and C.
"""
import json
import math
import os
import re

from bench import memory_v2, memory_v3
from runner import tools as tools_v1

RETRIEVE_K, VIEW_CHARS, VALUE_CHARS, MAX_PATHS = 4, 950, 220, 2
VIEW_ORDER = ("observed_research_question", "auto_outcome_status", "observed_hypothesis", "observed_result",
              "auto_failure_mechanism", "auto_limited_by", "auto_has_risk", "observed_failure_evidence",
              "observed_sample_and_power", "auto_validation_status", "auto_related_family", "observed_method",
              "observed_verdict", "observed_failure_type", "observed_notes", "auto_confidence", "auto_addresses_question",
              "auto_uses_method", "auto_uses_dataset", "auto_measures", "observed_member_records")
CONCEPT_SEEDS, FAMILY_SEEDS = 8, 4
TOOL_DOCS = {
    "retrieve_history": ("retrieve_history(research_concepts, methodological_questions, query): the prescribed retrieval "
                         "step. Returns the most relevant consolidated study-family records of earlier research by this "
                         "project that are available in this setting, with their identifiers; returns an empty list when "
                         "none are available."),
    "glossary": tools_v1.TOOL_DOCS["glossary"],
    "data_catalog": tools_v1.TOOL_DOCS["data_catalog"],
    "search_documents": f"search_documents(query): rank further study-family documents by text relevance; returns up to {RETRIEVE_K} families not yet returned.",
    "explore_graph": "explore_graph(node_id): the relationships of one graph node (a family or a question, method, dataset, measure, limitation or risk node), with neighbour labels.",
    "read_family": "read_family(id): the complete record of one study family (for example 'FAM:SF-APPA-001').",
}
CONDITION_TOOLS = {"A": ["retrieve_history", "glossary", "data_catalog"],
                   "B": ["retrieve_history", "glossary", "data_catalog", "search_documents", "read_family"],
                   "C": ["retrieve_history", "glossary", "data_catalog", "explore_graph", "read_family"]}
MEMORY_TOOLS = ("retrieve_history", "search_documents", "explore_graph", "read_family")


def _tfidf():
    from sklearn.feature_extraction.text import TfidfVectorizer
    return TfidfVectorizer(sublinear_tf=True, token_pattern=r"(?u)\b\w[\w\-]+\b")


def family_view(facts, budget=VIEW_CHARS):
    """The facts of one family shown by retrieval: fields in a fixed priority order, long values cut to VALUE_CHARS,
    added until the budget is used. Identical in B and C because it depends only on the facts."""
    out, used = [], 0
    rank = lambda p: VIEW_ORDER.index(p) if p in VIEW_ORDER else len(VIEW_ORDER)  # noqa: E731
    for p, o in sorted(((p, o) for p, o, _ in facts if p in VIEW_ORDER), key=lambda x: (rank(x[0]), x[1])):
        o = o if len(o) <= VALUE_CHARS else o[:VALUE_CHARS] + " [cut; read_family for the full text]"
        cost = len(p) + len(o) + 4
        if used + cost > budget and out:
            continue
        out.append((p, o))
        used += cost
    return out


class Toolbox3:
    def __init__(self, condition, snapshot_dir=None, max_chars=6000):
        self.condition, self.max_chars, self.protocol = condition, max_chars, 3
        self.allowed = CONDITION_TOOLS[condition]
        self.last_ids, self.last_trace, self.returned = [], {}, []
        self.facts, self.titles = {}, {}
        if condition == "A":
            return
        if condition == "B":
            facts, titles = memory_v2.facts_from_documents(os.path.join(snapshot_dir, "documents"))
        else:
            nodes = {}
            for l in open(os.path.join(snapshot_dir, "graph", "graph_nodes.jsonl"), encoding="utf-8"):
                n = json.loads(l)
                nodes[n["id"]] = n
            edges = [json.loads(l) for l in open(os.path.join(snapshot_dir, "graph", "graph_edges.jsonl"), encoding="utf-8")]
            facts, titles = memory_v2.facts_from_graph(nodes, edges)
            self.nodes, self.edges = nodes, edges
        for s, p, o, q in facts:
            self.facts.setdefault(s, []).append((p, o, q))
        self.titles = titles
        self.families = sorted(s for s in self.facts if s.startswith("FAM:"))
        if condition == "B":
            self.doc_text = {f: open(os.path.join(snapshot_dir, "documents", "families", f[4:] + ".md"), encoding="utf-8").read()
                             for f in self.families}
            self.vec = _tfidf()
            self.X = self.vec.fit_transform([self.doc_text[f] for f in self.families])
        else:
            self._build_graph_index()

    # ------------------------------------------------------------------ graph index (C)
    def _build_graph_index(self):
        self.adj = {}
        for e in self.edges:
            self.adj.setdefault(e["src"], []).append(("out", e["rel"], e["dst"], e["provenance"]))
            self.adj.setdefault(e["dst"], []).append(("in", e["rel"], e["src"], e["provenance"]))
        self.concepts = sorted(n for n in self.nodes if not n.startswith("FAM:"))
        ctext = [" ".join(str(v) for k, v in self.nodes[c].items() if k not in ("id", "type")).replace("_", " ") for c in self.concepts]
        self.cvec = _tfidf()
        self.CX = self.cvec.fit_transform(ctext)
        ftext = [" ".join(o for p, o, _ in self.facts[f] if p in ("observed_research_question", "observed_hypothesis")) for f in self.families]
        self.fvec = _tfidf()
        self.FX = self.fvec.fit_transform(ftext)

    def _graph_rank(self, q, exclude=()):
        cs = (self.cvec.transform([q]) @ self.CX.T).toarray().ravel()
        fs = (self.fvec.transform([q]) @ self.FX.T).toarray().ravel()
        cseeds = [(self.concepts[i], float(cs[i])) for i in cs.argsort()[::-1][:CONCEPT_SEEDS] if cs[i] > 0]
        fseeds = [(self.families[i], float(fs[i])) for i in fs.argsort()[::-1][:FAMILY_SEEDS] if fs[i] > 0]
        score, paths, traversed = {}, {}, 0
        for f, s in fseeds:
            score[f] = score.get(f, 0) + s
            paths.setdefault(f, []).append((s, f"request matches the question or hypothesis of {f} ({s:.2f})"))
        for c, s in cseeds:
            nb = [x for x in self.adj.get(c, []) if x[2].startswith("FAM:")]
            w = s / math.log2(2 + len(nb))
            for d, rel, f, _ in nb:
                traversed += 1
                score[f] = score.get(f, 0) + w
                paths.setdefault(f, []).append((w, f"request matches {c} ({s:.2f}); {f} {rel} {c}"))
        for g, s in fseeds:
            for d, rel, f, prov in self.adj.get(g, []):
                if f.startswith("FAM:") and f != g:
                    traversed += 1
                    score[f] = score.get(f, 0) + 0.5 * s
                    paths.setdefault(f, []).append((0.5 * s, f"{g} {rel} ({prov.get('relation', '')}) {f}"))
        ranked = sorted((f for f in score if f not in exclude), key=lambda f: (-score[f], f))[:RETRIEVE_K]
        trace = {"concept_seeds": [c for c, _ in cseeds], "family_seeds": [f for f, _ in fseeds], "edges_traversed": traversed,
                 "paths": {f: [p for _, p in sorted(paths[f], reverse=True)[:MAX_PATHS]] for f in ranked}}
        return [(f, round(score[f], 3)) for f in ranked], trace

    def _doc_rank(self, q, exclude=()):
        s = (self.vec.transform([q]) @ self.X.T).toarray().ravel()
        ranked = [(self.families[i], round(float(s[i]), 3)) for i in s.argsort()[::-1] if s[i] > 0 and self.families[i] not in exclude][:RETRIEVE_K]
        terms = set(self.vec.build_analyzer()(q))
        return ranked, {"query_terms": sorted(terms)[:40], "scores": dict(ranked)}

    # ------------------------------------------------------------------ rendering
    def _render(self, f, score, trace):
        view = family_view(self.facts[f])
        if self.condition == "B":
            text = f"# {f} | {self.titles.get(f, '')}\n" + "\n".join(f"- {p}: {o}" for p, o in view)
            return {"id": f, "score": score, "document": text}
        attrs, rels = {}, []
        for p, o in view:
            if memory_v3.ENTITY_RE.match(o):
                rels.append({"rel": p, "node": o})
            else:
                attrs[p] = o if p not in attrs else (attrs[p] + [o] if isinstance(attrs[p], list) else [attrs[p], o])
        return {"id": f, "label": self.titles.get(f, ""), "score": score, "reached_via": trace["paths"].get(f, []),
                "attributes": attrs, "relationships": rels}

    def retrieve(self, args, exclude=()):
        parts = [args.get("query", "")]
        for k in ("research_concepts", "methodological_questions"):
            v = args.get(k)
            parts += v if isinstance(v, list) else [v or ""]
        q = " ".join(str(x) for x in parts).strip()
        if self.condition == "A" or not q:
            self.last_trace = {"note": "no historical memory in this condition" if self.condition == "A" else "empty request"}
            return {"results": [], "n_results": 0}
        ranked, trace = (self._doc_rank if self.condition == "B" else self._graph_rank)(q, exclude)
        out = [self._render(f, s, trace) for f, s in ranked]
        while len(json.dumps({"results": out, "n_results": len(out)}, ensure_ascii=False)) > self.max_chars - 20 and \
                any(len(x.get("reached_via", [])) > 1 for x in out):
            max(out, key=lambda x: len(x.get("reached_via", [])))["reached_via"].pop()
        self.last_ids = [f for f, _ in ranked]
        self.last_trace = trace
        self.returned += self.last_ids
        return {"results": out, "n_results": len(out)}

    def read_family(self, fid):
        fid = fid if fid.startswith("FAM:") else "FAM:" + fid
        if fid not in self.facts:
            return {"error": f"no study family {fid!r}"}
        self.last_ids = [fid]
        self.returned.append(fid)
        if self.condition == "B":
            return {"id": fid, "document": self.doc_text[fid]}
        n = {k: v for k, v in self.nodes[fid].items() if k not in ("type",)}
        n["relationships"] = [{"direction": d, "rel": rel, "node": o, "label": self.titles.get(o, "")[:60], **prov}
                              for d, rel, o, prov in self.adj.get(fid, [])]
        return n

    def explore(self, nid):
        if nid not in self.nodes:
            return {"error": f"no node {nid!r}"}
        nb = self.adj.get(nid, [])
        self.last_ids = [o for _, _, o, _ in nb if o.startswith("FAM:")][:25]
        self.last_trace = {"explored": nid, "edges_traversed": len(nb)}
        self.returned += self.last_ids
        return {"id": nid, "label": self.titles.get(nid, ""), "n_relationships": len(nb),
                "relationships": [{"direction": d, "rel": rel, "node": o, "label": self.titles.get(o, "")[:60]} for d, rel, o, _ in nb[:40]]}

    # ------------------------------------------------------------------ dispatch
    def describe(self):
        return "\n".join("- " + TOOL_DOCS[t] for t in self.allowed)

    def call(self, name, args):
        self.last_ids, self.last_trace = [], {}
        if name not in self.allowed:
            return json.dumps({"error": f"tool {name!r} is not available"})
        args = args if isinstance(args, dict) else {}
        try:
            if name == "retrieve_history":
                out = self.retrieve(args)
            elif name == "search_documents":
                out = self.retrieve({"query": args.get("query", "")}, exclude=set(self.returned))
            elif name == "read_family":
                out = self.read_family(str(args.get("id", "")))
            elif name == "explore_graph":
                out = self.explore(str(args.get("node_id", args.get("id", ""))))
            elif name == "glossary":
                out = open(tools_v1.GLOSSARY, encoding="utf-8").read()
            else:
                out = tools_v1.data_catalog_text()
        except (TypeError, ValueError) as e:
            out = {"error": f"bad arguments: {e}"}
        s = out if isinstance(out, str) else json.dumps(out, ensure_ascii=False)
        return s[:self.max_chars] + (" ...[truncated]" if len(s) > self.max_chars else "")
