# Stage 1 user message (RT-012)

Supports Appendix B of Paper 1.

Research question (as posed on 2026-06-14, in the area of play-type labeling and data quality): Any teammate DRIVE preceding a PNR raises PNR PPP.

Data available on that date:

- NBA 2022-23 regular season and playoffs
- NBA 2023-24 regular season and playoffs
- NBA 2024-25 regular season and playoffs
- NBA 2025-26 regular season (complete from 2026-04-13; partial before)
- NBA 2025-26 playoffs (complete from 2026-06-21; partial before)
- Sources: Per-game files from the NBA stats API: play-by-play (action type, sub-type, clock, period, score, player, shot distance and result), substitution rotation intervals, starters, defensive matchup minutes and partial possessions, box-score summary. Derived play-type possession records (initiator, play type, points) in a graph database built from the play-by-play.

Your job is to decide, before any analysis is run, whether this question can be answered with this data, what has already been established about it, which methodological and statistical risks threaten a test of it, and either a pre-registration-quality design or a reasoned recommendation not to proceed.

Stage 1. Reply only with the retrieval call.
