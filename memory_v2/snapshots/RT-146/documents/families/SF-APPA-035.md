# FAM:SF-APPA-035 | Study family SF-APPA-035 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-035
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPA-063 {family=SF-APPA-035; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.42}
- validation_evidence: APPA-035: 'one holdout game 0022400946; spearman of predicted vs actual pt ppp (pt'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-035 | Finding of SF-APPA-035: untestable
- confidence: 0.95
- derived_from: EXP:APPA-035 {family=SF-APPA-035; rule=family member}
- statement: BOS rho 0.200, top-3 n/a, bottom-3 1/3; OKC rho 0.543, top-3 2/2, lift +0.308, bottom-3 1/3.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-APPA-035 | Hypothesis of SF-APPA-035
- addresses: RQC:RQC-011 {family=SF-APPA-035; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-035 {decided_by=APPA-035; family=SF-APPA-035; rule=automated adjudication stratum}
- source_record: APPA-035
- tested_by: EXP:APPA-035 {record=APPA-035; rule=family hypothesis tested by member record}
- text: Model's top-ranked play types score above team average in a held-out game.
