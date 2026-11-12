# FAM:SF-APPS-056 | Study family SF-APPS-056 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPS-056
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: DRIFT_NONSTATIONARITY
- validation_evidence: APPS-056: 'djusted spearman phi 0.714, bos 0.452. chat 6 also cites rs holdout methodology rho=0.54, n=454, mae 0.0922 ppp from pipeline_r'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-056 | Finding of SF-APPS-056: uncertain
- confidence: 0.65
- derived_from: EXP:APPS-056 {family=SF-APPS-056; rule=family member}
- statement: Winner: 27 CONFIRMED / 18 CONTRADICTED of 45 (60%). Canonical-10 team-side Spearman median ~0.536 (20 sides); series-mean median ~0.554. Example phi_bos_2526: predicted BOS (85.2% conf, PHI baseline 7.4%) CONTRADICTED (PHI 4-3); scheme-adjusted Spearman PHI 0.714, BOS 0.452. Chat 6 also cites RS holdout methodology rho=0.54, n=454, MAE 0.0922 PPP from pipeline_report_metadata.json.
- status: uncertain
- validation_status: same_pipeline_validation

# HYP:SF-APPS-056 | Hypothesis of SF-APPS-056
- addresses: RQC:RQC-107 {family=SF-APPS-056; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPS-056 {decided_by=APPS-056; family=SF-APPS-056; rule=automated adjudication stratum}
- source_record: APPS-056
- tested_by: EXP:APPS-056 {record=APPS-056; rule=family hypothesis tested by member record}
- text: Pregame predicted series winner and predicted PT-PPP ranks match realized playoff series outcomes.
