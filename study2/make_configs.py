"""Write configs/study2.json and configs/study2_smoke.json. Model settings are copied unchanged from configs/study1b.json."""
import json
import os

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = json.load(open(os.path.join(HB, "configs", "study1b.json"), encoding="utf-8"))
by = {m["model"]: {k: v for k, v in m.items() if k != "conditions"} for m in src["models"]}
order = ["gemini-2.5-flash", "deepseek/deepseek-v4-pro", "anthropic/claude-haiku-5.5", "openai/gpt-oss-20b"]
tasks = [t["task_id"] for t in json.load(open(os.path.join(HB, "study2", "task_manifest.json"), encoding="utf-8"))["tasks"]]
base = {
    "protocol": 3, "task_dir": "study2/tasks", "snapshot_dir": "study2",
    "conditions": ["A", "B", "O"], "seeds": [1], "order_seed": 20261113, "run_order": "model_then_seed",
    "oracle": {"gold_file": "study2/gold_families_frozen.json", "annotation_file": "study2/scope_annotations_none.json"},
    "budgets": src["budgets"], "max_consecutive_errors": src["max_consecutive_errors"], "env_path": src["env_path"]}
full = {"experiment_id": "study2_v1",
        "note": "Study 2 (prereg study2/prereg.md). Conditions A, B, O on the 68 main replay tasks not used in Study 1 "
                "(study2/tasks), seed 1. Model settings copied unchanged from configs/study1b.json. Models run in config "
                "order (run_order model_then_seed), so a budget stop cuts gpt-oss first, then Haiku.",
        **base, "models": [by[m] for m in order], "tasks": tasks,
        "budget_usd": 10.0, "stop_fraction": 0.8, "max_cost_usd": 8.0}
smoke = {"experiment_id": "study2_smoke_v1",
         "note": "Study 2 smoke test: Haiku only, two Study 2 tasks, A, B and O, seed 1. Not part of the analysis.",
         **base, "models": [by["anthropic/claude-haiku-5.5"]], "tasks": ["RT-005", "RT-036"], "max_cost_usd": 0.50}
for name, c in (("study2.json", full), ("study2_smoke.json", smoke)):
    json.dump(c, open(os.path.join(HB, "configs", name), "w", encoding="utf-8"), indent=1)
    print("wrote configs/" + name, len(c["models"]), "models", len(c["tasks"]), "tasks")
