# FAM:SF-TMP-039 | Study family SF-TMP-039 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict abandoned, mechanism E_unclear, no power information
- confidence: 0.65
- confidence_level: medium
- deciding_record: TMP-039
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: abandoned
- validation_status: no_validation_recorded

# FIND:SF-TMP-039 | Finding of SF-TMP-039: uncertain
- confidence: 0.65
- derived_from: EXP:TMP-039 {family=SF-TMP-039; rule=family member}
- statement: built 90 team-season tensors from full_edges.parquet in 16.7s
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-TMP-039 | Hypothesis of SF-TMP-039
- addresses: RQC:RQC-198 {family=SF-TMP-039; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-TMP-039 {decided_by=TMP-039; family=SF-TMP-039; rule=automated adjudication stratum}
- source_record: TMP-039
- tested_by: EXP:TMP-039 {record=TMP-039; rule=family hypothesis tested by member record}
- text: Recompute and lock all tables and statistics for When a Hub Sits from full_edges.parquet.
