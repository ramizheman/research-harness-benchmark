# FAM:SF-PAP-077 | Study family SF-PAP-077 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-077
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- validation_evidence: PAP-077: 'report.md). motivated the preregistered measurement study. held-out 2024-25 auc 0.721 vs 0.726; wrong unit (possessions not sto'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-077 | Finding of SF-PAP-077: untestable
- confidence: 1.0
- derived_from: EXP:PAP-077 {family=SF-PAP-077; rule=family member}
- statement: AUC clock+stint 0.721; adding stint points 0.726; ~1% of actual changes have predicted p>0.5; PPP SD 1.147; median lineup-game offensive poss=4 (p90=15); ~526 poss to detect 10/100 at 2 SE
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-PAP-077 | Hypothesis of SF-PAP-077
- addresses: RQC:RQC-177 {family=SF-PAP-077; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-077 {decided_by=PAP-077; family=SF-PAP-077; rule=automated adjudication stratum}
- source_record: PAP-077
- tested_by: EXP:PAP-077 {record=PAP-077; rule=family hypothesis tested by member record}
- text: Adding points scored in the current stint improves held-out prediction of within-period lineup changes beyond clock and stint length.
