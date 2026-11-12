"""Record condition O's tool outputs (first retrieval and read_family for every gold family, under the 6,000-character
cap) before fix 1, so a test can show fix 1 leaves O byte-identical. No model calls.
Run with %TEMP%\\supp_audit_venv\\Scripts\\python.exe study1b\\make_o_fixture.py
"""
import hashlib, json, os, sys

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from runner import tools_v3
from runner.experiment import ensure_snapshot_v3, load_task

GOLD = json.load(open(os.path.join(HB, "study1b", "gold_families_frozen.json"), encoding="utf-8"))["tasks"]
REQ = {"query": "defensive adjustment"}


def o_calls(t):
    snap, _ = ensure_snapshot_v3(load_task(t))
    tb = tools_v3.Toolbox3("O", snap, 6000, gold=GOLD[t], annotations={})
    return [tb.call("retrieve_history", REQ)] + [tb.call("read_family", {"id": f}) for f in GOLD[t]]


if __name__ == "__main__":
    fx = {t: [hashlib.sha256(s.encode()).hexdigest() for s in o_calls(t)] for t in GOLD}
    json.dump(fx, open(os.path.join(HB, "tests", "fixtures", "study1b_o_tool_outputs.json"), "w", encoding="utf-8"), indent=1)
    print(len(fx), "tasks written")
