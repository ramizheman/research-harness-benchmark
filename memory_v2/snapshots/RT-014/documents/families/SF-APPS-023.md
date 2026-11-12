# FAM:SF-APPS-023 | Study family SF-APPS-023 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-023
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-APPS-023; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPS-023; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPS-024 {family=SF-APPS-023; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.508}
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-023 | Finding of SF-APPS-023: rejected
- confidence: 0.95
- derived_from: EXP:APPS-023 {family=SF-APPS-023; rule=family member}
- rules_out: HYP:SF-APPS-023 {family=SF-APPS-023; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: All BEST vs mix: 1.481 vs 1.212, gap=+0.269, p=0.0000, n=283. Non-CUT BEST vs mix: 1.216 vs 1.206, gap=+0.010, p=0.1709, n=136. L3_MATCHUP non-CUT: gap=+0.001, p=0.3277, n=47. BEST vs AVOID gap=+0.692, p=0.0000, n=169. 147/283 BEST are CUT (51.9%).
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-023 | Hypothesis of SF-APPS-023
- addresses: RQC:RQC-024 {family=SF-APPS-023; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-023 {decided_by=APPS-023; family=SF-APPS-023; rule=automated adjudication stratum}
- source_record: APPS-023
- tested_by: EXP:APPS-023 {record=APPS-023; rule=family hypothesis tested by member record}
- text: Matchup-specific (non-CUT) BEST counters beat a feasibility-weighted league mix that ignores game state.
