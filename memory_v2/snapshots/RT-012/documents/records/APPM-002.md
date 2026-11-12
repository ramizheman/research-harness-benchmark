# EXP:APPM-002 | Top-player on/off features in calibrator
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Train-learned on/off deltas per top-N player, swept k_player shrinkage; val 690 cells, holdout 520 cells; compare R2_hol to 8-feat baseline +0.1150.
- hypothesis: Adding star on/off presence features (top-1 or top-3 players) improves holdout R2 over shipped 8-feature OLS.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPM-002 {record=APPM-002; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPM-002 {record=APPM-002; rule=record fields}
- project: Strategy app
- related_as_recorded: STARTER_SHARE.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ONOFF.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ONOFF_TOP1.md
- title: Top-player on/off features in calibrator
- uses_method: METH:calibration_scoring {record=APPM-002; rule=keyword rule METHOD_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPM-002; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPM-002; rule=keyword rule METHOD_RULES}

# RES:APPM-002 | Result of APPM-002
- failure_evidence: Holdout lift negative at every k (-0.0179 / -0.0285).
- failure_type: B_powered_null
- power_info: holdout 520 cells
- primary_result: top_n=3 best R2_hol +0.0971 (lift -0.0179); top_n=1 best R2_hol +0.0865 (lift -0.0285).
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
