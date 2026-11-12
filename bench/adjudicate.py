"""Automated adjudication of study families.

This is rule-based automated adjudication of the extracted records. It is not independent human adjudication: every
output carries the rule that produced it, a heuristic confidence, a leave-one-member-out stability score, and the
conflicting member evidence verbatim.

Outcome status (what the test found) and failure mechanism (why) are kept in separate columns. The benchmark stratum
combines them with fixed rules (record_stratum).
"""
import collections
import re

from . import common

OUTCOME = {"supported": "supported", "null": "not_supported", "failed_gate": "not_supported", "reversed": "not_supported",
           "artifact_found": "artifact", "inconclusive": "inconclusive", "abandoned": "abandoned",
           "descriptive": "descriptive", "tool_eval_pass": "tool_evaluation", "tool_eval_fail": "tool_evaluation"}
STRATA = ("supported", "rejected", "untestable", "artifact", "uncertain")
ARTIFACT_WORDS = re.compile(r"artifact|leak|confound|\bbug|mechanical|base[- ]rate|regression to (?:the )?mean|\brtm\b|"
                            r"selection|circular|explained by|by construction|spurious|in-sample|look-?ahead|placebo (?:also|shows|matches)|"
                            r"disappears?|vanish(?:es|ed)?", re.I)
CORRECTION_WORDS = re.compile(r"correct(?:ed|ion)|fix(?:ed)?|after (?:the )?fix|robust to|survives|controlling for|balanced on|"
                              r"re-?run|re-?test", re.I)
INDEPENDENT_RE = re.compile(r"independent(?:ly)? (?:replicat|reanaly|data|sample|analyst)|external (?:data|replication|validation)|"
                            r"second analyst|different data source|replicated by|published replication", re.I)
SAME_PIPELINE_RE = re.compile(r"holdout|held-out|out-of-sample|\boos\b|loso|leave-one-season|prospective|replicat|split-half|"
                              r"cross-?fit|cross-?valid|placebo|permutation|robust|other seasons?|across seasons|second season|"
                              r"validation|frozen", re.I)
SCARCITY_RE = common.DATA_SCARCITY_RE


def number_rate(inv_row):
    try:
        n, f = int(inv_row.get("numbers_in_result") or 0), int(inv_row.get("numbers_found_in_sources") or 0)
    except ValueError:
        return None
    return f / n if n >= 2 and inv_row.get("numbers_check") == "checked" else None


def consistency_flags(r):
    v, ft = r.get("verdict"), r.get("failure_type")
    f = []
    if v == "supported" and ft != "D_positive":
        f.append(f"supported with mechanism {ft}")
    if ft == "D_positive" and OUTCOME.get(v) in ("not_supported", "artifact", "abandoned"):
        f.append(f"mechanism D_positive with verdict {v}")
    if v == "artifact_found" and ft != "C_artifact":
        f.append(f"artifact_found with mechanism {ft}")
    if ft == "C_artifact" and v != "artifact_found":
        f.append(f"mechanism C_artifact with verdict {v}")
    if ft == "B_powered_null" and not (r.get("power_info") or "").strip():
        f.append("B_powered_null without power_info")
    return f


def artifact_signal(r):
    if r.get("verdict") == "artifact_found":
        return True
    return r.get("failure_type") == "C_artifact" and bool(ARTIFACT_WORDS.search(common.text(r, "failure_evidence", "notes", "primary_result")))


def record_stratum(r):
    """(stratum, substatus) for one record. Strata: the five benchmark strata, or not_a_test / no_result."""
    v, ft, pw = r.get("verdict"), r.get("failure_type"), (r.get("power_info") or "").strip()
    if not (r.get("primary_result") or "").strip():
        return "no_result", "no primary_result recorded"
    if v in ("descriptive", "tool_eval_pass", "tool_eval_fail"):
        return "not_a_test", v
    if artifact_signal(r):
        return "artifact", "verdict artifact_found" if v == "artifact_found" else f"mechanism C_artifact with verdict {v}"
    if ft == "A_unanswerable":
        return "untestable", f"mechanism A_unanswerable with verdict {v}"
    if v == "supported":
        return "supported", "mechanism " + (ft or "missing")
    if OUTCOME.get(v) == "not_supported" and ft == "B_powered_null" and pw:
        return "rejected", f"verdict {v}, powered null with power information"
    if OUTCOME.get(v) in ("not_supported", "abandoned"):
        return "uncertain", f"inadequately tested: verdict {v}, mechanism {ft or 'missing'}" + ("" if pw else ", no power information")
    if v == "inconclusive":
        return "uncertain", "inconclusive"
    return "uncertain", f"unmapped verdict {v}"


def record_confidence(r, inv_row=None):
    c, why = 1.0, []
    if r.get("failure_type") == "E_unclear":
        c -= 0.3
        why.append("mechanism unclear (-0.3)")
    flags = consistency_flags(r)
    if flags:
        c -= 0.2
        why.append("verdict and mechanism inconsistent (-0.2)")
    rate = number_rate(inv_row or {})
    if rate is not None and rate < 0.5:
        c -= 0.2
        why.append(f"only {rate:.0%} of result numbers found in sources (-0.2)")
    if not (r.get("primary_result") or "").strip():
        c -= 0.5
        why.append("no primary_result (-0.5)")
    lo, hi, reliable = common.date_interval(r)
    if not reliable:
        c -= 0.05
        why.append("date is an upper bound only (-0.05)")
    return max(0.05, round(c, 2)), why


def level(c):
    return "high" if c >= 0.75 else ("medium" if c >= 0.5 else "low")


def resolve(member_records, kind):
    """Adjudicate one family. Returns dict with stratum, deciding record, rule and confidence multiplier."""
    st = {r["id"]: record_stratum(r) for r in member_records}
    tests = [r for r in member_records if st[r["id"]][0] in STRATA]
    if not tests:
        r0 = min(member_records, key=lambda r: (common.SLICE_RANK[r["id"].split("-")[0]], r["id"]))
        return {"stratum": st[r0["id"]][0], "decider": r0["id"], "rule": "R0 no member is a hypothesis test", "mult": 1.0}
    strata = {st[r["id"]][0] for r in tests}
    if len(tests) == 1 or len(strata) == 1:
        r0 = min(tests, key=lambda r: (common.SLICE_RANK[r["id"].split("-")[0]], r["id"]))
        rule = "R0 single record" if len(member_records) == 1 else "R1 all members agree"
        return {"stratum": st[r0["id"]][0], "decider": r0["id"], "rule": rule, "mult": 1.0 if len(member_records) == 1 else 1.05}
    if kind == "bundle":
        return {"stratum": "mixed", "decider": "", "rule": "R6 bundle: members test different sub-claims", "mult": 0.5}
    artifacts = [r for r in tests if st[r["id"]][0] == "artifact"]
    for a in artifacts:
        later_rescue = [r for r in tests if st[r["id"]][0] == "supported" and common.order(r, a) == "after"
                        and CORRECTION_WORDS.search(common.text(r, "design", "primary_result", "failure_evidence", "notes"))]
        if not later_rescue:
            others_before = all(common.order(r, a) == "before" for r in tests if r is not a and st[r["id"]][0] != "artifact")
            return {"stratum": "artifact", "decider": a["id"],
                    "rule": "R2 invalidation dominates: an artifact finding not followed by a corrected positive re-test",
                    "mult": 0.75 if others_before else 0.65}
    latest = [r for r in tests if all(common.order(r, o) == "after" for o in tests if o is not r)]
    if latest:
        return {"stratum": st[latest[0]["id"]][0], "decider": latest[0]["id"],
                "rule": "R3 latest member supersedes earlier members (date order certain)", "mult": 0.65}
    paps = [r for r in tests if r["id"].startswith("PAP-")]
    if paps:
        p = sorted(paps, key=lambda r: (r.get("date") or "", r["id"]))[-1]
        return {"stratum": st[p["id"]][0], "decider": p["id"], "rule": "R4 paper record takes precedence (date order uncertain)", "mult": 0.55}
    return {"stratum": "uncertain", "decider": "", "rule": "R5 unresolved conflict: members disagree and no rule applies", "mult": 0.4}


def stability(member_records, kind, final):
    if len(member_records) < 3:
        return ""
    same = sum(1 for i in range(len(member_records))
               if resolve(member_records[:i] + member_records[i + 1:], kind)["stratum"] == final)
    return round(same / len(member_records), 2)


NEGATION_RE = re.compile(r"\b(?:not|no|never|without|lacks?)\b(?:\s+\w+){0,3}\s*$", re.I)


def affirmed(pattern, s):
    """First match of pattern that is not negated within the three preceding words."""
    for m in pattern.finditer(s):
        if not NEGATION_RE.search(s[max(0, m.start() - 40):m.start()]):
            return m
    return None


def validation_status(member_records, kind, strata_agree):
    blob = [(r["id"], common.text(r, "design", "primary_result", "notes", "power_info", "failure_evidence")) for r in member_records]
    for rid, s in blob:
        m = affirmed(INDEPENDENT_RE, s)
        if m:
            return "independent_validation_claimed", f"{rid}: '{snippet(s, m)}'"
    for rid, s in blob:
        m = affirmed(SAME_PIPELINE_RE, s)
        if m:
            return "same_pipeline_validation", f"{rid}: '{snippet(s, m)}'"
    if kind == "repeat_runs_or_robustness" and strata_agree:
        return "same_pipeline_validation", "repeat runs of the design agree"
    return "no_validation_recorded", ""


def snippet(s, m, width=60):
    a, b = max(0, m.start() - width), min(len(s), m.end() + width)
    return re.sub(r"\s+", " ", s[a:b]).strip()


def limitation_profile(member_records):
    lims = sorted({t for r in member_records for t in common.tags(common.LIMIT_RULES, common.text(r, "power_info", "failure_evidence", "notes"))})
    risks = sorted({c for r in member_records for c in common.risk_codes(common.text(r, "failure_evidence", "power_info", "notes"))})
    data_level, design_level, unclear = [], [], []
    scarce = any(SCARCITY_RE.search(common.text(r, "power_info", "failure_evidence", "notes")) for r in member_records)
    for l in lims:
        if l in common.DATA_LEVEL_LIMITS or (l in ("small sample", "low power / large MDE") and scarce):
            data_level.append(l)
        elif l in common.DESIGN_LEVEL_LIMITS:
            design_level.append(l)
        else:
            unclear.append(l)
    if scarce and not data_level:
        data_level.append("data scarcity (text pattern)")
    return lims, risks, data_level, design_level, unclear


def adjudicate_all(records, family_of, members, kind, inv=None):
    """One row per study family. inv: inventory rows by id (for number-verification rates); optional."""
    inv = inv or {}
    by_id = {r["id"]: r for r in records}
    rows = []
    for f in sorted({family_of[r["id"]] for r in records}):
        ms = [by_id[m] for m in members[f] if m in by_id]
        k = kind.get(f, "single_record")
        res = resolve(ms, k)
        confs = {r["id"]: record_confidence(r, inv.get(r["id"])) for r in ms}
        dec = by_id.get(res["decider"])
        base = confs[dec["id"]][0] if dec else min(c for c, _ in confs.values())
        conf = max(0.05, min(1.0, round(base * res["mult"], 2)))
        st = {r["id"]: record_stratum(r) for r in ms}
        strata = sorted({s for s, _ in st.values()})
        agree = len({s for s, _ in st.values() if s in STRATA}) <= 1
        val, val_ev = validation_status(ms, k, agree)
        lims, risks, data_lv, design_lv, unclear_lv = limitation_profile(ms)
        conflict = [f"{r['id']}: {st[r['id']][0]} ({r.get('verdict')}/{r.get('failure_type')}): {(r.get('primary_result') or '')[:160]}"
                    for r in ms] if len(strata) > 1 else []
        rows.append({
            "study_family_id": f, "family_kind": k, "members": "; ".join(r["id"] for r in ms),
            "representative": common.representative([r["id"] for r in ms]),
            "topic": common.topic_of(by_id[common.representative([r["id"] for r in ms])]),
            "member_strata": "; ".join(f"{r['id']}={st[r['id']][0]}" for r in ms),
            "member_verdicts": "; ".join(f"{r['id']}={r.get('verdict')}" for r in ms),
            "member_mechanisms": "; ".join(f"{r['id']}={r.get('failure_type')}" for r in ms),
            "members_disagree": "yes" if len(strata) > 1 else "no",
            "automated_stratum": res["stratum"],
            "automated_substatus": st[dec["id"]][1] if dec else "",
            "outcome_status": OUTCOME.get(dec.get("verdict"), "") if dec else ("mixed" if res["stratum"] == "mixed" else "contested"),
            "failure_mechanism": dec.get("failure_type", "") if dec else "",
            "mechanism_votes": "; ".join(f"{m}={c}" for m, c in collections.Counter(r.get("failure_type") for r in ms).most_common()),
            "deciding_record": res["decider"], "decision_rule": res["rule"],
            "confidence": conf, "confidence_level": level(conf),
            "confidence_reasons": " | ".join(f"{rid}: {'; '.join(w)}" for rid, (c, w) in confs.items() if w),
            "leave_one_out_stability": stability(ms, k, res["stratum"]),
            "validation_status": val, "validation_evidence": val_ev,
            "limitation_tags": "; ".join(lims), "risk_codes": "; ".join(risks),
            "data_level_limitations": "; ".join(data_lv), "design_level_limitations": "; ".join(design_lv),
            "level_unclear_limitations": "; ".join(unclear_lv),
            "conflicting_evidence": " || ".join(conflict),
            "adjudication_type": "automated (rule-based); not independent human adjudication",
        })
    return rows


def knowability(adj_rows, records, family_of, members, cluster_of):
    """Recompute whether each failure's limitation was knowable before the outcome, using only earlier information.

    yes_from_history: a family that certainly finished earlier shares the question cluster or a data-level
      limitation and a dataset tag, and was itself untestable or an artifact for an overlapping reason.
    yes_from_history_probable: as above, but the earlier family precedes only by recorded point dates (at least one
      side is dated by file modification time, so the order is probable rather than certain).
    yes_from_data: the limitation is data-level and outcome-independent (counts, exposure, coverage, reliability),
      so it could have been computed from the data before running the test.
    no_evidence: neither condition holds. not_applicable: supported, rejected, mixed or non-test families.
    """
    by_id = {r["id"]: r for r in records}
    adj = {a["study_family_id"]: a for a in adj_rows}
    ds = {f: {t for m in members[f] if m in by_id for t in common.tags(common.DATASET_RULES, common.text(by_id[m], "title", "hypothesis", "design", "project"))}
          for f in adj}
    out = {}
    for f, a in adj.items():
        if a["automated_stratum"] not in ("untestable", "artifact", "uncertain"):
            out[f] = {"knowable_auto": "not_applicable", "knowable_basis": "", "precedent_families": ""}
            continue
        mine = [by_id[m] for m in members[f] if m in by_id]
        my_data = set(filter(None, a["data_level_limitations"].split("; ")))
        my_risk = set(filter(None, a["risk_codes"].split("; ")))
        prec, probable = [], []
        my_first = min((x.get("date") or "9999") for x in mine)
        for g, b in adj.items():
            if g == f or b["automated_stratum"] not in ("untestable", "artifact"):
                continue
            theirs = [by_id[m] for m in members[g] if m in by_id]
            certain = all(common.strictly_before(x, y) for x in theirs for y in mine)
            point = max((x.get("date") or "9999") for x in theirs) < my_first
            if not (certain or point):
                continue
            same_cluster = cluster_of.get(g) == cluster_of.get(f)
            shared_data = my_data & set(filter(None, b["data_level_limitations"].split("; "))) and ds[f] & ds[g]
            shared_risk = my_risk & set(filter(None, b["risk_codes"].split("; ")))
            if (same_cluster and (shared_risk or shared_data or b["automated_stratum"] == a["automated_stratum"])) or (shared_data and shared_risk):
                (prec if certain else probable).append(g)
        if prec:
            out[f] = {"knowable_auto": "yes_from_history", "knowable_basis": "earlier family (date order certain) with overlapping limitation",
                      "precedent_families": "; ".join(sorted(prec + probable)[:8])}
        elif probable:
            out[f] = {"knowable_auto": "yes_from_history_probable", "knowable_basis": "earlier family (by recorded point dates) with overlapping limitation",
                      "precedent_families": "; ".join(sorted(probable)[:8])}
        elif a["automated_stratum"] == "untestable" and my_data:
            out[f] = {"knowable_auto": "yes_from_data", "knowable_basis": "data-level limitation: " + a["data_level_limitations"],
                      "precedent_families": ""}
        else:
            out[f] = {"knowable_auto": "no_evidence", "knowable_basis": "", "precedent_families": ""}
    return out


MONTHS = {m: i + 1 for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                          "september", "october", "november", "december"])}


def mentioned_dates(s):
    """ISO dates and 'Month D' dates (year 2026 assumed) mentioned in text."""
    out = set(re.findall(r"\b(2026-\d{2}-\d{2})\b", s))
    for m, d in re.findall(r"\b(" + "|".join(MONTHS) + r")\s+(\d{1,2})\b", s.lower()):
        if 1 <= int(d) <= 31:
            out.add(f"2026-{MONTHS[m]:02d}-{int(d):02d}")
    return sorted(out)


def date_audit(records):
    bulk = collections.Counter((r.get("date"), r.get("date_basis")) for r in records if r.get("date_basis") == "mtime")
    rows = []
    for r in records:
        lo, hi, reliable = common.date_interval(r)
        issues = []
        d, basis = r.get("date") or "", r.get("date_basis") or ""
        if not d:
            issues.append("no date")
        if basis == "mtime":
            issues.append("file modification time: upper bound only")
            if bulk[(d, basis)] >= 8:
                issues.append(f"{bulk[(d, basis)]} records share this modification date (possible bulk edit or sync)")
        later = [x for x in mentioned_dates(common.text(r, "design", "primary_result", "notes", "failure_evidence")) if d and x > d]
        if later:
            issues.append("text mentions later date(s) " + ", ".join(later[:3]))
        rows.append({"experiment_id": r["id"], "date": d, "date_basis": basis, "interval_low": lo, "interval_high": hi,
                     "reliable": "yes" if reliable and not later else "no", "issues": "; ".join(issues)})
    return rows


def overlaps(records, family_of, members, fam_sim_pairs, dup_tsv_rows):
    """Cross-family overlap candidates: lexical similarity at repeat level and/or shared distinctive numbers."""
    num = collections.defaultdict(int)
    for d in dup_tsv_rows:
        a, b = family_of.get(d["record_a"]), family_of.get(d["record_b"])
        if a and b and a != b:
            key = tuple(sorted((a, b)))
            num[key] = max(num[key], int(d["n_shared"]))
    keys = set(num) | set(fam_sim_pairs)
    rows = []
    for k in sorted(keys):
        sim = fam_sim_pairs.get(k, 0.0)
        n = num.get(k, 0)
        signals = (sim > 0) + (n >= 3)
        rows.append({"family_a": k[0], "family_b": k[1], "lexical_similarity": round(sim, 3), "shared_numbers": n,
                     "overlap_class": "probable_duplicate" if signals == 2 else "possible_overlap",
                     "basis": "; ".join(x for x in (f"lexical similarity {sim:.2f} >= repeat threshold" if sim else "",
                                                    f"{n} shared distinctive numbers" if n else "") if x)})
    return rows
