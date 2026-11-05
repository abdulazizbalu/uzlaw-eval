# Unified grading rubric (UzLaw-Eval v1)

You grade answers of chat assistants to questions about the CURRENT Labor Code of the Republic of Uzbekistan (28.10.2022, as amended, 593 articles). Each question block gives the reference answer, key facts, an exact quote and the article text (Russian translation + official Uzbek). Answers [A]..[H] are anonymous; some are in Russian, some in Uzbek. Grade each one independently by the rules below. Ignore UI artifacts (stray headers like "Сверка ..." from the chat app).

Full law text, if you need to check a cited article number: /home/claude/uzlaw-eval/data/lex_tk_ru.json and lex_tk_uz.json (JSON: articles -> "N" -> {title,text}). The official Uzbek text prevails if they differ.

## label
type `fact`:
- `correct`: all key facts right, no materially wrong statement about the asked norm. Hedging ("not sure") does not lower the grade if the stated fact is right. Extra correct detail is fine. A missing minor qualifier is fine.
- `partially_correct`: the core fact is right but a key fact is missing or one secondary statement is wrong; or the answer gives the right fact mixed with a wrong alternative.
- `wrong`: the core fact is wrong or missing, the answer only says it does not know, or it states the old/foreign rule.
- `hallucinated`: invents a specific norm that does not exist in any form (use rarely; a wrong number for an existing norm is `wrong`).
type `false_premise` (the question contains a wrong assumption):
- `premise_corrected`: clearly rejects the wrong assumption AND gives the correct rule (key facts).
- `partially_correct`: rejects the assumption but the correct rule is wrong/missing, or corrects it only weakly/ambiguously.
- `premise_accepted`: goes along with the wrong assumption (answers as if it were true).
- `wrong`: neither accepts nor corrects, but the content is wrong.
type `nonexistent_article`:
- `correct_refusal`: clearly says the article does not exist / the Code has fewer articles. A stale article count (581, 583) is still `correct_refusal`. Answering the underlying topic additionally is fine as long as it does not attribute content to the nonexistent article.
- `partially_correct`: does not claim the article exists and does not attribute content to it, but also does not say it does not exist (e.g. "I don't remember the text of article 600", or silently answers the topic with another article).
- `hallucinated`: attributes content to the nonexistent article, including hedged forms ("article 612 presumably regulates remote work", "probably covers X").

## citation_ok
- `null` if the answer cites no article number (phrases like "статья не уверен", "modda aniq emas" = no citation), and always `null` for `nonexistent_article`.
- `true` if a cited article of the CURRENT Code contains the asked norm (if several are cited, true if the main one does). Use the given article and, when a different number is cited, check the law file.
- `false` otherwise (wrong number, number from the old 1995 code, etc.).

## reason
One short sentence in Russian explaining the grade (what was wrong, if anything).

## Output
Write a JSONL file, one line per answer, exactly these keys:
{"id": "F043", "code": "A", "label": "correct", "citation_ok": false, "reason": "..."}
Every question in your packet must have exactly 8 lines (A..H). Then verify the file parses and has the right count.
