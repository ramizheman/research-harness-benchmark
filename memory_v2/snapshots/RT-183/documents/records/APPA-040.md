# EXP:APPA-040 | Cost of ignoring suppression: continue rate and points lost
- date: 2026-05-29
- date_basis: doc
- date_reliable: yes
- design: 55-series graph; Group A h2_n>=3 vs Group B h2_n<=1; within-game H1 vs H2 on suppressed PT; points decomposition via _points_not_ppp.py. RS confirm _rs_continue_rate.py.
- extends: EXP:APPA-047 {direction=corrected (citing record is the earlier one); needs_review=yes; origin=related field; record=APPA-040; rule=date-ordered record link}
- hypothesis: After a suppression trigger, teams keep running the suppressed play at near-H1 volume and lose several points per event.
- knowable_in_advance: no
- member_of: FAM:SF02 {record=APPA-040; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: H1 PPP floor=1.0 in cost/continue scripts but not in the trigger table; removing it changes continue 94.9% to 94.1%. Oracle ceiling 11.1 pts is labeled projection.
- prespecified: no
- produced: RES:APPA-040 {record=APPA-040; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-036; APPA-037
- related_to: EXP:APPA-037 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-040; rule=date-ordered record link}
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-040; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Cost of ignoring suppression: continue rate and points lost
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-040; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPA-040; rule=keyword rule DATASET_RULES}

# RES:APPA-040 | Result of APPA-040
- failure_evidence: 93% continue at ~97% of H1 volume; blowout-filtering continue rate is a volume-threshold artifact (78.8% at |margin|<=20) so the paper cites unfiltered 93%/94.9%.
- failure_type: D_positive
- power_info: 683 Group A PO triggers; 3,169 RS events
- primary_result: PO: 735 events; Group A 683 (93%) H1 1.522 to H2 0.876, cost/poss 0.646, ~8.2 H2 poss, ~97% H1 volume, ~5.4 pts/trigger; real actionable ~6.1 pts (5.3 keep-calling + 0.8 AVOID vs BEST). RS continue 93.1% (2,949/3,169); no-floor 94.1%.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
