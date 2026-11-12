# FAM:SF-APPS-057 | Study family SF-APPS-057 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict abandoned
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-057
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPS-057; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: abandoned
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPS-057: 'engine sha freeze 59a9be48; tuning 17 series cap_yy<=23; holdout 25 series. protocol written; holdout scoring result not fou'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-057 | Finding of SF-APPS-057: untestable
- confidence: 0.95
- derived_from: EXP:APPS-057 {family=SF-APPS-057; rule=family member}
- statement: No holdout hit-rate number found. Protocol states existing --full-calibrated 69.8% is in-sample until the holdout is run.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-APPS-057 | Hypothesis of SF-APPS-057
- addresses: RQC:RQC-078 {family=SF-APPS-057; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-057 {decided_by=APPS-057; family=SF-APPS-057; rule=automated adjudication stratum}
- source_record: APPS-057
- tested_by: EXP:APPS-057 {record=APPS-057; rule=family hypothesis tested by member record}
- text: A frozen-engine hit rate on 25 holdout series (cap_yy>23) is the defensible SQ2 number, vs in-sample 69.8%.
