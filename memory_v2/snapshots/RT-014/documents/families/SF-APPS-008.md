# FAM:SF-APPS-008 | Study family SF-APPS-008 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict failed_gate, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-008
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: APPS-008: '.469,0.585], v4 0.451. may-4 dir_acc: v4 0.205 vs a_shuffle placebo 0.511 (gap -0.306). version 1 (may 4) reported l2 lift +0.1'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-008 | Finding of SF-APPS-008: rejected
- confidence: 0.95
- derived_from: EXP:APPS-008 {family=SF-APPS-008; rule=family member}
- rules_out: HYP:SF-APPS-008 {family=SF-APPS-008; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: May-7 PT-level vs V0_NEUTRAL: V4 beat 0.422 [0.365,0.480], V2 0.399 [0.338,0.459], FP_SHUFFLE 0.479 [0.412,0.544]; vs V0: V2 0.526 [0.469,0.585], V4 0.451. May-4 dir_acc: V4 0.205 vs A_SHUFFLE placebo 0.511 (gap -0.306).
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPS-008 | Hypothesis of SF-APPS-008
- addresses: RQC:RQC-078 {family=SF-APPS-008; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-008 {decided_by=APPS-008; family=SF-APPS-008; rule=automated adjudication stratum}
- source_record: APPS-008
- tested_by: EXP:APPS-008 {record=APPS-008; rule=family hypothesis tested by member record}
- text: Each engine layer (PNR calibration, scheme fingerprint, tier correction, sequential conditioning) improves prediction of observed series PPP.
