"""Score each post against the held texts: share of its 5-word shingles found in the best-matching text.

usage: match.py WORK (run from the project root after `make all`); writes WORK/match.json
"""
import json,sqlite3,re,html,glob,os,sys
S=sys.argv[1]
def words(t):
    t=html.unescape(re.sub(r'<[^>]+>|<!--.*?-->',' ',t,flags=re.S)).lower()
    return re.findall(r'[a-z]{2,}',t)
def sh(w): return {' '.join(w[i:i+5]) for i in range(len(w)-4)}
docs={}
for f in glob.glob('build/docs/art*/index.md')+glob.glob('transcriptions/**/*.md',recursive=True):
    k=os.path.basename(os.path.dirname(f)) if f.endswith('index.md') else os.path.basename(f)[:-3]
    docs.setdefault(k,set()).update(sh(words(open(f,errors='replace').read())))
inv={r['id']:r for r in json.load(open('build/inventory.json'))}
db=sqlite3.connect(S+'/wp.db')
out=[]
for id,t,c in db.execute("select ID,post_title,post_content from wp_posts where post_type in('post','page') and post_status!='trash'"):
    s=sh(words(c))
    if len(s)<20: out.append((id,len(s),None,0)); continue
    best=max(docs,key=lambda k:len(s&docs[k]))
    out.append((id,len(s),best,len(s&docs[best])/len(s)))
json.dump(out,open(S+'/match.json','w'))
