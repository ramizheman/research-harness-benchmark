# EXP:APPS-013 | Defensive Style Index shift RS vs playoffs
- date: 2026-05-08
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: pbpstats Playoffs vs RS aggregates, same DSI formula, 2022-23 and 2023-24 playoff teams.
- hypothesis: Teams shift toward HELP/SWITCH and away from DROP in the playoffs, making RS DSI priors wrong.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPS-013 {record=APPS-013; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Partial support: SWITCH up and DROP down, but the hypothesized HELP shift was absent.
- prespecified: no
- produced: RES:APPS-013 {record=APPS-013; rule=record fields}
- project: Strategy app
- related_as_recorded: Defensive PPP allowed RS vs playoffs
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_dsi_rs_vs_playoff.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\dsi_rs_playoff_run.log
- title: Defensive Style Index shift RS vs playoffs
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-013; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-013; rule=keyword rule DATASET_RULES}

# RES:APPS-013 | Result of APPS-013
- failure_evidence: HELP shift +0.0135 'No meaningful shift'; per-team shifts range -0.287 to +0.271 with no test.
- failure_type: E_unclear
- power_info: 32 team-seasons; no CIs
- primary_result: SWITCH 0.294 -> 0.336 (+0.0426, 62% of teams); DROP 0.399 -> 0.343 (-0.0561); HELP 0.307 -> 0.321 (+0.0135, 'No meaningful shift').
- record_stratum: uncertain
- record_substatus: inadequately tested: verdict null, mechanism E_unclear
- verdict: null
