# FAM:SF-APPM-003 | Study family SF-APPM-003 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-003
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_evidence: APPM-003: '17 sequences; calibrators fit on val (690 cells), scored on holdout (520 cells); with and without 30-game recency half-life. ho'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-003 | Finding of SF-APPM-003: supported
- confidence: 0.95
- derived_from: EXP:APPM-003 {family=SF-APPM-003; rule=family member}
- statement: Holdout R2 baseline -0.1981 -> OLS +0.0323 (net lift +0.2305); HL30 variant baseline -0.1587 -> OLS +0.0321. Per-team R2 val +0.2449 but holdout +0.0213.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPM-003 | Hypothesis of SF-APPM-003
- addresses: RQC:RQC-034 {family=SF-APPM-003; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPM-003
- supported_by: FIND:SF-APPM-003 {decided_by=APPM-003; family=SF-APPM-003; rule=automated adjudication stratum}
- tested_by: EXP:APPM-003 {record=APPM-003; rule=family hypothesis tested by member record}
- text: A residual calibrator fit on VAL improves out-of-sample R2 of the equilibrium matchup evaluator.
