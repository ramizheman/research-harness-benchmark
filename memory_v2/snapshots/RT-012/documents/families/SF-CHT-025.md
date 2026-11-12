# FAM:SF-CHT-025 | Study family SF-CHT-025 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-025
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- validation_status: no_validation_recorded

# FIND:SF-CHT-025 | Finding of SF-CHT-025: artifact
- confidence: 1.0
- derived_from: EXP:CHT-025 {family=SF-CHT-025; rule=family member}
- rules_out: HYP:SF-CHT-025 {family=SF-CHT-025; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: OTHER: 36% end in fouls, PPP inflated (FOUL_BUCKET). DRIVE: 12pp below foul benchmark (FOUL_LEAK). PNR shows 22% foul rate. Only 335 of 50,668 possessions (0.7%) map to a real play type via initiation_type.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-025 | Hypothesis of SF-CHT-025
- addresses: RQC:RQC-087 {family=SF-CHT-025; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-025 {decided_by=CHT-025; family=SF-CHT-025; rule=automated adjudication stratum}
- source_record: CHT-025
- tested_by: EXP:CHT-025 {record=CHT-025; rule=family hypothesis tested by member record}
- text: Play-type PPP differences are real efficiency, not labeling/foul artifacts.
