# EXP:APPS-084 | Portability confirmatory: wiring-displacement signature travels
- date: 2026-07-26
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Gate movers=294 PASS. Confirmatory max_gap=0, n_perm=5000, dest_franchises=30.
- hypothesis: A player's wiring-displacement signature is a portable trait (self_sim > decoy_sim at destination).
- knowable_in_advance: no
- measures: VAR:three_point_attempts_or_luck {record=APPS-084; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF19 {record=APPS-084; rule=audit/study_family_review.csv or singleton}
- motivates: FOLLOW:APPS-084 {needs_review=yes; record=APPS-084; rule=text pattern motivate/follow-up/next step}
- n_runs: 2
- notes: Connector follow-ups later argue connector *value* is relational even if the displacement signature travels.
- prespecified: yes
- produced: RES:APPS-084 {record=APPS-084; rule=record fields}
- project: When a Hub Sits (Paper 2)
- related_as_recorded: APPS-080; APPS-087
- related_to: EXP:APPS-087 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-084; rule=date-ordered record link}
- reported_in: PAPER:When_a_Hub_Sits_manuscript {record=APPS-084; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\portability_full_result.txt
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\portability_gate_result.txt
- title: Portability confirmatory: wiring-displacement signature travels

# FOLLOW:APPS-084 | Follow-on candidate from APPS-084
- status: candidate from text pattern; not curated
- text: Connector follow-ups later argue connector *value* is relational even if the displacement signature travels.

# RES:APPS-084 | Result of APPS-084
- failure_evidence: Delta>0, perm<0.01, CI excludes 0 at destination-franchise clustering.
- failure_type: D_positive
- power_info: n=294 movers, 30 dest franchises
- primary_result: median self_sim=+0.129 decoy_sim=+0.049; T1 median Delta=+0.0557 perm_p=0.0050; 173/294=0.5884 sign_test_p=2.872e-03; dest-fr CI [+0.0192,+0.0859]. All three decision-rule bars True. T1 CONFIRMED.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
