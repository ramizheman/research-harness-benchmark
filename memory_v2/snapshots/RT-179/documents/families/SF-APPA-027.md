# FAM:SF-APPA-027 | Study family SF-APPA-027 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-027
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPA-027; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPA-028 {family=SF-APPA-027; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.363}
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-027 | Finding of SF-APPA-027: untestable
- confidence: 0.95
- derived_from: EXP:APPA-027 {family=SF-APPA-027; rule=family member}
- statement: Agrees with BEST 1/3; picks AVOID 2/3; disagreements engine right 2/2; mean H2 PPP BEST 1.650, agent 1.154, AVOID 0.642.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-027 | Hypothesis of SF-APPA-027
- addresses: RQC:RQC-019 {family=SF-APPA-027; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-027 {decided_by=APPA-027; family=SF-APPA-027; rule=automated adjudication stratum}
- source_record: APPA-027
- tested_by: EXP:APPA-027 {record=APPA-027; rule=family hypothesis tested by member record}
- text: The LLM picks the same counter as the BEST tier, and when it disagrees it is right in H2.
