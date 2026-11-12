# FAM:SF-APPS-070 | Study family SF-APPS-070 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-070
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-APPS-070; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: RTM_SELECTION
- validation_status: no_validation_recorded

# FIND:SF-APPS-070 | Finding of SF-APPS-070: rejected
- confidence: 0.95
- derived_from: EXP:APPS-070 {family=SF-APPS-070; rule=family member}
- rules_out: HYP:SF-APPS-070 {family=SF-APPS-070; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Test B: all BH-adjusted null/WEAK (PNR ATT=+0.0313 BH_p=0.0658 WEAK; others NULL). Test C top-1 acc=0.550 vs mean-reversion baseline 0.511 (+0.039) vs most-used 0.239. Test A PULL_UP slope -0.0581 p=0.0030; CUT -0.0917 p=0.0410; PNR +0.0562 p=0.0005 (wrong sign for suppression).
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-070 | Hypothesis of SF-APPS-070
- addresses: RQC:RQC-118 {family=SF-APPS-070; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-070 {decided_by=APPS-070; family=SF-APPS-070; rule=automated adjudication stratum}
- source_record: APPS-070
- tested_by: EXP:APPS-070 {record=APPS-070; rule=family hypothesis tested by member record}
- text: First-half reliance on a play type predicts second-half suppression after controlling for H1 PPP / mean reversion.
