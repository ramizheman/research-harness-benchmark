# FAM:SF-CHT-039 | Study family SF-CHT-039 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-039
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:confounding {family=SF-CHT-039; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-CHT-039; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: CONFOUNDING
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-CHT-039 | Finding of SF-CHT-039: untestable
- confidence: 1.0
- derived_from: EXP:CHT-039 {family=SF-CHT-039; rule=family member}
- statement: Game-level rho=-0.19 p=0.008 (inflated n, team-quality confound). Series-level rho=-0.26 p=0.07 (n=50, underpowered; ~80 series needed for p<0.05). Low AVOID-share bin 52.6% vs 25-50% bin 37.0%.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-CHT-039 | Hypothesis of SF-CHT-039
- addresses: RQC:RQC-103 {family=SF-CHT-039; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-CHT-039 {decided_by=CHT-039; family=SF-CHT-039; rule=automated adjudication stratum}
- source_record: CHT-039
- tested_by: EXP:CHT-039 {record=CHT-039; rule=family hypothesis tested by member record}
- text: Higher AVOID share predicts losing, independent of team quality.
