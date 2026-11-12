# FAM:SF-APPM-033 | Study family SF-APPM-033 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict abandoned, mechanism E_unclear, no power information
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPM-033
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: abandoned
- risk_code: DRIFT_NONSTATIONARITY
- validation_status: no_validation_recorded

# FIND:SF-APPM-033 | Finding of SF-APPM-033: uncertain
- confidence: 0.65
- derived_from: EXP:APPM-033 {family=SF-APPM-033; rule=family member}
- statement: Premiums CUT->PULL_UP +0.065, PUTBACK->TRANSITION +0.084, Brown DRIVE->Tatum PNR +0.326 later removed: 'doesn't hold up'.
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-APPM-033 | Hypothesis of SF-APPM-033
- addresses: RQC:RQC-018 {family=SF-APPM-033; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPM-033 {decided_by=APPM-033; family=SF-APPM-033; rule=automated adjudication stratum}
- source_record: APPM-033
- tested_by: EXP:APPM-033 {record=APPM-033; rule=family hypothesis tested by member record}
- text: Specific play-type sequences carry a PPP premium (e.g. CUT->PULL_UP +0.065, PUTBACK->TRANSITION +0.084).
