# EXP:APPA-021 | Alpha blend of actual-usage and equilibrium predictions
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: val 690 cells (84,319 poss), holdout 520 cells (69,876 poss); alpha sweep raw and OLS-calibrated.
- hypothesis: Blending equilibrium with actual-usage prediction beats either alone.
- knowable_in_advance: no
- member_of: FAM:SF-APPA-021 {record=APPA-021; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: partial
- produced: RES:APPA-021 {record=APPA-021; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-020
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ALPHA_BLEND.md
- title: Alpha blend of actual-usage and equilibrium predictions
- uses_dataset: DS:Box_score_and_traditional_stats {record=APPA-021; rule=keyword rule DATASET_RULES}
- uses_method: METH:calibration_scoring {record=APPA-021; rule=keyword rule METHOD_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPA-021; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPA-021; rule=keyword rule METHOD_RULES}

# RES:APPA-021 | Result of APPA-021
- failure_evidence: Best alpha ~1.0, meaning 'equilibrium is NOT predictive' per pre-written cheat sheet.
- failure_type: B_powered_null
- power_info: 520 holdout cells
- primary_result: Best alpha = 1.00 (pure actual usage): R2 hol +0.0451 raw, +0.0672 calibrated; fullEQ R2 -0.1981.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
