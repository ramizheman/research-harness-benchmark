# FAM:SF-APPM-048 | Study family SF-APPM-048 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-048
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPM-045 {family=SF-APPM-048; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:small_sample {family=SF-APPM-048; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPM-045 {family=SF-APPM-048; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.355}
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPM-048 | Finding of SF-APPM-048: untestable
- confidence: 0.95
- derived_from: EXP:APPM-048 {family=SF-APPM-048; rule=family member}
- statement: NYK modeled PPP 1.3240 vs observed 1.2487 (Delta -0.075, within 0.10 YES). PHI 1.2410 vs 1.0355 (Delta -0.205, within 0.10 NO). Predicted gap +0.0830 vs observed +0.2132 (same direction). NYK WP 84.0%; sweep 100%. Per-game NYK PPP 1.356 / 1.091 / 1.125 / 1.412. CUT share 6.0% + DRIVE 12.6% = 18.6% vs OTHER 28.4%.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPM-048 | Hypothesis of SF-APPM-048
- addresses: RQC:RQC-032 {family=SF-APPM-048; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPM-048 {decided_by=APPM-048; family=SF-APPM-048; rule=automated adjudication stratum}
- source_record: APPM-048
- tested_by: EXP:APPM-048 {record=APPM-048; rule=family hypothesis tested by member record}
- text: Pre-game modeled PPP gap and favorite match the series outcome and observed PPP within 0.10.
