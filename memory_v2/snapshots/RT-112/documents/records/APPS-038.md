# EXP:APPS-038 | Player sequential-premium family (same-player X->Y after opponent response)
- date: 2026-05-31
- date_basis: doc
- date_reliable: yes
- design: Same initiator on t and t+2; min n=30; focus pairs CUT->DRIVE, DRIVE->SPOT_UP, etc. Flag |t|>=2.0.
- hypothesis: Specific player X->Y sequences score above that player's unconditional Y baseline.
- knowable_in_advance: unclear
- member_of: FAM:SF40 {record=APPS-038; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Later Brown->Tatum +0.326 (n=43) was shown to be a placebo artifact (APPS-070).
- prespecified: no
- produced: RES:APPS-038 {record=APPS-038; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-037; APPS-070
- related_to: EXP:APPS-037 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-038; rule=date-ordered record link}
- related_to: EXP:APPS-070 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-038; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\player_seq_premium\player_sequence_premium_report.md
- title: Player sequential-premium family (same-player X->Y after opponent response)
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-038; rule=keyword rule DATASET_RULES}

# RES:APPS-038 | Result of APPS-038
- failure_evidence: Many |t|<2 and n<50; no multiplicity correction; mixed signs on the same pair across players.
- failure_type: E_unclear
- power_info: min n=30; DIRECTIONAL if n<50
- primary_result: Top: P. George DRIVE->SPOT_UP +0.560 (n=31, t=+2.2). D. Mitchell SPOT_UP->DRIVE +0.279 (n=56, t=+2.8). Bottom: C. White DRIVE->SPOT_UP -0.466 (n=37); D. Bane DRIVE->PNR -0.324 (n=70, t=-2.7). Most cells DIRECTIONAL (n<50).
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
