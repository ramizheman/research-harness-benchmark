# Remaining human requirements

Everything needed to generate tasks, memory, answer keys, challenges, runs, scores and statistics is automated. A human is still required only where the requirement is authority (credentials, money), independence (ground truth), or judgment that the automated screens cannot honestly supply. Each item says when it is needed and what happens without it.

## Required before the pilot can run

**1. A working model API key.**
- **What is needed.** The OpenRouter, OpenAI and Anthropic keys in `App\Strategy\.env` all return HTTP 401. The keys are well formed, so they have most likely been revoked or have expired. One valid key is enough: an OpenRouter key works with the current `configs\pilot.json`.
- **Effort.** Creating or renewing a key, about 5 minutes.
- **Without it.** Only the mock dry run is possible.

**2. Permission to spend.**
- **What is needed.** The pilot is about 0.14 USD by estimate, capped at 5 USD in the config. The runner refuses paid configs without `--confirm-spend`.

## Required before results are described as more than agreement with automated labels

**3. A small independent check of answer-key labels.**
- **Why.** The answer key is automated adjudication. Without an independent check, every replay score means "agreement with rule-based labels", and a high score could reflect a model that reproduces the same keyword logic.
- **Minimum.** A person who did not build the rules reads the source records for a random stratified sample and assigns a stratum without seeing the automated one. For the pilot, the 10 pilot tasks; for the main study, 30 tasks (6 per stratum). The error rate then bounds how far scores can be trusted.
- **Who.** The user can do this, but is not independent of the original research. A basketball analyst outside the project is better.
- **Without it.** Results are still reportable, labelled as provisional and relative to automated labels.
- **Not a substitute.** An LLM reviewer. A different model shares conventions and training data with the agents being scored. An LLM screen is already used as a filter: the model that built this pipeline screened the pilot entries, and one family (SF-APPA-046) was excluded because its hypothesis and verdict point in opposite directions (`audit\answer_key_flags.csv`). The screen did not relabel anything, and it must never be reported as independent.

## Required only for the prospective arm, and only if a claim survives validation

**4. Novelty against the published literature.**
- **Why.** Lexical screening against the project's own history is automated. Novelty against external sports-analytics research is not: search tools find candidate papers, but deciding whether a result is already known needs domain judgment.
- **When.** Needed only for claims that survive sealed validation, which are expected to be rare.

**5. Usefulness of a validated discovery.**
- **Why.** Whether a surviving result would change a coaching, roster or analysis decision is a judgment. A pre-specified usefulness rubric can structure it, but someone with basketball context must apply it.

**6. Network isolation for the code sandbox.**
- **Why.** On Windows, blocking network access for agent-run code needs either administrator rights (a firewall rule) or a container runtime.
- **When.** Needed once, when the prospective sandbox is built.

## Optional

**7. External timestamp.**
- **What.** Publishing the claim registry's closing hash before 2027-04-12, for example by sending it to an e-mail address or committing it to a repository.
- **Why it is optional.** The hash chain already proves order and integrity internally. Publishing the hash proves to an outsider that the claims predate the validation data.

**8. Final interpretation.**
- **What.** Deciding what the pilot result means for the research workflow, whether to scale up, and whether to keep, simplify or drop the graph memory.
- **Why a human.** The analysis follows pre-specified decision rules, but acting on them is a decision for the project owner.

## Not required

The following need no human at any stage:
- adjudicating families or resolving conflicts;
- dating records;
- clustering questions;
- correcting extends directions;
- generating task statements;
- selecting tasks;
- excluding leaked memory;
- writing or ranking challenges;
- running agents;
- redacting and blinding;
- registering and validating claims;
- scoring and statistics.

Every rule is in code, every decision has a recorded reason, and the unit tests run in a few seconds.
