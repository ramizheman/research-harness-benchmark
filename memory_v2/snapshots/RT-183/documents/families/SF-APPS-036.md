# FAM:SF-APPS-036 | Study family SF-APPS-036 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: APPS-036
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPS-036; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF-APPA-048 {family=SF-APPS-036; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.452}
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-036 | Finding of SF-APPS-036: supported
- confidence: 1.0
- derived_from: EXP:APPS-036 {family=SF-APPS-036; rule=family member}
- statement: Mean gap (n>=10 each tier) +0.427 PPP. Mean BEST 1.347 (38 players) vs AVOID 0.920 (94 players). Stars mean gap +0.542 (n=15) vs role +0.428 (n=16). Only 3 players clear n>=30 both tiers (all BOS: White +0.864, Brown +0.466, Tatum +0.391).
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPS-036 | Hypothesis of SF-APPS-036
- addresses: RQC:RQC-001 {family=SF-APPS-036; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-036
- supported_by: FIND:SF-APPS-036 {decided_by=APPS-036; family=SF-APPS-036; rule=automated adjudication stratum}
- tested_by: EXP:APPS-036 {record=APPS-036; rule=family hypothesis tested by member record}
- text: The team-level BEST vs AVOID gap holds when H2 possessions are filtered to initiating player.
