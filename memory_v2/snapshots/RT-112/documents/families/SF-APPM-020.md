# FAM:SF-APPM-020 | Study family SF-APPM-020 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-020
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPA-004 {family=SF-APPM-020; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:small_sample {family=SF-APPM-020; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPA-024 {family=SF-APPM-020; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.375}
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPM-020 | Finding of SF-APPM-020: untestable
- confidence: 0.95
- derived_from: EXP:APPM-020 {family=SF-APPM-020; rule=family member}
- statement: Shift toward rec PT: win rate 50.0% vs 50.0%; only 8 rows had a SHOULD vector (aligned 4/6 wins vs 1/2); A3 rec PT beat modal PT 87/94 (92.6%).
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPM-020 | Hypothesis of SF-APPM-020
- addresses: RQC:RQC-002 {family=SF-APPM-020; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPM-020 {decided_by=APPM-020; family=SF-APPM-020; rule=automated adjudication stratum}
- source_record: APPM-020
- tested_by: EXP:APPM-020 {record=APPM-020; rule=family hypothesis tested by member record}
- text: Teams that shift toward the engine's prescribed mix win more and improve PPP.
