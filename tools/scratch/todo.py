"""todo.py v10n2 : list stub articles of an issue that need a scan transcription (twins of online records excluded)."""
import sys,os,yaml
iss=sys.argv[1]
d=yaml.safe_load(open(f'transcriptions/contents/{iss}.yaml'))
print(d['source'])
def state(v):
    if os.path.exists(f'transcriptions/art{v}.md'): return 'T'
    h=f'build/site/art{v}/index.html'
    if not os.path.exists(h): return 'NOPAGE'
    return 'STUB' if 'not yet online' in open(h).read() else 'ONLINE'
for it in d['items']:
    v=it.get('vid')
    if not v: continue
    vs=v if isinstance(v,list) else [v]
    ss=[state(x) for x in vs]
    if 'ONLINE' in ss or 'T' in ss:
        continue
    for x,s in zip(vs,ss):
        print(x,s,it.get('page'),'|',it.get('title'),'|',it.get('author'),'|',it.get('note',''))
