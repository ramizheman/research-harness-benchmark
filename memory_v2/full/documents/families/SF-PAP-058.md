# FAM:SF-PAP-058 | Study family SF-PAP-058 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-058
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:low_power_large_MDE {family=SF-PAP-058; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: PAP-058: '2,+0.166] p=0.62; to +0.033 p=0.70; ft rate +0.161 p=0.061; robustness 915 player-seasons partial rho(l, deltappp|opp)=-0.087;'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-058 | Finding of SF-PAP-058: rejected
- confidence: 1.0
- derived_from: EXP:PAP-058 {family=SF-PAP-058; rule=family member}
- rules_out: HYP:SF-PAP-058 {family=SF-PAP-058; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: paper: essentially no relationship on 986; S3 PPP rho=-0.040 CI[-0.212,+0.166] p=0.62; TO +0.033 p=0.70; FT rate +0.161 p=0.061; robustness 915 player-seasons partial rho(L, DeltaPPP|opp)=-0.087; MDE rho~0.23
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-058 | Hypothesis of SF-PAP-058
- addresses: RQC:RQC-068 {family=SF-PAP-058; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-058 {decided_by=PAP-058; family=SF-PAP-058; rule=automated adjudication stratum}
- source_record: PAP-058
- tested_by: EXP:PAP-058 {record=PAP-058; rule=family hypothesis tested by member record}
- text: How much the offense reorganizes (relative to L) predicts the change in points per possession.
