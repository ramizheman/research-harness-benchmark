# EXP:APPA-034 | Opponent-relative leverage prevalence sweep
- date: 2026-04-20
- date_basis: mtime
- date_issues: file modification time: upper bound only; 11 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: 870 ordered team pairs; defense PT edge vs league >= +5% on seed PTs.
- hypothesis: How often does an opponent-specific exploitable defensive weakness exist?
- knowable_in_advance: unclear
- member_of: FAM:SF-APPA-034 {record=APPA-034; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Edges depend only on the defense (e.g. DAL PNR +9.2% for every offense), so they are not matchup-specific.
- prespecified: no
- produced: RES:APPA-034 {record=APPA-034; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\LEVERAGE_PREVALENCE.md
- title: Opponent-relative leverage prevalence sweep
- uses_dataset: DS:NCAA_tournament_and_ratings_data {record=APPA-034; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-034; rule=keyword rule DATASET_RULES}

# RES:APPA-034 | Result of APPA-034
- failure_type: E_unclear
- power_info: 870 pairs
- primary_result: Exploit available 33.3%; trap 23.3%; both 6.7%; neither 50.0%; median best edge 3.79%.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
