# EXP:APPM-009 | More training seasons (fixed-holdout A/B)
- date: 2026-04-16
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Same 155 test games / 240 cells scored by both engines for A3, A5, A5b; raw and normalized variants.
- hypothesis: Training on 3 seasons instead of 2024-25 only improves prediction on a fixed late-2024-25 test set.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPM-009 {record=APPM-009; rule=audit/study_family_review.csv or singleton}
- n_runs: 2
- notes: Later recency weighting (half-life 0.5 seasons) adopted.
- prespecified: no
- produced: RES:APPM-009 {record=APPM-009; rule=record fields}
- project: Strategy app
- related_as_recorded: STRATEGY_V2_RESULTS recency weighting
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SEASON_COMPARISON_FIXED.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SEASON_COMPARISON_NORMALIZED.md
- title: More training seasons (fixed-holdout A/B)
- uses_method: METH:holdout_backtest_or_replay {record=APPM-009; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPM-009; rule=keyword rule METHOD_RULES}

# RES:APPM-009 | Result of APPM-009
- failure_evidence: 0/5 metric wins in both raw and normalized runs.
- failure_type: B_powered_null
- power_info: 240 cells, 120 pairs
- primary_result: After worse on 5/5 metrics: A3 R2 -0.0866 -> -0.2225 (normalized -0.2285); win-side accuracy 65.0% -> 48.3% (53.3% normalized).
- record_stratum: rejected
- record_substatus: verdict reversed, powered null with power information
- verdict: reversed
