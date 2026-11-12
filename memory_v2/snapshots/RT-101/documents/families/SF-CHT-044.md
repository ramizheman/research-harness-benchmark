# FAM:SF-CHT-044 | Study family SF-CHT-044 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-044
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: inconclusive
- validation_evidence: CHT-044: '7 kept as exploratory. files in sequence_memory / playsheet_validation mentioned in later audits. h17 is real ~+0.12 but using it'
- validation_status: same_pipeline_validation

# FIND:SF-CHT-044 | Finding of SF-CHT-044: uncertain
- confidence: 0.8
- derived_from: EXP:CHT-044 {family=SF-CHT-044; rule=family member}
- statement: H17 PNR/CUT/DRIVE etc. ~+0.12 to +0.13 PPP (8/8 PTs). Sequence lags flat d~0.01-0.03, failed; H26 removed from engine. Suppression control opponent same PT H1-H2 +0.011 PPP.
- status: uncertain
- validation_status: same_pipeline_validation

# HYP:SF-CHT-044 | Hypothesis of SF-CHT-044
- addresses: RQC:RQC-041 {family=SF-CHT-044; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-CHT-044 {decided_by=CHT-044; family=SF-CHT-044; rule=automated adjudication stratum}
- source_record: CHT-044
- tested_by: EXP:CHT-044 {record=CHT-044; rule=family hypothesis tested by member record}
- text: Opponent next-possession PPP after you run play X is large enough to drive AVOID labels; own-sequence lags similarly matter.
