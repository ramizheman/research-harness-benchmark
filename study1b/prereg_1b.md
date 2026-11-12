# Study 1b preregistration: oracle retrieval and scope annotations

Status: draft for approval. **Nothing runs until Rami approves this document in writing.** No model or API call has been made for Study 1b.

Frozen inputs (git): `study1b/gold_rule.md` (committed before the gold list), `study1b/gold_families_frozen.json`, `study1b/scope_annotations_frozen.json`, `study1b/decisions.md`. Config: `configs/study1b.json`. Study 1 (paper 1) is fixed and is used only as a comparator.

## Open issue that must be resolved before approval

The first `retrieve_history` result in OS exceeds the 6,000-character tool-result limit (`budgets.max_tool_result_chars`, the Study 1 value) in 5 of the 7 tasks that have gold families: RT-012 by 274 characters, RT-014 by 258, RT-066 by 14, RT-112 by 1, RT-179 by 5 (`study1b/retrieval_sizes.txt`). The harness cuts the result at 6,000 characters, so the end of the last family's annotation is lost and the JSON is left unterminated. In the mock dry run this affected 60 of the 120 OS runs. O never exceeds the limit (largest 4,545). No Study 1 B or C first retrieval reached 6,000 (largest 5,952). `read_family` for SF04 (RT-066) exceeds the limit in OS only (by 12); SF20 (RT-066) exceeds it in O and OS, as it would have in Study 1's condition B. The annotations and the limit have not been changed. A decision is needed (see the report that accompanies this draft).

## Questions

- **Q1 (oracle).** When retrieval returns the families an audit-based rule marks as relevant, do decisions improve over no memory (A) and over Study 1's own retrieval (B document search, C graph traversal)?
- **Q2 (scope annotations, exploratory).** Does adding a scope annotation to each oracle family (OS) change decisions relative to O?

## Conditions

- **O.** `retrieve_history` returns the task's frozen gold families (at most 4, frozen order) whatever the request, rendered exactly as condition B rendered a family in Study 1. `read_family` is available for gold families only and returns the same document as B. No free search. Glossary and data catalog as in Study 1. RT-065, RT-101 and RT-146 have no gold families; there retrieval returns an empty list, as in A.
- **OS.** O plus each gold family's frozen scope annotation, as a separate `scope_annotation` field in both `retrieve_history` and `read_family` results. Identical text for a family in every task.
- **Comparators (not rerun).** Study 1 conditions A, B, C for the same model, tasks and seeds: `pilot3_v1` (Gemini), `cross_model_v1` (Haiku, gpt-oss-20b), `reasoning_models_v1` (Sonnet, DeepSeek).

Everything else is Study 1's: protocol 3 (stage 1 retrieval only, a preliminary assessment is rejected; stage 2 schema and answer), system prompt and stage texts, tasks, answer key, flag rule, scoring, budgets (12 tool calls, 2 repairs, 250,000 tokens, 900 s, 6,000 characters per tool result), memory_v3 snapshots, temperatures (0.7; 1.0 with extended thinking for Sonnet and DeepSeek) and provider routing. The only prompt difference from A is the tool list, which adds `read_family`.

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
- **Scope annotation changes decisions:** either (a) the OS − O balanced-accuracy 95% CI excludes 0, or (b) on at least 2 of the 7 tasks with gold families, the share of seeds flagged differs between OS and O by at least 2/3 (two of three seeds). The flag-rate differences on the three tasks without gold families, where OS and O are identical, are reported as the noise reference for (b).
- **Scope annotation does not change decisions:** neither (a) nor (b) holds.
- Whether changes move toward the answer key is reported separately (OS − O balanced accuracy and per-task correct rates).

## Disclosures

- The annotator (Opus) knew the answer key and Study 1 results. Every annotation sentence is record-faithful and passed a mechanical leakage check (numbers traced to the family record; no 5-gram overlap with the answer key or held-out task-family records; no decision vocabulary), but which sentences were selected may still be steered, and the mechanical check cannot detect that.
- The "Applies to" sentences that remain are the annotator's inference from the record, not record content. They were removed from SF-APPS-085 and SF07, the two judged to bear directly on their tasks.
- OS is exploratory. Its results are descriptive, not confirmatory.
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

The 1.4x markup is a guess; the smoke test (Phase 3) replaces it with measured per-run costs before the full run. If the re-estimated total exceeds the $8 stop, the plan is reduced in this order: drop Sonnet (high case without Sonnet: $6.67), then DeepSeek, then seeds (3 to 2). Smoke test: Haiku, RT-012 and RT-147, O and OS, seed 1, 4 runs, expected about $0.02 (high $0.04). RT-012 is one of the tasks whose OS retrieval exceeds the character limit, so the smoke test would show the open issue in a live run unless it is resolved first.

## Caps and stop conditions

- Study budget $10. The harness stops before any new run once recorded spend reaches 80% of it ($8.00; `budget_usd` 10, `stop_fraction` 0.8, `max_cost_usd` 8). Spend is the sum of `cost_usd` over finished runs: OpenRouter reports the cost of each call; for Gemini it is computed from token counts and the configured list price. The check runs before each run, so total spend can exceed $8 by at most one run (largest Study 1 run: $0.18).
- The harness also stops if any finished run has unknown cost, after 3 consecutive API errors, or if Gemini reports a model version other than gemini-2.5-flash.
- Rami sets the provider console cap. It covers OpenRouter (Haiku, gpt-oss-20b, DeepSeek, Sonnet) only; Gemini is billed by Google and is covered only by the harness stop.
- If a stop triggers, finished runs are kept and reported as an incomplete design; incomplete model-condition cells are not used for the Q1 or Q2 definitions above.

## Approval

Nothing runs, including the smoke test, until Rami approves this document in writing.
