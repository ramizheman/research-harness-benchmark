# FAM:SF-PAP-051 | Study family SF-PAP-051 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: PAP-051
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_status: no_validation_recorded

# FIND:SF-PAP-051 | Finding of SF-PAP-051: supported
- confidence: 0.95
- derived_from: EXP:PAP-051 {family=SF-PAP-051; rule=family member}
- statement: g1_mc median=0.0053 mean=0.0072; g1_scale median=0.0070 mean=0.0090; 95th pct scale=0.0265 from CSV (script also cites sampling-null median ~0.078)
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-051 | Hypothesis of SF-PAP-051
- addresses: RQC:RQC-172 {family=SF-PAP-051; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-051
- supported_by: FIND:SF-PAP-051 {decided_by=PAP-051; family=SF-PAP-051; rule=automated adjudication stratum}
- tested_by: EXP:PAP-051 {record=PAP-051; rule=family hypothesis tested by member record}
- text: Uniformly scaling remaining teammates' initiation rows by 1.25 leaves the unit fingerprint at Monte Carlo noise (so restoration is not mere volume).
