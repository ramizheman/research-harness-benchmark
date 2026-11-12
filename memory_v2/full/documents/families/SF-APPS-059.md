# FAM:SF-APPS-059 | Study family SF-APPS-059 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-059
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPS-059; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPS-059: 'ons; time-split test 2025-26 short-memory horizon is stable oos; almost all gain is lag-1, plateau by lag 4. absolute auc s'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-059 | Finding of SF-APPS-059: supported
- confidence: 0.95
- derived_from: EXP:APPS-059 {family=SF-APPS-059; rule=family member}
- statement: Per-lag GBT AUC N=0 0.5621 -> N=1 0.5863 (d+0.0242) -> N=3 0.5907 -> N=8 0.5911. R2 0.0051 -> 0.0133. Aggregated window declines after N=1 (AUC 0.5868 -> 0.5687 at N=8). Effective horizon ~2-3 possessions.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPS-059 | Hypothesis of SF-APPS-059
- addresses: RQC:RQC-047 {family=SF-APPS-059; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-059
- supported_by: FIND:SF-APPS-059 {decided_by=APPS-059; family=SF-APPS-059; rule=automated adjudication stratum}
- tested_by: EXP:APPS-059 {record=APPS-059; rule=family hypothesis tested by member record}
- text: Increasing prior-possession history changes the opponent's next-possession outcome after controlling for game state.
