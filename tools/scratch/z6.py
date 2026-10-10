"""z6.py PDF PAGE x0 y0 x1 y1 out : crop a 600 dpi render using 200 dpi coordinates.

Renders are cached in $VEC_CACHE (default: <tmpdir>/vec-rescue/r600).
"""
import sys,subprocess,os,tempfile
from PIL import Image
pdf,pg,x0,y0,x1,y1,out=sys.argv[1:8]
C=os.path.join(os.environ.get('VEC_CACHE',os.path.join(tempfile.gettempdir(),'vec-rescue')),'r600')
os.makedirs(C,exist_ok=True)
key=os.path.basename(pdf)[:16].replace('.','_')
f=f'{C}/{key}-{int(pg):03d}.png'
if not os.path.exists(f): subprocess.run(['pdftoppm','-r','600','-png','-gray','-f',pg,'-l',pg,'-singlefile',pdf,f[:-4]])
im=Image.open(f); k=3
im.crop((int(x0)*k,int(y0)*k,int(x1)*k,int(y1)*k)).save(out)
