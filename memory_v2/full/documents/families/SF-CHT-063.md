# FAM:SF-CHT-063 | Study family SF-CHT-063 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-063
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: BASE_RATE
- validation_status: no_validation_recorded

# FIND:SF-CHT-063 | Finding of SF-CHT-063: artifact
- confidence: 1.0
- derived_from: EXP:CHT-063 {family=SF-CHT-063; rule=family member}
- rules_out: HYP:SF-CHT-063 {family=SF-CHT-063; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: After event BEST 1.403 vs continue 1.154, gap +0.248 (SE 0.009). No-slump events +0.239 vs +0.248. League-wide ranking no game info +0.238. BEST is CUT 61% of the time. Residuals ~0 for continue, BEST +0.002, others -0.003.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-063 | Hypothesis of SF-CHT-063
- addresses: RQC:RQC-152 {family=SF-CHT-063; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-063 {decided_by=CHT-063; family=SF-CHT-063; rule=automated adjudication stratum}
- source_record: CHT-063
- tested_by: EXP:CHT-063 {record=CHT-063; rule=family hypothesis tested by member record}
- text: The BEST-vs-continue gap after a slump is evidence of costly failure to abandon a suppressed play (depends on the slump event).
