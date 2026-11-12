# FAM:SF-APPA-010 | Study family SF-APPA-010 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPA-010
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: inconclusive
- validation_evidence: APPA-010: '240 matchups, 23,922 holdout possessions; iterative best-response to approximate nash eq'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-010 | Finding of SF-APPA-010: uncertain
- confidence: 0.65
- derived_from: EXP:APPA-010 {family=SF-APPA-010; rule=family member}
- statement: Eq vs actual +1.16 pts/100; beats actual 127/240 (53%); vs baseline eq +8.52 pts/100; converged 159/240.
- status: uncertain
- validation_status: same_pipeline_validation

# HYP:SF-APPA-010 | Hypothesis of SF-APPA-010
- addresses: RQC:RQC-080 {family=SF-APPA-010; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPA-010 {decided_by=APPA-010; family=SF-APPA-010; rule=automated adjudication stratum}
- source_record: APPA-010
- tested_by: EXP:APPA-010 {record=APPA-010; rule=family hypothesis tested by member record}
- text: The system's offensive strategy survives optimal defensive adjustment and beats what teams ran.
