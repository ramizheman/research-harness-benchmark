# FAM:SF-APPS-076 | Study family SF-APPS-076 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-076
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-076 | Finding of SF-APPS-076: rejected
- confidence: 0.95
- derived_from: EXP:APPS-076 {family=SF-APPS-076; rule=family member}
- rules_out: HYP:SF-APPS-076 {family=SF-APPS-076; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: RTM (ppp_h1 alone) 32.9% of variance. Usage +0.0%; process+shot-zone +1.7%; lineup +0.0%; context +0.0%. Unexplained 65.4%. Total explained 34.6% (RTM=95% of explained).
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-076 | Hypothesis of SF-APPS-076
- addresses: RQC:RQC-121 {family=SF-APPS-076; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-076 {decided_by=APPS-076; family=SF-APPS-076; rule=automated adjudication stratum}
- source_record: APPS-076
- tested_by: EXP:APPS-076 {record=APPS-076; rule=family hypothesis tested by member record}
- text: Observable in-game process/usage/shot-selection/lineup/context changes explain suppression triggers beyond RTM.
