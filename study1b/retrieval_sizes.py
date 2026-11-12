"""Characters of the first retrieve_history result per task in O and OS (untruncated length, before the 6,000-character
tool-result cut), and of read_family for each gold family. No model calls. Writes study1b/retrieval_sizes.txt.
Run with %TEMP%\\supp_audit_venv\\Scripts\\python.exe study1b\\retrieval_sizes.py
"""
import json, os, sys

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from runner import tools_v3
from runner.experiment import ensure_snapshot_v3, load_task

GOLD = json.load(open(os.path.join(HB, "study1b", "gold_families_frozen.json"), encoding="utf-8"))["tasks"]
ANN = json.load(open(os.path.join(HB, "study1b", "scope_annotations_frozen.json"), encoding="utf-8"))["annotations"]
REQ = {"query": "defensive adjustment"}
LIMIT = 6000
lines = [f"limit {LIMIT} characters per tool result (budgets.max_tool_result_chars); lengths are before the cut", "",
         "first retrieve_history result", f"{'task':8s} {'gold':>4s} {'O':>6s} {'OS':>6s}  status"]
for t, gold in GOLD.items():
    snap, _ = ensure_snapshot_v3(load_task(t))
    n = {}
    for c in ("O", "OS"):
        tb = tools_v3.Toolbox3(c, snap, 10 ** 6, gold=gold, annotations=ANN)
        n[c] = len(tb.call("retrieve_history", REQ))
    status = "; ".join(f"{c} OVER by {n[c] - LIMIT}" for c in n if n[c] > LIMIT) or "within"
    lines.append(f"{t:8s} {len(gold):4d} {n['O']:6d} {n['OS']:6d}  {status}")
lines += ["", "read_family per gold family (O / OS)"]
for t, gold in GOLD.items():
    if not gold:
        continue
    snap, _ = ensure_snapshot_v3(load_task(t))
    o = tools_v3.Toolbox3("O", snap, 10 ** 6, gold=gold, annotations=ANN)
    s = tools_v3.Toolbox3("OS", snap, 10 ** 6, gold=gold, annotations=ANN)
    for f in gold:
        a, b = len(o.call("read_family", {"id": f})), len(s.call("read_family", {"id": f}))
        lines.append(f"{t:8s} {f:12s} {a:6d} {b:6d}" + ("  OVER" if max(a, b) > LIMIT else ""))
txt = "\n".join(lines)
print(txt)
open(os.path.join(HB, "study1b", "retrieval_sizes.txt"), "w", encoding="utf-8").write(txt + "\n")
