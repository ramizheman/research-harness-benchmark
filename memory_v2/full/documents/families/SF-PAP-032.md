# FAM:SF-PAP-032 | Study family SF-PAP-032 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.65
- confidence_level: medium
- deciding_record: PAP-032
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPM-039 {family=SF-PAP-032; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.447}
- risk_code: LEAKAGE_LOOKAHEAD
- risk_code: OUTCOME_DERIVED_LABEL
- validation_evidence: PAP-032: ', not graph-circular. same-sample quadrants; pap-033 is the holdout upgrade. n=198 movers net-rating gap additive vs irrelevant'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-032 | Finding of SF-PAP-032: uncertain
- confidence: 0.65
- derived_from: EXP:PAP-032 {family=SF-PAP-032; rule=family member}
- statement: n=198; embedded mpg>=15: additive 0.80, redundant 0.85, missed-need 0.50, irrelevant 0.68; mean dest net: additive -0.63, redundant -0.35, missed-need -2.50, irrelevant -3.58; corr(delta, dest_net)=+0.077; corr(travel_score, dest_net)=+0.155; corr(fit_score, dest_net)=-0.056
- status: uncertain
- validation_status: same_pipeline_validation

# HYP:SF-PAP-032 | Hypothesis of SF-PAP-032
- addresses: RQC:RQC-004 {family=SF-PAP-032; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-PAP-032 {decided_by=PAP-032; family=SF-PAP-032; rule=automated adjudication stratum}
- source_record: PAP-032
- tested_by: EXP:PAP-032 {record=PAP-032; rule=family hypothesis tested by member record}
- text: The travel x fit quadrant (additive vs redundant/missed-need/irrelevant) predicts post-move minutes, usage, and destination on-court net rating.
