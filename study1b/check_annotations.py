"""Leakage and fidelity check of the scope annotations. Read-only; no model calls.

fidelity  every number in an annotation appears in the family's own snapshot record
key       no shared word 5-gram with any answer-key text field of a task where the family is gold
held-out  no shared word 5-gram with the task family's own (held-out) records, from which the key was derived
terms     no task id, task-family id, or decision vocabulary (stop, proceed, flag, should, do_not_proceed, testable)
length    characters per annotation
"""
import json, os, re, sys

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import common
from runner.experiment import load_task, answer_key

ann = json.load(open(os.path.join(HB, "study1b", sys.argv[1] if len(sys.argv) > 1 else "scope_annotations_draft.json"), encoding="utf-8"))["annotations"]
gold = json.load(open(os.path.join(HB, "study1b", "gold_families_frozen.json"), encoding="utf-8"))["tasks"]
keys = answer_key()
records = {r["id"]: r for r in common.load_records()}
family_of, members, _, _ = common.load_families(list(records.values()))
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
TERMS = re.compile(r"\b(stop|stopp\w*|proceed\w*|flag\w*|should|do_not_proceed|testable|untestable)\b", re.I)


def words(s):
    return re.findall(r"[a-z0-9_]+", s.lower())


def grams(s, n=5):
    w = words(s)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def flat(v):
    return json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v


problems = 0
for f, text in ann.items():
    tasks = [t for t, fs in gold.items() if f in fs]
    t0 = tasks[0]
    node = next(json.loads(l) for l in open(os.path.join(HB, "memory_v3", "snapshots", t0, "graph", "graph_nodes.jsonl"), encoding="utf-8")
                if json.loads(l)["id"] == "FAM:" + f)
    rec = flat(node).replace(",", "")
    missing = [n for n in NUM.findall(text) if n.replace(",", "") not in rec]
    key_hits, held_hits, term_hits = [], [], [m.group(0) for m in TERMS.finditer(text)]
    for t in tasks:
        k, task = keys[t], load_task(t)
        key_hits += sorted(grams(text) & grams(" ".join(flat(v) for v in k.values())))
        own = " ".join(flat(records[m]) for m in members.get(task["study_family_id"], []) if m in records)
        held_hits += sorted(grams(text) & grams(own))
        term_hits += [x for x in (t, task["study_family_id"]) if x in text]
    bad = bool(missing or key_hits or held_hits or term_hits)
    problems += bad
    print(f"{'CHECK' if bad else 'ok   '} {f:12s} len={len(text):3d} tasks={','.join(tasks)}"
          + (f"\n      numbers not in record: {missing}" if missing else "")
          + (f"\n      5-grams shared with answer key: {key_hits}" if key_hits else "")
          + (f"\n      5-grams shared with held-out task-family records: {held_hits}" if held_hits else "")
          + (f"\n      terms: {term_hits}" if term_hits else ""))
print(f"\n{len(ann)} annotations; {problems} need a look; max length {max(len(x) for x in ann.values())}")
print("\nself-test: comparison texts are non-empty and a planted key phrase is caught")
for t in sorted(t for t, fs in gold.items() if fs):
    k, task = keys[t], load_task(t)
    kt = " ".join(flat(v) for v in k.values())
    own = " ".join(flat(records[m]) for m in members.get(task["study_family_id"], []) if m in records)
    planted = "Scope: " + " ".join(words(kt)[40:50])
    print(f"  {t}: key 5-grams {len(grams(kt))}, held-out 5-grams {len(grams(own))}, planted phrase caught {bool(grams(planted) & grams(kt))}")
