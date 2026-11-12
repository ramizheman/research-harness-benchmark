# EXP:APPA-022 | Blended prior-season shrinkage evaluator and k sweep
- date: 2026-04-16
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Fixed test 155 late-2024-25 games; current-only vs pooled vs blended (k=5,10,20,30); early-season simulation with 150 games.
- hypothesis: Blending prior seasons helps early season without hurting late season.
- knowable_in_advance: no
- member_of: FAM:SF-APPA-022 {record=APPA-022; rule=audit/study_family_review.csv or singleton}
- n_runs: 4
- notes: Supported only as relative improvement; absolute accuracy stays below a mean predictor.
- prespecified: partial
- produced: RES:APPA-022 {record=APPA-022; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-016
- related_to: EXP:APPA-016 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-022; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\BLENDED_REPORT.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\K_SWEEP.md
- title: Blended prior-season shrinkage evaluator and k sweep
- uses_method: METH:regression {record=APPA-022; rule=keyword rule METHOD_RULES}
- uses_method: METH:simulation {record=APPA-022; rule=keyword rule METHOD_RULES}

# RES:APPA-022 | Result of APPA-022
- failure_evidence: Early-season blend improves all 5 metrics, but all R2 remain negative.
- failure_type: D_positive
- power_info: 155 test games
- primary_result: Late: blended k=30 worse on 5/5 metrics (R2 -0.1065 vs -0.0866). Early: blended better 5/5 (R2 -0.2624 vs -0.4508; win-side 55.8% vs 52.5%). k sweep recommends k~5.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
