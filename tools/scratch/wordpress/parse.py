"""Parse the content tables of a phpMyAdmin dump into SQLite.

usage: parse.py DUMP.sql WORK/wp.db
Reads only the tables in KEEP: the dump also holds accounts, password hashes
and private messages, which must never enter the repository.
"""
import re, sqlite3, sys
src, dst = sys.argv[1], sys.argv[2]
KEEP = {'wp_posts','wp_postmeta','wp_terms','wp_term_taxonomy','wp_term_relationships'}
ESC = {'n':'\n','r':'\r','t':'\t','0':'\0','\\':'\\',"'":"'",'"':'"','Z':'\x1a','b':'\b'}
def rows(s, i):
    n=len(s)
    while i<n:
        while s[i] in ' \n\r,': i+=1
        if s[i]==';': return
        assert s[i]=='(', s[i:i+50]
        i+=1; row=[]
        while True:
            while s[i]==' ': i+=1
            if s[i]=="'":
                i+=1; buf=[]
                while True:
                    j=s.find("'",i); k=s.find('\\',i)
                    if k!=-1 and k<j: buf.append(s[i:k]); buf.append(ESC.get(s[k+1],s[k+1])); i=k+2
                    elif s[j+1:j+2]=="'": buf.append(s[i:j]+"'"); i=j+2
                    else: buf.append(s[i:j]); i=j+1; break
                row.append(''.join(buf))
            else:
                m=re.compile(r"[^,)]*").match(s,i); v=m.group().strip(); i=m.end()
                row.append(None if v=='NULL' else (int(v) if re.fullmatch(r'-?\d+',v) else v))
            while s[i]==' ': i+=1
            if s[i]==',': i+=1; continue
            if s[i]==')': i+=1; yield row; break
s=open(src,encoding='utf-8').read()
db=sqlite3.connect(dst)
for m in re.finditer(r"^INSERT INTO `(\w+)` \(([^)]*)\) VALUES\n", s, re.M):
    t=m.group(1)
    if t not in KEEP: continue
    cols=[c.strip(' `') for c in m.group(2).split(',')]
    db.execute(f"CREATE TABLE IF NOT EXISTS {t} ({','.join(cols)})")
    db.executemany(f"INSERT INTO {t} VALUES ({','.join('?'*len(cols))})", rows(s,m.end()))
db.commit()
for t in KEEP: print(t, db.execute(f"select count(*) from {t}").fetchone()[0])
