"""shot2.py PDF PAGE x0 y0 x1 y1 out.jpg : crop a 300 dpi greyscale render using 200 dpi coordinates.

For figures kept as images in transcriptions. Renders are cached in
$VEC_CACHE/r300; set VEC_CACHE to the session scratchpad.
"""
import sys,subprocess,os
from PIL import Image
pdf,pg,x0,y0,x1,y1,out=sys.argv[1:8]
if 'VEC_CACHE' not in os.environ: sys.exit('Set VEC_CACHE to the session scratchpad')
C=os.path.join(os.environ['VEC_CACHE'],'r300')
os.makedirs(C,exist_ok=True)
f=f'{C}/'+os.path.basename(pdf)[:16].replace('.','_')+f'-{int(pg):03d}.png'
if not os.path.exists(f): subprocess.run(['pdftoppm','-r','300','-png','-f',pg,'-l',pg,'-singlefile',pdf,f[:-4]])
im=Image.open(f).convert('L'); k=1.5
im.crop((int(int(x0)*k),int(int(y0)*k),int(int(x1)*k),int(int(y1)*k))).save(out,quality=82)
