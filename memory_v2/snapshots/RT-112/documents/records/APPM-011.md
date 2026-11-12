# EXP:APPM-011 | Net-swing play-type scoring prototype
- also_recorded_as: APPS-050
- date: 2026-05-23
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: 52 playoff series / 104 team-offense units; compare rank orderings own-PPP vs net-swing.
- hypothesis: Scoring PTs by own PPP minus opponent next-possession PPP changes recommendations.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPM-011; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPM-011 {record=APPM-011; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPM-011 {record=APPM-011; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\NET_SWING_SCORING_PROTOTYPE.md
- title: Net-swing play-type scoring prototype
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPM-011; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-011; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPM-011; rule=keyword rule DATASET_RULES}

# RES:APPM-011 | Result of APPM-011
- failure_evidence: Not evaluated against outcomes; uses in-series observed opp_next_PPP.
- failure_type: E_unclear
- primary_result: Top recommendation changes in 40/104 = 38% units; DRIVE median net swing -0.27 (negative 88%), POST_UP -0.22 (77%).
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
