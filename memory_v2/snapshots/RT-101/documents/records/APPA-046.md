# EXP:APPA-046 | Adaptation vs generic counter (W4)
- date: 2026-06-22
- date_basis: doc
- date_reliable: yes
- design: _adaptation_vs_generic.py; n=1,539 RS triggers with BEST tier + viable blended PPP (55.4% of 2,779).
- extends: EXP:APPA-041 {direction=verified by dates; needs_review=no; origin=related field; record=APPA-046; rule=date-ordered record link}
- hypothesis: BEST-tier counters are suppression-specific rather than the team's generic best available play.
- knowable_in_advance: no
- measures: VAR:PPP_points_per_possession {record=APPA-046; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-046 {record=APPA-046; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Deck '80%' and '1,600 triggers' should be 78.3% and 1,539. Pivot remains counterfactual: 93% do not pivot. Drop magnitude does not predict smarter counters (~22% flat).
- prespecified: no
- produced: RES:APPA-046 {record=APPA-046; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-041; APPA-042
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-046; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Adaptation vs generic counter (W4)

# RES:APPA-046 | Result of APPA-046
- failure_evidence: 78.3% of ranked BEST counters are the generic best available; Rank adds value in ~20-22%, 39.7% when defense took the team's best.
- failure_type: D_positive
- power_info: n=1,539 W4 triggers; 1,466 (95.3%) had a better option already
- primary_result: BEST == generic best 78.3%; suppression-specific 21.7%. Defense suppressed generic-best 4.7% (73); then specific 39.7%. When supp != generic, still picks generic 79.2%. (off,def) counter changes by what was suppressed 48.8% (190/389). PNR adapt 28.3% n=428; PULL_UP 28.5% n=291. True INSUFF (no valid counter) 0/11,087 full-graph triggers.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
