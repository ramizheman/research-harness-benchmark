r"""Run an experiment config through the phases run, blind, score and analyze.

Usage:
  python scripts\20_run_experiment.py configs\pilot_mock.json
  python scripts\20_run_experiment.py configs\pilot.json --confirm-spend       (real model calls; costs money)
  python scripts\20_run_experiment.py configs\pilot.json --phase analyze
Options: --phase all|run|blind|score|analyze, --limit N (at most N new runs).
Runs already on disk are skipped, so an interrupted run resumes where it stopped.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from runner import experiment  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("config")
ap.add_argument("--phase", default="all", choices=["all", "run", "blind", "score", "analyze"])
ap.add_argument("--limit", type=int)
ap.add_argument("--confirm-spend", action="store_true")
a = ap.parse_args()

cfg = experiment.load_config(a.config if os.path.isabs(a.config) else os.path.join(experiment.HB, a.config))
paid = [m for m in cfg["models"] if m["provider"] != "mock"]
if a.phase in ("all", "run"):
    if paid and not a.confirm_spend:
        sys.exit(f"config uses paid models ({', '.join(m['provider'] + ':' + m['model'] for m in paid)}); re-run with --confirm-spend")
    n = experiment.run_all(cfg, a.limit)
    print("new runs", n)
if a.phase in ("all", "blind"):
    print("blinded runs, redactions", experiment.blind(cfg))
if a.phase in ("all", "score", "analyze"):
    rows = experiment.score(cfg)
    print("scored runs", len(rows))
    if a.phase in ("all", "analyze"):
        res = experiment.analyze(cfg, rows)
        for c, s in res["summary_by_condition"].items():
            print(c, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in s.items()})
        print("report", os.path.join(cfg["_out"], "report.md"))
