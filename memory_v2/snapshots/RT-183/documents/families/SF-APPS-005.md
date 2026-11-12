# FAM:SF-APPS-005 | Study family SF-APPS-005 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-005
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: DRIFT_NONSTATIONARITY
- validation_status: no_validation_recorded

# FIND:SF-APPS-005 | Finding of SF-APPS-005: artifact
- confidence: 0.95
- derived_from: EXP:APPS-005 {family=SF-APPS-005; rule=family member}
- rules_out: HYP:SF-APPS-005 {family=SF-APPS-005; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: ~92.6% hit rate
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-APPS-005 | Hypothesis of SF-APPS-005
- addresses: RQC:RQC-094 {family=SF-APPS-005; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPS-005 {decided_by=APPS-005; family=SF-APPS-005; rule=automated adjudication stratum}
- source_record: APPS-005
- tested_by: EXP:APPS-005 {record=APPS-005; rule=family hypothesis tested by member record}
- text: Teams' in-series play-type choices matched what the engine said they should do and this predicted success.
