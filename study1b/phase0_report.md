# Study 1b, Phase 0: read and report

No model calls were made. Study 1 runs, tasks, prompts, answer key and scoring were not modified.

## 1. Audit fix

Two defects in `bench/retrieval_audit.py`:

- `_list()` parsed risk codes with `ast.literal_eval`, so a family whose `risk_code` was a plain string (106 of 151 tagged families in the RT-179 v2 snapshot) got no risk codes and could never enter the lesson tier.
- `runner/experiment.py` audited protocol-3 runs against the memory_v2 snapshot, but agents searched memory_v3.

Changes:

- `bench/retrieval_audit_study1.py`: frozen copy of the original audit (SHA-256 `3B6AA451...4F60B3`), header comment only. `analysis_fixes/experiment_study1_frozen.py`: frozen copy of the runner before the change.
- `bench/retrieval_audit.py`: new `_codes()` for snapshot risk codes (list, list literal, or plain string). `snapshot_info()` now also reads v3 graphs: `auto_outcome_status` mapped to v2 strata through the existing `V3_STATUS` table, risk codes from `auto_has_risk` edges, question membership from `auto_addresses_question` edges. `_list()` is unchanged; the answer-key fields it parses are already lists for all ten tasks.
- `runner/experiment.py` line 210: protocol-3 runs are audited against `ensure_snapshot_v3`; protocol 2 still uses v2.

v2 and v3 agree on content for all ten tasks: identical family sets, identical risk codes, and the only stratum differences are labels (uncertain/inconclusive 378, not_a_test/"not a hypothesis test" 404, no_result/"no result recorded" 16).

Verification (`analysis_fixes/verify_audit_fix.py`, output in `verify_audit_fix.txt`), 450 Study 1 primary runs:

| Check | Result |
|---|---|
| Frozen audit on v2 reproduces every audit column of the saved per_run.csv | 0 mismatched cells |
| Fixed audit on v3 equals fixed audit on v2 | 0 mismatched cells |
| Columns changed by the fix | only lesson-tier and derived columns; no other column changed |
| Rows where mentioned, returned or used changed | 29, all False to True, on RT-012, RT-066, RT-179, RT-183 |

## 2. Recompute and match

`analysis_fixes/recompute_and_match_study1.py` rescores all 450 raw runs with `scoring.score_replay` (0 differences from saved scores), re-audits them with the fixed audit on v3, and regenerates the primary table, sensitivity table, invalid-output counts, 300-pair tally and Appendix C counts. Result: 132 of 132 published numbers match (output in `recompute_and_match_study1.txt`). Two p-values sit exactly on a rounding half (0.875 printed .88, Holm 0.625 printed .62); both are correct at the published precision.

## 3. Harness inventory for O and OS

Exists and reusable: two-stage protocol 3 (`runner/agent.py`), memory_v3 snapshots for the ten tasks, `family_view` field selection and character budget, scoring, stats, the audit (now fixed), per-run cost recording, a cap check before every run (`run_all`, `max_cost_usd`), preflight.

Missing:

1. Conditions O and OS in `runner/tools_v3.py` (`CONDITION_TOOLS` has only A, B, C). O needs `retrieve_history` to return the frozen gold families for the task whatever the query; OS the same plus each family's scope annotation.
2. A frozen gold-family file and an annotation file, and a way for `Toolbox3` to know the task (it currently receives only the snapshot path).
3. A Study 1b config. The 80 percent stop can be `max_cost_usd: 8.0`, but the cap is per output directory, so all models should be in one config (or caps split across configs). The check runs before each run, so the last run can overshoot by at most one run's cost (Sonnet max in Study 1: $0.18).
4. Preflight branch: `scripts/21_preflight.py` requires the conditions to match earlier experiments and will fail for O/OS.
5. Analysis script for O and OS.
6. pytest is not installed in any interpreter on this machine (`python`, `py -3`, `supp_audit_venv`), so the 129 existing tests could not be run after the change.

## 4. Cost estimate (from Study 1 raw costs, memory conditions B and C)

| Model | Runs | Mean per run (B/C) | Estimate |
|---|---|---|---|
| Gemini 2.5 Flash | 60 | $0.018 | $1.06 |
| Claude Haiku 5.5 | 60 | $0.004 | $0.24 |
| gpt-oss-20b | 60 | $0.0005 | $0.03 |
| DeepSeek V4 Pro | 60 | $0.018 | $1.08 |
| Claude Sonnet 5.5 (O only) | 30 | $0.075 | $2.24 |
| Total | 270 | | about $4.65 |

With a 20 percent allowance for longer oracle and annotation context, about $5.60, under the $8 internal stop. Using the Study 1 maximum per-run cost for every run gives about $10, so the stop matters only in a worst case. Smoke test (Haiku, RT-012 and RT-147, O and OS, 1 seed, 4 runs): about $0.02.
