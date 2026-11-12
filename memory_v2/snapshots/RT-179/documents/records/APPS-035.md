# EXP:APPS-035 | Clutch-after-suppression star PPP vs overall (30 stars, RS 2025-26)
- also_recorded_as: CHT-043
- date: 2026-06-20
- date_basis: doc
- date_reliable: yes
- design: Clutch=Q4 last 5 min |margin|<=5. Group X=clutch in suppression games vs Z=overall. n_X>=15; n=24 OK-confidence players. Also raw clutch vs overall table.
- extends: EXP:APPS-044 {direction=corrected (citing record is the earlier one); needs_review=yes; origin=related field; record=APPS-035; rule=date-ordered record link}
- hypothesis: Stars elevate in clutch possessions of games where their team had a suppression trigger.
- knowable_in_advance: no
- measures: VAR:PPP_points_per_possession {record=APPS-035; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-035 {record=APPS-035; rule=audit/study_family_review.csv or singleton}
- motivates: FOLLOW:APPS-035 {needs_review=yes; record=APPS-035; rule=text pattern motivate/follow-up/next step}
- n_runs: 1
- notes: Selection likely: these clutch minutes occur in games where the offense already failed to adapt.
- prespecified: no
- produced: RES:APPS-035 {record=APPS-035; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-045
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\clutch_30stars.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\clutch_after_suppression.md
- title: Clutch-after-suppression star PPP vs overall (30 stars, RS 2025-26)
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-035; rule=keyword rule DATASET_RULES}
- uses_method: METH:correlation {record=APPS-035; rule=keyword rule METHOD_RULES}

# FOLLOW:APPS-035 | Follow-on candidate from APPS-035
- status: candidate from text pattern; not curated
- text: Selection likely: these clutch minutes occur in games where the offense already failed to adapt.

# RES:APPS-035 | Result of APPS-035
- failure_evidence: Significant league-wide decline (-0.065 PPP, p=0.025), opposite of elevated clutch-cooking; IE% does not predict uplift.
- failure_type: B_powered_null
- power_info: n=24 players with n_X>=15; PO replication not run
- primary_result: Mean X-Z uplift -0.065, t=-2.41, p=0.025, n=24 (16 negative / 8 positive). Pearson r(uplift, IE%)=0.031, p=0.885. Brunson X-Z=+0.003 (rank 8/24). Raw clutch vs overall: Edwards +0.225, Giannis -0.240; Brunson -0.021.
- record_stratum: rejected
- record_substatus: verdict reversed, powered null with power information
- verdict: reversed
