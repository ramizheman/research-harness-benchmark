# EXP:APPM-010 | Scheme-adjusted vs baseline Spearman across canonical series
- date: 2026-05-03
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Per team-series Spearman for 84 team rows across canonical playoff slugs.
- hypothesis: Scheme-adjusted engine (Step 2) ranks play types better than baseline (Step 1).
- knowable_in_advance: unclear
- member_of: FAM:SF-APPM-010 {record=APPM-010; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Spearman target definition not stated in the file.
- prespecified: no
- produced: RES:APPM-010 {record=APPM-010; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SEASON_COMPARISON.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_season_comparison.py
- title: Scheme-adjusted vs baseline Spearman across canonical series
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-010; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPM-010; rule=keyword rule DATASET_RULES}
- uses_method: METH:correlation {record=APPM-010; rule=keyword rule METHOD_RULES}

# RES:APPM-010 | Result of APPM-010
- failure_evidence: Mean delta +0.055; 42 improve vs 8 worse.
- failure_type: D_positive
- power_info: n=84 team rows; no test
- primary_result: Mean Spearman +0.524 -> +0.579 (median +0.548 -> +0.631); improves 42/84, worsens 8/84, noise 34/84.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
