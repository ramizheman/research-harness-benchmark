# FAM:SF-PAP-033 | Study family SF-PAP-033 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: PAP-033
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF-APPM-039 {family=SF-PAP-033; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.489}
- validation_evidence: PAP-033: 'splits, half~99 additive>irrelevant on net rating in 96% of holdout splits; minutes gap positive in 84%'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-033 | Finding of SF-PAP-033: supported
- confidence: 0.95
- derived_from: EXP:PAP-033 {family=SF-PAP-033; rule=family member}
- statement: 500 splits; embedded-rate gap median=+0.116 [10-90% -0.033, +0.248] P(>0)=0.838; net-rtg gap median=+2.926 [+0.541, +5.072] P(>0)=0.960; corr(travel forecast, net rtg) median=+0.178 P(>0)=0.976; corr(delta, net) median=+0.068 P(>0)=0.822
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-PAP-033 | Hypothesis of SF-PAP-033
- addresses: RQC:RQC-004 {family=SF-PAP-033; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-033
- supported_by: FIND:SF-PAP-033 {decided_by=PAP-033; family=SF-PAP-033; rule=automated adjudication stratum}
- tested_by: EXP:PAP-033 {record=PAP-033; rule=family hypothesis tested by member record}
- text: Additive > irrelevant on destination embedded minutes and on-court net rating survives when travel OLS and medians are fit on a calibration half and scored on holdout.
