r"""List pairs of merged records whose primary results share distinctive numbers (candidate residual duplicates).

A number is distinctive if it has at least three significant digits after stripping sign and leading zeros
(for example 0.646, 1.522, 11,064). Pairs sharing at least two such numbers are printed for manual review.
"""
import itertools
import json
import os
import re

HB = r"C:\Users\lisas\OneDrive\Documents\Basketball\Research Harness Benchmark"
rows = [json.loads(l) for l in open(os.path.join(HB, "memory", "ledger_merged.jsonl"), encoding="utf-8")]


def sig(text):
    out = set()
    for m in re.findall(r"\d[\d,]*\.?\d*", text or ""):
        m = m.replace(",", "").rstrip(".")
        digits = m.replace(".", "").lstrip("0")
        if len(digits) >= 3 and not re.fullmatch(r"20[12]\d", m):
            out.add(m.lstrip("0") if "." in m else m)
    return out


S = {r["id"]: sig(r.get("primary_result", "")) for r in rows}
T = {r["id"]: r["title"] for r in rows}
pairs = []
for a, b in itertools.combinations(S, 2):
    common = S[a] & S[b]
    if len(common) >= 2:
        pairs.append((a, b, sorted(common)))
GENERIC = {"100", "240"}
with open(os.path.join(HB, "audit", "duplicate_candidates_raw.tsv"), "w", encoding="utf-8") as fh:
    fh.write("record_a\trecord_b\tn_shared\tshared_numbers\ttitle_a\ttitle_b\n")
    for a, b, c in pairs:
        if set(c) - GENERIC and len(set(c) - GENERIC) >= 2:
            fh.write(f"{a}\t{b}\t{len(c)}\t{','.join(c[:8])}\t{T[a][:70]}\t{T[b][:70]}\n")
strict = [(a, b, c) for a, b, c in pairs
          if len(set(c) - GENERIC) >= 3 and len(set(c) - GENERIC) >= 0.5 * min(len(S[a] - GENERIC), len(S[b] - GENERIC))]
parent = {i: i for i in S}


def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i


for a, b, _ in strict:
    parent[find(a)] = find(b)
cl = {}
for i in S:
    cl.setdefault(find(i), []).append(i)
clusters = sorted((sorted(v) for v in cl.values() if len(v) > 1), key=lambda v: v[0])
V = {r["id"]: r["verdict"] for r in rows}
for v in clusters:
    print(" + ".join(f"{i} [{V[i]}] {T[i][:60]}" for i in v))
print(len(pairs), "pairs sharing >=2 numbers;", len(strict), "strict pairs;", len(clusters), "clusters covering",
      sum(len(v) for v in clusters), "records; collapsing removes", sum(len(v) - 1 for v in clusters))
