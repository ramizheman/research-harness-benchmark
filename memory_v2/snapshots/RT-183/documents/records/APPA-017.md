# EXP:APPA-017 | A5 player-routing and A5b defensive attention penalty
- date: 2026-04-15
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Calibration framework V4-V6; A5 vs A3 and A5b vs A5 signal in pts/100.
- hypothesis: Routing possessions to each play type's best player adds value over A3, and survives defensive attention adaptation.
- knowable_in_advance: no
- member_of: FAM:SF-APPA-017 {record=APPA-017; rule=audit/study_family_review.csv or singleton}
- n_runs: 3
- notes: Model-scored, not observed outcomes.
- prespecified: no
- produced: RES:APPA-017 {record=APPA-017; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-016
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\CALIBRATION_REPORT_V6.md
- title: A5 player-routing and A5b defensive attention penalty
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPA-017; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-017; rule=keyword rule DATASET_RULES}
- uses_method: METH:calibration_scoring {record=APPA-017; rule=keyword rule METHOD_RULES}
- uses_method: METH:matched_control {record=APPA-017; rule=keyword rule METHOD_RULES}

# RES:APPA-017 | Result of APPA-017
- failure_evidence: Shrinks from +0.94 to +0.03 pts/100 on the larger 520-matchup sample.
- failure_type: B_powered_null
- power_info: 520 matchups
- primary_result: V4 A5 vs A3 +0.77; V5 +0.94 (A5b vs A5 +0.01); V6 (520 matchups) A5 vs A3 +0.03, A5b vs A5 -0.00.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
