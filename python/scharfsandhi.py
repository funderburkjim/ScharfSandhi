# coding=utf-8
#!/usr/bin/env python
""" generated source for module ScharfSandhi """
# 
#  * Java implementation of 'sandhi' routine from SandhiGen.pp (PMS 2000/10/14)
#  * This is derived from the Perl implementation 'sandhi.pm' of Feb 9, 2009.
#  * Jim Funderburk
#  * June 2010
#  
# package org.sanskritlibrary.scharfsandhi;
# package scharfsandhi;
#import java.util

#import java.util.regex
import re
#@classmethod
#def diff_string(cls, x, y):
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

 
 
class ScharfSandhi(object):
 """ generated source for class ScharfSandhi """

 # 
 #   * The Sanskrit sounds represented in the font Sanskrit01
 #   * These are Strings of length 1, so could have been declared 'char'
 #   * However, it was felt that treating them as String objects was conceptually
 #   * simpler, and probably insignificantly less efficient.
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

 #  changed from"""";
 sktsvarita = "^"

 # {opt i space.  It precedes the sound it accents}
 sktudattaa = ""
 sktudattai = ""
 sktudattau = ""
 sktudattae = ""
 sktudattao = ""
 sktudattaai = ""
 sktsvaritaa = "	"
 sktsvaritai = ""
 sktsvaritau = ""
 sktsvaritae = ""
 sktsvaritao = ""
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

 #  Neutral characters
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
 sktudatta = "«"; #{opt e space.  It precedes the sound it accents}
 sktudattaaa = "§";
 sktudattaii = "ª";
 sktudattauu = "²";
 sktudattaau = "®";
 sktsvaritaaa = "¥";
 sktsvaritaii = "«";
 sktsvaritauu = "³";
 sktsvaritaai = "¦";
 sktsvaritaau = "¯";

 #  (ejf)What is 'CAntaPadary' supposed to be? It is coded as sets of chars
 #  The string is populated in init_CAntaPadary
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

 #  Pradi array of strings: prefixes
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

 #  various character sets. Since Sanskrit01 uses 1 ascii character to
 #  represent elements of the Sanskrit alphabet, these sets may be
 #  represented as character strings.
 #  Since the Sanskrit characters are represented as Java Strings,
 #  the 'union' of sets may be uniformly represented with Java '+'
 #  concatentaion of Strings.
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
 #  These are sets that were referenced by inline Pascal
 #  set construction operators. In conversion to Perl,
 #  it was convenient to construct these initialially and
 #  given then new names.
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

 #  initialize Soundary, and related constants
 maxyatna = 11
 maxsthana = 5

 #  private static final String[] Pradi = new String[1+pradimax];
 #Soundary = " "*maxsthana # ejf [None]*1 + maxsthana
 # Soundary is 2-dimensional array of strings of dimension
 # (1+maxsthana) (by 1+maxyatna)
 Soundary = []
 for i in xrange(0,1+maxsthana):
  Soundary.append(['' for j in xrange(0,1+maxyatna)])
 #  constants for first coord of Soundary
 ikanthya = 1
 italavya = 2
 imurdhanya = 3
 idantya = 4
 iosthya = 5

 #  second coord of Soundary
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
 linmax = int() # resolves to 0 in Python
 pratipadmax = 20

 # PMS Maximum length assumed for lexical items
 iapi = 13

 # PMS api usually is not an upasarga so check it separately
 #  variables global to sandhi routines
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

 #  initialize Soundary
 #  currently this routine does nothing.
 # 
 #   * 
 #   * @param x 
 #   * @param y
 #   * @return a String containing those characters of x which
 #   * are not in y.
 #   
 #   print "diff_string: x="+x + ", y=" + y + ", ans="+ ans;
 #  c is a char ,implemented as a string of length 1
 #  set is a "set of char", implemented as a string.
 # 
 #   * It returns 0 (ok) or 4 (error)
 #   * @param compound_ans C for compound sandhi, E for External sandhi
 #   * @param vedic_ans  Y or N
 #   * @param closeSandhi_ans N,Y,S
 #   * @param despace_ans Y or N
 #   
 #  initialize external flags to false.
 # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
 # PMS 8.3.36.  vA Sari
 # PMS 8.3.37.  kupvoH XkXpau ca.
 # PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
 # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
 # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 #  process vedic answer
 #  print "Is this a Vedic text (chandas)?\n";
 #  print "Default no: ";
 #  readln(Answer);
 # -- closeSandhi_ans
 #  print "Do you want to exercise close sandhi options?\n";
 #  print ""N" or "n" to decline\n";
 #  print ""Y" or "y" to accept\n";
 #  print ""S" or "s" to follow standard editorial practice\n";
 #  print "Any other character to select options individually: ";
 #  readln(Answer);
 # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
 # PMS 8.3.36.  vA Sari
 # PMS 8.3.37.  kupvoH XkXpau ca.
 # PMS 8.4.63.  SaS cho "Ti. (jhayaH 62, anyatarasyAm 62)
 # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
 # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 # PMS Close sandhi within compounds
 # PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
 # PMS 8.3.36.  vA Sari
 # PMS technically, 8.3.37 should also apply but it is never seen
 # PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
 # PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
 # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 # PMS display standard editorial practice for compound sandhi
 # PMS External: 8.4.63 and 8.4.45
 # PMS 8.4.63.  SaS cho "Ti. (jhayaH 62, anyatarasyAm 62)
 # PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 # print "The optional sandhi in the following sutras will apply:\n";
 # print "  8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
 # print "  8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62 ) . \n";
 # PMS disabled Close sandhi between upasargas and their following verb forms
 # PMS CloseUpasargaSandhi = true;
 # PMS print "Close sandhi will be observed between upasargas and their following verb forms\n";
 # PMS print "After the upasarga "sam",\n";
 # PMS print "  8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
 #  non-functioning. old code shown for possible reuse elsewhere
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
 # PMS peruse options
 # PMS Choose spacing options
 #   print "Hyphens will be deleted between compound elements.\n";
 # PMS spaceoptions
 #   print "Spaces will be deleted where a single vowel replaces final and initial vowels.\n";
 #   print "Do you wish to eliminate spaces between prefixes and verbs\n";
 #   print "and between final consonants and a following sound?\n";
 #   print "Y/y (yes) to delete spaces, any other character to keep.";
 #   readln(Answer);
 #   Answer = "Y"; //force despacing
 # PMS spaceoptions
 # 
 #   * returns position in Linary of the last character which is not a space;
 #   * returns 0 of all elements of Linary are spaces.
 #   
 # 
 #   * Searches Linary for either chtr or fldch. Returns of match.
 #   * Discounts trailing spaces.
 #   * @param chtr
 #   * @param fldch
 #   * @param istart
 #   * @return Returns -1 if istart is < 1 or > linmax
 #   *  Returns 0 if no match found in Linary
 #   *  Returns index (istart to linmax) of first match found.
 #   
 # 
 #   * Searches backward in Linary for first occurrence of given character
 #   * @param chtr character to search for
 #   * @param istart starting position
 #   * @return return -1 if istart is inappropriate
 #   * return 0 if chtr not found in Linary
 #   * return I if nearest occurrence (from istart down to 1) of chtr is at index I
 #   
 # error in conversion to Java  if (IEnd == 0){return 0;}
 # 
 #   * Insert character at given position in Linary.
 #   * If the position is prior to first position, it resets to first position
 #   * If position is after the last non-space position, it resets to first ending
 #   * non-space position.
 #   * Linary may be augmented by spaces, if necessary. Thus NoSpace will not be set to true.
 #   * @param chtr character to insert
 #   * @param index position of insertion
 #   
 #  add some more space to Linary
 # print "insertary: Augmenting Linary: linmax starts as " + linmax;
 #  this is what sandhimain modifies.
 #  print "insertary: linmax now " + linmax + ", IEnd= " + IEnd;
 # 
 #   * remove the character at position 'index' from Linary.
 #   * If index indexes a position after the last non-space, no character is deleted
 #   * @param index
 #   
 # 
 #   * Returns a substring of Linary consisting of (index1-index2)+1 characters beginning at index1
 #   * @param index1
 #   * @param index2
 #   * @return
 #   
 # 
 #   * Returns positions (Isthana and Iyatna) in Soundary matrix
 #   * where the character 'aksara' is found.
 #   * Returns (0,0) if not found.
 #   * @param aksara
 #   * @return
 #   
 # 
 #   * {1.1.9 vt. fkAra kArayoH savarRavidhiH}
 #   * uses globals Linary,Index.
 #   * May modify Linary,Isthana1,Isthana2
 #   
 # 
 #   * {6.1.101.  akaH savafRe dIrghaH}
 #   * Uses globals Linary,Index,Isthana1
 #   * Modifies Linary,EkahPurvaParayoh
 #   
 # {6.1.84.  ekaH pUrvaparayoH}
 # 
 #   * 6.1.88.  vfddhir eci
 #   * Uses globals Linary,Index,Isthana2
 #   * Modifies Linary,EkahPurvaParayoh
 #   
 # {6.1.84.  ekaH pUrvaparayoH}
 # 
 #   * 6..1.87.  Ad guRaH
 #   * Uses globals Linary,Index,Isthana2
 #   * Modifies Linary,EkahPurvaParayoh
 #   
 # {6.1.84.  ekaH pUrvaparayoH}
 # imurdhanya:
 # {1.1.51.  uraR raparaH}
 # idantya:
 # 
 #   * 6.1.77.  iko yaR aci
 #   * Uses globals Linary,Index,Isthana1
 #   * Modifies Linary
 #   
 # 
 #  * 6.1.109.  eNaH padAntAd ati
 #   * Uses globals Linary,Index
 #   * Modifies Linary
 #   
 # {}
 # 
 #  * 6.1.78.  eco 'yavAyAvaH
 #   * Uses globals Linary,Index
 #   * Modifies Linary,Index. May set Error
 #   
 # 
 #   * Uses globals Linary,Index,Isthana1,Isthana2
 #   * Modifies Linary,Index.
 #  * Calls: rlvarnayormithahsavarnyam, akahsavarnedirghah,vrddhireci,
 #  * adgunah,ikoyanaci,enahpadantadati,ecoyavayavah
 #   
 # {6.1.101.  akaH savafRe dIrghaH}
 # PMS: && Linary[Index+1] not in Avarna
 # PMS: 6.1.88  vfddhir eci
 # PMS: Linary[Index+1] in Ik
 # PMS: 6.1.87  Ad guRaH
 # PMS: Linary[Index-1] in Ik && not savarna with Linary[Index+1]
 # PMS: 6.1.77.  iko yaR aci
 # PMS: Linary[Index-1] in Ec
 # PMS: 6.1.109.  eNaH padAntAd ati
 # PMS: set_memberP(Linary[Index-1],Ec) && set_memberP(Linary[Index+1],Ic)
 # PMS: 6.1.78.  eco "yavAyAvaH
 # 
 #  * The substring of 'x' specified by idx1,idx2 is replaced by the string y.
 #  * @param x input string
 #  * @param idx1  first character position at which to replace (inclusive)
 #  * @param idx2  last character position at which to replace (exclusive)
 #  * @param y  string for replacement.
 #  * @return string resulting from replacement.
 #  
 # char[] ax = x.toCharArray();
 # 
 #  * Uses globals Pada1,Linary,Index
 #  * Modifies Pada1,Linary
 #  
 # 
 #  * 6.1.73.  che ca (tuk 71)
 #  * Uses globals Linary,Index,Iyatna1
 #  * Modifies Linary,Index,Error
 #  
 # 
 #  * 6.1.74.  ANmANoSca (che 73, tuk 71)
 #  * Uses globals Linary,Index,Pada1
 #  * Modifies Linary,Index,Error
 #  
 # PMS: you'll have to add the condition that these are AN && mAN when that info is available
 # 
 #  * 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
 #  * Uses globals Linary,Index,
 #  * Modifies Linary,Index,Error,Isthana1,Iyatna1
 #  
 # PMS: don"t want to do it if anmanosca just applied
 #  REPLACE exit(sandhi);
 # 
 #  * 6.1.132.  etattadoH sulopo "kor anaYsamAse hali
 #  * Uses globals Linary,Index,Pada1
 #  * Modifies Linary,Index
 #  
 # 
 #  * 8.2.39.  jhalAM jaSo 'nte
 #  * Uses globals Linary,Index,Pada1
 #  * Modifies Linary,Isthana1,Iyatna1
 #  
 # PMS: because ru =skts; I could choose another character
 # PMS: jhalamjasonte
 # 
 #  * Uses globals Linary,Index
 #  * Modifies Linary
 #  
 # PMS: 8.2.66.  sasajuzo ruH
 # PMS: exception to 8.2.39 so must apply before it
 # 
 #  * 8.2.68.  ahan
 #  * Uses globals Linary,Index,Pada1,Pada2
 #  * Modifies Linary
 #  
 # PMS: vArttika, but had to add rAtra 21045, rAtre 24028, rAtrARAm 33137
 # PMS: if ahan is termed pada && Pada2 in Sup, so that Linary[Index+1]=sktbh || skts, ditto
 # PMS: 8.2.69.  ro "supi
 # 
 #  * 8.2.70.  amnarUdharavarityubhayathA chandasi
 #  * Uses globals Linary,Index,Pada1
 #  * Modifies Linary
 #  
 # PMS: actually you get it both ways in chandas, ru too
 # 
 #  * 6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Index
 #  
 # PMS: Linary[Index-1=sktu; adguna
 # 
 #  * 8.3.7.  naS chavy apraSAn
 #  * Uses globals Linary,Index,Pada1
 #  * Modifies Linary,Index,Error
 #  
 # PMS: 8.3.4.  anunAsikAt paro "nusvAraH
 # 
 #  * 8.3.14.  ro ri
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Index,Dhralopa
 #  
 # 
 #  * 6.3.111.  qhralope pUrvasya dIrgho 'RaH
 #  * Uses globals Linary,Index,Dhralopa
 #  * Modifies Linary
 #  
 # 
 #  * 8.3.17.  bhobhagoaghoapUrvasya yo 'Si
 #  * Uses globals Linary,Index,Pada1
 #  * Modifies Linary
 #  
 # 
 #  * 8.3.15.  kharavasAnayor visarjanIyaH
 #  * Uses globals Linary,Index
 #  * Modifies Linary
 #  
 #  print "kharachk: '" + Linary[Index - 1] + "', '"+Linary[Index + 1]+"'" ;
 # 
 #  * 8.3.19.  lopaH SAkalyasya
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Index
 #  
 # 
 #  * 8.3.20.  oto gArgyasya
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Index
 #  
 # 
 #  * 8.3.23.  mo 'nusvAraH
 #  * Uses globals Linary,Index
 #  * Modifies Linary
 #  
 # 
 #  * 8.3.32.  Namo hrasvAd aci NamuR nityam
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Index,Error
 #  
 # 
 #  * 8.3.34.  visarjanIyasya saH
 #  * Uses globals Linary,Index
 #  * Modifies Linary
 #  
 #  type = boolean;
 # PMS: 8.3.35.  Sarpare visarjanIyaH.
 # PMS: 8.3.36.  vA Sari.  8.3.37.  kupvoH XkXpau ca.
 # 
 #  * 8.3.36.  vA Sari
 #  * Uses globals Linary,Index
 #  * Modifies Linary
 #  
 # 
 #  *  8.3.37.  kupvoH XkXpau ca (khari 15).
 #  *  8.3.41, 8.3.45 && 8.3.46 are apavAdas of this so must precede it.
 #  * Uses globals Linary,Index
 #  * Modifies Linary
 #  
 # PMS: by 8.3.15, kharavasAnayorvisarjanIyaH, visarga occurs before avasAna too.  but Xk && Xp don"t.
 # PMS: Hence, khari is understood here too
 # PMS: 8.3.35.  Sarpare visarjanIyaH.
 # 
 #  * 8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39
 #  * Uses globals Linary,Index,Pada1
 #  * Modifies Linary
 #  
 # PMS: exception to 8.3.36.  kupvoH XkaXpau ca, which is an exception to 8.3.34. visarjanIyasya saH,
 # PMS: so should accompany procedure visarjaniyasyasah.  Must follow 8.3.15.  kharavasAnayor visarjanIyaH
 # PMS: bahis, Avis =exception to 8.3.46
 # 
 #  * 8.3.45. nityamsamAse 'nutarapadasthasya
 #  * Uses globals Linary,Index
 #  * Modifies Linary
 #  
 # PMS: Pada1-u.p. [SOFT HYPHEN]
 # 
 #  * 8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya (samAse 45)
 #  * Uses globals Linary,Index,Pada1,Pada2
 #  * Modifies Linary
 #  
 # PMS: miTas, namas, (tiraskAra by 8.3.42.  avaskara, namaskAra?) krtvasuc, suc, i.e. not avyaya
 # 
 #  * 8.4.40.  stoH ScunA ScuH
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
 #  
 # PMS: 8.4.44.  SAt. (na, toH)
 # 
 #  * 8.4.41.  zwunA zwuH
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
 #  
 # PMS: 8.4.42.  na padAntAwworanAm
 # PMS: 8.4.43.  toH zi. (na)
 # 
 #  * 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58)
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Isthana2,Iyatna2
 #  
 # PMS: don"t exercise the option for semivowels (yan) just now
 # 
 #  * 8.4.60.  tor li
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Isthana1,Iyatna1,Index,Error
 #  
 # 
 #  * 8.4.62.  jhayo ho 'nyatarasyAm
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Isthana1,Iyatna1
 #  
 # 
 #  * 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
 #  * Uses globals Linary,Index
 #  * Modifies Linary
 #  
 # PMS: vt. chatvamamIti vaktavyam:  Am instead of At.  tacchlokena, tacchmaSruRA
 # 
 #  * 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
 #  
 # PMS: if ( set_memberP(Linary[Index - 1],Yar) && (Index + 2 < linmax) then
 # PMS: if (Iyatna2 eq isparsa5) || (Linary[Index + 2] == sktanunasika ) {
 # PMS: we wont exercise the nasalized option for the semivowels y, v && l; just for the stops
 # 
 #  * 8.4.55.  khari ca. (jhalAm 53, car 54)
 #  * Uses globals Linary,Index
 #  * Modifies Linary,Isthana1,Iyatna1
 #  
 # PMS: there is no final  "h" after jhalAm jaSo "nte, but there is skts by 8.3.34 visarjanIyasya saH
 # PMS: && sktsch && sktsh by 8.4.40-41 stoH ScunA scuH, zwunA zwuH so must exclude Sar
 # PMS: jhay=jhal-Sar
 # PMS: 8.4.56.  vavasane
 # 
 #  * 1.1.11. IdUdeddvivacanam pragfhyam
 #  * Uses globals Linary,Index,Pada1
 #  * Modifies Linary,Pragrhya
 #  
 # PMS: 1.1.11. IdUdeddvivacanam pragfhyam
 # PMS: 1.1.12.  adaso mAt
 # PMS: 1.1.15. ot
 # 
 #  * This routine inadequately documented
 # 
 # PMS: sa(u?ejf) is usually the pronoun tad [LATIN SMALL LETTER U WITH ACUTE]
 #  last character of Pada1.
 #  RiN change made 20090801, PMS.
 #  leave loop
 #  if (!PaninianText)
 # PMS (June 2010)The whole section of sandhiPrep up to "if Compound"
 #  is aimed specifically at the Astadhyayi and perhaps other texts of
 #   Paninian grammar and should be excluded from general sandhi.
 # PMS: purandrau
 # PMS: normal stem changes
 # PMS: aYc
 # PMS: ak
 # PMS: an-/in-
 #  noop
 # PMS: normal "an-"/"in-"
 # PMS: an-/in-
 # PMS: 82104
 # PMS: "pum"
 # PMS: no preparation necessary, normal sandhi will follow
 # PMS: case statement
 # PMS: astadhyayiSandhiPrep
 # PMS: sandhiprep
 # 
 #  * From a given input string, generate an array of strings.
 #  * The even elements (0,2,4...) of the array have value
 #  * "s" if the next array element is a string of Sanskrit characters
 #  * "o" if the next array element is a string of other non-Sanskrit characters
 #  * Sanskrit characters are according to the SLP1 spelling.
 #  * <p>
 #  * "- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/"
 #  * <p>
 #  * Note that the '/' is an artificial 'Sandhi-blocking' character.
 # 
 #  Only non-alphabetic chars considered to be Sanskrit are
 #  - and space and apostrophe and "|" and "/"
 #  20090801, "/" is a sandhi-blocking character.
 #  String sanskrit_str = "- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/";
 #  June 22: Added period to list of Sanskrit characters.
 #  state = OTHER
 #  should not occur
 # 
 #   * Prepare input for sandhimain
 #   * Accept string argument, to which sandhi is to be applied.
 #   * return a string argument as the answer
 #   * return a blank string if there is an error
 #   * print an informative message if there is an error.
 #  * Two special values of 's' are related to debugging: 'dbg' and 'off'
 # 
 #  this is what sandhimain modifies.
 #  change of June 22, 2010
 #  if ((Error != 0) && (!((NoSpace && (Error == 2))))){
 #  initialize some global variables
 #   initialize some local variables
 # PMS: the first character in Linary should not be a word boundary
 #  ejf.
 #   print "Index="+Index;
 # PMS: while a padbound character is found
 # PMS: PurvaPada, Pada1, Pada2
 # PMS: Pada1 is an uttarapada
 # PMS: first Pada1 in Linary
 # PMS: first Pada1 in Linary
 # July 2010.  On the first pass, Pada1 is known to begin with
 #  a blank, unless the following is done.
 # PMS: we've been through here before so
 # PMS: padbound=hyphen
 # PMS: not found so last word
 # PMS: for compound, Pada2, NxtPada1
 # PMS: now the next Pada1 when padbound =hyphen
 #  corrected
 # PMS: Pada2, NxtPada1 hyphen
 # PMS: end of PurvaPada, Pada1, Pada2
 # PMS: determine whether Pada1 is an upasarga
 # PMS: more likely karmapravacanIya than upasarga
 # to leave loop
 # PMS: stem final sound changes for compound sandhi && some special sandhi for grammatical technical terms
 # PMS: initialized in sandhiPrep
 # PMS: sandhi subroutines:  within compound && following an upasarga closer sandhi is observed when an option is allowed
 # PMS: otherwise (between syntactic units) looser sandhi is observed
 # PMS: kosher exceptions to sandhi
 # PMS: must precede 8.4.40.  stoH ScunA ScuH
 # PMS: 6.1.73.  che ca
 # PMS: 6.1.74.  ANmANoSca (che 73, tuk 71)
 # PMS: 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
 # PMS: must precede vowel sandhi
 # PMS: 6.1.132.  etattadoH sulopo "kor anaYsamAse hali
 # PMS: 8.2.70.  amnarUdharavarityubhayathA chandasi
 # PMS: 8.2.66.  sasajuzo ruH
 # PMS: exception in 63110
 # PMS: 8.2.68.  ahan
 # PMS: 6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca.  Must precede 6.1.109.  eNaH padAntAd ati
 # PMS: 8.2.39.  jhalAM jaSo "nte
 # PMS: 8.3.7.  naS chavy apraSAn
 # PMS: 8.3.14.  ro ri  ejf: Dhralopa is global
 # PMS: 6.3.111.  qhralope pUrvasya dIrgho "RaH
 # PMS: 8.3.17.  bhobhagoaghoapUrvasya yo "Si
 # PMS: 8.3.15.  kharavasAnayor visarjanIyaH
 # PMS: 8.3.20.  oto gArgyasya.  This cannot precede vowel sandhi
 # PMS: 8.3.23.  mo "nusvAraH
 # PMS: 8.3.32.  Namo hrasvAd aci NamuR nityam
 # PMS: 8.3.34.  visarjanIyasya saH
 # PMS: 8.3.36.  vA Sari
 # PMS: 8.3.41, 8.3.45 && 8.3.46 are apavAdas of 8.3.37 so they must precede it
 # PMS: 8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39)
 # PMS: 8.3 .45. nitya samAse "nutarapadasthasya
 # PMS: 8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya
 # PMS: 8.3.37.  kupvoH XkXpau ca (khari 15).
 # PMS: 8.4.40.  stoH ScunA ScuH
 # PMS: 8.4.41.  zwunA zwuH
 # PMS: 8.4.60.  tor li
 # PMS: 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
 # PMS: 8.4.62.  jhayo ho "nyatarasyAm
 # PMS: 8.4.55.  khari ca
 # PMS: 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
 # PMS: must follow vowel sandhi
 # PMS: 8.3.19.  lopaH SAkalyasya.  Must follow 6.1.78.  eco "yavAyAvaH
 # PMS: If made to include semivowels, 8.4.45 must follow 8.3.19-20.  In present form it needn"t.
 # PMS: 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 # PMS: get rid of the space between words
 # PMS: EkahPurvaParayoh set in acsandhi in subroutines: akahsavarnedirghah, adgunah, vrddhireci
 # PMS: do the same steps if two padbounds in a row because last sandhi eliminated single char word
 # PMS: the search for the next padbound begins at Index+1
 # PMS: Removed "or Upasarga"
 # PMS: find the next pada boundary
 # PMS: conclude while loop when padbound character is not found (Index=0)
 # 
 #   * Accept string argument, to which sandhi is to be applied.
 #   * Return a string argument as the answer
 #   * Return a blank string if there is an error
 #   * Print an informative message if there is an error.
 # 
 #  the doubling '\\' is a Java quirk of string literals
 #  \s is whitespace
 # 
 #  * 
 #  * @param strings
 #  * @param separator
 #  * @return
 #  
 # 
 #   * a debugging routine. If global 'dbg' value is true, then
 #   * a debugging message is printed labeled with the parameter 's'
 #   * @param s
 #   
 # dbg=true;
 @classmethod
 def init(cls):
  """ generated source for method init """


 @classmethod
 def set_memberP(cls, c, s):
  """ generated source for method set_memberP """
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
  return x.strip() # x.trim()

 @classmethod
 def sandhioptions(cls, compound_ans, vedic_ans, closeSandhi_ans, despace_ans):
  """ generated source for method sandhioptions """
  #Answer = str()
  Yes = "Y"
  No = "N"
  error = 0
  cls.Despace = False
  cls.External = False
  cls.Compound = False
  cls.Chandas = False
  cls.CloseUpasargaSandhi = False
  cls.TukPadantat = False
  cls.ScharSchari = False
  cls.XkXpKupvoh = False
  cls.ChAti = False
  cls.ParaSavarna = False
  cls.Anunasika = False
  Answer = compound_ans.upper()
  if Answer == "":
   Answer = "?"
  if Answer == "C":
   cls.Compound = True
   cls.Padbound = cls.hyphen
  elif Answer == "E":
   cls.External = True
   cls.Padbound = cls.space
  else:
   cls.Error = 4
   return cls.Error
  #print "sandhioptions: Padbound='%s'" % cls.Padbound 
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
  Answer = closeSandhi_ans.upper()
  if Answer == "":
   Answer = "?"
  if Answer == "Y":
   cls.TukPadantat = True
   cls.ScharSchari = True
   cls.XkXpKupvoh = True
   cls.ChAti = True
   cls.ParaSavarna = True
   cls.Anunasika = True
  elif Answer == "N":
   cls.TukPadantat = False
   cls.ScharSchari = False
   cls.XkXpKupvoh = False
   cls.ChAti = False
   cls.ParaSavarna = False
   cls.Anunasika = False
  elif Answer == "S":
   if cls.Compound:
    cls.TukPadantat = True
    cls.ScharSchari = True
    cls.ChAti = True
    cls.ParaSavarna = True
    cls.Anunasika = True
   else:
    cls.ChAti = True
    cls.Anunasika = True
    #if cls.dbg:  // ejf commented out
  else:
   cls.Error = 4
   return (cls.Error)
  if cls.Compound:
   pass # ejf
  elif cls.External:
   Answer = despace_ans
   if Answer == "":
    Answer = "?"
   if Answer == "Y":
    cls.Despace = True
   elif Answer == "N":
    cls.Despace = False
   else:
    cls.Error = 4
    return (cls.Error)
  cls.Error = 0
  return cls.Error

 @classmethod
 def lengthary(cls):
  """ generated source for method lengthary """
  I = cls.linmax
  dbgPrint(False,"lengthary. Linary has length=%s, linmax=%s\nLinary=%s" %(len(cls.Linary),cls.linmax,cls.Linary))
  while 1 <= I:
   if not (cls.Linary[I] == " "):
    return I
   I -= 1
  return 0

 @classmethod
 def nxtposary(cls, chtr, fldch, istart):
  """ generated source for method nxtposary """
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
  """ generated source for method lastposary """
  if istart < 1:
   return -1
  if istart > cls.linmax:
   return -1
  I = istart
  while 1 <= I:
   if cls.Linary[I] == chtr:
    return I
   I -= 1
  return 0

 @classmethod
 def insertary(cls, chtr, index):
  """ generated source for method insertary """
  cls.NoSpace = False
  IEnd = cls.lengthary()
  if IEnd == cls.linmax:
   #print "insertary: Augmenting Linary: linmax starts as ", cls.linmax,len(cls.Linary)
   #print "Linary=",cls.Linary
   s1 = "".join(cls.Linary)
   #print "s1='%s'"% s1
   #print "s1 length=",len(s1)
   s1 = s1 + "          "  # 10 spaces
   #print "s1 length (after padding)=",len(s1)
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
  """ generated source for method deletary """
  IEnd = cls.lengthary()
  if (index >= 1) and (index <= IEnd):
   I = index
   while I < IEnd:
    cls.Linary[I] = cls.Linary[I + 1]
    I += 1
   cls.Linary[IEnd] = ""

 @classmethod
 def substrary(cls, index1, index2):
  """ generated source for method substrary """
  Tempstr = [] #StringBuffer()
  ans = ""
  IEnd = cls.lengthary()
  if (index1 < 1) or (index1 > index2) or (index2 > IEnd):
   return ans
  if ((index2 - index1) + 1) > cls.pratipadmax:
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
  """ generated source for method identify """
  #I1 = int()
  #I2 = int()
  ans = [0,0] # " "*2 # ejf [None]*2
  I1 = 1
  while I1 <= cls.maxsthana:
   I2 = 1
   while I2 <= cls.maxyatna:
    if aksara == cls.Soundary[I1][I2]:
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
  """ generated source for method rlvarnayormithahsavarnyam """
  if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Rvarna_and_Lvarna)) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Rvarna_and_Lvarna)):
   cls.Linary[cls.Index - 1] = cls.sktri
   cls.Linary[cls.Index + 1] = cls.sktri
   cls.Isthana1 = cls.imurdhanya
   cls.Isthana2 = cls.imurdhanya
  cls.chk_point("rlvarnayormithahsavarnyam")

 @classmethod
 def akahsavarnedirghah(cls):
  """ generated source for method akahsavarnedirghah """
  cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana1][cls.idirgha]
  cls.deletary(cls.Index + 1)
  cls.EkahPurvaParayoh = True
  cls.chk_point("akahsavarnedirghah")

 @classmethod
 def vrddhireci(cls):
  """ generated source for method vrddhireci """
  cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana2][cls.ivrddhi]
  cls.deletary(cls.Index + 1)
  cls.EkahPurvaParayoh = True
  cls.chk_point("vrddhireci")

 @classmethod
 def adgunah(cls):
  """ generated source for method adgunah """
  cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana2][cls.iguna]
  if (cls.Isthana2 == cls.italavya) or (cls.Isthana2 == cls.iosthya):
   cls.deletary(cls.Index + 1)
  elif cls.Isthana2 == cls.imurdhanya:
   cls.Linary[cls.Index + 1] = cls.sktr
  elif cls.Isthana2 == cls.idantya:
   cls.Linary[cls.Index + 1] = cls.sktl
  cls.EkahPurvaParayoh = True
  cls.chk_point("adgunah")

 @classmethod
 def ikoyanaci(cls):
  """ generated source for method ikoyanaci """
  cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana1][cls.iantahstha]
  cls.chk_point("ikoyanaci")

 @classmethod
 def enahpadantadati(cls):
  """ generated source for method enahpadantadati """
  cls.Linary[cls.Index + 1] = cls.sktavagraha
  cls.chk_point("enahpadantadati")

 @classmethod
 def ecoyavayavah(cls):
  """ generated source for method ecoyavayavah """
  if cls.Linary[cls.Index - 1] == cls.skte:
   cls.Linary[cls.Index - 1] = cls.skta
   cls.insertary(cls.skty, cls.Index)
  elif cls.Linary[cls.Index - 1] == cls.skto:
   cls.Linary[cls.Index - 1] = cls.skta
   cls.insertary(cls.sktv, cls.Index)
  elif cls.Linary[cls.Index - 1] == cls.sktai:
   cls.Linary[cls.Index - 1] = cls.sktaa
   cls.insertary(cls.skty, cls.Index)
  elif cls.Linary[cls.Index - 1] == cls.sktau:
   cls.Linary[cls.Index - 1] = cls.sktaa
   cls.insertary(cls.sktv, cls.Index)
  if cls.NoSpace:
   cls.Error = 2
   return
  cls.Index = cls.Index + 1
  cls.chk_point("ecoyavayavah")

 @classmethod
 def acsandhi(cls):
  """ generated source for method acsandhi """
  cls.rlvarnayormithahsavarnyam()
  cprev = cls.Linary[cls.Index - 1]
  cnext = cls.Linary[cls.Index + 1]
  if cls.set_memberP(cls.Linary[cls.Index - 1], cls.Ak):
   if (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ak)) and (cls.Isthana1 == cls.Isthana2):
    cls.akahsavarnedirghah()
   elif cls.set_memberP(cls.Linary[cls.Index - 1], cls.Avarna):
    if cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ec):
     cls.vrddhireci()
    else:
     cls.adgunah()
   else:
    cls.ikoyanaci()
  else:
   if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Ekn)) and (cls.Linary[cls.Index + 1] == cls.skta):
    cls.enahpadantadati()
   else:
    cls.ecoyavayavah()
  cls.chk_point("acsandhi")

 @classmethod
 def strReplace(cls, x, idx1, idx2, y):
  """ generated source for method strReplace 
  'x' and 'y' are strings. Return a string
This Java method replaces the characters in a substring of this StringBuffer with characters in the specified String.

The substring begins at the specified start and extends to the character at index end - 1 or to the end of the StringBuffer if no such character exists. First the characters in the substring are removed and then the specified String is inserted at start.
  """
  #b = list(x)
  # b = b.replace(idx1, idx2, y)
  b0 = x[0:idx1]
  b1 = y
  b2 = x[idx2:]
  b = b0+b1+b2
  return str(b)

 @classmethod
 def visargaprep(cls):
  """ generated source for method visargaprep """
  L = len(cls.Pada1)
  if (cls.Pada1 == "ahaH") or (cls.Pada1 == "svaH") or (cls.Pada1 == "antaH") or (cls.Pada1 == "prAtaH") or (cls.Pada1 == "punaH") or (cls.Pada1 == "mAtaH") or (cls.Pada1 == "kOsalyAmAtaH") or (cls.Pada1 == "sanutaH") or (cls.Pada1 == "catuH") or (cls.Pada1 == "prAduH"):
   cls.Linary[cls.Index - 1] = cls.sktr
   cls.Pada1 = cls.strReplace(cls.Pada1, L - 1, L, cls.sktr)
  else:
   cls.Linary[cls.Index - 1] = cls.skts
   if not cls.Pada1 == "":
    cls.Pada1 = cls.strReplace(cls.Pada1, L - 1, L, cls.skts)
  cls.chk_point("visargaprep")

 @classmethod
 def checa(cls):
  """ generated source for method checa """
  if (cls.Linary[cls.Index + 1] == cls.sktch) and (cls.Iyatna1 == cls.ihrasva):
   cls.insertary(cls.sktt, cls.Index)
   if cls.NoSpace:
    cls.Error = 2
    return
   cls.Index = cls.Index + 1
  cls.chk_point("checa")

 @classmethod
 def anmanosca(cls):
  """ generated source for method anmanosca """
  if (cls.Linary[cls.Index + 1] == cls.sktch) and ((cls.Pada1 == "A") or (cls.Pada1 == "mA")):
   cls.insertary(cls.sktt, cls.Index)
   if cls.NoSpace:
    cls.Error = 2
    return
   cls.Index = cls.Index + 1
  cls.chk_point("anmanosca")

 @classmethod
 def padantadva(cls):
  """ generated source for method padantadva """
  temp = cls.identify(cls.Linary[cls.Index - 1])
  cls.Isthana1 = temp[0]
  cls.Iyatna1 = temp[1]
  if (cls.Linary[cls.Index + 1] == cls.sktch) and (cls.Iyatna1 == cls.idirgha):
   cls.insertary(cls.sktt, cls.Index)
   if cls.NoSpace:
    cls.Error = 2
    return
   cls.Index = cls.Index + 1
  cls.chk_point("padantadva")

 @classmethod
 def etattadohsulopo(cls):
  """ generated source for method etattadohsulopo """
  if ((cls.Pada1 == "sas") or (cls.Pada1 == "ezas")) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Hal)):
   cls.deletary(cls.Index - 1)
   cls.Index = cls.Index - 1
  cls.chk_point("etattadohsulopo")

 @classmethod
 def jhalamjasonte(cls):
  """ generated source for method jhalamjasonte """
  temp = cls.identify(cls.Linary[cls.Index - 1])
  cls.Isthana1 = temp[0]
  cls.Iyatna1 = temp[1]
  if cls.set_memberP(cls.Linary[cls.Index - 1], cls.Jhal_not_ru):
   cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana1][cls.isparsa3]
  cls.chk_point("jhalamjasonte")

 @classmethod
 def sasajusoruh(cls):
  """ generated source for method sasajusoruh """
  if cls.Index > 5:
   if cls.substrary(cls.Index - 5, cls.Index - 1) == "sajuz":
    cls.Linary[cls.Index - 1] = cls.ru
  if cls.Linary[cls.Index - 1] == cls.skts:
   cls.Linary[cls.Index - 1] = cls.ru
  cls.chk_point("sasajusoruh")

 @classmethod
 def ahan(cls):
  """ generated source for method ahan """
  if cls.Compound:
   if cls.Pada1 == "ahan":
    if (cls.Pada2 == "rUpa") or (cls.Pada2 == "rAtri") or (cls.Pada2 == "rAtra") or (cls.Pada2 == "rAtre") or (cls.Pada2 == "rAtrARAm") or (cls.Pada2 == "raTantara"):
     cls.Linary[cls.Index - 1] = cls.ru
    else:
     cls.Linary[cls.Index - 1] = cls.sktr
  cls.chk_point("ahan")

 @classmethod
 def amnarudharavar(cls):
  """ generated source for method amnarudharavar """
  if cls.Chandas:
   if (cls.Pada1 == "amnas") or (cls.Pada1 == "UDas") or (cls.Pada1 == "avas"):
    cls.Linary[cls.Index - 1] = cls.sktr
  cls.chk_point("amnarudharavar")

 @classmethod
 def atororhasica(cls):
  """ generated source for method atororhasica """
  if cls.Index > 2:
   if (cls.Linary[cls.Index - 2] == cls.skta) and (cls.Linary[cls.Index - 1] == cls.ru):
    if cls.set_memberP(cls.Linary[cls.Index + 1], cls.Hasch_and_skta):
     cls.Linary[cls.Index - 2] = cls.skto
     cls.deletary(cls.Index - 1)
     cls.Index = cls.Index - 1
  cls.chk_point("atororhasica")

 @classmethod
 def naschavyaprasan(cls):
  """ generated source for method naschavyaprasan """
  if (cls.Linary[cls.Index - 1] == cls.sktn and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Chav)) and not (cls.Pada1 == "praSAn")):
   cls.Linary[cls.Index - 1] = cls.ru
   cls.insertary(cls.sktanusvara, cls.Index - 1)
   if cls.NoSpace:
    cls.Error = 2
    return
   cls.Index = cls.Index + 1
  cls.chk_point("naschavyaprasan")

 @classmethod
 def rori(cls):
  """ generated source for method rori """
  cls.Dhralopa = False
  if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.sktr_and_ru)) and (cls.Linary[cls.Index + 1] == cls.sktr):
   cls.deletary(cls.Index - 1)
   cls.Index = cls.Index - 1
   cls.Dhralopa = True
  cls.chk_point("rori")

 @classmethod
 def dhralope(cls):
  """ generated source for method dhralope """
  if cls.Dhralopa:
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.An)) and (cls.Iyatna1 == cls.ihrasva):
    cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana1][cls.idirgha]
  cls.chk_point("dhralope")

 @classmethod
 def bhobhago(cls):
  """ generated source for method bhobhago """
  if (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Asch)) and (cls.Index > 2):
   if (cls.Pada1 == "bhos") or (cls.Pada1 == "bhagos") or (cls.Pada1 == "aghos") or ((cls.set_memberP(cls.Linary[cls.Index - 2], cls.Avarna)) and (cls.Linary[cls.Index - 1] == cls.ru)):
    cls.Linary[cls.Index - 1] = cls.skty
  cls.chk_point("bhobhago")

 @classmethod
 def kharavasanayor(cls):
  """ generated source for method kharavasanayor """
  if cls.set_memberP(cls.Linary[cls.Index - 1], cls.sktr_and_ru):
   if cls.set_memberP(cls.Linary[cls.Index + 1], cls.Khar_and_linend):
    cls.Linary[cls.Index - 1] = cls.sktvisarga
   else:
    cls.Linary[cls.Index - 1] = cls.sktr
  cls.chk_point("kharavasanayor")

 @classmethod
 def lopahsakalyasya(cls):
  """ generated source for method lopahsakalyasya """
  if (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Asch)) and (cls.Index > 2):
   if (cls.set_memberP(cls.Linary[cls.Index - 2], cls.Avarna)) and (cls.Linary[cls.Index - 1] == cls.skty):
    cls.deletary(cls.Index - 1)
    cls.Index = cls.Index - 1
  cls.chk_point("lopahsakalyasya")

 @classmethod
 def otogargyasya(cls):
  """ generated source for method otogargyasya """
  if cls.set_memberP(cls.Linary[cls.Index + 1], cls.Asch):
   if ((cls.Pada1 == "bhos") or (cls.Pada1 == "bhagos") or (cls.Pada1 == "aghos")):
    cls.deletary(cls.Index - 1)
    cls.Index = cls.Index - 1
  cls.chk_point("otogargyasya")

 @classmethod
 def monusvarah(cls):
  """ generated source for method monusvarah """
  if (cls.Linary[cls.Index - 1] == cls.sktm) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Hal)):
   cls.Linary[cls.Index - 1] = cls.sktanusvara
  cls.chk_point("monusvarah")

 @classmethod
 def namohrasvad(cls):
  """ generated source for method namohrasvad """
  cls.chk_point("namohrasvad enters with Index=%s, NoSpace=%s" %(cls.Index, cls.NoSpace))
  if (cls.Index > 2):
   temp = cls.identify(cls.Linary[cls.Index - 2])
   Sthana = temp[0]
   Yatna = temp[1]
   if (Yatna == cls.ihrasva) and (cls.set_memberP(cls.Linary[cls.Index - 1], cls.KNam)) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ac)):
    cls.chk_point("namohrasvad BEFORE: Soundary[%s][%s] = '%s'" %(cls.Isthana1,cls.isparsa5,cls.Soundary[cls.Isthana1][cls.isparsa5]))
    cls.insertary(cls.Soundary[cls.Isthana1][cls.isparsa5], cls.Index)
    cls.chk_point("namohrasvad  AFTER: Soundary[%s][%s] = '%s'" %(cls.Isthana1,cls.isparsa5,cls.Soundary[cls.Isthana1][cls.isparsa5]))
    if cls.NoSpace:
     cls.Error = 2
     return
    cls.Index = cls.Index + 1
   else:
    cls.chk_point("namohrasvad Test fails")
    cls.chk_point("Sthana=%s,Yatna=%s" % (Sthana,Yatna))
    cls.chk_point("penult.char=%s,Yatna=?ihrasva:%s" % (cls.Linary[cls.Index - 2],(Yatna == cls.ihrasva)))
    cls.chk_point("Prev char=%s,test=%s" % (cls.Linary[cls.Index - 1],cls.set_memberP(cls.Linary[cls.Index - 1], cls.KNam)))
    cls.chk_point("Next char=%s,test=%s" % (cls.Linary[cls.Index + 1],cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ac)))

  cls.chk_point("namohrasvad")

 @classmethod
 def visarjaniyasyasah(cls):
  """ generated source for method visarjaniyasyasah """
  Apavada = bool()
  if (cls.Linary[cls.Index - 1] == cls.sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Khar)):
   Apavada = False
   if (cls.Index + 2) < cls.linmax:
    if cls.set_memberP(cls.Linary[cls.Index + 2], cls.Schar):
     Apavada = True
   if cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ku_and_Pu_and_Schar):
    Apavada = True
   if not (Apavada):
    cls.Linary[cls.Index - 1] = cls.skts
  cls.chk_point("visarjaniyasyasah")

 @classmethod
 def vasari(cls):
  """ generated source for method vasari """
  if (cls.Linary[cls.Index - 1] == cls.sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Schar)):
   cls.Linary[cls.Index - 1] = cls.skts
  cls.chk_point("vasari")

 @classmethod
 def kupvohXkXpau(cls):
  """ generated source for method kupvohXkXpau """
  Apavada = bool()
  if (cls.Linary[cls.Index - 1] == cls.sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Khar)):
   Apavada = False
   if (cls.Index + 2 < cls.linmax):
    if cls.set_memberP(cls.Linary[cls.Index + 2], cls.Schar):
     Apavada = True
   if not (Apavada):
    if cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ku):
     cls.Linary[cls.Index - 1] = sktjihvamuliya
    elif cls.set_memberP(cls.Linary[cls.Index + 1], cls.Pu):
     cls.Linary[cls.Index - 1] = sktupadhmaniya
  cls.chk_point("kupvohXkXpau")

 @classmethod
 def idudupadhasya(cls):
  """ generated source for method idudupadhasya """
  if (cls.Linary[cls.Index - 1] == cls.sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ku_and_Pu)):
   if (cls.Pada1 == "nis") or (cls.Pada1 == "dus") or (cls.Pada1 == "bahis") or (cls.Pada1 == "Avis") or (cls.Pada1 == "catur") or (cls.Pada1 == "prAdur"):
    cls.Linary[cls.Index - 1] = cls.sktsh
  cls.chk_point("idudupadhasya")

 @classmethod
 def nityamsamase(cls):
  """ generated source for method nityamsamase """
  if cls.Compound:
   if (cls.Linary[cls.Index - 1] == cls.sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ku_and_Pu)) and (cls.Index > 2):
    if ((cls.Linary[cls.Index - 2] == cls.skti) or ((cls.Linary[cls.Index - 2] == cls.sktu) and (not cls.Uttarapada))):
     cls.Linary[cls.Index - 1] = cls.sktsh
  cls.chk_point("nityamsamase")

 @classmethod
 def atahkrkamikamsa(cls):
  """ generated source for method atahkrkamikamsa """
  if cls.Compound:
   if (cls.Linary[cls.Index - 1] == cls.sktvisarga) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ku_and_Pu)) and (cls.Index > 2):
    if (cls.Linary[cls.Index - 2] == cls.skta):
     if (cls.Pada2 == "kAra") or (cls.Pada2 == "kAma") or (cls.Pada2 == "kaMsa") or (cls.Pada2 == "kumBa") or (cls.Pada2 == "kumBI") or (cls.Pada2 == "pAtra") or (cls.Pada2 == "kuSA") or (cls.Pada2 == "karRI"):
      if not ((cls.Pada1 == "svar") or (cls.Pada1 == "antar") or (cls.Pada1 == "prAtar") or (cls.Pada1 == "punar") or (cls.Pada1 == "sanutar") or (cls.Pada1 == "hyas") or (cls.Pada1 == "Svas") or (cls.Pada1 == "avas") or (cls.Pada1 == "aDas")) and (not cls.Uttarapada):
       cls.Linary[cls.Index - 1] = cls.skts
  cls.chk_point("atahkrkamikamsa")

 @classmethod
 def stohscunascuh(cls):
  """ generated source for method stohscunascuh """
  Isthana = int()
  Iyatna = int()
  if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Tu_and_skts)) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Cu_and_sktsch)):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index - 1] = cls.Soundary[cls.italavya][cls.Iyatna1]
  elif (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Cu_and_sktsch)) and (cls.Linary[cls.Index + 1] == cls.skts):
   cls.Linary[cls.Index + 1] = cls.sktsch
   if (cls.Index + 2 < cls.linmax):
    if cls.Linary[cls.Index + 2] == cls.skts:
     cls.Linary[cls.Index + 1] = cls.sktsch
  elif (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Cu)) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Tu)):
   temp = cls.identify(cls.Linary[cls.Index + 1])
   cls.Isthana2 = temp[0]
   cls.Iyatna2 = temp[1]
   cls.Linary[cls.Index + 1] = cls.Soundary[cls.italavya][cls.Iyatna2]
   if (cls.Index + 2 < cls.linmax):
    if cls.set_memberP(cls.Linary[cls.Index + 2], cls.Tu_and_skts):
     temp = cls.identify(cls.Linary[cls.Index + 2])
     Isthana = temp[0]
     Iyatna = temp[1]
     cls.Linary[cls.Index + 2] = cls.Soundary[cls.italavya][Iyatna]
  cls.chk_point("stohscunascuh")

 @classmethod
 def stunastuh(cls):
  """ generated source for method stunastuh """
  Isthana = int()
  Iyatna = int()
  if ((cls.Linary[cls.Index - 1] == cls.sktsh) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Tu_and_skts))) or (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Retrotu) and (cls.Pada2 == "nAm")):
   temp = cls.identify(cls.Linary[cls.Index + 1])
   cls.Isthana2 = temp[0]
   cls.Iyatna2 = temp[1]
   cls.Linary[cls.Index + 1] = cls.Soundary[cls.imurdhanya][cls.Iyatna2]
   if (cls.Index + 2 < cls.linmax):
    if cls.set_memberP(cls.Linary[cls.Index + 2], cls.Tu_and_skts):
     temp = cls.identify(cls.Linary[cls.Index + 2])
     Isthana = temp[0]
     Iyatna = temp[1]
     cls.Linary[cls.Index + 1] = cls.Soundary[cls.imurdhanya][cls.Iyatna2]
     cls.Linary[cls.Index + 2] = cls.Soundary[cls.imurdhanya][Iyatna]
  elif (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Tu) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Retrotu))) or ((cls.Linary[cls.Index - 1] == cls.skts) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Retrotu_sktsh))):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index - 1] = cls.Soundary[cls.imurdhanya][cls.Iyatna1]
  cls.chk_point("stunastuh")

 @classmethod
 def anusvarasya(cls):
  """ generated source for method anusvarasya """
  if (cls.Linary[cls.Index - 1] == cls.sktanusvara) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Yay_not_Yan)):
   temp = cls.identify(cls.Linary[cls.Index + 1])
   cls.Isthana2 = temp[0]
   cls.Iyatna2 = temp[1]
   cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana2][cls.isparsa5]
  cls.chk_point("anusvarasya")

 @classmethod
 def torli(cls):
  """ generated source for method torli """
  if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Tu)) and (cls.Linary[cls.Index + 1] == cls.sktl):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index - 1] = cls.sktl
   if cls.Iyatna1 == cls.isparsa5:
    cls.insertary(cls.sktnasalization, cls.Index - 1)
    if cls.NoSpace:
     cls.Error = 2
     return
    cls.Index = cls.Index + 1
  cls.chk_point("torli")

 @classmethod
 def jhayoho(cls):
  """ generated source for method jhayoho """
  if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Jhay)) and (cls.Linary[cls.Index + 1] == cls.skth):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index + 1] = cls.Soundary[cls.Isthana1][cls.isparsa4]
  cls.chk_point("jhayoho")

 @classmethod
 def saschoti(cls):
  """ generated source for method saschoti """
  if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Jhay)) and ((cls.Index + 2) < cls.linmax):
   if (cls.Linary[cls.Index + 1] == cls.sktsch) and (cls.set_memberP(cls.Linary[cls.Index + 2], cls.At)):
    cls.Linary[cls.Index + 1] = cls.sktch
  cls.chk_point("saschoti")

 @classmethod
 def yaronunasike(cls):
  """ generated source for method yaronunasike """
  temp = cls.identify(cls.Linary[cls.Index + 1])
  cls.Isthana2 = temp[0]
  cls.Iyatna2 = temp[1]
  if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Jhay)) and (cls.Iyatna2 == cls.isparsa5):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana1][cls.isparsa5]
  cls.chk_point("yaronunasike")

 @classmethod
 def kharica(cls):
  """ generated source for method kharica """
  if cls.set_memberP(cls.Linary[cls.Index - 1], cls.Jhay):
   temp = cls.identify(cls.Linary[cls.Index - 1])
   cls.Isthana1 = temp[0]
   cls.Iyatna1 = temp[1]
   if cls.set_memberP(cls.Linary[cls.Index + 1], cls.Khar_and_linend):
    cls.Linary[cls.Index - 1] = cls.Soundary[cls.Isthana1][cls.isparsa1]
  cls.chk_point("kharica")

 @classmethod
 def idudeddvivacanampragrhyam(cls):
  """ generated source for method idudeddvivacanampragrhyam """
  cls.Pragrhya = False
  c = cls.Linary[cls.Index - 1]
  if cls.External:
   if c == cls.sktii:
    if (cls.Pada1 == "amI") or (cls.Pada1 == "aDiparI") or (cls.Pada1 == "aBipratI") or (cls.Pada1 == "manasI"):
     cls.Pragrhya = True
   elif c == cls.sktuu:
    if (cls.Pada1 == "amU"):
     cls.Pragrhya = True
   elif c == cls.skte:
    if (cls.Pada1 == "SAlInakOpIne") or (cls.Pada1 == "uBe"):
     cls.Pragrhya = True
   elif c == cls.skto:
    if (cls.Pada1 == "Aho") or (cls.Pada1 == "utAho"):
     cls.Pragrhya = True
  cls.chk_point("idudeddvivacanampragrhyam")

 @classmethod
 def sandhiPrep(cls):
  """ generated source for method sandhiPrep """
  L = int()
  IPada = int()
  NoPrep = bool()
  cls.NoStoh = False
  cls.NoKNam = False
  NoPrep = False
  cls.Exception = False
  cls.Pronoun = True
  cls.OtherCloseSandhi = False
  L = len(cls.Pada1)
  if L <= 1:
   return
  c = cls.Pada1[L-1] # cls.Pada1.substring(L - 1, L)
  if cls.dbg:
   print "sandhiPrep: Pada1='" + cls.Pada1 + "', c=" + c
   print "Is c = skts? %s" % (c == cls.skts,)
   print "is Pada1 = us? %s" % (cls.Pada1 == "us",)
  if c == cls.sktkn:
   if cls.Pada1 == "RiN":
    cls.Exception = True
  elif c == cls.sktc:
   while IPada <= cls.cantamax:
    if cls.Pada1 == cls.CAntaPadary[IPada]:
     NoPrep = True
     cls.NoStoh = True
     IPada = cls.cantamax
    IPada += 1
  elif c == cls.sktj:
   if (cls.Pada1 == "tij"):
    cls.Exception = True
   elif (cls.Pada1 == "tuj"):
    NoPrep = True
  elif c == cls.sktcn:
   if (cls.Pada1 == "aY") or (cls.Pada1 == "alaNkfY") or (cls.Pada1 == "nirAkfY") or (cls.Pada1 == "naY") or (cls.Pada1 == "wIwaY") or (cls.Pada1 == "WaY"):
    cls.NoStoh = True
  elif c == cls.sktretron:
   if (cls.Pada1 == "aR") or (cls.Pada1 == "uR") or (cls.Pada1 == "yaR"):
    cls.Exception = True
  elif c == cls.sktdh:
   if (cls.Pada1 == "aD") or (cls.Pada1 == "ruD"):
    cls.Exception = True
  elif c == cls.sktn:
   if (cls.Pada1 == "Wan") or (cls.Pada1 == "tran") or (cls.Pada1 == "dozan") or (cls.Pada1 == "yakan") or (cls.Pada1 == "yUzan") or (cls.Pada1 == "Sakan") or (cls.Pada1 == "zWan") or (cls.Pada1 == "han"):
    NoPrep = True
   elif (cls.Pada1 == "Ayan") or (cls.Pada1 == "Gan"):
    if cls.PaninianText:
     NoPrep = True
     cls.NoKNam = True
   elif (cls.Pada1 == "ktin") or (cls.Pada1 == "kvin") or (cls.Pada1 == "min") or (cls.Pada1 == "vin"):
    NoPrep = True
   elif (cls.Pada1 == "an") or (cls.Pada1 == "in") or (cls.Pada1 == "kan") or (cls.Pada1 == "kaDyEn") or (cls.Pada1 == "qvun") or (cls.Pada1 == "tan") or (cls.Pada1 == "dAn") or (cls.Pada1 == "man") or (cls.Pada1 == "vun"):
    cls.Exception = True
   elif cls.Pada1 == "tumun":
    cls.NoStoh = True
  elif c == cls.sktm:
   if (cls.Pada1 == "am") or (cls.Pada1 == "Am") or (cls.Pada1 == "num"):
    cls.Exception = True
   elif cls.Compound:
    if ((cls.Pada1 == "puram") and (cls.Pada2 == "dArO")):
     cls.OtherCloseSandhi = True
  elif c == cls.skty:
   if (cls.Pada1 == "ay") or (cls.Pada1 == "Ay"):
    cls.Exception = True
  elif c == cls.sktr:
   if (cls.Pada1 == "car") or (cls.Pada1 == "kur") or (cls.Pada1 == "Sar"):
    cls.Exception = True
  elif c == cls.sktsch:
   if (cls.Pada1 == "eS") or (cls.Pada1 == "KaS") or (cls.Pada1 == "jaS") or (cls.Pada1 == "niS"):
    cls.Exception = True
  elif c == cls.sktsh:
   if (cls.Pada1 == "Jaz") or (cls.Pada1 == "Baz"):
    cls.Exception = True
  elif c == cls.skts:
   cls.chk_point("sandhiPrep at c=skts:%s " % cls.Exception)
   if (cls.Pada1 == "as") or (cls.Pada1 == "atus") or (cls.Pada1 == "aTus") or (cls.Pada1 == "is") or (cls.Pada1 == "us") or (cls.Pada1 == "os") or (cls.Pada1 == "kas") or (cls.Pada1 == "kAs") or (cls.Pada1 == "Nas") or (cls.Pada1 == "tas") or (cls.Pada1 == "tAs") or (cls.Pada1 == "TAs") or (cls.Pada1 == "Bis") or (cls.Pada1 == "Byas"):
    cls.Exception = True
    cls.chk_point("sandhiPrep setting Exception to %s" % cls.Exception)
  if cls.Compound:
   if (not cls.Exception) and (not NoPrep):
    c = cls.Linary[cls.Index - 1]
    if c == cls.sktc:
     if cls.Pada1 == "aYc":
      cls.Linary[cls.Index - 1] = cls.sktk
      cls.deletary(cls.Index - 2)
      cls.Index = cls.Index - 1
     else:
      cls.Linary[cls.Index - 1] = cls.sktk
    elif c == cls.sktch:
     cls.Linary[cls.Index - 1] = cls.sktk
    elif c == cls.sktj:
     if (cls.Pada1 == "rAj"):
      cls.Linary[cls.Index - 1] = cls.sktretrot
     else:
      cls.Linary[cls.Index - 1] = cls.sktk
    elif c == cls.sktjh:
     cls.Linary[cls.Index - 1] = cls.sktk
    elif c == cls.sktn:
     if cls.Index > 2:
      if (cls.Linary[cls.Index - 2] == cls.skta) or (cls.Linary[cls.Index - 2] == cls.skti):
       if ((cls.Pada1 == "ahan") and (not cls.PurvaPada == "eka")):
        pass
       else:
        cls.deletary(cls.Index - 1)
        cls.Index = cls.Index - 1
    elif c == cls.sktr:
     if (cls.Pada1 == "pur") or (cls.Pada1 == "Dur"):
      cls.Linary[cls.Index - 2] = cls.sktuu
    elif c == cls.sktsch:
     if cls.Pada1 == "viS":
      cls.Linary[cls.Index - 1] = cls.sktretrot
     else:
      cls.Linary[cls.Index - 1] = cls.sktk
    elif c == cls.sktsh:
     if cls.Pada1 == "daDfz":
      cls.Linary[cls.Index - 1] = cls.sktk
    elif c == cls.skts:
     if (cls.Pada1 == "ASis"):
      cls.Linary[cls.Index - 2] = cls.sktii
     elif cls.Pada1 == "pums":
      cls.deletary(cls.Index - 1)
      cls.Index = cls.Index - 1
    else:
     pass

 @classmethod
 def sandhiSplit(cls, x):
  """ generated source for method sandhiSplit 
   'x' is a string
  """
  dbg = False
  a = [] # list of strings '' # list[] # ArrayList()
  INITIAL = 0
  SKT = 1
  OTHER = 2
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
  """ generated source for method sandhi1 """
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
  cls.Linary = [""] + list(s1)
  cls.linmax = len(cls.Linary) - 1
  #print "Linary=[" + ",".join(cls.Linary) + "]"
  cls.chk_point("calling sandhimain with:'" + "".join(cls.Linary) + "'")
  cls.Error = 0
  cls.sandhimain()
  if cls.NoSpace and (cls.Error == 2):
   cls.Error = 0
  if cls.Error != 0:
   print "Sandhi error: " + cls.Error + ", s = " + s
   return ""
  else:
   ans = "".join(cls.Linary)
   ans = ans.strip()
   return (ans)

 @classmethod
 def sandhimain(cls):
  """ generated source for method sandhimain """
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
  Inext = 0
  Inextsp = 0
  IPrev = 0
  IPrevSpace = 0
  I = 0
  cls.PurvaPada = ""
  cls.Pada1 = ""
  cls.Pada2 = ""
  cls.Index = cls.nxtposary(cls.Padbound, cls.FldChr, 2)
  cls.chk_point("sandhimain. Initial Index = %s" % cls.Index)
  cls.Upasarga = False
  while cls.Index > 0:
   cls.EkahPurvaParayoh = False
   cls.Uttarapada = False
   if cls.NxtUttarapada:
    cls.Uttarapada = True
   cls.NxtUttarapada = False
   cls.PurvaPada = cls.Pada1
   if IPrev == 0:
    if cls.Compound:
     IPrev = cls.lastposary(cls.space, cls.Index - 1)
    else:
     IPrev = cls.lastposary(cls.space, cls.Index - 1)
    cls.chk_point("sandhimain: Index=%s, IPrev=%s" %(cls.Index,IPrev))
    cls.Pada1 = cls.substrary(IPrev + 1, cls.Index - 1)
    cls.chk_point("sandhimain. Pada1='%s',  Compound=%s, IPrev=%s, Index=%s"  %(cls.Pada1,cls.Compound,IPrev, cls.Index))
   elif cls.External:
    cls.Pada1 = cls.Pada2
   else:
    cls.Pada1 = cls.NxtPada1
   Inext = cls.nxtposary(cls.Padbound, cls.FldChr, cls.Index + 1)
   if Inext == 0:
    Inext = cls.lengthary() + 1
   if cls.External:
    cls.Pada2 = cls.substrary(cls.Index + 1, Inext - 1)
   else:
    Inextsp = cls.nxtposary(cls.space, cls.FldChr, cls.Index + 1)
    if (Inextsp > 0) and (Inextsp < Inext):
     cls.Pada2 = cls.substrary(cls.Index + 1, Inextsp - 1)
    else:
     cls.Pada2 = cls.substrary(cls.Index + 1, Inext - 1)
    IPrevSpace = cls.lastposary(cls.space, Inext - 1)
    if IPrevSpace > cls.Index:
     cls.NxtPada1 = cls.substrary(IPrevSpace + 1, Inext - 1)
    else:
     cls.NxtPada1 = cls.Pada2
     cls.NxtUttarapada = True
   cls.Upasarga = False
   if cls.External and (cls.Pada1 == "ut"):
    cls.Pada1 = "ud"
   if cls.Pada1 == "api":
    pass # ejf
   else:
    i = 1
    while I <= cls.pradimax:
     if cls.Pada1 == cls.Pradi[I]:
      cls.Upasarga = True
      I = cls.pradimax
     I += 1
   cls.sandhiPrep()
   doSandhi = True
   cls.chk_point("sandhimain, Exception =%s " % cls.Exception)
   if cls.Exception:
    doSandhi = False
   else:
    if cls.Upasarga and cls.CloseUpasargaSandhi:
     cls.OtherCloseSandhi = True
    cls.idudeddvivacanampragrhyam()
    if cls.Pragrhya:
     doSandhi = False
   if doSandhi:
    if (cls.Linary[cls.Index - 1] == cls.sktvisarga):
     cls.visargaprep()
    temp = cls.identify(cls.Linary[cls.Index - 1])
    cls.Isthana1 = temp[0]
    cls.Iyatna1 = temp[1]
    temp = cls.identify(cls.Linary[cls.Index + 1])
    cls.Isthana2 = temp[0]
    cls.Iyatna2 = temp[1]
    cls.checa()
    cls.anmanosca()
    if (cls.TukPadantat):
     cls.padantadva()
    if cls.set_memberP(cls.Linary[cls.Index - 1], cls.sktn_and_sktsh_and_skts):
     if cls.Pronoun:
      cls.etattadohsulopo()
     cls.amnarudharavar()
     cls.sasajusoruh()
     if not cls.NoStoh:
      cls.ahan()
     cls.atororhasica()
    if cls.set_memberP(cls.Linary[cls.Index - 1], cls.Ac) and cls.set_memberP(cls.Linary[cls.Index + 1], cls.Ac):
     cls.acsandhi()
    elif (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Hal_and_ru)) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Al_and_Linend)):
     cls.jhalamjasonte()
     cls.naschavyaprasan()
     cls.rori()
     cls.dhralope()
     cls.bhobhago()
     cls.kharavasanayor()
     cls.otogargyasya()
     cls.monusvarah()
     cls.chk_point("NoKNam = %s" % cls.NoKNam)
     if not cls.NoKNam:
      cls.namohrasvad()
     cls.visarjaniyasyasah()
     if cls.ScharSchari:
      cls.vasari()
     cls.idudupadhasya()
     cls.nityamsamase()
     cls.atahkrkamikamsa()
     if cls.XkXpKupvoh:
      cls.kupvohXkXpau()
     if not cls.NoStoh:
      cls.stohscunascuh()
      cls.stunastuh()
     cls.torli()
     if cls.ChAti:
      cls.saschoti()
     cls.jhayoho()
     cls.kharica()
     if cls.ParaSavarna or cls.OtherCloseSandhi:
      cls.anusvarasya()
    if (cls.set_memberP(cls.Linary[cls.Index - 1], cls.Hal)) and (cls.set_memberP(cls.Linary[cls.Index + 1], cls.Al)):
     cls.lopahsakalyasya()
     if cls.Anunasika or cls.OtherCloseSandhi:
      cls.yaronunasike()
   cls.chk_point("label7000a. Index=%s"%cls.Index)
   if cls.EkahPurvaParayoh:
    cls.deletary(cls.Index)
    cls.Index = cls.Index - 1
   elif (cls.Index > 1) and cls.Despace:
    if cls.set_memberP(cls.Linary[cls.Index - 1], cls.Hal):
     cls.deletary(cls.Index)
   if cls.Linary[cls.Index] == cls.hyphen:
    cls.deletary(cls.Index)
    cls.Index = cls.Index - 1
   IPrev = cls.Index
   cls.chk_point("label7000b(0): Padbound=%s, FldChr=%s, Index=%s" %(cls.Padbound, cls.FldChr, cls.Index + 1))
   cls.Index = cls.nxtposary(cls.Padbound, cls.FldChr, cls.Index + 1)
   cls.chk_point("label7000b")
   if cls.dbg:
    print "label7000b(1) Index = %s" % cls.Index

 @classmethod
 def sandhi(cls, s):
  """ generated source for method sandhi """
  dbg = False
  dbgPrint(dbg,"sandhi. s=%s" % s)
  split = cls.sandhiSplit(s)
  
  dbgPrint(dbg,"sandhi: s='%s'" % s)
  dbgPrint(dbg,"sandhi: split=[%s]" % (",".join(split)))
  n = len(split)
  whitebeg = ""
  ans = whitebeg
  i = 0
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
  """ generated source for method join """
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
  """ generated source for method chk_point """
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

