# FAM:SF-PAP-081 | Study family SF-PAP-081 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-081
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:low_power_large_MDE {family=SF-PAP-081; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-PAP-081; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-PAP-084 {family=SF-PAP-081; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.423}
- risk_code: MECHANICAL_FLOOR
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-081 | Finding of SF-PAP-081: untestable
- confidence: 1.0
- derived_from: EXP:PAP-081 {family=SF-PAP-081; rule=family member}
- statement: three residual r=+0.010 CI[-0.031,+0.053]; rim -0.122 [-0.167,-0.077]; PPP -0.070 [-0.110,-0.033]; response r 5/5=0.14 [-0.12,0.39] n=63 MDE r=0.36; 3/3 r=0.056 [0.003,0.109] n=1,385
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-PAP-081 | Hypothesis of SF-PAP-081
- addresses: RQC:RQC-070 {family=SF-PAP-081; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-081 {decided_by=PAP-081; family=SF-PAP-081; rule=automated adjudication stratum}
- source_record: PAP-081
- tested_by: EXP:PAP-081 {record=PAP-081; rule=family hypothesis tested by member record}
- text: Matchup-specific shot mix or treated-minus-control response repeats from earlier to later meetings.
