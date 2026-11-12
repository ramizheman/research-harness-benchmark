# EXP:APPA-030 | Play-type label backfill verification
- date: 2026-05-24
- date_basis: doc
- date_reliable: yes
- design: 921,514 labelled possessions; band tests on PT shares, PNR cap, PPP sanity, temporal distribution, team identity and directional checks.
- hypothesis: Backfilled play-type labels match expected league distributions and team identities.
- knowable_in_advance: no
- measures: VAR:PPP_points_per_possession {record=APPA-030; rule=keyword rule VARIABLE_RULES}
- measures: VAR:play_type_share_mix {record=APPA-030; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-030 {record=APPA-030; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Report says do not run adaptation analysis until resolved.
- prespecified: yes
- produced: RES:APPA-030 {record=APPA-030; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\BACKFILL_VERIFICATION.md
- title: Play-type label backfill verification
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPA-030; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-030; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPA-030; rule=keyword rule METHOD_RULES}

# RES:APPA-030 | Result of APPA-030
- failure_evidence: 2024-25 PULL_UP shares 0.0-2.0% for many teams; 82.8% of PNR labels proxy_calibrated.
- failure_type: C_artifact
- power_info: 921,514 possessions
- primary_result: PNR 28.7% FAIL (band 20-28%); PULL_UP 7.9% FAIL; 3100 games with team PNR >33% FAIL; PNR PPP 0.948 PASS; temporal PASS; team identity FAIL; 2024-25 PULL_UP ~0-1% for many teams. Final: FAIL.
- record_stratum: uncertain
- record_substatus: inadequately tested: verdict failed_gate, mechanism C_artifact
- verdict: failed_gate
