from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import math,io,cairosvg
P=Path(__file__).resolve().parent; A=P/'assets/animations'; W,H=480,320
I='#303936'; S='#f4d8b8'; T='#aecb91'; L='#596061'; C='#a6adaa'; B='#48a7c8'
def art(kind,t):
 q=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 320"><rect width="480" height="320" fill="white"/>']
 def path(d,c):q.append(f'<path d="{d}" fill="{c}" stroke="{I}" stroke-width="1.7" stroke-linejoin="round"/>')
 def rect(x,y,w,h,c,r=4):q.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}" stroke="{I}" stroke-width="1.7"/>')
 def ell(x,y,rx,ry,c):q.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" stroke="{I}" stroke-width="1.5"/>')
 def line(a,b,c,w=2):q.append(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>')
 def seg(a,b,r1,r2,c):
  dx,dy=b[0]-a[0],b[1]-a[1];n=math.hypot(dx,dy) or 1; x,y=-dy/n,dx/n
  def p(a,r):return f'{a[0]+x*r} {a[1]+y*r}'
  path(f'M{p(a,r1)} L{p(b,r2)} Q{b[0]+dx/n*r2} {b[1]+dy/n*r2} {p(b,-r2)} L{p(a,-r1)} Q{a[0]-dx/n*r1} {a[1]-dy/n*r1} {p(a,r1)} Z',c)
 def chain(a,b,c,r1,r2,r3,col):seg(a,b,r1,r2,col);seg(b,c,r2,r3,col)
 def hand(a):ell(*a,7,9,S);line((a[0]-3,a[1]+3),(a[0]+3,a[1]+3),'#b38f76',1)
 def dumb(a):
  x,y=a;rect(x-17,y-3,34,6,'#717d7c',2);rect(x-20,y-8,9,16,B,3);rect(x+11,y-8,9,16,B,3);hand(a)
 def shoe(a,ang=0,front=False):
  q.append(f'<g transform="translate({a[0]} {a[1]}) rotate({ang})">')
  path('M-11 -9 Q-14 5 -10 10 L10 10 Q15 5 9 -9 Z' if front else 'M-10 -9 L8 -9 Q13 -2 24 0 Q32 1 33 7 L30 10 L-11 10 Q-14 5 -10 -9 Z','#fff');line((-9,5),(10 if front else 29,5),'#b4bdb8',1);q.append('</g>')
 def head(x,y,side=False):
  rect(x-8,y+20,16,20,S,5)
  if side:path(f'M{x-19} {y-5} Q{x-20} {y-30} {x} {y-30} Q{x+20} {y-29} {x+21} {y-5} L{x+25} {y+5} L{x+20} {y+9} Q{x+20} {y+23} {x+6} {y+26} Q{x-18} {y+23} {x-19} {y-5} Z',S)
  else:ell(x-19,y,4,7,S);ell(x+19,y,4,7,S);ell(x,y-2,19,28,S)
 line((65,300),(415,300),'#e1e7e2')
 if kind in ('curl','external','lateral_front'):
  rect(177,112,126,115,C,8);rect(174,217,132,13,C);rect(178,229,8,67,C);rect(294,229,8,67,C)
  for z in [-1,1]:
   x=240+z*30;path(f'M{x-22} 191 Q{x-25} 210 {x-19} 228 L{x-14} 284 Q{x} 290 {x+13} 284 L{x+19} 228 Q{x+24} 210 {x+19} 191 Z',L);shoe((x,287),front=True)
  head(240,52);path('M224 82 Q240 93 256 82 L276 90 Q287 97 291 118 L272 126 L273 191 Q240 200 207 191 L208 126 L189 118 Q193 97 204 90 Z',T)
  for z in [-1,1]:
   sh=(240+z*43,118);el=(240+z*49,166)
   if kind=='curl':ha=(el[0]+z*(5+9*math.sin(math.pi*t)),el[1]+44*math.cos(math.pi*t))
   elif kind=='external':ha=(240+z*(23+58*t),159-2*t)
   else:
    a=math.radians(82-47*t);el=(sh[0]+z*math.cos(a)*43,sh[1]+math.sin(a)*43);ha=(el[0]+z*math.cos(a+.12)*38,el[1]+math.sin(a+.12)*38)
   chain(sh,el,ha,10,8,5.5,S);dumb(ha) if kind=='curl' else hand(ha)
   if kind=='external':
    if z==-1:lh=ha
    else:line(lh,ha,'#d5a943',5);hand(lh);hand(ha)
 elif kind=='slide':
  rect(54,239,372,17,C,5);rect(66,256,9,43,C);rect(405,256,9,43,C);rect(65,217,69,22,'#e3eae2',7)
  q.append('<g transform="translate(108 213) rotate(-90)">');head(0,0,True);q.append('</g>');path('M132 197 Q157 189 186 197 L233 200 L243 234 L137 236 Q128 226 132 197 Z',T)
  chain((236,219),(313,225),(389,225),17,13,8,'#777f80');shoe((391,226),-75)
  hip=(235,219);a=(389-87*t,229);dx=a[0]-hip[0];dy=a[1]-hip[1];dist=math.hypot(dx,dy);h=math.sqrt(max(0,78**2-(dist/2)**2));k=((hip[0]+a[0])/2+dy/dist*h,(hip[1]+a[1])/2-dx/dist*h)
  chain(hip,k,a,18,14,9,L);shoe(a,-75+45*t);chain((153,211),(195,222),(233,223),9,7,5,S);hand((233,223))
 else:
  rect(142,103,12,116,C);rect(146,215,125,14,C);rect(152,229,8,67,C);rect(260,229,8,67,C)
  head(182,52,True);path('M171 82 L193 82 Q212 91 215 113 L209 137 L207 202 Q184 214 155 200 L157 115 Q157 94 171 82 Z',T)
  chain((182,207),(250,220),(250,288),17,13,9,'#777f80');shoe((250,288));hip=(186,207);k=(266,220);a=(266,287);rot=0
  if kind=='knee':ang=math.radians(90-66*t);a=(k[0]+67*math.cos(ang),k[1]+67*math.sin(ang));rot=-45*t
  if kind=='heel':rot=24*t;theta=math.radians(rot);a=(297-31*math.cos(theta),287-31*math.sin(theta));k=(266,220-4*t)
  if kind=='toe':rot=-22*t
  chain(hip,k,a,18,14,9,L);shoe(a,rot)
  if kind=='wrist':
   rect(208,165,98,11,C);rect(292,176,8,120,C);el=(208,155);wr=(289,156);chain((188,118),el,wr,10,8,5.5,S);ang=math.radians(18-43*t);ha=(wr[0]+19*math.cos(ang),wr[1]+19*math.sin(ang));seg(wr,ha,5.5,5,S);dumb(ha)
  else:chain((188,118),(195,164),(234,202),10,8,5.5,S);hand((234,202))
 q.append('</svg>');return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=''.join(q).encode(),output_width=W*2,output_height=H*2))).convert('RGB').resize((W,H),Image.Resampling.LANCZOS)
DATA=[('curl','手臂弯举','轻水瓶；肘贴身'),('external','肩外旋','空手或轻弹力带'),('lateral_front','低位侧抬','空手优先；不高于肩'),('knee','单腿伸膝','左右各8次；不痛范围'),('slide','仰卧脚跟滑动','左右各8次；脚跟贴床'),('heel','坐姿提踵','前脚掌贴地'),('toe','坐姿抬脚尖','脚跟贴地'),('wrist','支撑式腕屈伸','前臂放桌面；轻水瓶')]
for key,_,_ in DATA:
 frames=[]
 for i in range(25):
  p=i/5;t=p/2 if p<2 else (5-p)/3;frames.append(art(key,(1-math.cos(math.pi*t))/2))
 sheet=Image.new('RGB',(W*5,H*5),'white')
 for i,f in enumerate(frames):sheet.paste(f,(i%5*W,i//5*H))
 sheet.save(A/f'{key}.sheet.png',optimize=True);frames[0].save(A/f'{key}.gif',save_all=True,append_images=frames[1:],duration=200,loop=0,optimize=True);frames[0].save(A/f'{key}.png');frames[10].save(A/f'{key}.end.png')
F='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc';FB='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def font(n,b=False):return ImageFont.truetype(FB if b else F,n,index=2)
im=Image.new('RGB',(1600,2264),'white');d=ImageDraw.Draw(im)
def txt(x,y,s,n=34,b=False,c=I):d.text((x,y),s,font=font(n,b),fill=c)
txt(65,42,'每日20分钟 · 四肢轻量训练',64,True);txt(69,126,'居家轻量运动参考｜有健康限制请先咨询专业人员',34,False,'#356b60');txt(69,180,'热身3分钟 · 动作及休息14分钟 · 放松3分钟',36,True);txt(69,232,'周一 / 三 / 五 A/B交替；其他日舒缓活动或休息。',31)
for i,(key,name,note) in enumerate(DATA):
 x=60+i%2*750;y=300+i//2*375;d.rounded_rectangle((x,y,x+730,y+355),radius=20,fill='#f6f9f6',outline='#c8d9ce',width=3);txt(x+20,y+12,f'{i+1:02d}  {name}',40,True);txt(x+20,y+65,note,28)
 for j,suffix in enumerate(['','.end']):
  pic=Image.open(A/f'{key}{suffix}.png').resize((315,210));im.paste(pic,(x+15+j*385,y+110));txt(x+103+j*385,y+318,'起始' if j==0 else '呼气用力',25,False,'#356b60')
 d.line((x+333,y+216,x+390,y+216),fill='#669d62',width=6);d.polygon([(x+390,y+216),(x+371,y+203),(x+371,y+229)],fill='#669d62')
txt(68,1820,'先1组、每动作8次；用力2秒，还原3秒。',36,True);txt(68,1874,'轻水瓶250–500克起步；1kg仅经专业允许且适应后用于部分动作。',30);txt(68,1924,'背靠椅背，不憋气、不向下使劲；关节不适时减小幅度。',30)
d.rounded_rectangle((60,1990,1540,2200),radius=20,fill='#fff2ed',outline='#dfb0a3',width=3);txt(84,2007,'不适即停，不强求完成',42,True,'#8c4334');txt(84,2070,'疼痛或其他不适加重：停止；持续或明显加重请就医。',32,False,'#743f35');txt(84,2125,'严重症状及时就医。示意图仅供一般参考，非个体医疗处方。',30,False,'#743f35')
im.save(P/'printable/training.png');im.save(P/'printable/training.pdf',resolution=193.5)
