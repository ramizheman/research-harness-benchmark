# EXP:APPS-086 | Connector ecosystem quality: L(p) and |dA| do not predict Q_p
- date: 2026-07-26
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: N=102 connectors (pos=53, neg=49). Talent+opp+period+score residualized S_p and Q_p.
- hypothesis: Scalar structural load L(p) or an |dA|-weighted ecosystem lift predicts teammate-path quality Q_p.
- knowable_in_advance: unclear
- measures: VAR:structural_influence_load_L {record=APPS-086; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-086 {record=APPS-086; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Together with portability: signature may travel but connector *value* looks relational/context-specific.
- prespecified: no
- produced: RES:APPS-086 {record=APPS-086; rule=record fields}
- project: When a Hub Sits (Paper 2)
- related_as_recorded: APPS-085; APPS-084
- related_to: EXP:APPS-084 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-086; rule=date-ordered record link}
- reported_in: PAPER:When_a_Hub_Sits_manuscript {record=APPS-086; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_ecosystem_quality_report.md
- title: Connector ecosystem quality: L(p) and |dA| do not predict Q_p
- uses_method: METH:correlation {record=APPS-086; rule=keyword rule METHOD_RULES}

# RES:APPS-086 | Result of APPS-086
- failure_evidence: Proposed structural metrics add nothing beyond a uniform average of teammate lifts (eco residual r=+0.084 p=0.399). Load is not quality.
- failure_type: B_powered_null
- power_info: n=102
- primary_result: L(p) vs Q_p r~0. Uniform mean tm_dPPP vs Q_p r=+0.812; |dA|-weighted eco r=+0.703; eco residualized on uniform vs Q_p r=+0.084 p=0.399 NULL. Cosine to mean positive footprint vs Q_p r=-0.336 p=0.000559 (wrong sign). Pair-level dA contrasts do not survive FDR.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
