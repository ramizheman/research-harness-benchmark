# EXP:APPA-053 | Player and teammate sequential premiums
- date: 2026-05-31
- date_basis: doc
- date_reliable: yes
- design: Full graph; min n=30; same initiator vs different initiator on Y.
- hypothesis: Specific same-player and teammate X->Y sequences carry PPP premiums above Y's baseline.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPA-053; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF40 {record=APPA-053; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: DRIVE->SPOT_UP and DRIVE->PNR dominate the top list.
- prespecified: no
- produced: RES:APPA-053 {record=APPA-053; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-049; APPA-058
- related_to: EXP:APPA-058 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-053; rule=date-ordered record link}
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-053; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Player and teammate sequential premiums
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-053; rule=keyword rule DATASET_RULES}

# RES:APPA-053 | Result of APPA-053
- failure_evidence: Min n=30 cells; several labeled DIRECTIONAL at t~2.1-2.2; no multiplicity correction.
- failure_type: E_unclear
- power_info: min n=30
- primary_result: Top same-player: P. George DRIVE->SPOT_UP +0.560 n=31 t=+2.2; J. Brown +0.349 n=62; L. Doncic DRIVE->PNR +0.309 n=53. Top teammate: K. Towns->O. Anunoby DRIVE->SPOT_UP +0.398 n=30; J. Brown->J. Tatum DRIVE->PNR +0.326 n=43.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
