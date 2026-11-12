# FAM:SF-PAP-054 | Study family SF-PAP-054 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict failed_gate
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-054
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: data-level limitation: low measurement reliability
- knowable_before_outcome_auto: yes_from_data
- limited_by: LIM:low_measurement_reliability {family=SF-PAP-054; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- repeat_of_earlier_family: FAM:SF-TMP-017 {family=SF-PAP-054; order=before; rule=lexical similarity >= repeat threshold; similarity=0.354}
- risk_code: MEASURE_RELIABILITY
- validation_evidence: PAP-054: '>=0.02; paper: roughly twice as many spells would be needed split-half reliability 0.32 < 0.40; 0.01 among l_pre>=0.02'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-054 | Finding of SF-PAP-054: untestable
- confidence: 1.0
- derived_from: EXP:PAP-054 {family=SF-PAP-054; rule=family member}
- statement: SB restoration all spells 0.32; among 53 spells with L_pre>=0.02, SB=0.01 (CSV Spearman +0.004); excess-reorganization upper bound 0.38
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-PAP-054 | Hypothesis of SF-PAP-054
- addresses: RQC:RQC-065 {family=SF-PAP-054; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-054 {decided_by=PAP-054; family=SF-PAP-054; rule=automated adjudication stratum}
- source_record: PAP-054
- tested_by: EXP:PAP-054 {record=PAP-054; rule=family hypothesis tested by member record}
- text: Per-spell restoration is reliable enough (Spearman-Brown >=0.40) to test predictors of who rebuilds.
