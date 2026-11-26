from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
P=Path(__file__).resolve().parent
F='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; FB='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def font(n,b=False): return ImageFont.truetype(FB if b else F,n,index=2)
BG='#f3f7f5'; INK='#263b40'; SK='#dfac90'; TOP='#508b80'; PANTS='#55697c'; CH='#a9b9b4'; SHO='#34474d'; WEIGHT='#6d8794'
def art(kind,t=0):
 im=Image.new('RGB',(480,300),BG); d=ImageDraw.Draw(im)
 def line(p,c,w):
  d.line(p,fill=c,width=w,joint='curve'); r=w/2
  for x,y in [p[0],p[-1]]: d.ellipse((x-r,y-r,x+r,y+r),fill=c)
 def limb(p,c,w=17): line(p,INK,w+4);line(p,c,w)
 def head(x,y):
  d.ellipse((x-24,y-28,x+24,y+25),fill=SK,outline=INK,width=2);d.pieslice((x-26,y-32,x+25,y+22),175,365,fill='#a4a7a4');d.ellipse((x+10,y-3,x+13,y),fill=INK)
 def bottle(x,y): d.rounded_rectangle((x-8,y-18,x+8,y+18),radius=5,fill='#b8dce3',outline=INK,width=2);d.rectangle((x-5,y-22,x+5,y-17),fill=WEIGHT)
 def shoe(a,b): limb([a,b],SHO,13)
 def ground(): d.line((54,266,426,266),fill='#c3ceca',width=2)
 ground()
 if kind in ('curl','lateral','knee','heel','toe','wrist'):
  # side view: seated upright with backrest, feet pointing right
  d.rounded_rectangle((135,88,151,196),radius=5,fill=CH,outline=INK,width=2);d.rounded_rectangle((141,190,273,207),radius=5,fill=CH,outline=INK,width=2)
  line([(151,205),(151,263)],CH,10);line([(262,205),(262,263)],CH,10)
  head(185,61);limb([(185,88),(181,173)],TOP,44)
  # far leg remains supported
  limb([(186,180),(250,193),(250,251)],'#718294',20);shoe((250,253),(279,254))
  hip=(190,183); knee=(267,194)
  if kind=='knee':
   angle=math.radians(90-70*t); ankle=(knee[0]+65*math.cos(angle),knee[1]+65*math.sin(angle));foot=(ankle[0]+28,ankle[1]+3)
  elif kind=='heel': ankle=(267-8*t,251-22*t);foot=(296,255)
  elif kind=='toe': ankle=(267,251);foot=(296,255-23*t)
  else: ankle=(267,251);foot=(296,255)
  limb([hip,knee,ankle],PANTS,23);shoe(ankle,foot)
  shoulder=(184,106);elbow=(196,155)
  if kind=='curl':
   a=math.radians(70-150*t); hand=(elbow[0]+51*math.cos(a),elbow[1]+51*math.sin(a));limb([shoulder,elbow,hand],SK,15);bottle(*hand)
  elif kind=='wrist':
   d.rounded_rectangle((212,164,353,174),radius=4,fill=CH,outline=INK,width=2);line([(343,174),(343,263)],CH,9);elbow=(210,156);wr=(272,156);a=math.radians(18-38*t);hand=(wr[0]+24*math.cos(a),wr[1]+24*math.sin(a));limb([shoulder,elbow,wr,hand],SK,14);bottle(*hand)
  else: limb([shoulder,(197,154),(238,180)],SK,15)
 elif kind in ('external','lateral_front'):
  d.rounded_rectangle((170,88,310,205),radius=12,fill=CH,outline=INK,width=2);d.rounded_rectangle((158,190,322,208),radius=6,fill=CH,outline=INK,width=2)
  line([(171,207),(171,263)],CH,10);line([(309,207),(309,263)],CH,10)
  head(240,60);d.rounded_rectangle((199,91,281,188),radius=24,fill=TOP,outline=INK,width=2)
  for s in [-1,1]:
   h=(240+s*25,183);k=(240+s*40,207);a=(240+s*40,251);limb([h,k,a],PANTS,25);shoe(a,(a[0]+s*10,257))
  hands=[]
  for s in [-1,1]:
   sh=(240+s*42,108)
   if kind=='external': el=(240+s*47,153);hand=(240+s*(14+72*t),151-4*t)
   else: el=(sh[0]+s*(10+37*t),sh[1]+43-17*t);hand=(el[0]+s*(4+40*t),el[1]+39-22*t)
   limb([sh,el,hand],SK,15);hands.append(hand)
   if kind=='lateral_front':bottle(*hand)
  if kind=='external':line(hands,'#d4a541',5)
 elif kind=='slide':
  d.rounded_rectangle((65,205,420,225),radius=6,fill=CH,outline=INK,width=2);line([(75,225),(75,265)],CH,10);line([(410,225),(410,265)],CH,10)
  d.rounded_rectangle((75,180,143,205),radius=9,fill='#dce5e1');head(121,176);limb([(153,187),(239,189)],TOP,37);limb([(162,180),(206,193),(237,195)],SK,14)
  limb([(237,193),(312,194),(383,194)],'#718294',18);shoe((383,194),(398,187))
  # heel stays on bed, knee rises with flexion
  a=(382-82*t,195);k=(310-40*t,193-58*t);limb([(235,191),k,a],PANTS,22);shoe(a,(a[0]+15,a[1]-8))
 return im
DATA=[('curl','手臂弯举','轻水瓶；肘贴身'),('external','肩外旋','空手或轻弹力带'),('lateral_front','低位侧抬','空手优先；不高于肩'),('knee','单腿伸膝','左右各8次；不痛范围'),('slide','仰卧脚跟滑动','左右各8次；脚跟贴床'),('heel','坐姿提踵','前脚掌贴地'),('toe','坐姿抬脚尖','脚跟贴地'),('wrist','支撑式腕屈伸','前臂放桌面；轻水瓶')]
for key,name,note in DATA:
 frames=[]
 for i in range(25):
  p=i/25*5;t=(p/2 if p<2 else (5-p)/3); t=(1-math.cos(math.pi*t))/2
  im=art(key,t);d=ImageDraw.Draw(im);d.text((16,10),'呼气 · 慢慢用力' if p<2 else '吸气 · 缓慢还原',font=font(19,True),fill='#285b50');frames.append(im)
 frames[0].save(P/'assets/animations'/f'{key}.gif',save_all=True,append_images=frames[1:],duration=200,loop=0,optimize=True)
 art(key,0).save(P/'assets/animations'/f'{key}.png')
# A4 poster with two poses per cell
im=Image.new('RGB',(1600,2264),'#ffffff');d=ImageDraw.Draw(im)
def txt(x,y,s,n=34,b=False,c=INK):d.text((x,y),s,font=font(n,b),fill=c)
txt(70,48,'每日20分钟 · 四肢轻量训练',66,True);txt(73,132,'恢复期参考  |  经妇科或盆底康复专业评估允许后练习',35,False,'#356b60')
txt(73,196,'热身3分钟  ·  动作与休息约14分钟  ·  放松3分钟',37,True)
txt(73,252,'周一 / 三 / 五抗阻（A/B交替）；其余日轻活动，身体不适可休息。',30)
for i,(key,name,note) in enumerate(DATA):
 x=65+(i%2)*745;y=325+(i//2)*373
 d.rounded_rectangle((x,y,x+720,y+350),radius=22,fill=BG,outline='#d3e1db',width=3)
 txt(x+21,y+12,f'{i+1:02d}  {name}',41,True);txt(x+22,y+65,note,28)
 for j,t in enumerate([0,1]):
  pic=art(key,t).resize((310,194));im.paste(pic,(x+20+j*365,y+108));txt(x+100+j*365,y+298,'起始' if j==0 else '用力时呼气',27,False,'#356b60')
 d.line((x+333,y+205,x+380,y+205),fill='#356b60',width=5);d.polygon([(x+380,y+205),(x+365,y+195),(x+365,y+215)],fill='#356b60')
txt(73,1835,'每个动作先做1组、约8次；用力2秒，放回3秒。',36,True)
txt(73,1890,'轻水瓶250–500克起步；1公斤仅在专业允许且适应后用于部分动作。',30)
txt(73,1938,'背靠椅背，不憋气、不向下使劲；不做卷腹、重负荷深蹲或跳跃。',30)
d.rounded_rectangle((65,2000,1535,2207),radius=20,fill='#fff2ed',outline='#dfb0a3',width=3)
txt(88,2020,'不适即停，不强求完成',42,True,'#8c4334');txt(88,2080,'坠胀、突出感、漏尿或膝痛加重：停止训练；持续或明显加重请就医。',32,False,'#743f35');txt(88,2134,'出血、剧烈疼痛或无法排尿：及时就医。示意图不是个体医疗处方。',30,False,'#743f35')
im.save(P/'printable'/'training.png');im.save(P/'printable'/'training.pdf',resolution=193.5)
icon=Image.new('RGB',(192,192),'#356b60');di=ImageDraw.Draw(icon);di.rounded_rectangle((35,80,157,112),radius=13,fill='white');di.rounded_rectangle((28,56,56,136),radius=9,fill='white');di.rounded_rectangle((136,56,164,136),radius=9,fill='white');icon.save(P/'assets'/'icon.png')
