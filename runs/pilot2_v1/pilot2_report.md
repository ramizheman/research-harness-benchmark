# Pilot 2: required research-memory retrieval

Ten replay tasks, one model (Gemini 2.5 Flash, listed version 001, every response reporting `gemini-2.5-flash`), one
seed, conditions A (no historical memory), B (document memory) and C (graph memory). Answer key: automated rule-based
adjudication, not independent human adjudication. Pilot 1 files were read but not modified; the two pilots are
compared task by task and never pooled.

## Recommendation

**Do not scale to the 78-task benchmark in its current form.** Required retrieval worked as an execution fix and
raised how often relevant prior work reached the agent, but it did not change research decisions, and neither memory
condition improved the primary outcome over A. The binding constraint is not the protocol but what retrieval
delivers: none of the 160 items returned across the B and C runs was a study-family record, which is where the
project's adjudicated outcomes and failure mechanisms are stated, and no run used a follow-up memory tool. At 78 tasks
the primary contrast can detect a difference of roughly 0.16 in balanced accuracy (80% power, from the Pilot 2
task-level spread); the observed differences are near zero. Scaling would most likely produce a well-measured null about a retrieval step that does not show the agent the
information most likely to change a decision. Changes that would make a scaled run informative are listed at the end.

## What was run

| item | value |
|---|---|
| tasks | RT-012, RT-014 (artifact), RT-065, RT-066 (rejected), RT-101, RT-112 (supported), RT-146, RT-147 (uncertain), RT-179, RT-183 (untestable) |
| model and settings | `gemini-2.5-flash`, temperature 0.7, 8192 output tokens, thinking budget 2048, JSON mode, seed 1 (identical to Pilot 1; checked by preflight against the Pilot 1 manifest) |
| model version | listing version 001 and response `modelVersion` `gemini-2.5-flash`, the same as all 101 Pilot 1 responses; the runner stops on any other version |
| snapshots, answer key, scoring | unchanged; snapshot hashes, frozen task hashes and the exclusion check pass for all 10 tasks |
| configuration | `configs/pilot2.json` (experiment `pilot2_v1`, protocol 2); output `runs/pilot2_v1/` |
| runs | 30 of 30, all ending with a final answer, no API errors |
| cost | 0.4672 USD (244,357 input and 157,549 output tokens) plus 0.00007 USD for the preflight smoke request; Pilot 1 cost 0.5732 USD |

### Protocol 2 (identical in every condition apart from the tool list)

1. The agent states the research question.
2. It must call `retrieve_history(research_question, query)` before any other tool. The tool has one name and one
   description in every condition. In A it executes and returns an empty list. In B and C it returns the same eight
   top-ranked research records (identical TF-IDF ranking over the same snapshot), as document text in B and as graph
   nodes with their edges in C, each item capped at 700 characters. A has no other route to historical content.
3. The final answer adds `research_question`, `retrieval_summary` (prior findings, failed experiments, limitations,
   unresolved questions, each with an identifier) and `evidence_use` to the unchanged Pilot 1 output schema.
4. A gate rejects any answer or tool call before retrieval (up to two gate turns).

### Execution fixes and their regression tests

| Pilot 1 problem | fix | test |
|---|---|---|
| 4 runs ended unparseable: complete answers missing one closing brace | lenient parser appends up to three closing braces when the result is a complete object | `LenientParse.test_missing_closing_brace`; all four Pilot 1 failures recovered from their raw replies (`test_pilot1_failures_recovered`) |
| 13 first-turn protocol errors: a bare output object without the action wrapper | bare output objects and unwrapped finals with the required fields are accepted | `test_bare_output_and_unwrapped_final`, `test_tool_without_action` |
| 40 repair turns | no repair turn for a recoverable reply | `Gate.test_no_repair_turn_for_recoverable_reply` |
| unsafe inputs | truncated strings, missing fields and non-JSON are still rejected; the Pilot 1 strict parser is unchanged | `test_unsafe_inputs_rejected`, `test_protocol1_parser_unchanged` |

Further tests cover the retrieval gate, empty retrieval in A, identical ranked items in B and C, identical
instructions across conditions, the retrieval audit, the model-version stop and the fact that the added retrieval
fields do not change any score (70 tests, all passing). Pilot 2 needed 0 repair turns (Pilot 1: 40); 71 replies were
accepted through the lenient parser, mostly bare output objects.

## Primary outcome (P1, balanced flag accuracy)

The Pilot 1 comparator is the Pilot 1 raw output with its four unparseable answers recovered by the Pilot 2 parser
(identical to the Pilot 1 "recovered" sensitivity analysis). The Pilot 1 primary analysis, which scored those four as
missing, gave A 0.417, B 0.583, C 0.583.

| condition | Pilot 1 (recovered) | Pilot 2 |
|---|---|---|
| A, no memory | 0.583 | 0.583 |
| B, documents | 0.625 | 0.583 |
| C, graph | 0.583 | 0.542 |

| Pilot 2 contrast | tasks | mean difference | 95% interval | p (sign-flip) | p (Holm) |
|---|---|---|---|---|---|
| B - A | 10 | -0.042 | -0.375 to 0.250 | 1.00 | 1.00 |
| C - A | 10 | -0.042 | -0.375 to 0.250 | 1.00 | 1.00 |
| C - B | 10 | 0.000 | -0.375 to 0.375 | 1.00 | 1.00 |

C and B are not shown equivalent (90% interval -0.25 to 0.25 against a 0.10 margin). One B output (RT-179) failed the
schema because it used the risk code `ARTIFACT`, which is not in the taxonomy; under the unchanged scoring rules it is
excluded from balanced accuracy, and its flag was wrong.

Secondary outcomes (descriptive, uncorrected):

| metric | P1 A | P1 B | P1 C | P2 A | P2 B | P2 C |
|---|---|---|---|---|---|---|
| testability AUC | 0.625 | 0.812 | 0.719 | 0.656 | 0.938 | 0.688 |
| outcome log loss (lower is better) | 1.897 | 1.589 | 1.761 | 2.003 | 1.631 | 1.803 |
| risk recall | 0.417 | 0.417 | 0.417 | 0.583 | 0.400 | 0.583 |

B's testability and outcome calibration are better than A's in both pilots, which is the only consistent memory signal
across the two pilots; with 10 tasks and no correction it is a lead, not a finding. Risk recall rose in A and C, which
points to the summarising step rather than to memory content.

## Three effects, kept separate

| effect | contrast | P1 (balanced accuracy) | citing relevant prior work |
|---|---|---|---|
| making memory available (use optional) | Pilot 1: B - A, C - A | +0.042, 0.000 | +0.3, +0.1 |
| requiring retrieval, no content | A2 - A1 | 0.000 (-0.25 to 0.25) | 0 (A has no content) |
| requiring retrieval, with content | B2 - B1, C2 - C1 | -0.083 (-0.50 to 0.33), -0.042 (-0.375 to 0.25) | +0.1, +0.2 |
| change in the memory effect | (B2 - A2) - (B1 - A1), (C2 - A2) - (C1 - A1) | -0.083, -0.042 | +0.1, +0.2 (0 to 0.5) |
| the retrieved information, procedure held fixed | Pilot 2: B - A, C - A | -0.042, -0.042 | +0.4 (0.1 to 0.7), +0.3 |

Making memory available had no detectable effect on decisions in Pilot 1. Requiring retrieval increased use of
memory, most clearly in C, but did not change decisions. With the procedure held fixed, the retrieved information did
not improve P1.

The most direct evidence is inside the Pilot 2 runs. In 23 runs the model first produced a complete answer before
retrieving; the gate rejected it, the model retrieved, and it answered again. Comparing the two answers in the same run:

| condition | runs with a pre-retrieval draft | flag changed | decision changed | wrong to right | right to wrong | mean change in p(testable) |
|---|---|---|---|---|---|---|
| A (empty retrieval) | 6 | 0 | 0 | 0 | 0 | 0.04 |
| B | 8 | 0 | 1 | 0 | 0 | 0.13 |
| C | 9 | 1 | 0 | 1 | 0 | 0.07 |

The retrieved records shifted probabilities somewhat (more in B than in A) but changed the flag decision in one of 17
memory runs. The model largely decides before reading and then reports the retrieved evidence alongside an unchanged
decision.

## Did retrieval reach and get used?

Relevance is defined from data only. A prior family is question-relevant if it shares the task family's question
cluster, is a recorded knowability precedent, or has a record at or above the calibrated merge similarity (0.231). It
is lesson-relevant if it is an untestable, artifact or uncertain family in the snapshot carrying one of the task's
expected risk codes. Three tasks (RT-065, RT-101, RT-146) have no relevant family in memory at all, so for them the
correct behaviour is to report that nothing relevant was found.

| per condition (10 runs) | P1 A | P1 B | P1 C | P2 A | P2 B | P2 C |
|---|---|---|---|---|---|---|
| retrieval attempted | n/a | n/a | n/a | 10 | 10 | 10 |
| retrieval successful (a relevant family among returned items) | n/a | n/a | n/a | 0 | 5 | 4 |
| a relevant family appeared in any memory result | 0 | 3 | 1 | 0 | 5 | 5 |
| output cites a relevant family it was shown | 0 | 3 | 1 | 0 | 4 | 3 |
| meaningfully used (successful, cites it, explains its effect) | n/a | n/a | n/a | 0 | 4 | 3 |
| mean memory calls per run | 0 | 0.8 | 0.5 | 0 | 1.0 | 1.0 |
| follow-up memory calls after retrieval | n/a | n/a | n/a | 0 | 0 | 0 |

Retrieval was attempted in every run and was first in every run. An empty result (A, and the three tasks with nothing
relevant) is never counted as success. Successful retrieval needs relevant items in the top eight: on the seven tasks
with relevant prior work, a relevant family was among the returned items in five (B) and four (C). Relevant families
often rank far below eighth (for RT-012, with the research question as the query, the first relevant family ranks
about 90th), and no agent searched further.

## Was the evidence represented correctly?

| check | P2 B | P2 C |
|---|---|---|
| status claims about prior work that can be checked | 20 | 25 |
| status matches the family's stratum in the snapshot | 18 (90%) | 16 (64%) |
| of these, status stated in a returned record / inferred | 0 / 20 | 0 / 25 |
| cited identifiers never shown by any tool | 0 | 3 (one run) |
| runs claiming prior work already answered the question when it had not (`false_prior_claim`) | 0.29 of scorable runs | 0.13 |

No returned item stated a family's adjudicated outcome, so every status claim was the model's inference from an
experiment, result or hypothesis record. B's inferences were mostly right; C's were wrong more often, mainly by calling
uncertain or untestable work "supported" or by labelling everything "uncertain" (RT-014). The three unshown
identifiers in C (RT-012) are labels the model invented for its own limitation notes (`STATLIMIT_129`, `STATLIMIT_130`,
`RQ_345`), not claims about a prior result; they still break the instruction to cite only identifiers that were shown.
A made no prior-work claims (its retrieval was empty), so retrieval introduced the only incorrect prior assumptions,
at a modest rate. Statuses the answer schema cannot express (`not_a_test`, `no_result`) are excluded from these counts.

## Per task

`1` = correct flag decision, `0` = incorrect.

| task | stratum | should flag | relevant families in memory | P1 A B C | P2 A B C | P2 B, C cite relevant |
|---|---|---|---|---|---|---|
| RT-012 | artifact | yes | 4 | 0 0 0 | 0 0 0 | no, no |
| RT-014 | artifact | yes | 6 | 1 1 1 | 1 0 1 | no, no |
| RT-065 | rejected | no | 0 | 0 0 0 | 0 0 0 | no, no |
| RT-066 | rejected | no | 21 | 1 1 1 | 1 1 1 | no, yes |
| RT-101 | supported | no | 0 | 1 1 1 | 1 1 1 | no, no |
| RT-112 | supported | no | 7 | 1 1 1 | 1 1 1 | yes, yes |
| RT-146 | uncertain | no | 0 | 1 0 1 | 0 1 1 | no, no |
| RT-147 | uncertain | no | 1 | 0 0 0 | 1 1 1 | yes, no |
| RT-179 | untestable | yes | 6 | 0 1 0 | 0 0 (invalid) 0 | yes, no |
| RT-183 | untestable | yes | 22 | 1 1 1 | 1 1 0 | yes, yes |

RT-147 improved in all three conditions including A, so the change comes from the procedure, not from memory. RT-012
(artifact, recorded precedent available) was missed by every condition in both pilots, and RT-065 was flagged wrongly
everywhere. Runs that cited relevant evidence were correct more often (Pilot 2 B and C: 5 of 7 against 7 of 13), but
this is an observational association across different tasks, not an effect of retrieval.

## Cost and completion

| | P1 A | P1 B | P1 C | P2 A | P2 B | P2 C |
|---|---|---|---|---|---|---|
| ended with a final answer | 7 | 9 | 10 | 10 | 10 | 10 |
| valid output (after recovery for P1) | 10 | 10 | 10 | 10 | 9 | 10 |
| repair turns | 16 | 12 | 12 | 0 | 0 | 0 |
| gate turns | 0 | 0 | 0 | 7 | 9 | 9 |
| cost (USD) | 0.181 | 0.209 | 0.184 | 0.126 | 0.163 | 0.178 |

Retrieval itself took under 0.01 seconds per call. Retrieved content stays in the context for later turns, an
estimated 750 (B) and 1,170 (C) input tokens per run, under 0.001 USD per run. Pilot 2 was cheaper than Pilot 1
because repair turns disappeared. A 78-task, three-condition run at Pilot 2 cost per run (about 0.0156 USD) would cost
roughly 3.7 USD per seed.

## Uncertainty and limitations

- Ten tasks and one seed. A single task changing its flag moves a condition's P1 by 0.083 to 0.125; every interval
  includes zero, and the pilot is consistent with effects from about -0.4 to +0.3.
- Temperature 0.7 with one seed confounds run-to-run sampling noise with condition effects. RT-146 flipped in
  opposite directions in A and B between pilots, which is what noise looks like.
- The cross-pilot comparison changes three things at once (required procedure, lenient parser, extended schema). A2 - A1
  measures their combined effect without content; it does not separate them.
- The answer key and the relevance sets are automated. Relevance defined by question clusters, precedents, similarity
  and shared risk codes may miss records a human would judge relevant, or include weakly relevant ones.
- The ranking and item format of `retrieve_history` were designed for Pilot 2 and not tuned against the answer key
  (tuning them toward known relevant families would leak the key). Its record-type mix (no family records in the top
  eight) is a property of this design, and the results depend on it.
- Status correctness is measured against the snapshot's automated strata, which the agent was never shown directly.
- The first Pilot 2 run records a different code hash from the other 29 because the retrieval audit module, which runs
  do not use, was edited while the run was in progress. The scoring, audit and comparison were all recomputed
  afterwards from the unchanged raw runs.
- The model is deprecated by its provider (announced 2026-11-02), and requests are routed to newer models from
  2026-12-01. Any further run with the same model version must finish before then, or the comparison with both pilots
  is lost.

## Is the signal sufficient to justify scaling?

No, not for the benchmark as configured. In order of strength:

1. The primary outcome shows no memory benefit in either pilot (Pilot 2 B - A and C - A both -0.042).
2. Within a run, retrieved content changed the flag decision once in 17 opportunities, so a larger sample would mostly
   measure a decision the model makes before retrieval.
3. Required retrieval did raise memory use (relevant evidence reached the agent in 5 of 10 runs in B and C, against 3
   and 1 in Pilot 1), and B's calibration measures are better than A's in both pilots. These are the reasons not to
   abandon the comparison, but they are secondary and uncorrected.
4. C did not outperform B on any measure and represented prior statuses less accurately (64% against 90%).

What would make a scaled run informative, without changing the answer key, the scoring or the research history:

- Show the decision-relevant content. Include study-family records (adjudicated outcome, failure mechanism,
  limitations) in what `retrieve_history` returns, identically in B and C, so the agent sees what earlier work
  concluded rather than inferring it from experiment records.
- Make retrieval precede the decision. Ask for the research question and retrieval before any draft assessment (the
  gate already rejects drafts, but 23 of 30 runs wrote one first), or ask the agent to state explicitly what the
  retrieved evidence changes.
- Measure noise. Run at least three seeds, or temperature 0, so condition effects can be separated from sampling.
- Re-pilot those changes on the same 10 tasks (about 0.5 USD per seed) before committing to 78 tasks, and finish
  before the 2026-12-01 model routing change.

## Files

- `runs/pilot2_v1/raw/`: 30 run records (full prompts, replies, tool calls, retrieval queries, returned identifiers, latency, usage, model version)
- `runs/pilot2_v1/scores.csv`, `analysis.json`, `report.md`: automated scores, including the per-run retrieval audit
- `runs/pilot2_v1/comparison/`: `per_run.csv`, `per_task.csv`, `contrasts.csv`, `draft_vs_final.csv`, `summary.json`
- `configs/pilot2.json`, `configs/pilot2_mock.json`; `bench/retrieval_audit.py`; `scripts/23_compare_pilots.py`; `tests/test_pilot2.py`
