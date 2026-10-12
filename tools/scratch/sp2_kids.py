"""Second Pass (#305): adds children and page-unknown lines to $S/sp2/work.json; run once after sp2_worklist.py."""
import json,yaml,collections,os
S=os.environ['S']
d=json.load(open(S+'/sp2/work.json'))
# add the 11 page-unknown lines
for r in d['nopage']:
    items=yaml.safe_load(open(f"transcriptions/contents/{r['stem']}.yaml"))['items']
    it=items[r['idx']]; ind=it.get('indent',0)
    nxt=items[r['idx']+1] if r['idx']+1<len(items) else {}
    if nxt.get('indent',0)>ind: continue
    prev=[i.get('page') for i in items[:r['idx']] if str(i.get('page','')).isdigit()]
    after=[i.get('page') for i in items[r['idx']+1:] if str(i.get('page','')).isdigit()]
    r['page_between']=[prev[-1] if prev else None, after[0] if after else None]
    r['next_page']=None; d['work'].append(r)
c=collections.Counter()
for r in d['work']:
    items=yaml.safe_load(open(f"transcriptions/contents/{r['stem']}.yaml"))['items']
    it=items[r['idx']]; ind=it.get('indent',0); kids=[]
    for j in items[r['idx']+1:]:
        if j.get('indent',0)<=ind: break
        kids.append({k:j.get(k) for k in ('title','page','file','vid')})
    r['children']=kids
    if kids: c['with children']+=1
    if kids and all(k['file'] or k['vid'] for k in kids): c['all children texted']+=1
print(c, len(d['work']))
json.dump(d,open(S+'/sp2/work.json','w'),ensure_ascii=False,indent=1)
