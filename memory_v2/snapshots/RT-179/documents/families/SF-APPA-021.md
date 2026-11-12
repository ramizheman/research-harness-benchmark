# FAM:SF-APPA-021 | Study family SF-APPA-021 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-021
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPM-005 {family=SF-APPA-021; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.362}
- validation_evidence: APPA-021: 'val 690 cells (84,319 poss), holdout 520 cells (69,876 poss); alpha sweep raw and ols-calibrated'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-021 | Finding of SF-APPA-021: rejected
- confidence: 0.95
- derived_from: EXP:APPA-021 {family=SF-APPA-021; rule=family member}
- rules_out: HYP:SF-APPA-021 {family=SF-APPA-021; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Best alpha = 1.00 (pure actual usage): R2 hol +0.0451 raw, +0.0672 calibrated; fullEQ R2 -0.1981.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPA-021 | Hypothesis of SF-APPA-021
- addresses: RQC:RQC-017 {family=SF-APPA-021; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPA-021 {decided_by=APPA-021; family=SF-APPA-021; rule=automated adjudication stratum}
- source_record: APPA-021
- tested_by: EXP:APPA-021 {record=APPA-021; rule=family hypothesis tested by member record}
- text: Blending equilibrium with actual-usage prediction beats either alone.
