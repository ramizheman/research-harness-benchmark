"""Merge the extraction slices into one record per experiment design.

Reads Research Ledger\\raw\\*.jsonl (read-only) and writes memory\\ledger_merged.jsonl.
Differences from Research Ledger\\scratch\\dedupe.py: a record whose `supersedes` equals its own id replaces the
earlier copy instead of removing both (that bug dropped 8 records from Research Ledger\\ledger.jsonl), and the
manual duplicate pairs below were added after reading the near-miss list.
"""
import collections
import glob
import json
import os
import re

BB = r"C:\Users\lisas\OneDrive\Documents\Basketball"
RAW = os.path.join(BB, "Research Ledger", "raw")
OUT = os.path.join(BB, "Research Harness Benchmark", "memory", "ledger_merged.jsonl")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

recs = []
for f in sorted(glob.glob(os.path.join(RAW, "*.jsonl"))):
    for k, line in enumerate(open(f, encoding="utf-8")):
        if line.strip():
            r = json.loads(line)
            r["_slice"] = os.path.basename(f)
            r["_order"] = (os.path.basename(f), k)
            recs.append(r)

latest = {}
for r in recs:
    if r["id"] not in latest or r.get("supersedes") == r["id"]:
        latest[r["id"]] = r
replaced = {r["supersedes"] for r in recs if r.get("supersedes") and r["supersedes"] != r["id"]}
superseded_by = {r["supersedes"]: r["id"] for r in recs if r.get("supersedes") and r["supersedes"] != r["id"]}
live = [r for i, r in latest.items() if i not in replaced]

STOP = set("a an the of to and or vs v in on for with from by its their that this is are was were be not no".split())


def tokens(r):
    t = (r.get("title", "") + " " + r.get("hypothesis", "")).lower()
    return {w for w in re.findall(r"[a-z0-9]{3,}", t) if w not in STOP}


def files(r):
    out = set()
    for s in r.get("sources") or []:
        for m in re.findall(r"[\w.\\/-]+\.(?:md|py|tex|csv|json|log|pdf|docx)", str(s), re.I):
            out.add(os.path.basename(m).lower())
    return out


tok = [tokens(r) for r in live]
fil = [files(r) for r in live]
parent = list(range(len(live)))


def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i


def union(i, j, why, log):
    a, b = find(i), find(j)
    if a != b:
        parent[a] = b
        log.append((live[i]["id"], live[j]["id"], why))


log = []
for i in range(len(live)):
    for j in range(i + 1, len(live)):
        inter = len(tok[i] & tok[j])
        jac = inter / (len(tok[i] | tok[j]) or 1)
        if (fil[i] & fil[j]) and jac >= 0.34:
            union(i, j, f"shared source file and title/hypothesis overlap {jac:.2f}", log)
        elif jac >= 0.62 and inter >= 5:
            union(i, j, f"title/hypothesis overlap {jac:.2f}", log)
by_id = {r["id"]: i for i, r in enumerate(live)}
MANUAL = [
    ("APPA-002", "CHT-019"), ("APPA-054", "APPS-040"), ("APPM-012", "APPS-016"), ("APPM-016", "APPS-006"),
    ("APPS-003", "CHT-021"), ("APPS-027", "CHT-046"), ("APPS-035", "CHT-043"), ("APPS-066", "CHT-031"),
    ("CHT-056", "PAP-006"), ("CHT-071", "TMP-015"), ("CHT-082", "PAP-078"), ("CHT-080", "PAP-054"),
    ("CHT-081", "PAP-085"), ("CHT-084", "PAP-082"), ("APPS-082", "APPM-047"), ("PAP-024", "APPM-047"),
    ("CHT-069", "PAP-069"),
]
for a, b in MANUAL:
    if a in by_id and b in by_id:
        union(by_id[a], by_id[b], "manual review of near-miss list", log)

groups = collections.defaultdict(list)
for i in range(len(live)):
    groups[find(i)].append(i)
ORDER = {"PAP": 0, "TMP": 1, "APPA": 2, "APPM": 3, "APPS": 4, "CHT": 5}


def rank(i):
    r = live[i]
    return (ORDER.get(r["id"].split("-")[0], 9), -len(r.get("primary_result") or ""), r["id"])


# Resampling counts recorded as runs; each is one execution of one design.
RUN_OVERRIDES = {
    "PAP-033": "500 is the number of split-half resamples, not independent runs",
    "PAP-070": "200 is the number of shuffle placebo draws, not independent runs",
    "PAP-083": "200 is the number of placebo permutations, not independent runs",
}

kept = []
for members in groups.values():
    best = min(members, key=rank)
    rec = {k: v for k, v in live[best].items() if not k.startswith("_")}
    rec["slice_file"] = live[best]["_slice"]
    rec["also_recorded_as"] = sorted(live[i]["id"] for i in members if i != best)
    rec["supersedes_ids"] = sorted({live[best]["id"] if live[best].get("supersedes") == live[best]["id"] else "",
                                    live[best].get("supersedes", "")} - {""})
    n = int(rec.get("n_runs") or 1)
    rec["n_runs_recorded"] = n
    rec["n_runs"] = 1 if rec["id"] in RUN_OVERRIDES else n
    rec["n_runs_note"] = RUN_OVERRIDES.get(rec["id"], "")
    kept.append(rec)

with open(OUT, "w", encoding="utf-8") as fh:
    for r in sorted(kept, key=lambda r: r["id"]):
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(os.path.join(os.path.dirname(OUT), "merge_log.tsv"), "w", encoding="utf-8") as fh:
    fh.write("record_a\trecord_b\treason\n")
    for a, b, why in log:
        fh.write(f"{a}\t{b}\t{why}\n")
print(f"raw lines {len(recs)}; unique ids {len(latest)}; replaced by a newer id {len(replaced)}; "
      f"live {len(live)}; merged duplicates {len(live) - len(kept)}; designs {len(kept)}; "
      f"runs {sum(r['n_runs'] for r in kept)} (recorded {sum(r['n_runs_recorded'] for r in kept)})")
