# FAM:SF-PAP-044 | Study family SF-PAP-044 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-044
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-PAP-044; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-PAP-044; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_of_earlier_family: FAM:SF08 {family=SF-PAP-044; order=before; rule=lexical similarity >= repeat threshold; similarity=0.392}
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: PAP-044: '30 teams on 2025-26 rs holdout; pearson r of best-tier share vs official win%. pearson r=+'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-044 | Finding of SF-PAP-044: rejected
- confidence: 1.0
- derived_from: EXP:PAP-044 {family=SF-PAP-044; rule=family member}
- rules_out: HYP:SF-PAP-044 {family=SF-PAP-044; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Pearson r=+0.25 across 30 teams
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-044 | Hypothesis of SF-PAP-044
- addresses: RQC:RQC-001 {family=SF-PAP-044; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-044 {decided_by=PAP-044; family=SF-PAP-044; rule=automated adjudication stratum}
- source_record: PAP-044
- tested_by: EXP:PAP-044 {record=PAP-044; rule=family hypothesis tested by member record}
- text: Teams that follow BEST-tier counters more often win more.
