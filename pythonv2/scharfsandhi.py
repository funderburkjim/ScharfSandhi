# coding=utf-8
#!/usr/bin/env python
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
  This Java method replaces the characters in a substring of this
    StringBuffer with characters in the specified String.
  The substring begins at the specified start and extends to the character
  at index end - 1 or to the end of the StringBuffer if no such character
  exists. First the characters in the substring are removed and then the
  specified String is inserted at start.
 """
 # char[] ax = x.toCharArray();
 #b = list(x)
 # b = b.replace(idx1, idx2, y)
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
 a = [] # list of strings '' # list[] # ArrayList()
 INITIAL = 0
 SKT = 1
 OTHER = 2
 #  Only non-alphabetic chars considered to be Sanskrit are
 #  - and space and apostrophe and "|" and "/"
 #  20090801, "/" is a sandhi-blocking character.
 #  String sanskrit_str = "- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/";
 #  June 22: Added period to list of Sanskrit characters.
 sanskrit_str = "- '.aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/"
 #sanskrit_strs = sanskrit_str.split("")
 #sanskrit_strs_list = Arrays.asList(sanskrit_strs)
 sanskrit_set = set(sanskrit_str) #HashSet(sanskrit_strs_list)
 #xarr = x.split("")
 xarr =  x  # Java x.split("") has empty string as first element of return
 ilen = len(x)
 state = INITIAL
 more = True
 y = "" # list of characters   StringBuffer()
 #c = str()
 ipos = 0
 while ipos < ilen:
  c = xarr[ipos]
  if state == INITIAL:
   y = c
   if (c in sanskrit_set):
    state = SKT
    #y.append(c)
   else:
    state = OTHER
    #y.append(c)
  elif state == SKT:
   if (c in sanskrit_set):
    y = y + c #.append(c)
   else:
    dbgPrint(dbg,"sandhiSplit 1. i=%s,c='%s'" %(ipos,c))
    a.append("s")
    a.append(y) # (str(y))
    y = c #.append(c)
    state = OTHER
  else:
   #  state = OTHER
   if (c in sanskrit_set):
    a.append("o")
    a.append(y) # (str(y))
    y = c 
    state = SKT
   else:
    y = y + c 
  ipos += 1
 if 0 != len(y):
  if state == SKT:
   dbgPrint(dbg,"sandhiSplit 2.")
   a.append("s")
   a.append(y) # (str(y))
  elif state == OTHER:
   a.append("o")
   a.append(y) # (str(y))
  else:
   #  should not occur
   pass
 #temp = a.toArray()
 #l = len(temp)
 #ans = " " # ejf[None]*l
 #i = 0
 #while i < l:
 # ans[i] = str(a.get(i))
 # i += 1
 #return ans
 return a

def dbgPrint(dbg,text):
 if dbg:
  print text

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
# * These are Strings of length 1, so could have been declared 'char'
# * However, it was felt that treating them as String objects was conceptually
# * simpler, and probably insignificantly less efficient.
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
star = "*"
slash = "/"
openparen = "("
closeparen = ")"

# extended ascii. Required to fill Soundary, but otherwise unused
sktjihvamuliya = "»"; #{opt k}
sktupadhmaniya = "¹"; #{opt p}
sktanunasika = "µ"; #{opt m.  It should follow the sound it nasalizes}
sktroot = "§"; #{opt v}
#constant sktudatta = "«"; #{opt e space.  It precedes the sound it accents}
#constant sktudattaaa = "§";
#constant sktudattaii = "ª";
#constant sktudattauu = "²";
#constant sktudattaau = "®";
#constant sktsvaritaaa = "¥";
#constant sktsvaritaii = "«";
#constant sktsvaritauu = "³";
#constant sktsvaritaai = "¦";
#constant sktsvaritaau = "¯";

# (ejf)What is 'CAntaPadary' supposed to be? It is coded as sets of chars
# The string is populated in init_CAntaPadary
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
# Since the Sanskrit characters are represented as Java Strings,
# the 'union' of sets may be uniformly represented with Java '+'
# concatentaion of Strings.
ru = "s"
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
An2 = Ac + skth + Yan

# PMS vowels, h and semivowels
In2 = diff_string(An2, Avarna)
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

# PMS non-nasal stops and silibants
Hal = skty + sktv + sktr + sktl + sktcn + sktm + sktkn + sktretron + sktn + sktjh + sktbh + sktgh + sktretrodh + sktdh + sktj + sktb + sktg + sktretrod + sktd + sktkh + sktph + sktch + sktretroth + sktth + sktc + sktretrot + sktt + sktk + sktp + sktsch + sktsh + skts + skth
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
# set construction operators. In conversion to Perl,
# it was convenient to construct these initialially and
# given then new names.
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

# private static final String[] Pradi = new String[1+pradimax];
#Soundary = " "*maxsthana # ejf [None]*1 + maxsthana
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

# constants global to sandhi routine
pratipadmax = 20

# PMS Maximum length assumed for lexical items
iapi = 13

# PMS api usually is not an upasarga so check it separately

class ScharfSandhi(object):
 #  variables global to sandhi routines
 linmax = int() # resolves to 0 in Python
 Linary = []

 # = new String[1+linmax]; #
 Isthana1 = int() 
 Isthana2 = int()
 Iyatna1 = int()
 Iyatna2 = int()
 PurvaPada = str() # Resolves to empty string in Python
 Pada1 = str()
 NxtPada1 = str()
 Pada2 = str()

 #  usu. max len pratipadmax
 Upasarga = bool()  # Resolves to False in Python
 NoStoh = bool()
 NoKNam = bool()
 Exception = bool()
 Pronoun = bool()
 EkahPurvaParayoh = bool()
 Error = int()
 IEnd = int()
 Inextsp = int()
 IPrev = int()
 Inext = int()
 IPrevSpace = int()
 Index = int()
 Found = bool()
 NoSpace = bool()
 Dhralopa = bool()
 OtherCloseSandhi = bool()
 Pragrhya = bool()
 Uttarapada = bool()
 NxtUttarapada = bool()
 FldChr = None # str()  Java is String FldChr, whose (default) value is 'null'
 Despace = bool()
 External = bool()
 Compound = bool()
 Chandas = bool()
 CloseUpasargaSandhi = bool()
 PaninianText = False

 #  June 2010. Not reset.
 TukPadantat = bool()
 ScharSchari = bool()
 XkXpKupvoh = bool()
 ChAti = bool()
 ParaSavarna = bool()
 Anunasika = bool()
 Padbound = str()
 dbg = False
 

 def sandhioptions(self, compound_ans, vedic_ans, closeSandhi_ans, despace_ans):
  """ method sandhioptions 
  # 
  #   * Returns 0 (ok) or 4 (error)
  #   * @param compound_ans C for compound sandhi, E for External sandhi
  #   * @param vedic_ans  Y or N
  #   * @param closeSandhi_ans N,Y,S
  #   * @param despace_ans Y or N
  """
  #Answer = str()
  Yes = "Y"
  No = "N"
  error = 0
  #  initialize external flags to false.
  self.Despace = False
  self.External = False
  self.Compound = False
  self.Chandas = False
  self.CloseUpasargaSandhi = False
  self.TukPadantat = False # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
  self.ScharSchari = False # PMS 8.3.36.  vA Sari
  self.XkXpKupvoh = False  # PMS 8.3.37.  kupvoH XkXpau ca.
  self.ChAti = False     # PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
  self.ParaSavarna = False # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
  self.Anunasika = False # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
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
     # if self.dbg:  // ejf commented out
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
    Answer = "?"
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

 def lengthary(self):
  """ method lengthary
   return position in Linary of the last character which is not a space;
   return 0 if all elements of Linary are spaces.
  """
  I = self.linmax
  dbgPrint(False,"lengthary. Linary has length=%s, linmax=%s\nLinary=%s" %(len(self.Linary),self.linmax,self.Linary))
  while 1 <= I:
   if not (self.Linary[I] == " "):
    return I
   I -= 1
  return 0

 def nxtposary(self, chtr, fldch, istart):
  """ method nxtposary
  Searches Linary for either chtr or fldch. Returns of match.
  Discounts trailing spaces.
  @param chtr
  @param fldch
  @param istart
  @return Returns -1 if istart is < 1 or > linmax
   Returns 0 if no match found in Linary
   Returns index (istart to linmax) of first match found.
  """
  if istart < 1:
   return -1
  if istart > self.linmax:
   return -1
  IEnd = self.lengthary()
  self.chk_point('nxtposary: IEnd=%s' % IEnd)
  if IEnd == 0:
   return 0
  I = istart
  while I <= IEnd:
   if self.Linary[I] == chtr:
    return I
   if self.Linary[I] == fldch:
    return I
   I += 1
  return 0

 def lastposary(self, chtr, istart):
  """ method lastposary
  Searches backward in Linary for first occurrence of given character
  @param chtr character to search for
  @param istart starting position
  @return return -1 if istart is inappropriate
  return 0 if chtr not found in Linary
  return I if nearest occurrence (from istart down to 1) of chtr is
  at index I
  """
  if istart < 1:
   return -1
  if istart > self.linmax:
   return -1
  # error in conversion to Java  if (IEnd == 0){return 0;}
  I = istart
  while 1 <= I:
   if self.Linary[I] == chtr:
    return I
   I -= 1
  return 0

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
  self.NoSpace = False
  IEnd = self.lengthary()
  if IEnd == self.linmax:
   #  add some more space to Linary
   #print "insertary: Augmenting Linary: linmax starts as ", self.linmax,len(self.Linary)
   #print "Linary=",self.Linary
   s1 = "".join(self.Linary)
   #print "s1='%s'"% s1
   #print "s1 length=",len(s1)
   s1 = s1 + "          "  # 10 spaces
   #print "s1 length (after padding)=",len(s1)
   # self.Linary  this is what sandhimain modifies.
   self.Linary = [""] + list(s1) #s1.split("")
   #self.Linary = list(s1) #s1.split("")
   #print "new length of Linary=",len(self.Linary)
   self.linmax = len(self.Linary) - 1
   #print "s1 length=",len(s1)
   #print "linmax now = ",self.linmax
   IEnd = self.lengthary()
   #print "IEnd now = ",IEnd
  if IEnd == self.linmax:
   self.NoSpace = True
   print "WARNING: insertary: NoSpace now " + self.NoSpace
   return
  Ipt = index
  if Ipt < 1:
   Ipt = 1
  if Ipt > IEnd:
   Ipt = IEnd + 1
  I = IEnd
  while Ipt <= I:
   self.Linary[I + 1] = self.Linary[I]
   I -= 1
  self.Linary[Ipt] = chtr
  return

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

 def substrary(self, index1, index2):
  """ method substrary
  Returns a substring of Linary consisting of (index1-index2)+1 characters beginning at index1
  @param index1
  @param index2
  @return
  """
  Tempstr = [] #StringBuffer()
  ans = ""
  IEnd = self.lengthary()
  if (index1 < 1) or (index1 > index2) or (index2 > IEnd):
   return ans
  if ((index2 - index1) + 1) > pratipadmax:
   return ans
  if self.dbg:
   print "substrary: index1=%s, index2=%s" %(index1,index2)
  I = index1
  while I <= index2:
   Tempstr.append(self.Linary[I])
   I += 1
  #ans = str(Tempstr)
  ans = "".join(Tempstr)
  return ans

 def identify(self, aksara):
  """ method identify
  Returns positions (Isthana and Iyatna) in Soundary matrix
  where the character 'aksara' is found.
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

 def rlvarnayormithahsavarnyam(self):
  """ method rlvarnayormithahsavarnyam
  {1.1.9 vt. fkAra kArayoH savarRavidhiH}
  uses globals Linary,Index.
  May modify Linary,Isthana1,Isthana2
  """
  if (set_memberP(self.Linary[self.Index - 1], Rvarna_and_Lvarna)) and (set_memberP(self.Linary[self.Index + 1], Rvarna_and_Lvarna)):
   self.Linary[self.Index - 1] = sktri
   self.Linary[self.Index + 1] = sktri
   self.Isthana1 = imurdhanya
   self.Isthana2 = imurdhanya
  self.chk_point("rlvarnayormithahsavarnyam")

 def akahsavarnedirghah(self):
  """ method akahsavarnedirghah
  {6.1.101.  akaH savafRe dIrghaH}
  Uses globals Linary,Index,Isthana1
  Modifies Linary,EkahPurvaParayoh
  """
  self.Linary[self.Index - 1] = Soundary[self.Isthana1][idirgha]
  self.deletary(self.Index + 1) # {6.1.84.  ekaH pUrvaparayoH}
  self.EkahPurvaParayoh = True
  self.chk_point("akahsavarnedirghah")

 def vrddhireci(self):
  """ method vrddhireci
  6.1.88.  vfddhir eci
  Uses globals Linary,Index,Isthana2
  Modifies Linary,EkahPurvaParayoh
  """
  self.Linary[self.Index - 1] = Soundary[self.Isthana2][ivrddhi]
  self.deletary(self.Index + 1) # {6.1.84.  ekaH pUrvaparayoH}
  self.EkahPurvaParayoh = True
  self.chk_point("vrddhireci")

 def adgunah(self):
  """ method adgunah
  6..1.87.  Ad guRaH
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
  self.chk_point("adgunah")

 def ikoyanaci(self):
  """ method ikoyanaci
  6.1.77.  iko yaR aci
  Uses globals Linary,Index,Isthana1
  Modifies Linary
  """
  self.Linary[self.Index - 1] = Soundary[self.Isthana1][iantahstha]
  self.chk_point("ikoyanaci")

 def enahpadantadati(self):
  """ method enahpadantadati
  6.1.109.  eNaH padAntAd ati
  Uses globals Linary,Index
  Modifies Linary
  """
  self.Linary[self.Index + 1] = sktavagraha
  self.chk_point("enahpadantadati")

 def ecoyavayavah(self):
  """ method ecoyavayavah
  6.1.78.  eco 'yavAyAvaH
  Uses globals Linary,Index
  Modifies Linary,Index. May set Error
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
  if self.NoSpace:
   self.Error = 2
   return
  self.Index = self.Index + 1
  self.chk_point("ecoyavayavah")

 def acsandhi(self):
  """ method acsandhi
  Uses globals Linary,Index,Isthana1,Isthana2
  Modifies Linary,Index.
  Calls: rlvarnayormithahsavarnyam, akahsavarnedirghah,vrddhireci,
  adgunah,ikoyanaci,enahpadantadati,ecoyavayavah
  """
  self.rlvarnayormithahsavarnyam()
  cprev = self.Linary[self.Index - 1]
  cnext = self.Linary[self.Index + 1]
  if set_memberP(self.Linary[self.Index - 1], Ak):
   if (set_memberP(self.Linary[self.Index + 1], Ak)) and (self.Isthana1 == self.Isthana2):
    self.akahsavarnedirghah() # {6.1.101.  akaH savafRe dIrghaH}
   elif set_memberP(self.Linary[self.Index - 1], Avarna):
    # PMS: && Linary[Index+1] not in Avarna
    if set_memberP(self.Linary[self.Index + 1], Ec):
     self.vrddhireci() # PMS: 6.1.88  vfddhir eci
    else:
     # PMS: Linary[Index+1] in Ik
     self.adgunah() # PMS: 6.1.87  Ad guRaH
   else:
    # PMS: Linary[Index-1] in Ik && not savarna with Linary[Index+1]
    self.ikoyanaci() # PMS: 6.1.77.  iko yaR aci
  else:
   # PMS: Linary[Index-1] in Ec
   if (set_memberP(self.Linary[self.Index - 1], Ekn)) and (self.Linary[self.Index + 1] == skta):
    self.enahpadantadati() # PMS: 6.1.109.  eNaH padAntAd ati
   else:
    # PMS: set_memberP(Linary[Index-1],Ec) && set_memberP(Linary[Index+1],Ic)
    self.ecoyavayavah() # PMS: 6.1.78.  eco "yavAyAvaH
  self.chk_point("acsandhi")

 def visargaprep(self):
  """ method visargaprep
   Uses globals Pada1,Linary,Index
   Modifies Pada1,Linary
  """
  L = len(self.Pada1)
  if (self.Pada1 == "ahaH") or (self.Pada1 == "svaH") or (self.Pada1 == "antaH") or (self.Pada1 == "prAtaH") or (self.Pada1 == "punaH") or (self.Pada1 == "mAtaH") or (self.Pada1 == "kOsalyAmAtaH") or (self.Pada1 == "sanutaH") or (self.Pada1 == "catuH") or (self.Pada1 == "prAduH"):
   self.Linary[self.Index - 1] = sktr
   self.Pada1 = strReplace(self.Pada1, L - 1, L, sktr)
  else:
   self.Linary[self.Index - 1] = skts
   if not self.Pada1 == "":
    self.Pada1 = strReplace(self.Pada1, L - 1, L, skts)
  self.chk_point("visargaprep")

 def checa(self):
  """ method checa
   6.1.73.  che ca (tuk 71)
   Uses globals Linary,Index,Iyatna1
   Modifies Linary,Index,Error
  """
  if (self.Linary[self.Index + 1] == sktch) and (self.Iyatna1 == ihrasva):
   self.insertary(sktt, self.Index)
   if self.NoSpace:
    self.Error = 2
    return
   self.Index = self.Index + 1
  self.chk_point("checa")

 def anmanosca(self):
  """ method anmanosca
   6.1.74.  ANmANoSca (che 73, tuk 71)
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index,Error
     PMS: you'll have to add the condition that these are AN && mAN
     when that info is available
  """
  if (self.Linary[self.Index + 1] == sktch) and ((self.Pada1 == "A") or (self.Pada1 == "mA")):
   self.insertary(sktt, self.Index)
   if self.NoSpace:
    self.Error = 2
    return
   self.Index = self.Index + 1
  self.chk_point("anmanosca")

 def padantadva(self):
  """ method padantadva
   6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
   Uses globals Linary,Index,
   Modifies Linary,Index,Error,Isthana1,Iyatna1
  """
  # PMS: don"t want to do it if anmanosca just applied
  temp = self.identify(self.Linary[self.Index - 1])
  self.Isthana1 = temp[0]
  self.Iyatna1 = temp[1]
  if (self.Linary[self.Index + 1] == sktch) and (self.Iyatna1 == idirgha):
   self.insertary(sktt, self.Index)
   if self.NoSpace:
    self.Error = 2
    return #  REPLACE exit(sandhi);
   self.Index = self.Index + 1
  self.chk_point("padantadva")

 def etattadohsulopo(self):
  """ method etattadohsulopo
   6.1.132.  etattadoH sulopo "kor anaYsamAse hali
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index
  """
  if ((self.Pada1 == "sas") or (self.Pada1 == "ezas")) and (set_memberP(self.Linary[self.Index + 1], Hal)):
   self.deletary(self.Index - 1)
   self.Index = self.Index - 1
  self.chk_point("etattadohsulopo")

 def jhalamjasonte(self):
  """ method jhalamjasonte
   8.2.39.  jhalAM jaSo 'nte
   Uses globals Linary,Index,Pada1
   Modifies Linary,Isthana1,Iyatna1
  """
  temp = self.identify(self.Linary[self.Index - 1])
  self.Isthana1 = temp[0]
  self.Iyatna1 = temp[1]
  if set_memberP(self.Linary[self.Index - 1], Jhal_not_ru):
   # PMS: because ru =skts; I could choose another character
   self.Linary[self.Index - 1] = Soundary[self.Isthana1][isparsa3]
   # PMS: jhalamjasonte
  self.chk_point("jhalamjasonte")

 def sasajusoruh(self):
  """ method sasajusoruh
   Uses globals Linary,Index
   Modifies Linary
   PMS: 8.2.66.  sasajuzo ruH
   PMS: exception to 8.2.39 so must apply before it
  """
  if self.Index > 5:
   if self.substrary(self.Index - 5, self.Index - 1) == "sajuz":
    self.Linary[self.Index - 1] = ru
  if self.Linary[self.Index - 1] == skts:
   self.Linary[self.Index - 1] = ru
  self.chk_point("sasajusoruh")

 def ahan(self):
  """ method ahan
   8.2.68.  ahan
   Uses globals Linary,Index,Pada1,Pada2
   Modifies Linary
  """
  if self.Compound:
   if self.Pada1 == "ahan":
    if (self.Pada2 == "rUpa") or (self.Pada2 == "rAtri") or (self.Pada2 == "rAtra") or (self.Pada2 == "rAtre") or (self.Pada2 == "rAtrARAm") or (self.Pada2 == "raTantara"):
     # PMS: vArttika, but had to add rAtra 21045,
     # rAtre 24028, rAtrARAm 33137
     self.Linary[self.Index - 1] = ru
     # PMS: if ahan is termed pada && Pada2 in Sup, 
     # so that Linary[Index+1]=sktbh || skts, ditto
    else:
     self.Linary[self.Index - 1] = sktr # PMS: 8.2.69.  ro "supi
  self.chk_point("ahan")

 def amnarudharavar(self):
  """ method amnarudharavar
   8.2.70.  amnarUdharavarityubhayathA chandasi
   Uses globals Linary,Index,Pada1
   Modifies Linary
  """
  if self.Chandas:
   if (self.Pada1 == "amnas") or (self.Pada1 == "UDas") or (self.Pada1 == "avas"):
    # PMS: actually you get it both ways in chandas, ru too
    self.Linary[self.Index - 1] = sktr
  self.chk_point("amnarudharavar")

 def atororhasica(self):
  """ method atororhasica
   6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca
   Uses globals Linary,Index
   Modifies Linary,Index
  """
  if self.Index > 2:
   if (self.Linary[self.Index - 2] == skta) and (self.Linary[self.Index - 1] == ru):
    if set_memberP(self.Linary[self.Index + 1], Hasch_and_skta):
     self.Linary[self.Index - 2] = skto # PMS: Linary[Index-1=sktu; adguna
     self.deletary(self.Index - 1)
     self.Index = self.Index - 1
  self.chk_point("atororhasica")

 def naschavyaprasan(self):
  """ method naschavyaprasan 
   8.3.7.  naS chavy apraSAn
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index,Error
  """
  if (self.Linary[self.Index - 1] == sktn and (set_memberP(self.Linary[self.Index + 1], Chav)) and not (self.Pada1 == "praSAn")):
   self.Linary[self.Index - 1] = ru
   # PMS: 8.3.4.  anunAsikAt paro "nusvAraH
   self.insertary(sktanusvara, self.Index - 1)
   if self.NoSpace:
    self.Error = 2
    return
   self.Index = self.Index + 1
  self.chk_point("naschavyaprasan")

 def rori(self):
  """ method rori 
   8.3.14.  ro ri
   Uses globals Linary,Index
   Modifies Linary,Index,Dhralopa
  """
  self.Dhralopa = False
  if (set_memberP(self.Linary[self.Index - 1], sktr_and_ru)) and (self.Linary[self.Index + 1] == sktr):
   self.deletary(self.Index - 1)
   self.Index = self.Index - 1
   self.Dhralopa = True
  self.chk_point("rori")

 def dhralope(self):
  """ method dhralope 
   6.3.111.  qhralope pUrvasya dIrgho 'RaH
   Uses globals Linary,Index,Dhralopa
   Modifies Linary
  """
  if self.Dhralopa:
   temp = self.identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   if (set_memberP(self.Linary[self.Index - 1], An)) and (self.Iyatna1 == ihrasva):
    self.Linary[self.Index - 1] = Soundary[self.Isthana1][idirgha]
  self.chk_point("dhralope")

 def bhobhago(self):
  """ method bhobhago 
   8.3.17.  bhobhagoaghoapUrvasya yo 'Si
   Uses globals Linary,Index,Pada1
   Modifies Linary
  """
  if (set_memberP(self.Linary[self.Index + 1], Asch)) and (self.Index > 2):
   if (self.Pada1 == "bhos") or (self.Pada1 == "bhagos") or (self.Pada1 == "aghos") or ((set_memberP(self.Linary[self.Index - 2], Avarna)) and (self.Linary[self.Index - 1] == ru)):
    self.Linary[self.Index - 1] = skty
  self.chk_point("bhobhago")

 def kharavasanayor(self):
  """ method kharavasanayor 
   8.3.15.  kharavasAnayor visarjanIyaH
   Uses globals Linary,Index
   Modifies Linary
  """
  # print "kharachk: '" + Linary[Index - 1] + "', '"+Linary[Index + 1]+"'" ;
  if set_memberP(self.Linary[self.Index - 1], sktr_and_ru):
   if set_memberP(self.Linary[self.Index + 1], Khar_and_linend):
    self.Linary[self.Index - 1] = sktvisarga
   else:
    self.Linary[self.Index - 1] = sktr
  self.chk_point("kharavasanayor")

 def lopahsakalyasya(self):
  """ method lopahsakalyasya 
   8.3.19.  lopaH SAkalyasya
   Uses globals Linary,Index
   Modifies Linary,Index
  """
  if (set_memberP(self.Linary[self.Index + 1], Asch)) and (self.Index > 2):
   if (set_memberP(self.Linary[self.Index - 2], Avarna)) and (self.Linary[self.Index - 1] == skty):
    self.deletary(self.Index - 1)
    self.Index = self.Index - 1
  self.chk_point("lopahsakalyasya")

 def otogargyasya(self):
  """ method otogargyasya 
   8.3.20.  oto gArgyasya
   Uses globals Linary,Index
   Modifies Linary,Index
  """
  if set_memberP(self.Linary[self.Index + 1], Asch):
   if ((self.Pada1 == "bhos") or (self.Pada1 == "bhagos") or (self.Pada1 == "aghos")):
    self.deletary(self.Index - 1)
    self.Index = self.Index - 1
  self.chk_point("otogargyasya")

 def monusvarah(self):
  """ method monusvarah 
   8.3.23.  mo 'nusvAraH
   Uses globals Linary,Index
   Modifies Linary
  """
  if (self.Linary[self.Index - 1] == sktm) and (set_memberP(self.Linary[self.Index + 1], Hal)):
   self.Linary[self.Index - 1] = sktanusvara
  self.chk_point("monusvarah")

 def namohrasvad(self):
  """ method namohrasvad 
   8.3.32.  Namo hrasvAd aci NamuR nityam
   Uses globals Linary,Index
   Modifies Linary,Index,Error
  """
  self.chk_point("namohrasvad enters with Index=%s, NoSpace=%s" %(self.Index, self.NoSpace))
  if (self.Index > 2):
   temp = self.identify(self.Linary[self.Index - 2])
   Sthana = temp[0]
   Yatna = temp[1]
   if (Yatna == ihrasva) and (set_memberP(self.Linary[self.Index - 1], KNam)) and (set_memberP(self.Linary[self.Index + 1], Ac)):
    self.chk_point("namohrasvad BEFORE: Soundary[%s][%s] = '%s'" %(self.Isthana1,isparsa5,Soundary[self.Isthana1][isparsa5]))
    self.insertary(Soundary[self.Isthana1][isparsa5], self.Index)
    self.chk_point("namohrasvad  AFTER: Soundary[%s][%s] = '%s'" %(self.Isthana1,isparsa5,Soundary[self.Isthana1][isparsa5]))
    if self.NoSpace:
     self.Error = 2
     return
    self.Index = self.Index + 1
   else:
    self.chk_point("namohrasvad Test fails")
    self.chk_point("Sthana=%s,Yatna=%s" % (Sthana,Yatna))
    self.chk_point("penult.char=%s,Yatna=?ihrasva:%s" % (self.Linary[self.Index - 2],(Yatna == ihrasva)))
    self.chk_point("Prev char=%s,test=%s" % (self.Linary[self.Index - 1],set_memberP(self.Linary[self.Index - 1], KNam)))
    self.chk_point("Next char=%s,test=%s" % (self.Linary[self.Index + 1],set_memberP(self.Linary[self.Index + 1], Ac)))

  self.chk_point("namohrasvad")

 def visarjaniyasyasah(self):
  """ method visarjaniyasyasah 
   8.3.34.  visarjanIyasya saH
   Uses globals Linary,Index
   Modifies Linary
  """
  Apavada = bool() #  type = boolean;
  if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Khar)):
   Apavada = False
   if (self.Index + 2) < self.linmax:
    if set_memberP(self.Linary[self.Index + 2], Schar):
     Apavada = True # PMS: 8.3.35.  Sarpare visarjanIyaH.
   if set_memberP(self.Linary[self.Index + 1], Ku_and_Pu_and_Schar):
    Apavada = True # PMS: 8.3.36.  vA Sari.  8.3.37.  kupvoH XkXpau ca.
   if not (Apavada):
    self.Linary[self.Index - 1] = skts
  self.chk_point("visarjaniyasyasah")

 def vasari(self):
  """ method vasari 
   8.3.36.  vA Sari
   Uses globals Linary,Index
   Modifies Linary
  """
  if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Schar)):
   self.Linary[self.Index - 1] = skts
  self.chk_point("vasari")

 def kupvohXkXpau(self):
  """ method kupvohXkXpau 
    8.3.37.  kupvoH XkXpau ca (khari 15).
    8.3.41, 8.3.45 && 8.3.46 are apavAdas of this so must precede it.
   Uses globals Linary,Index
   Modifies Linary
  """
  Apavada = bool()
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
  self.chk_point("kupvohXkXpau")

 def idudupadhasya(self):
  """ method idudupadhasya 
   8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39
   Uses globals Linary,Index,Pada1
   Modifies Linary
   PMS: exception to 8.3.36.  kupvoH XkaXpau ca, 
        which is an exception to 8.3.34. visarjanIyasya saH,
        so should accompany procedure visarjaniyasyasah.  
        Must follow 8.3.15.  kharavasAnayor visarjanIyaH
  """
  if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Ku_and_Pu)):
   if (self.Pada1 == "nis") or (self.Pada1 == "dus") or (self.Pada1 == "bahis") or (self.Pada1 == "Avis") or (self.Pada1 == "catur") or (self.Pada1 == "prAdur"):
    self.Linary[self.Index - 1] = sktsh # PMS: bahis, Avis =exception to 8.3.46
  self.chk_point("idudupadhasya")

 def nityamsamase(self):
  """ method nityamsamase 
   8.3.45. nityamsamAse 'nutarapadasthasya
   Uses globals Linary,Index
   Modifies Linary
  """
  if self.Compound:
   if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Ku_and_Pu)) and (self.Index > 2):
    if ((self.Linary[self.Index - 2] == skti) or ((self.Linary[self.Index - 2] == sktu) and (not self.Uttarapada))):
     # PMS: Pada1-u.p. [SOFT HYPHEN]
     self.Linary[self.Index - 1] = sktsh
  self.chk_point("nityamsamase")

 def atahkrkamikamsa(self):
  """ method atahkrkamikamsa 
   8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya (samAse 45)
   Uses globals Linary,Index,Pada1,Pada2
   Modifies Linary
  """
  if self.Compound:
   if (self.Linary[self.Index - 1] == sktvisarga) and (set_memberP(self.Linary[self.Index + 1], Ku_and_Pu)) and (self.Index > 2):
    if (self.Linary[self.Index - 2] == skta):
     if (self.Pada2 == "kAra") or (self.Pada2 == "kAma") or (self.Pada2 == "kaMsa") or (self.Pada2 == "kumBa") or (self.Pada2 == "kumBI") or (self.Pada2 == "pAtra") or (self.Pada2 == "kuSA") or (self.Pada2 == "karRI"):
      if not ((self.Pada1 == "svar") or (self.Pada1 == "antar") or (self.Pada1 == "prAtar") or (self.Pada1 == "punar") or (self.Pada1 == "sanutar") or (self.Pada1 == "hyas") or (self.Pada1 == "Svas") or (self.Pada1 == "avas") or (self.Pada1 == "aDas")) and (not self.Uttarapada):
       self.Linary[self.Index - 1] = skts
  # PMS: miTas, namas, (tiraskAra by 8.3.42.  avaskara, namaskAra?)
  # krtvasuc, suc, i.e. not avyaya

  self.chk_point("atahkrkamikamsa")

 def stohscunascuh(self):
  """ method stohscunascuh 
   8.4.40.  stoH ScunA ScuH
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  Isthana = int()
  Iyatna = int()
  if (set_memberP(self.Linary[self.Index - 1], Tu_and_skts)) and (set_memberP(self.Linary[self.Index + 1], Cu_and_sktsch)):
   temp = self.identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index - 1] = Soundary[italavya][self.Iyatna1]
  elif (set_memberP(self.Linary[self.Index - 1], Cu_and_sktsch)) and (self.Linary[self.Index + 1] == skts):
   self.Linary[self.Index + 1] = sktsch
   if (self.Index + 2 < self.linmax):
    if self.Linary[self.Index + 2] == skts:
     self.Linary[self.Index + 1] = sktsch
  elif (set_memberP(self.Linary[self.Index - 1], Cu)) and (set_memberP(self.Linary[self.Index + 1], Tu)):
   # PMS: 8.4.44.  SAt. (na, toH)
   temp = self.identify(self.Linary[self.Index + 1])
   self.Isthana2 = temp[0]
   self.Iyatna2 = temp[1]
   self.Linary[self.Index + 1] = Soundary[italavya][self.Iyatna2]
   if (self.Index + 2 < self.linmax):
    if set_memberP(self.Linary[self.Index + 2], Tu_and_skts):
     temp = self.identify(self.Linary[self.Index + 2])
     Isthana = temp[0]
     Iyatna = temp[1]
     self.Linary[self.Index + 2] = Soundary[italavya][Iyatna]
  self.chk_point("stohscunascuh")

 def stunastuh(self):
  """ method stunastuh 
   8.4.41.  zwunA zwuH
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  Isthana = int()
  Iyatna = int()
  if ((self.Linary[self.Index - 1] == sktsh) and (set_memberP(self.Linary[self.Index + 1], Tu_and_skts))) or (set_memberP(self.Linary[self.Index - 1], Retrotu) and (self.Pada2 == "nAm")):
   # PMS: 8.4.42.  na padAntAwworanAm
   temp = self.identify(self.Linary[self.Index + 1])
   self.Isthana2 = temp[0]
   self.Iyatna2 = temp[1]
   self.Linary[self.Index + 1] = Soundary[imurdhanya][self.Iyatna2]
   if (self.Index + 2 < self.linmax):
    if set_memberP(self.Linary[self.Index + 2], Tu_and_skts):
     temp = self.identify(self.Linary[self.Index + 2])
     Isthana = temp[0]
     Iyatna = temp[1]
     self.Linary[self.Index + 1] = Soundary[imurdhanya][self.Iyatna2]
     self.Linary[self.Index + 2] = Soundary[imurdhanya][Iyatna]
  elif (set_memberP(self.Linary[self.Index - 1], Tu) and (set_memberP(self.Linary[self.Index + 1], Retrotu))) or ((self.Linary[self.Index - 1] == skts) and (set_memberP(self.Linary[self.Index + 1], Retrotu_sktsh))):
   # PMS: 8.4.43.  toH zi. (na)
   temp = self.identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index - 1] = Soundary[imurdhanya][self.Iyatna1]
  self.chk_point("stunastuh")

 def anusvarasya(self):
  """ method anusvarasya 
   8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58)
   PMS: don"t exercise the option for semivowels (yan) just now
   Uses globals Linary,Index
   Modifies Linary,Isthana2,Iyatna2
  """
  if (self.Linary[self.Index - 1] == sktanusvara) and (set_memberP(self.Linary[self.Index + 1], Yay_not_Yan)):
   temp = self.identify(self.Linary[self.Index + 1])
   self.Isthana2 = temp[0]
   self.Iyatna2 = temp[1]
   self.Linary[self.Index - 1] = Soundary[self.Isthana2][isparsa5]
  self.chk_point("anusvarasya")

 def torli(self):
  """ method torli 
   8.4.60.  tor li
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Index,Error
  """
  if (set_memberP(self.Linary[self.Index - 1], Tu)) and (self.Linary[self.Index + 1] == sktl):
   temp = self.identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index - 1] = sktl
   if self.Iyatna1 == isparsa5:
    self.insertary(sktnasalization, self.Index - 1)
    if self.NoSpace:
     self.Error = 2
     return
    self.Index = self.Index + 1
  self.chk_point("torli")

 def jhayoho(self):
  """ method jhayoho 
   8.4.62.  jhayo ho 'nyatarasyAm
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1
  """
  if (set_memberP(self.Linary[self.Index - 1], Jhay)) and (self.Linary[self.Index + 1] == skth):
   temp = self.identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index + 1] = Soundary[self.Isthana1][isparsa4]
  self.chk_point("jhayoho")

 def saschoti(self):
  """ method saschoti 
   8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
   Uses globals Linary,Index
   Modifies Linary
  """
  if (set_memberP(self.Linary[self.Index - 1], Jhay)) and ((self.Index + 2) < self.linmax):
   if (self.Linary[self.Index + 1] == sktsch) and (set_memberP(self.Linary[self.Index + 2], At)):
    # PMS: vt. chatvamamIti vaktavyam:  
    # Am instead of At.  tacchlokena, tacchmaSruRA
    self.Linary[self.Index + 1] = sktch
  self.chk_point("saschoti")

 def yaronunasike(self):
  """ method yaronunasike 
   8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  temp = self.identify(self.Linary[self.Index + 1])
  self.Isthana2 = temp[0]
  self.Iyatna2 = temp[1]
  # PMS: if ( set_memberP(Linary[Index - 1],Yar) && (Index + 2 < linmax) then
  # PMS: if (Iyatna2 eq isparsa5) || (Linary[Index + 2] == sktanunasika ) {
  # PMS: we won't exercise the nasalized option for the semivowels 
  #      y, v && l; just for the stops
  if (set_memberP(self.Linary[self.Index - 1], Jhay)) and (self.Iyatna2 == isparsa5):
   temp = self.identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   self.Linary[self.Index - 1] = Soundary[self.Isthana1][isparsa5]
  self.chk_point("yaronunasike")

 def kharica(self):
  """ method kharica 
   8.4.55.  khari ca. (jhalAm 53, car 54)
   PMS: there is no final  "h" after jhalAm jaSo "nte, 
     but there is skts by 8.3.34 visarjanIyasya saH
     && sktsch && sktsh by 
     8.4.40-41 stoH ScunA scuH, zwunA zwuH so must exclude Sar
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1
  """
  if set_memberP(self.Linary[self.Index - 1], Jhay):
   # PMS: jhay=jhal-Sar
   temp = self.identify(self.Linary[self.Index - 1])
   self.Isthana1 = temp[0]
   self.Iyatna1 = temp[1]
   if set_memberP(self.Linary[self.Index + 1], Khar_and_linend):
    # PMS: 8.4.56.  vavasane
    self.Linary[self.Index - 1] = Soundary[self.Isthana1][isparsa1]
  self.chk_point("kharica")

 def idudeddvivacanampragrhyam(self):
  """ method idudeddvivacanampragrhyam 
   1.1.11. IdUdeddvivacanam pragfhyam
   Uses globals Linary,Index,Pada1
   Modifies Linary,Pragrhya
  """
  # PMS: 1.1.11. IdUdeddvivacanam pragfhyam
  self.Pragrhya = False
  c = self.Linary[self.Index - 1]
  if self.External:
   if c == sktii:
    if (self.Pada1 == "amI") or (self.Pada1 == "aDiparI") or (self.Pada1 == "aBipratI") or (self.Pada1 == "manasI"):
     self.Pragrhya = True
   elif c == sktuu:
    if (self.Pada1 == "amU"):
     # PMS: 1.1.12.  adaso mAt
     self.Pragrhya = True
   elif c == skte:
    if (self.Pada1 == "SAlInakOpIne") or (self.Pada1 == "uBe"):
     self.Pragrhya = True
   elif c == skto:
    if (self.Pada1 == "Aho") or (self.Pada1 == "utAho"):
     # PMS: 1.1.15. ot
     self.Pragrhya = True
  self.chk_point("idudeddvivacanampragrhyam")

 def sandhiPrep(self):
  """ method sandhiPrep 
      This routine inadequately documented
  """
  L = int()
  IPada = int()
  NoPrep = bool()
  self.NoStoh = False
  self.NoKNam = False
  NoPrep = False
  self.Exception = False
  self.Pronoun = True # PMS: saú is usually the pronoun tad [LATIN SMALL LETTER U WITH ACUTE]
  self.OtherCloseSandhi = False
  L = len(self.Pada1)
  if L <= 1:
   return
  c = self.Pada1[L-1] #  last character of Pada1. # self.Pada1.substring(L - 1, L)
  if self.dbg:
   print "sandhiPrep: Pada1='" + self.Pada1 + "', c=" + c
   print "Is c = skts? %s" % (c == skts,)
   print "is Pada1 = us? %s" % (self.Pada1 == "us",)
  if c == sktkn:
   #  RiN change made 20090801, PMS.
   if self.Pada1 == "RiN":
    self.Exception = True
  elif c == sktc:
   while IPada <= cantamax:
    if self.Pada1 == CAntaPadary[IPada]:
     NoPrep = True
     self.NoStoh = True
     IPada = cantamax #  leave loop
    IPada += 1
  elif c == sktj:
   if (self.Pada1 == "tij"):
    self.Exception = True
   elif (self.Pada1 == "tuj"):
    NoPrep = True
  elif c == sktcn:
   if (self.Pada1 == "aY") or (self.Pada1 == "alaNkfY") or (self.Pada1 == "nirAkfY") or (self.Pada1 == "naY") or (self.Pada1 == "wIwaY") or (self.Pada1 == "WaY"):
    self.NoStoh = True
  elif c == sktretron:
   if (self.Pada1 == "aR") or (self.Pada1 == "uR") or (self.Pada1 == "yaR"):
    self.Exception = True
  elif c == sktdh:
   if (self.Pada1 == "aD") or (self.Pada1 == "ruD"):
    self.Exception = True
  elif c == sktn:
   if (self.Pada1 == "Wan") or (self.Pada1 == "tran") or (self.Pada1 == "dozan") or (self.Pada1 == "yakan") or (self.Pada1 == "yUzan") or (self.Pada1 == "Sakan") or (self.Pada1 == "zWan") or (self.Pada1 == "han"):
    NoPrep = True
   elif (self.Pada1 == "Ayan") or (self.Pada1 == "Gan"):
    #  if (!PaninianText)
    # PMS (June 2010)The whole section of sandhiPrep up to "if Compound"
    #  is aimed specifically at the Astadhyayi and perhaps other texts of
    #   Paninian grammar and should be excluded from general sandhi.
    if self.PaninianText:
     NoPrep = True
     self.NoKNam = True
   elif (self.Pada1 == "ktin") or (self.Pada1 == "kvin") or (self.Pada1 == "min") or (self.Pada1 == "vin"):
    NoPrep = True
   elif (self.Pada1 == "an") or (self.Pada1 == "in") or (self.Pada1 == "kan") or (self.Pada1 == "kaDyEn") or (self.Pada1 == "qvun") or (self.Pada1 == "tan") or (self.Pada1 == "dAn") or (self.Pada1 == "man") or (self.Pada1 == "vun"):
    self.Exception = True
   elif self.Pada1 == "tumun":
    self.NoStoh = True
  elif c == sktm:
   if (self.Pada1 == "am") or (self.Pada1 == "Am") or (self.Pada1 == "num"):
    self.Exception = True
   elif self.Compound:
    if ((self.Pada1 == "puram") and (self.Pada2 == "dArO")):
     # PMS: purandrau
     self.OtherCloseSandhi = True
  elif c == skty:
   if (self.Pada1 == "ay") or (self.Pada1 == "Ay"):
    self.Exception = True
  elif c == sktr:
   if (self.Pada1 == "car") or (self.Pada1 == "kur") or (self.Pada1 == "Sar"):
    self.Exception = True
  elif c == sktsch:
   if (self.Pada1 == "eS") or (self.Pada1 == "KaS") or (self.Pada1 == "jaS") or (self.Pada1 == "niS"):
    self.Exception = True
  elif c == sktsh:
   if (self.Pada1 == "Jaz") or (self.Pada1 == "Baz"):
    self.Exception = True
  elif c == skts:
   self.chk_point("sandhiPrep at c=skts:%s " % self.Exception)
   if (self.Pada1 == "as") or (self.Pada1 == "atus") or (self.Pada1 == "aTus") or (self.Pada1 == "is") or (self.Pada1 == "us") or (self.Pada1 == "os") or (self.Pada1 == "kas") or (self.Pada1 == "kAs") or (self.Pada1 == "Nas") or (self.Pada1 == "tas") or (self.Pada1 == "tAs") or (self.Pada1 == "TAs") or (self.Pada1 == "Bis") or (self.Pada1 == "Byas"):
    self.Exception = True
    self.chk_point("sandhiPrep setting Exception to %s" % self.Exception)
  if self.Compound:
   # PMS: normal stem changes
   if (not self.Exception) and (not NoPrep):
    c = self.Linary[self.Index - 1]
    if c == sktc:
     if self.Pada1 == "aYc":
      # PMS: aYc
      self.Linary[self.Index - 1] = sktk # PMS: ak
      self.deletary(self.Index - 2)
      self.Index = self.Index - 1
     else:
      self.Linary[self.Index - 1] = sktk
    elif c == sktch:
     self.Linary[self.Index - 1] = sktk
    elif c == sktj:
     if (self.Pada1 == "rAj"):
      self.Linary[self.Index - 1] = sktretrot
     else:
      self.Linary[self.Index - 1] = sktk
    elif c == sktjh:
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
        self.deletary(self.Index - 1)
        self.Index = self.Index - 1
      # PMS: an-/in- (end)
    elif c == sktr:
     if (self.Pada1 == "pur") or (self.Pada1 == "Dur"):
      self.Linary[self.Index - 2] = sktuu
    elif c == sktsch:
     if self.Pada1 == "viS":
      self.Linary[self.Index - 1] = sktretrot
     else:
      self.Linary[self.Index - 1] = sktk
    elif c == sktsh:
     if self.Pada1 == "daDfz":
      self.Linary[self.Index - 1] = sktk
    elif c == skts:
     if (self.Pada1 == "ASis"):
      self.Linary[self.Index - 2] = sktii # PMS: 82104
     elif self.Pada1 == "pums":
      # PMS: "pum"
      self.deletary(self.Index - 1)
      self.Index = self.Index - 1
    else:
     # PMS: no preparation necessary, normal sandhi will follow
     pass
    # PMS: case statement (end)
   # PMS: astadhyayiSandhiPrep (end)
  # PMS: sandhiprep

 def sandhi1(self, s):
  """ method sandhi1 
   Prepare input for sandhimain
   Accept string argument, to which sandhi is to be applied.
   return a string argument as the answer
   return a blank string if there is an error
   print an informative message if there is an error.
   Two special values of 's' are related to debugging: 'dbg' and 'off'
  """
  dbgPrint(False,"sandhi1. s=%s" % s)
  s1 = s.strip()
  if (s == "dbg") or (s == "off"):
   if not self.dbg:
    print "Turning on debug. To turn off, enter 'off'"
    self.dbg = True
   else:
    print "Turning off debug. To turn on, enter 'dbg'"
    self.dbg = False
   return ""
  s1 = " " + s1 + "    "
  #self.Linary = s1.split("")
  #self.Linary = list(s1)
  # Java adds an empty string at the beginning with s1.split("")
  #print "sandhi1: s=%s, s1=%s" %(s,s1)
  self.Linary = [""] + list(s1) #  this is what sandhimain modifies.
  self.linmax = len(self.Linary) - 1
  #print "Linary=[" + ",".join(self.Linary) + "]"
  self.chk_point("calling sandhimain with:'" + "".join(self.Linary) + "'")
  self.Error = 0
  self.sandhimain()
  if self.NoSpace and (self.Error == 2):
   #  change of June 22, 2010
   self.Error = 0
  if self.Error != 0:
   #  if ((Error != 0) && (!((NoSpace && (Error == 2))))) ...
   print "Sandhi error: " + self.Error + ", s = " + s
   return ""
  else:
   ans = "".join(self.Linary)
   ans = ans.strip()
   return (ans)

 def sandhimain(self):
  """ method sandhimain 
 
  """
  #  initialize some global variables
  self.Isthana1 = 0
  self.Isthana2 = 0
  self.Iyatna1 = 0
  self.Iyatna2 = 0
  self.IEnd = 0
  self.Index = 0
  self.Found = False
  self.NoSpace = False
  self.Dhralopa = False
  self.OtherCloseSandhi = False
  self.Pragrhya = False
  self.Uttarapada = False
  self.NxtUttarapada = False
  #   initialize some local variables
  Inext = 0
  Inextsp = 0
  IPrev = 0
  IPrevSpace = 0
  I = 0
  self.PurvaPada = ""
  self.Pada1 = ""
  self.Pada2 = ""
  # PMS: the first character in Linary should not be a word boundary
  self.Index = self.nxtposary(self.Padbound, self.FldChr, 2)
  self.chk_point("sandhimain. Initial Index = %s" % self.Index)
  self.Upasarga = False #  ejf.
  while self.Index > 0:
   # print "Index="+Index;
   # PMS: while a padbound character is found
   self.EkahPurvaParayoh = False
   # PMS: PurvaPada, Pada1, Pada2
   self.Uttarapada = False
   if self.NxtUttarapada:
    self.Uttarapada = True # PMS: Pada1 is an uttarapada
   self.NxtUttarapada = False
   # PMS: first Pada1 in Linary
   self.PurvaPada = self.Pada1
   if IPrev == 0:
    # PMS: first Pada1 in Linary
    if self.Compound:
     IPrev = self.lastposary(space, self.Index - 1)
    else:
     # July 2010.  On the first pass, Pada1 is known to begin with
     #  a blank, unless the following is done.
     IPrev = self.lastposary(space, self.Index - 1)
    self.chk_point("sandhimain: Index=%s, IPrev=%s" %(self.Index,IPrev))
    self.Pada1 = self.substrary(IPrev + 1, self.Index - 1)
    self.chk_point("sandhimain. Pada1='%s',  Compound=%s, IPrev=%s, Index=%s"  %(self.Pada1,self.Compound,IPrev, self.Index))
   elif self.External:
    # PMS: we've been through here before so
    self.Pada1 = self.Pada2
   else:
    # PMS: padbound=hyphen
    self.Pada1 = self.NxtPada1
   Inext = self.nxtposary(self.Padbound, self.FldChr, self.Index + 1)
   if Inext == 0:
    # PMS: not found so last word
    Inext = self.lengthary() + 1
   if self.External:
    self.Pada2 = self.substrary(self.Index + 1, Inext - 1)
   else:
    # PMS: for compound, Pada2, NxtPada1
    Inextsp = self.nxtposary(space, self.FldChr, self.Index + 1)
    if (Inextsp > 0) and (Inextsp < Inext):
     self.Pada2 = self.substrary(self.Index + 1, Inextsp - 1)
    else:
     self.Pada2 = self.substrary(self.Index + 1, Inext - 1)
    # PMS: now the next Pada1 when padbound =hyphen
    IPrevSpace = self.lastposary(space, Inext - 1)
    if IPrevSpace > self.Index:
     self.NxtPada1 = self.substrary(IPrevSpace + 1, Inext - 1) #  corrected
    else:
     self.NxtPada1 = self.Pada2
     self.NxtUttarapada = True
   # PMS: Pada2, NxtPada1 hyphen (end)
   # PMS: end of PurvaPada, Pada1, Pada2
   # PMS: determine whether Pada1 is an upasarga
   self.Upasarga = False
   if self.External and (self.Pada1 == "ut"):
    self.Pada1 = "ud"
   if self.Pada1 == "api":
    # PMS: more likely karmapravacanIya than upasarga
    pass 
   else:
    i = 1
    while I <= pradimax:
     if self.Pada1 == Pradi[I]:
      self.Upasarga = True
      I = pradimax # to leave loop
     I += 1
   # PMS: stem final sound changes for compound sandhi && some 
   #      special sandhi for grammatical technical terms
   self.sandhiPrep()
   doSandhi = True
   self.chk_point("sandhimain, Exception =%s " % self.Exception)
   if self.Exception:
    doSandhi = False
   else:
    if self.Upasarga and self.CloseUpasargaSandhi:
     self.OtherCloseSandhi = True # PMS: initialized in sandhiPrep
    # PMS: sandhi subroutines:  within compound && following an upasarga 
    # closer sandhi is observed when an option is allowed
    # PMS: otherwise (between syntactic units) looser sandhi is observed
    self.idudeddvivacanampragrhyam() # PMS: kosher exceptions to sandhi
    if self.Pragrhya:
     doSandhi = False
   if doSandhi:
    if (self.Linary[self.Index - 1] == sktvisarga):
     self.visargaprep()
    temp = self.identify(self.Linary[self.Index - 1])
    self.Isthana1 = temp[0]
    self.Iyatna1 = temp[1]
    temp = self.identify(self.Linary[self.Index + 1])
    self.Isthana2 = temp[0]
    self.Iyatna2 = temp[1]
    # PMS: must precede 8.4.40.  stoH ScunA ScuH
    self.checa() # PMS: 6.1.73.  che ca
    self.anmanosca() # PMS: 6.1.74.  ANmANoSca (che 73, tuk 71)
    if (self.TukPadantat):
     self.padantadva() # PMS: 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
    # PMS: must precede vowel sandhi
    if set_memberP(self.Linary[self.Index - 1], sktn_and_sktsh_and_skts):
     if self.Pronoun:
      # PMS: 6.1.132.  etattadoH sulopo "kor anaYsamAse hali
      self.etattadohsulopo() 
     # PMS: 8.2.70.  amnarUdharavarityubhayathA chandasi
     self.amnarudharavar() 
     # PMS: 8.2.66.  sasajuzo ruH
     self.sasajusoruh()
     if not self.NoStoh:
      # PMS: exception in 63110
      # PMS: 8.2.68.  ahan
      self.ahan()
     # PMS: 6.1.13.  ato ror aplutad aplute.  
     #      6.1.14.  haSi ca.  Must precede 6.1.109.  eNaH padAntAd ati
     self.atororhasica()
    if set_memberP(self.Linary[self.Index - 1], Ac) and set_memberP(self.Linary[self.Index + 1], Ac):
     self.acsandhi()
    elif (set_memberP(self.Linary[self.Index - 1], Hal_and_ru)) and (set_memberP(self.Linary[self.Index + 1], Al_and_Linend)):
     # PMS: 8.2.39.  jhalAM jaSo "nte
     self.jhalamjasonte()
     # PMS: 8.3.7.  naS chavy apraSAn
     self.naschavyaprasan()
     # PMS: 8.3.14.  ro ri  
     self.rori()
     # ejf: Dhralopa is global
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
     self.chk_point("NoKNam = %s" % self.NoKNam)
     if not self.NoKNam:
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
    if (set_memberP(self.Linary[self.Index - 1], Hal)) and (set_memberP(self.Linary[self.Index + 1], Al)):
     # PMS: must follow vowel sandhi
     # PMS: 8.3.19.  lopaH SAkalyasya.  Must follow 6.1.78.  eco "yavAyAvaH
     self.lopahsakalyasya()
     #  PMS: If made to include semivowels, 8.4.45 must follow 8.3.19-20. 
     #   In present form it needn't.
     if self.Anunasika or self.OtherCloseSandhi:
      # PMS: 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
      self.yaronunasike()
   self.chk_point("label7000a. Index=%s"%self.Index)
   # PMS: get rid of the space between words
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
   if self.Linary[self.Index] == hyphen:
    self.deletary(self.Index)
    self.Index = self.Index - 1
   IPrev = self.Index
   self.chk_point("label7000b(0): Padbound=%s, FldChr=%s, Index=%s" %(self.Padbound, self.FldChr, self.Index + 1))
   # PMS: find the next pada boundary
   self.Index = self.nxtposary(self.Padbound, self.FldChr, self.Index + 1)
   self.chk_point("label7000b")
   if self.dbg:
    print "label7000b(1) Index = %s" % self.Index
  # PMS: conclude while loop when padbound character is not found (Index=0)

 def sandhi(self, s):
  """ method sandhi 
   Accept string argument, to which sandhi is to be applied.
   Return a string argument as the answer
   Return a blank string if there is an error
   Print an informative message if there is an error.
  """
  dbg = False
  dbgPrint(dbg,"sandhi. s=%s" % s)
  split = sandhiSplit(s)
  
  dbgPrint(dbg,"sandhi: s='%s'" % s)
  dbgPrint(dbg,"sandhi: split=[%s]" % (",".join(split)))
  n = len(split)
  whitebeg = ""
  ans = whitebeg
  i = 0
  #  the doubling '\\' is a Java quirk of string literals
  #  \s is whitespace
  #p1 = Pattern.compile("^(\\s+)(.*)$")
  #p2 = Pattern.compile("(.*?)(\\s+)")
  p1= re.compile(r"^(\s+)(.*)$")
  p2= re.compile(r"^(.*?)(\s+)$")  # ScharfSandhi.java doesn't have '^','$'
  #m = Matcher()
  while i < n:
   x = split[i + 1]
   dbgPrint(dbg,"sandhi: i=%s, x=%s" % (i,x))
   m = re.search(p1,x)
   if m:
    whitebeg = m.group(1)
    x = m.group(2)
   else:
    whitebeg = ""
   dbgPrint(dbg,"sandhi(p1): x=%s" % x)
   m = re.search(p2,x) #p2.matcher(x)
   if m:
    whiteend = m.group(2)
    x = m.group(1)
   else:
    whiteend = ""
   dbgPrint(dbg,"sandhi(p2): x=%s" % x)
   if split[i] == "s":
    y = self.sandhi1(x)
    dbgPrint(dbg,"sandhi(after sandhi1) y=%s" %y)
   else:
    y = x
   y = whitebeg + y + whiteend
   ans += y
   i += 2
  return ans

 def chk_point(self, s):
  """ method chk_point 
   a debugging routine. If global 'dbg' value is true, then
   a debugging message is printed labeled with the parameter 's'
   @param s
  """
  if self.dbg:
   out = "%s(%s,%s): %s:%s" %(s,self.Index,self.linmax,self.NoSpace,"".join(self.Linary))
   print out
   #print s + "(" + self.Index + "," + self.linmax + "):" + self.NoSpace + ":" + "".join(self.Linary)

