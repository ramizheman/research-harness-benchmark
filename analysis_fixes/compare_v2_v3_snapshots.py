"""Compare family stratum, risk codes and question-cluster links between the v2 and v3 snapshot graphs per task.
Read-only."""
import ast, json, os
from collections import Counter
HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]


def codes(v):
    if v in (None, ""):
        return set()
    if isinstance(v, list):
        return set(v)
    try:
        x = ast.literal_eval(str(v))
        return set(x) if isinstance(x, list) else {str(v)}
    except (ValueError, SyntaxError):
        return {s.strip() for s in str(v).split(",") if s.strip()}


def load(ver, t):
    g = os.path.join(HB, ver, "snapshots", t, "graph")
    nodes = [json.loads(l) for l in open(os.path.join(g, "graph_nodes.jsonl"), encoding="utf-8")]
    edges = [json.loads(l) for l in open(os.path.join(g, "graph_edges.jsonl"), encoding="utf-8")]
    return nodes, edges


for t in T:
    n2, e2 = load("memory_v2", t)
    n3, e3 = load("memory_v3", t)
    s2 = {n["id"][4:]: n.get("automated_stratum") for n in n2 if n["id"].startswith("FAM:")}
    r2 = {n["id"][4:]: codes(n.get("risk_code")) for n in n2 if n["id"].startswith("FAM:")}
    s3 = {n["id"][4:]: n.get("auto_outcome_status") for n in n3 if n["id"].startswith("FAM:")}
    r3 = {f: set() for f in s3}
    for e in e3:
        if e["rel"] == "auto_has_risk" and e["src"].startswith("FAM:"):
            r3.setdefault(e["src"][4:], set()).add(e["dst"].split(":", 1)[1])
    fams = set(s2) | set(s3)
    st_diff = [f for f in fams if s2.get(f) != s3.get(f)]
    rk_diff = [f for f in fams if r2.get(f, set()) != r3.get(f, set())]
    print(f"{t}: families v2={len(s2)} v3={len(s3)} only_v2={len(set(s2) - set(s3))} only_v3={len(set(s3) - set(s2))} "
          f"stratum_diff={len(st_diff)} risk_diff={len(rk_diff)}")
    for f in sorted(st_diff)[:4]:
        print(f"    stratum {f}: v2={s2.get(f)} v3={s3.get(f)}")
    for f in sorted(rk_diff)[:4]:
        print(f"    risk {f}: v2={sorted(r2.get(f, set()))} v3={sorted(r3.get(f, set()))}")
    if t == "RT-179":
        print("    v2 edge rels:", dict(Counter(e["rel"] for e in e2)))
        print("    v2 node prefixes:", dict(Counter(n["id"].split(":")[0] for n in n2)))
        print("    v3 node prefixes:", dict(Counter(n["id"].split(":")[0] for n in n3)))
