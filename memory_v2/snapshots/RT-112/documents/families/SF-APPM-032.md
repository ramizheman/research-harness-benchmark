# FAM:SF-APPM-032 | Study family SF-APPM-032 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-032
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF-APPS-034 {family=SF-APPM-032; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.39}
- risk_code: MECHANICAL_FLOOR
- validation_evidence: APPM-032: 'rs holdout; shrinkage-blended h2h oracle (prior weight 50), rotation-f'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-032 | Finding of SF-APPM-032: supported
- confidence: 0.95
- derived_from: EXP:APPM-032 {family=SF-APPM-032; rule=family member}
- statement: Routing regret +0.094 PPP (stale) / +0.124 RS (corrected); SPOT_UP +0.183 (n=385), CUT +0.129 (n=295), DRIVE +0.081 (n=280).
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPM-032 | Hypothesis of SF-APPM-032
- addresses: RQC:RQC-033 {family=SF-APPM-032; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPM-032
- supported_by: FIND:SF-APPM-032 {decided_by=APPM-032; family=SF-APPM-032; rule=automated adjudication stratum}
- tested_by: EXP:APPM-032 {record=APPM-032; rule=family hypothesis tested by member record}
- text: Routing counters to the oracle initiator adds PPP beyond play selection.
