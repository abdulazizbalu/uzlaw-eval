import json,collections
key=json.load(open("regrade/blind_key.json"));ov=json.load(open("regrade/overrides.json"))
qmap=json.load(open("prompts/qmap.json")); inv={v:k for k,v in qmap.items()}
Q={json.loads(l)["id"]:json.loads(l) for l in open("data/questions_v1.jsonl",encoding="utf-8")}
out=collections.defaultdict(list); seen=set()
for p in range(1,5):
    for l in open(f"regrade/graded_part_{p}.jsonl",encoding="utf-8"):
        x=json.loads(l); k=f"{x['id']}|{x['code']}"; assert k not in seen; seen.add(k)
        if k in ov: x["label"],x["reason"]=ov[k][0],ov[k][1]+" (ручная правка)"
        t=Q[x["id"]]["type"]
        if t=="nonexistent_article": x["citation_ok"]=None
        out[key[k]].append({"qid":inv[x["id"]],"id":x["id"],"type":t,"label":x["label"],"citation_ok":x["citation_ok"],"reason":x["reason"]})
assert len(seen)==800
for r,rows in out.items():
    rows.sort(key=lambda z:z["qid"]); assert len(rows)==100
    with open(f"results/graded_{r}.jsonl","w",encoding="utf-8") as f:
        for z in rows: f.write(json.dumps(z,ensure_ascii=False)+"\n")
print("ok")
