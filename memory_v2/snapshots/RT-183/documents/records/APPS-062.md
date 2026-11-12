# EXP:APPS-062 | Test 3: cumulative Q1-Q3 star load -> Q4 PPP
- date: 2026-06-14
- date_basis: mtime
- date_issues: file modification time: upper bound only; 9 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Unit=(star, game). Top vs bottom tercile Q1-Q3 load; match Q4 margin x opp def-rating quartile x season x home.
- hypothesis: High Q1-Q3 initiator load lowers Q4 star PPP (mechanism for Test 2).
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPS-062; rule=keyword rule VARIABLE_RULES}
- measures: VAR:structural_influence_load_L {record=APPS-062; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-062 {record=APPS-062; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: yes
- produced: RES:APPS-062 {record=APPS-062; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-061
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\test_3_star_load.md
- title: Test 3: cumulative Q1-Q3 star load -> Q4 PPP
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-062; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPS-062; rule=keyword rule METHOD_RULES}
- uses_method: METH:placebo_or_permutation_test {record=APPS-062; rule=keyword rule METHOD_RULES}

# RES:APPS-062 | Result of APPS-062
- failure_evidence: ATT~0, CI excludes large load effects; perm/placebo ~0.77. Test 2 Q4 decline is not explained by raw possession load.
- failure_type: B_powered_null
- power_info: 1854 high-load vs 2375 low-load games
- primary_result: Matched ATT=-0.0052, 95% CI[-0.0387,+0.0239], perm p=0.7706, placebo p=0.7760. Raw high-low -0.0146. high-load games=1854, low=2375.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
