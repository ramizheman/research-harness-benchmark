"""Record what conditions A, B and C return for every Study 1 task with fixed requests, plus the system prompts, so a
test can show the Study 1b changes leave them byte-identical. Run once on the pre-change code. No model calls.
Run with %TEMP%\\supp_audit_venv\\Scripts\\python.exe study1b\\make_abc_fixture.py
"""
import hashlib, json, os, sys

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from runner import agent, tools_v3
from runner.experiment import load_task, ensure_snapshot_v3

T = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]
REQ = {"research_concepts": ["play-type labels", "defensive adjustment"], "methodological_questions": ["is the sample large enough"],
       "query": "does the defense adjust after a play type is used heavily"}


def calls(cond, snap):
    tb = tools_v3.Toolbox3(cond, snap if cond != "A" else None, 6000)
    out = [tb.call("retrieve_history", REQ)]
    first = list(tb.last_ids)
    if cond in ("B", "C") and first:
        out.append(tb.call("read_family", {"id": first[0]}))
    if cond == "B":
        out.append(tb.call("search_documents", {"query": "label error"}))
    if cond == "C":
        out.append(tb.call("explore_graph", {"node_id": first[0] if first else "x"}))
    out.append(tb.call("read_family", {"id": "SF-CHT-025"}))
    return out, agent.system_prompt_v3(tb, 12)


fx = {}
for t in T:
    snap, _ = ensure_snapshot_v3(load_task(t))
    for c in "ABC":
        out, prompt = calls(c, snap)
        fx[f"{t}|{c}"] = {"calls_sha256": [hashlib.sha256(s.encode()).hexdigest() for s in out],
                          "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
fx["_stage"] = {"STAGE1": hashlib.sha256(agent.STAGE1.encode()).hexdigest(), "STAGE2": hashlib.sha256(agent.stage2_text().encode()).hexdigest(),
                "RETRIEVE_FIRST_V3": hashlib.sha256(agent.RETRIEVE_FIRST_V3.encode()).hexdigest()}
os.makedirs(os.path.join(HB, "tests", "fixtures"), exist_ok=True)
json.dump(fx, open(os.path.join(HB, "tests", "fixtures", "study1_abc_tool_outputs.json"), "w", encoding="utf-8"), indent=1)
print(len(fx) - 1, "task-condition fixtures written")
