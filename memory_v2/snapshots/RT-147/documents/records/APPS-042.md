# EXP:APPS-042 | POST_UP vs PUTBACK Q1-Q4 gradient and double-suppression stack
- date: 2026-05-31
- date_basis: doc
- date_reliable: yes
- design: POST_UP cluster (Jokic, Doncic, LeBron, Fox, Brown) Q1-Q4 deltas; TRANSITION cluster (Tatum, Morant, Young, Haliburton); league POST_UP then PUTBACK 4-hop stack n=1047.
- hypothesis: PUTBACK suppression is fatigue (Q4-heavy); POST_UP is immediate rhythm disruption; stacking them is additive.
- knowable_in_advance: unclear
- member_of: FAM:SF09 {record=APPS-042; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Authors read POST_UP as rhythm/read disruption not fatigue; TRANSITION unexpected +0.075 flagged to re-examine sample.
- prespecified: no
- produced: RES:APPS-042 {record=APPS-042; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-040
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\postup_putback_gradient\postup_vs_putback_gradient.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\three_mechanisms\double_suppression_mitchell_report.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\three_mechanisms\transition_immunity_report.md
- title: POST_UP vs PUTBACK Q1-Q4 gradient and double-suppression stack
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-042; rule=keyword rule DATASET_RULES}

# RES:APPS-042 | Result of APPS-042
- failure_evidence: PUTBACK vs POST_UP gradients differ as hypothesized, but TRANSITION gradient has the wrong sign and stacked suppression is less than additive; per-player stacked n often <5.
- failure_type: E_unclear
- power_info: cluster n=5 players; stacked n=1047 league / typically n<10 per star
- primary_result: POST_UP Q1->Q4 -0.065 (Q1 -0.119 to Q4 -0.184); PUTBACK -0.374 (0.144 to -0.23). TRANSITION cluster gradient +0.075 (unexpected vs hypothesized flat). Stacked delta -0.071 vs additive prediction -0.232 (less than additive). League after PUTBACK -0.113 (n=15898), after POST_UP -0.119 (n=76329).
- record_stratum: uncertain
- record_substatus: inconclusive
- verdict: inconclusive
