"""Run Study 2 to completion without changing the runner.

Completed runs stay on disk, so a restart resumes. A run that stops on an API or runner error is moved to
runs/study2_v1/failed_attempts/ (the file is kept) and tried again, at most twice. The run is not restarted after
the $8 stop, an unknown cost, or a model-version mismatch. Writes study2/full_run.log.
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import time

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
RAW = os.path.join(HB, "runs", "study2_v1", "raw")
FAILED = os.path.join(HB, "runs", "study2_v1", "failed_attempts")
LOG = os.path.join(HB, "study2", "full_run.log")
CAP = 8.0
PLANNED = 816
MAX_RETRIES = 2


def log(msg):
    line = time.strftime("%Y-%m-%d %H:%M:%S") + " " + msg
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def runs():
    out = []
    for p in glob.glob(os.path.join(RAW, "*.json")):
        out.append((p, json.load(open(p, encoding="utf-8"))))
    return out


def spent_of(rows):
    spent, unknown = 0.0, False
    for _, r in rows:
        u = r.get("usage") or {}
        if u.get("cost_known") is False:
            unknown = True
        spent += u.get("cost_usd") or 0.0
    return spent, unknown


def main():
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    retries = {}
    while True:
        proc = subprocess.run([PY, os.path.join(HB, "scripts", "20_run_experiment.py"), "configs/study2.json",
                                "--confirm-spend", "--phase", "run"], cwd=HB)
        rows = runs()
        spent, unknown = spent_of(rows)
        log(f"runner exit {proc.returncode}; raw files {len(rows)}/{PLANNED}; spent ${spent:.4f}; unknown_cost {unknown}")
        if unknown:
            log("HALT: a run has unknown cost. Not restarting.")
            return 2
        if spent >= CAP:
            log("HALT: recorded spend reached the $8 stop. Not restarting and not raising the cap.")
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
            wait = 30 * max(retries.values())
            log(f"waiting {wait} seconds before resume")
            time.sleep(wait)


if __name__ == "__main__":
    sys.exit(main())
