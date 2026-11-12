# FAM:SF-APPS-089 | Study family SF-APPS-089 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-089
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-089 | Finding of SF-APPS-089: rejected
- confidence: 0.95
- derived_from: EXP:APPS-089 {family=SF-APPS-089; rule=family member}
- rules_out: HYP:SF-APPS-089 {family=SF-APPS-089; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Corr(L, raw)=+0.013; Corr(L, adj)=+0.008. Quadrants ~25 each of highL-highScore / highL-lowScore / lowL-highScore / lowL-lowScore. Negative on/off n=49; 78% mechanism NONINITIATOR_TEAM_PATH (noninit_team_lift -3.52 vs +2.44 for positives).
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-089 | Hypothesis of SF-APPS-089
- addresses: RQC:RQC-045 {family=SF-APPS-089; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-089 {decided_by=APPS-089; family=SF-APPS-089; rule=automated adjudication stratum}
- source_record: APPS-089
- tested_by: EXP:APPS-089 {record=APPS-089; rule=family hypothesis tested by member record}
- text: Higher structural load L predicts higher adjusted on-off scoring among connectors.
