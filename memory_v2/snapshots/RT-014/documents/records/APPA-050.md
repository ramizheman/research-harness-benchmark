# EXP:APPA-050 | Superstar sequential suppression: opponent play before the star
- date: 2026-05-30
- date_basis: doc
- date_reliable: yes
- design: Full graph RS+PO; 30 stars; min n=30 after the suppressor PT.
- hypothesis: A specific opponent play type on the preceding possession suppresses each star's next-possession PPP relative to that star's baseline.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPA-050; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-050 {record=APPA-050; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: PUTBACK as a league-wide suppressor is the claim later tested as a mechanism in APPA-054/055.
- prespecified: no
- produced: RES:APPA-050 {record=APPA-050; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-054; APPA-055
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-050; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Superstar sequential suppression: opponent play before the star
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPA-050; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-050; rule=keyword rule DATASET_RULES}

# RES:APPA-050 | Result of APPA-050
- failure_evidence: No multiplicity correction; n_after is 32-95 for several PUTBACK cells vs thousands of baseline possessions.
- failure_type: E_unclear
- power_info: 30 stars; min n_after=30
- primary_result: PUTBACK is top suppressor for 6+ stars (e.g. D. Mitchell 1.178 to 0.884, d=-0.294, n_after=95; B. Beal d=-0.345 n=32; C. Holmgren d=-0.222 n=52). Other tops: TRANSITION (A. Davis -0.058), POST_UP (N. Jokic -0.075), PULL_UP (A. Edwards -0.043).
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
