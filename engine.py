import json,os,urllib.request
aU=os.environ['MAKEFUN_ENV_URL']
def B(p,b):
 r=urllib.request.Request(aU+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 with urllib.request.urlopen(r) as f:return json.load(f)
aQ={'p':100,'n':320,'b':330,'r':500,'q':900,'k':0}
def aS(i):return min(i,7-i)
N=[0,0,4,8,14,24,40,0];aD=[0,0,0,10,15,10,5,0];H=[20,25,10,0,0,10,25,20]
def h(l,r,f):
 c=aS(f)+aS(r)
 if l=='p':return N[r]+(aD[r] if f in(3,4) else 0)
 if l=='n':return 6*c-20
 if l=='b':return 4*c-8
 if l=='r':return (15 if r==6 else 0)+(5 if r==0 and f in(3,4) else 0)
 if l=='q':return 2*c-6
 return H[f] if r==0 else max(-50,-15*r)
def jj(r,f):return 8*(aS(f)+aS(r))-24
P=6400
z=30000
aI=60000
aR=[0];aF=[0];aO=[0,0];Y=[0];aB=[0];aM=[15]
def aA(s):return 22+(8-int(s[1]))*10+ord(s[0])-97
def uci2m(u):
 return (aA(u[:2]),aA(u[2:4]),u[4] if len(u)>4 else '')
def parse(fen):
 b=['']*120
 for r,row in enumerate(fen.split()[0].split('/')):
  f=0
  for c in row:
   if c.isdigit():f+=int(c)
   else:b[(2+r)*10+2+f]=c;f+=1
 return b
def J(fen):
 c=fen.split()[2] if len(fen.split())>2 else '-'
 v=0
 if 'K' in c:v|=1
 if 'Q' in c:v|=2
 if 'k' in c:v|=4
 if 'q' in c:v|=8
 return v
aX=bytes(21<=t<100 and 2<=t%10<=9 for t in range(130))
O=aX.__getitem__
def K(i,wh):
 r=i//10-2;f=i%10-2
 return ((7-r) if wh else r)*8+f
def Q(p,i):
 if p=='K' or p=='k':return 0
 l=p.lower()
 z=K(i,p<'a');v=aQ[l]+h(l,z//8,z%8)
 return v if p<'a' else -v
def S(i,wh):
 ph=aF[0]
 if ph>P:ph=P
 r=K(i,wh)
 return int(round((h('k',r//8,r%8)*ph+jj(r//8,r%8)*(P-ph))/float(P)))
def W(b,w):
 s=aR[0]+S(Y[0],1)-S(aB[0],0)
 if aO[0]>=2:s+=30
 if aO[1]>=2:s-=30
 if aF[0]<2400:
  pf=[0]*12;pf2=[0]*12
  for i in range(21,100):
   q=b[i]
   if q=='P':pf[i%10]+=1
   elif q=='p':pf2[i%10]+=1
  for i in range(2,10):
   if pf[i]>1:s-=12*(pf[i]-1)
   elif pf[i]==1 and not (pf[i-1] or pf[i+1]):s-=16
   if pf2[i]>1:s+=12*(pf2[i]-1)
   elif pf2[i]==1 and not (pf2[i-1] or pf2[i+1]):s+=16
 return s if w else -s
aT={'n':(-21,-19,-12,-8,8,12,19,21),'b':(-11,-9,9,11),'r':(-10,-1,1,10),'q':(-11,-10,-9,-1,1,9,10,11),'k':(-11,-10,-9,-1,1,9,10,11)}
aJ=(-11,-10,-9,-1,1,9,10,11)
def atk(b,s,c):
 if c:
  for d in aJ:
   t=s+d
   if O(t) and b[t]=='K':return 1
  for d in aT['n']:
   t=s+d
   if O(t) and b[t]=='N':return 1
  for d in (9,11):
   t=s+d
   if O(t) and b[t]=='P':return 1
  for d in (-10,-1,1,10):
   t=s+d
   while O(t):
    q=b[t]
    if q:
     if q=='R' or q=='Q':return 1
     break
    t+=d
  for d in (-11,-9,9,11):
   t=s+d
   while O(t):
    q=b[t]
    if q:
     if q=='B' or q=='Q':return 1
     break
    t+=d
 else:
  for d in aJ:
   t=s+d
   if O(t) and b[t]=='k':return 1
  for d in aT['n']:
   t=s+d
   if O(t) and b[t]=='n':return 1
  for d in (-9,-11):
   t=s+d
   if O(t) and b[t]=='p':return 1
  for d in (-10,-1,1,10):
   t=s+d
   while O(t):
    q=b[t]
    if q:
     if q=='r' or q=='q':return 1
     break
    t+=d
  for d in (-11,-9,9,11):
   t=s+d
   while O(t):
    q=b[t]
    if q:
     if q=='b' or q=='q':return 1
     break
    t+=d
 return 0
def king(b,c):
 k='K' if c else 'k'
 for i in range(21,100):
  if b[i]==k:return i
 return 0
def gen(b,w,cap=0):
 M=[]
 for i in range(21,100):
  p=b[i]
  if not p or (p<'a')!=w:continue
  l=p.lower()
  if l=='p':
   d=-10 if w else 10
   pr=(i//10==3) if w else (i//10==8)
   o=i+d
   if O(o) and not b[o] and not cap:
    if pr:
     for x in 'qrbn':M.append((i,o,x))
    else:
     M.append((i,o,''))
     if ((i//10==8) if w else (i//10==3)) and not b[i+2*d]:M.append((i,i+2*d,''))
   for c in (d-1,d+1):
    t=i+c
    if O(t) and b[t] and (b[t]<'a')!=w:
     if pr:
      for x in 'qrbn':M.append((i,t,x))
     else:M.append((i,t,''))
  else:
   for d in aT[l]:
    t=i+d
    while O(t):
     q=b[t]
     if q:
      if (q<'a')!=w and q.lower()!='k':M.append((i,t,''))
      break
     if not cap:M.append((i,t,''))
     if l=='n' or l=='k':break
     t+=d
  if l=='k':
   if w and i==aA('e1'):
    if (aM[0]&1) and b[aA('h1')]=='R' and not b[aA('f1')] and not b[aA('g1')] and not atk(b,aA('e1'),0) and not atk(b,aA('f1'),0):M.append((i,aA('g1'),'c'))
    if (aM[0]&2) and b[aA('a1')]=='R' and not b[aA('b1')] and not b[aA('c1')] and not b[aA('d1')] and not atk(b,aA('e1'),0) and not atk(b,aA('d1'),0):M.append((i,aA('c1'),'c'))
   elif not w and i==aA('e8'):
    if (aM[0]&4) and b[aA('h8')]=='r' and not b[aA('f8')] and not b[aA('g8')] and not atk(b,aA('e8'),1) and not atk(b,aA('f8'),1):M.append((i,aA('g8'),'c'))
    if (aM[0]&8) and b[aA('a8')]=='r' and not b[aA('b8')] and not b[aA('c8')] and not b[aA('d8')] and not atk(b,aA('e8'),1) and not atk(b,aA('d8'),1):M.append((i,aA('c8'),'c'))
 return M
aL=aA('a1');aC=aA('h1');aH=aA('a8');X=aA('h8')
def mk(b,m):
 f,t,pr=m;pc=b[f];cap=b[t]
 if pc=='K' and abs(t-f)==2 and not pr:pr='c'
 elif pc=='k' and abs(t-f)==2 and not pr:pr='c'
 ocr=aM[0];okw=Y[0];okb=aB[0]
 d=-Q(pc,f)
 b[f]='';b[t]=pc
 if cap:
  d-=Q(cap,t)
  l=cap.lower()
  if l!='p':aF[0]-=aQ[l]
  if l=='b':aO[0 if cap<'a' else 1]-=1
 if pr=='c':
  if t>f:
   r=b[t+1];d-=Q(r,t+1);d+=Q(r,t-1);b[t-1]=r;b[t+1]=''
  else:
   r=b[t-2];d-=Q(r,t-2);d+=Q(r,t+1);b[t+1]=r;b[t-2]=''
 elif pr:
  b[t]=pr.upper() if pc<'a' else pr
  aF[0]+=aQ[pr]
  if pr=='b':aO[0 if pc<'a' else 1]+=1
 d+=Q(b[t],t)
 aR[0]+=d
 if pc=='K':Y[0]=t;aM[0]&=12
 elif pc=='k':aB[0]=t;aM[0]&=3
 if f==aL or t==aL:aM[0]&=13
 if f==aC or t==aC:aM[0]&=14
 if f==aH or t==aH:aM[0]&=7
 if f==X or t==X:aM[0]&=11
 return (f,t,cap,pc,pr,d,ocr,okw,okb)
def un(b,u):
 f,t,cap,pc,pr,d,ocr,okw,okb=u
 aR[0]-=d
 b[f]=pc;b[t]=cap
 if pr=='c':
  if t>f:b[t+1]=b[t-1];b[t-1]=''
  else:b[t-2]=b[t+1];b[t+1]=''
 elif pr:
  aF[0]-=aQ[pr]
  if pr=='b':aO[0 if pc<'a' else 1]-=1
 if cap:
  l=cap.lower()
  if l!='p':aF[0]+=aQ[l]
  if l=='b':aO[0 if cap<'a' else 1]+=1
 aM[0]=ocr;Y[0]=okw;aB[0]=okb
aK=[]
aE={}
G=[[None,None] for _ in range(80)]
F={}
y=[0]
A=[0]
def aN(b,w,a,e,q=0):
 y[0]+=1
 if y[0]>aI:return None
 inc=atk(b,Y[0] if w else aB[0],not w)
 if not inc:
  s=W(b,w)
  if q>=6:return s
  if s>=e:return s
  if s>a:a=s
  if a>=e:return a
  ms=gen(b,w,1)
 else:
  s=-z-1
  ms=gen(b,w)
 ms.sort(key=lambda m:-(aQ[b[m[1]].lower()]*16-aQ[b[m[0]].lower()]) if b[m[1]] else 0)
 any=0
 for m in ms:
  u=mk(b,m)
  if atk(b,Y[0] if w else aB[0],not w):un(b,u);continue
  any=1
  r=aN(b,not w,-e,-a,q+1)
  un(b,u)
  if r is None:return None
  v=-r
  if v>s:s=v
  if v>a:
   a=v
   if a>=e:return a
 if not any and inc:return -z
 return s
def Z(b,w,d,a,e,p,nullok=1):
 y[0]+=1
 if y[0]>aI:return None
 k=(tuple(b),w,aM[0])
 if p>0:
  for q in aK:
   if q==k:return 0
 aK.append(k)
 t=aE.get(k)
 tm=None
 if t:
  tm=t[3]
  if t[0]>=d:
   if t[1]==0:aK.pop();return t[2]
   if t[1]==1 and t[2]>=e:aK.pop();return t[2]
   if t[1]==2 and t[2]<=a:aK.pop();return t[2]
 inc=atk(b,Y[0] if w else aB[0],not w)
 if inc:d+=1
 if d<=0:aK.pop();return aN(b,w,a,e)
 if nullok and not inc and d>=3 and e-a<2:
  if any(q and (q<'a')==w and q.lower() not in'pk' for q in b):
   R=2+d//5
   r=Z(b,not w,d-1-R,-e,-e+1,p+1,0)
   if r is None:aK.pop();return None
   v=-r
   if v>=e:aK.pop();return v
 ms=gen(b,w)
 if not ms:aK.pop();return -z+p
 km=G[p] if p<80 else (None,None)
 ms.sort(key=lambda m:-999999 if m==tm else (-(aQ[b[m[1]].lower()]*16-aQ[b[m[0]].lower()]) if b[m[1]] else -50000 if m[2] else -9000 if m==km[0] else -8000 if m==km[1] else -F.get(m,0)))
 o0=a;bs=-z-1;bm=None;an=0;n=0
 for m in ms:
  u=mk(b,m)
  if atk(b,Y[0] if w else aB[0],not w):un(b,u);continue
  an=1;n+=1
  quiet=not b[m[1]] and not m[2]
  v=None
  if n==1:
   v=Z(b,not w,d-1,-e,-a,p+1)
   if v is not None:v=-v
  else:
   rd=0
   if quiet and d>=3 and n>3 and not inc:
    rd=1 if n<10 else 2
    if rd>d-2:rd=max(0,d-2)
   r=Z(b,not w,d-1-rd,-a-1,-a,p+1)
   if r is None:v=None
   else:
    v=-r
    if rd and v>a and v<e:
     r=Z(b,not w,d-1,-e,-a,p+1)
     v=None if r is None else -r
    elif not rd and a<v<e:
     r=Z(b,not w,d-1,-e,-a,p+1)
     v=None if r is None else -r
    elif rd and v>=e:
     r=Z(b,not w,d-1,-e,-a,p+1)
     v=None if r is None else -r
  un(b,u)
  if v is None:aK.pop();return None
  if v>bs:bs=v;bm=m
  if v>a:
   a=v
   if a>=e:
    if p<80 and G[p][0]!=m:G[p][1]=G[p][0];G[p][0]=m
    if quiet:F[m]=F.get(m,0)+d*d
    break
 if not an:aK.pop();return -z+p if inc else 0
 aE[k]=(d,2 if bs<=o0 else 1 if bs>=e else 0,bs,bm)
 aK.pop()
 return bs
def j(b,w=True):
 aR[0]=0;aF[0]=0;aO[0]=0;aO[1]=0;aK[:]=[]
 for i in range(21,100):
  p=b[i]
  if not p:continue
  aR[0]+=Q(p,i)
  l=p.lower()
  if l!='p' and l!='k':aF[0]+=aQ[l]
  if l=='b':aO[0 if p<'a' else 1]+=1
  if p=='K':Y[0]=i
  elif p=='k':aB[0]=i
def best(b,w,legal,cr=15):
 aM[0]=cr
 j(b)
 y[0]=0
 aE.clear();F.clear()
 A[0]=0
 for i in range(80):G[i][0]=G[i][1]=None
 ent=[uci2m(u) for u in legal]
 if not ent:return legal[0]
 aU={m:u for m,u in zip(ent,legal)}
 bm=ent[0]
 for d in range(1,24):
  bs=-z-1;cur=None
  ab=0
  for n,m in enumerate(ent):
   uu=mk(b,m)
   if n==0:
    v=Z(b,not w,d-1,-z-1,z+1,1)
    if v is not None:v=-v
   else:
    r=Z(b,not w,d-1,-bs-1,-bs,1)
    if r is None:v=None
    else:
     v=-r
     if v>bs and v<z+1:
      r=Z(b,not w,d-1,-z-1,-bs,1)
      v=None if r is None else -r
   un(b,uu)
   if v is None:ab=1;break
   if v>bs:bs=v;cur=m
   if v>z-100:break
  if ab:break
  if cur:bm=cur;A[0]=d
  else:break
  ent.sort(key=lambda m:0 if m==bm else 1)
 return aU[bm]
while True:
 g=B('/game',{})
 if g.get('status')=='done':break
 cr=J(g.get('fen','')+' ')
 while g.get('status')=='your_move':
  b=parse(g['fen']);w=g['fen'].split()[1]=='w'
  mv=best(b,w,g['legal_moves'],cr)
  g=B('/move',{'game':g['game'],'move':mv})
