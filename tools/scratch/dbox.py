# DISP-style boxes: cell = str | list of lines | ('row', [cells]) | ('grid', [[cells]])
def lines(c):
    if isinstance(c,str): return [c]
    if isinstance(c,tuple) and c[0]=='row': return grid([c[1]])
    if isinstance(c,tuple) and c[0]=='grid': return grid(c[1])
    return c
def grid(rows):
    R=[[lines(c) for c in r] for r in rows]
    nc=len(R[0])
    W=[max(max(len(l) for l in R[i][j]) for i in range(len(R))) for j in range(nc)]
    H=[max(len(c) for c in r) for r in R]
    out=['┌'+'┬'.join('─'*w for w in W)+'┐']
    for i,r in enumerate(R):
        for k in range(H[i]):
            out.append('│'+'│'.join((r[j][k] if k<len(r[j]) else '').ljust(W[j]) for j in range(nc))+'│')
        out.append(('├'+'┼'.join('─'*w for w in W)+'┤') if i<len(R)-1 else '└'+'┴'.join('─'*w for w in W)+'┘')
    return out
def row(*cells): return '\n'.join(grid([list(cells)]))
def g(rows): return '\n'.join(grid(rows))
