# FAM:SF-APPS-085 | Study family SF-APPS-085 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict failed_gate
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-085
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: data-level limitation: low measurement reliability
- knowable_before_outcome_auto: yes_from_data
- limited_by: LIM:low_measurement_reliability {family=SF-APPS-085; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPS-086 {family=SF-APPS-085; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.376}
- risk_code: MEASURE_RELIABILITY
- validation_evidence: APPS-085: 'fect (true r<=0.25 could still be missed). n=102 connectors split-half r=0.215 / sb 0.355 is too low to treat q_p as a stable scou'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-085 | Finding of SF-APPS-085: untestable
- confidence: 0.95
- derived_from: EXP:APPS-085 {family=SF-APPS-085; rule=family member}
- statement: Pearson r(Q_a,Q_b)=+0.215 p=0.0297; Spearman rho=+0.242. Spearman-Brown Q~0.355, S~0.278. Sign agreement 65.7% (67/102) binomial p=0.000996. ICC(player-season)=0.216 (78.4% within). Attenuation: even a perfect predictor max |r| with Q_p ~0.595; true r=0.30 attenuates to 0.179 (often undetectable).
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-APPS-085 | Hypothesis of SF-APPS-085
- addresses: RQC:RQC-052 {family=SF-APPS-085; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-085 {decided_by=APPS-085; family=SF-APPS-085; rule=automated adjudication stratum}
- source_record: APPS-085
- tested_by: EXP:APPS-085 {record=APPS-085; rule=family hypothesis tested by member record}
- text: Connector quality Q_p (teammate-initiated on-off PPP gap) is a stable player-season attribute.
