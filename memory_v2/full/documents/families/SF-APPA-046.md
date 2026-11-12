# FAM:SF-APPA-046 | Study family SF-APPA-046 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: APPA-046
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPA-046; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-046 | Finding of SF-APPA-046: supported
- confidence: 1.0
- derived_from: EXP:APPA-046 {family=SF-APPA-046; rule=family member}
- statement: BEST == generic best 78.3%; suppression-specific 21.7%. Defense suppressed generic-best 4.7% (73); then specific 39.7%. When supp != generic, still picks generic 79.2%. (off,def) counter changes by what was suppressed 48.8% (190/389). PNR adapt 28.3% n=428; PULL_UP 28.5% n=291. True INSUFF (no valid counter) 0/11,087 full-graph triggers.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPA-046 | Hypothesis of SF-APPA-046
- addresses: RQC:RQC-088 {family=SF-APPA-046; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPA-046
- supported_by: FIND:SF-APPA-046 {decided_by=APPA-046; family=SF-APPA-046; rule=automated adjudication stratum}
- tested_by: EXP:APPA-046 {record=APPA-046; rule=family hypothesis tested by member record}
- text: BEST-tier counters are suppression-specific rather than the team's generic best available play.
