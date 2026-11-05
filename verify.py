# Checks that every quote is an exact substring of its article on lex.uz,
# that nonexistent articles really do not exist, and that IDs are unique.
import json, re, sys

law = json.load(open("data/lex_tk_ru.json", encoding="utf-8"))
A = law["articles"]
norm = lambda s: re.sub(r"\s+", " ", s).strip()
max_art = max(int(k) for k in A)

bad, ids = 0, set()
rows = [json.loads(l) for l in open("data/questions_v1.jsonl", encoding="utf-8")]
for r in rows:
    if r["id"] in ids:
        print("DUP ID", r["id"]); bad += 1
    ids.add(r["id"])
    if r["type"] == "nonexistent_article":
        if str(r["article"]) in A or r["article"] <= max_art:
            print("ARTICLE EXISTS", r["id"], r["article"]); bad += 1
        continue
    art = A.get(str(r["article"]))
    if not art:
        print("NO ARTICLE", r["id"], r["article"]); bad += 1; continue
    if norm(r["quote"]) not in norm(art["text"]):
        print("QUOTE NOT FOUND", r["id"], "art", r["article"], "|", r["quote"][:80]); bad += 1
    if "—" in r["answer_ru"] or "—" in r["answer_en"]:
        pass
print(f"rows={len(rows)} max_article={max_art} errors={bad}")
sys.exit(1 if bad else 0)
