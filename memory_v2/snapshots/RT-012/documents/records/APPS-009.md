# EXP:APPS-009 | Player routing V4 vs V5 direct scoring
- date: 2026-05-05
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Series where V4 and V5 routed to different players; compare observed PPP (n>=5 each).
- hypothesis: V5 player routing picks players with higher observed PPP than V4 routing.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPS-009; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-009 {record=APPS-009; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Data coverage could be checked before running.
- prespecified: no
- produced: RES:APPS-009 {record=APPS-009; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\player_routing_results.md
- title: Player routing V4 vs V5 direct scoring
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-009; rule=keyword rule DATASET_RULES}

# RES:APPS-009 | Result of APPS-009
- failure_evidence: Scoreable 0 of 8; V5 mostly routed to 'team' rather than a player.
- failure_type: A_unanswerable
- power_info: n=8 divergences, 0 scoreable
- primary_result: 8 divergences, 0 scoreable, 8 unscored (player missing from Neo4j); hit rate n/a.
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict inconclusive
- verdict: inconclusive
