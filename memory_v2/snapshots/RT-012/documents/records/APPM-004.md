# EXP:APPM-004 | Calibration variance diagnostic (matchup signal collapse)
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: 690 val / 520 holdout cells: variance ratios, slope test, drop-one and single-feature ablation, residual structure.
- hypothesis: The calibrated pipeline preserves enough variance and the matchup model pred_raw carries usable signal.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPM-004 {record=APPM-004; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPM-004 {record=APPM-004; rule=record fields}
- project: Strategy app
- related_as_recorded: Shrinkage sweep (SHRINKAGE_SWEEP.md)
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\VARIANCE_DIAG.md
- title: Calibration variance diagnostic (matchup signal collapse)
- uses_method: METH:ablation {record=APPM-004; rule=keyword rule METHOD_RULES}
- uses_method: METH:calibration_scoring {record=APPM-004; rule=keyword rule METHOD_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPM-004; rule=keyword rule METHOD_RULES}
- uses_method: METH:matched_control {record=APPM-004; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPM-004; rule=keyword rule METHOD_RULES}

# RES:APPM-004 | Result of APPM-004
- failure_evidence: pred_raw contributes ~0 (dR2 +0.0002); SHRINKAGE_SWEEP later showed the equilibrium optimizer collapses signal (R2 +0.004 vs +0.045 with actual usage).
- failure_type: C_artifact
- power_info: holdout 520 cells
- primary_result: pred_cal variance 3.9% of actual; pred_raw alone R2 +0.0042; dropping pred_raw changes R2 by +0.0002; team_mult alone +0.0392.
- record_stratum: artifact
- record_substatus: verdict artifact_found
- verdict: artifact_found
