"""Prospective challenge candidates for 2026-27, automated screening against the history, ranking and selection.

Candidates are research objectives, not hypotheses. Each names the data fields it needs from the per-game NBA stats API
files the project already collects. Unit counts per game are planning estimates; expected counts for the development
and validation periods use the share of regular-season games played by 31 January in 2024-25 (711 of 1,230).

Screening is automated.
  redundant          lexical similarity to some record >= the repeat threshold (median similarity of known same-study
                     records; a family's similarity is its most similar member)
  history-relevant   the challenge's design involves a risk type (LESSON_RULES) that at least MIN_LESSON_FAMILIES
                     untestable, artifact or uncertain families in the history carry as a recorded risk code
  history-irrelevant no such lesson applies
  adaptation flag    similarity to a lineup or in-game adaptation family at or above the cluster merge threshold
Lexical similarity alone cannot separate relevant from irrelevant challenges: the maximum over 384 records exceeds the
single-pair baseline for almost any basketball text, so relevance is defined by applicable lessons instead.
The generator's usefulness rating is a judgment by the model that wrote the candidates, recorded as such.
"""
import re

import numpy as np

from . import clusters, common

MIN_LESSON_FAMILIES = 3
LESSON_RULES = [
    ("MEASURE_RELIABILITY", r"stable|stability|reliab|trait|stabiliz"),
    ("EXPOSURE_SPARSITY", r"lineup|stint|\bunits?\b|bench|matchup|on the floor|on and off"),
    ("RTM_SELECTION", r"slump|scoring run|\bruns?\b|cold stretch|streak|after an extreme"),
    ("LABEL_ERROR", r"play type|from (?:play-by-play )?descriptions|drives?\b|label"),
    ("LEAKAGE_LOOKAHEAD", r"same-game|within the same game|in-game information"),
]

DEV_GAMES, VAL_GAMES = 711, 519
D0, D1, D2 = "2026-10-20", "2027-01-31", "2027-04-12"
FIELDS = {
    "pbp": "play-by-play actions (actionType, subType, clock, period, teamId, personId, scoreHome/scoreAway, shotDistance, xLegacy/yLegacy, shotResult, shotValue, description)",
    "rotation": "rotation intervals per player (in_time, out_time, player_pts, pt_diff)",
    "matchups": "defensive matchups (off/def player, matchup_minutes, partial_possessions, switches_on, player_points, fg_made, fg_attempted)",
    "summary": "box-score summary (game date, officials, attendance, national TV broadcaster, inactive players, line score)",
    "starters": "starters per team",
}

C = [
    ("PC-01", "Late-game free throws", "Measure whether players' free-throw accuracy in the final three minutes of close games differs from their own baseline, and whether any difference is a stable player trait.", ["pbp"], "free-throw attempts in close late-game situations", 3.0, 1200, 4, "A player-level difference that is reliable across halves of the development period and replicates in direction on validation data, or a well-powered null that bounds the effect.", "Correlate player-level late-game deviations between development and validation periods; report the bound if the correlation is indistinguishable from zero.", "Late-game free-throw pressure studies exist (clutch free throws); no project record studies free throws."),
    ("PC-02", "Foul trouble and rotations", "Quantify how coaches change a starter's minutes after two first-quarter fouls and the scoring margin cost of benching versus playing through.", ["pbp", "rotation"], "starter two-foul first-quarter events", 0.5, 250, 4, "An estimate of the margin difference between benching and playing through, with game-state controls, precise enough to rank the two policies.", "Apply the development-period estimate to validation events and test the sign with the registered model.", "Foul-trouble benching has public analyses (for example 'foul trouble' studies by analytics writers); the project history mentions foul trouble only in one opponent-attack question."),
    ("PC-03", "Back-to-back fatigue and shot quality", "Estimate how the second night of a back-to-back changes a team's shot distance profile and shooting efficiency, controlling for opponent and travel.", ["pbp", "summary"], "second-night team-games", 0.36, 150, 3, "A shift in shot location mix or efficiency on second nights that persists after opponent adjustment.", "Re-estimate on validation second nights with the frozen model; check the registered direction and interval.", "Rest and schedule-density effects are studied in public work; not in the project history."),
    ("PC-04", "Possession start type", "Measure points per possession by how the possession started (after a defensive rebound, live-ball turnover, made basket or dead ball) and how much teams differ in exploiting live-ball starts.", ["pbp"], "possessions", 200, 50000, 4, "Reliable team-level differences in live-ball-start efficiency that are not explained by overall offense.", "Split-half reliability within development; team ranking correlation between development and validation periods.", "Possession-start efficiency is a known public analysis (for example Inpredictable); the history studies play-type sequences, not start types."),
    ("PC-05", "Corner three allocation", "Describe which teams generate corner threes, from which actions, and whether corner-three share predicts later offensive efficiency beyond total three-point rate.", ["pbp"], "corner three attempts", 10, 3000, 3, "Incremental prediction of validation-period offensive rating by development-period corner share.", "Out-of-sample prediction of validation offensive rating with and without corner share.", "Corner three value is widely discussed publicly; not in the project history."),
    ("PC-06", "Officiating crews", "Estimate whether referee crews differ reliably in foul rates and free-throw rates after adjusting for teams and pace.", ["pbp", "summary"], "officiated games", 1.0, 400, 3, "Crew effects with split-half reliability above a pre-set level and a replicated ranking.", "Correlate crew effects between development and validation games.", "Referee tendencies and bias are studied publicly (for example Price and Wolfers); not in the project history."),
    ("PC-07", "Timeouts and scoring runs", "Estimate the effect of calling a timeout during an opponent scoring run on the next possessions, separating the timeout from regression after an extreme run.", ["pbp"], "opponent runs of 8-0 or more", 3.0, 1500, 4, "An estimate of the timeout effect that survives a matched comparison of runs with and without timeouts at the same run length and game state.", "Apply the frozen matching rule to validation runs; compare the registered estimate and interval.", "Timeout and momentum studies exist publicly; the history includes scoring-run and adaptation work with regression-to-the-mean lessons."),
    ("PC-08", "Hot hand with shot difficulty", "Estimate within-game shooting persistence after makes, controlling for shot distance and defender proximity proxies available in play-by-play.", ["pbp"], "consecutive shot pairs", 120, 60000, 2, "A persistence estimate with a bias correction for streak selection.", "Replicate on validation shot pairs with the frozen model.", "Heavily studied (Gilovich and colleagues; Miller and Sanjurjo); novelty is unlikely."),
    ("PC-09", "Rookie minutes and impact", "Track how rookie minutes evolve through the season and whether early on-court margin predicts later minutes and later margin.", ["rotation", "starters"], "rookie player-games", 6, 3000, 3, "A prediction of later minutes from early impact that beats a minutes-only baseline.", "Predict validation-period minutes with frozen development models.", "Player development curves are studied publicly; not in the project history."),
    ("PC-10", "Starting lineup changes", "Measure the first-quarter margin effect of a changed starting lineup relative to the team's usual starters.", ["starters", "rotation", "pbp"], "games with a changed starting five", 0.8, 400, 3, "An estimate of the starting-lineup change effect with opponent adjustment.", "Re-estimate on validation games; test the registered direction.", "Lineup studies are common; the history contains lineup exposure limits and on/off reliability lessons."),
    ("PC-11", "All-bench units", "Estimate how all-bench units perform relative to mixed units and whether the gap is a stable team trait.", ["rotation", "pbp"], "all-bench stints", 4, 2000, 3, "Reliable team-level bench-unit gaps that persist into validation.", "Correlate team bench gaps across periods.", "Bench-unit analyses exist publicly; the history has lineup exposure lessons."),
    ("PC-12", "Matchup difficulty for top scorers", "Measure how often top scorers are guarded by the opponent's best on-ball defender and how their efficiency varies with matchup difficulty.", ["matchups"], "top-scorer matchup rows", 30, 15000, 4, "A matchup-difficulty gradient in efficiency that holds out of sample.", "Fit on development matchups; test the gradient on validation matchups.", "Matchup data studies exist (for example defensive matchup difficulty metrics); the history has matchup and synergy work with exposure limits."),
    ("PC-13", "Switching and opponent efficiency", "Estimate how switch frequency in matchup data relates to opponent efficiency, team by team, and whether high-switch teams concede different shot types.", ["matchups", "pbp"], "team-game switch counts", 2, 1000, 4, "A relationship between switching and opponent shot mix that replicates.", "Re-estimate the team-level relationship on validation games.", "Switching analyses exist publicly; the history includes defensive scheme labeling work."),
    ("PC-14", "Heavy-minute players on back-to-backs", "Measure efficiency and minutes of players above 30 minutes per game on the second night of back-to-backs.", ["pbp", "rotation", "summary"], "player second-night games", 3, 1500, 3, "A per-player efficiency change with a credible interval on second nights.", "Replicate the pooled estimate on validation games.", "Load management studies exist publicly; not in the project history."),
    ("PC-15", "Fouling up three", "Estimate the win-probability value of intentionally fouling when leading by three in the final seconds.", ["pbp"], "late leading-by-three possessions", 0.05, 1000, 4, "An estimate of the value of fouling versus defending.", "Compare outcomes on validation situations.", "Published analyses exist on fouling up three; sample sizes are small."),
    ("PC-16", "Two-for-one possessions", "Measure how often teams take two-for-one shots at the end of quarters and the net points gained.", ["pbp"], "end-of-quarter two-for-one opportunities", 1.5, 800, 3, "A net points estimate with team-level variation.", "Replicate the net value on validation quarters.", "Public analyses of two-for-one value exist; not in the project history."),
    ("PC-17", "Early-season stabilization", "Determine how many games each team statistic needs before it predicts the rest of the season better than last season's value.", ["pbp", "summary"], "team-games", 2, 1000, 4, "A stabilization point per statistic with intervals.", "Use development games to estimate stabilization; test predictions against validation-period values.", "Stat stabilization is studied publicly; the history contains reliability analyses of team traits."),
    ("PC-18", "Coach's challenges", "Measure coach's challenge success rates by call type and game situation, and the value of the timeout lost on failure.", ["pbp"], "coach's challenges", 1.2, 600, 2, "A situational success model that predicts validation outcomes.", "Score the frozen model on validation challenges.", "Some public analysis of challenge success exists; not in the project history."),
    ("PC-19", "Starter return timing", "Describe when starters return after their first rest and whether earlier returns change the margin of the return stint.", ["rotation", "pbp"], "starter first-rest returns", 8, 4000, 3, "An association between return timing and stint margin robust to game state.", "Re-estimate on validation games with the frozen model.", "Rotation timing studies are uncommon publicly; the history includes lineup-change timing with a stoppage-unit lesson."),
    ("PC-20", "Rim protection on and off", "Estimate opponents' rim efficiency with and without each center on the floor, with shrinkage, and its reliability.", ["rotation", "pbp"], "opponent rim attempts", 30, 15000, 4, "Center rim-protection estimates with reliability above a pre-set level.", "Correlate development and validation estimates.", "Rim protection metrics exist publicly; the history contains on/off reliability lessons."),
    ("PC-21", "Shooting slumps and shot selection", "Measure whether players in a three-point slump change shot selection, separating behaviour from regression after selection on a cold stretch.", ["pbp"], "player slump spells", 1.5, 700, 3, "A change in three-point attempt share after slumps relative to matched non-slump spells.", "Apply the frozen matching rule to validation spells.", "Slump studies exist publicly; the history contains slump-triggered designs with regression-to-the-mean artifacts."),
    ("PC-22", "Late-game pace when trailing", "Measure how trailing teams change pace and shot selection in the fourth quarter and the efficiency cost.", ["pbp"], "fourth-quarter possessions by score state", 50, 25000, 2, "A pace and efficiency gradient by deficit.", "Replicate the gradient on validation games.", "Score-state effects are studied publicly; not in the project history."),
    ("PC-23", "Late-season defense stability", "Estimate how stable opponent-adjusted team defense is from the development to the validation period.", ["pbp"], "team-games", 2, 1000, 3, "A stability coefficient with interval.", "Directly measured on validation data.", "Defense stability is studied publicly; the history contains team-trait reliability work."),
    ("PC-24", "Assisted shot concentration", "Describe how concentrated each team's assists are among passers and whether concentration changes predict offensive efficiency changes.", ["pbp"], "assisted field goals", 50, 25000, 3, "A within-team association between assist concentration and efficiency that replicates.", "Re-estimate on validation games.", "Passing network studies exist publicly; the history contains structural influence work on initiations."),
    ("PC-25", "Attendance and home advantage", "Estimate whether crowd size (attendance) relates to home advantage after team quality adjustment.", ["summary", "pbp"], "home games", 1, 500, 3, "A dose-response estimate of attendance on home margin.", "Re-estimate on validation games.", "Crowd effects were studied publicly during and after empty-arena seasons; not in the project history."),
    ("PC-26", "Travel and early-game scoring", "Estimate whether cross-time-zone travel affects first-quarter scoring and shooting.", ["summary", "pbp"], "team-games after travel", 1, 500, 3, "A first-quarter effect of travel with opponent adjustment.", "Re-estimate on validation games.", "Travel and circadian effects are studied publicly; not in the project history."),
    ("PC-27", "Live-ball turnovers and transition", "Measure points off live-ball versus dead-ball turnovers and which teams convert live-ball turnovers best, reliably.", ["pbp"], "turnovers", 28, 14000, 3, "Reliable team conversion differences.", "Correlate team conversion rates across periods.", "Public analyses of turnover types exist; not in the project history."),
    ("PC-28", "Offensive rebounding trade-off", "Estimate the trade-off between crashing the offensive glass and allowing transition points, at team level.", ["pbp"], "missed shots", 80, 40000, 3, "A net value of offensive rebounding effort with interval.", "Replicate the team-level relationship on validation data.", "Public analyses of crash versus get-back exist; not in the project history."),
    ("PC-29", "Garbage-time definitions", "Measure how team net ratings change under different garbage-time definitions and which definition best predicts later results.", ["pbp"], "team-games", 2, 1000, 3, "A definition that improves validation-period prediction.", "Compare prediction of validation results under each frozen definition.", "Garbage-time filters are discussed publicly; the history excludes garbage time in several designs."),
    ("PC-30", "Score state and three-point rate", "Measure how leading teams change three-point attempt rate in the fourth quarter and whether it costs points.", ["pbp"], "fourth-quarter possessions", 50, 25000, 2, "A score-state effect on three-point rate and efficiency.", "Replicate on validation games.", "Score-state strategy is studied publicly; not in the project history."),
    ("PC-31", "Guard-on-center mismatches", "Measure how often switches leave guards on centers in matchup data and the scoring value of attacking those mismatches.", ["matchups"], "guard-on-center matchup rows", 6, 3000, 4, "A mismatch scoring premium that replicates.", "Re-estimate on validation matchups.", "Mismatch hunting is discussed publicly; the history has matchup and synergy work."),
    ("PC-32", "National TV games", "Estimate whether national TV games differ in foul rates, pace or star minutes after adjustment.", ["summary", "pbp", "rotation"], "national TV games", 0.25, 120, 2, "A difference with interval.", "Re-estimate on validation games.", "Little public analysis; not in the project history."),
    ("PC-33", "Second-chance points by rebounder", "Measure second-chance efficiency by the offensive rebounder's position and distance.", ["pbp"], "offensive rebounds", 22, 11000, 2, "Reliable differences by rebounder type.", "Replicate on validation data.", "Some public analysis exists; not in the project history."),
    ("PC-34", "Shooting fouls on threes", "Measure which players draw three-shot fouls and whether the skill is reliable.", ["pbp"], "three-point attempts", 75, 38000, 2, "A reliable player-level foul-drawing rate on threes.", "Correlate player rates across periods.", "Some public analysis exists; not in the project history."),
    ("PC-35", "Inactive stars and opponent strategy", "Estimate how opponents change shot mix when a team's leading scorer is inactive.", ["summary", "pbp"], "games with an inactive leading scorer", 0.4, 200, 3, "A change in opponent shot mix with interval.", "Re-estimate on validation games.", "The history studies absence and reorganization in depth."),
    ("PC-36", "Opening-possession plays", "Describe how teams use the first possession of each quarter and whether it scores better than average.", ["pbp"], "quarter-opening possessions", 8, 4000, 2, "A quarter-opening efficiency premium by team.", "Replicate on validation data.", "Little public analysis; the history includes opener rankings in the strategy app."),
    ("PC-37", "Minutes concentration", "Measure how concentrated teams' minutes are among their top eight players and whether concentration predicts later-season performance.", ["rotation"], "team-games", 2, 1000, 3, "A prediction of validation results from development concentration.", "Out-of-sample prediction.", "Some public discussion; not in the project history."),
    ("PC-38", "Clutch shot selection", "Describe shot selection in clutch time (final five minutes, margin of five or less) and its efficiency by shot type.", ["pbp"], "clutch possessions", 12, 6000, 3, "Efficiency differences by clutch shot type that replicate.", "Replicate on validation clutch possessions.", "Clutch studies are common publicly; the history includes clutch scripts."),
    ("PC-39", "Free-throw rate and drives", "Measure how much of each team's free-throw rate comes from drives, using play-by-play descriptions, and its stability.", ["pbp"], "drive possessions (from descriptions)", 40, 20000, 3, "Reliable team-level drive free-throw rates.", "Correlate across periods.", "Public drive statistics exist; the history includes play-type label quality lessons."),
    ("PC-40", "End-of-quarter heaves", "Measure how end-of-quarter heaves distort player three-point percentages and how often players avoid them.", ["pbp"], "end-of-quarter heave attempts", 1, 500, 1, "A correction to three-point percentage.", "Replicate on validation data.", "Known public observation; low decision value."),
]
CATEGORY = {"PC-01": "late game", "PC-15": "late game", "PC-16": "late game", "PC-22": "late game", "PC-30": "late game",
            "PC-38": "late game", "PC-40": "late game", "PC-02": "rotations", "PC-09": "rotations", "PC-10": "rotations",
            "PC-11": "rotations", "PC-19": "rotations", "PC-37": "rotations", "PC-03": "schedule and context",
            "PC-14": "schedule and context", "PC-25": "schedule and context", "PC-26": "schedule and context",
            "PC-32": "schedule and context", "PC-06": "officiating", "PC-18": "officiating", "PC-34": "officiating",
            "PC-04": "possession types", "PC-27": "possession types", "PC-28": "possession types", "PC-33": "possession types",
            "PC-36": "possession types", "PC-05": "shooting", "PC-08": "shooting", "PC-21": "shooting", "PC-39": "shooting",
            "PC-12": "defense and matchups", "PC-13": "defense and matchups", "PC-20": "defense and matchups",
            "PC-31": "defense and matchups", "PC-23": "measurement", "PC-17": "measurement", "PC-29": "measurement",
            "PC-07": "in-game decisions", "PC-24": "team structure", "PC-35": "team structure"}
KEYS = ("challenge_id", "theme", "objective", "data", "unit", "units_per_game", "required_validation_units", "generator_usefulness",
        "meaningful_finding", "validation_approach", "known_related_work")


def candidates():
    return [dict(zip(KEYS, c)) | {"category": CATEGORY[c[0]]} for c in C]


def screen(records, family_of, members, adj_rows, cal):
    """Add similarity, redundancy, relevance and feasibility to every candidate."""
    by_id = {r["id"]: r for r in records}
    adj = {a["study_family_id"]: a for a in adj_rows}
    rtexts = clusters.record_texts(records)
    cands = candidates()
    ctexts = [f"{c['theme']}. {c['objective']}. {c['unit']}" for c in cands]
    vec, Xr = clusters.vectorizer(rtexts)
    Xc = vec.transform(ctexts)
    R = (Xc @ Xr.T).toarray()
    low, mid, high = cal["other_p95"], cal["merge_similarity"], cal["repeat_similarity"]
    fams = sorted({family_of[r["id"]] for r in records})
    fam_col = {f: [i for i, r in enumerate(records) if family_of[r["id"]] == f] for f in fams}
    S = np.column_stack([R[:, fam_col[f]].max(axis=1) for f in fams])
    adaptation = {f for f in fams if adj[f]["topic"] == "In-game and series adaptation" or
                  any(by_id[m].get("project") in ("Lineup Adaptation", "Team Adaptation", "Lineup/Team Adaptation") for m in members[f] if m in by_id)}
    out = []
    for i, c in enumerate(cands):
        order = np.argsort(-S[i])[:5]
        near = [(fams[j], float(S[i, j])) for j in order]
        mx = near[0][1]
        ctext = " ".join([c["objective"], c["unit"], c["meaningful_finding"]]).lower()
        codes = [code for code, pat in LESSON_RULES if re.search(pat, ctext)]
        lessons, lesson_fams = [], []
        for code in codes:
            fs = [f for f in fams if code in adj[f]["risk_codes"].split("; ") and adj[f]["automated_stratum"] in ("untestable", "artifact", "uncertain")]
            if len(fs) >= MIN_LESSON_FAMILIES:
                lessons.append(f"{code} ({len(fs)} failed or uncertain families)")
                lesson_fams += sorted(fs, key=lambda f: -S[i, fams.index(f)])[:3]
        if mx >= high:
            rel, redundant = "redundant", True
        elif lessons:
            rel, redundant = "history-relevant", False
        else:
            rel, redundant = "history-irrelevant", False
        adapt_near = [f for f, s in near if f in adaptation and s >= mid]
        dev_units = c["units_per_game"] * DEV_GAMES
        val_units = c["units_per_game"] * VAL_GAMES
        feas = min(1.0, val_units / c["required_validation_units"]) * min(1.0, dev_units / c["required_validation_units"])
        score = round(feas * c["generator_usefulness"] / 5.0, 3)
        reasons = []
        if redundant:
            reasons.append(f"redundant with {near[0][0]} (similarity {mx:.2f} >= {high})")
        if adapt_near:
            reasons.append("close to lineup or in-game adaptation work (" + ", ".join(adapt_near) + ")")
        if feas < 0.5:
            reasons.append(f"infeasible: about {val_units:.0f} validation units for {c['required_validation_units']} required")
        if c["generator_usefulness"] <= 1:
            reasons.append("low decision value")
        out.append(c | {"data": "; ".join(FIELDS[d] for d in c["data"]), "data_sources": "; ".join(c["data"]),
                        "development_period": f"{D0} to {D1} (frozen at D1)", "validation_period": f"{D1} to {D2} (sealed until claims are registered)",
                        "expected_dev_units": round(dev_units), "expected_validation_units": round(val_units),
                        "feasibility": round(feas, 3), "max_history_similarity": round(mx, 3),
                        "nearest_families": "; ".join(f"{f} ({s:.2f})" for f, s in near),
                        "history_relation": rel, "history_lessons": "; ".join(lessons),
                        "history_lessons_from": "; ".join(dict.fromkeys(lesson_fams)),
                        "non_redundancy_basis": (f"highest similarity to any study family is {mx:.2f}, below the repeat threshold {high}"
                                                 if not redundant else "redundant"),
                        "score": score, "eligible": "no" if reasons else "yes", "exclusion_reasons": " | ".join(reasons),
                        "selected": "no", "selection_rationale": "", "usefulness_basis": "generator judgment (model that wrote the candidates); not independent"})
    return out


def select(rows, per_class=6, per_category=2):
    """Top candidates by score: per_class history-relevant and per_class history-irrelevant (weakly related as fallback),
    at most per_category from one category across the whole selection."""
    import collections
    used = collections.Counter()
    for cls, fallback in (("history-relevant", "history-weakly-related"), ("history-irrelevant", "history-weakly-related")):
        picked = 0
        for pool_cls in (cls, fallback):
            for r in sorted((x for x in rows if x["eligible"] == "yes" and x["history_relation"] == pool_cls and x["selected"] == "no"),
                            key=lambda x: (-x["score"], x["challenge_id"])):
                if picked >= per_class or used[r["category"]] >= per_category:
                    continue
                r["selected"] = "yes"
                r["selection_class"] = cls
                r["selection_rationale"] = (f"rank by score (feasibility x usefulness) within {cls}; at most {per_category} per category"
                                            + ("" if pool_cls == cls else f"; filled from {pool_cls} because {cls} had too few eligible"))
                used[r["category"]] += 1
                picked += 1
    for r in rows:
        r.setdefault("selection_class", "")
        if r["selected"] == "no" and r["eligible"] == "yes":
            r["selection_rationale"] = "eligible, not in the top of its class"
    return rows
