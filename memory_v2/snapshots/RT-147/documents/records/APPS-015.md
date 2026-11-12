# EXP:APPS-015 | Player BEST/AVOID tier tendency in H2 trigger games (55 series)
- date: 2026-06-16
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: trigger_table_clean.csv, 55 series 2022-2026, 179 players, 25 teams, min 10 poss.
- hypothesis: Teams and players differ in how often H2 trigger possessions land on the engine's BEST vs AVOID counter.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPS-015 {record=APPS-015; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPS-015 {record=APPS-015; rule=record fields}
- project: Strategy app
- related_as_recorded: Agent Test B counter recs
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\player_tier_tendency_by_team.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\player_tier_tendency_league_summary.md
- title: Player BEST/AVOID tier tendency in H2 trigger games (55 series)
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-015; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-015; rule=keyword rule DATASET_RULES}

# RES:APPS-015 | Result of APPS-015
- failure_evidence: No outcome test; player samples 10-178 possessions.
- failure_type: E_unclear
- power_info: min 10 poss per player
- primary_result: Team AVOID% ranges 50.6% (ORL) to 6.8% (SAC); team BEST% 0.0%-15.8%.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
