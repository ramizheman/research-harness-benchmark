# FAM:SF-APPM-057 | Study family SF-APPM-057 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-057
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPM-057; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPM-057: '25; cumulative ++0.0911. verdict both: genuinely distinct - robust label is fully earned. at 0.50 threshold clusters collapse'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-057 | Finding of SF-APPM-057: supported
- confidence: 0.95
- derived_from: EXP:APPM-057 {family=SF-APPM-057; rule=family member}
- statement: BOS vs OKC: 12 adaptations, 11 clusters at 0.90 (D3 STAR_DENIAL ~ D12 tighten PNR cosine 0.97). Baseline PPP 1.2916; opener POST_UP-4%->CUT+4% cumulative ++0.0625. OKC vs BOS: 11 adaptations, 10 clusters at 0.90 (D3~D11 cosine 0.96). Baseline 1.2025; cumulative ++0.0911. Verdict both: GENUINELY DISTINCT - ROBUST label is fully earned. At 0.50 threshold clusters collapse to 7 and 6.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPM-057 | Hypothesis of SF-APPM-057
- addresses: RQC:RQC-075 {family=SF-APPM-057; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPM-057
- supported_by: FIND:SF-APPM-057 {decided_by=APPM-057; family=SF-APPM-057; rule=automated adjudication stratum}
- tested_by: EXP:APPM-057 {record=APPM-057; rule=family hypothesis tested by member record}
- text: The N~8-12 defensive adaptations used to certify playsheet ROBUST are genuinely distinct regimes (cosine clusters at 0.90), not near-duplicate single-knob tweaks.
