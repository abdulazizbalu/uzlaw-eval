import json,random,string
Q=[json.loads(l) for l in open("data/questions_v1.jsonl",encoding="utf-8")]
qmap=json.load(open("prompts/qmap.json"))  # Q### -> ID
inv={v:k for k,v in qmap.items()}
ru=json.load(open("data/lex_tk_ru.json",encoding="utf-8"))["articles"]
uz=json.load(open("data/lex_tk_uz.json",encoding="utf-8"))["articles"]
RUNS=[(f"{p}{m}") for m in ("chatgpt","gemini","claude","deepseek") for p in ("","uz_")]
ans={}
for r in RUNS:
    for l in open(f"results/answers_{r}.jsonl",encoding="utf-8"):
        x=json.loads(l); ans[(r,x["id"])]=x["answer"]
rnd=random.Random(2026)
key={}
Qs=sorted(Q,key=lambda q:inv[q["id"]])
for part in range(4):
    out=[]
    for q in Qs[part*25:(part+1)*25]:
        codes=list(string.ascii_uppercase[:8]); rnd.shuffle(codes)
        a=str(q["article"])
        block=[f"### {q['id']} (type: {q['type']}, article {a})",
               f"Question RU: {q['question_ru']}", f"Question UZ: {q['question_uz_latn']}"]
        if q["type"]!="nonexistent_article":
            block+= [f"Reference answer: {q['answer_ru']}", f"Key facts: {q['key_facts']}", f"Quote: {q['quote']}"]
            if q.get("note"): block.append(f"Note: {q['note']}")
            block.append(f"Art. {a} RU (lex.uz): {ru[a]['title']}\n{ru[a]['text'][:6000]}")
            block.append(f"Art. {a} UZ official (lex.uz): {uz[a]['title']}\n{uz[a]['text'][:6000]}")
        else:
            block.append("The Code has 593 articles (582-593 added by ZRU-1150 of 11.06.2026). This article does not exist.")
        pairs=sorted(zip(codes,RUNS))
        for c,r in pairs:
            key[f"{q['id']}|{c}"]=r
            block.append(f"[{c}] {ans[(r,q['id'])]}")
        out.append("\n".join(block))
    open(f"regrade/packet_{part+1}.md","w",encoding="utf-8").write("\n\n".join(out))
json.dump(key,open("regrade/blind_key.json","w"),indent=0)
print("ok",len(key))
