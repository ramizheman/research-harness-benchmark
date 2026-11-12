# EXP:APPM-006 | Starter-share features in calibrator
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Add 2 OLS features (top-5 by train possessions) to shipped 6-feat calibrator; val 690 / holdout cells.
- hypothesis: Offensive/defensive starter-share features improve holdout R2.
- knowable_in_advance: unclear
- measures: VAR:play_type_share_mix {record=APPM-006; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPM-006 {record=APPM-006; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Ship threshold stated in doc.
- prespecified: partial
- produced: RES:APPM-006 {record=APPM-006; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\STARTER_SHARE.md
- title: Starter-share features in calibrator
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPM-006; rule=keyword rule DATASET_RULES}
- uses_method: METH:calibration_scoring {record=APPM-006; rule=keyword rule METHOD_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPM-006; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPM-006; rule=keyword rule METHOD_RULES}

# RES:APPM-006 | Result of APPM-006
- failure_evidence: Lift +0.0315 > +0.01 ship threshold.
- failure_type: D_positive
- primary_result: 8-feat R2_hol +0.1150 vs 6-feat +0.0835 (lift +0.0315).
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
