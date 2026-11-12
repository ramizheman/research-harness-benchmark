# FAM:SF-APPM-004 | Study family SF-APPM-004 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-004
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- validation_evidence: APPM-004: '690 val / 520 holdout cells: variance ratios, slope test, drop-one and single-fea'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-004 | Finding of SF-APPM-004: artifact
- confidence: 0.95
- derived_from: EXP:APPM-004 {family=SF-APPM-004; rule=family member}
- rules_out: HYP:SF-APPM-004 {family=SF-APPM-004; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: pred_cal variance 3.9% of actual; pred_raw alone R2 +0.0042; dropping pred_raw changes R2 by +0.0002; team_mult alone +0.0392.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-APPM-004 | Hypothesis of SF-APPM-004
- addresses: RQC:RQC-063 {family=SF-APPM-004; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPM-004 {decided_by=APPM-004; family=SF-APPM-004; rule=automated adjudication stratum}
- source_record: APPM-004
- tested_by: EXP:APPM-004 {record=APPM-004; rule=family hypothesis tested by member record}
- text: The calibrated pipeline preserves enough variance and the matchup model pred_raw carries usable signal.
