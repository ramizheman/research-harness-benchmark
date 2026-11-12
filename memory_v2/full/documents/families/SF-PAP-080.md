# FAM:SF-PAP-080 | Study family SF-PAP-080 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-080
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: PAP-080: '4 pp of 0 design is not blind to personnel. fake-timing and permutation placebos consistent with null opponent effect. own-only +3'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-080 | Finding of SF-PAP-080: supported
- confidence: 1.0
- derived_from: EXP:PAP-080 {family=SF-PAP-080; rule=family member}
- statement: own-only three +3.1 pp (SE 1.2); rim -1.1 (1.1); mid -2.0 (1.1); opponent-only all within 1.4 pp of 0
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-PAP-080 | Hypothesis of SF-PAP-080
- addresses: RQC:RQC-023 {family=SF-PAP-080; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-080
- supported_by: FIND:SF-PAP-080 {decided_by=PAP-080; family=SF-PAP-080; rule=automated adjudication stratum}
- tested_by: EXP:PAP-080 {record=PAP-080; rule=family hypothesis tested by member record}
- text: Changing the offensive five itself moves shot mix, showing the design can detect personnel effects.
