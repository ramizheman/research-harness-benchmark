"""Automated scoring of agent outputs against the answer key.

Every function is deterministic. Scores that rest on text rules (risk codes, pre-registration rubric, redundancy
similarity) measure completeness and overlap, not scientific judgment; see automated_scoring_spec.md.
"""
import math
import re

from . import common

STRATA = ("supported", "rejected", "untestable", "artifact", "uncertain")
DECISIONS = ("proceed", "proceed_with_changes", "do_not_proceed")
DESIGN_FIELDS = ("estimand", "unit", "sample", "power", "controls", "falsification", "multiplicity", "decision_rule", "data_version")

OUTPUT_SCHEMA = {
    "testability": {"p_testable": "number in [0,1]: probability the question can be answered with the stated data at useful power",
                    "blocking_constraints": [{"code": "one of RISK_CODES", "text": "string"}]},
    "prior_work": {"already_answered": "yes | partly | no | unknown", "cited": ["identifiers of prior work relied on"],
                   "summary": "string"},
    "risks": [{"code": "one of RISK_CODES", "text": "string"}],
    "predicted_outcome": {s: "probability" for s in STRATA},
    "decision": "proceed | proceed_with_changes | do_not_proceed",
    "design": {f: "string" for f in DESIGN_FIELDS},
}


def validate_output(o):
    """Return a list of schema problems (empty when valid)."""
    p = []
    if not isinstance(o, dict):
        return ["output is not a JSON object"]
    t = o.get("testability", {})
    if not isinstance(t, dict) or not isinstance(t.get("p_testable"), (int, float)) or not 0 <= t.get("p_testable") <= 1:
        p.append("testability.p_testable missing or outside [0,1]")
    if o.get("decision") not in DECISIONS:
        p.append("decision must be one of " + ", ".join(DECISIONS))
    po = o.get("predicted_outcome")
    if not isinstance(po, dict) or not all(isinstance(po.get(s), (int, float)) for s in STRATA):
        p.append("predicted_outcome needs a number for each of " + ", ".join(STRATA))
    for r in o.get("risks", []) if isinstance(o.get("risks"), list) else []:
        if not isinstance(r, dict) or r.get("code") not in common.RISK_CODES:
            p.append(f"risk code {r.get('code') if isinstance(r, dict) else r!r} not in taxonomy")
    if not isinstance(o.get("design"), dict):
        p.append("design must be an object")
    return p


def outcome_probs(o):
    po = o.get("predicted_outcome") or {}
    raw = {s: max(0.0, float(po.get(s, 0) or 0)) for s in STRATA}
    tot = sum(raw.values())
    if tot <= 0:
        return {s: 1 / len(STRATA) for s in STRATA}
    return {s: v / tot for s, v in raw.items()}


def flagged(o):
    """The agent judged the work not worth running as posed."""
    pt = float((o.get("testability") or {}).get("p_testable", 1.0))
    pr = outcome_probs(o)
    return o.get("decision") == "do_not_proceed" or pt < 0.5 or (pr["untestable"] + pr["artifact"]) > 0.5


SPECIFIC = {
    "estimand": r"\b(?:difference|ratio|correlation|rho|effect|slope|share|rate|ppp|mean|odds|auc|coefficient)\b",
    "unit": r"\b(?:possession|game|player|team|season|spell|stint|lineup|pair|shot|series|trigger|matchup|quarter|half)s?\b",
    "sample": r"\d",
    "power": r"\d.*\b(?:power|mde|minimum detectable|detectable)\b|\b(?:power|mde|minimum detectable|detectable)\b.*\d",
    "controls": r"\b(?:control|matched|baseline|adjust|fixed effect|opponent|placebo)\w*",
    "falsification": r"\b(?:placebo|permutation|negative control|falsif|shuffle|holdout|held-out|out-of-sample|pre-period)\w*",
    "multiplicity": r"\b(?:holm|bonferroni|fdr|benjamini|single primary|one primary|no multiple)\w*",
    "decision_rule": r"(?:<|>|=|≥|≤|\bat least\b|\bexceed|\bbelow\b|\babove\b).*\d|\d.*(?:<|>|≥|≤)",
    "data_version": r"\b(?:20\d\d|season|snapshot|frozen|version|cutoff|as of)\b",
}


def prereg_score(design):
    """0, 1 or 2 per field: 0 empty or under 15 characters, 1 present, 2 present and specific (rule SPECIFIC)."""
    design = design if isinstance(design, dict) else {}
    items = {}
    for f in DESIGN_FIELDS:
        v = str(design.get(f) or "").strip()
        if len(v) < 15:
            items[f] = 0
        else:
            items[f] = 2 if re.search(SPECIFIC[f], v.lower()) else 1
    return items, sum(items.values()) / (2 * len(DESIGN_FIELDS))


def risk_scores(o, key):
    codes = {r.get("code") for r in (o.get("risks") or []) if isinstance(r, dict)}
    codes |= {r.get("code") for r in ((o.get("testability") or {}).get("blocking_constraints") or []) if isinstance(r, dict)}
    codes &= set(common.RISK_CODES)
    exp = set(key.get("expected_risk_codes") or [])
    recall = len(codes & exp) / len(exp) if exp else None
    return {"risk_codes_raised": sorted(codes), "risk_recall": recall, "risk_hits": len(codes & exp),
            "risk_expected": len(exp), "risk_codes_not_in_key": len(codes - exp)}


def redundancy_scores(o, key, condition):
    ans = str((o.get("prior_work") or {}).get("already_answered", "unknown")).lower()
    subset = bool(key.get("prior_same_question_families_in_memory"))
    recognized = ans in ("yes", "partly")
    return {"redundancy_subset": subset,
            "prior_work_recognized": recognized if subset else None,
            "false_prior_claim": (recognized if not subset else None) if condition != "A" else None}


def proposal_overlap(o, permitted_texts, vectorizer, threshold):
    """Max similarity of the proposed design to permitted memory records, and whether it reaches the repeat threshold."""
    d = o.get("design") or {}
    txt = " ".join(str(d.get(f) or "") for f in DESIGN_FIELDS)
    if not txt.strip() or not permitted_texts:
        return {"proposal_max_similarity": 0.0, "proposal_repeats_memory": False}
    X = vectorizer.transform([txt] + permitted_texts)
    sims = (X[0] @ X[1:].T).toarray().ravel()
    m = float(sims.max()) if len(sims) else 0.0
    return {"proposal_max_similarity": round(m, 3), "proposal_repeats_memory": m >= threshold}


def score_replay(o, key, condition, usage=None):
    """All automated replay scores for one run. o is the parsed final output (or None if the run failed)."""
    usage = usage or {}
    row = {"valid_output": False, "schema_problems": ""}
    if not isinstance(o, dict):
        row.update({"schema_problems": "no parseable output"})
        return row | usage
    probs = validate_output(o)
    row["valid_output"] = not probs
    row["schema_problems"] = "; ".join(probs)
    y = 1.0 if key["testable"] else 0.0
    pt = float((o.get("testability") or {}).get("p_testable", 0.5) or 0.5)
    pt = min(1.0, max(0.0, pt))
    pr = outcome_probs(o)
    f = flagged(o)
    items, pq = prereg_score(o.get("design"))
    row.update({
        "p_testable": pt, "testable_truth": int(y), "testability_brier": (pt - y) ** 2,
        "flagged": int(f), "should_flag": int(key["should_flag_before_running"]),
        "flag_correct": int(f == key["should_flag_before_running"]),
        "predicted_stratum": max(pr, key=pr.get), "stratum": key["stratum"],
        "outcome_log_loss": -math.log(max(0.01, pr[key["stratum"]])),
        "decision": o.get("decision"), "prereg_quality": round(pq, 3),
        **{f"prereg_{k}": v for k, v in items.items()},
    })
    row.update(risk_scores(o, key))
    row.update(redundancy_scores(o, key, condition))
    return row | usage
