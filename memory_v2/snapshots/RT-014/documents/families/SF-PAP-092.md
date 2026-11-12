# FAM:SF-PAP-092 | Study family SF-PAP-092 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: PAP-092
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: data-level limitation: data scarcity (text pattern)
- knowable_before_outcome_auto: yes_from_data
- limited_by: LIM:data_scarcity_text_pattern {family=SF-PAP-092; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: DRIFT_NONSTATIONARITY
- validation_evidence: PAP-092: 'full loso 2003-2025; version a add 6 kp features; version b drop pom/'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-092 | Finding of SF-PAP-092: untestable
- confidence: 0.95
- derived_from: EXP:PAP-092 {family=SF-PAP-092; rule=family member}
- statement: baseline 0.17405; A 0.17453 (delta +0.00048); B 0.17525 (+0.00120); coverage 753/1449 (52.0%)
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-PAP-092 | Hypothesis of SF-PAP-092
- addresses: RQC:RQC-108 {family=SF-PAP-092; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-092 {decided_by=PAP-092; family=SF-PAP-092; rule=automated adjudication stratum}
- source_record: PAP-092
- tested_by: EXP:PAP-092 {record=PAP-092; rule=family hypothesis tested by member record}
- text: KenPom preseason/final AdjO/AdjD and momentum beat or replace pom_rank/trk_rank.
