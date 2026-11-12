# FAM:SF-APPM-055 | Study family SF-APPM-055 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPM-055
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPM-055; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: MECHANICAL_FLOOR
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPM-055 | Finding of SF-APPM-055: uncertain
- confidence: 0.65
- derived_from: EXP:APPM-055 {family=SF-APPM-055; rule=family member}
- statement: L1 (first run): after DRIVE best=CUT 1.261 vs PNR 1.132 (spread +0.129, CUT n_mu=5 PIVOT_WINS); after PNR best=TRANSITION 1.271 (n=35); after PULL_UP best=CUT 1.370 (n=5). L2 MIA disagrees with L1 on DRIVE (L2 best=PNR not CUT, gap=+0.125), PNR (DRIVE not TRANSITION), POST_UP, PULL_UP, SPOT_UP. Playoff right-counter: after DRIVE best=SPOT_UP 1.150 vs non_pivot 1.098 (n=26); after PNR best=DRIVE 1.151 vs 1.161 (n=35); after SPOT_UP best=PULL_UP 1.302 (n=4). Later L1 (2425 file): after CUT best=PULL_UP 1.231 (n=23 PIVOT_WINS) not PNR.
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-APPM-055 | Hypothesis of SF-APPM-055
- addresses: RQC:RQC-033 {family=SF-APPM-055; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPM-055 {decided_by=APPM-055; family=SF-APPM-055; rule=automated adjudication stratum}
- source_record: APPM-055
- tested_by: EXP:APPM-055 {record=APPM-055; rule=family hypothesis tested by member record}
- text: The best counter after a suppressed play type is stable from population (L1) to team (L2) to matchup (L3); otherwise the playsheet should not use a league default.
