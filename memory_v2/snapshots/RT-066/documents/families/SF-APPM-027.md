# FAM:SF-APPM-027 | Study family SF-APPM-027 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-027
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPM-027; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPM-027 | Finding of SF-APPM-027: untestable
- confidence: 0.95
- derived_from: EXP:APPM-027 {family=SF-APPM-027; rule=family member}
- statement: Smart-share edge +0.0307 (winner higher in 50% of upsets); 2024-25 +0.0616 (48%).
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPM-027 | Hypothesis of SF-APPM-027
- addresses: RQC:RQC-093 {family=SF-APPM-027; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPM-027 {decided_by=APPM-027; family=SF-APPM-027; rule=automated adjudication stratum}
- source_record: APPM-027
- tested_by: EXP:APPM-027 {record=APPM-027; rule=family hypothesis tested by member record}
- text: Upset winners ran more BEST + AVOID_OVERRIDE plays.
