# EXP:APPA-045 | Joint vs sequential Rank-then-Route ranking
- date: 2026-06-22
- date_basis: doc
- date_reliable: yes
- design: _joint_vs_sequential.py; n=2,779 RS triggers; blended matchup PPP, min 3 H2H poss/player.
- hypothesis: Picking play type and player jointly beats sequential Rank then Route enough to justify the extra step.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPA-045; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-045 {record=APPA-045; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Prior weight 50 ? reroutes partly reflect talent routing, not pure matchup.
- prespecified: no
- produced: RES:APPA-045 {record=APPA-045; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-044
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-045; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Joint vs sequential Rank-then-Route ranking
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-045; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPA-045; rule=keyword rule METHOD_RULES}

# RES:APPA-045 | Result of APPA-045
- failure_evidence: Mean +0.020 PPP left on table is small; sequential declared safe ~80% with joint tiebreak in ~20%.
- failure_type: E_unclear
- power_info: n=2,779 triggers
- primary_result: Joint pick = sequential 80.3%; joint reroutes 19.7% (547). Mean PPP left on table +0.020 all / +0.099 reroutes only (median +0.080). Play-type gap BEST vs 2nd 0.215 mean / 0.182 median. Routing premium +0.089. Strict dominance 49.2%.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
