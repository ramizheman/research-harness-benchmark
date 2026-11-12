# FAM:SF-PAP-020 | Study family SF-PAP-020 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-020
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-PAP-020 | Finding of SF-PAP-020: rejected
- confidence: 1.0
- derived_from: EXP:PAP-020 {family=SF-PAP-020; rule=family member}
- rules_out: HYP:SF-PAP-020 {family=SF-PAP-020; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: AUC=0.61, corr vs self_sim=+0.06; within shapers r~0
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-PAP-020 | Hypothesis of SF-PAP-020
- addresses: RQC:RQC-151 {family=SF-PAP-020; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-020 {decided_by=PAP-020; family=SF-PAP-020; rule=automated adjudication stratum}
- source_record: PAP-020
- tested_by: EXP:PAP-020 {record=PAP-020; rule=family hypothesis tested by member record}
- text: Origin structural influence, signature stability and usage forecast portability.
