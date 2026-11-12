# FAM:SF-CHT-058 | Study family SF-CHT-058 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-058
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-CHT-058 | Finding of SF-CHT-058: rejected
- confidence: 1.0
- derived_from: EXP:CHT-058 {family=SF-CHT-058; rule=family member}
- rules_out: HYP:SF-CHT-058 {family=SF-CHT-058; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: A. When to acquire: all null (e.g. brit_top1 rho=-0.06 p=0.60; scarce-roster rho=+0.17 p=0.11). B. Dest brittleness vs Delta: all null. Adding brittleness to cut does not help.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-CHT-058 | Hypothesis of SF-CHT-058
- addresses: RQC:RQC-140 {family=SF-CHT-058; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-CHT-058 {decided_by=CHT-058; family=SF-CHT-058; rule=automated adjudication stratum}
- source_record: CHT-058
- tested_by: EXP:CHT-058 {record=CHT-058; rule=family hypothesis tested by member record}
- text: Team brittleness or connector scarcity predicts benefit from acquiring a connector, or destination brittleness predicts role reproduction.
