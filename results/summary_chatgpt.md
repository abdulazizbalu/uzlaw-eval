# ChatGPT (web, Plus, reasoning "high", temporary chat), 5 Nov 2026

Setup: 100 questions in Russian, sent in 4 messages (10, 10, 40, 40 questions) in fresh temporary chats, with an instruction not to use web search, to answer briefly, cite the Labor Code article and say so when unsure. Question order shuffled, neutral IDs (Q001..Q100). Graded by an independent LLM judge against the lex.uz text.

| Type | Total | Result |
|---|---|---|
| fact | 75 | correct 73, partially correct 2 |
| false_premise | 15 | premise corrected 14, partially correct 1 |
| nonexistent_article | 10 | correctly said "no such article" 10 |

Citations: 70 of 72 cited articles were correct (97%); in 28 answers the model gave no article or said it did not remember the number.

No hallucinated norms, no accepted false premises.

## Notable misses
- Q027 (fixed-term contract "up to 5 years"): did not reject the premise clearly; did not say the initial term is at most 3 years (Art. 110); cited Art. 110 for the 5-year total rule that is in Art. 111.
- Q026 (who cannot be recalled from leave): "harmful and dangerous" instead of "especially harmful and especially hard"; attributed the Group I/II disability rule to Art. 232 (it is Art. 429).
- Q063 (work record books): missed the exception for individual employers; added a condition ("main job") that is not in Art. 125.
- Q049: right answer, wrong article (Art. 171 instead of 125).
- Q069: claimed the Code has 581 articles; the current version has 593 (Arts. 582-593 added by ZRU-1150 of 11.06.2026).

## Caveats
- Web chat, not API: the vendor's system prompt, memory and personalization may affect answers; reasoning mode may use tools despite the instruction (no visible sign of web search).
- Questions were batched, not asked one by one.
- The dataset is not yet lawyer-reviewed.
- Strong result suggests v1 is too easy for a frontier model with reasoning: harder items (cross-article exceptions, recent amendments, Uzbek language) are needed.
