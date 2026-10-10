def vec(s):
    return ['┌→'+'─'*(len(s)-1)+'┐','│'+s+'│','└'+'─'*len(s)+'┘']
def cmat(rows,empty_mark=None):
    if not rows:
        m=empty_mark or '⊖'
        return ['┌'+m+'┐','│ │','└─┘']
    w=max(len(r) for r in rows)
    out=['┌→'+'─'*(w-1)+'┐']
    for i,r in enumerate(rows):
        out.append(('↓' if i==0 else '│')+r.ljust(w)+'│')
    out.append('└'+'─'*w+'┘')
    return out
def mat(cells):
    nc=len(cells[0])
    W=[max(max(len(l) for l in r[j]) for r in cells) for j in range(nc)]
    body=[]
    for r in cells:
        h=max(len(c) for c in r)
        for k in range(h):
            body.append(' '.join((r[j][k] if k<len(r[j]) else '').ljust(W[j]) for j in range(nc))+' ')
    w=len(body[0])
    out=['┌→'+'─'*(w-1)+'┐']
    for i,b in enumerate(body): out.append(('↓' if i==0 else '│')+b+'│')
    out.append('└∊'+'─'*(w-1)+'┘')
    return '\n'.join(out)
