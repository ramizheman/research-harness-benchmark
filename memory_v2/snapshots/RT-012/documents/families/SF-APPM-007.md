# FAM:SF-APPM-007 | Study family SF-APPM-007 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism B_powered_null, no power information
- confidence: 0.75
- confidence_level: high
- deciding_record: APPM-007
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_evidence: APPM-007: 'add xppp and team make-skill features to 8-feat ols; holdout r2. best +xppp only r2_hol +0.1204 (lift +0.0054); shot-ski'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-007 | Finding of SF-APPM-007: uncertain
- confidence: 0.75
- derived_from: EXP:APPM-007 {family=SF-APPM-007; rule=family member}
- statement: Best +xPPP only R2_hol +0.1204 (lift +0.0054); shot-skills -0.0003.
- status: uncertain
- validation_status: same_pipeline_validation

# HYP:SF-APPM-007 | Hypothesis of SF-APPM-007
- addresses: RQC:RQC-055 {family=SF-APPM-007; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPM-007 {decided_by=APPM-007; family=SF-APPM-007; rule=automated adjudication stratum}
- source_record: APPM-007
- tested_by: EXP:APPM-007 {record=APPM-007; rule=family hypothesis tested by member record}
- text: Shot-zone expected PPP and team shot-making skill add signal beyond box-score features.
