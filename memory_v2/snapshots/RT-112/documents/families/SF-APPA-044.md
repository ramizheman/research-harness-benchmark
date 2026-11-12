# FAM:SF-APPA-044 | Study family SF-APPA-044 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: APPA-044
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPA-044; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-044 | Finding of SF-APPA-044: supported
- confidence: 1.0
- derived_from: EXP:APPA-044 {family=SF-APPA-044; rule=family member}
- statement: 64/78 (82%) (off, PT) cells have >1 oracle player across opponents; 19/78 dominated by one player (>=90%); median oracle-player entropy 0.928.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPA-044 | Hypothesis of SF-APPA-044
- addresses: RQC:RQC-029 {family=SF-APPA-044; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPA-044
- supported_by: FIND:SF-APPA-044 {decided_by=APPA-044; family=SF-APPA-044; rule=automated adjudication stratum}
- tested_by: EXP:APPA-044 {record=APPA-044; rule=family hypothesis tested by member record}
- text: The oracle BEST player for a counter play type varies by opponent, not a single team identity.
