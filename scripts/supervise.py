"""Run a preregistered config to completion without changing the runner (generalised from study2/supervise_run.py).

Usage: python scripts/supervise.py configs/study1_embed.json
Completed runs stay on disk, so a restart resumes. A run that stops on an API or runner error is moved to
runs/<id>/failed_attempts/ (the file is kept) and tried again, at most twice. The run is not restarted after the spend
stop, an unknown cost, or a model-version mismatch. Writes runs/<id>/supervisor.log.
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import time

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from runner import experiment  # noqa: E402

CFG_PATH = sys.argv[1]
CFG = experiment.load_config(os.path.join(HB, CFG_PATH))
OUT = CFG["_out"]
RAW, FAILED, LOG = os.path.join(OUT, "raw"), os.path.join(OUT, "failed_attempts"), os.path.join(OUT, "supervisor.log")
CAP = experiment.spend_cap(CFG)
PLANNED = len(experiment.plan(CFG))
MAX_RETRIES = 2
PY = sys.executable


def log(msg):
    line = time.strftime("%Y-%m-%d %H:%M:%S") + " " + msg
    print(line, flush=True)
    os.makedirs(OUT, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def runs():
    return [(p, json.load(open(p, encoding="utf-8"))) for p in glob.glob(os.path.join(RAW, "*.json"))]


def main():
    retries = {}
    log(f"start {CFG['experiment_id']}: planned {PLANNED}, spend stop ${CAP}")
    while True:
        proc = subprocess.run([PY, os.path.join(HB, "scripts", "20_run_experiment.py"), CFG_PATH, "--confirm-spend",
                               "--phase", "run"], cwd=HB)
        rows = runs()
        spent = sum((r.get("usage") or {}).get("cost_usd") or 0.0 for _, r in rows)
        unknown = any((r.get("usage") or {}).get("cost_known") is False for _, r in rows)
        log(f"runner exit {proc.returncode}; raw files {len(rows)}/{PLANNED}; spent ${spent:.4f}; unknown_cost {unknown}")
        if unknown:
            log("HALT: a run has unknown cost. Not restarting.")
            return 2
        if CAP is not None and spent >= CAP:
            log(f"HALT: recorded spend reached the ${CAP} stop. Not restarting and not raising the cap.")
            return 0
        failed = [(p, r) for p, r in rows if r.get("stop_reason") in ("api_error", "error")]
        if len(rows) >= PLANNED and not failed:
            log("DONE: all planned runs are on disk.")
            return 0
        moved = False
        for p, r in failed:
            n = retries.get(r["run_id"], 0) + 1
            retries[r["run_id"]] = n
            if n > MAX_RETRIES:
                log(f"giving up after {n - 1} retries: {r['run_id']} ({r.get('error') or r.get('api_error')})")
                continue
            os.makedirs(FAILED, exist_ok=True)
            dest = os.path.join(FAILED, f"attempt{n}_" + os.path.basename(p))
            shutil.move(p, dest)
            log(f"retry {n}/{MAX_RETRIES}: {r['run_id']} kept at {dest}")
            moved = True
        if not moved:
            if proc.returncode == 0:
                log("HALT: runner stopped without a retryable error. Not restarting.")
                return 3
            log(f"runner crashed (exit {proc.returncode}); resuming in 60 seconds. Completed files are kept.")
            time.sleep(60)
        else:
            time.sleep(30 * max(retries.values()))


if __name__ == "__main__":
    sys.exit(main())
