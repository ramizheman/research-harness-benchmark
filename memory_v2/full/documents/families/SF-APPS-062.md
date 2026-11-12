# FAM:SF-APPS-062 | Study family SF-APPS-062 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-062
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: APPS-062: 'atched att=-0.0052, 95% ci[-0.0387,+0.0239], perm p=0.7706, placebo p=0.7760. raw high-low -0.0146. high-load games=1854, low=2'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-062 | Finding of SF-APPS-062: rejected
- confidence: 0.95
- derived_from: EXP:APPS-062 {family=SF-APPS-062; rule=family member}
- rules_out: HYP:SF-APPS-062 {family=SF-APPS-062; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Matched ATT=-0.0052, 95% CI[-0.0387,+0.0239], perm p=0.7706, placebo p=0.7760. Raw high-low -0.0146. high-load games=1854, low=2375.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPS-062 | Hypothesis of SF-APPS-062
- addresses: RQC:RQC-127 {family=SF-APPS-062; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-062 {decided_by=APPS-062; family=SF-APPS-062; rule=automated adjudication stratum}
- source_record: APPS-062
- tested_by: EXP:APPS-062 {record=APPS-062; rule=family hypothesis tested by member record}
- text: High Q1-Q3 initiator load lowers Q4 star PPP (mechanism for Test 2).
