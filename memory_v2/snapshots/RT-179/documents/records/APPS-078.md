# EXP:APPS-078 | Channel 2: possession ending state vs next 90-180s volume/points
- date: 2026-06-16
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 911968 possessions. Baseline end state MADE_DEAD. Same-period clock windows.
- hypothesis: A possession's ending state changes opponent points/possessions in the next 90-180s beyond ~0.01-0.02 PPP boundary drift.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPS-078; rule=keyword rule VARIABLE_RULES}
- measures: VAR:turnovers {record=APPS-078; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-078 {record=APPS-078; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPS-078 {record=APPS-078; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-075
- related_to: EXP:APPS-075 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-078; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\channel2_volume.py
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\channel2_volume_analysis.md
- title: Channel 2: possession ending state vs next 90-180s volume/points
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-078; rule=keyword rule DATASET_RULES}

# RES:APPS-078 | Result of APPS-078
- failure_evidence: No inferential tests in the core table; live TO raising opponent possession count is largely definitional (steal starts a break).
- failure_type: E_unclear
- power_info: n=911968; MADE_DEAD n=354564
- primary_result: 90s vs MADE_DEAD: TURNOVER_LIVE dOppPts=+0.510 dNetPts=-0.306 (dOppPPP=+0.055, dOppPoss=+0.298); MISSED_DEAD dNetPts=-0.112; PUTBACK dNetPts=+0.078. Volume (dOppPoss), not PPP, carries most of the live-TO cost.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
