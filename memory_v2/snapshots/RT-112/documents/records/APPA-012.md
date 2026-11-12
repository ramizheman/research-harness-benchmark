# EXP:APPA-012 | A4 five-player matchup model vs three-player A3
- date: 2026-04-15
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 240 matchups adversarial equilibrium comparison.
- hypothesis: Modeling 5 players per team improves equilibrium PPP over 3.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPA-012; rule=keyword rule VARIABLE_RULES}
- measures: VAR:three_point_attempts_or_luck {record=APPA-012; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-012 {record=APPA-012; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPA-012 {record=APPA-012; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-011
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT_V4.md
- title: A4 five-player matchup model vs three-player A3
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPA-012; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPA-012; rule=keyword rule METHOD_RULES}

# RES:APPA-012 | Result of APPA-012
- failure_evidence: A4-A3 -0.46 pts/100, no test reported.
- failure_type: E_unclear
- power_info: 240 matchups
- primary_result: A4 +1.61 vs A3 +2.06 pts/100; A4-A3 -0.46; A4 beats A3 87/240.
- record_stratum: uncertain
- record_substatus: inadequately tested: verdict null, mechanism E_unclear
- verdict: null
