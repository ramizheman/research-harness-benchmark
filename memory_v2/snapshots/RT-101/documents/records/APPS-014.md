# EXP:APPS-014 | Within-game DRIVE decline by game third
- date: 2026-05-08
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Pooled playoff possessions split into game thirds by elapsed time; Game 1 only and all games.
- hypothesis: DRIVE efficiency drops within a single playoff game (defense moves first) before cross-game adaptation.
- knowable_in_advance: no
- member_of: FAM:SF-APPS-014 {record=APPS-014; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPS-014 {record=APPS-014; rule=record fields}
- project: Strategy app
- related_as_recorded: Play-type PPP change across series game buckets
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_drive_within_game.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\drive_within_game_run.log
- title: Within-game DRIVE decline by game third
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-014; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-014; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-014; rule=keyword rule DATASET_RULES}

# RES:APPS-014 | Result of APPS-014
- failure_evidence: DRIVE rises early-to-late (+0.078 G1, +0.093 all games) instead of dropping.
- failure_type: B_powered_null
- power_info: n=1746-1987 per third (all games)
- primary_result: Game 1 DRIVE 0.864 (n=323) -> 0.942 (n=346), +0.078; all games 0.880 (n=1746) -> 0.973 (n=1987), +0.093.
- record_stratum: rejected
- record_substatus: verdict reversed, powered null with power information
- verdict: reversed
