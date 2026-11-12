# FAM:SF-APPS-060 | Study family SF-APPS-060 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-060
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_evidence: APPS-060: 'season x offensive team. cluster bootstrap 1000; perm 2000; placebo 1000; bh across 64. min n=30. 1 of 64 survived matching+bh+'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-060 | Finding of SF-APPS-060: rejected
- confidence: 0.95
- derived_from: EXP:APPS-060 {family=SF-APPS-060; rule=family member}
- rules_out: HYP:SF-APPS-060 {family=SF-APPS-060; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: 1 of 64 survived matching+BH+placebo: CUT->PNR ATT=-0.0502*. Top unsigned ATT PUTBACK->PUTBACK +0.0615 CI[-0.060,+0.168] not sig. TRANSITION->DRIVE +0.0355 perm_p=0.0020 BH_adj_p=0.0640.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPS-060 | Hypothesis of SF-APPS-060
- addresses: RQC:RQC-044 {family=SF-APPS-060; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-060 {decided_by=APPS-060; family=SF-APPS-060; rule=automated adjudication stratum}
- source_record: APPS-060
- tested_by: EXP:APPS-060 {record=APPS-060; rule=family hypothesis tested by member record}
- text: Predecessor play type A changes PPP of next play type B after exact matching, surviving BH-FDR and placebo.
