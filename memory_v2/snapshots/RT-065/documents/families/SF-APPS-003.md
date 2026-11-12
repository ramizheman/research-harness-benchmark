# FAM:SF-APPS-003 | Study family SF-APPS-003 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-003
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPS-003; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- repeat_order_unknown: FAM:SF-APPS-004 {family=SF-APPS-003; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.404}
- risk_code: LEAKAGE_LOOKAHEAD
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPS-003: 'the drive ban and cut ppp level were known before scoring. holdout protocol (tuning 17 series, holdout 25, sha 59a9be48) was w'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-003 | Finding of SF-APPS-003: artifact
- confidence: 0.95
- derived_from: EXP:APPS-003 {family=SF-APPS-003; rule=family member}
- rules_out: HYP:SF-APPS-003 {family=SF-APPS-003; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Full-calibrated headline 69.8% (37/53); DRIVE-modal (banned-PT) comparisons 85.7% (12/14); clean comparisons 64.1% (25/39); high-confidence 64.3% (27/42). CUT recs 13/13; POST_UP 0/4. Uncalibrated archival: 51.7% (31/60), high-conf 42.9%, DRIVE recs 8% (n=25).
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-APPS-003 | Hypothesis of SF-APPS-003
- addresses: RQC:RQC-035 {family=SF-APPS-003; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPS-003 {decided_by=APPS-003; family=SF-APPS-003; rule=automated adjudication stratum}
- source_record: APPS-003
- tested_by: EXP:APPS-003 {record=APPS-003; rule=family hypothesis tested by member record}
- text: The V4 engine's recommended play type outperforms the team's highest-volume play type in that playoff series.
