# FAM:SF-APPM-054 | Study family SF-APPM-054 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-054
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPM-054; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPM-054 | Finding of SF-APPM-054: rejected
- confidence: 0.95
- derived_from: EXP:APPM-054 {family=SF-APPM-054; rule=family member}
- rules_out: HYP:SF-APPM-054 {family=SF-APPM-054; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: 10/12 pairs CONSISTENT and within 0.10 of non-pivot (no PIVOT_WINS). PNR->PULL_UP sustained 1.069 vs non_pivot 1.224 (n_matchups=9) PIVOT_LOSES. DRIVE->PULL_UP 1.101 vs 1.217 (n=5) PIVOT_LOSES. Largest positive pair in the table: DRIVE->SPOT_UP 1.150 vs 1.098 (n=26). Shelf-life ~34-41 possessions.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPM-054 | Hypothesis of SF-APPM-054
- addresses: RQC:RQC-036 {family=SF-APPM-054; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPM-054 {decided_by=APPM-054; family=SF-APPM-054; rule=automated adjudication stratum}
- source_record: APPM-054
- tested_by: EXP:APPM-054 {record=APPM-054; rule=family hypothesis tested by member record}
- text: Pivoting to a listed counter after suppression sustains higher PPP than not pivoting, consistently across playoff matchups.
