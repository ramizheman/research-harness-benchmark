"""Characters of the first retrieve_history result per task in O and OS, and of read_family for each gold family.
Under fix 1 the scope_annotation characters in OS do not count against the 6,000-character tool-result cap, so the
counted length of an OS result equals the O length. "cut" is checked with the real 6,000 cap. No model calls.
Writes study1b/retrieval_sizes.txt.
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
CUT = "...[truncated]"


def sizes(snap, gold, call, args):
    full = {c: len(tools_v3.Toolbox3(c, snap, 10 ** 6, gold=gold, annotations=ANN).call(call, args)) for c in ("O", "OS")}
    cut = [c for c in ("O", "OS") if tools_v3.Toolbox3(c, snap, LIMIT, gold=gold, annotations=ANN).call(call, args).endswith(CUT)]
    return full, cut


lines = [f"limit {LIMIT} characters per tool result (budgets.max_tool_result_chars); fix 1: OS annotation characters",
         "are not counted, so the counted OS length equals O. 'O' = counted length; 'OS total' = length including annotations.", "",
         "first retrieve_history result", f"{'task':8s} {'gold':>4s} {'O':>6s} {'OS total':>8s}  status"]
for t, gold in GOLD.items():
    snap, _ = ensure_snapshot_v3(load_task(t))
    n, cut = sizes(snap, gold, "retrieve_history", REQ)
    lines.append(f"{t:8s} {len(gold):4d} {n['O']:6d} {n['OS']:8d}  " + ("cut: " + ", ".join(cut) if cut else "not cut"))
lines += ["", "read_family per gold family", f"{'task':8s} {'family':12s} {'O':>6s} {'OS total':>8s}  status"]
for t, gold in GOLD.items():
    if not gold:
        continue
    snap, _ = ensure_snapshot_v3(load_task(t))
    for f in gold:
        n, cut = sizes(snap, gold, "read_family", {"id": f})
        lines.append(f"{t:8s} {f:12s} {n['O']:6d} {n['OS']:8d}  " + ("cut: " + ", ".join(cut) + " (same place)" if cut else "not cut"))
txt = "\n".join(lines)
print(txt)
open(os.path.join(HB, "study1b", "retrieval_sizes.txt"), "w", encoding="utf-8").write(txt + "\n")
