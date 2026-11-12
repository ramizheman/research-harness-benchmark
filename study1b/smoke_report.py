"""Plumbing report for the Study 1b smoke test (runs/study1b_smoke_v1). Reads saved runs only; no model calls.
Reports validity, cost and logging fields. Does not report correctness against the answer key."""
import csv, glob, json, os

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HB, "runs", "study1b_smoke_v1")
ANN = json.load(open(os.path.join(HB, "study1b", "scope_annotations_frozen.json"), encoding="utf-8"))["annotations"]
scores = {r["run_id"]: r for r in csv.DictReader(open(os.path.join(OUT, "scores.csv"), encoding="utf-8-sig"))}
L, total = [], 0.0
for p in sorted(glob.glob(os.path.join(OUT, "raw", "*.json"))):
    r = json.load(open(p, encoding="utf-8"))
    s, u = scores[r["run_id"]], r.get("usage") or {}
    total += u.get("cost_usd") or 0.0
    tool_msgs = [m["content"] for m in r["messages"] if m["role"] == "user" and m["content"].startswith("TOOL_RESULT")]
    first = next(m for m in tool_msgs if m.startswith("TOOL_RESULT retrieve_history"))
    gold = r["oracle"]["gold"]
    L += [f"=== {r['task_id']} {r['condition']} seed {r['seed']}  ({os.path.basename(p)})",
          f"snapshot_fact_hash {r['snapshot_fact_hash'][:16]}  gold file {r['oracle']['gold_file_sha256'][:12]}  annotation file {r['oracle']['annotation_file_sha256'][:12]}",
          f"stop_reason {r['stop_reason']}  model_versions {r.get('model_versions')}  error {r.get('error') or 'none'}",
          f"tool calls: " + "; ".join(f"{t['name']}({json.dumps(t['args'], ensure_ascii=False)[:80]}) -> {t.get('returned_ids')} [{t['result_chars']} chars]" for t in r["tool_calls"]),
          f"retrieval first {s['retrieval_first']}  preliminary answers rejected {r.get('preliminary_answers', 0)}  gate turns {r.get('gate_turns', 0)}  repair turns {r.get('repair_turns', 0)}  correction turns {r.get('correction_turns', 0)}",
          f"families returned by first retrieval equal frozen gold: {r['tool_calls'][0]['returned_ids'] == ['FAM:' + f for f in gold]}",
          f"any tool result cut: {any('...[truncated]' in m for m in tool_msgs)}",
          f"annotation text present in first retrieval: " + ", ".join(f"{f} {json.dumps(ANN[f], ensure_ascii=False)[1:-1] in first}" for f in gold),
          f"valid_output {s['valid_output']}  schema problems {s.get('schema_problems') or 'none'}",
          f"cited ids {s['cited_ids']}",
          f"tokens {u.get('input_tokens')} in + {u.get('output_tokens')} out  cost_usd {u.get('cost_usd'):.6f}  cost_known {u.get('cost_known')}",
          ""]
L.append(f"total cost {total:.6f} USD over {len(scores)} runs; mean {total / len(scores):.6f} USD per run")
txt = "\n".join(L)
print(txt)
open(os.path.join(HB, "study1b", "smoke_report.txt"), "w", encoding="utf-8").write(txt + "\n")
