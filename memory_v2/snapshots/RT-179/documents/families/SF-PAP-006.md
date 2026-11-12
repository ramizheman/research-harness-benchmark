# FAM:SF-PAP-006 | Study family SF-PAP-006 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-006
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_status: no_validation_recorded

# FIND:SF-PAP-006 | Finding of SF-PAP-006: supported
- confidence: 1.0
- derived_from: EXP:PAP-006 {family=SF-PAP-006; rule=family member}
- statement: rho(resid,net rating)=-0.018; rho(L,net rating)=+0.203; adj net rating organizers +1.22 vs shapers +0.50, p=0.10 (Mann-Whitney)
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-006 | Hypothesis of SF-PAP-006
- addresses: RQC:RQC-052 {family=SF-PAP-006; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-006
- supported_by: FIND:SF-PAP-006 {decided_by=PAP-006; family=SF-PAP-006; rule=automated adjudication stratum}
- tested_by: EXP:PAP-006 {record=PAP-006; rule=family hypothesis tested by member record}
- text: Residual structural influence is not a disguised value metric (no relation to net rating).
