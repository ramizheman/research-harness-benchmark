"""Tools available to the agent. glossary and data_catalog exist in every condition; memory tools differ by condition.

B (documents): search_documents ranks document sections by TF-IDF; read_document returns one section or file.
C (graph): query_graph supports find (by type, attribute equality and text), node and neighbors.
Both read the same snapshot, whose documents and graph encode the same canonical facts (manifest 'equivalent').
"""
import json
import os
import re

from bench import challenges, common

HB = common.HB
GLOSSARY = os.path.join(HB, "tasks", "glossary.md")


def data_catalog_text():
    lines = ["Fields in the per-game NBA stats API files (all seasons):"]
    for src, fields in challenges.FIELDS.items():
        lines.append(f"- {src}: {fields}")
    return "\n".join(lines)


class DocumentMemory:
    def __init__(self, doc_dir):
        from sklearn.feature_extraction.text import TfidfVectorizer
        self.sections, self.files = [], {}
        for root, _, fns in os.walk(doc_dir):
            for fn in sorted(fns):
                key = os.path.relpath(os.path.join(root, fn), doc_dir).replace("\\", "/").rsplit(".", 1)[0]
                txt = open(os.path.join(root, fn), encoding="utf-8").read()
                self.files[key] = txt
                for block in re.split(r"\n(?=# )", txt):
                    block = block.strip()
                    if block.startswith("# "):
                        sid = block[2:].split(" | ")[0].strip()
                        self.sections.append((sid, key, block))
        self.by_id = {s: b for s, _, b in self.sections}
        self.vec = TfidfVectorizer(sublinear_tf=True, token_pattern=r"(?u)\b\w[\w\-]+\b")
        self.X = self.vec.fit_transform([b for _, _, b in self.sections]) if self.sections else None

    def search(self, query, k=8):
        if self.X is None:
            return []
        s = (self.vec.transform([query]) @ self.X.T).toarray().ravel()
        top = s.argsort()[::-1][:max(1, min(int(k), 20))]
        return [{"section": self.sections[i][0], "document": self.sections[i][1], "score": round(float(s[i]), 3),
                 "text": self.sections[i][2][:700]} for i in top if s[i] > 0]

    def rank(self, query, prefixes, k):
        """Top-k sections whose id starts with one of the prefixes, by the same TF-IDF score as search()."""
        if self.X is None:
            return []
        s = (self.vec.transform([query]) @ self.X.T).toarray().ravel()
        out = []
        for i in s.argsort()[::-1]:
            if s[i] <= 0 or len(out) >= k:
                break
            if self.sections[i][0].startswith(prefixes):
                out.append({"section": self.sections[i][0], "document": self.sections[i][1], "score": round(float(s[i]), 3),
                            "text": self.sections[i][2][:700]})
        return out

    def read(self, key):
        return self.by_id.get(key) or self.files.get(key) or f"no section or document named {key!r}"


class GraphMemory:
    def __init__(self, graph_dir):
        self.nodes = {}
        for l in open(os.path.join(graph_dir, "graph_nodes.jsonl"), encoding="utf-8"):
            if l.strip():
                n = json.loads(l)
                self.nodes[n["id"]] = n
        self.out, self.inn = {}, {}
        for l in open(os.path.join(graph_dir, "graph_edges.jsonl"), encoding="utf-8"):
            if l.strip():
                e = json.loads(l)
                self.out.setdefault(e["src"], []).append(e)
                self.inn.setdefault(e["dst"], []).append(e)
        self.types = sorted({n["type"] for n in self.nodes.values()})
        from sklearn.feature_extraction.text import TfidfVectorizer
        self.ids = sorted(self.nodes)
        blobs = [" ".join(str(v) for k, v in self.nodes[i].items() if k not in ("type",)) for i in self.ids]
        self.vec = TfidfVectorizer(sublinear_tf=True, token_pattern=r"(?u)\b\w[\w\-]+\b")
        self.X = self.vec.fit_transform(blobs)
        self.row = {i: k for k, i in enumerate(self.ids)}

    def find(self, type=None, where=None, text=None, limit=20):
        where = where if isinstance(where, dict) else {}
        sims = (self.vec.transform([text]) @ self.X.T).toarray().ravel() if text else None
        hits = []
        for i in self.ids:
            n = self.nodes[i]
            if type and n["type"] != type:
                continue
            if any(str(n.get(k)) != str(v) and str(v) not in (n.get(k) if isinstance(n.get(k), list) else []) for k, v in where.items()):
                continue
            s = float(sims[self.row[i]]) if sims is not None else 0.0
            if sims is not None and s <= 0:
                continue
            hits.append((s, i))
        hits.sort(key=lambda x: (-x[0], x[1]))
        return [self.node(i, brief=True) | {"match": round(s, 3)} for s, i in hits[:max(1, min(int(limit), 50))]]

    SNIPPET_KEYS = ("text", "statement", "hypothesis", "title", "primary_result", "status", "automated_stratum")

    def node(self, id, brief=False):
        n = self.nodes.get(id)
        if n is None:
            return {"error": f"no node {id!r}"}
        if brief:
            snip = " | ".join(f"{k}: {n[k]}" for k in self.SNIPPET_KEYS if isinstance(n.get(k), str))
            return {"id": id, "type": n["type"], "label": n.get("_label", ""), "snippet": snip[:400]}
        return {k if k != "_label" else "label": v for k, v in n.items()}

    def neighbors(self, id, rel=None, direction="both", limit=50):
        res = []
        for d, edges, end in (("out", self.out, "dst"), ("in", self.inn, "src")):
            if direction in (d, "both"):
                res += [{"direction": d, "rel": e["rel"], "node": e[end], "label": self.nodes.get(e[end], {}).get("_label", ""),
                         "qualifiers": e["provenance"]} for e in edges.get(id, []) if not rel or e["rel"] == rel]
        return res[:max(1, min(int(limit), 200))]


TOOL_DOCS = {
    "glossary": "glossary(): definitions of basketball and project terms used in task statements.",
    "data_catalog": "data_catalog(): the fields available in each per-game data file.",
    "search_documents": "search_documents(query, k=8): rank sections of the research-history documents by text relevance; returns section id, document, snippet.",
    "read_document": "read_document(key): full text of one section (by section id such as 'FAM:SF12') or one document (such as 'families/SF12').",
    "query_graph": ("query_graph(op, ...): structured access to the research-history graph. "
                    "op='find' with optional type (node type), where (attribute equality), text (keyword match), limit; "
                    "op='node' with id; op='neighbors' with id, optional rel and direction ('out', 'in', 'both')."),
}

CONDITION_TOOLS = {"A": ["glossary", "data_catalog"],
                   "B": ["glossary", "data_catalog", "search_documents", "read_document"],
                   "C": ["glossary", "data_catalog", "query_graph"]}

# Protocol 2: the prescribed retrieval step has one name and one description in every condition. In A it returns no
# records; in B and C it returns the same top-ranked items (identical TF-IDF ranking over the same section texts),
# as document text in B and as graph nodes with their edges in C. Only research records are ranked (families,
# family groups, hypotheses, experiments, results, findings); question-cluster and vocabulary nodes are reachable
# through the follow-up tools. Follow-up tools are the condition's own.
TOOL_DOCS["retrieve_history"] = ("retrieve_history(research_question, query, k=8): the prescribed retrieval step. Returns the "
                                 "most relevant records of earlier research by this project that are available in this "
                                 "setting, with their identifiers; returns an empty list when none are available.")
CONDITION_TOOLS_V2 = {"A": ["retrieve_history", "glossary", "data_catalog"],
                      "B": ["retrieve_history", "glossary", "data_catalog", "read_document"],
                      "C": ["retrieve_history", "glossary", "data_catalog", "query_graph"]}
RETRIEVE_K, ITEM_CHARS = 8, 700  # 8 items of at most 700 characters fit within the 6000-character tool-result cap
RECORD_PREFIXES = ("FAM:", "FG:", "HYP:", "EXP:", "RES:", "FIND:")


class Toolbox:
    def __init__(self, condition, snapshot_dir=None, max_chars=6000, protocol=1):
        self.condition, self.max_chars, self.protocol = condition, max_chars, protocol
        self.allowed = (CONDITION_TOOLS_V2 if protocol >= 2 else CONDITION_TOOLS)[condition]
        need_docs = condition == "B" or (protocol >= 2 and condition == "C")
        self.docs = DocumentMemory(os.path.join(snapshot_dir, "documents")) if need_docs else None
        self.graph = GraphMemory(os.path.join(snapshot_dir, "graph")) if condition == "C" else None
        self.last_ids = []

    def describe(self):
        docs = [TOOL_DOCS[t] + (" Node types: " + ", ".join(self.graph.types) + "." if t == "query_graph" else "") for t in self.allowed]
        return "\n".join("- " + d for d in docs)

    def retrieve(self, args):
        q = " ".join(str(args.get(k, "")) for k in ("research_question", "query")).strip()
        try:
            k = max(1, min(int(args.get("k", RETRIEVE_K)), RETRIEVE_K))
        except (TypeError, ValueError):
            k = RETRIEVE_K
        if self.condition == "A" or not q:
            return {"results": [], "n_results": 0}
        hits = self.docs.rank(q, RECORD_PREFIXES, k)
        out = []
        for h in hits:
            if self.condition == "B":
                item = {"id": h["section"], "document": h["document"], "score": h["score"], "text": ""}
                room = ITEM_CHARS - len(json.dumps(item, ensure_ascii=False))
                text = h["text"]
                while len(json.dumps(text[:room], ensure_ascii=False)) - 2 > room and room > 0:
                    room -= 20
                item["text"] = text[:max(room, 0)]
                out.append(item)
            else:
                n = self.graph.node(h["section"])
                attrs = {kk: (v if not isinstance(v, str) else v[:240]) for kk, v in n.items() if kk not in ("id", "type", "label")}
                edges = [f"{e['direction']} {e['rel']} {e['node']}" for e in self.graph.neighbors(h["section"], limit=12)]
                item = {"id": h["section"], "type": n.get("type"), "label": n.get("label", ""), "score": h["score"],
                        "attributes": attrs, "edges": edges}
                s = json.dumps(item, ensure_ascii=False)
                while len(s) > ITEM_CHARS and (item["edges"] or item["attributes"]):
                    minor = [kk for kk in item["attributes"] if kk not in GraphMemory.SNIPPET_KEYS]
                    if minor:
                        item["attributes"].pop(max(minor, key=lambda kk: len(str(item["attributes"][kk]))))
                    elif len(item["edges"]) > 4 or not item["attributes"]:
                        item["edges"].pop()
                    else:
                        item["attributes"].pop(max(item["attributes"], key=lambda kk: len(str(item["attributes"][kk]))))
                    s = json.dumps(item, ensure_ascii=False)
                out.append(item)
        self.last_ids = [o["id"] for o in out]
        return {"results": out, "n_results": len(out)}

    def call(self, name, args):
        self.last_ids = []
        if name not in self.allowed:
            return {"error": f"tool {name!r} is not available"}
        args = args if isinstance(args, dict) else {}
        try:
            if name == "retrieve_history":
                out = self.retrieve(args)
            elif name == "glossary":
                out = open(GLOSSARY, encoding="utf-8").read()
            elif name == "data_catalog":
                out = data_catalog_text()
            elif name == "search_documents":
                out = self.docs.search(str(args.get("query", "")), args.get("k", 8))
            elif name == "read_document":
                out = self.docs.read(str(args.get("key", "")))
                if self.protocol >= 2 and not out.startswith("no section"):
                    self.last_ids = [str(args.get("key", ""))]
            else:
                op = args.get("op")
                if op == "find":
                    out = self.graph.find(args.get("type"), args.get("where"), args.get("text"), args.get("limit", 20))
                elif op == "node":
                    out = self.graph.node(str(args.get("id", "")))
                elif op == "neighbors":
                    out = self.graph.neighbors(str(args.get("id", "")), args.get("rel"), args.get("direction", "both"), args.get("limit", 50))
                else:
                    out = {"error": "op must be find, node or neighbors"}
        except (TypeError, ValueError) as e:
            out = {"error": f"bad arguments: {e}"}
        s = out if isinstance(out, str) else json.dumps(out, ensure_ascii=False)
        s = s[:self.max_chars] + (" ...[truncated]" if len(s) > self.max_chars else "")
        if self.protocol >= 2 and name == "query_graph":
            self.last_ids = list(dict.fromkeys(NODE_ID_RE.findall(s)))
        if self.protocol >= 2 and name == "retrieve_history":
            self.last_ids = [i for i in self.last_ids if f'"{i}"' in s]
        return s


NODE_ID_RE = re.compile(r"\b(?:EXP|RES|FAM|HYP|FIND|RQC|FG|DS|METH|LIM|VAR|PAPER|FOLLOW):[A-Za-z0-9_\-]+")
