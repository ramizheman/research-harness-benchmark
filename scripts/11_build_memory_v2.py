r"""Build the revised memory (version 2) for the full history and audit it against version 1.

Outputs: memory_v2\full\documents\..., memory_v2\full\graph\graph_nodes.jsonl, graph_edges.jsonl, memory_v2\full\manifest.json,
         audit\memory_v2_audit.json, audit\extends_direction_audit.csv
Version 1 (memory\documents, memory\graph_*.jsonl) is read, never modified.
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bench import common, memory_v2  # noqa: E402

HB = common.HB
records = common.load_records()
by_id = {r["id"]: r for r in records}
inv = common.load_inventory()
out = os.path.join(HB, "memory_v2", "full")
manifest, F, meta, nodes, edges = memory_v2.snapshot(records, out, inv=inv, label="full history")

# ---------------------------------------------------------------- version-1 extends edges: direction audit
v1 = [json.loads(l) for l in open(os.path.join(HB, "memory", "graph_edges.jsonl"), encoding="utf-8")]
rows = []
for e in v1:
    if e["rel"] != "extends":
        continue
    a, b = e["src"][4:], e["dst"][4:]
    if a not in by_id or b not in by_id:
        continue
    o = common.order(by_id[a], by_id[b])
    rows.append({"v1_src": a, "v1_dst": b, "v1_rule": e["provenance"].get("rule", ""),
                 "date_order_of_src": o,
                 "assessment": {"after": "direction correct", "before": "direction reversed", "unknown": "direction ambiguous"}[o],
                 "src_date": f"{by_id[a].get('date')} ({by_id[a].get('date_basis')})",
                 "dst_date": f"{by_id[b].get('date')} ({by_id[b].get('date_basis')})"})
common.write_csv(os.path.join(HB, "audit", "extends_direction_audit.csv"), rows)
v1_assess = collections.Counter((r["v1_rule"].split(" (")[0], r["assessment"]) for r in rows)

# ---------------------------------------------------------------- version-2 statistics
rel_counts = collections.Counter(e["rel"] for e in edges)
no_rule = [e for e in edges if not e["provenance"].get("rule")]
link_dir = collections.Counter((e["rel"], e["provenance"].get("direction", "")) for e in edges
                               if e["rel"] in ("extends", "related_to", "invalidates"))
findings = collections.Counter(n.get("status") for n in nodes.values() if n["type"] == "Finding")
groups = [n for n in nodes.values() if n["type"] == "ConsolidatedFinding"]
lim_levels = collections.Counter((e["dst"], e["provenance"].get("level")) for e in edges if e["rel"] == "limited_by")
fam_lim = collections.Counter(e["provenance"].get("level") for e in edges if e["rel"] == "limited_by")
repeat_rel = collections.Counter(e["rel"] for e in edges if e["src"].startswith("FAM:") and e["dst"].startswith("FAM:") and e["rel"] != "limitation_precedent")
stats = {
    "manifest": manifest,
    "node_types": dict(collections.Counter(n["type"] for n in nodes.values())),
    "edge_types": dict(rel_counts),
    "edges_without_rule": len(no_rule),
    "edges_needing_review": sum(1 for e in edges if e["provenance"].get("needs_review") == "yes"),
    "record_link_directions": {f"{k[0]} | {k[1]}": v for k, v in link_dir.items()},
    "v1_extends_assessment": {f"{k[0]} | {k[1]}": v for k, v in v1_assess.items()},
    "findings_by_status": dict(findings),
    "consolidated_findings": len(groups),
    "consolidated_by_status": dict(collections.Counter(g.get("status") for g in groups)),
    "families_in_consolidated": sum(int(g.get("n_families", 0)) for g in groups),
    "family_limitations_by_level": dict(fam_lim),
    "limitations_by_level": {f"{k[0]} | {k[1]}": v for k, v in lim_levels.items()},
    "family_question_relations": dict(repeat_rel),
    "calibration": meta["calibration"],
    "v1_counts": {"nodes": sum(1 for _ in open(os.path.join(HB, "memory", "graph_nodes.jsonl"), encoding="utf-8")),
                  "edges": len(v1), "documents": len(os.listdir(os.path.join(HB, "memory", "documents")))},
}
json.dump(stats, open(os.path.join(HB, "audit", "memory_v2_audit.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(json.dumps(stats, indent=1, ensure_ascii=False)[:6000])
