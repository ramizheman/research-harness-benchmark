"""Write the four smoke-test raw outputs (final JSON as returned) to study1b/smoke_raw_outputs.md and print the
start of the OS first-retrieval tool result for RT-147, showing the scope_annotation field. No model calls."""
import glob, json, os

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HB, "runs", "study1b_smoke_v1", "raw")
L = ["# Study 1b smoke test: raw outputs", "", "Final outputs exactly as saved in runs/study1b_smoke_v1/raw. Not scored against the answer key or the predictions.", ""]
for p in sorted(glob.glob(os.path.join(OUT, "*.json"))):
    r = json.load(open(p, encoding="utf-8"))
    L += [f"## {r['task_id']} {r['condition']} seed {r['seed']}", "", f"File: `{os.path.relpath(p, HB)}`", "", "```json",
          json.dumps(r["final"], indent=1, ensure_ascii=False), "```", ""]
open(os.path.join(HB, "study1b", "smoke_raw_outputs.md"), "w", encoding="utf-8").write("\n".join(L))
print("chars per final output:", {os.path.basename(p)[-14:]: len(json.dumps(json.load(open(p, encoding="utf-8"))["final"])) for p in sorted(glob.glob(os.path.join(OUT, "*.json")))})
r = json.load(open(glob.glob(os.path.join(OUT, "*RT-147_OS_s1.json"))[0], encoding="utf-8"))
first = next(m["content"] for m in r["messages"] if m["content"].startswith("TOOL_RESULT retrieve_history"))
print(first[:900])
