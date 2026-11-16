"""Pre-compute and cache bge-small embeddings for every task snapshot used by the embedding-retrieval runs."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runner import experiment, tools_v3  # noqa: E402

t0, n = time.time(), 0
for path in ("configs/study1_embed.json", "configs/study2_embed.json"):
    cfg = experiment.load_config(os.path.join(experiment.HB, path))
    for tid in cfg["tasks"]:
        snap, _ = experiment.ensure_snapshot_v3(experiment.load_task(tid))
        for cond in ("B", "C"):
            tools_v3.Toolbox3(cond, snap, 14000, retrieval=cfg["retrieval"])
        n += 1
        print(n, path, tid, round(time.time() - t0), flush=True)
print("WARM DONE")
