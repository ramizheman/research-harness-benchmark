# FAM:SF-APPS-049 | Study family SF-APPS-049 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-049
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPM-011 {family=SF-APPS-049; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.431}
- validation_status: no_validation_recorded

# FIND:SF-APPS-049 | Finding of SF-APPS-049: rejected
- confidence: 0.95
- derived_from: EXP:APPS-049 {family=SF-APPS-049; rule=family member}
- rules_out: HYP:SF-APPS-049 {family=SF-APPS-049; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: durable_branches=[]. Median net swing: CUT +0.36 (neg in 9%), TRANSITION +0.26 (21%), PULL_UP +0.09 (33%), PNR +0.04 (45%), SPOT_UP +0.02 (40%), POST_UP -0.22 (77%), DRIVE -0.27 (88%). n_units: CUT 103, DRIVE/POST_UP/SPOT_UP/TRANSITION/PULL_UP 104, PUTBACK 47.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-049 | Hypothesis of SF-APPS-049
- addresses: RQC:RQC-008 {family=SF-APPS-049; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-049 {decided_by=APPS-049; family=SF-APPS-049; rule=automated adjudication stratum}
- source_record: APPS-049
- tested_by: EXP:APPS-049 {record=APPS-049; rule=family hypothesis tested by member record}
- text: If-X-fails-then-Y pivot branches and PT net-swing (own PPP - opp next PPP) are durable across ~104 playoff team-offense units.
