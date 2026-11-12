# FAM:SF-APPS-009 | Study family SF-APPS-009 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-009
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: data-level limitation: small sample
- knowable_before_outcome_auto: yes_from_data
- limited_by: LIM:small_sample {family=SF-APPS-009; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-009 | Finding of SF-APPS-009: untestable
- confidence: 0.95
- derived_from: EXP:APPS-009 {family=SF-APPS-009; rule=family member}
- statement: 8 divergences, 0 scoreable, 8 unscored (player missing from Neo4j); hit rate n/a.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPS-009 | Hypothesis of SF-APPS-009
- addresses: RQC:RQC-017 {family=SF-APPS-009; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-009 {decided_by=APPS-009; family=SF-APPS-009; rule=automated adjudication stratum}
- source_record: APPS-009
- tested_by: EXP:APPS-009 {record=APPS-009; rule=family hypothesis tested by member record}
- text: V5 player routing picks players with higher observed PPP than V4 routing.
