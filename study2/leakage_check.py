"""Study 2: independent re-check of the memory-exclusion rules on the 68 main tasks not used in Study 1.

Re-derives every exclusion from the records rather than trusting the pool build, with two checks made stricter than
bench/tasks.py: a record "cites" the task family if a member id appears in any text field (the build looked at
related and notes only), and shared distinctive result numbers are counted over every record pair (the build used
the precomputed candidate list audit/duplicate_candidates_raw.tsv). Calendar years are not counted as distinctive.

Run directly to check the original snapshots in tasks/replay (writes study2/leakage_check.json and .md; exit code 1
if any original snapshot violates a check). study2/build_tasks.py imports Checker to enforce the same rules.
"""
import collections
import csv
import json
import os
import re
import sys

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HB)
from bench import common, tasks as btasks  # noqa: E402

STUDY1_TASKS = {"RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"}
TEXT_FIELDS = ("title", "hypothesis", "design", "primary_result", "failure_evidence", "power_info", "knowable_in_advance",
               "related", "notes", "also_recorded_as", "supersedes_ids")
RESULT_FIELDS = ("primary_result", "failure_evidence", "power_info")
YEAR_RE = re.compile(r"^(19|20)\d\d$")
MIN_SHARED = 3


def study2_task_ids():
    pool = list(csv.DictReader(open(os.path.join(HB, "replay_task_pool.csv"), encoding="utf-8-sig")))
    return sorted(r["task_id"] for r in pool if r["selected_main"] == "yes" and r["task_id"] not in STUDY1_TASKS)


def result_numbers(r):
    nums = set().union(*(btasks.distinctive_numbers(r.get(f)) for f in RESULT_FIELDS))
    return {n for n in nums if not YEAR_RE.match(n)}


def field_text(v):
    return " ".join(map(str, v)) if isinstance(v, list) else str(v or "")


class Checker:
    def __init__(self):
        records = common.load_records()
        self.by_id = {r["id"]: r for r in records}
        self.family_of, self.members, _, _ = common.load_families(records)
        self.probable_dup = collections.defaultdict(set)
        for o in csv.DictReader(open(os.path.join(HB, "audit", "overlap_candidates.csv"), encoding="utf-8-sig")):
            if o.get("overlap_class") == "probable_duplicate":
                self.probable_dup[o["family_a"]].add(o["family_b"])
                self.probable_dup[o["family_b"]].add(o["family_a"])
        self.nums = {r["id"]: result_numbers(r) for r in records}

    def check(self, t):
        """Violations of every exclusion rule in task t's permitted records, by check name."""
        f, viol = t["study_family_id"], collections.defaultdict(list)
        mem = set(self.members[f]) & set(self.by_id)
        if mem != set(t["excluded_records"]):
            viol["excluded records differ from the task family"].append(t["task_id"])
        if not t.get("task_date"):
            viol["no task date"].append(t["task_id"])
            return dict(viol)
        if len(set(t["permitted_records"])) != len(t["permitted_records"]):
            viol["duplicate permitted record ids"].append(t["task_id"])
        first = min((self.by_id[m] for m in mem), key=lambda r: common.date_interval(r)[1])
        lo, _, reliable = common.date_interval(first)
        cutoff = lo if reliable else t["task_date"]
        for rid in t["permitted_records"]:
            r = self.by_id.get(rid)
            if r is None:
                viol["unknown record id"].append(rid)
                continue
            if rid in mem or self.family_of[rid] == f:
                viol["own family"].append(rid)
            if common.date_interval(r)[1] >= cutoff:
                viol["not certainly before the task date"].append(rid)
            cited = {m: fld for fld in TEXT_FIELDS for m in set(common.ID_RE.findall(field_text(r.get(fld)).upper())) & mem}
            if cited:
                viol["cites the task family (any field)"].append(rid + " [" + ", ".join(f"{m} in {fld}" for m, fld in sorted(cited.items())) + "]")
            if self.family_of[rid] in self.probable_dup.get(f, set()):
                viol["probable duplicate family"].append(rid)
            n, m = max((len(self.nums[rid] & self.nums[m]), m) for m in mem)
            if n >= MIN_SHARED:
                viol[f"shares {MIN_SHARED}+ distinctive result numbers (all pairs)"].append(
                    f"{rid} [{n} with {m}: {', '.join(sorted(self.nums[rid] & self.nums[m])[:6])}]")
        return dict(viol)


def records_to_remove(viol):
    return sorted({v.split(" [")[0] for name, vs in viol.items() if name not in ("excluded records differ from the task family",
                                                                                 "no task date", "duplicate permitted record ids") for v in vs})


def main():
    ck, out, total = Checker(), {}, collections.Counter()
    for tid in study2_task_ids():
        t = json.load(open(os.path.join(HB, "tasks", "replay", f"{tid}.json"), encoding="utf-8"))
        viol = ck.check(t)
        rm = records_to_remove(viol)
        out[tid] = {"study_family_id": t["study_family_id"], "task_date": t["task_date"], "permitted_before": len(t["permitted_records"]),
                    "violations": viol, "records_to_remove": rm, "permitted_after": len(t["permitted_records"]) - len(rm)}
        for c, vs in viol.items():
            total[c] += len(vs)
    changed = {t: v for t, v in out.items() if v["violations"]}
    res = {"tasks_checked": len(out), "tasks_with_violations": sorted(changed), "violations_by_check": dict(total),
           "rules": {"text_fields_for_citing": TEXT_FIELDS, "result_fields_for_numbers": RESULT_FIELDS,
                     "min_shared_numbers": MIN_SHARED, "calendar_years_ignored": True}, "tasks": out}
    json.dump(res, open(os.path.join(HB, "study2", "leakage_check.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    lines = ["# Study 2 leakage re-check of the original snapshots (tasks/replay)", "",
             f"Tasks checked: {len(out)}. Tasks with at least one violation: {len(changed)}.", "",
             "| Check | Violations |", "|---|---|"] + [f"| {c} | {n} |" for c, n in sorted(total.items())] + [""]
    for tid, v in changed.items():
        lines.append(f"## {tid} ({v['study_family_id']}): {v['permitted_before']} -> {v['permitted_after']} permitted records")
        lines += [f"- {c}: " + "; ".join(vs) for c, vs in v["violations"].items()] + [""]
    open(os.path.join(HB, "study2", "leakage_check.md"), "w", encoding="utf-8").write("\n".join(lines))
    print("\n".join(lines))
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
