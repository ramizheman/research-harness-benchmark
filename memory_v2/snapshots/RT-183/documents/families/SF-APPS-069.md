# FAM:SF-APPS-069 | Study family SF-APPS-069 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict failed_gate, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-069
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPS-069; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: MECHANICAL_FLOOR
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-069 | Finding of SF-APPS-069: rejected
- confidence: 0.95
- derived_from: EXP:APPS-069 {family=SF-APPS-069; rule=family member}
- rules_out: HYP:SF-APPS-069 {family=SF-APPS-069; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Process-only lag-1 r=+0.645 vs null +0.655; EXCESS=-0.010, cluster-bootstrap 95% CI [-0.012,-0.009]. Scoring excess -0.000; action texture +0.003. Instantaneous scoring autocorr lag-1=-0.0128.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-069 | Hypothesis of SF-APPS-069
- addresses: RQC:RQC-108 {family=SF-APPS-069; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-069 {decided_by=APPS-069; family=SF-APPS-069; rule=automated adjudication stratum}
- source_record: APPS-069
- tested_by: EXP:APPS-069 {record=APPS-069; rule=family hypothesis tested by member record}
- text: Process-only latent state (PCA-1 of tempo/transition) persists above the rolling-window overlap null after game x team demeaning.
