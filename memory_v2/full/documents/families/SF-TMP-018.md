# FAM:SF-TMP-018 | Study family SF-TMP-018 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-018
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:implementation_bug {family=SF-TMP-018; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:low_measurement_reliability {family=SF-TMP-018; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-TMP-018; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: IMPLEMENTATION_BUG
- risk_code: MEASURE_RELIABILITY
- validation_evidence: TMP-018: 'team-seasons; season-to-date shrunk priors; random-opponent placebo; payoff regression; split-half heterogeneity. tilt -2.353 p'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-018 | Finding of SF-TMP-018: rejected
- confidence: 0.95
- derived_from: EXP:TMP-018 {family=SF-TMP-018; rule=family member}
- rules_out: HYP:SF-TMP-018 {family=SF-TMP-018; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Tilt -2.353 pp per PPP (SE 1.212, t=-1.94); payoff +0.83 (SE 0.82); heterogeneity split-half r=+0.242, SB +0.389, p=0.020; CUT/POST/SPOT tilt -8.271 (SE 2.240).
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-TMP-018 | Hypothesis of SF-TMP-018
- addresses: RQC:RQC-192 {family=SF-TMP-018; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-TMP-018 {decided_by=TMP-018; family=SF-TMP-018; rule=automated adjudication stratum}
- source_record: TMP-018
- tested_by: EXP:TMP-018 {record=TMP-018; rule=family hypothesis tested by member record}
- text: Offenses tilt play-type mix toward play types tonight's opponent defended poorly in prior games, the tilt pays, and teams differ reliably.
