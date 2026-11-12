# FAM:SF-APPM-016 | Study family SF-APPM-016 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-016
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPM-016 | Finding of SF-APPM-016: rejected
- confidence: 0.95
- derived_from: EXP:APPM-016 {family=SF-APPM-016; rule=family member}
- rules_out: HYP:SF-APPM-016 {family=SF-APPM-016; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: A +0.140 PPP [0.084,0.196]; B DiD +0.090 [0.041,0.141]; C gamma +0.0088 SE 0.0239 p=0.7139.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPM-016 | Hypothesis of SF-APPM-016
- addresses: RQC:RQC-067 {family=SF-APPM-016; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPM-016 {decided_by=APPM-016; family=SF-APPM-016; rule=automated adjudication stratum}
- source_record: APPM-016
- tested_by: EXP:APPM-016 {record=APPM-016; rule=family hypothesis tested by member record}
- text: Possessions on the engine's recommended PT score more than other PTs within the series, beyond inherent PT PPP.
