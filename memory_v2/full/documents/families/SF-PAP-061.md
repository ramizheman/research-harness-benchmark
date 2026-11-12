# FAM:SF-PAP-061 | Study family SF-PAP-061 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-061
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-061 | Finding of SF-PAP-061: rejected
- confidence: 1.0
- derived_from: EXP:PAP-061 {family=SF-PAP-061; rule=family member}
- rules_out: HYP:SF-PAP-061 {family=SF-PAP-061; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: mean dist G0=0.145, G1=0.141, noise floor=0.085; dist(G0)-dist(G1)=+0.0032 CI[-0.0050,+0.0106] p=0.44 Holm 0.87; G1 beats G0 in 49% of spells
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-PAP-061 | Hypothesis of SF-PAP-061
- addresses: RQC:RQC-020 {family=SF-PAP-061; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-061 {decided_by=PAP-061; family=SF-PAP-061; rule=automated adjudication stratum}
- source_record: PAP-061
- tested_by: EXP:PAP-061 {record=PAP-061; rule=family hypothesis tested by member record}
- text: G1 (leave-one-out) is closer to the evaluation fingerprint than G0 (no change).
