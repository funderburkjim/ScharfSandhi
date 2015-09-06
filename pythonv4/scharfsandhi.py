# coding=utf-8
#!/usr/bin/env python
""" Aug 6, 2015  In methods 'bhobhago' and 'otogargyasya',
    change "bhos", "bhagos", and "aghos" to the usual SLP1 coding of
    "Bos","Bagos", and "aGos".  Also, in 'bhobhago', similarly correct
    the sutra spelling in the comment.
    Minor question: in derivation, of 'Bos atra' to 'Bo atra', Katre
    gives the last step as 8.3.19, while this code gives as 8.3.20.
    Sep 6, 2015.  Make the 'wrapper' decorator reside in 
    module scharfsandhiWrapper, rather than in 'wrapper'.  A slight
    namespace improvement.  Use of Python 'package' might be better,
    but I'm not sure how to do this.
"""
from scharfsandhiWrapper import wrapper
import re

def set_memberP( c, s):
 """ method set_memberP 
 c is a char ,implemented as a string of length 1
 s is a "set of char", implemented as a string.
 """
 if c in s:
  return True
 else:
  return False

def strReplace( x, idx1, idx2, y):
 """ method strReplace 
  The substring of 'x' specified by idx1,idx2 is replaced by the string y.
  @param x input string
  @param idx1  first character position at which to replace (inclusive)
  @param idx2  last character position at which to replace (exclusive)
  @param y  string for replacement.
  @return string resulting from replacement.
  'x' and 'y' are strings. Return a string

  The substring begins at the specified start and extends to the character
  at index end - 1 or to the end of the StringBuffer if no such character
  exists. First the characters in the substring are removed and then the
  specified String is inserted at start.
 """

 b0 = x[0:idx1]
 b1 = y
 b2 = x[idx2:]
 b = b0+b1+b2
 return str(b)

def sandhiSplit( x):
 """ method sandhiSplit 
  'x' is a string
  From a given input string, generate an array of strings.
  The even elements (0,2,4...) of the array have value
  "s" if the next array element is a string of Sanskrit characters
  "o" if the next array element is a string of other non-Sanskrit characters
  Sanskrit characters are according to the SLP1 spelling.
  <p>
  "- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/"
  <p>
  Note that the '/' is an artificial 'Sandhi-blocking' character.
 """
 dbg = False
 a = [] # list of strings 
 INITIAL = 0
 SKT = 1
 OTHER = 2
 #  Only non-alphabetic chars considered to be Sanskrit are
 #  - and space and apostrophe and "|" and "/"
 #  20090801, "/" is a sandhi-blocking character.

 #  June 22: Added period to list of Sanskrit characters.
 sanskrit_str = "- '.aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/"
 #sanskrit_strs = sanskrit_str.split("")
 #sanskrit_strs_list = Arrays.asList(sanskrit_strs)
 sanskrit_set = set(sanskrit_str)
 #xarr = x.split("")
 xarr =  x
 ilen = len(x)
 state = INITIAL
 more = True
 y = "" # list of characters
 #c = ""
 ipos = 0
 while ipos < ilen:
  c = xarr[ipos]
  if state == INITIAL:
   y = c
   if (c in sanskrit_set):
    state = SKT

   else:
    state = OTHER

  elif state == SKT:
   if (c in sanskrit_set):
    y = y + c
   else:

    a.append("s")
    a.append(y)
    y = c
    state = OTHER
  else:
   #  state = OTHER
   if (c in sanskrit_set):
    a.append("o")
    a.append(y)
    y = c 
    state = SKT
   else:
    y = y + c 
  ipos += 1
 if 0 != len(y):
  if state == SKT:

   a.append("s")
   a.append(y)
  elif state == OTHER:
   a.append("o")
   a.append(y)
  else:
   #  should not occur
   pass

 return a

def diff_string(x, y):
 """ method diff_string 
  x and y are strings
  Return a string which consists of all characters in x which are
  not in y. 
 """
 b = [c for c in x if c not in y]
 return (''.join(b))

# 
# * The Sanskrit sounds represented in the font Sanskrit01

# 
skta = "a"
sktaa = "A"
skti = "i"
sktii = "I"
sktu = "u"
sktuu = "U"
sktri = "f"
sktrii = "F"
sktlri = "x"
sktlrii = "X"
skte = "e"
sktai = "E"
skto = "o"
sktau = "O"
sktvisarga = "H"
sktanusvara = "M"
sktnasalization = "~"

# {shift `.  It precedes the sound it nazalizes}
sktavagraha = "'"

# changed from"""";
#constant sktsvarita = "^"

# {opt i space.  It precedes the sound it accents}
#constant sktudattaa = ""
#constant sktudattai = ""
#constant sktudattau = "

#constant sktudattae = ""
#constant sktudattao = ""
#constant sktudattaai = ""
#constant sktsvaritaa = "	"
#constant sktsvaritai = ""
#constant sktsvaritau = "

#constant sktsvaritae = ""
#constant sktsvaritao = ""
sktk = "k"
sktkh = "K"
sktg = "g"
sktgh = "G"
sktkn = "N"
sktc = "c"
sktch = "C"
sktj = "j"
sktjh = "J"
sktcn = "Y"
sktretrot = "w"
sktretroth = "W"
sktretrod = "q"
sktretrodh = "Q"
sktretron = "R"
sktt = "t"
sktth = "T"
sktd = "d"
sktdh = "D"
sktn = "n"
sktp = "p"
sktph = "P"
sktb = "b"
sktbh = "B"
sktm = "m"
skty = "y"
sktr = "r"
sktl = "l"
sktv = "v"
sktsch = "S"
sktsh = "z"
skts = "s"
skth = "h"

# Neutral characters
newline = "\n"
tab = "\t"
space = " "
hyphen = "-"
comma = ","
semicolon = ";"
colon = ":"
period = "."

# extended ascii. Required to fill Soundary, but otherwise unused
sktjihvamuliya = "Z"
sktupadhmaniya = "V"
# sktanunasika = "µ" #{opt m.  It should follow the sound it nasalizes}
#sktroot = "§" #{opt v}

cantamax = 27
CAntaPadary = ["" for x in xrange(0,cantamax+1)]
CAntaPadary[1] = "aqac"
CAntaPadary[2] = "Awac"
CAntaPadary[3] = "Alac"
CAntaPadary[4] = "ec"
CAntaPadary[5] = "Ac"
CAntaPadary[6] = "ic"
CAntaPadary[7] = "ilac"
CAntaPadary[8] = "izRuc"
CAntaPadary[9] = "Irac"
CAntaPadary[10] = "ktic"
CAntaPadary[11] = "KizRuc"
CAntaPadary[12] = "Wac"
CAntaPadary[13] = "Rac"
CAntaPadary[14] = "tfc"
CAntaPadary[15] = "daGnac"
CAntaPadary[16] = "dvayasac"
CAntaPadary[17] = "dvyac"
CAntaPadary[18] = "nAwac"
CAntaPadary[19] = "biqac"
CAntaPadary[20] = "birIsac"
CAntaPadary[21] = "mAtrac"
CAntaPadary[22] = "yAc"
CAntaPadary[23] = "vuc"
CAntaPadary[24] = "vfc"
CAntaPadary[25] = "SaNkawac"
CAntaPadary[26] = "SAlac"
CAntaPadary[27] = "zWac"

# Pradi array of strings: prefixes
pradimax = 27
Pradi = [" " for x in xrange(0,27+1)]
Pradi[1] = "pra"
Pradi[2] = "parA"
Pradi[3] = "apa"
Pradi[4] = "sam"
Pradi[5] = "anu"
Pradi[6] = "ava"
Pradi[7] = "nis"
Pradi[8] = "dus"
Pradi[9] = "vi"
Pradi[10] = "A"
Pradi[11] = "ni"
Pradi[12] = "aDi"
Pradi[13] = "api"
Pradi[14] = "ati"
Pradi[15] = "su"
Pradi[16] = "ud"
Pradi[17] = "aBi"
Pradi[18] = "prati"
Pradi[19] = "pari"
Pradi[20] = "upa"

# various character sets. Since Sanskrit01 uses 1 ascii character to
# represent elements of the Sanskrit alphabet, these sets may be
# represented as character strings.

ru = skts
Avarna = skta + sktaa
Ivarna = skti + sktii
Uvarna = sktu + sktuu
Rvarna = sktri + sktrii
Lvarna = sktlri + sktlrii
Ku = sktk + sktkh + sktg + sktgh + sktkn
Cu = sktc + sktch + sktj + sktjh + sktcn
Retrotu = sktretrot + sktretroth + sktretrod + sktretrodh + sktretron
Tu = sktt + sktth + sktd + sktdh + sktn
Pu = sktp + sktph + sktb + sktbh + sktm
An = Avarna + Ivarna + Uvarna
Ak = Avarna + Ivarna + Uvarna + Rvarna + Lvarna
Ik = Ivarna + Uvarna + Rvarna + Lvarna
Uk = Uvarna + Rvarna + Lvarna
Ekn = skte + skto
Ec = skte + skto + sktai + sktau
# PMS dipthongs
Aic = sktai + sktau
Ac = Ak + Ec
Ic = diff_string(Ac, Avarna)
At = Ac + skth + skty + sktv + sktr
Yan = skty + sktv + sktr + sktl
# PMS semivowels


Yam = skty + sktv + sktr + sktl + sktcn + sktm + sktkn + sktretron + sktn

# PMS semivowels and nasals
Am = Ac + skth + Yam

# PMS vowels, semivowels, nasals and h
KNam = sktkn + sktretron + sktn
Yacn = Yam + sktjh + sktbh
Jhash = sktjh + sktbh + sktgh + sktretrodh + sktdh

# PMS voiced aspirated stops
Bhash = sktbh + sktgh + sktretrodh + sktdh

# PMS voiced aspirated stops other than jh
Jasch = sktj + sktb + sktg + sktretrod + sktd

# PMS unvoiced unaspirated stops
Basch = sktb + sktg + sktretrod + sktd

# PMS unvoiced unaspirated stops other than j
Jhasch = sktjh + sktbh + sktgh + sktretrodh + sktdh + sktj + sktb + sktg + sktretrod + sktd

# PMS voiced stops
Hasch = skth + Yam + Jhasch

# PMS voiced consonants
Vasch = diff_string(Hasch, skth + skty)

# PMS voiced consonants other than h and y
Asch = Ac + Hasch

# PMS voiced sounds
Chav = sktch + sktretroth + sktth + sktc + sktretrot + sktt
Khay = sktkh + sktph + sktch + sktretroth + sktth + sktc + sktretrot + sktt + sktk + sktp

# PMS unvoiced stops
Jhay = Jhasch + Khay

# PMS non-nasal stops both voiced and unvoiced
Yay = Yam + Jhay

# PMS semivowels and stops
May = sktm + sktkn + sktretron + sktn + Jhay

# PMS stops other than palatal n
Cay = sktc + sktretrot + sktt + sktk + sktp
Khar = sktkh + sktph + sktch + sktretroth + sktth + sktc + sktretrot + sktt + sktk + sktp + sktsch + sktsh + skts

# PMS unvoiced sounds
Car = sktc + sktretrot + sktt + sktk + sktp + sktsch + sktsh + skts
Schar = sktsch + sktsh + skts

# PMS unvoiced sylibants
Jhar = Jhay + Schar

# PMS non-nasal stops and unvoiced silibants
Yar = Yam + Jhay + Schar

# PMS semivowels, stops and unvoiced silibants (consonants other than h)
Schal = sktsch + sktsh + skts + skth
Jhal = Jhay + Schal

# PMS non-nasal stops and silibants ?
# ejf: Hal contains all consonants
Hal = skty + sktv + sktr + sktl + sktcn + sktm + sktkn + sktretron + sktn + sktjh + sktbh + sktgh + sktretrodh + sktdh + sktj + sktb + sktg + sktretrod + sktd + sktkh + sktph + sktch + sktretroth + sktth + sktc + sktretrot + sktt + sktk + sktp + sktsch + sktsh + skts + skth
#print "Hal=",Hal,len(Hal)
Ral = diff_string(Hal, skty + sktv)

# PMS consonants other than y and v
Val = diff_string(Hal, skty)

# PMS consonants other than y
Al = Ac + Hal

# PMS all independent sounds
Guna = skta + skte + skto
Vrddhi = sktaa + sktai + sktau
Sounds = Al + sktvisarga + sktanusvara
Linend = space + comma + semicolon + colon + period

# ----- ejf set constants
# These are sets that were referenced by inline Pascal
# set construction operators.

Rvarna_and_Lvarna = Rvarna + Lvarna
Jhal_not_ru = diff_string(Jhal, ru)
Hasch_and_skta = Hasch + skta
sktr_and_ru = sktr + ru
Khar_and_linend = Khar + Linend
Ku_and_Pu_and_Schar = Ku + Pu + Schar
Ku_and_Pu = Ku + Pu
Tu_and_skts = Tu + skts
Cu_and_sktsch = Cu + sktsch
Retrotu_sktsh = Retrotu + sktsh
Yay_not_Yan = diff_string(Yay, Yan)
sktn_and_sktsh_and_skts = sktn + sktsh + skts
Hal_and_ru = Hal + ru
Al_and_Linend = Al + Linend

# initialize Soundary, and related constants
maxyatna = 11
maxsthana = 5

# Soundary is 2-dimensional array of strings of dimension
# (1+maxsthana) (by 1+maxyatna)
Soundary = []
for i in xrange(0,1+maxsthana):
 Soundary.append(['' for j in xrange(0,1+maxyatna)])
# constants for first coord of Soundary
ikanthya = 1
italavya = 2
imurdhanya = 3
idantya = 4
iosthya = 5

# second coord of Soundary
ihrasva = 1
idirgha = 2
iguna = 3
ivrddhi = 4
isparsa1 = 5
isparsa2 = 6
isparsa3 = 7
isparsa4 = 8
isparsa5 = 9
iantahstha = 10
iusmana = 11

# initialize Soundary
Soundary[ikanthya][ihrasva] = skta
Soundary[ikanthya][idirgha] = sktaa
Soundary[ikanthya][iguna] = skta
Soundary[ikanthya][ivrddhi] = sktaa
Soundary[ikanthya][isparsa1] = sktk
Soundary[ikanthya][isparsa2] = sktkh
Soundary[ikanthya][isparsa3] = sktg
Soundary[ikanthya][isparsa4] = sktgh
Soundary[ikanthya][isparsa5] = sktkn
Soundary[ikanthya][iantahstha] = skth
Soundary[ikanthya][iusmana] = sktjihvamuliya

Soundary[italavya][ihrasva] = skti
Soundary[italavya][idirgha] = sktii
Soundary[italavya][iguna] = skte
Soundary[italavya][ivrddhi] = sktai
Soundary[italavya][isparsa1] = sktc
Soundary[italavya][isparsa2] = sktch
Soundary[italavya][isparsa3] = sktj
Soundary[italavya][isparsa4] = sktjh
Soundary[italavya][isparsa5] = sktcn
Soundary[italavya][iantahstha] = skty
Soundary[italavya][iusmana] = sktsch

Soundary[imurdhanya][ihrasva] = sktri
Soundary[imurdhanya][idirgha] = sktrii
Soundary[imurdhanya][iguna] = skta
Soundary[imurdhanya][ivrddhi] = sktaa
Soundary[imurdhanya][isparsa1] = sktretrot
Soundary[imurdhanya][isparsa2] = sktretroth
Soundary[imurdhanya][isparsa3] = sktretrod
Soundary[imurdhanya][isparsa4] = sktretrodh
Soundary[imurdhanya][isparsa5] = sktretron
Soundary[imurdhanya][iantahstha] = sktr
Soundary[imurdhanya][iusmana] = sktsh

Soundary[idantya][ihrasva] = sktlri
Soundary[idantya][idirgha] = sktlrii
Soundary[idantya][iguna] = skta
Soundary[idantya][ivrddhi] = sktaa
Soundary[idantya][isparsa1] = sktt
Soundary[idantya][isparsa2] = sktth
Soundary[idantya][isparsa3] = sktd
Soundary[idantya][isparsa4] = sktdh
Soundary[idantya][isparsa5] = sktn
Soundary[idantya][iantahstha] = sktl
Soundary[idantya][iusmana] = skts

Soundary[iosthya][ihrasva] = sktu
Soundary[iosthya][idirgha] = sktuu
Soundary[iosthya][iguna] = skto
Soundary[iosthya][ivrddhi] = sktau
Soundary[iosthya][isparsa1] = sktp
Soundary[iosthya][isparsa2] = sktph
Soundary[iosthya][isparsa3] = sktb
Soundary[iosthya][isparsa4] = sktbh
Soundary[iosthya][isparsa5] = sktm
Soundary[iosthya][iantahstha] = sktv
Soundary[iosthya][iusmana] = sktupadhmaniya

def identify(aksara):
 """ identify
 Returns positions (Isthana and Iyatna) in Soundary matrix
 where the character 'aksara' is found.
 Note that some sounds (notably vowels. e.g. skta) appear multiple times
 in the Soundary listing.  In these cases, the FIRST occurrence is used.
 Returns (0,0) if not found.
 @param aksara
 @return
 """
 ans = [0,0] 
 I1 = 1
 while I1 <= maxsthana:
  I2 = 1
  while I2 <= maxyatna:
   if aksara == Soundary[I1][I2]:
    ans[0] = I1
    ans[1] = I2
    return ans
   I2 += 1
  I1 += 1
 ans[0] = 0
 ans[1] = 0
 return ans

# constants global to sandhi routine
pratipadmax = 20

# PMS Maximum length assumed for lexical items
iapi = 13

# PMS api usually is not an upasarga so check it separately

# ejf additions for efficiency in lookup
sandhi_exceptions_list = [
   "RiN", #  RiN change made 20090801, PMS.
   "tij",
   "aR","uR","yaR",
   "aD","ruD",
   "an","in","kan","kaDyEn","qvun","tan","dAn","man","vun",
   "am","Am","num",
   "ay","Ay",
   "car", "kur", "Sar",
   "eS", "KaS", "jaS", "niS",
   "Jaz", "Baz",
   "as","atus","aTus","is","us","os","kas","kAs","Nas","tas","tAs","TAs","Bis","Byas"
]
sandhi_exceptions_set = set(sandhi_exceptions_list)
CAntaPadary_set = set(CAntaPadary)
sandhi_noprep_list = [
   "tuj",
   "Wan","tran","dozan","yakan","yUzan","Sakan","zWan","han",
   "ktin","kvin","min","vin"
]
sandhi_noprep_set = set(sandhi_noprep_list)
# next used only by idudeddvivacanampragrhyam to set self.Pragrhya
pragrhya_list = [
 "amI","aDiparI","aBipratI","manasI",
 "amU", # PMS: 1.1.12.  adaso mAt
 "SAlInakOpIne", "uBe",
 "Aho", "utAho" # PMS: 1.1.15. ot
]
pragrhya_set = set(pragrhya_list)

visargaprep_exceptions_list= [
   "ahaH","svaH","antaH","prAtaH","punaH",
   "mAtaH", "kOsalyAmAtaH", "sanutaH", "catuH", "prAduH"
]
visargaprep_exceptions_set = set(visargaprep_exceptions_list)

class ScharfSandhi(object):

 def __init__(self):
  #  variables global to sandhi routines
  self.linmax = 0 
  self.Linary = []
 
  self.Isthana1 = 0 
  self.Isthana2 = 0
  self.Iyatna1 = 0
  self.Iyatna2 = 0
  self.PurvaPada = "" 
  self.Pada1 = ""
  #self.NxtPada1 = ""
  self.Pada2 = ""
 
  self.Upasarga = False
  self.NoStoh = False
  self.NoKNam = False
  self.Exception = False
  self.Pronoun = False
  self.EkahPurvaParayoh = False
  self.Error = 0
  #self.IEnd = 0
  #self.Inextsp = 0
  #self.IPrev = 0
  #self.Inext = 0
  #self.IPrevSpace = 0
  self.Index = 0
  #self.Found = False  #unused
  #self.NoSpace = False
  self.Dhralopa = False
  self.OtherCloseSandhi = False
  self.Pragrhya = False
  self.Uttarapada = False
  #self.NxtUttarapada = False
  #self.FldChr = None # Never changed.
  self.Despace = False
  self.External = False
  self.Compound = False
  self.Chandas = False
  self.CloseUpasargaSandhi = False
  self.PaninianText = False
 
  self.TukPadantat = False
  self.ScharSchari = False
  self.XkXpKupvoh = False
  self.ChAti = False
  self.ParaSavarna = False
  self.Anunasika = False
  self.Padbound = ""

  self.dbg = False
  
 @wrapper
 def simple_sandhioptions(self,code):
  """  method simple_sandhioptions
    code should be one of a preconfigured set of options.
    Set a 'Standard' set of options for each.
    Set self.Error and return same
  """
  if (code == 'C'):
   self.sandhioptions("C","N","S","")
  elif (code == 'E'):
   self.sandhioptions("E","N","S","Y")
  elif (code == 'E1'):
   self.sandhioptions("E","N","S","")
  elif (code == 'E2'):
   self.sandhioptions("E","N","S","Y")
   self.lopah_v=True
  else:
   self.Error = 5
  return self.Error

 @wrapper
 def sandhioptions(self, compound_ans, vedic_ans, closeSandhi_ans, despace_ans):
  """ method sandhioptions 
  # 
  #   * Returns 0 (ok) or 4 (error)
  #   * @param compound_ans C for compound sandhi, E for External sandhi
  #   * @param vedic_ans  Y or N
  #   * @param closeSandhi_ans N,Y,S
  #   * @param despace_ans Y or N
  #  Sep 5, 2015. set flag lopah_v=False. (used by lopahsakalyasya method)
  """
  #Answer = ""
  Yes = "Y"
  No = "N"
  error = 0
  #  initialize external flags to false.
  self.External = False
  self.Compound = False
  self.Despace = False
  self.Chandas = False
  self.CloseUpasargaSandhi = False
  self.TukPadantat = False # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
  self.ScharSchari = False # PMS 8.3.36.  vA Sari
  self.XkXpKupvoh = False  # PMS 8.3.37.  kupvoH XkXpau ca.
  self.ChAti = False     # PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
  self.ParaSavarna = False # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
  self.Anunasika = False # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
  self.lopah_v = False
  Answer = compound_ans.upper()
  if Answer == "":
   Answer = "?"
  if Answer == "C":
   self.Compound = True
   self.Padbound = hyphen
  elif Answer == "E":
   self.External = True
   self.Padbound = space
  else:
   self.Error = 4
   return self.Error
  #  process vedic answer
  #  print "Is this a Vedic text (chandas)?\n";
  #  print "Default no: ";
  #  readln(Answer);
  Answer = vedic_ans.upper()
  if Answer == "":
   Answer = "?"
  if Answer == "Y":
   self.Chandas = True
  elif Answer == "N":
   self.Chandas = False
  else:
   self.Error = 4
   return self.Error
  # -- closeSandhi_ans
  #  print "Do you want to exercise close sandhi options?\n";
  #  print ""N" or "n" to decline\n";
  #  print ""Y" or "y" to accept\n";
  #  print ""S" or "s" to follow standard editorial practice\n";
  #  print "Any other character to select options individually: ";
  #  readln(Answer);
  Answer = closeSandhi_ans.upper()
  if Answer == "":
   Answer = "?"
  if Answer == "Y":
   self.TukPadantat = True # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
   self.ScharSchari = True # PMS 8.3.36.  vA Sari
   self.XkXpKupvoh = True  # PMS 8.3.37.  kupvoH XkXpau ca.
   self.ChAti = True # PMS 8.4.63.  SaS cho "Ti. (jhayaH 62, anyatarasyAm 62)
   self.ParaSavarna = True # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
   self.Anunasika = True # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
  elif Answer == "N":
   self.TukPadantat = False
   self.ScharSchari = False
   self.XkXpKupvoh = False
   self.ChAti = False
   self.ParaSavarna = False
   self.Anunasika = False
  elif Answer == "S":
   if self.Compound:
    # PMS Close sandhi within compounds
    self.TukPadantat = True # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
    self.ScharSchari = True # PMS 8.3.36.  vA Sari
    # PMS technically, 8.3.37 should also apply but it is never seen
    self.ChAti = True # PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
    self.ParaSavarna = True # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
    self.Anunasika = True # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
    # PMS display standard editorial practice for compound sandhi
   else:
    # PMS External: 8.4.63 and 8.4.45
    self.ChAti = True # PMS 8.4.63.  SaS cho "Ti. (jhayaH 62, anyatarasyAm 62)
    self.Anunasika = True # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)

     # print "The optional sandhi in the following sutras will apply:\n";
     # print "  8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
     # print "  8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62 ) . \n";
     # PMS disabled Close sandhi between upasargas and their following verb forms
     # PMS CloseUpasargaSandhi = true;
     # PMS print "Close sandhi will be observed between upasargas and their following verb forms\n";
     # PMS print "After the upasarga "sam",\n";
     # PMS print "  8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
  else:   #  non-functioning. old code shown for possible reuse elsewhere
   # PMS peruse options
   # print "Choose sandhi options ("Y" or "y" to accept):\n";
   # print "6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71).\n";
   # print "  Pada final long vowel augmented with c before ch ? ";
   #   readln(Answer);
   #   if ( Answer eq "" ) {
   # Answer = "?";
   #   }
   #   if (Answer eq "Y") {
   # TukPadantat = true;
   #   }
   #   //print "8.3.36.  vA Sari.\n";
   #   print "  S, z or s before palatal, retroflex or dental stop respectively? ";
   # //  readln(Answer);
   #   if ( Answer eq "" ) {
   # Answer = "?";
   #   }
   #   if (Answer eq "Y") {
   # ScharSchari = true;
   #   }
   #   print "8.3.37.  kupvoH XkXpau ca.\n";
   #   print "   jihvamuliya, upadhmaniya before gutteral or labial stop respectively? ";
   # //  readln(Answer);
   #   if ( Answer eq "" ) {
   # Answer = "?";
   #   }
   #   if (Answer eq "Y") {
   # XkXpKupvoh = true;
   #   }
   #   print "8.4.63.  SaS cho "wi . (jhayaH 62, anyatarasyAm 62\n";
   #   print " ch after stops ? ";
   # //  readln(Answer);
   #   if ( Answer eq "" ) {
   # Answer = "?";
   #   }
   #   if (Answer eq "Y") {
   # ChAti = true;
   #   }
   #   print "8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
   #   print "  AnusvAra  stop homogenous with following stop? ";
   # //  readln(Answer);
   #   if ( Answer eq "" ) {
   # Answer = "?";
   #   }
   #   if (Answer eq "Y") {
   # ParaSavarna = true;
   #   }
   #   print "8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
   #   print "(At present the program does not handle nasalized semivowels)\n";
   #   print "(which, though rarely found in editions, go with this sandhi.)\n";
   #   print "  Stops  corresponding nasal before a nasal? ";
   # //  readln(Answer);
   #   if ( Answer eq "" ) {
   # Answer = "?";
   #   }
   #   if (Answer eq "Y") {
   # Anunasika = true;
   #   }
   #   if ( (not ParaSavarna) or (not Anunasika) ) {
   # print " Do you want to observe close sandhi after upasargas ? ";
   # //   readln(Answer);
   # if ( Answer eq "" ) {
   #  Answer = "?";
   # }
   # if (Answer eq "Y") {
   #  CloseUpasargaSandhi = true;
   # }
   #   }
   #   print "The optional sandhi in the following sutras will apply:\n";
   #   if ( TukPadantat ) {
   # print "  6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71).\n";
   #   }
   #   if ( ScharSchari ) {
   # print "  8.3.36.  vA Sari.\n";
   #   }
   #   if ( XkXpKupvoh ) {
   # print "  8.3.37.  kupvoH XkXpau ca.\n";
   #   }
   #   if ( ChAti ) {
   # print "  8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62 ) . \n";
   #   }
   #   if ( ParaSavarna ) {
   # print "  8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
   #   }
   #   if ( Anunasika ) {
   # print "  8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
   #   }
   #   if ( CloseUpasargaSandhi ) {
   # //PMS close upasarga sandhi
   # print "Close sandhi will be observed after upasargas\n";
   # if ( not ParaSavarna ) {
   #  print "After the upasarga "sam",\n";
   #  print "  8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
   #  }
   # if ( not Anunasika ) {
   #  print "After the upasarga "ud",\n";
   #  print "  8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
   #  }
   # } //PMS close upasarga sandhi
   self.Error = 4
   return (self.Error) # PMS peruse options
  # PMS Choose spacing options
  if self.Compound:
   #   print "Hyphens will be deleted between compound elements.\n";
   pass 
  elif self.External:
   # PMS spaceoptions
   #   print "Spaces will be deleted where a single vowel replaces final and initial vowels.\n";
   #   print "Do you wish to eliminate spaces between prefixes and verbs\n";
   #   print "and between final consonants and a following sound?\n";
   #   print "Y/y (yes) to delete spaces, any other character to keep.";
   #   readln(Answer);
   Answer = despace_ans
   #   Answer = "Y"; //force despacing
   if Answer == "":
    Answer = "N" # July 27, 2015 was "?"
   if Answer == "Y":
    self.Despace = True
   elif Answer == "N":
    self.Despace = False
   else:
    self.Error = 4
    return (self.Error)
  # PMS spaceoptions
  self.Error = 0
  return self.Error

 @wrapper
 def lengthary(self):
  """ method lengthary
   return position in Linary of the last character which is not a space;
   return 0 if all elements of Linary are spaces.
  """
  I = self.linmax

  while 1 <= I:
   if not (self.Linary[I] == " "):
    return I
   I -= 1
  return 0

 @wrapper
 def nxtposary(self, chtr, istart):
  """ method nxtposary  
  July 27, 2015. Removed fldch parameter as it never used
  Searches Linary for character chtr Returns of match.
  Discounts trailing spaces.
  @param chtr
  @param istart
  @return Returns -1 if istart is < 1 or > linmax
       Aug 7, 2015: Also return 0 instead of -1 in above case
   Returns 0 if no match found in Linary
   Returns index (istart to linmax) of first match found.
  """
  if istart < 1:
   return 0 #-1
  if istart > self.linmax:
   return 0 #-1
  IEnd = self.lengthary()

  if IEnd == 0:
   return 0
  I = istart
  while I <= IEnd:
   if self.Linary[I] == chtr:
    return I
   I += 1
  return 0

 @wrapper
 def lastposary(self, chtr, istart):
  """ method lastposary
  Searches backward in Linary for first occurrence of given character
  @param chtr character to search for
  @param istart starting position
  @return return -1 if istart is inappropriate
  ejf: Aug 7, 2015: Also return 0 if istart is inappropriate
  return 0 if chtr not found in Linary
  return I if nearest occurrence (from istart down to 1) of chtr is
  at index I
  """
  if istart < 1:
   return 0 # -1 #ejf
  if istart > self.linmax:
   return 0 # -1 #ejf

  I = istart
  while 1 <= I:
   if self.Linary[I] == chtr:
    return I
   I -= 1
  return 0

 #@wrapper
 def insertary(self, chtr, index):
  """ method insertary
  Insert character at given position in Linary.
  If the position is prior to first position, it resets to first position
  If position is after the last non-space position, it resets to first ending
  non-space position.
  Linary may be augmented by spaces, if necessary. Thus NoSpace will not be set to true.
  @param chtr character to insert
  @param index position of insertion
   """
  # Linary is a Python list, use the insert method.
  # Various 'error checking' is skipped.
  self.Linary.insert(index,chtr)
  self.linmax = self.linmax+1
  #self.NoSpace = False

 @wrapper
 def deletary(self, index):
  """ method deletary
  remove the character at position 'index' from Linary.
  If index indexes a position after the last non-space, no character is deleted
  @param index
  """
  IEnd = self.lengthary()
  if (index >= 1) and (index <= IEnd):
   I = index
   while I < IEnd:
    self.Linary[I] = self.Linary[I + 1]
    I += 1
   self.Linary[IEnd] = ""

 @wrapper
 def substrary(self, index1, index2):
  """ method substrary
  Returns a substring of Linary consisting of (index1-index2)+1 characters beginning at index1
  @param index1
  @param index2
  @return
  """
  Tempstr = []
  ans = ""
  IEnd = self.lengthary()
  if (index1 < 1) or (index1 > index2) or (index2 > IEnd):
   return ans
  if ((index2 - index1) + 1) > pratipadmax:
   return ans

  I = index1
  while I <= index2:
   Tempstr.append(self.Linary[I])
   I += 1

  ans = "".join(Tempstr)
  return ans

 @wrapper
 def rlvarnayormithahsavarnyam(self):
  """ method rlvarnayormithahsavarnyam
  {1.1.9 vt. fkAra kArayoH savarRavidhiH}
  A Preparation routine.
  (fFxX,fFxX) -> (f,f)
  uses globals Linary,Index.
  May modify Linary,Isthana1,Isthana2
  """
  if (set_memberP(self.Linary[self.Index - 1], Rvarna_and_Lvarna)) and (set_memberP(self.Linary[self.Index + 1], Rvarna_and_Lvarna)):
   self.Linary[self.Index - 1] = sktri
   self.Linary[self.Index + 1] = sktri
   self.Isthana1 = imurdhanya  # for Lvarna, which appear as idantya in Soundary
   self.Isthana2 = imurdhanya

 @wrapper
 def akahsavarnedirghah(self):
  """ method akahsavarnedirghah
  {6.1.101.  akaH savafRe dIrghaH}
  (aA,aA) -> (A,), (iI,iI) -> (I,), (uU,uU) -> (U,), (f,f) -> (F,).
  Also, EkahPurvaParayoh -> True
  Uses globals Linary,Index,Isthana1
  Modifies Linary,EkahPurvaParayoh
  """
  self.Linary[self.Index - 1] = Soundary[self.Isthana1][idirgha]
  self.deletary(self.Index + 1) # {6.1.84.  ekaH pUrvaparayoH}
  self.EkahPurvaParayoh = True

 @wrapper
 def vrddhireci(self):
  """ method vrddhireci
  6.1.88.  vfddhir eci
  (aA,eEoO) -> (vfdDi of eEoO,), and set EkahPurvaParayoh
   NOTE: vfdDi of eEoO == {E,E,O,O}
  Uses globals Linary,Index,Isthana2
  Modifies Linary,EkahPurvaParayoh
  """
  self.Linary[self.Index - 1] = Soundary[self.Isthana2][ivrddhi]
  self.deletary(self.Index + 1) # {6.1.84.  ekaH pUrvaparayoH}
  self.EkahPurvaParayoh = True

 @wrapper
 def adgunah(self):
  """ method adgunah
  6..1.87.  Ad guRaH
  (aA,iIuU) -> (guna of iIuU,) 
  (aA,fF) -> (a,r) 
  (aA,xX) -> (a,l)
  Note: guna of iIuU == {e,e,o,o}
  Also, set EkahPurvaParayoh
  Uses globals Linary,Index,Isthana2
  Modifies Linary,EkahPurvaParayoh
  """
  self.Linary[self.Index - 1] = Soundary[self.Isthana2][iguna]
  if (self.Isthana2 == italavya) or (self.Isthana2 == iosthya):
   self.deletary(self.Index + 1) # {6.1.84.  ekaH pUrvaparayoH}
  elif self.Isthana2 == imurdhanya: # imurdhanya:
   self.Linary[self.Index + 1] = sktr # {1.1.51.  uraR raparaH}
  elif self.Isthana2 == idantya: # idantya:
   self.Linary[self.Index + 1] = sktl
  self.EkahPurvaParayoh = True

 @wrapper
 def ikoyanaci(self):
  """ method ikoyanaci
  6.1.77.  iko yaR aci
  (iI,[aAuUfFxXeEoO]) -> (y,_)
  (uU,[aAiIfFxXeEoO]) -> (v,_)
  (fF,[aAiIuUxXeEoO]) -> (r,_)
  (xX,[aAiIuUfFeEoO]) -> (l,_)

  Uses globals Linary,Index,Isthana1
  Modifies Linary
  """
  self.Linary[self.Index - 1] = Soundary[self.Isthana1][iantahstha]

 @wrapper
 def enahpadantadati(self):
  """ method enahpadantadati
  6.1.109.  eNaH padAntAd ati
  (eo,a) -> (eo,')
  Uses globals Linary,Index
  Modifies Linary
  """
  self.Linary[self.Index + 1] = sktavagraha

 @wrapper
 def ecoyavayavah(self):
  """ method ecoyavayavah
  6.1.78.  eco 'yavAyAvaH
  (eEoO,AiIuUfFxXeEoO):
  (e,[AiIuUfFxXeEoO]) -> (ay,_)
  (o,[AiIuUfFxXeEoO)) -> (av,_)
  (E,[AiIuUfFxXeEoO)) -> (Ay,_)
  (O,[AiIuUfFxXeEoO)) -> (Av,_)
  Uses globals Linary,Index
  Modifies Linary,Index.
  """
  if self.Linary[self.Index - 1] == skte:
   self.Linary[self.Index - 1] = skta
   self.insertary(skty, self.Index)
  elif self.Linary[self.Index - 1] == skto:
   self.Linary[self.Index - 1] = skta
   self.insertary(sktv, self.Index)
  elif self.Linary[self.Index - 1] == sktai:
   self.Linary[self.Index - 1] = sktaa
   self.insertary(skty, self.Index)
  elif self.Linary[self.Index - 1] == sktau:
   self.Linary[self.Index - 1] = sktaa
   self.insertary(sktv, self.Index)
  self.Index = self.Index + 1

 @wrapper  
 def acsandhi(self):
  """ method acsandhi
  Uses globals Linary,Index,Isthana1,Isthana2
  vowel + vowel
  # acsandhi makes no direct changes itself, but rather orchestrates
  # calls to other methods
  (aAiIuUfFxXeEoO,aAiIuUfFxXeEoO)
  (fFxX,fFxX) -> (f,f) rlvarnayormithahsavarnyam  (continue)
  (aA,aA) -> (A,) akahsavarnedirghah set EkahPurvaParayoh
  (iI,iI) -> (I,) akahsavarnedirghah
  (uU,uU) -> (U,) akahsavarnedirghah
  (f,f) -> (F,)   akahsavarnedirghah
  (aA,eEoO) -> (vfdDi of eEoO,)  vrddhireci set EkahPurvaParayoh
  (aA,iIuU) -> (guna of iIuU,)  adgunah set EkahPurvaParayoh
  (aA,fF) -> (a,r) adgunah set EkahPurvaParayoh
  (aA,xX) -> (a,l) adgunah set EkahPurvaParayoh
  
  (iI,[aAuUfFxXeEoO]) -> (y,aAuUfFxXeEoO) ikoyanaci
  (uU,aAiIfFxXeEoO) -> (v,aAiIfFxXeEoO) ikoyanaci
  (fF,aAiIuUxXeEoO) -> (r,aAiIuUxXeEoO) ikoyanaci
  (xX,aAiIuUfFeEoO) -> (l,aAiIuUfFeEoO) ikoyanaci

  (eo,a) -> (eo,')  enahpadantadati
  (e,AiIuUfFxXeEoO)) -> (ay,AiIuUfFxXeEoO) ecoyavayavah
  (o,AiIuUfFxXeEoO)) -> (av,AiIuUfFxXeEoO) ecoyavayavah
  (E,AiIuUfFxXeEoO)) -> (Ay,AiIuUfFxXeEoO) ecoyavayavah
  (O,AiIuUfFxXeEoO)) -> (Av,AiIuUfFxXeEoO) ecoyavayavah

  Modifies Linary,Index.
  Calls: rlvarnayormithahsavarnyam, akahsavarnedirghah,vrddhireci,
  adgunah,ikoyanaci,enahpadantadati,ecoyavayavah
  """
  
  self.rlvarnayormithahsavarnyam() # (fFxX,fFxX) changed to (f,f)
  cprev = self.Linary[self.Index - 1]
  cnext = self.Linary[self.Index + 1]
  # use cprev, cnext Jul 27, 2015
  # This is called when cprev and cnext are vowels (i.e., in set Ac)
  # Ac is disjoint union of Ak and Ec
  if set_memberP(cprev, Ak):  # cprev is non-diphthong vowel
   if (set_memberP(cnext, Ak)) and (self.Isthana1 == self.Isthana2):
    # This encompasses several cases.
    # (cprev,cnext) = (aA,aA), (iI,iI), (uU,uU), (fF,fF),
    # Lengthen cprev and remove cnext, and set EkahPurvaParayoh
    self.akahsavarnedirghah() # {6.1.101.  akaH savafRe dIrghaH}
   elif set_memberP(cprev, Avarna):
    # PMS: && cnext not in Avarna
    if set_memberP(cnext, Ec):
     # (cprev,cnext) = (aA,eEoO)
     # Replace cprev by vfdDi of eEoO, remove cnext,
     # and set EkahPurvaParayoh
     self.vrddhireci() # PMS: 6.1.88  vfddhir eci
    else:
     # PMS: cnext in Ik
     # (cprev,cnext) = (aA,iIuUfFxX)
     self.adgunah() # PMS: 6.1.87  Ad guRaH 
   else:
    # PMS: cprev in Ik && not savarna with cnext
    self.ikoyanaci() # PMS: 6.1.77.  iko yaR aci
  else: 
   # PMS: cprev in Ec 
   if (set_memberP(cprev, Ekn)) and (cnext == skta):
    self.enahpadantadati() # PMS: 6.1.109.  eNaH padAntAd ati
   else:
    # PMS: set_memberP(cprev,Ec) && set_memberP(cnext,Ic)
    self.ecoyavayavah() # PMS: 6.1.78.  eco "yavAyAvaH

 @wrapper
 def non_acsandhi(self):
  """ method non_acsandhi
   ejf refactored this code, which formerly was in sandhimain
   Consonant + (Consonant or Vowel or Linend)
   (kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzssh,
      ,.:;aAiIuUfFxXeEoOkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh) 
   (kKgGh,[any]) -> (g,[any]) jhalamjasonte
   (cCjJS,[any]) -> (j,[any]) jhalamjasonte
   (wWqQz,[any]) -> (q,[any]) jhalamjasonte
   (tTdD,[any]) -> (d,[any]) jhalamjasonte
   (pPbB,[any]) -> (b,[any]) jhalamjasonte
   (n,cCwWtT) -> (Ms,cCwWtT) naschavyaprasan (but not for ('praSAn',cCwWtT))
   (rs,r) -> (,r)  rori  (set Dhralopa)
   (a,[any]) -> (A,[any]) dhralope  (if Dhralopa)
   (i,[any]) -> (I,[any]) dhralope  (if Dhralopa)
   (U,[any]) -> (U,[any]) dhralope  (if Dhralopa)
   (As,aAiIuUfFxXeEoOgGNjJYqQRdDnbBmyrlvh) -> (Ay,_) bhobhago 
    or as ? or "Bos" or "Bagos" or "aGos", replace that 's' with 'y'
  """
  # PMS: 8.2.39.  jhalAM jaSo "nte
  self.jhalamjasonte()
  # PMS: 8.3.7.  naS chavy apraSAn
  self.naschavyaprasan()
  # PMS: 8.3.14.  ro ri  
  self.rori()
  # PMS: 6.3.111.  qhralope pUrvasya dIrgho "RaH
  self.dhralope()
  # PMS: 8.3.17.  bhobhagoaghoapUrvasya yo "Si
  self.bhobhago() 
  # PMS: 8.3.15.  kharavasAnayor visarjanIyaH
  self.kharavasanayor()
  # PMS: 8.3.20.  oto gArgyasya.  This cannot precede vowel sandhi
  self.otogargyasya()
  # PMS: 8.3.23.  mo "nusvAraH
  self.monusvarah()
  if not self.NoKNam:
   # ejf: This condition is ALWAYS TRUE. See comment in namohrasvad.
   # PMS: 8.3.32.  Namo hrasvAd aci NamuR nityam
   self.namohrasvad()
  # PMS: 8.3.34.  visarjanIyasya saH
  self.visarjaniyasyasah()
  if self.ScharSchari:
   # PMS: 8.3.36.  vA Sari
   self.vasari()
  # PMS: 8.3.41, 8.3.45 && 8.3.46 are apavAdas of 8.3.37
  # so they must precede it
  # PMS: 8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39)
  self.idudupadhasya()
  # PMS: 8.3 .45. nitya samAse "nutarapadasthasya
  self.nityamsamase()
  # PMS: 8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya
  self.atahkrkamikamsa()
  if self.XkXpKupvoh:
   # PMS: 8.3.37.  kupvoH XkXpau ca (khari 15).
   self.kupvohXkXpau()
  if not self.NoStoh:
   # PMS: 8.4.40.  stoH ScunA ScuH
   self.stohscunascuh()
   # PMS: 8.4.41.  zwunA zwuH
   self.stunastuh()
  # PMS: 8.4.60.  tor li
  self.torli()
  if self.ChAti:
   # PMS: 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
   self.saschoti()
  # PMS: 8.4.62.  jhayo ho "nyatarasyAm
  self.jhayoho()
  # PMS: 8.4.55.  khari ca
  self.kharica()
  if self.ParaSavarna or self.OtherCloseSandhi:
   # PMS: 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
   self.anusvarasya()

 @wrapper
 def visargaprep(self):
  """ method visargaprep
   Called once in sandhimain.
   (H,_)-> ({rs},_) Also, change Pada1
   
   Uses globals Pada1,Linary,Index
   Modifies Pada1,Linary
  """
  if (self.Linary[self.Index - 1] != sktvisarga):
   return # not applicable
  # choose replacement for H
  if self.Pada1 in visargaprep_exceptions_set:
   replace=sktr
  else:
   replace=skts
  # Pada1 is not empty, since it ends in 'H'. 
  L = len(self.Pada1) # So, L>0
  # make replacement in Linary and in Pada1
  self.Linary[self.Index - 1] = replace
  self.Pada1 = strReplace(self.Pada1, L - 1, L, replace)

 @wrapper
 def checa(self):
  """ method checa
   6.1.73.  che ca (tuk 71)
   ([aiufx],C) -> (_t,_)
   Uses globals Linary,Index,Iyatna1
   Modifies Linary,Index,Error
  """
  if (self.Linary[self.Index + 1] == sktch) and (self.Iyatna1 == ihrasva):
   self.insertary(sktt, self.Index)
   self.Index = self.Index + 1

 @wrapper
 def anmanosca(self):
  """ method anmanosca
   6.1.74.  ANmANoSca (che 73, tuk 71)
   (["A","mA"],C) ->(_t,_)
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index,Error
     PMS: you'll have to add the condition that these are AN && mAN
     when that info is available
  """
  if (self.Linary[self.Index + 1] == sktch) and ((self.Pada1 == "A") or (self.Pada1 == "mA")):
   self.insertary(sktt, self.Index)
   self.Index = self.Index + 1

 @wrapper
 def padantadva(self):
  """ method padantadva
   6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
   Requires option flag TukPadantat== True
   ([AIUFX],C) -> (_t,C)
   Uses globals Linary,Index,
   Modifies Linary,Index,Error,Isthana1,Iyatna1
  """
  # PMS: don"t want to do it if anmanosca just applied
  [self.Isthana1,self.Iyatna1] = identify(self.Linary[self.Index - 1])
  if (self.Linary[self.Index + 1] == sktch) and (self.Iyatna1 == idirgha):
   self.insertary(sktt, self.Index)
   self.Index = self.Index + 1

 @wrapper
 def etattadohsulopo(self):
  """ method etattadohsulopo
   6.1.132.  etattadoH sulopo "kor anaYsamAse hali
   Require self.Pronoun == True 
   (["sas","ezas"],[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh] -> ({"sa","ezas"},_)
   When Pada1 is sas or ezas, and Pada2 starts with constant, then
    the 's' is dropped from Pada1
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index
  """
  if not self.Pronoun:
   return
  if ((self.Pada1 == "sas") or (self.Pada1 == "ezas")) and (set_memberP(self.Linary[self.Index + 1], Hal)):
   self.deletary(self.Index - 1)
   self.Index = self.Index - 1

 @wrapper
 def amnarudharavar(self):
  """ method amnarudharavar
   8.2.70.  amnarUdharavarityubhayathA chandasi
   Requires Chandas option == True - (Vedic option = "Y")
   (["amnas","UDas","avas"],_) -> ({"amnar","UDar","avar"},_)
   Uses globals Linary,Index,Pada1
   Modifies Linary
  """
  if self.Chandas:
   if self.Pada1 in ["amnas","UDas","avas"]:
    # PMS: actually you get it both ways in chandas, ru too
    self.Linary[self.Index - 1] = sktr

 @wrapper
 def sasajusoruh(self):
  """ method sasajusoruh
   Uses globals Linary,Index
   Modifies Linary
   (_"sajuz",_) -> (_"sajus",_)
   If Pada1 ends with 'sajuz', change that 'z' to ru ('s')
   PMS: 8.2.66.  sasajuzo ruH
   PMS: exception to 8.2.39 so must apply before it
  """
  if self.Index > 5:
   if self.substrary(self.Index - 5, self.Index - 1) == "sajuz":
    self.Linary[self.Index - 1] = ru
  # this is odd, since ru and skts are both names for 's'
  if self.Linary[self.Index - 1] == skts:
   self.Linary[self.Index - 1] = ru

 @wrapper
 def ahan(self):
  """ method ahan
   8.2.68.  ahan
   Requires flag NoStoh == False  and External flag == True
   If then Pada1 is 'ahan', then 
    * that 'n' is changed to ru ('s') when Pada2 is in a list
    * otherwise that  'n' is changed to 'r'
     
   Uses globals Linary,Index,Pada1,Pada2
   Modifies Linary
  """
  if self.NoStoh:
   return
  if not self.Compound:
   return
  if self.Pada1 != "ahan":
   return
  if self.Pada2 in ["rUpa", "rAtri", "rAtra", "rAtre","rAtrARAm", "raTantara"]:
   # PMS: vArttika, but had to add rAtra 21045,
   # rAtre 24028, rAtrARAm 33137
   self.Linary[self.Index - 1] = ru
   # PMS: if ahan is termed pada && Pada2 in Sup, 
   # so that Linary[Index+1]=sktbh || skts, ditto
  else:
   self.Linary[self.Index - 1] = sktr # PMS: 8.2.69.  ro "supi

 @wrapper
 def atororhasica(self):
  """ method atororhasica
   6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca
   Must precede 6.1.109.  eNaH padAntAd ati
  (_"as",[agGNjJYqQRdDnbBmyrlvh]) ->(_o,_)
   When Pada1 ends in 'as' and Pada2 begins with one of
     "agGNjJYqQRdDnbBmyrlvh" (a soft consonant or 'a'),
     then change that 'as' to 'o'
   Uses globals Linary,Index
   Modifies Linary,Index
  """
  if self.Index > 2:
   if (self.Linary[self.Index - 2] == skta) and (self.Linary[self.Index - 1] == ru):
    if set_memberP(self.Linary[self.Index + 1], Hasch_and_skta):
     self.Linary[self.Index - 2] = skto # PMS: Linary[Index-1=sktu; adguna
     self.deletary(self.Index - 1)
     self.Index = self.Index - 1

 @wrapper
 def jhalamjasonte(self):
  """ method jhalamjasonte
   8.2.39.  jhalAM jaSo 'nte
   NOTE: Based on testsuite, the call to identify and reset of 
         Isthana1, Iyatna1 seems unneeded.
         However, it is neede in the example C "latA-Cada" 
   (kKgGh,[any]) -> (g,[any])
   (cCjJS,[any]) -> (j,[any])
   (wWqQz,[any]) -> (q,[any])
   (tTdD,[any]) -> (d,[any])
   (pPbB,[any]) -> (b,[any])

   Uses globals Linary,Index,Pada1
   Modifies Linary,Isthana1,Iyatna1
  """
  [self.Isthana1,self.Iyatna1] = identify(self.Linary[self.Index - 1])
  if set_memberP(self.Linary[self.Index - 1], Jhal_not_ru):
   # PMS: because ru =skts; I could choose another character
   self.Linary[self.Index - 1] = Soundary[self.Isthana1][isparsa3]
   # PMS: jhalamjasonte

 @wrapper
 def naschavyaprasan(self):
  """ method naschavyaprasan 
   8.3.7.  naS chavy apraSAn
   (n,cCwWtT) -> (Ms,cCwWtT)  (but not for ('praSAn',cCwWtT))
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index,Error
  """
  if (self.Linary[self.Index - 1] == sktn and (set_memberP(self.Linary[self.Index + 1], Chav)) and not (self.Pada1 == "praSAn")):
   self.Linary[self.Index - 1] = ru
   # PMS: 8.3.4.  anunAsikAt paro "nusvAraH
   self.insertary(sktanusvara, self.Index - 1)
   self.Index = self.Index + 1

 @wrapper
 def rori(self):
  """ method rori 
   8.3.14.  ro ri
   ([rs],r) -> (,r)  set Dhralopa flag to True.
   Note: This is the only place Dhralopa is set to True
   Uses globals Linary,Index
   Modifies Linary,Index,Dhralopa
  """
  self.Dhralopa = False
  if (set_memberP(self.Linary[self.Index - 1], sktr_and_ru)) and (self.Linary[self.Index + 1] == sktr):
   self.deletary(self.Index - 1)
   self.Index = self.Index - 1
   self.Dhralopa = True

 @wrapper
 def dhralope(self):
  """ method dhralope 
   6.3.111.  qhralope pUrvasya dIrgho 'RaH
   if Dhralopa: (this is only place where Dhralopa is a condition)
   (a,[any]) -> (A,[any])
   (i,[any]) -> (I,[any])
   (U,[any]) -> (U,[any])

   Uses globals Linary,Index,Dhralopa
   Modifies Linary
  """
  if self.Dhralopa:
   temp = identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   if (set_memberP(self.Linary[self.Index - 1], An)) and (self.Iyatna1 == ihrasva):
    self.Linary[self.Index - 1] = Soundary[self.Isthana1][idirgha]

 @wrapper
 def bhobhago(self):
  """ method bhobhago 
   8.3.17.  BoBagoaGoapUrvasya yo 'Si
   (_[aA]s,[aAiIuUfFxXeEoOgGNjJYqQRdDnbBmyrlvh]) -> (__y,_)  # Occurs with '_as' ?
   Similarly if Pada1 is Bos, Bagos, aGos, change 's' to 'y'
   (["Bos","Bagos","aGos"],[aAiIuUfFxXeEoOgGNjJYqQRdDnbBmyrlvh]]->({"Boy","Bagoy","aGoy"},_)
   Uses globals Linary,Index,Pada1
   Modifies Linary
  """
  if (set_memberP(self.Linary[self.Index + 1], Asch)) and (self.Index > 2):
   if self.Pada1 in ["Bos","Bagos","aGos"]:
    self.Linary[self.Index - 1] = skty
   elif (set_memberP(self.Linary[self.Index - 2], Avarna)) and (self.Linary[self.Index - 1] == ru):
    self.Linary[self.Index - 1] = skty

 @wrapper
 def kharavasanayor(self):
  """ method kharavasanayor 
   8.3.15.  kharavasAnayor visarjanIyaH
   ([rs],[  ,.:;kKcCwWtTpPSzs]) -> (H,_)
   ([rs],Not [  ,.:;kKcCwWtTpPSzs]) -> (r,_) 
   Uses globals Linary,Index
   Modifies Linary
  """

  if set_memberP(self.Linary[self.Index - 1], sktr_and_ru):
   if set_memberP(self.Linary[self.Index + 1], Khar_and_linend):
    self.Linary[self.Index - 1] = sktvisarga
   else:
    self.Linary[self.Index - 1] = sktr

 @wrapper
 def lopahsakalyasya(self):
  """ method lopahsakalyasya 
   8.3.19.  lopaH SAkalyasya
   (_[aA]y,[aAiIuUfFxXeEoOgGNjJYqQRdDnbBmyrlvh]) -> (__,_)  # drop the 'y'
   Uses globals Linary,Index
   Modifies Linary,Index
   Sep 5, 2015. Use lopah_v flag, to remove 'v' if this flag is True
   Sep 6, 2015. Use lopah_v flag, to remove 'v' if this flag is True AND if
                preceding vowel is 'a'.  This is to 
                force agreement with Bucknell.
   (_[aA]y,[aAiIuUfFxXeEoOgGNjJYqQRdDnbBmyrlvh]) -> (__,_)  # drop the 'y'
     and
   (_[a]v,[aAiIuUfFxXeEoOgGNjJYqQRdDnbBmyrlvh]) -> (__,_)  # drop the 'v'
                
                
  """
  if (set_memberP(self.Linary[self.Index + 1], Asch)) and (self.Index > 2):
   if (set_memberP(self.Linary[self.Index - 2], Avarna)) and (self.Linary[self.Index - 1] == skty):
    self.deletary(self.Index - 1)
    self.Index = self.Index - 1
   elif (set_memberP(self.Linary[self.Index - 2], [skta])) and (self.Linary[self.Index - 1] == sktv) and self.lopah_v:
    self.deletary(self.Index - 1)
    self.Index = self.Index - 1

 @wrapper
 def otogargyasya(self):
  """ method otogargyasya 
   8.3.20.  oto gArgyasya
   (["Bos","Bagos","aGos"],[aAiIuUfFxXeEoOgGNjJYqQRdDnbBmyrlvh]) -> ({"Bo","Bago","Ago"},_)
     Note: drop final 's' in Pada1
   Uses globals Linary,Index
   Modifies Linary,Index
  """
  if set_memberP(self.Linary[self.Index + 1], Asch):
   if self.Pada1 in ["Bos","Bagos","aGos"]:
    self.deletary(self.Index - 1)
    self.Index = self.Index - 1

 @wrapper
 def monusvarah(self):
  """ method monusvarah 
   8.3.23.  mo 'nusvAraH
   ([m],[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh]) -> (M,_)
   Uses globals Linary,Index
   Modifies Linary
  """
  if (self.Linary[self.Index - 1] == sktm) and (set_memberP(self.Linary[self.Index + 1], Hal)):
   self.Linary[self.Index - 1] = sktanusvara

 @wrapper
 def namohrasvad(self):
  """ method namohrasvad 
   8.3.32.  Namo hrasvAd aci NamuR nityam
   Requires NoKNam flag == False
   ([aiufx][NRn],[aAiIuUfFxXeEoO]) -> (__{NRn},_)  (double last char Pada1)
   ejf:  NoKNam is set to True only in sandhiPrep routine, and only for
       Pada1 == "Ayan" or "Gan" and only when PaninianText is True.
       HOWEVER, PaninianText is never set to True !!.  Thus, NoKNam is
       ALWAYS FALSE, and is thus the condition (of sandhimain) 
       'If not self.NoKNam' is ALWAYS TRUE, and thus unneeded
   Uses globals Linary,Index
   Modifies Linary,Index,Error
  """

  if (self.Index > 2):
   temp = identify(self.Linary[self.Index - 2])
   Sthana = temp[0]
   Yatna = temp[1]
   if (Yatna == ihrasva) and (set_memberP(self.Linary[self.Index - 1], KNam)) and (set_memberP(self.Linary[self.Index + 1], Ac)):
    # ejf: By assumption, Isthana1,Iyatna1 refers to the last letter in
    # Pada1, namely [NRn] (== KNam).  And iyatna1 == isparsa5 for N,R,n.
    # Thus, Soundary[self.Isthana1][isparsa5] is just the last letter of
    # Pada1, and the next statement indicates to double this last letter.
    self.insertary(Soundary[self.Isthana1][isparsa5], self.Index)
    self.Index = self.Index + 1

 @wrapper
 def visarjaniyasyasah(self):
  """ method visarjaniyasyasah 
   8.3.34.  visarjanIyasya saH
   (H,[kKcCwWtTpPSzs]) -> ({s},_) UNLESS
     (a) 2nd char of Pada2 is [Szs] or
     (b) 1st char of Padad2 is [kKgGNpPbBmSzs]
    In other words, that H becomes 's' when
     (a1) Pada2 starts with [cCwWtT] and 
     (b1) 2nd char of Pada2 is not [Szs]
         Note: No words in mw start [cCwW][Szs]. However,
         tsaru satisfies a1,b1 so rAmaH tsaruH is unchanged (rule does
         not apply).
   Uses globals Linary,Index
   Modifies Linary
  """
  Apavada = False
  if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Khar)):
   Apavada = False
   if (self.Index + 2) < self.linmax:
    if set_memberP(self.Linary[self.Index + 2], Schar):
     Apavada = True # PMS: 8.3.35.  Sarpare visarjanIyaH.
   if set_memberP(self.Linary[self.Index + 1], Ku_and_Pu_and_Schar):
    Apavada = True # PMS: 8.3.36.  vA Sari.  8.3.37.  kupvoH XkXpau ca.
   if not (Apavada):
    self.Linary[self.Index - 1] = skts

 @wrapper
 def vasari(self):
  """ method vasari 
   8.3.36.  vA Sari
   Requires option ScharSchari  == True (close Sandhi or standard practice)
   (H,[Szs]) -> (s,_)
   Uses globals Linary,Index
   Modifies Linary
  """
  if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Schar)):
   self.Linary[self.Index - 1] = skts

 @wrapper
 def kupvohXkXpau(self):
  """ method kupvohXkXpau 
    8.3.37.  kupvoH XkXpau ca (khari 15).
    8.3.41, 8.3.45 && 8.3.46 are apavAdas of this so must precede it.
   Requires option XkXpKupvoh==True (close sandhi = "Y").  This is
   rare.  The visarga is changed to one of the non-ascii characters
   sktjihvamuliya (Z) or sktupadhmaniya(V)
   (H,[kKcCwWtTpPSzs][NOT Szs]) 
   (H,[kK]) -> (Z,_)
   (H,[pP]) -> (V,_)
   Uses globals Linary,Index
   Modifies Linary
  """
  # PMS: by 8.3.15, kharavasAnayorvisarjanIyaH, visarga occurs
  # before avasAna too.  but Xk && Xp don't.
  if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Khar)):
   # PMS: Hence, khari is understood here too
   Apavada = False
   if (self.Index + 2 < self.linmax):
    if set_memberP(self.Linary[self.Index + 2], Schar):
     Apavada = True # PMS: 8.3.35.  Sarpare visarjanIyaH.
   if not (Apavada):
    if set_memberP(self.Linary[self.Index + 1], Ku):
     self.Linary[self.Index - 1] = sktjihvamuliya
    elif set_memberP(self.Linary[self.Index + 1], Pu):
     self.Linary[self.Index - 1] = sktupadhmaniya

 @wrapper
 def idudupadhasya(self):
  """ method idudupadhasya 
   8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39
   (H,[kKgGNpPbBm]) -> (z,_) provided
    Pada1 is one of  ["nis","dus","bahis","Avis","catur","prAdur"]
   Note: The condition 'H' refers to Linary[Index-1], which sometimes
     differs from Pada1. For example, with 'nis kuru', the 's' is changed
     to 'H' by kharavasanayor, so this method changes to 'niz kuru'.
     But 'nis guru' changes to 'nir guru' by kharavasanayor, so this
     method does not even apply.
   Uses globals Linary,Index,Pada1
   Modifies Linary
   PMS: exception to 8.3.36.  kupvoH XkaXpau ca, 
        which is an exception to 8.3.34. visarjanIyasya saH,
        so should accompany procedure visarjaniyasyasah.  
        Must follow 8.3.15.  kharavasAnayor visarjanIyaH
  """
  if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Ku_and_Pu)):
   if self.Pada1 in ["nis","dus","bahis","Avis","catur","prAdur"]:
    self.Linary[self.Index - 1] = sktsh # PMS: bahis, Avis =exception to 8.3.46

 @wrapper
 def nityamsamase(self):
  """ method nityamsamase 
   8.3.45. nityamsamAse 'nutarapadasthasya
   Requires option Compound == True
   ([iu]H,[kKgGNpPbBm]) -> ([iu]z,_) provided Uttarapada flag is False.
   example: C guruBiH-kftaH
   Uses globals Linary,Index
   Modifies Linary
  """
  if self.Compound:
   if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Ku_and_Pu)) and (self.Index > 2):
    if ((self.Linary[self.Index - 2] == skti) or ((self.Linary[self.Index - 2] == sktu) and (not self.Uttarapada))):
     # PMS: Pada1-u.p. [SOFT HYPHEN]
     self.Linary[self.Index - 1] = sktsh

 @wrapper
 def atahkrkamikamsa(self):
  """ method atahkrkamikamsa 
   8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya (samAse 45)
   Requires option Compound==True and flag  Uttarapada==False.
   (aH,[kKgGNpPbBm]) -> (as,_) provided 
     - Pada2  is one of ["kAra","kAma","kaMsa","kumBa","kumBI","pAtra",
                         "kuSA","karRI"]
     - Pada1 is not one of ["svar","antar","prAtar","punar","sanutar",
                            "hyas","Svas","avas","aDas"]
   ejf note: The condition on Pada2 prevents Pada2 from being an 
    inflected form. Is this intended?
   Uses globals Linary,Index,Pada1,Pada2
   Modifies Linary
  """
  if self.Compound:
   if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Ku_and_Pu)) and (self.Index > 2):
    if (self.Linary[self.Index - 2] == skta):
     if self.Pada2 in ["kAra","kAma","kaMsa","kumBa","kumBI","pAtra","kuSA","karRI"]:
      if self.Pada1 not in ["svar","antar","prAtar","punar","sanutar","hyas","Svas","avas","aDas"]:
       if not self.Uttarapada:
        self.Linary[self.Index - 1] = skts
  # PMS: miTas, namas, (tiraskAra by 8.3.42.  avaskara, namaskAra?)
  # krtvasuc, suc, i.e. not avyaya

 @wrapper
 def stohscunascuh(self):
  """ method stohscunascuh 
   8.4.40.  stoH ScunA ScuH
   Requires flag NoStoh== False  
   - ([tTdDns],[cCjJYS]) -> ({cCjJYS},_)
   - ([cCjJYS],s) -> (_,S)
   - ([cCjJY],[tTdDn]) -> (_,{cCjJY})
   - ([cCjJY],[tTdDn][tTdDns]) -> (_,{cCjJY}{cCjJYS}
      NOTE: Can't think of any Pada2 examples here
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  Isthana = 0
  Iyatna = 0
  if (set_memberP(self.Linary[self.Index - 1], Tu_and_skts)) and (set_memberP(self.Linary[self.Index + 1], Cu_and_sktsch)):
   temp = identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index - 1] = Soundary[italavya][self.Iyatna1]
  elif (set_memberP(self.Linary[self.Index - 1], Cu_and_sktsch)) and (self.Linary[self.Index + 1] == skts):
   self.Linary[self.Index + 1] = sktsch # ?
   if (self.Index + 2 < self.linmax):
    if self.Linary[self.Index + 2] == skts:
     self.Linary[self.Index + 1] = sktsch
  elif (set_memberP(self.Linary[self.Index - 1], Cu)) and (set_memberP(self.Linary[self.Index + 1], Tu)):
   # PMS: 8.4.44.  SAt. (na, toH)
   temp = identify(self.Linary[self.Index + 1])
   self.Isthana2 = temp[0]
   self.Iyatna2 = temp[1]
   self.Linary[self.Index + 1] = Soundary[italavya][self.Iyatna2]
   if (self.Index + 2 < self.linmax):
    if set_memberP(self.Linary[self.Index + 2], Tu_and_skts):
     temp = identify(self.Linary[self.Index + 2])
     Isthana = temp[0]
     Iyatna = temp[1]
     self.Linary[self.Index + 2] = Soundary[italavya][Iyatna]

 @wrapper
 def stunastuh(self):
  """ method stunastuh 
   8.4.41.  zwunA zwuH
   Assumes flag NoStoh==False
   (z,[tTdDns][tTdDns]) -> (_,{wWqQRz}{wWqQRz})
   (z,[tTdDns]) -> (_,{wWqQRz})
    NOTE: How can S ever end Pada2 AT THIS POINT, given sandhiPrep, etc. ?
   ([wWqQR],"nAm") -> (_,"RAm")
   ([tTdDn],[wWqQR]) -> ({tTdDn},_)
   (s,[wWqQRz]) -> (z,_)
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  if ((self.Linary[self.Index - 1] == sktsh) and (set_memberP(self.Linary[self.Index + 1], Tu_and_skts))) or (set_memberP(self.Linary[self.Index - 1], Retrotu) and (self.Pada2 == "nAm")):
   # PMS: 8.4.42.  na padAntAwworanAm
   temp = identify(self.Linary[self.Index + 1])
   self.Isthana2 = temp[0]
   self.Iyatna2 = temp[1]
   self.Linary[self.Index + 1] = Soundary[imurdhanya][self.Iyatna2]
   if (self.Index + 2 < self.linmax):
    if set_memberP(self.Linary[self.Index + 2], Tu_and_skts):
     temp = identify(self.Linary[self.Index + 2])
     Isthana = temp[0]
     Iyatna = temp[1]
     #self.Linary[self.Index + 1] = Soundary[imurdhanya][self.Iyatna2]  # redundant
     self.Linary[self.Index + 2] = Soundary[imurdhanya][Iyatna]
  elif (set_memberP(self.Linary[self.Index - 1], Tu) and (set_memberP(self.Linary[self.Index + 1], Retrotu))) or ((self.Linary[self.Index - 1] == skts) and (set_memberP(self.Linary[self.Index + 1], Retrotu_sktsh))):
   # PMS: 8.4.43.  toH zi. (na)
   temp = identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index - 1] = Soundary[imurdhanya][self.Iyatna1]

 @wrapper
 def anusvarasya(self):
  """ method anusvarasya 
   8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58)
   PMS: don"t exercise the option for semivowels (yan) just now
   Requires: option ParaSavarna == True or OtherCloseSandhi == True
   [M,[kKgGNcCjJYwWqQRtTdDnpPbBm]) -> ({NYRnm},_)
   Uses globals Linary,Index
   Modifies Linary,Isthana2,Iyatna2
  """
  if (self.Linary[self.Index - 1] == sktanusvara) and (set_memberP(self.Linary[self.Index + 1], Yay_not_Yan)):
   temp = identify(self.Linary[self.Index + 1])
   self.Isthana2 = temp[0]
   self.Iyatna2 = temp[1]
   self.Linary[self.Index - 1] = Soundary[self.Isthana2][isparsa5]

 @wrapper
 def torli(self):
  """ method torli 
   8.4.60.  tor li
   ([tTdD],l) -> (l,l)
   (n,l) -> (~l,l)    See notes.org for question about the placement of nasalization
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Index,Error
  """
  if (set_memberP(self.Linary[self.Index - 1], Tu)) and (self.Linary[self.Index + 1] == sktl):
   temp = identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index - 1] = sktl
   if self.Iyatna1 == isparsa5:
    #self.insertary(sktnasalization, self.Index - 1)
    self.insertary(sktnasalization, self.Index) # ~ AFTER sktl
    self.Index = self.Index + 1

 @wrapper
 def jhayoho(self):
  """ method jhayoho 
   8.4.62.  jhayo ho 'nyatarasyAm
   ([kKgGcCjJwWqQtTdDpPbB],h) -> (_,{GJQDB})
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1
  """
  if (set_memberP(self.Linary[self.Index - 1], Jhay)) and (self.Linary[self.Index + 1] == skth):
   temp = identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index + 1] = Soundary[self.Isthana1][isparsa4]

 @wrapper
 def saschoti(self):
  """ method saschoti 
   8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
   Only when option ChAti == True.
   ([kKgGcCjJwWqQtTdDpPbB],S[aAiIuUfFxXeEoOyrvh]) -> (_,C_)
   Uses globals Linary,Index
   Modifies Linary
  """
  if (set_memberP(self.Linary[self.Index - 1], Jhay)) and ((self.Index + 2) < self.linmax):
   if (self.Linary[self.Index + 1] == sktsch) and (set_memberP(self.Linary[self.Index + 2], At)):
    # PMS: vt. chatvamamIti vaktavyam:  
    # Am instead of At.  tacchlokena, tacchmaSruRA
    self.Linary[self.Index + 1] = sktch

 @wrapper
 def yaronunasike(self):
  """ method yaronunasike 
   8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
   Requires option Anunasika == True OR OtherCloseSandhi == True
   ([kKgGcCjJwWqQtTdDpPbB],[NYRnm]) ->({NYRnm},_)
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  [self.Isthana2,self.Iyatna2] = identify(self.Linary[self.Index + 1])
  # PMS: if ( set_memberP(Linary[Index - 1],Yar) && (Index + 2 < linmax) then
  # PMS: if (Iyatna2 eq isparsa5) || (Linary[Index + 2] == sktanunasika ) {
  # PMS: we won't exercise the nasalized option for the semivowels 
  #      y, v && l; just for the stops
  if (set_memberP(self.Linary[self.Index - 1], Jhay)) and (self.Iyatna2 == isparsa5):
   [self.Isthana1,self.Iyatna1] = identify(self.Linary[self.Index - 1])
   self.Linary[self.Index - 1] = Soundary[self.Isthana1][isparsa5]

 @wrapper
 def kharica(self):
  """ method kharica 
   8.4.55.  khari ca. (jhalAm 53, car 54)
   PMS: there is no final  "h" after jhalAm jaSo "nte, 
     but there is skts by 8.3.34 visarjanIyasya saH
     && sktsch && sktsh by 
     8.4.40-41 stoH ScunA scuH, zwunA zwuH so must exclude Sar
   ([kKgGcCjJwWqQtTdDpPbB],[ ,.:;kKcCwWtTpPSzs]) -> ({kcwtp},_)
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1
  """
  if set_memberP(self.Linary[self.Index - 1], Jhay):
   # PMS: jhay=jhal-Sar
   temp = identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   if set_memberP(self.Linary[self.Index + 1], Khar_and_linend):
    # PMS: 8.4.56.  vavasane
    self.Linary[self.Index - 1] = Soundary[self.Isthana1][isparsa1]

 @wrapper
 def idudeddvivacanampragrhyam(self):
  """ method idudeddvivacanampragrhyam 
   1.1.11. IdUdeddvivacanam pragfhyam
   Requires option External == True
   if Pada1 is in pragrhya_set, set Pragrhya flag == True
   Uses globals Linary,Index,Pada1
   Modifies Linary,Pragrhya
  """
  # PMS: 1.1.11. IdUdeddvivacanam pragfhyam
  if self.External and self.Pada1 in pragrhya_set:
   self.Pragrhya = True

 def _sandhiPrepException(self):
  """ extracted from sandhiPrep
      Uses module variable sandhi_exceptions_set for efficiency
      Sets Exception flag
  """
  if self.Pada1 in sandhi_exceptions_set:
   self.Exception = True
  else:
   self.Exception = False
  return self.Exception

 def _sandhiPrepNoPrep(self):
  """ extracted from sandhiPrep
      NoPreps could be made a Module variable, for efficiency
      Returns a Boolean; may set NoStoh flag.
  """
  if self.Pada1 in CAntaPadary_set:
   NoPrep = True
   self.NoStoh = True  # extra condition
  elif self.Pada1 in sandhi_noprep_set:
   NoPrep = True
  else:
   NoPrep = False
  return NoPrep

 @wrapper 
 def sandhiPrepCompoundAdjust(self):
  """ Make adjustments to Linary and Index.
     Assumes flag Compound == True
     Changes are based on Pada1 (but Pada1 itself is not changed)
     "aYc" -> "ak"
     _c -> _k
     _C -> _k
     "rAj" -> "rAw"
     _j -> _k
     _J -> _k
     _[ai]n -> __  unless (a) Pada1 == "ahan", or (b) PurvaPada == "eka" (?)
     "pur" -> "pUr"
     "dur" -> "dUr"
     "viS" -> "viw"
     _S -> _k
     "daDfz" -> "daDfk"
     "ASis" -> "ASIs"
     "pums" -> "pum"

  """
  # c is last character of Pada1
  c = self.Linary[self.Index - 1]
  if c == sktc:
   if self.Pada1 == "aYc":
    # PMS: aYc -> ak
    self.Linary[self.Index - 1] = sktk 
    self.deletary(self.Index - 2)
    self.Index = self.Index - 1
   else: # change that 'c' to 'k'
    self.Linary[self.Index - 1] = sktk
  elif c == sktch: # change that 'C' to 'k'
   self.Linary[self.Index - 1] = sktk
  elif c == sktj:
   if (self.Pada1 == "rAj"): # change that 'j' to 'w'
    self.Linary[self.Index - 1] = sktretrot
   else: # change that 'j' to 'k'
    self.Linary[self.Index - 1] = sktk
  elif c == sktjh: # change that 'J' to 'k'
   self.Linary[self.Index - 1] = sktk
  elif c == sktn:
   if self.Index > 2:
    if (self.Linary[self.Index - 2] == skta) or (self.Linary[self.Index - 2] == skti):
     # PMS: an-/in-
     if ((self.Pada1 == "ahan") and (not self.PurvaPada == "eka")):
      #  noop
      pass
     else:
      # PMS: normal "an-"/"in-"
      # ejf; "Xan-" -> "Xa-", "Xin-" -> "Xi-"  (X anything)
      self.deletary(self.Index - 1)  
      self.Index = self.Index - 1
    # PMS: an-/in- (end)
  elif c == sktr:
   if (self.Pada1 == "pur") or (self.Pada1 == "Dur"):
    self.Linary[self.Index - 2] = sktuu  # penultimate "u" -> "U"
  elif c == sktsch:
   if self.Pada1 == "viS": # that 'S' -> 'w'
    self.Linary[self.Index - 1] = sktretrot
   else: # that 'S' -> 'k'
    self.Linary[self.Index - 1] = sktk
  elif c == sktsh:
   if self.Pada1 == "daDfz": # that 'z' -> 'k'
    self.Linary[self.Index - 1] = sktk
  elif c == skts:
   if (self.Pada1 == "ASis"):  # ASis -> ASIs
    self.Linary[self.Index - 2] = sktii # PMS: 82104
   elif self.Pada1 == "pums":
    # PMS: "pum"  
    # "pums" -> "pum"
    self.deletary(self.Index - 1)
    self.Index = self.Index - 1

 def sandhiPrep(self):
  """ method sandhiPrep 
      This routine inadequately documented
      This routine modifies various flags (either directly, or by calls to other methods.
      NoStoh, NoKNam, Pronoun, OtherCloseSandhi, Exception
      Also, adjusts Linary based on Pada1. This done in sandhiPrepCompoundAdjust
  """
  #
  # Part 0: initialze some instance flags
  #
  self.NoStoh = False
  self.NoKNam = False
  self.Pronoun = True # PMS: saú is usually the pronoun tad [LATIN SMALL LETTER U WITH ACUTE]
  self.OtherCloseSandhi = False
  #self.Exception = False # set in _sandhiPrepException()

  # return if Pada1 empty or 1 character (probably never occurs?)
  if len(self.Pada1) <= 1:
   return  
  #
  # Part 1:  Some logicaly simple conditions to check
  #

  # check for exceptions to sandhi. set self.
  if self._sandhiPrepException():
   return
  # check for cases where no further preparation required
  NoPrep = self._sandhiPrepNoPrep()
  if NoPrep:
   return

  # Check for some further odd cases
  if self.Pada1 in ["aY","alaNkfY","nirAkfY","naY","wIwaY","WaY"]:
   self.NoStoh = True
  elif self.Pada1 in ["Ayan","Gan"] and self.PaninianText:
   #  if (!PaninianText)  #ejf note this differs from above condition??
   # PMS (June 2010)The whole section of sandhiPrep up to "if Compound"
   #  is aimed specifically at the Astadhyayi and perhaps other texts of
   #   Paninian grammar and should be excluded from general sandhi.
   NoPrep = True
   self.NoKNam = True
  elif self.Pada1 == "tumun":
   self.NoStoh = True
  elif self.Compound and (self.Pada1 == "puram") and (self.Pada2 == "dArO"):
   # PMS: purandrau
   self.OtherCloseSandhi = True

  if (not self.Compound) or (self.Exception) or NoPrep:
   #ejf note. From above, we know that self.Exception == False and NoPrep == False
   return
  #
  # Part 2: adjustments re compound sandhi
  #
  self.sandhiPrepCompoundAdjust()

 @wrapper
 def sandhimain(self):
  """ method sandhimain 
 
  """
  #  initialize some instance variables
  self.Isthana1 = 0
  self.Isthana2 = 0
  self.Iyatna1 = 0
  self.Iyatna2 = 0
  #self.IEnd = 0
  self.Index = 0
  #self.Found = False
  #self.NoSpace = False
  self.Dhralopa = False
  self.OtherCloseSandhi = False
  self.Pragrhya = False
  self.Uttarapada = False
  NxtUttarapada = False
  self.PurvaPada = ""
  self.Pada1 = ""
  self.Pada2 = ""
  self.Upasarga = False #  ejf.
  #   initialize some variables used by this method only
  #Inext = 0
  #Inextsp = 0
  IPrev = 0
  #IPrevSpace = 0
  I = 0
  # PMS: the first character in Linary should not be a word boundary
  if (False): # dbg
   j0=-1
   print "Linary=",self.Linary
   for j in xrange(0,len(self.Linary)):
    if self.Linary[j]!=' ':
     j0=j
     break
   print "sandhimain, j0=",j0
  # find first Padbound, by searching Linary starting at index 2.
  # ejf.  Initialize self.Index to 1, so that, in the while loop,
  # the first call to nxtposary will have '2' as 2nd parameter.
  # Thus, no call to nxtposary is needed at end of loop.
  self.Index = 1
  while self.Index > 0:
   self.Index = self.nxtposary(self.Padbound,  self.Index + 1)
   if self.Index <= 0:
    break  # this is how the while loop terminates
   # PMS: while a padbound character is found
   self.EkahPurvaParayoh = False
   # PMS: PurvaPada, Pada1, Pada2
   #self.Uttarapada = False
   #if NxtUttarapada:
   # self.Uttarapada = True # PMS: Pada1 is an uttarapada
   self.Uttarapada = NxtUttarapada
   NxtUttarapada = False
   self.PurvaPada = self.Pada1  # Pada1 for previous iteration of while loop
   #--------------------------------------------------------
   # Pada1.  Also, may set IPrev (on first loop iteration)
   #--------------------------------------------------------
   if IPrev == 0:
    # PMS: first Pada1 in Linary  
    # ejf. This is why there needs to be at least one extra space at the beginning
    # of Linary.  
    # The condition loop condition (while self.Index > 0) may(?) be the reason
    # there need to be TWO extra spaces at the beginning of Linary
    IPrev = self.lastposary(space, self.Index - 1)
    self.Pada1 = self.substrary(IPrev + 1, self.Index - 1)
   elif self.External:
    # PMS: we've been through here before so
    self.Pada1 = self.Pada2
   else:
    # PMS: padbound=hyphen
    self.Pada1 = NxtPada1
   #--------------------------------------------------------
   # Pada2.  Also, may set IPrev (on first loop iteration)
   # Also set are: 
   # Nxtpada1
   # NxtUttarapada
   #--------------------------------------------------------
   inext = self.nxtposary(self.Padbound,  self.Index + 1)
   if inext == 0:
    # PMS: not found so last word
    inext = self.lengthary() + 1
   if self.External:
    self.Pada2 = self.substrary(self.Index + 1, inext - 1)
   else:
    # PMS: for compound, Pada2, NxtPada1
    inextsp = self.nxtposary(space,  self.Index + 1)
    if (inextsp > 0) and (inextsp < inext):
     self.Pada2 = self.substrary(self.Index + 1, inextsp - 1)
    else:
     self.Pada2 = self.substrary(self.Index + 1, inext - 1)
    # PMS: now the next Pada1 when padbound =hyphen
    iPrevSpace = self.lastposary(space, inext - 1)
    if iPrevSpace > self.Index:
     NxtPada1 = self.substrary(iPrevSpace + 1, inext - 1) #  corrected
    else:
     NxtPada1 = self.Pada2
     NxtUttarapada = True
   #--------------------------------------------------------
   # PMS: determine whether Pada1 is an upasarga
   # set Upasarga. 
   # resets Pada1 from "ut" to "ud" if External
   #--------------------------------------------------------
   self.Upasarga = False
   if self.External and (self.Pada1 == "ut"):
    self.Pada1 = "ud"
   if self.Pada1 == "api":
    # PMS: more likely karmapravacanIya than upasarga
    pass 
   elif self.Pada1 in Pradi:
    self.Upasarga = True
   #--------------------------------------------------------
   # PMS: stem final sound changes for compound sandhi && some 
   #      special sandhi for grammatical technical terms
   #--------------------------------------------------------
   self.sandhiPrep()
   doSandhi = True
   if self.Exception:
    doSandhi = False
   else:
    if self.Upasarga and self.CloseUpasargaSandhi:
     # PMS: sandhi subroutines:  within compound && following an upasarga 
     # closer sandhi is observed when an option is allowed.
     # Otherwise (between syntactic units) looser sandhi is observed
     # ejf note: In this version, CloseUpasargaSandhi is always False,
     # so this condition will never occur
     self.OtherCloseSandhi = True
    # PMS: kosher exceptions to sandhi
    # ejf: External sandhi only
    self.idudeddvivacanampragrhyam() 
    if self.Pragrhya:
     doSandhi = False
   #--------------------------------------------------------
   # Main section which does the sandhi at the current Padbound
   #--------------------------------------------------------
   if doSandhi:
    self.visargaprep() # change final H in pada1 to 'r' or 's'. Why not in sandhiPrep?
    #classify character before and after Padbound using Soundary
    [self.Isthana1,self.Iyatna1] = identify(self.Linary[self.Index - 1])
    [self.Isthana2,self.Iyatna2] = identify(self.Linary[self.Index + 1])
    # PMS: must precede 8.4.40.  stoH ScunA ScuH
    self.checa() # PMS: 6.1.73.  che ca
    self.anmanosca() # PMS: 6.1.74.  ANmANoSca (che 73, tuk 71)
    if (self.TukPadantat): # ejf. Normally true flag, as 'standard editorial practice' for close sandhi
     self.padantadva() # PMS: 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
    # PMS: must precede vowel sandhi
    #nshs_flag = set_memberP(self.Linary[self.Index - 1], sktn_and_sktsh_and_skts)
    # ejf:  Original code had next 5 routine calls only if nshs_flag.  
    # However, I think these are 'independent' and thus don't need this condition
    self.etattadohsulopo()  # PMS: 6.1.132.  etattadoH sulopo "kor anaYsamAse hali
    self.amnarudharavar() # PMS: 8.2.70.  amnarUdharavarityubhayathA chandasi
    self.sasajusoruh() # PMS: 8.2.66.  sasajuzo ruH
    self.ahan() # PMS: exception in 63110 8.2.68.  ahan
    # PMS: 6.1.13.  ato ror aplutad aplute.  
    #      6.1.14.  haSi ca.  Must precede 6.1.109.  eNaH padAntAd ati
    self.atororhasica()
    if (set_memberP(self.Linary[self.Index - 1], Ac) and set_memberP(self.Linary[self.Index + 1], Ac)):
     # a. Vowel + Vowel
     self.acsandhi()
    elif (set_memberP(self.Linary[self.Index - 1], Hal_and_ru)) and (set_memberP(self.Linary[self.Index + 1], Al_and_Linend)):
     # b. Consonant + (Consonant or Vowel or Linend)
     self.non_acsandhi()
    # 
    if (set_memberP(self.Linary[self.Index - 1], Hal)) and (set_memberP(self.Linary[self.Index + 1], Al)):
     # PMS: must follow vowel sandhi
     # PMS: 8.3.19.  lopaH SAkalyasya.  Must follow 6.1.78.  eco "yavAyAvaH
     self.lopahsakalyasya()
     #  PMS: If made to include semivowels, 8.4.45 must follow 8.3.19-20. 
     #   In present form it needn't.
     if self.Anunasika or self.OtherCloseSandhi:
      # PMS: 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
      self.yaronunasike()
   #--------------------------------------------------------
   # After 'doSandhi' section
   # Last cleanup section, after sandhi has been done
   #--------------------------------------------------------
   if self.EkahPurvaParayoh:
    # PMS: EkahPurvaParayoh set in acsandhi in subroutines: 
    #   akahsavarnedirghah, adgunah, vrddhireci
    # PMS: do the same steps if two padbounds in a row 
    #   because last sandhi eliminated single char word
    self.deletary(self.Index)
    # PMS: the search for the next padbound begins at Index+1
    self.Index = self.Index - 1
   elif (self.Index > 1) and self.Despace:
    if set_memberP(self.Linary[self.Index - 1], Hal):
     # PMS: Removed "or Upasarga"
     self.deletary(self.Index)
   # PMS: get rid of the hyphen between words
   if self.Linary[self.Index] == hyphen:
    self.deletary(self.Index)
    self.Index = self.Index - 1
   # prepare for next iteration
   IPrev = self.Index

   # PMS: find the next pada boundary
   #self.Index = self.nxtposary(self.Padbound,  self.Index + 1)
   # return to top of while loop
  # PMS: conclude while loop when padbound character is not found (Index=0)

 @wrapper
 def sandhi1(self, s):
  """ method sandhi1 
   Prepare input for sandhimain
   Accept string argument, to which sandhi is to be applied.
   return a string argument as the answer
   return a blank string if there is an error
   print an informative message if there is an error.
   Two special values of 's' are related to debugging: 'dbg' and 'off'
  """

  s1 = s.strip() 
  if (s == "dbg") or (s == "off"):
   # kludgy addition by ejf. Probably should be removed. (Aug 9, 2015)
   if not self.dbg:
    self.dbg = True
   else:
    self.dbg = False
   return ""
  s1 = " " + s1 + "    "

  self.Linary = [" "] + list(s1) #  was [""] Jul 29, 2015
  self.linmax = len(self.Linary) - 1

  self.Error = 0
  self.sandhimain()
  if self.Error != 0:
   #  if ((Error != 0) && (!((NoSpace && (Error == 2))))) ...
   return ""
  else:
   ans = "".join(self.Linary)
   ans = ans.strip()
   return (ans)

 @wrapper
 def sandhi(self, s):
  """ method sandhi Main entry
   Accept string argument, to which sandhi is to be applied.
   Return a string argument as the answer
   Return a blank string if there is an error

  """
  split = sandhiSplit(s)
  n = len(split)
  whitebeg = ""
  ans = whitebeg
  #  \s is whitespace
  p1= re.compile(r"^(\s+)(.*)$")
  p2= re.compile(r"^(.*?)(\s+)$")
  # split is organized as pairs: (split[0],split[1]), (split[2],split[3]), etc.
  # split[0],[2], etc are codes classifying as Sanskrit or not-Sanskrit the
  # correspond text in split[1],split[3], etc.
  i = 0
  while i < n:
   x = split[i + 1]
   # strip whitespace from beginning of x, save as whitebeg
   m = re.search(p1,x)
   if m:
    whitebeg = m.group(1)
    x = m.group(2)
   else:
    whitebeg = ""
   # strip whitespace from end of x, save as whiteend
   m = re.search(p2,x)
   if m:
    whiteend = m.group(2)
    x = m.group(1)
   else:
    whiteend = ""
   # if 'x' is Sanskrit, apply sandhi
   if split[i] == "s":
    y = self.sandhi1(x)
   else:
    y = x
   # replace whitespace around sandhied form y
   y = whitebeg + y + whiteend
   ans += y
   # next iteration
   i += 2
  return ans

