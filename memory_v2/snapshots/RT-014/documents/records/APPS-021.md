# EXP:APPS-021 | Cost of ignoring suppression (continue suppressed PT in H2)
- date: 2026-05-29
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 735 suppression events, 271 games; Group A h2_n>=3 (n=683) vs Group B h2_n<=1 (n=31). Canonical deck uses trigger CSV H1/H2 n>=5 (633 PO / 2779 RS).
- hypothesis: When a suppression trigger fires and teams keep running the suppressed play type, H2 PPP on that PT is materially below H1.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPS-021; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF02 {record=APPS-021; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Do not cite poss-weighted cost 0.646 on slides; locked methodology is trigger row-mean drop 0.63. Win rates 48.8% vs 48.4% are indistinguishable.
- prespecified: no
- produced: RES:APPS-021 {record=APPS-021; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-022; APPS-025
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\COHERENT_NUMBERS.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\cost_of_ignoring_results.md
- title: Cost of ignoring suppression (continue suppressed PT in H2)
- uses_dataset: DS:NCAA_tournament_and_ratings_data {record=APPS-021; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-021; rule=keyword rule DATASET_RULES}

# RES:APPS-021 | Result of APPS-021
- failure_evidence: One-sample t on (h1-h2) p=0.0000 n=683; pivoting overall-H2 advantage not significant (p=0.2642, n_B=31).
- failure_type: D_positive
- power_info: n=683 Group A; n=31 Group B underpowered for pivot vs continue
- primary_result: Group A: H1 1.522 -> post-trigger 0.876, cost 0.646 PPP/poss, 5.16 pts/trigger (t=48.172, p=0.0000, n=683). Pivot vs continue overall H2 1.074 vs 1.043, MW p=0.2642. Locked row-mean (n>=5): H1 1.48->H2 0.85, drop 0.63, 5.4 pts/trigger, n=633 PO / 2779 RS; full-graph drop 0.619 (n=11087).
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
