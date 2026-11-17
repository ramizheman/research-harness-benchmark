# Pilots and experiments

Supports Appendix A.1 of Paper 1. The same values are in `table8_pilots.csv`.

A is no memory, B is document retrieval, C is graph retrieval. Balanced accuracy under the primary scoring rule. Pilot 1's no-memory figure is low partly because three of its ten no-memory answers could not be parsed at the time and count as wrong; when those answers are recovered with the parser introduced in Pilot 2, Pilot 1 gives 0.583 / 0.625 / 0.583.

| Experiment | Model | Runs | What changed | A / B / C |
|---|---|---:|---|---|
| Pilot 1 | Gemini 2.5 Flash | 30 | Individual records | 0.333 / 0.500 / 0.583 |
| Pilot 2 | Gemini 2.5 Flash | 30 | Family records, retrieval first | 0.583 / 0.542 / 0.542 |
| Experiment 1 | Gemini 2.5 Flash | 90 | Two-stage protocol, three seeds | 0.639 / 0.681 / 0.583 |
| Experiment 2 | Claude Haiku 5.5 | 90 | Same protocol, new model | 0.625 / 0.583 / 0.639 |
| Experiment 2 | gpt-oss-20b | 90 | Same protocol, new model | 0.542 / 0.528 / 0.528 |
| Experiment 3 | Claude Sonnet 5.5 | 90 | Extended thinking | 0.736 / 0.653 / 0.722 |
| Experiment 3 | DeepSeek V4 Pro | 90 | Extended thinking | 0.514 / 0.681 / 0.722 |
| Primary (3 experiments, 5 models) | | 450 | | |
| Pilots (protocol development) | | 60 | | |
| Total | | 510 | | |
