# FAM:SF-PAP-001 | Study family SF-PAP-001 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-001
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_evidence: PAP-001: '8 frozen pilot team-seasons, odd/even game split, min-overlap associ'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-001 | Finding of SF-PAP-001: supported
- confidence: 1.0
- derived_from: EXP:PAP-001 {family=SF-PAP-001; rule=family member}
- statement: C1 8/8 p<0.05; C2 S=0.319 within=43.027 between=134.770 perm_p=0.0002 (cosine S=0.154); C3 R2=0.080
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-PAP-001 | Hypothesis of SF-PAP-001
- addresses: RQC:RQC-158 {family=SF-PAP-001; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-001
- supported_by: FIND:SF-PAP-001 {decided_by=PAP-001; family=SF-PAP-001; rule=automated adjudication stratum}
- tested_by: EXP:PAP-001 {record=PAP-001; rule=family hypothesis tested by member record}
- text: Offensive play-type co-initiation association matrix clears a fixed-margin null, is team-persistent across split halves, and is not collinear with play-type rates (pilot).
