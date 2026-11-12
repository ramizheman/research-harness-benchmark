# EXP:APPS-010 | Play-type PPP change across playoff series game buckets
- date: 2026-05-08
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Pooled (series, team, PT, bucket) records (1197), EARLY G1-2 / MID G3-4 / LATE G5-7, min 10 poss, min 3 series.
- hypothesis: Play-type PPP (especially DRIVE) declines as a playoff series progresses, so DRIVE is a good early-series call.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPS-010; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-010 {record=APPS-010; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPS-010 {record=APPS-010; rule=record fields}
- project: Strategy app
- related_as_recorded: RS vs playoff PPP; Within-game DRIVE decline
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_series_game_adaptation.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\game_adaptation_run.log
- title: Play-type PPP change across playoff series game buckets
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-010; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-010; rule=keyword rule DATASET_RULES}

# RES:APPS-010 | Result of APPS-010
- failure_evidence: 'NO CLEAR SIGNAL - DRIVE PPP is stable or improves across the series'; observational with selection caveats.
- failure_type: E_unclear
- power_info: 1197 records; no CIs
- primary_result: DRIVE 0.889 -> 0.949 (+0.060); CUT +0.114; PNR +0.087; PULL_UP -0.077; POST_UP -0.032.
- record_stratum: uncertain
- record_substatus: inadequately tested: verdict null, mechanism E_unclear
- verdict: null
