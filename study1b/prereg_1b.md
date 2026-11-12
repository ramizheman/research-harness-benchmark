# Study 1b preregistration: oracle retrieval and scope annotations

Status: draft for approval. **Nothing runs until Rami approves this document in writing.** No model or API call has been made for Study 1b.

Frozen inputs (git): `study1b/gold_rule.md` (committed before the gold list), `study1b/gold_families_frozen.json`, `study1b/scope_annotations_frozen.json`, `study1b/decisions.md`. Config: `configs/study1b.json`. Study 1 (paper 1) is fixed and is used only as a comparator.

## Tool-result length limit (decided: fix 1)

With the annotations counted, the first OS `retrieve_history` result would have exceeded the 6,000-character tool-result limit (`budgets.max_tool_result_chars`, the Study 1 value) in 5 of the 7 tasks with gold families, and the cut would have dropped the end of the last annotation. Rami chose fix 1: in OS, the characters of the `scope_annotation` fields do not count against the limit. The rest of an OS result is counted and cut exactly as the same result in O. Consequences, all checked without model calls (`tests/test_study1b.py`, `study1b/retrieval_sizes.txt`, `study1b/dry_run_report.txt`):

- No first retrieval is cut in O or OS (O largest 4,545 characters; OS total largest 6,274).
- Removing the annotation fields from any OS result gives the O result byte for byte, for the first retrieval and every `read_family`.
- O outputs are byte-identical to those recorded before the fix, and Study 1 A, B and C tool outputs and prompts are byte-identical to those recorded before any Study 1b change.
- The only cut result is `read_family` for SF20 (RT-066), which is cut at the same place in O and OS, as it would have been in Study 1's condition B.
- The annotation limit and the annotations themselves were not changed.

## Questions

- **Q1 (oracle).** When retrieval returns the families an audit-based rule marks as relevant, do decisions improve over no memory (A) and over Study 1's own retrieval (B document search, C graph traversal)?
- **Q2 (scope annotations, exploratory).** Does adding a scope annotation to each oracle family (OS) change decisions relative to O?

## Conditions

- **O.** `retrieve_history` returns the task's frozen gold families (at most 4, frozen order) whatever the request, rendered exactly as condition B rendered a family in Study 1. `read_family` is available for gold families only and returns the same document as B. No free search. Glossary and data catalog as in Study 1. RT-065, RT-101 and RT-146 have no gold families; there retrieval returns an empty list, as in A. O uses B's document format only; an oracle in C's graph format is not tested, so O − C mixes the effect of which families are retrieved with the effect of format.
- **OS.** O plus each gold family's frozen scope annotation, as a separate `scope_annotation` field placed before the document in both `retrieve_history` and `read_family` results. Identical text for a family in every task. Annotation characters do not count against the tool-result limit (fix 1 above).
- **Comparators (not rerun).** Study 1 conditions A, B, C for the same model, tasks and seeds: `pilot3_v1` (Gemini), `cross_model_v1` (Haiku, gpt-oss-20b), `reasoning_models_v1` (Sonnet, DeepSeek).

Everything else is Study 1's: protocol 3 (stage 1 retrieval only, a preliminary assessment is rejected; stage 2 schema and answer), system prompt and stage texts, tasks, answer key, flag rule, scoring, budgets (12 tool calls, 2 repairs, 250,000 tokens, 900 s, 6,000 characters per tool result, with the OS annotation exception above), memory_v3 snapshots, temperatures (0.7; 1.0 with extended thinking for Sonnet and DeepSeek) and provider routing. The only prompt difference from A is the tool list, which adds `read_family`.

## Models, seeds, runs

| Model | Conditions | Seeds | Runs |
|---|---|---|---|
| Gemini 2.5 Flash | O, OS | 1, 2, 3 | 60 |
| Claude Haiku 5.5 | O, OS | 1, 2, 3 | 60 |
| gpt-oss-20b | O, OS | 1, 2, 3 | 60 |
| DeepSeek V4 Pro | O, OS | 1, 2, 3 | 60 |
| Claude Sonnet 5.5 | O | 1, 2, 3 | 30 |
| Total | | | 270 |

Runs execute model by model in the order above, seeds ascending within a model, shuffled within each model and seed (`run_order: model_then_seed`, `order_seed` 20261112). A budget stop therefore cuts Sonnet first, then DeepSeek, then the highest seeds.

## Metric and scoring

Balanced flag accuracy over the ten tasks, computed at the task level: seeds averaged within each task, then the mean over flag tasks and the mean over no-flag tasks averaged. Same flag rule as Study 1 (`bench/scoring.py flagged()`: decision do_not_proceed, or p_testable < 0.5, or P(untestable) + P(artifact) > 0.5). Same three scoring rules as paper 1: primary (scored where possible; an output with no scorable flag counts as wrong), strict (invalid output counts as wrong), valid-only (invalid outputs dropped). Primary is the headline; strict and valid-only are sensitivity checks.

## Statistics

- Per-task correct rates for every model and condition.
- Balanced-accuracy differences per model: O − A, O − B, O − C (Q1) and OS − O (Q2), each with a percentile bootstrap 95% CI over tasks (`bench.stats.bootstrap_ci`, 10,000 resamples, seed 0, Study 1 task weights) and an exact sign-flip p-value (`bench.stats.sign_flip_p`). Holm correction across models within each contrast family, as in paper 1.
- Ten tasks cannot detect effects below about 0.3 in balanced accuracy. All results are descriptive. Absence of a detected difference is not evidence of no effect.
- Q1 compares runs made on different dates (Study 1 on 2026-11-10 and 11; Study 1b later), so model or provider drift is possible. The three tasks without gold families make O equivalent to A apart from the listed `read_family` tool, and serve as a drift check: their O correct rates are reported next to Study 1's A rates.

## Operational definitions

All on the primary scoring rule, per model.

- **Oracle helps:** the O − A balanced-accuracy difference is positive and its 95% CI lower bound is above 0.
- **Oracle does not help:** the O − A 95% CI includes 0 or lies below 0. If the upper bound is below 0, the oracle is also reported as having **harmed** accuracy. Given the power limit above, "does not help" means no effect was detected, not that none exists.
- O − B and O − C use the same definitions and are secondary.
- **Scope annotation changes decisions** (a descriptive label, not a confirmatory test; it does not separate the annotation from the extra length, see Disclosures): either (a) the OS − O balanced-accuracy 95% CI excludes 0, or (b) on at least 2 of the 7 tasks with gold families, the share of seeds flagged differs between OS and O by at least 2/3 (two of three seeds). The flag-rate differences on the three tasks without gold families, where OS and O are identical, are reported as the noise reference for (b).
- **Scope annotation does not change decisions:** neither (a) nor (b) holds.
- Whether changes move toward the answer key is reported separately (OS − O balanced accuracy and per-task correct rates).

## Disclosures

- The annotator (Opus) knew the answer key and Study 1 results. Every annotation sentence is record-faithful and passed a mechanical leakage check (numbers traced to the family record; no 5-gram overlap with the answer key or held-out task-family records; no decision vocabulary), but which sentences were selected may still be steered, and the mechanical check cannot detect that.
- The "Applies to" sentences that remain are the annotator's inference from the record, not record content. They were removed from SF-APPS-085 and SF07, the two judged to bear directly on their tasks.
- OS is exploratory. Its results are descriptive, not confirmatory.
- OS delivers more total text than O: the first retrieval is 729 to 1,784 characters longer on the 7 tasks with gold families, and each `read_family` is 210 to 505 characters longer (`study1b/retrieval_sizes.txt`). There is no length-matched control, so any OS − O difference is read as the effect of "annotation plus extra length", not of the annotation alone.
- SF-CHT-025 is a declared manual addition to the gold sets of RT-012 and RT-147 (the audit rule cannot select it). It was chosen partly because of its role in Study 1, so RT-012 and RT-147 are a targeted case test, not an unbiased sample.

## Predictions

### Notes recorded in decisions.md (copied verbatim)

Notes for the preregistration (Phase 2), recorded 2026-11-12:

- SF-CHT-025 cannot separate RT-012 from RT-147: its record and annotation fit both tasks equally. The expected outcome on that pair is a null for OS. Dated prediction to state: O helps RT-012; OS does not rescue RT-147.
- OS may therefore not test the scope-condition idea from paper 1: a record-faithful annotation cannot carry the effect-size information that separated RT-012 from RT-147. State this plainly.

### Rami's prediction

[TO BE WRITTEN BY RAMI BEFORE APPROVAL]

### Per-task predictions

| Task | Rami: O vs A | Rami: OS vs O |
|---|---|---|
| RT-012 | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] |
| RT-147 | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] |
| RT-179 | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] |

## Cost estimate

Per-run costs from Study 1's memory conditions. Low uses the mean Study 1 per-run cost; expected applies an assumed 1.4x markup for longer oracle and annotation context; high applies the same markup to the largest Study 1 per-run cost of each model (memory conditions).

| Model | Runs | Per run (Study 1 mean / max) | Low | Expected (1.4x) | High (1.4x max) |
|---|---|---|---|---|---|
| Gemini 2.5 Flash | 60 | $0.016 / $0.0332 | $0.96 | $1.34 | $2.79 |
| Claude Haiku 5.5 | 60 | $0.003 / $0.0079 | $0.18 | $0.25 | $0.66 |
| gpt-oss-20b | 60 | $0.0004 / $0.0020 | $0.02 | $0.03 | $0.17 |
| DeepSeek V4 Pro | 60 | $0.016 / $0.0363 | $0.96 | $1.34 | $3.05 |
| Claude Sonnet 5.5 | 30 | $0.070 / $0.1759 | $2.10 | $2.94 | $7.39 |
| Total | 270 | | $4.22 | $5.91 | $14.06 |

The 1.4x markup is a guess; the smoke test (Phase 3) replaces it with measured per-run costs before the full run. If the re-estimated total exceeds the $8 stop, the plan is reduced in this order: drop Sonnet (high case without Sonnet: $6.67), then DeepSeek, then seeds (3 to 2). Smoke test: Haiku, RT-012 and RT-147, O and OS, seed 1, 4 runs, expected about $0.02 (high $0.04). RT-012 has the longest OS first retrieval (6,274 characters in total), so the smoke test also shows fix 1 in a live run.

## Caps and stop conditions

- Study budget $10. The harness stops before any new run once recorded spend reaches 80% of it ($8.00; `budget_usd` 10, `stop_fraction` 0.8, `max_cost_usd` 8). Spend is the sum of `cost_usd` over finished runs: OpenRouter reports the cost of each call; for Gemini it is computed from token counts and the configured list price. The check runs before each run, so total spend can exceed $8 by at most one run (largest Study 1 run: $0.18).
- The harness also stops if any finished run has unknown cost, after 3 consecutive API errors, or if Gemini reports a model version other than gemini-2.5-flash.
- Rami sets the provider console cap. It covers OpenRouter (Haiku, gpt-oss-20b, DeepSeek, Sonnet) only; Gemini is billed by Google and is covered only by the harness stop, so before the smoke test Rami also sets a Google Cloud billing budget alert or cap for the Gemini key's project.
- If a stop triggers, finished runs are kept and reported as an incomplete design; incomplete model-condition cells are not used for the Q1 or Q2 definitions above.

## Approval

Nothing runs, including the smoke test, until Rami approves this document in writing.
