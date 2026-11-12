# FAM:SF-APPS-064 | Study family SF-APPS-064 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict failed_gate, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-064
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-064 | Finding of SF-APPS-064: rejected
- confidence: 0.95
- derived_from: EXP:APPS-064 {family=SF-APPS-064; rule=family member}
- rules_out: HYP:SF-APPS-064 {family=SF-APPS-064; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Q_obs=0.3838; Q_null=0.4300+-0.0010 range[0.4282,0.4324]; z=-46.85 p_emp=1.000. VERDICT: KILL ? no structure beyond volume+schedule.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-064 | Hypothesis of SF-APPS-064
- addresses: RQC:RQC-111 {family=SF-APPS-064; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-064 {decided_by=APPS-064; family=SF-APPS-064; rule=automated adjudication stratum}
- source_record: APPS-064
- tested_by: EXP:APPS-064 {record=APPS-064; rule=family hypothesis tested by member record}
- text: Attacker-defender assignment networks have community structure beyond volume and schedule.
