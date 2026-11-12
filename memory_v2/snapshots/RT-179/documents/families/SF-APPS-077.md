# FAM:SF-APPS-077 | Study family SF-APPS-077 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-077
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- validation_evidence: APPS-077: 'x 64 cells=1920; 883 estimated (n_t>=30). bh-within-star + placebo + ft-clean. pre-reg drive->pnr: all null/weak (sga att=-0.2'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-077 | Finding of SF-APPS-077: untestable
- confidence: 0.95
- derived_from: EXP:APPS-077 {family=SF-APPS-077; rule=family member}
- statement: Pre-reg DRIVE->PNR: all NULL/WEAK (SGA ATT=-0.222 BH_p=0.433). FINDING cells: 2 (Curry CUT->DRIVE +0.460 n=66 LOW_CONFIDENCE; Leonard SPOT_UP->POST_UP -0.360 n=137). Zero transition types FIND in 3+ stars. WEAK: 36.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-APPS-077 | Hypothesis of SF-APPS-077
- addresses: RQC:RQC-044 {family=SF-APPS-077; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-077 {decided_by=APPS-077; family=SF-APPS-077; rule=automated adjudication stratum}
- source_record: APPS-077
- tested_by: EXP:APPS-077 {record=APPS-077; rule=family hypothesis tested by member record}
- text: Teammate DRIVE -> star PNR (inferrer-only) is a recurring setup; other star transitions are structural if they FIND in 3+ stars.
