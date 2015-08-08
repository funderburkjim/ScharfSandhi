# coding=utf-8
#!/usr/bin/env python
import re
def dbgPrint(dbg,text):
 if dbg:
  print text

def diff_string(x, y):
 """ generated source for method diff_string 
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
 
 @classmethod
 def init(cls):
  """ generated source for method init 
      currently this routine does nothing.
  """


 @classmethod
 def set_memberP(cls, c, s):
  """ generated source for method set_memberP 
  c is a char ,implemented as a string of length 1
  s is a "set of char", implemented as a string.
  """
  if c in s:
   return True
  else:
   return False
 
 @classmethod
 def str_trim(cls, x):
  """ generated source for method str_trim 
      This method returns a copy of the string, 
      with leading and trailing whitespace omitted.
  """
  return x.strip() 

 @classmethod
 def sandhioptions(cls, compound_ans, vedic_ans, closeSandhi_ans, despace_ans):
  """ generated source for method sandhioptions 
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
  cls.Despace = False
  cls.External = False
  cls.Compound = False
  cls.Chandas = False
  cls.CloseUpasargaSandhi = False
  cls.TukPadantat = False # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
  cls.ScharSchari = False # PMS 8.3.36.  vA Sari
  cls.XkXpKupvoh = False  # PMS 8.3.37.  kupvoH XkXpau ca.
  cls.ChAti = False     # PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
  cls.ParaSavarna = False # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
  cls.Anunasika = False # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
  Answer = compound_ans.upper()
  if Answer == "":
   Answer = "?"
  if Answer == "C":
   cls.Compound = True
   cls.Padbound = hyphen
  elif Answer == "E":
   cls.External = True
   cls.Padbound = space
  else:
   cls.Error = 4
   return cls.Error
  #  process vedic answer
  #  print "Is this a Vedic text (chandas)?\n";
  #  print "Default no: ";
  #  readln(Answer);
  Answer = vedic_ans.upper()
  if Answer == "":
   Answer = "?"
  if Answer == "Y":
   cls.Chandas = True
  elif Answer == "N":
   cls.Chandas = False
  else:
   cls.Error = 4
   return cls.Error
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
   cls.TukPadantat = True # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
   cls.ScharSchari = True # PMS 8.3.36.  vA Sari
   cls.XkXpKupvoh = True  # PMS 8.3.37.  kupvoH XkXpau ca.
   cls.ChAti = True # PMS 8.4.63.  SaS cho "Ti. (jhayaH 62, anyatarasyAm 62)
   cls.ParaSavarna = True # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
   cls.Anunasika = True # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
  elif Answer == "N":
   cls.TukPadantat = False
   cls.ScharSchari = False
   cls.XkXpKupvoh = False
   cls.ChAti = False
   cls.ParaSavarna = False
   cls.Anunasika = False
  elif Answer == "S":
   if cls.Compound:
    # PMS Close sandhi within compounds
    cls.TukPadantat = True # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
    cls.ScharSchari = True # PMS 8.3.36.  vA Sari
    # PMS technically, 8.3.37 should also apply but it is never seen
    cls.ChAti = True # PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
    cls.ParaSavarna = True # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
    cls.Anunasika = True # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
    # PMS display standard editorial practice for compound sandhi
   else:
    # PMS External: 8.4.63 and 8.4.45
    cls.ChAti = True # PMS 8.4.63.  SaS cho "Ti. (jhayaH 62, anyatarasyAm 62)
    cls.Anunasika = True # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
     # if cls.dbg:  // ejf commented out
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
   cls.Error = 4
   return (cls.Error) # PMS peruse options
  # PMS Choose spacing options
  if cls.Compound:
   #   print "Hyphens will be deleted between compound elements.\n";
   pass 
  elif cls.External:
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
    cls.Despace = True
   elif Answer == "N":
    cls.Despace = False
   else:
    cls.Error = 4
    return (cls.Error)
  # PMS spaceoptions
  cls.Error = 0
  return cls.Error

 @classmethod
 def lengthary(cls):
  """ generated source for method lengthary
   return position in Linary of the last character which is not a space;
   return 0 if all elements of Linary are spaces.
  """
  I = cls.linmax
  dbgPrint(False,"lengthary. Linary has length=%s, linmax=%s\nLinary=%s" %(len(cls.Linary),cls.linmax,cls.Linary))
  while 1 <= I:
   if not (cls.Linary[I] == " "):
    return I
   I -= 1
  return 0

 @classmethod
 def nxtposary(cls, chtr, fldch, istart):
  """ generated source for method nxtposary
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
  if istart > cls.linmax:
   return -1
  IEnd = cls.lengthary()
  cls.chk_point('nxtposary: IEnd=%s' % IEnd)
  if IEnd == 0:
   return 0
  I = istart
  while I <= IEnd:
   if cls.Linary[I] == chtr:
    return I
   if cls.Linary[I] == fldch:
    return I
   I += 1
  return 0

 @classmethod
 def lastposary(cls, chtr, istart):
  """ generated source for method lastposary
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
  if istart > cls.linmax:
   return -1
  # error in conversion to Java  if (IEnd == 0){return 0;}
  I = istart
  while 1 <= I:
   if cls.Linary[I] == chtr:
    return I
   I -= 1
  return 0

 @classmethod
 def insertary(cls, chtr, index):
  """ generated source for method insertary
  Insert character at given position in Linary.
  If the position is prior to first position, it resets to first position
  If position is after the last non-space position, it resets to first ending
  non-space position.
  Linary may be augmented by spaces, if necessary. Thus NoSpace will not be set to true.
  @param chtr character to insert
  @param index position of insertion
   """
  cls.NoSpace = False
  IEnd = cls.lengthary()
  if IEnd == cls.linmax:
   #  add some more space to Linary
   #print "insertary: Augmenting Linary: linmax starts as ", cls.linmax,len(cls.Linary)
   #print "Linary=",cls.Linary
   s1 = "".join(cls.Linary)
   #print "s1='%s'"% s1
   #print "s1 length=",len(s1)
   s1 = s1 + "          "  # 10 spaces
   #print "s1 length (after padding)=",len(s1)
   # cls.Linary  this is what sandhimain modifies.
   cls.Linary = [""] + list(s1) #s1.split("")
   #cls.Linary = list(s1) #s1.split("")
   #print "new length of Linary=",len(cls.Linary)
   cls.linmax = len(cls.Linary) - 1
   #print "s1 length=",len(s1)
   #print "linmax now = ",cls.linmax
   IEnd = cls.lengthary()
   #print "IEnd now = ",IEnd
  if IEnd == cls.linmax:
   cls.NoSpace = True
   print "WARNING: insertary: NoSpace now " + cls.NoSpace
   return
  Ipt = index
  if Ipt < 1:
   Ipt = 1
  if Ipt > IEnd:
   Ipt = IEnd + 1
  I = IEnd
  while Ipt <= I:
   cls.Linary[I + 1] = cls.Linary[I]
   I -= 1
  cls.Linary[Ipt] = chtr
  return

 @classmethod
 def deletary(cls, index):
  """ generated source for method deletary
  remove the character at position 'index' from Linary.
  If index indexes a position after the last non-space, no character is deleted
  @param index
  """
  IEnd = cls.lengthary()
  if (index >= 1) and (index <= IEnd):
   I = index
   while I < IEnd:
    cls.Linary[I] = cls.Linary[I + 1]
    I += 1
   cls.Linary[IEnd] = ""

 @classmethod
 def substrary(cls, index1, index2):
  """ generated source for method substrary
  Returns a substring of Linary consisting of (index1-index2)+1 characters beginning at index1
  @param index1
  @param index2
  @return
  """
  Tempstr = [] #StringBuffer()
  ans = ""
  IEnd = cls.lengthary()
  if (index1 < 1) or (index1 > index2) or (index2 > IEnd):
   return ans
  if ((index2 - index1) + 1) > pratipadmax:
   return ans
  if cls.dbg:
   print "substrary: index1=%s, index2=%s" %(index1,index2)
  I = index1
  while I <= index2:
   Tempstr.append(cls.Linary[I])
   I += 1
  #ans = str(Tempstr)
  ans = "".join(Tempstr)
  return ans

 @classmethod
 def identify(cls, aksara):
  """ generated source for method identify
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

 @classmethod
 def rlvarnayormithahsavarnyam(cls):
  """ generated source for method rlvarnayormithahsavarnyam
  {1.1.9 vt. fkAra kArayoH savarRavidhiH}
  uses globals Linary,Index.
  May modify Linary,Isthana1,Isthana2
  """
  if (cls.set_memberP(cls.Linary[cls.Index - 1], Rvarna_and_Lvarna)) and (cls.set_memberP(cls.Linary[cls.Index + 1], Rvarna_and_Lvarna)):
   cls.Linary[cls.Index - 1] = sktri
   cls.Linary[cls.Index + 1] = sktri
   cls.Isthana1 = imurdhanya
   cls.Isthana2 = imurdhanya
  cls.chk_point("rlvarnayormithahsavarnyam")

 @classmethod
 def akahsavarnedirghah(cls):
  """ generated source for method akahsavarnedirghah
  {6.1.101.  akaH savafRe dIrghaH}
  Uses globals Linary,Index,Isthana1
  Modifies Linary,EkahPurvaParayoh
  """
  cls.Linary[cls.Index - 1] = Soundary[cls.Isthana1][idirgha]
  cls.deletary(cls.Index + 1) # {6.1.84.  ekaH pUrvaparayoH}
  cls.EkahPurvaParayoh = True
  cls.chk_point("akahsavarnedirghah")

 @classmethod
 def vrddhireci(cls):
  """ generated source for method vrddhireci
  6.1.88.  vfddhir eci
  Uses globals Linary,Index,Isthana2
  Modifies Linary,EkahPurvaParayoh
  """
  cls.Linary[cls.Index - 1] = Soundary[cls.Isthana2][ivrddhi]
  cls.deletary(cls.Index + 1) # {6.1.84.  ekaH pUrvaparayoH}
  cls.EkahPurvaParayoh = True
  cls.chk_point("vrddhireci")

 @classmethod
 def adgunah(cls):
  """ generated source for method adgunah
  6..1.87.  Ad guRaH
  Uses globals Linary,Index,Isthana2
  Modifies Linary,EkahPurvaParayoh
  """
  cls.Linary[cls.Index - 1] = Soundary[cls.Isthana2][iguna]
  if (cls.Isthana2 == italavya) or (cls.Isthana2 == iosthya):
   cls.deletary(cls.Index + 1) # {6.1.84.  ekaH pUrvaparayoH}
  elif cls.Isthana2 == imurdhanya: # imurdhanya:
   cls.Linary[cls.Index + 1] = sktr # {1.1.51.  uraR raparaH}
  elif cls.Isthana2 == idantya: # idantya:
   cls.Linary[cls.Index + 1] = sktl
  cls.EkahPurvaParayoh = True
  cls.chk_point("adgunah")

 @classmethod
 def ikoyanaci(cls):
  """ generated source for method ikoyanaci
  6.1.77.  iko yaR aci
  Uses globals Linary,Index,Isthana1
  Modifies Linary
  """
  cls.Linary[cls.Index - 1] = Soundary[cls.Isthana1][iantahstha]
  cls.chk_point("ikoyanaci")

 @classmethod
 def enahpadantadati(cls):
  """ generated source for method enahpadantadati
  6.1.109.  eNaH padAntAd ati
  Uses globals Linary,Index
  Modifies Linary
  """
  cls.Linary[cls.Index + 1] = sktavagraha
  cls.chk_point("enahpadantadati")

 @classmethod
 def ecoyavayavah(cls):
  """ generated source for method ecoyavayavah
  6.1.78.  eco 'yavAyAvaH
  Uses globals Linary,Index
  Modifies Linary,Index. May set Error
  """
  if cls.Linary[cls.Index - 1] == skte:
   cls.Linary[cls.Index - 1] = skta
   cls.insertary(skty, cls.Index)
  elif cls.Linary[cls.Index - 1] == skto:
   cls.Linary[cls.Index - 1] = skta
   cls.insertary(sktv, cls.Index)
  elif cls.Linary[cls.Index - 1] == sktai:
   cls.Linary[cls.Index - 1] = sktaa
   cls.insertary(skty, cls.Index)
  elif cls.Linary[cls.Index - 1] == sktau:
   cls.Linary[cls.Index - 1] = sktaa
   cls.insertary(sktv, cls.Index)
  if cls.NoSpace:
   cls.Error = 2
   return
  cls.Index = cls.Index + 1
  cls.chk_point("ecoyavayavah")

 @classmethod
 def acsandhi(cls):
  """ generated source for method acsandhi
  Uses globals Linary,Index,Isthana1,Isthana2
  Modifies Linary,Index.
  Calls: rlvarnayormithahsavarnyam, akahsavarnedirghah,vrddhireci,
  adgunah,ikoyanaci,enahpadantadati,ecoyavayavah
  """
  cls.rlvarnayormithahsavarnyam()
  cprev = cls.Linary[cls.Index - 1]
  cnext = cls.Linary[cls.Index + 1]
  if cls.set_memberP(cls.Linary[cls.Index - 1], Ak):
   if (cls.set_memberP(cls.Linary[cls.Index + 1], Ak)) and (cls.Isthana1 == cls.Isthana2):
    cls.akahsavarnedirghah() # {6.1.101.  akaH savafRe dIrghaH}
   elif cls.set_memberP(cls.Linary[cls.Index - 1], Avarna):
    # PMS: && Linary[Index+1] not in Avarna
    if cls.set_memberP(cls.Linary[cls.Index + 1], Ec):
     cls.vrddhireci() # PMS: 6.1.88  vfddhir eci
    else:
     # PMS: Linary[Index+1] in Ik
     cls.adgunah() # PMS: 6.1.87  Ad guRaH
   else:
    # PMS: Linary[Index-1] in Ik && not savarna with Linary[Index+1]
    cls.ikoyanaci() # PMS: 6.1.77.  iko yaR aci
  else:
   # PMS: Linary[Index-1] in Ec
   if (cls.set_memberP(cls.Linary[cls.Index - 1], Ekn)) and (cls.Linary[cls.Index + 1] == skta):
    cls.enahpadantadati() # PMS: 6.1.109.  eNaH padAntAd ati
   else:
    # PMS: set_memberP(Linary[Index-1],Ec) && set_memberP(Linary[Index+1],Ic)
    cls.ecoyavayavah() # PMS: 6.1.78.  eco "yavAyAvaH
  cls.chk_point("acsandhi")

 @classmethod
 def strReplace(cls, x, idx1, idx2, y):
  """ generated source for method strReplace 
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

 @classmethod
 def visargaprep(cls):
  """ generated source for method visargaprep
   Uses globals Pada1,Linary,Index
   Modifies Pada1,Linary
  """
  L = len(cls.Pada1)
  if (cls.Pada1 == "ahaH") or (cls.Pada1 == "svaH") or (cls.Pada1 == "antaH") or (cls.Pada1 == "prAtaH") or (cls.Pada1 == "punaH") or (cls.Pada1 == "mAtaH") or (cls.Pada1 == "kOsalyAmAtaH") or (cls.Pada1 == "sanutaH") or (cls.Pada1 == "catuH") or (cls.Pada1 == "prAduH"):
   cls.Linary[cls.Index - 1] = sktr
   cls.Pada1 = cls.strReplace(cls.Pada1, L - 1, L, sktr)
  else:
   cls.Linary[cls.Index - 1] = skts
   if not cls.Pada1 == "":
    cls.Pada1 = cls.strReplace(cls.Pada1, L - 1, L, skts)
  cls.chk_point("visargaprep")

 @classmethod
 def checa(cls):
  """ generated source for method checa
   6.1.73.  che ca (tuk 71)
   Uses globals Linary,Index,Iyatna1
   Modifies Linary,Index,Error
  """
  if (cls.Linary[cls.Index + 1] == sktch) and (cls.Iyatna1 == ihrasva):
   cls.insertary(sktt, cls.Index)
   if cls.NoSpace:
    cls.Error = 2
    return
   cls.Index = cls.Index + 1
  cls.chk_point("checa")

 @classmethod
 def anmanosca(cls):
  """ generated source for method anmanosca
   6.1.74.  ANmANoSca (che 73, tuk 71)
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index,Error
     PMS: you'll have to add the condition that these are AN && mAN
     when that info is available
  """
  if (cls.Linary[cls.Index + 1] == sktch) and ((cls.Pada1 == "A") or (cls.Pada1 == "mA")):
   cls.insertary(sktt, cls.Index)
   if cls.NoSpace:
    cls.Error = 2
    return
   cls.Index = cls.Index + 1
  cls.chk_point("anmanosca")

 @classmethod
 def padantadva(cls):
  """ generated source for method padantadva
   6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
   Uses globals Linary,Index,
   Modifies Linary,Index,Error,Isthana1,Iyatna1
  """
  # PMS: don"t want to do it if anmanosca just applied
  temp = cls.identify(cls.Linary[cls.Index - 1])
  cls.Isthana1 = temp[0]
  cls.Iyatna1 = temp[1]
  if (cls.Linary[cls.Index + 1] == sktch) and (cls.Iyatna1 == idirgha):
   cls.insertary(sktt, cls.Index)
   if cls.NoSpace:
    cls.Error = 2
    return #  REPLACE exit(sandhi);
   cls.Index = cls.Index + 1
  cls.chk_point("padantadva")

 @classmethod
 def etattadohsulopo(cls):
  """ generated source for method etattadohsulopo
   6.1.132.  etattadoH sulopo "kor anaYsamAse hali
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index
  """
  if ((cls.Pada1 == "sas") or (cls.Pada1 == "ezas")) and (cls.set_memberP(cls.Linary[cls.Index + 1], Hal)):
   cls.deletary(cls.Index - 1)
   cls.Index = cls.Index - 1
  cls.chk_point("etattadohsulopo")

 @classmethod
 def jhalamjasonte(cls):
  """ generated source for method jhalamjasonte
   8.2.39.  jhalAM jaSo 'nte
   Uses globals Linary,Index,Pada1
   Modifies Linary,Isthana1,Iyatna1
  """
  temp = cls.identify(cls.Linary[cls.Index - 1])
  cls.Isthana1 = temp[0]
  cls.Iyatna1 = temp[1]
  if cls.set_memberP(cls.Linary[cls.Index - 1], Jhal_not_ru):
   # PMS: because ru =skts; I could choose another character
   cls.Linary[cls.Index - 1] = Soundary[cls.Isthana1][isparsa3]
   # PMS: jhalamjasonte
  cls.chk_point("jhalamjasonte")

 @classmethod
 def sasajusoruh(cls):
  """ generated source for method sasajusoruh
   Uses globals Linary,Index
   Modifies Linary
   PMS: 8.2.66.  sasajuzo ruH
   PMS: exception to 8.2.39 so must apply before it
  """
  if cls.Index > 5:
   if cls.substrary(cls.Index - 5, cls.Index - 1) == "sajuz":
    cls.Linary[cls.Index - 1] = ru
  if cls.Linary[cls.Index - 1] == skts:
   cls.Linary[cls.Index - 1] = ru
  cls.chk_point("sasajusoruh")

 @classmethod
 def ahan(cls):
  """ generated source for method ahan
   8.2.68.  ahan
   Uses globals Linary,Index,Pada1,Pada2
   Modifies Linary
  """
  if cls.Compound:
   if cls.Pada1 == "ahan":
    if (cls.Pada2 == "rUpa") or (cls.Pada2 == "rAtri") or (cls.Pada2 == "rAtra") or (cls.Pada2 == "rAtre") or (cls.Pada2 == "rAtrARAm") or (cls.Pada2 == "raTantara"):
     # PMS: vArttika, but had to add rAtra 21045,
     # rAtre 24028, rAtrARAm 33137
     cls.Linary[cls.Index - 1] = ru
     # PMS: if ahan is termed pada && Pada2 in Sup, 
     # so that Linary[Index+1]=sktbh || skts, ditto
    else:
     cls.Linary[cls.Index - 1] = sktr # PMS: 8.2.69.  ro "supi
  cls.chk_point("ahan")

 @classmethod
 def amnarudharavar(cls):
  """ generated source for method amnarudharavar
   8.2.70.  amnarUdharavarityubhayathA chandasi
   Uses globals Linary,Index,Pada1
   Modifies Linary
  """
  if cls.Chandas:
   if (cls.Pada1 == "amnas") or (cls.Pada1 == "UDas") or (cls.Pada1 == "avas"):
    # PMS: actually you get it both ways in chandas, ru too
    cls.Linary[cls.Index - 1] = sktr
  cls.chk_point("amnarudharavar")

 @classmethod
 def atororhasica(cls):
  """ generated source for method atororhasica
   6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca
   Uses globals Linary,Index
   Modifies Linary,Index
  """
  if cls.Index > 2:
   if (cls.Linary[cls.Index - 2] == skta) and (cls.Linary[cls.Index - 1] == ru):
    if cls.set_memberP(cls.Linary[cls.Index + 1], Hasch_and_skta):
     cls.Linary[cls.Index - 2] = skto # PMS: Linary[Index-1=sktu; adguna
     cls.deletary(cls.Index - 1)
     cls.Index = cls.Index - 1
  cls.chk_point("atororhasica")

 @classmethod
 def naschavyaprasan(cls):
  """ generated source for method naschavyaprasan 
   8.3.7.  naS chavy apraSAn
   Uses globals Linary,Index,Pada1
   Modifies Linary,Index,Error
  """
  if (cls.Linary[cls.Index - 1] == sktn and (cls.set_memberP(cls.Linary[cls.Index + 1], Chav)) and not (cls.Pada1 == "praSAn")):
   cls.Linary[cls.Index - 1] = ru
   # PMS: 8.3.4.  anunAsikAt paro "nusvAraH
   cls.insertary(sktanusvara, cls.Index - 1)
   if cls.NoSpace:
    cls.Error = 2
    return
   cls.Index = cls.Index + 1
  cls.chk_point("naschavyaprasan")

 @classmethod
 def rori(cls):
  """ generated source for method rori 
   8.3.14.  ro ri
   Uses globals Linary,Index
   Modifies Linary,Index,Dhralopa
  """
  cls.Dhralopa = False
  if (cls.set_memberP(cls.Linary[cls.Index - 1], sktr_and_ru)) and (cls.Linary[cls.Index + 1] == sktr):
   cls.deletary(cls.Index - 1)
   cls.Index = cls.Index - 1
   cls.Dhralopa = True
  cls.chk_point("rori")

 @classmethod
 def dhralope(cls):
  """ generated source for method dhralope 
   6.3.111.  qhralope pUrvasya dIrgho 'RaH
   Uses globals Linary,Index,Dhralopa
   Modifies Linary
  """
  if cls.Dhralopa:
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   if (cls.set_memberP(cls.Linary[cls.Index - 1], An)) and (cls.Iyatna1 == ihrasva):
    cls.Linary[cls.Index - 1] = Soundary[cls.Isthana1][idirgha]
  cls.chk_point("dhralope")

 @classmethod
 def bhobhago(cls):
  """ generated source for method bhobhago 
   8.3.17.  bhobhagoaghoapUrvasya yo 'Si
   Uses globals Linary,Index,Pada1
   Modifies Linary
  """
  if (cls.set_memberP(cls.Linary[cls.Index + 1], Asch)) and (cls.Index > 2):
   if (cls.Pada1 == "bhos") or (cls.Pada1 == "bhagos") or (cls.Pada1 == "aghos") or ((cls.set_memberP(cls.Linary[cls.Index - 2], Avarna)) and (cls.Linary[cls.Index - 1] == ru)):
    cls.Linary[cls.Index - 1] = skty
  cls.chk_point("bhobhago")

 @classmethod
 def kharavasanayor(cls):
  """ generated source for method kharavasanayor 
   8.3.15.  kharavasAnayor visarjanIyaH
   Uses globals Linary,Index
   Modifies Linary
  """
  # print "kharachk: '" + Linary[Index - 1] + "', '"+Linary[Index + 1]+"'" ;
  if cls.set_memberP(cls.Linary[cls.Index - 1], sktr_and_ru):
   if cls.set_memberP(cls.Linary[cls.Index + 1], Khar_and_linend):
    cls.Linary[cls.Index - 1] = sktvisarga
   else:
    cls.Linary[cls.Index - 1] = sktr
  cls.chk_point("kharavasanayor")

 @classmethod
 def lopahsakalyasya(cls):
  """ generated source for method lopahsakalyasya 
   8.3.19.  lopaH SAkalyasya
   Uses globals Linary,Index
   Modifies Linary,Index
  """
  if (cls.set_memberP(cls.Linary[cls.Index + 1], Asch)) and (cls.Index > 2):
   if (cls.set_memberP(cls.Linary[cls.Index - 2], Avarna)) and (cls.Linary[cls.Index - 1] == skty):
    cls.deletary(cls.Index - 1)
    cls.Index = cls.Index - 1
  cls.chk_point("lopahsakalyasya")

 @classmethod
 def otogargyasya(cls):
  """ generated source for method otogargyasya 
   8.3.20.  oto gArgyasya
   Uses globals Linary,Index
   Modifies Linary,Index
  """
  if cls.set_memberP(cls.Linary[cls.Index + 1], Asch):
   if ((cls.Pada1 == "bhos") or (cls.Pada1 == "bhagos") or (cls.Pada1 == "aghos")):
    cls.deletary(cls.Index - 1)
    cls.Index = cls.Index - 1
  cls.chk_point("otogargyasya")

 @classmethod
 def monusvarah(cls):
  """ generated source for method monusvarah 
   8.3.23.  mo 'nusvAraH
   Uses globals Linary,Index
   Modifies Linary
  """
  if (cls.Linary[cls.Index - 1] == sktm) and (cls.set_memberP(cls.Linary[cls.Index + 1], Hal)):
   cls.Linary[cls.Index - 1] = sktanusvara
  cls.chk_point("monusvarah")

 @classmethod
 def namohrasvad(cls):
  """ generated source for method namohrasvad 
   8.3.32.  Namo hrasvAd aci NamuR nityam
   Uses globals Linary,Index
   Modifies Linary,Index,Error
  """
  cls.chk_point("namohrasvad enters with Index=%s, NoSpace=%s" %(cls.Index, cls.NoSpace))
  if (cls.Index > 2):
   temp = cls.identify(cls.Linary[cls.Index - 2])
   Sthana = temp[0]
   Yatna = temp[1]
   if (Yatna == ihrasva) and (cls.set_memberP(cls.Linary[cls.Index - 1], KNam)) and (cls.set_memberP(cls.Linary[cls.Index + 1], Ac)):
    cls.chk_point("namohrasvad BEFORE: Soundary[%s][%s] = '%s'" %(cls.Isthana1,isparsa5,Soundary[cls.Isthana1][isparsa5]))
    cls.insertary(Soundary[cls.Isthana1][isparsa5], cls.Index)
    cls.chk_point("namohrasvad  AFTER: Soundary[%s][%s] = '%s'" %(cls.Isthana1,isparsa5,Soundary[cls.Isthana1][isparsa5]))
    if cls.NoSpace:
     cls.Error = 2
     return
    cls.Index = cls.Index + 1
   else:
    cls.chk_point("namohrasvad Test fails")
    cls.chk_point("Sthana=%s,Yatna=%s" % (Sthana,Yatna))
    cls.chk_point("penult.char=%s,Yatna=?ihrasva:%s" % (cls.Linary[cls.Index - 2],(Yatna == ihrasva)))
    cls.chk_point("Prev char=%s,test=%s" % (cls.Linary[cls.Index - 1],cls.set_memberP(cls.Linary[cls.Index - 1], KNam)))
    cls.chk_point("Next char=%s,test=%s" % (cls.Linary[cls.Index + 1],cls.set_memberP(cls.Linary[cls.Index + 1], Ac)))

  cls.chk_point("namohrasvad")

 @classmethod
 def visarjaniyasyasah(cls):
  """ generated source for method visarjaniyasyasah 
   8.3.34.  visarjanIyasya saH
   Uses globals Linary,Index
   Modifies Linary
  """
  Apavada = bool() #  type = boolean;
  if (cls.Linary[cls.Index - 1] == sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], Khar)):
   Apavada = False
   if (cls.Index + 2) < cls.linmax:
    if cls.set_memberP(cls.Linary[cls.Index + 2], Schar):
     Apavada = True # PMS: 8.3.35.  Sarpare visarjanIyaH.
   if cls.set_memberP(cls.Linary[cls.Index + 1], Ku_and_Pu_and_Schar):
    Apavada = True # PMS: 8.3.36.  vA Sari.  8.3.37.  kupvoH XkXpau ca.
   if not (Apavada):
    cls.Linary[cls.Index - 1] = skts
  cls.chk_point("visarjaniyasyasah")

 @classmethod
 def vasari(cls):
  """ generated source for method vasari 
   8.3.36.  vA Sari
   Uses globals Linary,Index
   Modifies Linary
  """
  if (cls.Linary[cls.Index - 1] == sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], Schar)):
   cls.Linary[cls.Index - 1] = skts
  cls.chk_point("vasari")

 @classmethod
 def kupvohXkXpau(cls):
  """ generated source for method kupvohXkXpau 
    8.3.37.  kupvoH XkXpau ca (khari 15).
    8.3.41, 8.3.45 && 8.3.46 are apavAdas of this so must precede it.
   Uses globals Linary,Index
   Modifies Linary
  """
  Apavada = bool()
  # PMS: by 8.3.15, kharavasAnayorvisarjanIyaH, visarga occurs
  # before avasAna too.  but Xk && Xp don't.
  if (cls.Linary[cls.Index - 1] == sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], Khar)):
   # PMS: Hence, khari is understood here too
   Apavada = False
   if (cls.Index + 2 < cls.linmax):
    if cls.set_memberP(cls.Linary[cls.Index + 2], Schar):
     Apavada = True # PMS: 8.3.35.  Sarpare visarjanIyaH.
   if not (Apavada):
    if cls.set_memberP(cls.Linary[cls.Index + 1], Ku):
     cls.Linary[cls.Index - 1] = sktjihvamuliya
    elif cls.set_memberP(cls.Linary[cls.Index + 1], Pu):
     cls.Linary[cls.Index - 1] = sktupadhmaniya
  cls.chk_point("kupvohXkXpau")

 @classmethod
 def idudupadhasya(cls):
  """ generated source for method idudupadhasya 
   8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39
   Uses globals Linary,Index,Pada1
   Modifies Linary
   PMS: exception to 8.3.36.  kupvoH XkaXpau ca, 
        which is an exception to 8.3.34. visarjanIyasya saH,
        so should accompany procedure visarjaniyasyasah.  
        Must follow 8.3.15.  kharavasAnayor visarjanIyaH
  """
  if (cls.Linary[cls.Index - 1] == sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], Ku_and_Pu)):
   if (cls.Pada1 == "nis") or (cls.Pada1 == "dus") or (cls.Pada1 == "bahis") or (cls.Pada1 == "Avis") or (cls.Pada1 == "catur") or (cls.Pada1 == "prAdur"):
    cls.Linary[cls.Index - 1] = sktsh # PMS: bahis, Avis =exception to 8.3.46
  cls.chk_point("idudupadhasya")

 @classmethod
 def nityamsamase(cls):
  """ generated source for method nityamsamase 
   8.3.45. nityamsamAse 'nutarapadasthasya
   Uses globals Linary,Index
   Modifies Linary
  """
  if cls.Compound:
   if (cls.Linary[cls.Index - 1] == sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], Ku_and_Pu)) and (cls.Index > 2):
    if ((cls.Linary[cls.Index - 2] == skti) or ((cls.Linary[cls.Index - 2] == sktu) and (not cls.Uttarapada))):
     # PMS: Pada1-u.p. [SOFT HYPHEN]
     cls.Linary[cls.Index - 1] = sktsh
  cls.chk_point("nityamsamase")

 @classmethod
 def atahkrkamikamsa(cls):
  """ generated source for method atahkrkamikamsa 
   8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya (samAse 45)
   Uses globals Linary,Index,Pada1,Pada2
   Modifies Linary
  """
  if cls.Compound:
   if (cls.Linary[cls.Index - 1] == sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], Ku_and_Pu)) and (cls.Index > 2):
    if (cls.Linary[cls.Index - 2] == skta):
     if (cls.Pada2 == "kAra") or (cls.Pada2 == "kAma") or (cls.Pada2 == "kaMsa") or (cls.Pada2 == "kumBa") or (cls.Pada2 == "kumBI") or (cls.Pada2 == "pAtra") or (cls.Pada2 == "kuSA") or (cls.Pada2 == "karRI"):
      if not ((cls.Pada1 == "svar") or (cls.Pada1 == "antar") or (cls.Pada1 == "prAtar") or (cls.Pada1 == "punar") or (cls.Pada1 == "sanutar") or (cls.Pada1 == "hyas") or (cls.Pada1 == "Svas") or (cls.Pada1 == "avas") or (cls.Pada1 == "aDas")) and (not cls.Uttarapada):
       cls.Linary[cls.Index - 1] = skts
  # PMS: miTas, namas, (tiraskAra by 8.3.42.  avaskara, namaskAra?)
  # krtvasuc, suc, i.e. not avyaya

  cls.chk_point("atahkrkamikamsa")

 @classmethod
 def stohscunascuh(cls):
  """ generated source for method stohscunascuh 
   8.4.40.  stoH ScunA ScuH
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  Isthana = int()
  Iyatna = int()
  if (cls.set_memberP(cls.Linary[cls.Index - 1], Tu_and_skts)) and (cls.set_memberP(cls.Linary[cls.Index + 1], Cu_and_sktsch)):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index - 1] = Soundary[italavya][cls.Iyatna1]
  elif (cls.set_memberP(cls.Linary[cls.Index - 1], Cu_and_sktsch)) and (cls.Linary[cls.Index + 1] == skts):
   cls.Linary[cls.Index + 1] = sktsch
   if (cls.Index + 2 < cls.linmax):
    if cls.Linary[cls.Index + 2] == skts:
     cls.Linary[cls.Index + 1] = sktsch
  elif (cls.set_memberP(cls.Linary[cls.Index - 1], Cu)) and (cls.set_memberP(cls.Linary[cls.Index + 1], Tu)):
   # PMS: 8.4.44.  SAt. (na, toH)
   temp = cls.identify(cls.Linary[cls.Index + 1])
   cls.Isthana2 = temp[0]
   cls.Iyatna2 = temp[1]
   cls.Linary[cls.Index + 1] = Soundary[italavya][cls.Iyatna2]
   if (cls.Index + 2 < cls.linmax):
    if cls.set_memberP(cls.Linary[cls.Index + 2], Tu_and_skts):
     temp = cls.identify(cls.Linary[cls.Index + 2])
     Isthana = temp[0]
     Iyatna = temp[1]
     cls.Linary[cls.Index + 2] = Soundary[italavya][Iyatna]
  cls.chk_point("stohscunascuh")

 @classmethod
 def stunastuh(cls):
  """ generated source for method stunastuh 
   8.4.41.  zwunA zwuH
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  Isthana = int()
  Iyatna = int()
  if ((cls.Linary[cls.Index - 1] == sktsh) and (cls.set_memberP(cls.Linary[cls.Index + 1], Tu_and_skts))) or (cls.set_memberP(cls.Linary[cls.Index - 1], Retrotu) and (cls.Pada2 == "nAm")):
   # PMS: 8.4.42.  na padAntAwworanAm
   temp = cls.identify(cls.Linary[cls.Index + 1])
   cls.Isthana2 = temp[0]
   cls.Iyatna2 = temp[1]
   cls.Linary[cls.Index + 1] = Soundary[imurdhanya][cls.Iyatna2]
   if (cls.Index + 2 < cls.linmax):
    if cls.set_memberP(cls.Linary[cls.Index + 2], Tu_and_skts):
     temp = cls.identify(cls.Linary[cls.Index + 2])
     Isthana = temp[0]
     Iyatna = temp[1]
     cls.Linary[cls.Index + 1] = Soundary[imurdhanya][cls.Iyatna2]
     cls.Linary[cls.Index + 2] = Soundary[imurdhanya][Iyatna]
  elif (cls.set_memberP(cls.Linary[cls.Index - 1], Tu) and (cls.set_memberP(cls.Linary[cls.Index + 1], Retrotu))) or ((cls.Linary[cls.Index - 1] == skts) and (cls.set_memberP(cls.Linary[cls.Index + 1], Retrotu_sktsh))):
   # PMS: 8.4.43.  toH zi. (na)
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index - 1] = Soundary[imurdhanya][cls.Iyatna1]
  cls.chk_point("stunastuh")

 @classmethod
 def anusvarasya(cls):
  """ generated source for method anusvarasya 
   8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58)
   PMS: don"t exercise the option for semivowels (yan) just now
   Uses globals Linary,Index
   Modifies Linary,Isthana2,Iyatna2
  """
  if (cls.Linary[cls.Index - 1] == sktanusvara) and (cls.set_memberP(cls.Linary[cls.Index + 1], Yay_not_Yan)):
   temp = cls.identify(cls.Linary[cls.Index + 1])
   cls.Isthana2 = temp[0]
   cls.Iyatna2 = temp[1]
   cls.Linary[cls.Index - 1] = Soundary[cls.Isthana2][isparsa5]
  cls.chk_point("anusvarasya")

 @classmethod
 def torli(cls):
  """ generated source for method torli 
   8.4.60.  tor li
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Index,Error
  """
  if (cls.set_memberP(cls.Linary[cls.Index - 1], Tu)) and (cls.Linary[cls.Index + 1] == sktl):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index - 1] = sktl
   if cls.Iyatna1 == isparsa5:
    cls.insertary(sktnasalization, cls.Index - 1)
    if cls.NoSpace:
     cls.Error = 2
     return
    cls.Index = cls.Index + 1
  cls.chk_point("torli")

 @classmethod
 def jhayoho(cls):
  """ generated source for method jhayoho 
   8.4.62.  jhayo ho 'nyatarasyAm
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1
  """
  if (cls.set_memberP(cls.Linary[cls.Index - 1], Jhay)) and (cls.Linary[cls.Index + 1] == skth):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index + 1] = Soundary[cls.Isthana1][isparsa4]
  cls.chk_point("jhayoho")

 @classmethod
 def saschoti(cls):
  """ generated source for method saschoti 
   8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
   Uses globals Linary,Index
   Modifies Linary
  """
  if (cls.set_memberP(cls.Linary[cls.Index - 1], Jhay)) and ((cls.Index + 2) < cls.linmax):
   if (cls.Linary[cls.Index + 1] == sktsch) and (cls.set_memberP(cls.Linary[cls.Index + 2], At)):
    # PMS: vt. chatvamamIti vaktavyam:  
    # Am instead of At.  tacchlokena, tacchmaSruRA
    cls.Linary[cls.Index + 1] = sktch
  cls.chk_point("saschoti")

 @classmethod
 def yaronunasike(cls):
  """ generated source for method yaronunasike 
   8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
  """
  temp = cls.identify(cls.Linary[cls.Index + 1])
  cls.Isthana2 = temp[0]
  cls.Iyatna2 = temp[1]
  # PMS: if ( set_memberP(Linary[Index - 1],Yar) && (Index + 2 < linmax) then
  # PMS: if (Iyatna2 eq isparsa5) || (Linary[Index + 2] == sktanunasika ) {
  # PMS: we won't exercise the nasalized option for the semivowels 
  #      y, v && l; just for the stops
  if (cls.set_memberP(cls.Linary[cls.Index - 1], Jhay)) and (cls.Iyatna2 == isparsa5):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index - 1] = Soundary[cls.Isthana1][isparsa5]
  cls.chk_point("yaronunasike")

 @classmethod
 def kharica(cls):
  """ generated source for method kharica 
   8.4.55.  khari ca. (jhalAm 53, car 54)
   PMS: there is no final  "h" after jhalAm jaSo "nte, 
     but there is skts by 8.3.34 visarjanIyasya saH
     && sktsch && sktsh by 
     8.4.40-41 stoH ScunA scuH, zwunA zwuH so must exclude Sar
   Uses globals Linary,Index
   Modifies Linary,Isthana1,Iyatna1
  """
  if cls.set_memberP(cls.Linary[cls.Index - 1], Jhay):
   # PMS: jhay=jhal-Sar
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   if cls.set_memberP(cls.Linary[cls.Index + 1], Khar_and_linend):
    # PMS: 8.4.56.  vavasane
    cls.Linary[cls.Index - 1] = Soundary[cls.Isthana1][isparsa1]
  cls.chk_point("kharica")

 @classmethod
 def idudeddvivacanampragrhyam(cls):
  """ generated source for method idudeddvivacanampragrhyam 
   1.1.11. IdUdeddvivacanam pragfhyam
   Uses globals Linary,Index,Pada1
   Modifies Linary,Pragrhya
  """
  # PMS: 1.1.11. IdUdeddvivacanam pragfhyam
  cls.Pragrhya = False
  c = cls.Linary[cls.Index - 1]
  if cls.External:
   if c == sktii:
    if (cls.Pada1 == "amI") or (cls.Pada1 == "aDiparI") or (cls.Pada1 == "aBipratI") or (cls.Pada1 == "manasI"):
     cls.Pragrhya = True
   elif c == sktuu:
    if (cls.Pada1 == "amU"):
     # PMS: 1.1.12.  adaso mAt
     cls.Pragrhya = True
   elif c == skte:
    if (cls.Pada1 == "SAlInakOpIne") or (cls.Pada1 == "uBe"):
     cls.Pragrhya = True
   elif c == skto:
    if (cls.Pada1 == "Aho") or (cls.Pada1 == "utAho"):
     # PMS: 1.1.15. ot
     cls.Pragrhya = True
  cls.chk_point("idudeddvivacanampragrhyam")

 @classmethod
 def sandhiPrep(cls):
  """ generated source for method sandhiPrep 
      This routine inadequately documented
  """
  L = int()
  IPada = int()
  NoPrep = bool()
  cls.NoStoh = False
  cls.NoKNam = False
  NoPrep = False
  cls.Exception = False
  cls.Pronoun = True # PMS: saú is usually the pronoun tad [LATIN SMALL LETTER U WITH ACUTE]
  cls.OtherCloseSandhi = False
  L = len(cls.Pada1)
  if L <= 1:
   return
  c = cls.Pada1[L-1] #  last character of Pada1. # cls.Pada1.substring(L - 1, L)
  if cls.dbg:
   print "sandhiPrep: Pada1='" + cls.Pada1 + "', c=" + c
   print "Is c = skts? %s" % (c == skts,)
   print "is Pada1 = us? %s" % (cls.Pada1 == "us",)
  if c == sktkn:
   #  RiN change made 20090801, PMS.
   if cls.Pada1 == "RiN":
    cls.Exception = True
  elif c == sktc:
   while IPada <= cantamax:
    if cls.Pada1 == CAntaPadary[IPada]:
     NoPrep = True
     cls.NoStoh = True
     IPada = cantamax #  leave loop
    IPada += 1
  elif c == sktj:
   if (cls.Pada1 == "tij"):
    cls.Exception = True
   elif (cls.Pada1 == "tuj"):
    NoPrep = True
  elif c == sktcn:
   if (cls.Pada1 == "aY") or (cls.Pada1 == "alaNkfY") or (cls.Pada1 == "nirAkfY") or (cls.Pada1 == "naY") or (cls.Pada1 == "wIwaY") or (cls.Pada1 == "WaY"):
    cls.NoStoh = True
  elif c == sktretron:
   if (cls.Pada1 == "aR") or (cls.Pada1 == "uR") or (cls.Pada1 == "yaR"):
    cls.Exception = True
  elif c == sktdh:
   if (cls.Pada1 == "aD") or (cls.Pada1 == "ruD"):
    cls.Exception = True
  elif c == sktn:
   if (cls.Pada1 == "Wan") or (cls.Pada1 == "tran") or (cls.Pada1 == "dozan") or (cls.Pada1 == "yakan") or (cls.Pada1 == "yUzan") or (cls.Pada1 == "Sakan") or (cls.Pada1 == "zWan") or (cls.Pada1 == "han"):
    NoPrep = True
   elif (cls.Pada1 == "Ayan") or (cls.Pada1 == "Gan"):
    #  if (!PaninianText)
    # PMS (June 2010)The whole section of sandhiPrep up to "if Compound"
    #  is aimed specifically at the Astadhyayi and perhaps other texts of
    #   Paninian grammar and should be excluded from general sandhi.
    if cls.PaninianText:
     NoPrep = True
     cls.NoKNam = True
   elif (cls.Pada1 == "ktin") or (cls.Pada1 == "kvin") or (cls.Pada1 == "min") or (cls.Pada1 == "vin"):
    NoPrep = True
   elif (cls.Pada1 == "an") or (cls.Pada1 == "in") or (cls.Pada1 == "kan") or (cls.Pada1 == "kaDyEn") or (cls.Pada1 == "qvun") or (cls.Pada1 == "tan") or (cls.Pada1 == "dAn") or (cls.Pada1 == "man") or (cls.Pada1 == "vun"):
    cls.Exception = True
   elif cls.Pada1 == "tumun":
    cls.NoStoh = True
  elif c == sktm:
   if (cls.Pada1 == "am") or (cls.Pada1 == "Am") or (cls.Pada1 == "num"):
    cls.Exception = True
   elif cls.Compound:
    if ((cls.Pada1 == "puram") and (cls.Pada2 == "dArO")):
     # PMS: purandrau
     cls.OtherCloseSandhi = True
  elif c == skty:
   if (cls.Pada1 == "ay") or (cls.Pada1 == "Ay"):
    cls.Exception = True
  elif c == sktr:
   if (cls.Pada1 == "car") or (cls.Pada1 == "kur") or (cls.Pada1 == "Sar"):
    cls.Exception = True
  elif c == sktsch:
   if (cls.Pada1 == "eS") or (cls.Pada1 == "KaS") or (cls.Pada1 == "jaS") or (cls.Pada1 == "niS"):
    cls.Exception = True
  elif c == sktsh:
   if (cls.Pada1 == "Jaz") or (cls.Pada1 == "Baz"):
    cls.Exception = True
  elif c == skts:
   cls.chk_point("sandhiPrep at c=skts:%s " % cls.Exception)
   if (cls.Pada1 == "as") or (cls.Pada1 == "atus") or (cls.Pada1 == "aTus") or (cls.Pada1 == "is") or (cls.Pada1 == "us") or (cls.Pada1 == "os") or (cls.Pada1 == "kas") or (cls.Pada1 == "kAs") or (cls.Pada1 == "Nas") or (cls.Pada1 == "tas") or (cls.Pada1 == "tAs") or (cls.Pada1 == "TAs") or (cls.Pada1 == "Bis") or (cls.Pada1 == "Byas"):
    cls.Exception = True
    cls.chk_point("sandhiPrep setting Exception to %s" % cls.Exception)
  if cls.Compound:
   # PMS: normal stem changes
   if (not cls.Exception) and (not NoPrep):
    c = cls.Linary[cls.Index - 1]
    if c == sktc:
     if cls.Pada1 == "aYc":
      # PMS: aYc
      cls.Linary[cls.Index - 1] = sktk # PMS: ak
      cls.deletary(cls.Index - 2)
      cls.Index = cls.Index - 1
     else:
      cls.Linary[cls.Index - 1] = sktk
    elif c == sktch:
     cls.Linary[cls.Index - 1] = sktk
    elif c == sktj:
     if (cls.Pada1 == "rAj"):
      cls.Linary[cls.Index - 1] = sktretrot
     else:
      cls.Linary[cls.Index - 1] = sktk
    elif c == sktjh:
     cls.Linary[cls.Index - 1] = sktk
    elif c == sktn:
     if cls.Index > 2:
      if (cls.Linary[cls.Index - 2] == skta) or (cls.Linary[cls.Index - 2] == skti):
       # PMS: an-/in-
       if ((cls.Pada1 == "ahan") and (not cls.PurvaPada == "eka")):
        #  noop
        pass
       else:
        # PMS: normal "an-"/"in-"
        cls.deletary(cls.Index - 1)
        cls.Index = cls.Index - 1
      # PMS: an-/in- (end)
    elif c == sktr:
     if (cls.Pada1 == "pur") or (cls.Pada1 == "Dur"):
      cls.Linary[cls.Index - 2] = sktuu
    elif c == sktsch:
     if cls.Pada1 == "viS":
      cls.Linary[cls.Index - 1] = sktretrot
     else:
      cls.Linary[cls.Index - 1] = sktk
    elif c == sktsh:
     if cls.Pada1 == "daDfz":
      cls.Linary[cls.Index - 1] = sktk
    elif c == skts:
     if (cls.Pada1 == "ASis"):
      cls.Linary[cls.Index - 2] = sktii # PMS: 82104
     elif cls.Pada1 == "pums":
      # PMS: "pum"
      cls.deletary(cls.Index - 1)
      cls.Index = cls.Index - 1
    else:
     # PMS: no preparation necessary, normal sandhi will follow
     pass
    # PMS: case statement (end)
   # PMS: astadhyayiSandhiPrep (end)
  # PMS: sandhiprep

 @classmethod
 def sandhiSplit(cls, x):
  """ generated source for method sandhiSplit 
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

 @classmethod
 def sandhi1(cls, s):
  """ generated source for method sandhi1 
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
   if not cls.dbg:
    print "Turning on debug. To turn off, enter 'off'"
    cls.dbg = True
   else:
    print "Turning off debug. To turn on, enter 'dbg'"
    cls.dbg = False
   return ""
  s1 = " " + s1 + "    "
  #cls.Linary = s1.split("")
  #cls.Linary = list(s1)
  # Java adds an empty string at the beginning with s1.split("")
  #print "sandhi1: s=%s, s1=%s" %(s,s1)
  cls.Linary = [""] + list(s1) #  this is what sandhimain modifies.
  cls.linmax = len(cls.Linary) - 1
  #print "Linary=[" + ",".join(cls.Linary) + "]"
  cls.chk_point("calling sandhimain with:'" + "".join(cls.Linary) + "'")
  cls.Error = 0
  cls.sandhimain()
  if cls.NoSpace and (cls.Error == 2):
   #  change of June 22, 2010
   cls.Error = 0
  if cls.Error != 0:
   #  if ((Error != 0) && (!((NoSpace && (Error == 2))))) ...
   print "Sandhi error: " + cls.Error + ", s = " + s
   return ""
  else:
   ans = "".join(cls.Linary)
   ans = ans.strip()
   return (ans)

 @classmethod
 def sandhimain(cls):
  """ generated source for method sandhimain 
 
  """
  #  initialize some global variables
  cls.Isthana1 = 0
  cls.Isthana2 = 0
  cls.Iyatna1 = 0
  cls.Iyatna2 = 0
  cls.IEnd = 0
  cls.Index = 0
  cls.Found = False
  cls.NoSpace = False
  cls.Dhralopa = False
  cls.OtherCloseSandhi = False
  cls.Pragrhya = False
  cls.Uttarapada = False
  cls.NxtUttarapada = False
  #   initialize some local variables
  Inext = 0
  Inextsp = 0
  IPrev = 0
  IPrevSpace = 0
  I = 0
  cls.PurvaPada = ""
  cls.Pada1 = ""
  cls.Pada2 = ""
  # PMS: the first character in Linary should not be a word boundary
  cls.Index = cls.nxtposary(cls.Padbound, cls.FldChr, 2)
  cls.chk_point("sandhimain. Initial Index = %s" % cls.Index)
  cls.Upasarga = False #  ejf.
  while cls.Index > 0:
   # print "Index="+Index;
   # PMS: while a padbound character is found
   cls.EkahPurvaParayoh = False
   # PMS: PurvaPada, Pada1, Pada2
   cls.Uttarapada = False
   if cls.NxtUttarapada:
    cls.Uttarapada = True # PMS: Pada1 is an uttarapada
   cls.NxtUttarapada = False
   # PMS: first Pada1 in Linary
   cls.PurvaPada = cls.Pada1
   if IPrev == 0:
    # PMS: first Pada1 in Linary
    if cls.Compound:
     IPrev = cls.lastposary(space, cls.Index - 1)
    else:
     # July 2010.  On the first pass, Pada1 is known to begin with
     #  a blank, unless the following is done.
     IPrev = cls.lastposary(space, cls.Index - 1)
    cls.chk_point("sandhimain: Index=%s, IPrev=%s" %(cls.Index,IPrev))
    cls.Pada1 = cls.substrary(IPrev + 1, cls.Index - 1)
    cls.chk_point("sandhimain. Pada1='%s',  Compound=%s, IPrev=%s, Index=%s"  %(cls.Pada1,cls.Compound,IPrev, cls.Index))
   elif cls.External:
    # PMS: we've been through here before so
    cls.Pada1 = cls.Pada2
   else:
    # PMS: padbound=hyphen
    cls.Pada1 = cls.NxtPada1
   Inext = cls.nxtposary(cls.Padbound, cls.FldChr, cls.Index + 1)
   if Inext == 0:
    # PMS: not found so last word
    Inext = cls.lengthary() + 1
   if cls.External:
    cls.Pada2 = cls.substrary(cls.Index + 1, Inext - 1)
   else:
    # PMS: for compound, Pada2, NxtPada1
    Inextsp = cls.nxtposary(space, cls.FldChr, cls.Index + 1)
    if (Inextsp > 0) and (Inextsp < Inext):
     cls.Pada2 = cls.substrary(cls.Index + 1, Inextsp - 1)
    else:
     cls.Pada2 = cls.substrary(cls.Index + 1, Inext - 1)
    # PMS: now the next Pada1 when padbound =hyphen
    IPrevSpace = cls.lastposary(space, Inext - 1)
    if IPrevSpace > cls.Index:
     cls.NxtPada1 = cls.substrary(IPrevSpace + 1, Inext - 1) #  corrected
    else:
     cls.NxtPada1 = cls.Pada2
     cls.NxtUttarapada = True
   # PMS: Pada2, NxtPada1 hyphen (end)
   # PMS: end of PurvaPada, Pada1, Pada2
   # PMS: determine whether Pada1 is an upasarga
   cls.Upasarga = False
   if cls.External and (cls.Pada1 == "ut"):
    cls.Pada1 = "ud"
   if cls.Pada1 == "api":
    # PMS: more likely karmapravacanIya than upasarga
    pass 
   else:
    i = 1
    while I <= pradimax:
     if cls.Pada1 == Pradi[I]:
      cls.Upasarga = True
      I = pradimax # to leave loop
     I += 1
   # PMS: stem final sound changes for compound sandhi && some 
   #      special sandhi for grammatical technical terms
   cls.sandhiPrep()
   doSandhi = True
   cls.chk_point("sandhimain, Exception =%s " % cls.Exception)
   if cls.Exception:
    doSandhi = False
   else:
    if cls.Upasarga and cls.CloseUpasargaSandhi:
     cls.OtherCloseSandhi = True # PMS: initialized in sandhiPrep
    # PMS: sandhi subroutines:  within compound && following an upasarga 
    # closer sandhi is observed when an option is allowed
    # PMS: otherwise (between syntactic units) looser sandhi is observed
    cls.idudeddvivacanampragrhyam() # PMS: kosher exceptions to sandhi
    if cls.Pragrhya:
     doSandhi = False
   if doSandhi:
    if (cls.Linary[cls.Index - 1] == sktvisarga):
     cls.visargaprep()
    temp = cls.identify(cls.Linary[cls.Index - 1])
    cls.Isthana1 = temp[0]
    cls.Iyatna1 = temp[1]
    temp = cls.identify(cls.Linary[cls.Index + 1])
    cls.Isthana2 = temp[0]
    cls.Iyatna2 = temp[1]
    # PMS: must precede 8.4.40.  stoH ScunA ScuH
    cls.checa() # PMS: 6.1.73.  che ca
    cls.anmanosca() # PMS: 6.1.74.  ANmANoSca (che 73, tuk 71)
    if (cls.TukPadantat):
     cls.padantadva() # PMS: 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
    # PMS: must precede vowel sandhi
    if cls.set_memberP(cls.Linary[cls.Index - 1], sktn_and_sktsh_and_skts):
     if cls.Pronoun:
      # PMS: 6.1.132.  etattadoH sulopo "kor anaYsamAse hali
      cls.etattadohsulopo() 
     # PMS: 8.2.70.  amnarUdharavarityubhayathA chandasi
     cls.amnarudharavar() 
     # PMS: 8.2.66.  sasajuzo ruH
     cls.sasajusoruh()
     if not cls.NoStoh:
      # PMS: exception in 63110
      # PMS: 8.2.68.  ahan
      cls.ahan()
     # PMS: 6.1.13.  ato ror aplutad aplute.  
     #      6.1.14.  haSi ca.  Must precede 6.1.109.  eNaH padAntAd ati
     cls.atororhasica()
    if cls.set_memberP(cls.Linary[cls.Index - 1], Ac) and cls.set_memberP(cls.Linary[cls.Index + 1], Ac):
     cls.acsandhi()
    elif (cls.set_memberP(cls.Linary[cls.Index - 1], Hal_and_ru)) and (cls.set_memberP(cls.Linary[cls.Index + 1], Al_and_Linend)):
     # PMS: 8.2.39.  jhalAM jaSo "nte
     cls.jhalamjasonte()
     # PMS: 8.3.7.  naS chavy apraSAn
     cls.naschavyaprasan()
     # PMS: 8.3.14.  ro ri  
     cls.rori()
     # ejf: Dhralopa is global
     # PMS: 6.3.111.  qhralope pUrvasya dIrgho "RaH
     cls.dhralope()
     # PMS: 8.3.17.  bhobhagoaghoapUrvasya yo "Si
     cls.bhobhago()
     # PMS: 8.3.15.  kharavasAnayor visarjanIyaH
     cls.kharavasanayor()
     # PMS: 8.3.20.  oto gArgyasya.  This cannot precede vowel sandhi
     cls.otogargyasya()
     # PMS: 8.3.23.  mo "nusvAraH
     cls.monusvarah()
     cls.chk_point("NoKNam = %s" % cls.NoKNam)
     if not cls.NoKNam:
      # PMS: 8.3.32.  Namo hrasvAd aci NamuR nityam
      cls.namohrasvad()
     # PMS: 8.3.34.  visarjanIyasya saH
     cls.visarjaniyasyasah()
     if cls.ScharSchari:
      # PMS: 8.3.36.  vA Sari
      cls.vasari()
     # PMS: 8.3.41, 8.3.45 && 8.3.46 are apavAdas of 8.3.37
     # so they must precede it
     # PMS: 8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39)
     cls.idudupadhasya()
     # PMS: 8.3 .45. nitya samAse "nutarapadasthasya
     cls.nityamsamase()
     # PMS: 8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya
     cls.atahkrkamikamsa()
     if cls.XkXpKupvoh:
      # PMS: 8.3.37.  kupvoH XkXpau ca (khari 15).
      cls.kupvohXkXpau()
     if not cls.NoStoh:
      # PMS: 8.4.40.  stoH ScunA ScuH
      cls.stohscunascuh()
      # PMS: 8.4.41.  zwunA zwuH
      cls.stunastuh()
     # PMS: 8.4.60.  tor li
     cls.torli()
     if cls.ChAti:
      # PMS: 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
      cls.saschoti()
     # PMS: 8.4.62.  jhayo ho "nyatarasyAm
     cls.jhayoho()
     # PMS: 8.4.55.  khari ca
     cls.kharica()
     if cls.ParaSavarna or cls.OtherCloseSandhi:
      # PMS: 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
      cls.anusvarasya()
    if (cls.set_memberP(cls.Linary[cls.Index - 1], Hal)) and (cls.set_memberP(cls.Linary[cls.Index + 1], Al)):
     # PMS: must follow vowel sandhi
     # PMS: 8.3.19.  lopaH SAkalyasya.  Must follow 6.1.78.  eco "yavAyAvaH
     cls.lopahsakalyasya()
     #  PMS: If made to include semivowels, 8.4.45 must follow 8.3.19-20. 
     #   In present form it needn't.
     if cls.Anunasika or cls.OtherCloseSandhi:
      # PMS: 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
      cls.yaronunasike()
   cls.chk_point("label7000a. Index=%s"%cls.Index)
   # PMS: get rid of the space between words
   if cls.EkahPurvaParayoh:
    # PMS: EkahPurvaParayoh set in acsandhi in subroutines: 
    #   akahsavarnedirghah, adgunah, vrddhireci
    # PMS: do the same steps if two padbounds in a row 
    #   because last sandhi eliminated single char word
    cls.deletary(cls.Index)
    # PMS: the search for the next padbound begins at Index+1
    cls.Index = cls.Index - 1
   elif (cls.Index > 1) and cls.Despace:
    if cls.set_memberP(cls.Linary[cls.Index - 1], Hal):
     # PMS: Removed "or Upasarga"
     cls.deletary(cls.Index)
   if cls.Linary[cls.Index] == hyphen:
    cls.deletary(cls.Index)
    cls.Index = cls.Index - 1
   IPrev = cls.Index
   cls.chk_point("label7000b(0): Padbound=%s, FldChr=%s, Index=%s" %(cls.Padbound, cls.FldChr, cls.Index + 1))
   # PMS: find the next pada boundary
   cls.Index = cls.nxtposary(cls.Padbound, cls.FldChr, cls.Index + 1)
   cls.chk_point("label7000b")
   if cls.dbg:
    print "label7000b(1) Index = %s" % cls.Index
  # PMS: conclude while loop when padbound character is not found (Index=0)

 @classmethod
 def sandhi(cls, s):
  """ generated source for method sandhi 
   Accept string argument, to which sandhi is to be applied.
   Return a string argument as the answer
   Return a blank string if there is an error
   Print an informative message if there is an error.
  """
  dbg = False
  dbgPrint(dbg,"sandhi. s=%s" % s)
  split = cls.sandhiSplit(s)
  
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
    y = cls.sandhi1(x)
    dbgPrint(dbg,"sandhi(after sandhi1) y=%s" %y)
   else:
    y = x
   y = whitebeg + y + whiteend
   ans += y
   i += 2
  return ans

 @classmethod
 def join(cls, strings, separator):
  """ generated source for method join 
   @param strings
   @param separator
   @return
  """
  sb = StringBuffer()
  i = 0
  while len(strings):
   if i != 0:
    sb.append(separator)
   sb.append(strings[i])
   i += 1
  return sb.__str__()

 @classmethod
 def chk_point(cls, s):
  """ generated source for method chk_point 
   a debugging routine. If global 'dbg' value is true, then
   a debugging message is printed labeled with the parameter 's'
   @param s
  """
  if cls.dbg:
   out = "%s(%s,%s): %s:%s" %(s,cls.Index,cls.linmax,cls.NoSpace,"".join(cls.Linary))
   print out
   #print s + "(" + cls.Index + "," + cls.linmax + "):" + cls.NoSpace + ":" + "".join(cls.Linary)

 @classmethod
 def main(cls, args):
  """ generated source for method main """
  if 0 == 1:
   err = cls.sandhioptions("E", "N", "S", "Y")
   print "sandhioptions err=" + err
   print "x=" + x + " => " + y
  if 0 == 1:
   print "s = " + s
   while len(split):
    print i + ":" + split[i]
    i += 1
  if 0 == 1:
   if b:
    print "s=" + s + ",$1=" + m.group(1) + ",$2=" + m.group(2)
   else:
    print "No match"
  if 0 == 1:
   s[0] = "abc"
   s[1] = "def"
   print "s1=" + s1
  if 0 == 0:
   cls.dbg = True
   cls.dbg = False
   #cls.sandhi("dbg")
   cls.sandhioptions("C", "N", "S", "")
   s = "tat-gam"
   s1 = cls.sandhi(s)
   print (s + " => " + s1)
   #
   cls.sandhioptions("E", "N", "S", "Y")
   s = "rAmaH agacCat"
   s1 = cls.sandhi(s)
   print s + " => " + s1
  if 0 == 0:
   cls.dbg = False
   cls.dbg = True
   cls.sandhioptions("E", "N", "S", "N")
   s = "yan agacCat"
   print "-----------test of " + s
   s1 = cls.sandhi(s)
   print s + " => " + s1
  if 0 == 1:
   cls.sandhioptions("C", "N", "S", "")

if __name__ == '__main__':
 import sys
 ScharfSandhi.main(sys.argv)

