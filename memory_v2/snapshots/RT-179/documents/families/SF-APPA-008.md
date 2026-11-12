# FAM:SF-APPA-008 | Study family SF-APPA-008 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-008
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPA-008; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-008 | Finding of SF-APPA-008: artifact
- confidence: 0.95
- derived_from: EXP:APPA-008 {family=SF-APPA-008; rule=family member}
- rules_out: HYP:SF-APPA-008 {family=SF-APPA-008; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: 706 findings with n<5; list_h2h_games called 0 times; series winners LLM-inferred; MIA-BOS G7 score invented (BOS 100 vs graph 84); what_came_next skips a possession; point costs are LLM arithmetic.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-APPA-008 | Hypothesis of SF-APPA-008
- addresses: RQC:RQC-060 {family=SF-APPA-008; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPA-008 {decided_by=APPA-008; family=SF-APPA-008; rule=automated adjudication stratum}
- source_record: APPA-008
- tested_by: EXP:APPA-008 {record=APPA-008; rule=family hypothesis tested by member record}
- text: The agent batch's findings (defensive adjustments, point costs, adaptation predicts series winners 9/10) are valid.
