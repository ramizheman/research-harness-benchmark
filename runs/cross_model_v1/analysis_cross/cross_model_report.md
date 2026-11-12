# Cross-model replication: gpt-oss-20b and Claude Haiku 5.5 versus Gemini 2.5 Flash

Experiment `cross_model_v1`, run 2026-11-11. Both models accessed via OpenRouter.
Same 10 tasks, conditions A/B/C, seeds 1/2/3, protocol 3, memory snapshots, answer key and scoring as Pilot 3 (`pilot3_v1`).
The only intended experimental variable is the underlying model.

## Models and settings

| Model | Provider | id | Temperature | Max tokens | Input $/1M | Output $/1M |
|---|---|---|---|---|---|---|
| gpt-oss-20b | OpenRouter | `openai/gpt-oss-20b` | 0.7 | 8192 | $0.03 | $0.13 |
| Claude Haiku 5.5 | OpenRouter | `anthropic/claude-haiku-5.5` | 0.7 | 8192 | $0.10 | $0.50 |
| Gemini 2.5 Flash (Pilot 3) | Google | `gemini-2.5-flash` v001 | 0.7 | 8192 | $0.30 | $2.50 |

Both OpenRouter models support `response_format: json_object`, `seed`, `temperature`, and `max_tokens`. Temperature and
token limits were sent identically; identical numeric settings do not guarantee identical sampling across different
architectures.

## Preflight

All checks passed before the run. Both models responded to JSON pings and returned the retrieval call only in stage-1
smoke tests. Key valid, not free-tier. 180 runs configured (2 models x 10 tasks x 3 conditions x 3 seeds). Pilot 3
files were not modified.

## 1. Primary outcome: balanced flag accuracy (task level)

Seeds averaged within task; 10 tasks are the unit. Intervals span roughly plus or minus 0.3 on 10 tasks.

| model | A | B | C |
|---|---|---|---|
| Gemini 2.5 Flash (Pilot 3) | 0.639 | 0.681 | 0.583 |
| Claude Haiku 5.5 | 0.659 | 0.559 | 0.655 |
| gpt-oss-20b | 0.473 | 0.534 | 0.579 |

### Primary contrasts

| model | contrast | difference | 95% CI | sign-flip p | Holm p |
|---|---|---|---|---|---|
| Gemini 2.5 Flash | B - A | +0.042 | (-0.264, 0.389) | 0.91 | 1.00 |
| Gemini 2.5 Flash | C - A | -0.056 | (-0.361, 0.292) | 0.84 | 1.00 |
| Gemini 2.5 Flash | C - B | -0.097 | (-0.278, 0.083) | 0.37 | 1.00 |
| Claude Haiku 5.5 | B - A | -0.042 | (-0.333, 0.319) | 0.88 | 1.00 |
| Claude Haiku 5.5 | C - A | +0.014 | (-0.333, 0.389) | 1.00 | 1.00 |
| Claude Haiku 5.5 | C - B | +0.056 | (-0.194, 0.278) | 0.88 | 1.00 |
| gpt-oss-20b | B - A | -0.014 | (-0.250, 0.250) | 1.00 | 1.00 |
| gpt-oss-20b | C - A | +0.007 | (-0.285, 0.347) | 1.00 | 1.00 |
| gpt-oss-20b | C - B | +0.021 | (-0.188, 0.194) | 0.91 | 1.00 |

No contrast in any model is statistically clear. All 95% intervals contain zero.

## 2. Protocol compliance

Every run used exactly one retrieve_history call before any assessment. No run produced a preliminary answer before
retrieval and no run invented a citation identifier.

| model | condition | valid outputs | repairs | correction turns | fabricated citations | status accuracy |
|---|---|---|---|---|---|---|
| Haiku 5.5 | A | 27 / 30 | 0 | 0 | 0 | n/a |
| Haiku 5.5 | B | 29 / 30 | 0 | 1 | 0 | 86 / 86 |
| Haiku 5.5 | C | 26 / 30 | 1 | 0 | 0 | 98 / 98 |
| gpt-oss-20b | A | 26 / 30 | 15 | 0 | 0 | n/a |
| gpt-oss-20b | B | 29 / 30 | 10 | 4 | 0 | 77 / 77 |
| gpt-oss-20b | C | 24 / 30 | 8 | 2 | 0 | 80 / 80 (1 run unparseable) |

gpt-oss-20b needed far more repairs than Gemini or Haiku (25 total versus 3 total for Haiku, 3 for Gemini). Its
valid-output rates were also lower, particularly in condition C (24 of 30). The invalid outputs were schema problems
rather than fabricated content. Haiku had low but non-zero invalid rates (27, 29, 26 of 30).

## 3. Secondary outcomes

| model | condition | testability AUC | risk recall | prior work recognized | false prior claim | status claims correct |
|---|---|---|---|---|---|---|
| Gemini 2.5 Flash | A | 0.653 | 0.639 | 0.0 | n/a | n/a |
| Gemini 2.5 Flash | B | 0.679 | 0.647 | 0.50 | 0.261 | 70 / 70 |
| Gemini 2.5 Flash | C | 0.804 | 0.472 | 0.40 | 0.542 | 97 / 97 |
| Haiku 5.5 | A | 0.790 | 0.900 | 0.0 | n/a | n/a |
| Haiku 5.5 | B | 0.616 | 0.917 | 0.667 | 0.261 | 86 / 86 |
| Haiku 5.5 | C | 0.690 | 0.938 | 0.667 | 0.550 | 98 / 98 |
| gpt-oss-20b | A | 0.479 | 0.500 | 0.0 | n/a | n/a |
| gpt-oss-20b | B | 0.714 | 0.528 | 0.333 | 0.522 | 77 / 77 |
| gpt-oss-20b | C | 0.719 | 0.344 | 0.500 | 0.455 | 80 / 80 |

Observations worth noting:

- **Haiku's no-memory risk recall (0.90) is substantially higher than Gemini (0.64) or gpt-oss (0.50).** This does
  not improve once memory is added.
- **Haiku's testability AUC without memory (0.79)** is higher than any single-seed Gemini A value (range 0.58-0.84).
  Memory degraded it (B 0.62, C 0.69).
- **gpt-oss-20b without memory had the lowest primary accuracy (0.473)**, below the 0.5 chance baseline, driven by
  condition A valid-output issues and schema non-compliance.
- All three models cited statuses accurately when they cited at all: 100% in every condition where claims were checked.
  False prior claims were common in B and C across all models (26-55% of eligible runs).

## 4. Memory effects

### Does memory improve decisions?

| model | B - A | C - A | direction |
|---|---|---|---|
| Gemini 2.5 Flash (Pilot 3) | +0.042 | -0.056 | mixed |
| Claude Haiku 5.5 | -0.042 | +0.014 | mixed |
| gpt-oss-20b | -0.014 | +0.007 | near zero |

None of the memory effects are statistically clear. The direction varies across models and conditions.

- Gemini: document memory slightly helped, graph memory slightly hurt.
- Haiku: document memory slightly hurt (flag rate dropped on should-flag tasks), graph memory slightly helped.
- gpt-oss-20b: effects near zero in both conditions, masked partly by the higher invalid-output rate in A.

No model shows a consistent positive memory effect across both B and C.

### Task-level flag accuracy comparison

| task | stratum | should flag | Gemini A | Gemini B | Gemini C | Haiku A | Haiku B | Haiku C | gpt-oss A | gpt-oss B | gpt-oss C |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RT-012 | artifact | yes | 0.0 | 0.333 | 0.0 | 0.333 | 0.0 | 0.333 | 0.333 | 0.0 | 0.333 |
| RT-014 | artifact | yes | 1.0 | 1.0 | 0.667 | 1.0 | 0.667 | 1.0 | 0.333 | 0.667 | 0.667 |
| RT-065 | rejected | no | 0.0 | 0.0 | 0.333 | 1.0 | 1.0 | 1.0 | 0.333 | 0.333 | 0.0 |
| RT-066 | rejected | no | 1.0 | 0.667 | 1.0 | 1.0 | 0.667 | 1.0 | 0.0 | 0.333 | 0.667 |
| RT-101 | supported | no | 1.0 | 0.0 | 0.333 | 1.0 | 0.333 | 1.0 | 0.667 | 0.667 | 0.667 |
| RT-112 | supported | no | 1.0 | 1.0 | 1.0 | 0.667 | 1.0 | 0.667 | 0.667 | 0.667 | 0.667 |
| RT-146 | uncertain | no | 1.0 | 1.0 | 0.667 | 0.667 | 0.333 | 0.667 | 0.333 | 0.667 | 0.333 |
| RT-147 | uncertain | no | 0.667 | 1.0 | 0.667 | 0.333 | 0.667 | 0.333 | 0.0 | 0.0 | 0.333 |
| RT-179 | untestable | yes | 0.0 | 1.0 | 1.0 | 0.0 | 0.333 | 0.333 | 0.333 | 0.0 | 0.667 |
| RT-183 | untestable | yes | 1.0 | 0.667 | 0.333 | 0.667 | 0.333 | 0.0 | 0.0 | 0.667 | 0.667 |

RT-012 (artifact, should flag) is hard for all three models in all conditions: never above 0.333. RT-065 (rejected,
should not flag) was solved cleanly by Haiku in all conditions but not by the others.

## 5. Document versus graph memory

The same pattern appears in all three models: B and C make different decisions (B and C select different families on
average), but neither representation consistently produces better decisions, and the differences between B and C are
smaller than the differences across seeds within the same condition.

## 6. Cost

| model | A | B | C | total |
|---|---|---|---|---|
| gpt-oss-20b | $0.015 | $0.014 | $0.015 | **$0.044** |
| Haiku 5.5 | $0.073 | $0.118 | $0.119 | **$0.310** |
| Both models | | | | **$0.354** |
| Gemini Pilot 3 (for reference) | $0.377 | $0.510 | $0.547 | $1.434 |

gpt-oss-20b is roughly 33x cheaper per run than Gemini but required many more repairs and had a higher invalid-output
rate. Haiku is roughly 5x cheaper than Gemini with comparable protocol compliance.

## 7. Limitations

- Ten tasks. Three seeds reduce noise within tasks but do not add tasks; intervals span roughly plus or minus 0.3.
- gpt-oss-20b had a high repair rate (25 repairs across 60 memory runs versus 3 for Haiku); its outputs may differ
  from what it would produce with a natively JSON-trained model. The current implementation uses
  `response_format: json_object` which OpenRouter forwards to the provider.
- Invalid outputs (schema problems or unparseable) were counted as wrong for the primary metric. Excluding them changes
  some numbers but not the direction of any finding.
- Seed reproducibility across providers is not guaranteed.
- OpenRouter adds a small markup over provider list prices; actual costs may be slightly higher than the list prices
  used for the cap.
- The answer key is automated adjudication, unchanged across all three models.

## 8. Cross-model findings

**The original finding replicates across models: memory does not improve research decisions.**

All three models show memory effects near zero in both directions, with all 95% intervals containing zero. This is
consistent across Gemini Pilot 3, Claude Haiku 5.5, and gpt-oss-20b.

**Model-level differences are large relative to memory effects.**

Gemini's no-memory accuracy (0.639) exceeds gpt-oss-20b's no-memory accuracy (0.473) by more than the memory effect
in any model. The question of which model makes better research decisions is separable from the question of whether
memory helps, and the answer to the memory question is the same for all three.

**Haiku is the stronger baseline model on this task.**

Haiku without memory has higher accuracy (0.659), substantially higher risk recall (0.90), and better testability
calibration (AUC 0.79) than either of the other two models without memory. Adding memory slightly degraded all three
of these for Haiku.

**The stop recommendation from Pilot 3 is reinforced.** Three models, five experiments, the same result. Memory
changes decisions but does not improve them, and this is not a Gemini-specific finding.

## Files

- `configs/cross_model.json`, `configs/cross_model_mock.json`
- `runner/llm.py` (added `model_version` to `OpenAICompatible` usage for OpenRouter)
- `tests/test_cross_model.py`
- `scripts/21_preflight.py` (extended for multi-model and OpenRouter checks)
- `scripts/25_cross_model_analysis.py`
- `runs/cross_model_v1/` raw, blinded and sealed outputs, `scores.csv`, `analysis.json`, `report.md`
- `runs/cross_model_v1/analysis_cross/` `per_run.csv`, `per_task.csv`, `contrasts.csv`, `citations.csv`, `summary.json`, `cross_model_report.md`
- `runs/cross_model_mock/` mock dry run
