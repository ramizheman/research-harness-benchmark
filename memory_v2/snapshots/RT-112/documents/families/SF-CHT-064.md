# FAM:SF-CHT-064 | Study family SF-CHT-064 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-064
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: data-level limitation: low measurement reliability
- knowable_before_outcome_auto: yes_from_data
- limited_by: LIM:low_measurement_reliability {family=SF-CHT-064; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-TMP-005 {family=SF-CHT-064; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.425}
- risk_code: MEASURE_RELIABILITY
- risk_code: MECHANICAL_FLOOR
- validation_evidence: CHT-064: 'split-half (two halves of a season) correlation across 120 team-season'
- validation_status: same_pipeline_validation

# FIND:SF-CHT-064 | Finding of SF-CHT-064: untestable
- confidence: 1.0
- derived_from: EXP:CHT-064 {family=SF-CHT-064; rule=family member}
- statement: H2-change trait r=-0.001 (p<.05 needs ~0.18). H1 defensive level r=+0.356 (test works). Season-to-season -0.19, -0.26, +0.16. Offensive H2-change r=+0.139 ns.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-CHT-064 | Hypothesis of SF-CHT-064
- addresses: RQC:RQC-003 {family=SF-CHT-064; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-CHT-064 {decided_by=CHT-064; family=SF-CHT-064; rule=automated adjudication stratum}
- source_record: CHT-064
- tested_by: EXP:CHT-064 {record=CHT-064; rule=family hypothesis tested by member record}
- text: A defense's effect on opponents' H2-H1 change is a reliable team trait.
