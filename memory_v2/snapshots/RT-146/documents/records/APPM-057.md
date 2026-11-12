# EXP:APPM-057 | Defense-pool diversity: ROBUST label vs duplicate regimes
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Reuse _build_playsheet_conditional pool; pairwise cosine on PT delta vectors; single-link clusters at 0.95/0.90/0.80/0.50. Two matchups: BOS vs OKC and OKC vs BOS.
- hypothesis: The N~8-12 defensive adaptations used to certify playsheet ROBUST are genuinely distinct regimes (cosine clusters at 0.90), not near-duplicate single-knob tweaks.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPM-057; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPM-057 {record=APPM-057; rule=audit/study_family_review.csv or singleton}
- n_runs: 2
- notes: STAR_DENIAL is nearly collinear with PNR-tighten in both directions; still counted as distinct at 0.90 because only that pair merges.
- prespecified: no
- produced: RES:APPM-057 {record=APPM-057; rule=record fields}
- project: Strategy app
- related_as_recorded: CASE_STUDIES.md scheme robustness
- source: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_audit_defense_pool.py
- source: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_audit_out.txt
- title: Defense-pool diversity: ROBUST label vs duplicate regimes
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-057; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPM-057; rule=keyword rule METHOD_RULES}

# RES:APPM-057 | Result of APPM-057
- failure_evidence: 11/12 and 10/11 distinct at the registered 0.90 threshold.
- failure_type: D_positive
- power_info: n=2 matchups
- primary_result: BOS vs OKC: 12 adaptations, 11 clusters at 0.90 (D3 STAR_DENIAL ~ D12 tighten PNR cosine 0.97). Baseline PPP 1.2916; opener POST_UP-4%->CUT+4% cumulative ++0.0625. OKC vs BOS: 11 adaptations, 10 clusters at 0.90 (D3~D11 cosine 0.96). Baseline 1.2025; cumulative ++0.0911. Verdict both: GENUINELY DISTINCT - ROBUST label is fully earned. At 0.50 threshold clusters collapse to 7 and 6.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
