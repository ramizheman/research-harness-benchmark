# FAM:SF-APPA-019 | Study family SF-APPA-019 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-019
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:label_or_classification_error {family=SF-APPA-019; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: LABEL_ERROR
- validation_evidence: APPA-019: 'same 23,922 holdout possessions; per-possession and distribution-level evaluati'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-019 | Finding of SF-APPA-019: rejected
- confidence: 0.95
- derived_from: EXP:APPA-019 {family=SF-APPA-019; rule=family member}
- rules_out: HYP:SF-APPA-019 {family=SF-APPA-019; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: A2 -8.32 pts/100 vs baseline; A2 vs A -6.84; A2 outperforms baseline 47/240. Distribution: A2 mix +13.40 pts/100 vs actual (beats 217/240) but -24.85 vs B argmax.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPA-019 | Hypothesis of SF-APPA-019
- addresses: RQC:RQC-018 {family=SF-APPA-019; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPA-019 {decided_by=APPA-019; family=SF-APPA-019; rule=automated adjudication stratum}
- source_record: APPA-019
- tested_by: EXP:APPA-019 {record=APPA-019; rule=family hypothesis tested by member record}
- text: Diminishing-returns usage curves improve recommendations over static argmax and baseline.
