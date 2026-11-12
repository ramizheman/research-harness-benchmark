"""Source material for scope annotations: each gold family's own record as it appears in the memory_v3 snapshot of
every task where it is gold. Reads no answer-key field. Writes study1b/annotation_sources.md. No model calls."""
import json, os, sys

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
gold = json.load(open(os.path.join(HB, "study1b", "gold_families_frozen.json"), encoding="utf-8"))["tasks"]
SKIP = ("id", "type", "observed_member_records")
fams = {}
for t, fs in gold.items():
    for f in fs:
        fams.setdefault(f, []).append(t)
lines = ["# Scope-annotation sources (family records from the task snapshots; no answer-key content)", ""]
for f in sorted(fams):
    recs = {}
    for t in fams[f]:
        nodes = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HB, "memory_v3", "snapshots", t, "graph", "graph_nodes.jsonl"), encoding="utf-8")}
        edges = [json.loads(l) for l in open(os.path.join(HB, "memory_v3", "snapshots", t, "graph", "graph_edges.jsonl"), encoding="utf-8")]
        n = nodes["FAM:" + f]
        rel = sorted(f"{e['rel']} {e['dst']}" for e in edges if e["src"] == "FAM:" + f and not e["rel"].startswith("auto_related"))
        recs[t] = ({k: v for k, v in n.items() if k not in SKIP}, rel, n.get("observed_member_records"))
    same = len({json.dumps(r, sort_keys=True) for r in recs.values()}) == 1
    lines += [f"## {f} (gold in {', '.join(fams[f])}; record identical across these snapshots: {same})", ""]
    for t, (node, rel, members) in recs.items():
        if t != fams[f][0] and same:
            break
        lines.append(f"Snapshot {t}; member records: {members}")
        for k, v in node.items():
            lines.append(f"- {k}: {v}")
        lines.append(f"- edges: {'; '.join(rel)}")
        lines.append("")
open(os.path.join(HB, "study1b", "annotation_sources.md"), "w", encoding="utf-8").write("\n".join(lines))
print(len(fams), "families;", "differ across snapshots:", [f for f in fams if len(fams[f]) > 1 and "False" in "".join(l for l in lines if l.startswith(f"## {f} "))])
