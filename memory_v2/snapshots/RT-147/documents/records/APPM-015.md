# EXP:APPM-015 | Routing prior vs H2H posterior gate diagnostic
- date: 2026-06-10
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 6,221 (offense, opponent, PT) cells; count H2H leaders differing from season default at gates 5/10/15/25.
- hypothesis: The n>=15 H2H gate suppresses real player-routing signal.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPM-015; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF31 {record=APPM-015; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Recommendation: keep n>=15 gate.
- prespecified: no
- produced: RES:APPM-015 {record=APPM-015; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ROUTING_PRIOR_VS_H2H_DIAGNOSTIC.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_diag_routing_vs_h2h.py
- title: Routing prior vs H2H posterior gate diagnostic
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-015; rule=keyword rule DATASET_RULES}

# RES:APPM-015 | Result of APPM-015
- failure_evidence: Apparent +1.13 PPP edge is small-sample inflation (e.g. n=6, PPP=3.00).
- failure_type: C_artifact
- primary_result: Mean PPP delta lead-default +1.259 (n>=5) to +1.129 (n>=15); low-n leaders are role players with 2-3 PPP on 5-7 possessions.
- record_stratum: artifact
- record_substatus: verdict artifact_found
- verdict: artifact_found
