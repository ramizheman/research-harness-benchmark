# EXP:APPM-008 | Final feature stacking ceiling
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Nested OLS models on 8-feat baseline plus xPPP, per-PT interaction, shot_rate, pct_3s.
- hypothesis: Stacking all clean-signal features raises the R2 ceiling materially.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPM-008 {record=APPM-008; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPM-008 {record=APPM-008; rule=record fields}
- project: Strategy app
- related_as_recorded: SHOT_QUALITY.md; STARTER_SHARE.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\STACK_FINAL.md
- title: Final feature stacking ceiling
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-008; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Shot_level_data_with_expected_FG {record=APPM-008; rule=keyword rule DATASET_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPM-008; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPM-008; rule=keyword rule METHOD_RULES}

# RES:APPM-008 | Result of APPM-008
- failure_evidence: Max lift +0.0094; doc calls ~0.12 the practical ceiling.
- failure_type: B_powered_null
- primary_result: Best +xPPP + per-pt interaction R2_hol +0.1244 (lift +0.0094); adding more features lowered holdout R2 (12f +0.1167).
- record_stratum: uncertain
- record_substatus: inadequately tested: verdict null, mechanism B_powered_null, no power information
- verdict: null
