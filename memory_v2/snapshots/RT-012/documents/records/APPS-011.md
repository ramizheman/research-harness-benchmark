# EXP:APPS-011 | Regular season vs playoff PPP by play type (DRIVE over-prediction)
- date: 2026-05-08
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Team-level (team, PT, context) cells, min 30 poss, up to 25 teams.
- hypothesis: DRIVE PPP is materially higher in RS than playoffs, so an RS-calibrated optimizer over-recommends DRIVE.
- knowable_in_advance: no
- measures: VAR:PPP_points_per_possession {record=APPS-011; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-011 {record=APPS-011; rule=audit/study_family_review.csv or singleton}
- motivates: FOLLOW:APPS-011 {needs_review=yes; record=APPS-011; rule=text pattern motivate/follow-up/next step}
- n_runs: 1
- notes: Motivated the playoff DRIVE exclusion and a proposed playoff DSI offset.
- prespecified: no
- produced: RES:APPS-011 {record=APPS-011; rule=record fields}
- project: Strategy app
- related_as_recorded: SQ2 decision quality hit rate (DRIVE exclusion); Defensive style RS vs playoff
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_rs_vs_playoff_ppp.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\rs_vs_playoff_run.log
- title: Regular season vs playoff PPP by play type (DRIVE over-prediction)
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-011; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-011; rule=keyword rule DATASET_RULES}
- uses_method: METH:calibration_scoring {record=APPS-011; rule=keyword rule METHOD_RULES}

# FOLLOW:APPS-011 | Follow-on candidate from APPS-011
- status: candidate from text pattern; not curated
- text: Motivated the playoff DRIVE exclusion and a proposed playoff DSI offset.

# RES:APPS-011 | Result of APPS-011
- failure_evidence: DRIVE playoff PPP 0.286 below RS across 25 teams; top-10 teams all -0.30 to -0.43.
- failure_type: D_positive
- power_info: 25 teams, min 30 poss per cell; no CIs
- primary_result: DRIVE RS 1.198 vs PO 0.912 (-0.286, 25 teams); PNR -0.173; PULL_UP +0.301; others within -0.07.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
