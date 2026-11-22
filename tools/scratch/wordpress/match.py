"""Score each post against the held texts: share of its 5-word shingles found in the best-matching text.

usage: match.py WORK (run from the project root after `make all`); writes WORK/match.json
"""
import json,sqlite3,re,html,glob,os,sys
S=sys.argv[1]
TAGS=r'</?(?:a|img|figure|figcaption|span|sup|sub|br|div|p|em|strong|code|pre|table|tr|td|th|tbody|thead|ul|ol|li|h[1-6]|blockquote)\b[^>]*>'
def words(t, post=False):
    # Posts: strip all tags (their code is entity-escaped). Held Markdown: only
    # known tags, as APL and J code is full of < (#328: `<[^>]+>` ate code).
    t=re.sub(r'<!--.*?-->|'+(r'<[^>]+>' if post else TAGS),' ',t,flags=re.S|re.I)
    return re.findall(r'[a-z]{2,}',html.unescape(t).lower())
def sh(w): return {' '.join(w[i:i+5]) for i in range(len(w)-4)}
docs={}
for f in glob.glob('build/docs/art*/index.md')+glob.glob('transcriptions/**/*.md',recursive=True):
    k=os.path.basename(os.path.dirname(f)) if f.endswith('index.md') else os.path.basename(f)[:-3]
    docs.setdefault(k,set()).update(sh(words(open(f,errors='replace').read())))
inv={r['id']:r for r in json.load(open('build/inventory.json'))}
db=sqlite3.connect(S+'/wp.db')
out=[]
for id,t,c in db.execute("select ID,post_title,post_content from wp_posts where post_type in('post','page') and post_status!='trash'"):
    s=sh(words(c,post=True))
    if len(s)<20: out.append((id,len(s),None,0)); continue
    best=max(docs,key=lambda k:len(s&docs[k]))
    out.append((id,len(s),best,len(s&docs[best])/len(s)))
json.dump(out,open(S+'/match.json','w'))
