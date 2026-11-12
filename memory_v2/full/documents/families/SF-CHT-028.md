# FAM:SF-CHT-028 | Study family SF-CHT-028 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict failed_gate
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-028
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: DRIFT_NONSTATIONARITY
- validation_status: no_validation_recorded

# FIND:SF-CHT-028 | Finding of SF-CHT-028: untestable
- confidence: 1.0
- derived_from: EXP:CHT-028 {family=SF-CHT-028; rule=family member}
- statement: action_sequences CV=0.612, stability CV=0.919 (unstable); MERGE into possession_flow. Locked 9-pattern set with clutch_performance r(win)=+0.38.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-CHT-028 | Hypothesis of SF-CHT-028
- addresses: RQC:RQC-146 {family=SF-CHT-028; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-CHT-028 {decided_by=CHT-028; family=SF-CHT-028; rule=automated adjudication stratum}
- source_record: CHT-028
- tested_by: EXP:CHT-028 {record=CHT-028; rule=family hypothesis tested by member record}
- text: action_sequences is a stable, non-redundant tactical signal vs possession_flow.
