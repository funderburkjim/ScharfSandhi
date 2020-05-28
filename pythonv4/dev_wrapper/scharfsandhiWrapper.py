"""scharfsandhiWrapper.py
  wrapper function is a decorator used by scharfsandhi.
  This is one possible implementation, useful with ScharfSandhiArg.py.
"""
mdicttxt = """
rlvarnayormithahsavarnyam:1.1.9:fkAra kArayoH savarRaviDiH
idudeddvivacanampragrhyam:1.1.11:IdUdeddvivacanam pragfhyam
atororhasica:6.1.13:ato ror aplutad aplute.  6.1.14.  haSi ca
checa:6.1.73:Ce ca (tuk 71)
anmanosca:6.1.74:ANmANoSca (Ce 73, tuk 71)
padantadva:6.1.76:padAntAdvA (dIrGAt 75, Ce 73, tuk 71)
ikoyanaci:6.1.77:iko yaR aci
ecoyavayavah:6.1.78:eco 'yavAyAvaH
adgunah:6.1.87:Ad guRaH
vrddhireci:6.1.88:vfdDir eci
akahsavarnedirghah:6.1.101:akaH savafRe dIrGaH
enahpadantadati:6.1.109:eNaH padAntAd ati
etattadohsulopo:6.1.132:etattadoH sulopo 'kor anaYsamAse hali
dhralope:6.3.111:Qralope pUrvasya dIrGo 'RaH
jhalamjasonte:8.2.39:JalAM jaSo 'nte
sasajusoruh:8.2.66:sasajuzo ruH
ahan:8.2.68:ahan
amnarudharavar:8.2.70:amnarUDaravarityuBayaTA Candasi
naschavyaprasan:8.3.7:naS Cavy apraSAn
rori:8.3.14:ro ri
kharavasanayor:8.3.15:KaravasAnayor visarjanIyaH
bhobhago:8.3.17:BoBagoaGoapUrvasya yo 'Si
lopahsakalyasya:8.3.19:lopaH SAkalyasya
otogargyasya:8.3.20:oto gArgyasya
monusvarah:8.3.23:mo 'nusvAraH
nnohkuktuksari:8.3.28:NRoH kukwuk Sari (vA 26)
situk:8.3.31:Si tuk (naH 30, Sari 28, vA 26)
namohrasvad:8.3.32:Namo hrasvAd aci NamuR nityam
visarjaniyasyasah:8.3.34:visarjanIyasya saH
vasari:8.3.36:vA Sari
kupvohXkXpau:8.3.37:kupvoH XkXpau ca (Kari 15).
idudupadhasya:8.3.41:idudupaDasya cApratyayasya (kupvoH 37, iRaH zaH 39
nityamsamase:8.3.45:nityamsamAse 'nutarapadasTasya
atahkrkamikamsa:8.3.46:ataH kfkamikaMsakumBapAtrakuSAkarRIzvanavyayasya (samAse 45)
stohscunascuh:8.4.40:stoH ScunA ScuH
stunastuh:8.4.41:zwunA zwuH
yaronunasike:8.4.45:yaro 'nunAsike 'nunAsiko vA. (padAnta 42)
kharica:8.4.55:Kari ca. (JalAm 53, car 54)
anusvarasya:8.4.59:vA padAntasya (anusvArasya yayi parasavarRaH 58)
torli:8.4.60:tor li
jhayoho:8.4.62:Jayo ho 'nyatarasyAm
saschoti:8.4.63:SaS Co 'wi. (JayaH 62, anyatarasyAm 62)
chatvamami:8.4.63:vt. [964].  Catvam amIti vaktavyam.
jharojharisavarne:8.4.65:Jaro Jari savarRe (halaH 64)
"""
def wrapper_get_mdict():
 lines = mdicttxt.splitlines()
 d = {}
 for line in lines:
  line = line.strip()
  if line != '':
   (method,sutraref,sutra) = line.split(':')
   d[method] = (sutraref,sutra)
 return d
wrapper_mdict = wrapper_get_mdict()

def wrapper(f):
 def inner(*args,**kwargs):
  self = args[0]
  if not self.dbg:
   ans = f(*args,**kwargs)
   return ans
  name=f.__name__
  if name in ['deletary','sandhi1']:
   ans = f(*args,**kwargs)
   return ans
  # Append to self.history
  h = self.history
  # sandhi is first routine - add extra line   
  if name in ['sandhi']:
   s = args[1]
   h.append('"%s" START [%s]' %(s,name))
  before = ''.join(self.Linary).strip()
  if name == 'sandhimain':
   h.append('"%s" START [%s]' %(before,name))
  # call the function, and save the answer
  ans = f(*args,**kwargs)
  if name in ['sandhi']:
   h.append('"%s" DONE [%s]' %(ans,name))
  else:
   after = ''.join(self.Linary).strip()
   if name in ['sandhimain']:
    h.append('"%s" DONE [%s]' %(after,name))
   elif (before != after) and (name == 'acsandhi'):
    pass  # acsandhi does no direct changes itself    
   elif (before != after):
    #h.append('%s: "%s" (before="%s")' %(name,after,before))
    if name in wrapper_mdict:
     (sutraref,sutra)= wrapper_mdict[name]
     out = '"%s" %s %s [%s]'%(after,sutraref,sutra,name)
     h.append(out)
    elif name == 'non_acsandhi':
     pass
    else:
     h.append('"%s" [%s]' %(after,name))
  return ans
 return inner

# next is the wrapper at commit 565d3ef015a36d8e29465e28b4c924b335d4f5c3
def wrapper_v2(f):
 def inner(*args,**kwargs):
  self = args[0]
  if not self.dbg:
   ans = f(*args,**kwargs)
   return ans
  name=f.__name__
  if name in ['deletary','sandhi1']:
   ans = f(*args,**kwargs)
   return ans
  # Append to self.history
  h = self.history
  # sandhi is first routine - add extra line   
  if name in ['sandhi']:
   s = args[1]
   h.append('%s: XSTART: "%s"' %(name,s))
  before = ''.join(self.Linary).strip()
  if name == 'sandhimain':
   h.append('%s: START: "%s"' %(name,before))
  # call the function, and save the answer
  ans = f(*args,**kwargs)
  if name in ['sandhi']:
   h.append('%s: DONE: "%s"' %(name,ans))
  else:
   after = ''.join(self.Linary).strip()
   if name in ['sandhimain']:
    h.append('%s: DONE: "%s"' %(name,after))
   elif (before != after) and (name == 'acsandhi'):
    pass  # acsandhi does no direct changes itself    
   elif (before != after):
    #h.append('%s: "%s" (before="%s")' %(name,after,before))
    h.append('%s: "%s"' %(name,after))
  return ans
 return inner

def wrapper_v1(f):
 def inner(*args,**kwargs):
  self = args[0]
  if not self.dbg:
   ans = f(*args,**kwargs)
   return ans
  name=f.__name__
  if name in ['deletary']:
   ans = f(*args,**kwargs)
   return ans
  # Append to self.history
  h = self.history
  # sandhi is first routine - add extra line   
  if name in ['sandhi','sandhi1']:
   s = args[1]
   h.append('%s: START="%s"' %(name,s))
  before = ''.join(self.Linary)
  if name == 'sandhimain':
   h.append('%s: START Linary="%s"' %(name,before))
  # call the function, and save the answer
  ans = f(*args,**kwargs)
  after = ''.join(self.Linary)
  if (before != after):
   h.append('%s: Linary="%s"' %(name,after))
  return ans
 return inner
