# FAM:SF-APPM-023 | Study family SF-APPM-023 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-023
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPM-023; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPM-023: 'her seed. per_team calibrator chosen on val r2 0.242 though holdout r2 earlier was 0.0213. n=4 games equal-weight pooling of 4'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-023 | Finding of SF-APPM-023: artifact
- confidence: 0.95
- derived_from: EXP:APPM-023 {family=SF-APPM-023; rule=family member}
- rules_out: HYP:SF-APPM-023 {family=SF-APPM-023; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Pooled: ORL 59%/DET 41% (8 seed favored); fixed: DET 86%/ORL 14%; all 4 now favor higher seed.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-APPM-023 | Hypothesis of SF-APPM-023
- addresses: RQC:RQC-096 {family=SF-APPM-023; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPM-023 {decided_by=APPM-023; family=SF-APPM-023; rule=automated adjudication stratum}
- source_record: APPM-023
- tested_by: EXP:APPM-023 {record=APPM-023; rule=family hypothesis tested by member record}
- text: Win probabilities from the decision context favor the higher seed in 4 2025-26 R1 matchups.
