"""Write the embedding-retrieval configs. Model settings are copied unchanged from configs/study1b.json (which copied
them from the Study 1 configs). Conditions B and C use bge-small-en-v1.5, 10 results per call, 14,000-character cap."""
import json, os
HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = json.load(open(os.path.join(HB, "configs", "study1b.json"), encoding="utf-8"))
by = {m["model"]: {k: v for k, v in m.items() if k != "conditions"} for m in src["models"]}
RET = {"method": "embedding", "model": "BAAI/bge-small-en-v1.5", "k": 10, "max_tool_result_chars": 14000}
s1_order = ["openai/gpt-oss-20b", "anthropic/claude-haiku-5.5", "gemini-2.5-flash", "deepseek/deepseek-v4-pro", "anthropic/claude-sonnet-5.5"]
s2_order = ["gemini-2.5-flash", "deepseek/deepseek-v4-pro", "anthropic/claude-haiku-5.5", "openai/gpt-oss-20b"]
s2tasks = [t["task_id"] for t in json.load(open(os.path.join(HB, "study2", "task_manifest.json"), encoding="utf-8"))["tasks"]]
common = {"protocol": 3, "retrieval": RET, "budgets": src["budgets"], "max_consecutive_errors": src["max_consecutive_errors"],
          "env_path": src["env_path"], "run_order": "model_then_seed"}
s1 = {"experiment_id": "study1_embed_v1",
      "note": "Study 1 rerun with embedding retrieval (prereg study1_embed/prereg.md). Conditions B and C only; A is unchanged and is taken from the original Study 1 runs. Same 10 tasks, seeds, models, settings, snapshots and scoring as Study 1.",
      **common, "models": [by[m] for m in s1_order], "tasks": src["tasks"], "conditions": ["B", "C"], "seeds": [1, 2, 3],
      "order_seed": 20261116, "budget_usd": 18.0, "stop_fraction": 0.8, "max_cost_usd": 14.4}
s2 = {"experiment_id": "study2_embed_v1",
      "note": "Study 2 with embedding retrieval (prereg study2/prereg_v2.md). Conditions A, B, O on the 68 Study 2 tasks, seed 1. B uses bge-small embeddings, 10 results.",
      **common, "task_dir": "study2/tasks", "snapshot_dir": "study2", "conditions": ["A", "B", "O"], "seeds": [1], "order_seed": 20261113,
      "oracle": {"gold_file": "study2/gold_families_frozen.json", "annotation_file": "study2/scope_annotations_none.json"},
      "models": [by[m] for m in s2_order], "tasks": s2tasks, "budget_usd": 14.0, "stop_fraction": 0.8, "max_cost_usd": 11.2}
sm1 = {**s1, "experiment_id": "study1_embed_smoke_v1", "note": "Smoke test, not analysed.", "models": [by["openai/gpt-oss-20b"]],
       "tasks": ["RT-147"], "seeds": [1], "max_cost_usd": 0.5}
sm1.pop("budget_usd"); sm1.pop("stop_fraction")
for n, c in (("study1_embed", s1), ("study2_embed", s2), ("study1_embed_smoke", sm1)):
    json.dump(c, open(os.path.join(HB, "configs", n + ".json"), "w", encoding="utf-8"), indent=1)
    print(n, len(c["models"]), "models", len(c["tasks"]), "tasks", len(c["conditions"]), "conditions")

