# EXP:APPA-023 | Per-play-type interaction residual feature (Phase 1b)
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: 870 train cells (386,675 poss); shrinkage k sweep 25-1000; holdout R2.
- hypothesis: Per-PT team-pair interaction deltas add R2 over the 8-feature baseline (ship if lift > +0.005).
- knowable_in_advance: no
- member_of: FAM:SF-APPA-023 {record=APPA-023; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Negative weight suggests overfitting sparse cells.
- prespecified: partial
- produced: RES:APPA-023 {record=APPA-023; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-020
- related_to: EXP:APPA-020 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-023; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\INTERACTION_PT.md
- title: Per-play-type interaction residual feature (Phase 1b)
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-023; rule=keyword rule DATASET_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPA-023; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPA-023; rule=keyword rule METHOD_RULES}

# RES:APPA-023 | Result of APPA-023
- failure_evidence: Lift +0.0042 < +0.005 ship threshold.
- failure_type: B_powered_null
- power_info: 870 train cells
- primary_result: Best k=500 R2_hol +0.1192 vs +0.1150 baseline; lift +0.0042; w_pt negative (-1.4014).
- record_stratum: rejected
- record_substatus: verdict failed_gate, powered null with power information
- verdict: failed_gate
