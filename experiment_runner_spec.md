# Experiment runner specification

Code: `runner\` (`llm.py`, `tools.py`, `agent.py`, `experiment.py`), `scripts\20_run_experiment.py`, `scripts\21_preflight.py`, `configs\`. Tests: `tests\test_runner.py`.

## 1. What is held identical across conditions

| element | A (no memory) | B (documents) | C (graph) |
|---|---|---|---|
| task statement | frozen file, hash checked before every run | same | same |
| system prompt | identical text; only the tool list differs (unit test strips the tool block and compares) | same | same |
| always-available tools | glossary, data_catalog | same | same |
| memory tools | none | search_documents, read_document | query_graph (find, node, neighbors) |
| memory content | none | task snapshot documents | task snapshot graph, same canonical facts (equivalence checked) |
| free-text ranking | not applicable | TF-IDF | TF-IDF (same vectoriser settings) |
| budgets | max 12 tool calls, 2 repair turns, 250,000 tokens, 900 seconds, 6,000 characters per tool result | same | same |
| model, temperature, seed, max output tokens | from config | same | same |
| output schema and scoring | identical | same | same |

## 2. Run plan

A config lists models, tasks, conditions and seeds. `experiment.plan` forms every combination and shuffles the order with a fixed seed. This interleaves conditions so that provider drift over the session does not line up with a condition.

The run ID is `<experiment>|<provider:model>|<task>|<condition>|s<seed>`.

`configs\pilot.json` defines:
- 1 model through OpenRouter;
- 10 pilot tasks (2 per stratum);
- conditions A, B and C;
- seed 1;
- 30 runs in all, with a cost cap of 5 USD.

`configs\pilot_mock.json` defines the same plan with the scripted mock client.

## 3. Agent protocol

Every model reply must be exactly one JSON object:

- `{"action": "tool", "tool": ..., "args": {...}}`
- `{"action": "final", "output": {...}}`

This works the same way for every provider: there is no provider-specific function calling, so differences between providers' tool-calling implementations cannot enter the comparison.

**Tool results.** Each result is returned as a user message beginning with `TOOL_RESULT`, truncated to the character limit.

**Malformed replies.** A malformed reply gets a repair prompt naming the problem. After two failures the run stops as `unparseable`.

**Budget exhaustion.** When the tool budget is reached, the next message instructs the model to finish. Token and wall-clock budgets end the run with the stop reason recorded.

## 4. Frozen inputs and per-task memory

- **Task file.** `tasks\replay\RT-*.json` holds the statement, the task date, the permitted record list, the excluded records and a SHA-256 hash over the task ID, statement and permitted list. `load_task` refuses a file whose hash no longer matches.
- **Snapshot.** `memory_v2\snapshots\<task>\` is built on first use from the permitted records, then reused. `ensure_snapshot` refuses a snapshot when:
  - its record list differs from the task's permitted list;
  - its documents and graph are not equivalent;
  - it contains an excluded record.
- **Run record.** Each run stores the task hash, the snapshot fact hash, the config hash and a hash of all code in `bench\` and `runner\`.

## 5. Logging and reproducibility

`runs\<experiment>\raw\<run>.json` stores the full message history and every reply. For each turn it also records the parse result, token usage, tool name, arguments and result size. Run-level fields are the stop reason, tool and memory-tool counts, wall-clock time, total tokens and cost (USD where OpenRouter reports it).

`runs\<experiment>\manifest.json` stores the config, its hash, the code hash and the creation time.

**Resuming.** An existing run file is never overwritten. Re-running the same config resumes with the missing runs only.

**Reproducibility limits.** Model sampling is not bit-reproducible across providers, even with a seed. Reproducibility here means that the inputs, memory, code and protocol are fixed and recorded, and that the analysis can be repeated exactly from the saved runs.

## 6. Blinding, redaction and claim registration

**Blinding.** The `blind` phase writes `runs\<experiment>\blinded\<blind id>.json`, containing the task statement and the redacted output, with no condition, model or run ID. The blind ID is an HMAC of the run ID. The map and secret are in `runs\<experiment>\sealed\blinding_key.json`.

**Claims (prospective arm).** Claims are registered with `bench\claims.register` under the blind ID before any validation data exists locally. `scripts\14_fetch_2026_27.py` refuses the validation window until `claims.release_allowed` passes: the registry verifies, it is closed, and today is after 2027-04-12. The development fetch requests only games dated 2026-10-20 to 2027-01-30, so results from the validation period are never downloaded early.

## 7. Phases

| phase | command | output |
|---|---|---|
| pre-flight | `21_preflight.py configs\pilot.json` | checks of tasks, snapshots, answer key, API key and model listing; cost estimate; spends nothing |
| run | `20_run_experiment.py <config> --phase run --confirm-spend` | raw runs (paid configs refuse to start without `--confirm-spend`) |
| blind | `--phase blind` | blinded outputs and sealed key |
| score | `--phase score` | `scores.csv` |
| analyze | `--phase analyze` | `analysis.json`, `report.md` (mock runs are labelled MOCK at the top) |

## 8. Mock dry run (completed 2026-11-10)

`configs\pilot_mock.json` ran 30 of 30 runs. Every run ended with a valid final output, B and C each made one memory call per run, and the run was blinded, scored and analysed (`runs\pilot_mock\report.md`).

The mock client is scripted. Its numbers test the code path and say nothing about memory.

The dry run exposed and fixed two problems:
- the graph tool's free-text search was a word-overlap count with constant ties, weaker than document search; it now uses the same TF-IDF ranking;
- a threshold lookup used the wrong data type.

## 9. Pilot readiness

| item | status |
|---|---|
| 10 frozen tasks, snapshots equivalent, answer key present | ready (pre-flight PASS for all 10) |
| runner, scoring, analysis, report | ready (mock dry run complete; 41 unit tests pass) |
| model and price | `openai/gpt-4.1-mini` listed on OpenRouter at 0.40 / 1.60 USD per million input / output tokens; estimated pilot cost about 0.14 USD |
| API key | **blocked**: the OpenRouter, OpenAI and Anthropic keys in the project `.env` all return HTTP 401 |

Once a valid key is in place, the pilot runs with two commands (see `automation_plan.md`). The provider and model can be changed in `configs\pilot.json` without code changes: providers `openrouter`, `openai` or `anthropic`.

## 10. Not built yet (by design)

- **Prospective agent sandbox.** A code-execution tool for the 2026-27 development data, for challenge runs. Its requirements:
  - a subprocess per call, with a timeout and a working directory per run;
  - read-only access to `data_2026_27\development\`;
  - no network access;
  - claim registration through `bench\claims` as the only exit for results.

  On Windows, network isolation needs an external mechanism, such as a firewall rule or a container. That is a reason to build the sandbox only after the replay pilot shows whether memory matters.
- **Multiple models and seeds.** The config supports them now. Adding them before the pilot is unnecessary cost.
