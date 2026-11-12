# FAM:SF-PAP-024 | Study family SF-PAP-024 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-024
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:low_power_large_MDE {family=SF-PAP-024; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-PAP-024; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: PAP-024: 'ns, 30 franchises; gate passed then confirmatory with churn robustness. c1a rho=+0.079 p=0.0882 ci[-0.114,+0.234]; c1b rho=+0.'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-024 | Finding of SF-PAP-024: rejected
- confidence: 1.0
- derived_from: EXP:PAP-024 {family=SF-PAP-024; rule=family member}
- rules_out: HYP:SF-PAP-024 {family=SF-PAP-024; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: C1a rho=+0.079 p=0.0882 CI[-0.114,+0.234]; C1b rho=+0.095 p=0.0738; robust 0.2/0.3 also fail
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-024 | Hypothesis of SF-PAP-024
- addresses: RQC:RQC-145 {family=SF-PAP-024; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-024 {decided_by=PAP-024; family=SF-PAP-024; rule=automated adjudication stratum}
- source_record: PAP-024
- tested_by: EXP:PAP-024 {record=PAP-024; rule=family hypothesis tested by member record}
- text: Teams whose structural influence is concentrated are more defensively vulnerable.
