# FAM:SF-APPA-016 | Study family SF-APPA-016 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-016
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPA-016 | Finding of SF-APPA-016: rejected
- confidence: 0.95
- derived_from: EXP:APPA-016 {family=SF-APPA-016; rule=family member}
- rules_out: HYP:SF-APPA-016 {family=SF-APPA-016; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: V1 bias +0.0112 (+1.12 pts/100), R2 -0.1758, win-side 58.8%; V2 +1.69; V3 +1.26; V6 bias -0.0012 (-0.12 pts/100), R2 0.0323, win-side 61.9%, model>actual 47.5%.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPA-016 | Hypothesis of SF-APPA-016
- addresses: RQC:RQC-059 {family=SF-APPA-016; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPA-016 {decided_by=APPA-016; family=SF-APPA-016; rule=automated adjudication stratum}
- source_record: APPA-016
- tested_by: EXP:APPA-016 {record=APPA-016; rule=family hypothesis tested by member record}
- text: A3 predicted PPP exceeds actual (treated as validated optimization signal) and is well calibrated.
