# Study 2 preregistration: oracle retrieval on 68 new tasks

Status: **draft for approval. Nothing runs until I approve in writing.**

Everything below is a plan or a hypothesis. No result is described here, and none will be called a finding unless it
meets the decision rules in section 6.

## 1. Question

Study 1b, on ten tasks, found higher accuracy with oracle retrieval for four of five models, but no difference was
detectable. Study 2 asks the same question on tasks not used before.

**Q1.** On 68 new tasks, does giving the agent the relevant prior families (condition O) improve the decision about
whether a proposed study should proceed, compared with no memory (A) and with search-based document retrieval (B)?

- H1: accuracy is higher under O than under A.
- H2: accuracy is higher under O than under B.

## 2. Design

| Item | Plan |
|---|---|
| Tasks | 68: the main replay set (built and keyed before Study 1) minus the ten Study 1 tasks. Frozen copies are in `study2/tasks/`; the manifest is `study2/task_manifest.json`. |
| Strata | 14 untestable, 14 supported, 14 rejected, 14 artifact, 12 uncertain. 28 should be flagged, 40 should proceed. |
| Conditions | A (no memory), B (document retrieval, as Study 1), O (the frozen gold families through the same retrieval tool, as Study 1b). Protocol 3, prompts, tools and budgets as in Study 1 and 1b. |
| Gold families | The Study 1b rule (`study1b/gold_rule.md`) applied by `study2/gold.py`, by code only. 50 tasks have gold families; 18 have none, and on those O gives the agent the same empty list as A. |
| Models | Gemini 2.5 Flash, DeepSeek V4 Pro, Claude Haiku 5.5, gpt-oss-20b. Settings are copied unchanged from `configs/study1b.json`. Sonnet 5.5 is not run. |
| Seeds | Seed 1 only. |
| Runs | 68 Ã— 3 Ã— 4 = 816 (`configs/study2.json`). |
| Order | Gemini, DeepSeek, Haiku, gpt-oss, with tasks and conditions shuffled within each model (order seed 20261113). |
| Condition S | Not run. It would need new scope annotations for 186 gold slots, written by someone who knows the answer key (the Study 1b weakness), so it needs its own preregistration. |

## 3. Outcome and scoring (unchanged from Study 1)

- **Flag rule.** `bench.scoring.score_replay`. A run counts as a flag if any of these holds:
  - its decision is "do not proceed";
  - its stated testability probability is below 0.5;
  - its predicted probability of an untestable or artifact outcome exceeds 0.5.
- **Correct.** A run is correct when its flag matches `should_flag_before_running`.
- **Per-task rate.** Each task's correct rate is its single seed-1 run.
- **Balanced accuracy.** The mean of the flag-task rate and the no-flag-task rate.
- **Scoring rules.**
  - primary: no scorable flag counts as wrong;
  - strict: an invalid output counts as wrong;
  - valid_only: invalid or unscorable runs are dropped.

## 4. Contrasts and tests

All analysis is by `study2/analysis.py study2`. This is the script that reproduces all 161 published Study 1 and 1b
numbers.

- **Task as the unit.** Per-task differences are weighted by 1/(2p) for flag tasks and 1/(2(1 âˆ’ p)) for no-flag tasks, with p = 28/68. Their mean equals the balanced-accuracy difference.
- **Primary.** Pooled O âˆ’ A and pooled O âˆ’ B. Each task's difference is the mean over the four models.
  - 95% percentile bootstrap CI over tasks (10,000 resamples, seed 0).
  - Two-sided sign-flip p (20,000 sign draws, seed 0).
  - Holm across the two primary contrasts.
- **Secondary.** O âˆ’ A and O âˆ’ B for each model, with Holm across the four models within each contrast. A model whose runs are incomplete is analyzed on the tasks where it has all three conditions, and this is reported.

## 5. Power

Minimum detectable effects at 80% power were computed by `study2/analysis.py power` (`study2/power.json`). They use the
spread of seed-1 per-task differences in the Study 1 and 1b runs (ten tasks, four models), rescaled to 68 tasks:

| Contrast | MDE, pooled (Î± = 0.025, Holm first step) | MDE, per model (Î± = 0.0125, Holm first step) |
|---|---|---|
| O âˆ’ A | 0.14 | 0.20 (Haiku) to 0.26 (Gemini) |

- The O âˆ’ B spread could not be estimated from ten tasks (Haiku's seed-1 O and B runs agreed on all ten), so the O âˆ’ A values are the planning values for O âˆ’ B too.
- Study 1b's O âˆ’ A estimates were 0.01 to 0.26. Study 2 can therefore detect a pooled effect of about the Study 1b average size, but per model only effects as large as the largest Study 1b estimate.
- If O helps only where there are gold families, the effect over all 68 tasks is about 50/68 of the effect on those 50.

## 6. Decision rules (fixed now)

**For H1, pooled O âˆ’ A:**
- **Supported:** the difference is above 0, the 95% CI lower bound is above 0, and the Holm-adjusted p is below 0.05.
- **No meaningful benefit:** the 90% bootstrap CI lies inside (âˆ’0.10, +0.10) (`bench.stats.tost`, margin 0.10). This outcome would count against the Study 1b direction.
- **Otherwise:** inconclusive.

**For H2, pooled O âˆ’ B:** the same three rules.

**Per model:**
- "Oracle helps": O âˆ’ A above 0, CI lower bound above 0, and Holm-adjusted p below 0.05.
- "Oracle harms": CI upper bound below 0.
- Otherwise: no detectable difference.

**Reading the combinations (stated in advance):**

| H1 (O vs A) | H2 (O vs B) | What it would suggest |
|---|---|---|
| Supported | Supported | Retrieval quality limits what memory adds. |
| Supported | Not supported | Search already captures most of what the gold families add. |
| No meaningful benefit | Any | Giving the agent the right families does not detectably improve this decision, which points to applicability or representation rather than retrieval. |
| Inconclusive | Any | The study cannot separate these. |

## 7. Secondary analyses (descriptive; no claims beyond section 6)

1. **Sensitivity.** The primary contrasts under the strict and valid_only rules, and on these subsets:
   - without the 12 uncertain tasks (contestable keys);
   - the 50 tasks with gold families;
   - the 18 tasks without gold families, as a noise reference, since O is A there.
2. **Run-level tally.** Same model, task and seed: O versus A, B versus A, and O versus B, counted as fixed, broke, same correct or same wrong.
3. **Retrieval audit for B and O.** Fixed definitions in `bench/retrieval_audit.py`. For each model, the share of runs where a relevant family was surfaced, returned, "meaningfully used" (Study 1 definition), and decision-linked (the stronger definition in `study2/phase0_report.md`, section 4).
4. **Hand check.** 30 runs coded as used under either definition are sampled (seed 20261112) into `study2/analysis/used_hand_check.csv`. Rami codes them by hand, and agreement with each automated definition is reported.
5. **Validity and cost.** Invalid outputs, unscorable flags, stop reasons and cost per model.
6. **Recompute-and-match.** The rescored flags compared with the runner's `scores.csv`.

## 8. Budget and stopping

**Budget.** $10, covering every call. The runner stops at 80% ($8.00: `budget_usd` 10, `stop_fraction` 0.8,
`max_cost_usd` 8.0). It also stops if any finished run has unknown cost, or after 3 consecutive API errors.

**Cost arithmetic** (`study2/cost_estimate.txt`). Measured mean cost per run (Study 1 A and B, Study 1b O) Ã— 68 tasks:

| Model | A | B | O | Total |
|---|---|---|---|---|
| Gemini | 0.85 | 1.16 | 1.04 | 3.05 |
| DeepSeek | 0.76 | 1.17 | 0.98 | 2.91 |
| Haiku | 0.17 | 0.27 | 0.23 | 0.67 |
| gpt-oss | 0.03 | 0.03 | 0.04 | 0.10 |
| **Total** | | | | **$6.72** |

- The expected total is $6.72, which is 67% of the budget and under the 70% target. That is $0.033 per task-condition across the four models.
- No cuts are planned.
- The high scenario, where every run costs as much as the most expensive measured task, is $8.43, which would reach the stop. Because models run in order, a stop would cut gpt-oss first, then Haiku, keeping Gemini and DeepSeek.
- If the stop binds, the analysis uses the completed runs and reports what was cut.

**Time.** About 13 hours if run in one process (mean measured wall time; DeepSeek about 9 of those hours).

**Procedure.**
1. Gate check.
2. Preflight (no model calls).
3. Smoke test after "go smoke": `configs/study2_smoke.json`, Haiku only, RT-005 and RT-036, A, B and O, 6 runs, $0.50 cap. The smoke runs are not analyzed.
4. Stop, report, and wait for "go full".
5. Full run, with no changes during it. Any amendment is recorded here, with its reason, before it takes effect.

## 9. Disclosures

- **Sonnet 5.5 excluded.** This is for cost. It had the highest Study 1 accuracy without memory.
- **Single seed.** Each task-condition cell is one run, so per-task results are noisy. The no-gold tasks show how large differences between identical conditions can be.
- **Builder/subject overlap.**
  - The harness, task generator, adjudication rules and gold rule were written by the Cursor coding agent, Claude Opus (Anthropic).
  - That agent's answer-key "consistency screen" excluded one family, which is in no task.
  - The Study 2 build was done by Claude Opus as well.
  - None of the four subject models took part. Claude Haiku 5.5, a subject model, is from the same developer as the builder.
- **The answer key is automated** (rule-based adjudication of extracted records), not independent human adjudication. All 12 uncertain tasks are keyed "proceed" by convention.
- **Relevance coding is automated.**
  - Question relevance uses question clusters and a TF-IDF threshold; lesson relevance uses automated risk-code tags.
  - Some relevant prior work may be missed, and some listed families may be weakly relevant.
  - The Study 1 "used" measure is weak (met in 94% of successful retrievals). The decision-linked measure is stricter but still a text rule.
- **Gold coverage is uneven.** 18 tasks have no gold families, 8 of them uncertain tasks, and 138 of the 186 gold slots are lesson-tier.
- **Stricter leakage rule.** It removed 4 records from 3 tasks' memory (RT-024, RT-063, RT-070) relative to the original frozen tasks.
- **Task selection.** The tasks are not a random sample. The main set was chosen by a priority rule (confidence, self-contained statement, reliable date) with stratum quotas, and the Study 1 pilot was drawn from it first.
- **Prior knowledge.** The design and the gold rule were fixed after Study 1 and 1b results were known, but before any Study 2 run. The predictions below are written with that knowledge.

## 10. Rami's prediction

Overall prediction: [TO BE WRITTEN BY RAMI BEFORE APPROVAL]

Basis: [TO BE WRITTEN BY RAMI BEFORE APPROVAL]

| Model | O vs A (help / hurt / no clear difference) | O vs B (help / hurt / no clear difference) |
|---|---|---|
| Pooled | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] |
| Gemini | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] |
| DeepSeek | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] |
| Haiku | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] |
| gpt-oss | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] | [TO BE WRITTEN BY RAMI BEFORE APPROVAL] |

Predictions written on [TO BE WRITTEN BY RAMI BEFORE APPROVAL], after the Study 1 and 1b results and before any Study 2 run.

## 11. Frozen inputs (sha256)

| File | sha256 |
|---|---|
| `study2/task_manifest.json` | `eaf1d22fe28bf9aa517c31ed297b3c13346e948e90fdb13565e171f044193bea` |
| `study2/gold_families_frozen.json` | `e11f83fb424dbc0100079cf45ef3ff4ca629bfb1a493b47c465a5b104ddfdbbd` |
| `study2/scope_annotations_none.json` | `f1cb43d5fbcf1526efaeaf76d0669583323e8042ed4e500d4847739f6052034f` |
| `benchmark_answer_key.jsonl` | `cdb876cb2d22b0e72ad1fc8c93e406a5b0ef32138d8ebc1462f465fb409819d0` |
| `configs/study2.json` | `0c1a316c2a06f8726ec0a577e4e18160877353ec6d0768c936b459d53512b093` |
| `configs/study2_smoke.json` | `19d347cb6a26cc82d2d28fd4f86e82a467e43961eb51fe62570e2a7b335a6233` |
| `study1b/gold_rule.md` | `6351c76a3e307a4c4987b56aa40b6e71fe233dbf17e3ca58c8b2e29c9aec62a1` |
| `bench/scoring.py` | `437fa27bdb5aac037042a1b61f9a6ad9e2f0bea87e4ee1007ca95ba6f0537441` |
| `bench/retrieval_audit.py` | `1968dab7072937610a9a0593552a6d8b1031543d4b1a5c705297f47c4fde7d79` |
| `bench/stats.py` | `8a86e3eb5ad7095501920119d0917f0c9437b326c286d9d309649397919612b8` |
| `runner/agent.py` | `aa99acd71524799fc767b8d2a379ca08a58447f2a011ec2e96d2da990aa113c4` |
| `runner/tools_v3.py` | `6893c42471f877ab5c0b136c76b026996c8ebf7a4e07abded2ca25c8bdd210c9` |
| `runner/experiment.py` | `f838e892e4c1c1ad09ad5cdca62bea8c440ecc97e67121af0e4eec8d01334303` |
| `study2/analysis.py` | `21b5310fad3a954438ea3c1bf9c36886bc839090d5921cb3bdaabafa95552501` |

Config hash (as recorded in each run): `23f469a23965823ca42de19cb8deb4cb4f6eba260e7af9b9f31c34eb693201fb`.
Code hash (`bench` and `runner`): `9af7b0b91b33b2e5b04a53ce405f174671db82b9beecf4e8cbd60e04d66a292f`.

## 12. Approval

Nothing runs until I approve in writing.

Approved by: ____________________  Date: ____________
