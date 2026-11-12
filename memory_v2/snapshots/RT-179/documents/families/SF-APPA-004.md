# FAM:SF-APPA-004 | Study family SF-APPA-004 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-004
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-APPA-004; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPA-004; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-004 | Finding of SF-APPA-004: untestable
- confidence: 0.95
- derived_from: EXP:APPA-004 {family=SF-APPA-004; rule=family member}
- statement: Adapters 4/8 rows; mean dPPP adapters +0.0327 vs non-adapters -0.2987. A2 could not be computed: no SHOULD vector in correction_log.json.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-004 | Hypothesis of SF-APPA-004
- addresses: RQC:RQC-002 {family=SF-APPA-004; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-004 {decided_by=APPA-004; family=SF-APPA-004; rule=automated adjudication stratum}
- source_record: APPA-004
- tested_by: EXP:APPA-004 {record=APPA-004; rule=family hypothesis tested by member record}
- text: Within-game and within-series adaptation toward engine counters coincides with better PPP in one series.
