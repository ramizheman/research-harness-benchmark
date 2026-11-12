# EXP:APPS-034 | Oracle player-routing sensitivity (RS holdout)
- date: 2026-06-18
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: RS holdout BEST rows n>=5 (980). Ablate min_n gate and top-K rotation filter.
- hypothesis: Routing regret (+0.137 baseline) is not an artifact of low-volume bench oracles.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPS-034 {record=APPS-034; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Shrinkage prior weight=50 means n=3 H2H is ~94% league mean. PO oracle player tables flagged exploratory (typical n=3-8).
- prespecified: no
- produced: RES:APPS-034 {record=APPS-034; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-020; APPS-009
- related_to: EXP:APPS-009 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-034; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\oracle_sensitivity.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\rs_holdout_25_26\rs_player_routing_regret.md
- title: Oracle player-routing sensitivity (RS holdout)
- uses_method: METH:holdout_backtest_or_replay {record=APPS-034; rule=keyword rule METHOD_RULES}

# RES:APPS-034 | Result of APPS-034
- failure_evidence: Regret shrinks under stricter gates but stays positive; recommended cite is +0.094 not +0.137.
- failure_type: E_unclear
- power_info: n=980 BEST rows baseline
- primary_result: Baseline min_n=3: regret +0.137, 63.0% oracle>actual, n=980. min_n=20: +0.050, 52.5%, n=703. Recommended top-8 + min_n=5: +0.094, 57.9%, n=970. Strict top-4+n5: +0.068, 54.8%.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
