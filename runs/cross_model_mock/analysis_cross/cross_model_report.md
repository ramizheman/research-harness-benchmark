# Cross-model replication: gpt-oss-20b and Claude Haiku 5.5 versus Gemini 2.5 Flash

Experiment `cross_model_mock`. Mock run — no API calls.
10 tasks, conditions A/B/C, seeds [1, 2, 3]. 1 model(s) x 30 runs = 180 runs.

## Models

- **mock-gpt-oss-20b** (`mock-gpt-oss-20b` via mock, temperature ?, max_tokens ?, input $0.03/1M out $0.13/1M)
- **mock-haiku-5.5** (`mock-haiku-5.5` via mock, temperature ?, max_tokens ?, input $0.1/1M out $0.5/1M)

## Primary outcome: balanced flag accuracy (task level)

Seeds averaged within task.

| condition | mock:scripted | gemini-2.5-flash (P3) |
|---|---|---|
| A | 0.5 | 0.639 |
| B | 0.5 | 0.669 |
| C | 0.5 | 0.574 |

### Primary contrasts (task-paired, 10 tasks, 95% CI from cluster bootstrap)

| model | contrast | difference | 95% CI | sign-flip p | Holm p |
|---|---|---|---|---|---|
| mock:scripted | B - A | 0.0 | (0.0, 0.0) | 1.0 | 1.0 |
| mock:scripted | C - A | 0.0 | (0.0, 0.0) | 1.0 | 1.0 |
| mock:scripted | C - B | 0.0 | (0.0, 0.0) | 1.0 | 1.0 |

## Secondary outcomes

| model | condition | testability AUC | Brier | log loss | risk recall | prior_work_recog | false_prior | citations correct | cost USD |
|---|---|---|---|---|---|---|---|---|---|
| mock:scripted | A | 0.142 | 0.259 | 1.656 | 0.083 | 0.0 | None | n/a | 0 |
| mock:scripted | B | 0.142 | 0.259 | 1.656 | 0.083 | 1.0 | 1.0 | 24.0/24.0 | 0 |
| mock:scripted | C | 0.142 | 0.259 | 1.656 | 0.083 | 1.0 | 1.0 | 48.0/48.0 | 0 |

## Cross-model comparison (memory effect, task-paired)

| models | condition | B-A difference | 95% CI | sign-flip p |
|---|---|---|---|---|
| gemini-2.5-flash | B - A | 0.042 | (-0.264, 0.389) | 0.90625 |
| gemini-2.5-flash | C - A | -0.056 | (-0.361, 0.292) | 0.84375 |
| mock:scripted | B - A | 0.0 | (0.0, 0.0) | 1.0 |
| mock:scripted | C - A | 0.0 | (0.0, 0.0) | 1.0 |

## Protocol compliance

| model | condition | valid | prelim answers | gate turns | repairs | correction turns | fabricated citations |
|---|---|---|---|---|---|---|---|
| mock:scripted | A | 60/60 | 0 | 0 | 0 | 0 | 0 |
| mock:scripted | B | 60/60 | 0 | 0 | 0 | 60.0 | 0 |
| mock:scripted | C | 60/60 | 0 | 0 | 0 | 48.0 | 0 |

## Cost

- **mock:scripted**: $0 (A $0, B $0, C $0)

## Limitations

- Ten tasks. Three seeds reduce per-task noise but do not add tasks; intervals span roughly plus or minus 0.3.
- The answer key is automated adjudication, unchanged from the Gemini pilots.
- Pricing sourced from openrouter.ai/models on 2026-11-11; OpenRouter adds a small markup over provider list prices.
- Temperature and max_tokens are sent identically to both models; identical numeric settings do not guarantee
  identical sampling behaviour across different tokenizers and training regimes.
- Seed reproducibility is not guaranteed across providers.
