def disp(x):
    if isinstance(x,int): return [str(x)]
    if isinstance(x,str):
        w=len(x); return ['┌→'+'─'*(w-1)+'┐','│'+x+'│','└'+'─'*w+'┘']
    cells=[disp(e) for e in x]
    h=max(len(c) for c in cells)
    cols=[]
    for c in cells:
        w=max(len(l) for l in c)
        if len(c)==1:
            t=[' '*w]*h; t[h//2]=c[0].ljust(w); c=t
        else:
            c=[l.ljust(w) for l in c]+[' '*w]*(h-len(c))
        cols.append(c)
    rows=[' '.join(c[i] for c in cols)+' ' for i in range(h)]
    w=len(rows[0])
    nested=any(not isinstance(e,int) for e in x)
    return ['┌→'+'─'*(w-1)+'┐']+['│'+r+'│' for r in rows]+['└'+('∊' if nested else '─')+'─'*(w-1)+'┘']
