"""Crop only the unused white margins from each original 5x5 sheet.
Requires Pillow; not needed for Pages deployment. Run from any directory.
All 25 frames use an identical crop, so frame coordinates remain stable.
"""
from pathlib import Path
from PIL import Image
base=Path(__file__).parent/'assets'/'animations'
boxes={'curl':(115,8,365,308),'external':(115,8,365,308),'lateral_front':(115,8,365,308),'knee':(119,8,369,308),'heel':(95,8,345,308),'toe':(95,8,345,308),'wrist':(110,8,360,308),'slide':(40,130,440,310)}
for name,box in boxes.items():
    sheet=Image.open(base/(name+'.sheet.png')).convert('RGB')
    assert sheet.size==(2400,1600), (name,sheet.size)
    x,y,r,b=box; w,h=r-x,b-y
    out=Image.new('RGB',(5*w,5*h),'white')
    for i in range(25):
        dx,dy=i%5,i//5
        out.paste(sheet.crop((dx*480+x,dy*320+y,dx*480+r,dy*320+b)),(dx*w,dy*h))
    out.save(base/(name+'.player.png'),optimize=True)
