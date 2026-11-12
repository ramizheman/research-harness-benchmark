# FAM:SF-APPM-001 | Study family SF-APPM-001 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-001
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_evidence: APPM-001: '908 holdout game-team rows (454 games), terciles of l1 distance actual'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-001 | Finding of SF-APPM-001: supported
- confidence: 0.95
- derived_from: EXP:APPM-001 {family=SF-APPM-001; rule=family member}
- statement: Raw gap aligned-deviated +5.18 ORtg; strength-controlled gap +3.27 ORtg (+0.0193 vs -0.0134 PPP residual). Model regret median +25.94 ORtg (non-negative by construction).
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPM-001 | Hypothesis of SF-APPM-001
- addresses: RQC:RQC-024 {family=SF-APPM-001; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPM-001
- supported_by: FIND:SF-APPM-001 {decided_by=APPM-001; family=SF-APPM-001; rule=automated adjudication stratum}
- tested_by: EXP:APPM-001 {record=APPM-001; rule=family hypothesis tested by member record}
- text: Holdout games where a team's play-type mix is closer to the model's recommended mix score more efficiently.
