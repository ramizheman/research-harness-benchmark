"""Write configs/study1b_smoke.json from configs/study1b.json: Haiku only, RT-012 and RT-147, O and OS, seed 1.
Every other setting is copied unchanged. max_cost_usd 0.50 is the smoke test's hard cap; the $8 study stop
(budget_usd x stop_fraction) also applies, and the lower of the two is enforced before every run."""
import json, os

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(HB, "configs", "study1b.json"), encoding="utf-8"))
cfg.update({
    "experiment_id": "study1b_smoke_v1",
    "note": "Study 1b smoke test (prereg study1b/prereg_1b.md, Phase 3): plumbing check only, not scored against predictions. "
            "Derived from configs/study1b.json by study1b/make_smoke_config.py; Haiku settings unchanged.",
    "models": [m for m in cfg["models"] if m["model"] == "anthropic/claude-haiku-5.5"],
    "tasks": ["RT-012", "RT-147"],
    "seeds": [1],
    "max_cost_usd": 0.50,
})
assert len(cfg["models"]) == 1
json.dump(cfg, open(os.path.join(HB, "configs", "study1b_smoke.json"), "w", encoding="utf-8"), indent=1)
