import json,collections,os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
MODELS=[("chatgpt","ChatGPT"),("gemini","Gemini"),("claude","Claude"),("deepseek","DeepSeek")]
GOOD={"correct","premise_corrected","correct_refusal"}
def load(p):
    return [json.loads(l) for l in open(p,encoding="utf-8")] if os.path.exists(p) else None
rows=[]
for key,name in MODELS:
    for lang,prefix in (("RU",""),("UZ","uz_")):
        g=load(f"results/graded_{prefix}{key}.jsonl")
        if not g: continue
        c=collections.Counter(x["label"] for x in g)
        cit=[x["citation_ok"] for x in g if x["citation_ok"] is not None]
        bytype={t:sum(1 for x in g if x["type"]==t and x["label"] in GOOD) for t in ("fact","false_premise","nonexistent_article")}
        rows.append(dict(model=name,lang=lang,good=sum(c[l] for l in GOOD),partial=c["partially_correct"],
            wrong=c["wrong"],bad=c["hallucinated"]+c["premise_accepted"],
            cit=f"{sum(cit)}/{len(cit)}" if cit else "none",fact=bytype["fact"],fp=bytype["false_premise"],ne=bytype["nonexistent_article"]))
json.dump(rows,open("results/summary.json","w"),indent=1,ensure_ascii=False)
for r in rows: print(r)
# chart 1: fully right RU vs UZ
fig,ax=plt.subplots(figsize=(8.5,4.2))
names=[n for _,n in MODELS]; w=0.38
ru=[next((r["good"] for r in rows if r["model"]==n and r["lang"]=="RU"),0) for n in names]
uz=[next((r["good"] for r in rows if r["model"]==n and r["lang"]=="UZ"),0) for n in names]
x=range(len(names))
b1=ax.bar([i-w/2 for i in x],ru,w,label="Russian",color="#3b6ea5")
b2=ax.bar([i+w/2 for i in x],uz,w,label="Uzbek (Latin)",color="#d9822b")
ax.bar_label(b1); ax.bar_label(b2)
ax.set_xticks(list(x)); ax.set_xticklabels(names); ax.set_ylim(0,105)
ax.set_ylabel("Fully correct answers (of 100)"); ax.set_title("UzLaw-Eval v1: same 100 questions, two languages")
ax.legend(frameon=False); ax.spines[["top","right"]].set_visible(False)
plt.tight_layout(); plt.savefig("results/chart_ru_vs_uz.png",dpi=160)
# chart 2: false premise handling
fig,ax=plt.subplots(figsize=(8.5,4.2))
fr=[next((r["fp"] for r in rows if r["model"]==n and r["lang"]=="RU"),0) for n in names]
fu=[next((r["fp"] for r in rows if r["model"]==n and r["lang"]=="UZ"),0) for n in names]
b1=ax.bar([i-w/2 for i in x],fr,w,label="Russian",color="#3b6ea5"); b2=ax.bar([i+w/2 for i in x],fu,w,label="Uzbek (Latin)",color="#d9822b")
ax.bar_label(b1); ax.bar_label(b2)
ax.set_xticks(list(x)); ax.set_xticklabels(names); ax.set_ylim(0,16)
ax.set_ylabel("False premises corrected (of 15)"); ax.set_title("Does the model push back on a wrong assumption?")
ax.legend(frameon=False); ax.spines[["top","right"]].set_visible(False)
plt.tight_layout(); plt.savefig("results/chart_false_premise.png",dpi=160)
