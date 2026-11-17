# Invalid outputs by model and condition

Supports Appendix F of Paper 1. Counts are out of 30 runs each. The same values are in `table19_invalid.csv`.

They were schema failures, not invented findings. gpt-oss-20b had the most (11), followed by Sonnet (9) and Haiku (8); Sonnet's were all in the memory conditions.

| Model | A | B | C |
|---|---:|---:|---:|
| Gemini 2.5 Flash | 0 | 1 | 1 |
| Claude Haiku 5.5 | 3 | 1 | 4 |
| gpt-oss-20b | 4 | 1 | 6 |
| Claude Sonnet 5.5 | 0 | 6 | 3 |
| DeepSeek V4 Pro | 0 | 1 | 1 |
