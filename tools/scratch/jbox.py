import sys
def box(items):
    # items: list of str or nested lists; returns list of lines
    cells=[]
    for it in items:
        cells.append(box(it) if isinstance(it,list) else [it])
    h=max(len(c) for c in cells)
    ws=[max(len(l) for l in c) for c in cells]
    out=['┌'+'┬'.join('─'*w for w in ws)+'┐']
    for i in range(h):
        out.append('│'+'│'.join((c[i] if i<len(c) else '').ljust(w) for c,w in zip(cells,ws))+'│')
    out.append('└'+'┴'.join('─'*w for w in ws)+'┘')
    return out
p=[['#','~'],['1:','=',['#','@','q:']]]
t0=[['+','/'],'@',['1:','=',['+.','i.']]]
t3=['*',[[['-.','@','%'],'@','~.'],'&.','q:']]
for n,x in (('p',p),('t0',t0),('t3',t3)):
    print(n); print('\n'.join(box(x)))
