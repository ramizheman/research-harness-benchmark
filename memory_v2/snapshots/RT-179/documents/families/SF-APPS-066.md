# FAM:SF-APPS-066 | Study family SF-APPS-066 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-066
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPS-066; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: PLACEBO_DEPENDENCE
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPS-066: '99 bos drive->tatum-pnr chains (brown 43 / other 56). placebo 5000 relabels; also league-wide teammate-drive->pnr. reprod'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-066 | Finding of SF-APPS-066: artifact
- confidence: 0.95
- derived_from: EXP:APPS-066 {family=SF-APPS-066; rule=family member}
- rules_out: HYP:SF-APPS-066 {family=SF-APPS-066; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Reproduced premium +0.3262 n=43 vs Tatum PNR baseline 1.0459. Brown-other gap +0.3185, MW p=0.1702. Placebo 95% [-0.1389,+0.4192], observed inside, p=0.1136; perm p=0.2034. League teammate-DRIVE->PNR controlled beta=+0.0220 p=0.0044 n_t=20658 (tiny). Tatum any-teammate +0.1524 p=0.2546, perm inside.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-APPS-066 | Hypothesis of SF-APPS-066
- addresses: RQC:RQC-010 {family=SF-APPS-066; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPS-066 {decided_by=APPS-066; family=SF-APPS-066; rule=automated adjudication stratum}
- source_record: APPS-066
- tested_by: EXP:APPS-066 {record=APPS-066; rule=family hypothesis tested by member record}
- text: The reported +0.326 Brown->Tatum PNR premium is Brown-specific, not any-teammate DRIVE->Tatum PNR.
