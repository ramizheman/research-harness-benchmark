# FAM:SF-APPA-028 | Study family SF-APPA-028 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-028
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPA-027 {family=SF-APPA-028; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:implementation_bug {family=SF-APPA-028; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPA-028; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPA-027 {family=SF-APPA-028; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.363}
- risk_code: IMPLEMENTATION_BUG
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-028 | Finding of SF-APPA-028: untestable
- confidence: 0.95
- derived_from: EXP:APPA-028 {family=SF-APPA-028; rule=family member}
- statement: Agreement 2/5 (40%); disagreements 3: debate wins 1, optimizer 1, tie 1; mean H2 PPP optimizer 1.812 vs debate 1.683.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-028 | Hypothesis of SF-APPA-028
- addresses: RQC:RQC-019 {family=SF-APPA-028; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-028 {decided_by=APPA-028; family=SF-APPA-028; rule=automated adjudication stratum}
- source_record: APPA-028
- tested_by: EXP:APPA-028 {record=APPA-028; rule=family hypothesis tested by member record}
- text: The LLM debate adds value over the deterministic optimizer counter.
