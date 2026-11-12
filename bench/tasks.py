"""Replay task generation and the machine-readable answer key.

A replay task re-poses one historical study family's question as of the family's earliest date. The task statement is
built by template from the recorded hypothesis, the data available on that date and the recorded sample sizes; titles,
designs, results and record ids are never shown. The answer key comes from the automated adjudication.
"""
import collections
import hashlib
import json
import random
import re

from . import adjudicate, common

STRATA_QUOTA = {"supported": 16, "rejected": 16, "untestable": 16, "artifact": 16, "uncertain": 14}
PILOT_PER_STRATUM = 2
MAX_PER_CLUSTER = 2
MAX_ADAPTATION_SHARE = 0.20
NEAR_IDENTICAL_SIM = 0.60
MIN_CONFIDENCE = 0.5
MIN_PERMITTED_FOR_PILOT = 30
ADAPTATION_PROJECTS = {"Lineup Adaptation", "Team Adaptation", "Lineup/Team Adaptation"}
LINEUP_ADAPTATION_PROJECTS = {"Lineup Adaptation", "Lineup/Team Adaptation", "When a Hub Sits (Paper 2) / Lineup Adaptation"}

COMMON_ACRONYMS = {"NBA", "PPP", "NCAA", "RAPM", "PNR", "ORTG", "DRTG", "FG", "FGA", "EPV", "OT", "MDE", "CI", "RTM", "XFG",
                   "BPM", "ESPN", "TOV", "FT", "EFG", "TS", "PER", "USG", "AST", "REB", "PTS", "LLM", "AI", "ROC", "AUC",
                   "OLS", "DID", "SE", "SD", "AND", "OR", "NOT", "H1", "H2", "Q1", "Q2", "Q3", "Q4", "PO", "RS", "US", "ID"}
NUM_RE = re.compile(r"(?<![\w.])[-+−]?\d*\.\d+|\b\d{3,}\b")
GLOSSARY = {"PNR", "DRIVE", "CUT", "SPOT_UP", "PULL_UP", "POST_UP", "PUTBACK", "TRANSITION", "BEST", "AVOID", "L_pre",
            "D_real", "H1", "H2", "RS", "PO", "PPP"}
PROJECT_TERMS = re.compile(r"\b(?:brittle\w*|absorption|cascade\w*|vacuity|signature|fingerprint distance|"
                           r"net[ _]swing|alpha blend|kernel|playsheet|opener\w*|routing|routed|"
                           r"oracle|ceiling|regret|tier \d|w\d|z\d|design \d|gate \d|g\d)\b", re.I)
FLAGS = __import__("os").path.join(common.HB, "audit", "answer_key_flags.csv")

SEASONS = [
    ("NBA 2022-23 regular season and playoffs", "2026-03-01"),
    ("NBA 2023-24 regular season and playoffs", "2026-03-01"),
    ("NBA 2024-25 regular season and playoffs", "2026-03-01"),
    ("NBA 2025-26 regular season (complete from 2026-04-13; partial before)", "2026-03-01"),
    ("NBA 2025-26 playoffs (complete from 2026-06-21; partial before)", "2026-04-18"),
]
SOURCES = ("Per-game files from the NBA stats API: play-by-play (action type, sub-type, clock, period, score, player, "
           "shot distance and result), substitution rotation intervals, starters, defensive matchup minutes and partial "
           "possessions, box-score summary. Derived play-type possession records (initiator, play type, points) in a "
           "graph database built from the play-by-play.")


def jargon_terms(s):
    """Project-specific terms in a question that the glossary (tasks/glossary.md) does not define."""
    terms = set()
    for t in re.findall(r"\b[A-Za-z]+_[A-Za-z0-9_]+\b", s):
        terms.add(t)
    for t in re.findall(r"\b[A-Z][A-Z0-9]{1,}\b", s):
        if t not in COMMON_ACRONYMS and not t.isdigit():
            terms.add(t)
    for t in re.findall(r"\b(?:Design|Gate|Phase|Step|Test|Model|Variant|Stage) ?[0-9A-Z]\b|\b[A-Z][0-9]\b", s):
        terms.add(t)
    for t in re.findall(r"\b[a-z]+[A-Z][a-zA-Z]+\b", s):
        terms.add(t)
    terms |= {m.group(0).lower() for m in PROJECT_TERMS.finditer(s)}
    return sorted(t for t in terms if t not in GLOSSARY)


def load_flags(path=FLAGS):
    import csv
    import os
    if not os.path.exists(path):
        return {}
    return {r["study_family_id"]: r for r in csv.DictReader(open(path, encoding="utf-8-sig")) if r.get("action") == "exclude"}


def distinctive_numbers(s):
    out = set()
    for n in NUM_RE.findall(s or ""):
        n = n.replace("−", "-").lstrip("+-")
        n = "0" + n if n.startswith(".") else n
        if len(n.replace(".", "").lstrip("0")) >= 2:
            out.add(n)
    return out


def is_adaptation(fam_row, cluster_label, by_id):
    reps = [by_id[m] for m in fam_row["members"].split("; ")]
    return (fam_row["topic"] == "In-game and series adaptation" or any(r.get("project") in ADAPTATION_PROJECTS for r in reps)
            or "adapt" in cluster_label)


def data_available(task_date, project, dataset_tags):
    seasons = [s for s, avail in SEASONS if avail <= task_date]
    if project in LINEUP_ADAPTATION_PROJECTS:
        seasons = [s for s in seasons if "2025-26" not in s]
    lines = list(seasons)
    if any("NCAA" in t for t in dataset_tags):
        lines = ["NCAA men's and women's tournament results, seeds and public team ratings for past tournaments"]
    return lines


def sizes_hint(records):
    s = " ".join(common.text(r, "design", "power_info") for r in records)
    pats = [r"\bn\s?=\s?[\d,]+(?:\s+[a-z-]+){0,2}",
            r"[\d,]{2,}\s+(?:team-seasons|spells|series|games|possessions|players|pairs|stoppages|events|windows|teams|seasons|lineups|stints|shots|cases|triggers|clusters)"]
    hits = []
    for p in pats:
        for m in re.findall(p, s, re.I):
            if m.strip() not in hits:
                hits.append(m.strip())
    return hits[:4]


def statement(hypothesis, task_date, topic, data_lines, sizes):
    lines = [f"Research question (as posed on {task_date}, in the area of {topic.lower()}):", hypothesis.strip(), "",
             "Data available on that date:"] + [f"- {d}" for d in data_lines] + [f"- Sources: {SOURCES}"]
    if sizes:
        lines.append("- Units available to a study of this question (as recorded): " + "; ".join(sizes))
    lines += ["", "Your job is to decide, before any analysis is run, whether this question can be answered with this data, "
              "what has already been established about it, which methodological and statistical risks threaten a test of it, "
              "and either a pre-registration-quality design or a reasoned recommendation not to proceed."]
    return "\n".join(lines)


def learned_text(a, decider):
    st, ev = a["automated_stratum"], (decider.get("failure_evidence") or "").strip()
    res, pw = (decider.get("primary_result") or "").strip(), (decider.get("power_info") or "").strip()
    if st == "supported":
        return f"The recorded test supported the hypothesis: {res} Validation: {a['validation_status'].replace('_', ' ')}."
    if st == "rejected":
        return (f"An adequately powered test did not support the hypothesis as specified ({pw}). This rules out the effect "
                f"for this design and data, not every related hypothesis. Result: {res}")
    if st == "untestable":
        return f"The available data could not support a test of this question: {ev or res}"
    if st == "artifact":
        return f"The apparent result was produced by an artifact: {ev or res}"
    return f"The test did not settle the question ({a['automated_substatus']}): {ev or res}"


UNRESOLVED_RE = re.compile(r"[^.;]*(?:cannot|can't|untested|not tested|remains?|open|future|would need|needs?|unclear|"
                           r"not separable|cannot separate|underpowered|too few)[^.;]*", re.I)


def unresolved_text(a, ms):
    hits = []
    for r in ms:
        for m in UNRESOLVED_RE.findall(" ".join(str(r.get(f) or "") for f in ("notes", "power_info", "failure_evidence"))):
            m = m.strip()
            if len(m) > 15 and m not in hits:
                hits.append(m)
    if a["automated_stratum"] == "rejected":
        hits.append("Hypotheses with other units, data or effect definitions were not tested by this family.")
    if a["automated_stratum"] == "supported" and a["validation_status"] != "independent_validation_claimed":
        hits.append("No independent replication is recorded.")
    return hits[:5]


def generate(records, family_of, members, kind, adj_rows, cluster_rows, overlap_rows, dup_rows, cal, seed=20261110):
    """Return (pool_rows, answer_key, frozen_tasks). pool_rows includes excluded families with reasons."""
    by_id = {r["id"]: r for r in records}
    adj = {a["study_family_id"]: a for a in adj_rows}
    cl = {r["study_family_id"]: r for r in cluster_rows}
    probable_dup = collections.defaultdict(set)
    for o in overlap_rows:
        if o.get("overlap_class") == "probable_duplicate":
            probable_dup[o["family_a"]].add(o["family_b"])
            probable_dup[o["family_b"]].add(o["family_a"])
    shared_numbers = collections.defaultdict(int)
    for d in dup_rows:
        k = tuple(sorted((d["record_a"], d["record_b"])))
        shared_numbers[k] = max(shared_numbers[k], int(d["n_shared"]))
    from . import clusters as cmod
    fams, _, X = cmod.family_matrix(records, family_of, members)
    S = cmod.cosine(X)
    fidx = {f: i for i, f in enumerate(fams)}
    rng = random.Random(seed)
    flags = load_flags()
    pool, keys, frozen = [], [], {}
    for f in sorted(adj):
        a = adj[f]
        ms = [by_id[m] for m in members[f] if m in by_id]
        rep = by_id[a["representative"]]
        reasons = []
        if f in flags:
            reasons.append(f"answer-key screen: {flags[f]['flag']} ({flags[f]['screened_by']})")
        st = a["automated_stratum"]
        if st not in STRATA_QUOTA:
            reasons.append(f"stratum {st} is not one of the five task strata")
        if a["confidence"] < MIN_CONFIDENCE:
            reasons.append(f"automated adjudication confidence {a['confidence']} below {MIN_CONFIDENCE}")
        hyp = (rep.get("hypothesis") or "").strip()
        if len(hyp) < 30:
            reasons.append("hypothesis text missing or too short to pose a task")
        first = min(ms, key=lambda r: common.date_interval(r)[1])
        lo, hi, reliable = common.date_interval(first)
        task_date = hi if hi != "9999-12-31" else ""
        if not task_date:
            reasons.append("no date, so no chronological cutoff")
        tier = 1 if reliable and all(common.date_interval(r)[2] for r in ms) else 2
        project = rep.get("project", "")
        if project in LINEUP_ADAPTATION_PROJECTS and any("2025-26" in common.text(r, "design", "primary_result", "hypothesis") or
                                                         "2526" in common.text(r, "design", "primary_result") for r in ms):
            reasons.append("lineup-adaptation study that used 2025-26 data, which is excluded from that analysis")
        dtags = sorted({t for r in ms for t in common.tags(common.DATASET_RULES, common.text(r, "title", "hypothesis", "design", "project"))})
        topic = a["topic"]
        jt = jargon_terms(hyp)
        if topic == "Strategy engine and AI agent evaluation" and ("LLM or agent outputs" in dtags or len(jt) > 0):
            reasons.append("evaluates internal strategy-app software that the task cannot describe")
        own_nums = set().union(*(distinctive_numbers(r.get("primary_result")) for r in ms)) if ms else set()
        leaked = sorted(distinctive_numbers(hyp) & own_nums)
        if leaked:
            reasons.append("hypothesis text contains the family's own result numbers: " + ", ".join(leaked[:4]))
        # permitted memory and disclosure screening
        member_ids = {r["id"] for r in ms}
        permitted, removed = [], collections.Counter()
        for r in records:
            if r["id"] in member_ids:
                continue
            if not task_date or common.date_interval(r)[1] >= (common.date_interval(first)[0] if reliable else task_date):
                removed["not certainly before the task date"] += 1
                continue
            if set(common.ID_RE.findall(common.text(r, "related", "notes").upper())) & member_ids:
                removed["cites the task family"] += 1
                continue
            if family_of[r["id"]] in probable_dup.get(f, set()):
                removed["probable duplicate of the task family"] += 1
                continue
            if any(shared_numbers.get(tuple(sorted((r["id"], m))), 0) >= 3 for m in member_ids):
                removed["shares 3 or more distinctive result numbers with the task family"] += 1
                continue
            permitted.append(r["id"])
        perm_fams = sorted({family_of[x] for x in permitted})
        near = [g for g in perm_fams if f in fidx and g in fidx and S[fidx[f], fidx[g]] >= NEAR_IDENTICAL_SIM]
        if near:
            reasons.append("answer disclosed: permitted memory holds a near-identical earlier family (" + ", ".join(near) + ")")
        prior_same_q = [g for g in perm_fams if (cl.get(g, {}).get("cluster_id") == cl.get(f, {}).get("cluster_id"))
                        or (f in fidx and g in fidx and S[fidx[f], fidx[g]] >= cal["repeat_similarity"])]
        adapt = is_adaptation(a | {"members": a["members"]}, cl.get(f, {}).get("cluster_label_terms", ""), by_id)
        row = {"task_id": "", "study_family_id": f, "stratum": st, "confidence": a["confidence"],
               "confidence_level": a["confidence_level"], "topic": topic, "question_cluster": cl.get(f, {}).get("cluster_id", ""),
               "adaptation_group": "yes" if adapt else "no", "task_date": task_date, "date_tier": tier,
               "jargon_terms": "; ".join(jt), "self_contained": "yes" if not jt else "no",
               "permitted_records": len(permitted), "permitted_families": len(perm_fams),
               "memory_exclusions": "; ".join(f"{k}: {v}" for k, v in removed.items()),
               "prior_same_question_families": "; ".join(prior_same_q), "redundancy_subset": "yes" if prior_same_q else "no",
               "knowable_auto": a["knowable_auto"], "eligible": "no" if reasons else "yes",
               "exclusion_reasons": " | ".join(reasons), "selected_main": "no", "selected_pilot": "no", "selection_reason": "",
               "_priority": a["confidence"] + (0.3 if not jt else 0) + (0.2 if tier == 1 else 0) + rng.random() * 0.05}
        pool.append(row)
        if reasons:
            continue
        decider = by_id.get(a["deciding_record"]) or rep
        expected_risks = sorted(set(filter(None, a["risk_codes"].split("; "))))
        key = {
            "study_family_id": f, "stratum": st, "substatus": a["automated_substatus"], "outcome_status": a["outcome_status"],
            "failure_mechanism": a["failure_mechanism"], "testable": st != "untestable",
            "should_flag_before_running": st in ("untestable", "artifact"),
            "prior_same_question_families_in_memory": prior_same_q,
            "prior_same_question_strata": {g: adj[g]["automated_stratum"] for g in prior_same_q},
            "expected_risk_codes": expected_risks,
            "data_level_limitations": list(filter(None, a["data_level_limitations"].split("; "))),
            "design_level_limitations": list(filter(None, a["design_level_limitations"].split("; "))),
            "knowable_before_outcome_auto": a["knowable_auto"], "knowable_precedents": a["precedent_families"],
            "what_was_learned": learned_text(a, decider), "unresolved": unresolved_text(a, ms),
            "primary_result": decider.get("primary_result", ""), "failure_evidence": decider.get("failure_evidence", ""),
            "power_info": decider.get("power_info", ""), "validation_status": a["validation_status"],
            "confidence": a["confidence"], "confidence_level": a["confidence_level"], "decision_rule": a["decision_rule"],
            "conflicting_evidence": a["conflicting_evidence"], "member_records": [r["id"] for r in ms],
            "sources": [str(s) for r in ms for s in r.get("sources") or []],
            "answer_key_type": "automated from extracted records (rule-based adjudication); not independent human adjudication",
        }
        task = {"study_family_id": f, "task_date": task_date, "date_tier": tier, "topic": topic,
                "statement": statement(hyp, task_date, topic, data_available(task_date, project, dtags), sizes_hint(ms)),
                "permitted_records": permitted, "excluded_records": sorted(member_ids),
                "memory_exclusion_counts": dict(removed)}
        keys.append(key)
        frozen[f] = task
    select(pool)
    tid = {}
    n = 0
    for row in sorted(pool, key=lambda r: (r["eligible"] != "yes", r["stratum"], r["study_family_id"])):
        if row["eligible"] == "yes":
            n += 1
            tid[row["study_family_id"]] = f"RT-{n:03d}"
            row["task_id"] = tid[row["study_family_id"]]
    for k in keys:
        k["task_id"] = tid[k["study_family_id"]]
    out_tasks = {}
    for f, t in frozen.items():
        t["task_id"] = tid[f]
        body = json.dumps({k: t[k] for k in ("task_id", "statement", "permitted_records")}, sort_keys=True, ensure_ascii=False)
        t["task_hash"] = hashlib.sha256(body.encode("utf-8")).hexdigest()
        out_tasks[tid[f]] = t
    for row in pool:
        row.pop("_priority", None)
    return pool, sorted(keys, key=lambda k: k["task_id"]), out_tasks


def select(pool):
    """Balanced main set and pilot set, with caps per question cluster and on the adaptation group."""
    elig = sorted((r for r in pool if r["eligible"] == "yes"), key=lambda r: -r["_priority"])
    total = sum(STRATA_QUOTA.values())
    max_adapt = int(MAX_ADAPTATION_SHARE * total)
    per_cluster, n_adapt, taken = collections.Counter(), 0, collections.Counter()
    for r in elig:
        st = r["stratum"]
        if taken[st] >= STRATA_QUOTA[st]:
            r["selection_reason"] = "stratum quota full"
            continue
        if per_cluster[r["question_cluster"]] >= MAX_PER_CLUSTER:
            r["selection_reason"] = f"question cluster cap ({MAX_PER_CLUSTER}) reached"
            continue
        if r["adaptation_group"] == "yes" and n_adapt >= max_adapt:
            r["selection_reason"] = f"adaptation cap ({max_adapt}) reached"
            continue
        r["selected_main"] = "yes"
        r["selection_reason"] = "selected by priority (confidence, self-contained statement, reliable date)"
        taken[st] += 1
        per_cluster[r["question_cluster"]] += 1
        n_adapt += r["adaptation_group"] == "yes"
    state = {"cl": set(), "topic": collections.Counter(), "adapt": 0, "n": collections.Counter()}
    # Pass 0 applies every pilot criterion; later passes relax one criterion at a time for strata still short.
    relax_order = [(), ("topic spread",), ("topic spread", "high confidence"), ("topic spread", "high confidence", "self-contained")]
    for relaxed in relax_order:
        for r in elig:
            if r["selected_main"] != "yes" or r["selected_pilot"] == "yes" or state["n"][r["stratum"]] >= PILOT_PER_STRATUM:
                continue
            if r["date_tier"] != 1 or r["permitted_records"] < MIN_PERMITTED_FOR_PILOT or r["question_cluster"] in state["cl"]:
                continue
            if "self-contained" not in relaxed and r["self_contained"] != "yes":
                continue
            if r["confidence"] < (0.5 if "high confidence" in relaxed else 0.75):
                continue
            if "topic spread" not in relaxed and state["topic"][r["topic"]] >= 2:
                continue
            if r["adaptation_group"] == "yes" and state["adapt"] >= 1:
                continue
            r["selected_pilot"] = "yes"
            r["selection_reason"] += (f"; pilot: reliable date, at least {MIN_PERMITTED_FOR_PILOT} permitted records, distinct "
                                      "question cluster, at most one adaptation task"
                                      + (", relaxed: " + ", ".join(relaxed) if relaxed else
                                         ", self-contained, high confidence, at most two per topic"))
            state["n"][r["stratum"]] += 1
            state["cl"].add(r["question_cluster"])
            state["topic"][r["topic"]] += 1
            state["adapt"] += r["adaptation_group"] == "yes"
