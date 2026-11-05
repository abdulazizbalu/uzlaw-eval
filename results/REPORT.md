# UzLaw-Eval v1: do chat assistants know Uzbek labor law?

**Date:** 5 November 2026. **Author:** Abdulaziz Abdujalilov.

100 questions on the Labor Code of the Republic of Uzbekistan were asked in two languages, Russian and Uzbek (Latin script), through the consumer web apps of four assistants. The set has 75 factual questions, 15 questions with a false premise and 10 questions about articles that do not exist. Every reference answer is backed by an exact quote from lex.uz. Answers were graded by independent LLM judges that had the full text of the Code.

![Fully correct answers, Russian vs Uzbek](chart_ru_vs_uz.png)

| Assistant (web) | Lang | Fully right | Partly right | Wrong | Invented norm or accepted false premise | Cited article correct |
|---|---|---|---|---|---|---|
| ChatGPT (Plus, reasoning "high") | RU | **97** | 3 | 0 | 0 | 70 of 72 |
| | UZ | **94** | 4 | 2 | 0 | 57 of 59 |
| Gemini (free, "Auto") | RU | **81** | 9 | 10 | 0 | 73 of 96 |
| | UZ | **61** | 10 | 25 | 4 | 41 of 94 |
| Claude (Opus 5.5, effort "high", incognito) | RU | **62** | 10 | 26 | 2 | never cited |
| | UZ | **62** | 6 | 30 | 2 | never cited |
| DeepSeek (DeepThink on, search off) | RU | **52** | 6 | 28 | 14 | 2 of 49 |
| | UZ | **54** | 12 | 25 | 9 | 0 of 25 |

"Fully right" = correct fact, corrected false premise, or "no such article" for a nonexistent one.

## Findings

1. **Language matters a lot for one model and not at all for others.** Gemini lost 20 points when the same questions were asked in Uzbek, and its share of correct article numbers fell from 76% to 44%. ChatGPT lost 3 points. Claude scored the same in both languages.
2. **In Uzbek, Gemini started agreeing with wrong premises.** In Russian it accepted none of the 15 false premises; in Uzbek it accepted 4 (a 5-year fixed-term contract, a 1-month deadline to sue for reinstatement, a 2-year disciplinary sanction, a 9-hour day on a five-day week) and corrected only 6.
3. **Wrong answers usually look like another country's law.** 120 hours of overtime a year, double pay for every overtime hour, a "remark" as a sanction, light work from age 14: these match the old Uzbek code or the Russian Labor Code, not the current Uzbek one. Recent amendments (overtime rules changed in November 2025) were missed by Gemini and Claude in both languages.
4. **Right content, wrong article number.** A large part of Gemini's citations point 1 to 4 articles away from the actual norm. For a lawyer this is a real risk: the answer looks verifiable, but the reference sends you to the wrong place.
5. **Refusals were backed by stale facts.** ChatGPT, Gemini and Claude refused all or nearly all nonexistent articles, but most answers said the Code has 581 or 583 articles. The current version has 593 (articles 582 to 593 were added on 11 June 2026).
6. **DeepSeek invented articles and agreed with wrong premises most often.** In Russian it described the content of 6 of the 10 nonexistent articles (for example, "Article 612 sets out the rights of remote workers") and accepted 8 of 15 false premises; in Uzbek it accepted 9. Its article numbers mostly came from the old 1995 code: 2 of 49 citations were right in Russian, 0 of 25 in Uzbek.
7. **Abstention is not the same as being right.** Claude hedged often ("not sure", no article numbers at all) and never invented an article, but its guesses were often wrong. Calibration, not just accuracy, is worth measuring.

## A side finding about the source text

The Russian text on lex.uz is an unofficial translation; the official text is Uzbek. They can differ: for overtime pay, the official Uzbek Art. 262 says "the first two hours *in a day*", while the Russian translation says only "the first two hours". Benchmarks built on translations should check the official text.

## Method and limits

- Consumer web apps, not APIs: system prompts, memory and model routing are outside our control and change over time. ChatGPT used a temporary chat, Claude an incognito chat, Gemini and DeepSeek regular chats.
- Different tiers: ChatGPT Plus with reasoning, free Gemini, Claude Opus with high effort, free DeepSeek with DeepThink.
- Questions were sent in batches of 10 to 50 per message, with an instruction not to search the web. One run per model and language.
- Graders are LLMs with the law text; each grade has a written reason in `graded_*.jsonl`. The dataset itself was checked automatically (all quotes match lex.uz) and by an independent AI review, but not yet by a qualified lawyer.
- The Uzbek questions are my translations using the terminology of the official text.

## Files

- `data/questions_v1.jsonl`: questions (RU, UZ Latin, UZ Cyrillic), reference answers, key facts, quotes.
- `results/raw_*`: raw model answers. `results/answers_*.jsonl`: answers aligned to questions. `results/graded_*.jsonl`: grades with reasons. `results/summary.json`: the table above.
