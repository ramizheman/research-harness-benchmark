# EXP:APPA-058 | Season stability of top suppressors and negative teammate pairs
- date: 2026-05-31
- date_basis: doc
- date_reliable: yes
- design: 30 stars x 4 seasons; min n=20 per player-season-opp_play cell. Negative pairs: premium < -0.10, n>=30.
- extends: EXP:APPA-050 {direction=verified by dates; needs_review=no; origin=related field; record=APPA-058; rule=date-ordered record link}
- hypothesis: Each star's top sequential suppressor is stable across seasons, and some teammate X->Y sequences have large negative premiums.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPA-058 {record=APPA-058; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Positive counterpart Brown DRIVE -> Tatum PNR +0.326 n=43; sequence type matters more than pairing.
- prespecified: no
- produced: RES:APPA-058 {record=APPA-058; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-050; APPA-053
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-058; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Season stability of top suppressors and negative teammate pairs

# RES:APPA-058 | Result of APPA-058
- failure_evidence: Only 2/30 stars meet the 75% same-top-suppressor stability rule.
- failure_type: B_powered_null
- power_info: 30 stars x 4 seasons; min n=20/cell
- primary_result: 2/30 (7%) stable (>=75% same top suppressor): D. Mitchell PUTBACK 75%, L. James POST_UP 75%. Negative: J. Tatum->K. Porzingis DRIVE->SPOT_UP -0.444 n=31; Giannis->Lillard DRIVE->PNR -0.263 n=31; J. Brown->J. Tatum SPOT_UP->DRIVE -0.186 n=37.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
