"""Build and freeze the Study 2 task set. No model calls.

1. Checks that study2/gold.py reproduces the rule-proposed Study 1b gold lists on the ten Study 1 tasks.
2. Copies the 68 main replay tasks not used in Study 1 from tasks/replay (left untouched) to study2/tasks, removing
   permitted records that fail a study2/leakage_check.py rule, and recomputes the task hash.
3. Re-checks every Study 2 task and stops with an error if any rule is still violated.
4. Builds each task's memory_v3 snapshot under study2/memory_v3/snapshots.
5. Applies the Study 1b gold rule to each Study 2 snapshot.
Outputs: study2/tasks/RT-*.json, study2/gold_families_frozen.json, study2/gold_details.json,
study2/scope_annotations_none.json, study2/task_manifest.json, study2/build_report.md.

Usage: python study2/build_tasks.py
"""
import collections
import hashlib
import json
import os
import sys

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
sys.path.insert(0, os.path.join(HB, "study2"))
from bench import retrieval_audit as ra  # noqa: E402
from runner import experiment  # noqa: E402
import gold as gold_rule  # noqa: E402
import leakage_check  # noqa: E402

S2 = os.path.join(HB, "study2")
TASK_DIR = os.path.join(S2, "tasks")
CONTESTABLE_STRATA = {"uncertain": "all uncertain tasks are keyed proceed by convention (should_flag_before_running is true only "
                                   "for untestable and artifact); the convention RT-147 exposed in Study 1"}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def task_hash(t):
    body = json.dumps({k: t[k] for k in ("task_id", "statement", "permitted_records")}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def main():
    keys, ctx = experiment.answer_key(), ra.Context()

    proposed = json.load(open(os.path.join(HB, "study1b", "gold_families_proposed.json"), encoding="utf-8"))
    for t in sorted(leakage_check.STUDY1_TASKS):
        task = experiment.load_task(t)
        g = gold_rule.gold_for(task, keys[t], experiment.ensure_snapshot_v3(task)[0], ctx)
        want = [x["family"] for x in proposed[t]["gold"]]
        if [x["family"] for x in g["gold"]] != want:
            raise SystemExit(f"gold rule does not reproduce Study 1b on {t}: {[x['family'] for x in g['gold']]} vs {want}")
    print("gold rule reproduces the Study 1b rule-proposed lists on all ten Study 1 tasks")

    ck = leakage_check.Checker()
    ids = leakage_check.study2_task_ids()
    os.makedirs(TASK_DIR, exist_ok=True)
    new_tasks = {}
    for tid in ids:
        src = os.path.join(HB, "tasks", "replay", f"{tid}.json")
        t = json.load(open(src, encoding="utf-8"))
        if task_hash(t) != t["task_hash"]:
            raise SystemExit(f"{tid}: original frozen task fails its own hash")
        if tid not in keys or keys[tid]["study_family_id"] != t["study_family_id"]:
            raise SystemExit(f"{tid}: no matching answer-key entry")
        viol = ck.check(t)
        rm = leakage_check.records_to_remove(viol)
        reasons = {r: [c for c, vs in viol.items() if any(v.split(" [")[0] == r for v in vs)] for r in rm}
        n = {**t, "permitted_records": [r for r in t["permitted_records"] if r not in rm],
             "source_task_file": f"tasks/replay/{tid}.json", "source_task_hash": t["task_hash"],
             "study2_removed_records": {r: "; ".join(c) for r, c in reasons.items()}}
        n["task_hash"] = task_hash(n)
        left = ck.check(n)
        if left:
            raise SystemExit(f"{tid}: Study 2 task still violates {left}")
        new_tasks[tid] = n
        p = os.path.join(TASK_DIR, f"{tid}.json")
        if os.path.exists(p) and json.load(open(p, encoding="utf-8"))["task_hash"] != n["task_hash"]:
            raise SystemExit(f"{tid}: a different frozen Study 2 task already exists; delete it deliberately to rebuild")
        json.dump(n, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{len(new_tasks)} Study 2 tasks written; every exclusion rule passes")

    experiment.TASK_DIR, experiment.SNAPSHOT_DIR = TASK_DIR, S2
    golds, details, manifest = {}, {}, []
    for i, tid in enumerate(ids, 1):
        task = experiment.load_task(tid)
        snap, man = experiment.ensure_snapshot_v3(task)
        g = gold_rule.gold_for(task, keys[tid], snap, ctx)
        golds[tid] = [x["family"] for x in g["gold"]]
        details[tid] = g
        k = keys[tid]
        manifest.append({
            "task_id": tid, "study_family_id": task["study_family_id"], "task_date": task["task_date"], "stratum": k["stratum"],
            "outcome_status": k["outcome_status"], "should_flag_before_running": k["should_flag_before_running"],
            "confidence_level": k["confidence_level"],
            "contestable_key": CONTESTABLE_STRATA.get(k["stratum"], ""),
            "prior_same_question_in_memory": bool(k.get("prior_same_question_families_in_memory")),
            "knowable_precedents": bool(k.get("knowable_precedents")),
            "n_permitted_records": len(task["permitted_records"]), "removed_for_study2": task["study2_removed_records"],
            "task_hash": task["task_hash"], "source_task_hash": task["source_task_hash"],
            "snapshot_fact_hash": man["fact_hash"], "snapshot_n_facts": man.get("n_facts"),
            "answer_key_entry_sha256": hashlib.sha256(json.dumps(k, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest(),
            "gold_families": golds[tid], "gold_tiers": [x["tier"] for x in g["gold"]],
            "n_question_tier": g["n_question_tier"], "n_lesson_tier": g["n_lesson_tier"]})
        print(f"[{i}/{len(ids)}] {tid} {k['stratum']:10s} permitted={len(task['permitted_records'])} gold={golds[tid]}")

    gold_path = os.path.join(S2, "gold_families_frozen.json")
    json.dump({"note": "Study 2 gold families: study1b/gold_rule.md applied by study2/gold.py to each Study 2 memory_v3 snapshot. "
                       "Computed by code only; no model and no manual additions or deviations.", "tasks": golds},
              open(gold_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(details, open(os.path.join(S2, "gold_details.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    ann_path = os.path.join(S2, "scope_annotations_none.json")
    json.dump({"note": "Study 2 runs A, B and O only. Condition O never reads annotations; the runner requires the file.",
               "annotations": {}}, open(ann_path, "w", encoding="utf-8"), indent=1)
    files = {p: sha(os.path.join(HB, p)) for p in ("benchmark_answer_key.jsonl", "replay_task_pool.csv", "study1b/gold_rule.md",
                                                    "study2/gold.py", "study2/leakage_check.py", "study2/build_tasks.py",
                                                    "study2/gold_families_frozen.json", "study2/scope_annotations_none.json")}
    json.dump({"tasks": manifest, "file_sha256": files, "code_hash": experiment.code_hash()},
              open(os.path.join(S2, "task_manifest.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    st = collections.Counter(m["stratum"] for m in manifest)
    ng = collections.Counter(len(m["gold_families"]) for m in manifest)
    changed = [m for m in manifest if m["removed_for_study2"]]
    lines = ["# Study 2 task build", "", f"Tasks: {len(manifest)} (main replay set minus the ten Study 1 tasks). No model calls.", "",
             "Strata: " + ", ".join(f"{k} {v}" for k, v in sorted(st.items())) + ".",
             f"Should flag: {sum(m['should_flag_before_running'] for m in manifest)}; proceed: {sum(not m['should_flag_before_running'] for m in manifest)}.",
             f"Prior same-question family in memory: {sum(m['prior_same_question_in_memory'] for m in manifest)}.",
             f"Contestable keys (uncertain stratum): {sum(bool(m['contestable_key']) for m in manifest)}.",
             "Gold families per task: " + ", ".join(f"{k}: {v} tasks" for k, v in sorted(ng.items())) + ".", "",
             "## Tasks whose memory changed from tasks/replay", ""]
    lines += [f"- {m['task_id']}: removed {', '.join(f'{r} ({c})' for r, c in m['removed_for_study2'].items())}" for m in changed] or ["- none"]
    lines += ["", "## File hashes (sha256)", ""] + [f"- `{p}`: {h}" for p, h in files.items()]
    open(os.path.join(S2, "build_report.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
