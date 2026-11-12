# FAM:SF-APPS-086 | Study family SF-APPS-086 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-086
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPS-085 {family=SF-APPS-086; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.375}
- risk_code: DRIFT_NONSTATIONARITY
- validation_status: no_validation_recorded

# FIND:SF-APPS-086 | Finding of SF-APPS-086: rejected
- confidence: 0.95
- derived_from: EXP:APPS-086 {family=SF-APPS-086; rule=family member}
- rules_out: HYP:SF-APPS-086 {family=SF-APPS-086; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: L(p) vs Q_p r~0. Uniform mean tm_dPPP vs Q_p r=+0.812; |dA|-weighted eco r=+0.703; eco residualized on uniform vs Q_p r=+0.084 p=0.399 NULL. Cosine to mean positive footprint vs Q_p r=-0.336 p=0.000559 (wrong sign). Pair-level dA contrasts do not survive FDR.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-086 | Hypothesis of SF-APPS-086
- addresses: RQC:RQC-047 {family=SF-APPS-086; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-086 {decided_by=APPS-086; family=SF-APPS-086; rule=automated adjudication stratum}
- source_record: APPS-086
- tested_by: EXP:APPS-086 {record=APPS-086; rule=family hypothesis tested by member record}
- text: Scalar structural load L(p) or an |dA|-weighted ecosystem lift predicts teammate-path quality Q_p.
