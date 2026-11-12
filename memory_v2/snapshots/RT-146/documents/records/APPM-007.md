# EXP:APPM-007 | Shot-quality (xPPP, team shot-making) features
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Add xPPP and team make-skill features to 8-feat OLS; holdout R2.
- hypothesis: Shot-zone expected PPP and team shot-making skill add signal beyond box-score features.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPM-007; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPM-007 {record=APPM-007; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: partial
- produced: RES:APPM-007 {record=APPM-007; rule=record fields}
- project: Strategy app
- related_as_recorded: STACK_FINAL.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SHOT_QUALITY.md
- title: Shot-quality (xPPP, team shot-making) features
- uses_dataset: DS:Box_score_and_traditional_stats {record=APPM-007; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Shot_level_data_with_expected_FG {record=APPM-007; rule=keyword rule DATASET_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPM-007; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPM-007; rule=keyword rule METHOD_RULES}

# RES:APPM-007 | Result of APPM-007
- failure_evidence: Lift +0.0054 below the +0.02 'real signal' threshold (doc: mostly absorbed).
- failure_type: B_powered_null
- primary_result: Best +xPPP only R2_hol +0.1204 (lift +0.0054); shot-skills -0.0003.
- record_stratum: uncertain
- record_substatus: inadequately tested: verdict null, mechanism B_powered_null, no power information
- verdict: null
