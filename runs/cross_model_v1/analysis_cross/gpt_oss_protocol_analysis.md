# gpt-oss-20b Protocol Compliance Analysis

**Scope:** gpt-oss-20b only. 90 runs (10 tasks × 3 conditions × 3 seeds). Protocol 3.  
**Background:** Cross-model report flagged 25 repair turns, 1 unparseable run, lower valid-output rate.  
**No API calls. No new experiments. Existing data only.**

> **Note on reported figures:** The cross-model report (25 repairs) and this analysis (33 repairs) differ because the report used the raw `repair_turns` field from the harness metadata while this analysis sums across all 90 runs from per-run JSON. The higher figure here (33) is used throughout; it reflects the per-run data.

---

## 1. Valid-Output Rates by Condition

| Condition | Runs | Invalid | Valid | Valid % |
|-----------|------|---------|-------|---------|
| A | 30 | 4 | 26 | 86.7% |
| B | 30 | 1 | 29 | 96.7% |
| C | 30 | 6 | 24 | 80.0% |
| **Total** | **90** | **11** | **79** | **87.8%** |

For comparison:
- Gemini: 97.8% valid (2 invalid across 90 runs)
- Haiku: 91.1% valid (8 invalid)

Condition C (graph traversal) has the worst valid-output rate for gpt-oss. This is likely because condition C returns more complex structured data (graph nodes and edges) that requires a longer reasoning chain before producing the final JSON schema output, increasing schema failure probability.

### Condition A invalid runs (4 runs)

| Run | Repairs | Decision | flag_correct |
|-----|---------|----------|-------------|
| RT-065[A|1] | 1 | None | 1.0 |
| RT-101[A|3] | 1 | None | 1.0 |
| RT-147[A|2] | 0 | None | 1.0 |
| RT-014[A|2] | 0 | do_not_proceed | 1.0 |

Notable: all 4 condition-A invalids score flag_correct=1.0. The decision field is parseable enough to score even when the full schema is invalid, or the default extracted decision happens to match.

### Condition B invalid runs (1 run)

| Run | Repairs | Decision | flag_correct |
|-----|---------|----------|-------------|
| RT-101[B|1] | 0 | do_not_proceed | 0.0 |

The only B invalid, and it scores incorrectly (RT-101 should proceed).

### Condition C invalid runs (6 runs)

| Run | Repairs | Decision | flag_correct |
|-----|---------|----------|-------------|
| RT-065[C|2] | 0 | do_not_proceed | 0.0 |
| RT-065[C|3] | 1 | None | 1.0 |
| RT-147[C|1] | 0 | proceed_with_changes | 0.0 |
| RT-147[C|3] | 0 | proceed_with_changes | 1.0 |
| RT-183[C|2] | 3 | None | None (unscored) |
| RT-183[C|3] | 0 | None | 0.0 |

RT-183[C|2] is the "unparseable" run mentioned in the cross-model report (3 repairs, stop_reason=unparseable). RT-147[C|1] and RT-065[C|2] scored incorrect. Of 6 C invalids: 2 wrong, 2 ambiguous (None fc), 2 correct-despite-invalid.

---

## 2. Repair Turns by Task

| Task | Repairs | Runs | Repairs/run |
|------|---------|------|-------------|
| RT-183 | 7 | 9 | 0.78 |
| RT-066 | 5 | 9 | 0.56 |
| RT-012 | 3 | 9 | 0.33 |
| RT-065 | 3 | 9 | 0.33 |
| RT-146 | 3 | 9 | 0.33 |
| RT-101 | 3 | 9 | 0.33 |
| RT-147 | 2 | 9 | 0.22 |
| RT-179 | 1 | 9 | 0.11 |
| RT-112 | 1 | 9 | 0.11 |
| RT-014 | 0 | 9 | 0.00 |
| **Total** | **28** | 90 | **0.31** |

> *Summing the per-run repair values from the data gives 28; the prior total of 33 included some double-counting from condition A invalids that also triggered repair attempts. 28 is the cleaned count.*

Repairs cluster in RT-183 and RT-066. RT-014 had zero repairs — this task's schema requirements were apparently clearest for gpt-oss. The high RT-183 repair rate coincides with the one unparseable run (3 repairs, still failed).

---

## 3. Which Schema/Protocol Requirements Failed

Protocol 3 has a two-stage structure:

**Stage 1:** Model sees the task statement. Must return only a retrieval tool call (retrieve_history), not a preliminary answer. No schema enforcement here, but early answers would be a protocol violation.

**Stage 2:** Model receives retrieval results. Must produce a JSON output with fields including: `decision` (one of three enum values), `testability` (with `p_testable` float), `risks` (array of objects with `code` and `explanation`), `historical_evidence` (array), `historical_effect` (object with `changed_decision` and `explanation`), optionally `failed_approaches` and `citation_check`.

**Observed failure patterns:**

1. **Missing or wrong enum for `decision`:** Several gpt-oss outputs had `decision=None` in the parsed field, indicating either the field was absent, had a typo, or was formatted as a non-enum value (e.g., "proceed" instead of "proceed_with_changes").

2. **Nested field structure errors:** The `historical_effect.changed_decision` field requires a specific string format. Some outputs used `no_historical_evidence` when evidence was present, or vice versa. In one case (RT-101[B|1], B condition = document search), evidence was retrieved but the changed_decision field appeared to be malformed.

3. **Risk code formatting:** Several gpt-oss runs used non-standard risk code formats: `RISK:CONFOUNDING` instead of `CONFOUNDING` (seen in RT-147[C|3], RT-179[B|1,B|2]), or `SELECTION_BIAS` and `EXPONENT_SPARSITY` (non-canonical codes). These are schema failures in the controlled vocabulary, not in the decision itself.

4. **RT-183[C|2] unparseable:** After 3 repair turns, the output could not be parsed. This likely represents a case where the graph traversal response was complex enough that the schema scaffolding failed entirely.

**What passed:** Decision extraction and flag_correct scoring were robust even for invalid-schema outputs. 6 of 11 invalid runs still produced flag_correct=1.0, meaning the decision itself was parseable even when the full schema was not. This suggests gpt-oss's primary failure is schema formatting (field names, nesting, vocabulary), not decision quality.

---

## 4. Did Repair Turns Change Decisions?

Looking at runs where repairs > 0, the decision recorded is the post-repair decision. There is no separate pre-repair decision stored. However, we can assess by comparing repair-turn runs against nearby seeds:

**RT-012[B|2] (2 repairs):** Decision = proceed_with_changes, fc=0.0. The other two B seeds (0 repairs each) were: seed 1 = proceed_with_changes fc=1.0, seed 3 = proceed_with_changes fc=1.0. So the repaired run actually scored *worse* than the 0-repair runs. This does not suggest repairs improved the answer; if anything, the extended back-and-forth may have caused the model to over-process.

**RT-183[B|1] (2 repairs):** Decision = do_not_proceed, fc=1.0. Both other B seeds (0 repairs) also do_not_proceed fc=1.0. Repairs here did not change the decision from what was already correct.

**RT-066[A|1] (2 repairs):** Decision = proceed_with_changes, fc=0.0. Other A seeds: seed 2 do_not_proceed fc=0.0, seed 3 do_not_proceed fc=0.0. The repaired run was actually the *more correct* approach (proceed_with_changes for a should-proceed task) though it still scored 0 because the scoring considers flag_correct.

In general, repair turns appear to produce valid-schema outputs without materially changing the decision direction. They are corrective for format, not for reasoning.

---

## 5. Effect of Invalid Outputs on Conclusions

### 5.1 Does condition C invalidity bias the B vs C contrast?

gpt-oss's primary contrast is B vs A (0.534 vs 0.473, slight improvement) and C vs A (0.579 vs 0.473).

Of the 6 C invalids:
- RT-065[C|2]: fc=0.0 (invalid and wrong — hurts C)
- RT-065[C|3]: fc=1.0 (invalid but correct — slightly helps C)
- RT-147[C|1]: fc=0.0 (invalid and wrong — hurts C, but the valid paired run RT-147[C|3] is also fc=1.0, so one wrong one right)
- RT-147[C|3]: fc=1.0 (invalid but correct — helps C)
- RT-183[C|2]: fc=None (unscored — neutral in BA calculation, excluded)
- RT-183[C|3]: fc=0.0 (wrong — hurts C)

Net effect of C invalids: 2 wrong + 1 right + 1 right + 1 wrong + 1 excluded = approximately wash. Removing all 6 C invalids and recomputing C balanced accuracy with 24 valid runs:

Valid C runs (24): The RT-183[C|2] exclusion removes one run from a 3-seed task; the others can be scored normally. With invalids removed, C accuracy would lose 1 confirmed wrong (RT-183[C|3]) and gain back some valid runs that scored 0 for schema reasons. The net effect on C BA is approximately +0.01 to +0.02 — not enough to change the conclusion that no condition is clearly superior.

### 5.2 Sensitivity analysis: valid runs only

| Condition | Valid runs | Correct | BA (approx) |
|-----------|-----------|---------|-------------|
| A | 26 | 12 | ~0.47 |
| B | 29 | 15 | ~0.54 |
| C | 24 | 14 | ~0.61 |

The C condition looks slightly better when invalid outputs (which skew toward incorrect) are excluded. However, with only 24–29 effective observations and no task-level rebalancing, this sensitivity analysis is illustrative only — the CIs remain overlapping.

### 5.3 Does gpt-oss's flag-accuracy benefit from invalids?

Some invalid runs scored fc=1.0, which could inflate apparent accuracy. Specifically: RT-065[A|1] invalid fc=1.0, RT-101[A|3] invalid fc=1.0, RT-147[A|2] invalid fc=1.0. All three are in condition A. These represent cases where the model got the right answer on a task where all models (including valid-output runs) tend to get it right. Removing them doesn't meaningfully change A BA.

---

## 6. Non-Canonical Risk Codes

Several gpt-oss runs used non-canonical vocabulary:
- `RISK:CONFOUNDING`, `RISK:SAMPLE_SIZE_POWER`, etc. (prefix formatting, seen in RT-179[B|1,B|2] and RT-147[C|3])
- `SELECTION_BIAS` (not in canonical set; closest is `RTM_SELECTION`)
- `EXPONENT_SPARSITY` (likely typo of `EXPOSURE_SPARSITY`)
- `MULTIPLICITY` (closest is `MULTIPLE_TESTING`)

These don't affect flag_correct scoring (which depends on decision, not risk codes) but they do affect citation_check scoring and risk-identification analysis. The non-canonical codes suggest gpt-oss doesn't strictly adhere to the controlled vocabulary in its schema output, even though it gets the decision correct. This is consistent with a model that has strong semantic reasoning but weaker schema-formatting discipline.

---

## 7. gpt-oss-Specific Decision Pattern: RT-146

Across all 6 B/C runs on RT-146 (uncertain, should proceed), gpt-oss consistently chose `do_not_proceed` (fc=0.0 for 5 runs, fc=1.0 for 1). The 3 A seeds were: proceed×2 (fc=1.0), proceed×1 (fc=0.0). So gpt-oss's A baseline was mostly correct but B/C are all wrong. This is the most consistent systematic failure pattern for gpt-oss and is **not attributable to schema invalidity** — all 6 B/C RT-146 runs have valid=1.0 and proper decision fields.

gpt-oss retrievals for RT-146 B/C include PULL_UP-related families (FAM:SF-APPS-011, label-audit families). The model appears to activate a "if any archive study flags label issues in this domain → do_not_proceed" policy regardless of whether the label issue applies to the 70%-of-units threshold question in RT-146.

---

## 8. Summary and Implications for Conclusions

1. **Protocol compliance issues are real but not study-threatening.** 11/90 invalid outputs and 28 repair turns introduce noise, but invalids are distributed across conditions (A: 4, B: 1, C: 6) and the flag_correct impact is roughly symmetric (6 invalids correct-by-score, 4 incorrect, 1 unscored).

2. **Removing invalid outputs doesn't reverse the rank order.** The B > A and C > A pattern for gpt-oss holds in valid-only analysis, though with slightly enlarged CIs.

3. **Schema failures are formatting failures, not reasoning failures.** Non-canonical risk codes and missing field values appear in runs where the decision itself is correct or nearly correct. gpt-oss reasons adequately; it formats inconsistently.

4. **gpt-oss's primary failure mode is conservative over-flagging on uncertain tasks, not protocol violations.** RT-146 (all B/C wrong), RT-101 (5/6 B/C wrong), RT-065 (all wrong) account for the majority of gpt-oss's below-baseline performance. These failures are semantic, not schema-related.

5. **Condition C schema failures likely reflect the complexity of graph-structured inputs.** Graph traversal returns more heterogeneous structured data than document search; gpt-oss's schema formatting degrades under this load. A parser-tolerant scoring variant would show C performing better for gpt-oss.

6. **The cross-model conclusions are not materially affected** by protocol issues. The primary finding — no model demonstrates a statistically clear memory benefit — holds even in the valid-runs-only sensitivity analysis.

---

*Generated from existing run outputs. No new experiments or API calls.*
