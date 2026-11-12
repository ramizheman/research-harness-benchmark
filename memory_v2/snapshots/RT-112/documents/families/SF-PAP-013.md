# FAM:SF-PAP-013 | Study family SF-PAP-013 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.45
- confidence_level: low
- deciding_record: PAP-013
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: inconclusive
- repeated_by_later_family: FAM:SF-PAP-011 {family=SF-PAP-013; order=after; rule=lexical similarity >= repeat threshold; similarity=0.4}
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: MULTIPLE_TESTING
- validation_status: no_validation_recorded

# FIND:SF-PAP-013 | Finding of SF-PAP-013: uncertain
- confidence: 0.45
- derived_from: EXP:PAP-013 {family=SF-PAP-013; rule=family member}
- statement: beta3 HasShaper x Clutch = -5.13 pts/100, t=-2.93, p=0.0034, ts-bootstrap CI[-8.64,-1.65]; main HasShaper +0.17 (p=0.80)
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-PAP-013 | Hypothesis of SF-PAP-013
- addresses: RQC:RQC-057 {family=SF-PAP-013; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-PAP-013 {decided_by=PAP-013; family=SF-PAP-013; rule=automated adjudication stratum}
- source_record: PAP-013
- tested_by: EXP:PAP-013 {record=PAP-013; rule=family hypothesis tested by member record}
- text: The shaper presence effect on PPP differs in clutch possessions.
