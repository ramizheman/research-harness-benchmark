# FAM:SF-APPM-039 | Study family SF-APPM-039 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-039
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF-PAP-033 {family=SF-APPM-039; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.495}
- validation_evidence: APPM-039: 'utcomes); loo travel forecast; 500 random 50/50 calibration/holdout splits. loo corr 0.1998, auc 0.5986; holdout additive embed'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-039 | Finding of SF-APPM-039: supported
- confidence: 0.95
- derived_from: EXP:APPM-039 {family=SF-APPM-039; rule=family member}
- statement: LOO corr 0.1998, AUC 0.5986; holdout additive embedded 89.59% vs irrelevant 48.11%; P(add emb > irr)=0.984; P(add net > irr)=0.99; corr(travel,net) 0.1881.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPM-039 | Hypothesis of SF-APPM-039
- addresses: RQC:RQC-004 {family=SF-APPM-039; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPM-039
- supported_by: FIND:SF-APPM-039 {decided_by=APPM-039; family=SF-APPM-039; rule=automated adjudication stratum}
- tested_by: EXP:APPM-039 {record=APPM-039; rule=family hypothesis tested by member record}
- text: Forecast portability (travel) and fit quadrants predict mover outcomes (embedded minutes, net rating).
