import json,re,glob,sys
qmap=json.load(open('prompts/qmap.json'))
rows={json.loads(l)['id']:json.loads(l) for l in open('data/questions_v1.jsonl',encoding='utf-8')}
def collect(rawdir, out, label, lang):
    ans={}
    for f in sorted(glob.glob(f'{rawdir}/*.txt')):
        t=open(f,encoding='utf-8').read().replace('**','')
        for x in re.finditer(r'(Q\d{3})\s*[:.]\s*(.*?)(?=\n\s*Q\d{3}\s*[:.]|\n\s*ChatGPT может|\n\s*Modda raqamlarini|\Z)',t,re.S):
            if x.group(1) not in ans: ans[x.group(1)]=x.group(2).strip()
    with open(out,'w',encoding='utf-8') as f:
        for q,i in qmap.items():
            r=rows[i]
            f.write(json.dumps(dict(qid=q,id=i,type=r['type'],article=r['article'],lang=lang,
              question=r['question_uz_latn'] if lang=='uz' else r['question_ru'],question_ru=r['question_ru'],
              answer_ref=r['answer_ru'],key_facts=r['key_facts'],model=label,answer=ans.get(q,"")),ensure_ascii=False)+'\n')
    return len(ans), sorted(set(qmap)-set(ans))
if __name__=="__main__":
    print(collect(*sys.argv[1:5]))
