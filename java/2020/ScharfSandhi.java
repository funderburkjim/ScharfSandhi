/*
 * Java implementation of 'sandhi' routine from SandhiGen.pp (PMS 2000/10/14)
 * This is derived from the Perl implementation 'sandhi.pm' of Feb 9, 2009.
 * Jim Funderburk
 * June 2010
 */

//package org.sanskritlibrary.scharfsandhi;
//package scharfsandhi;
import java.util.*;
import java.util.regex.*;

public class ScharfSandhi {
 /**
  * The Sanskrit sounds represented in the font Sanskrit01
  * These are Strings of length 1, so could have been declared 'char'
  * However, it was felt that treating them as String objects was conceptually
  * simpler, and probably insignificantly less efficient.
  */
  private static final String skta = "a";
  private static final String sktaa = "A";
  private static final String skti = "i";
  private static final String sktii = "I";
  private static final String sktu = "u";
  private static final String sktuu = "U";
  private static final String sktri = "f";
  private static final String sktrii = "F";
  private static final String sktlri = "x";
  private static final String sktlrii = "X";
  private static final String skte = "e";
  private static final String sktai = "E";
  private static final String skto = "o";
  private static final String sktau = "O";
  private static final String sktvisarga = "H";
  private static final String sktjihvamuliya = "»"; //{opt k}
  private static final String sktupadhmaniya = "¹"; //{opt p}
  private static final String sktanusvara = "M";
  private static final String sktanunasika = "µ"; //{opt m.  It should follow the sound it nasalizes}
  private static final String sktnasalization = "~"; //{shift `.  It follows the sound it nazalizes}
  private static final String sktavagraha = "'"; // changed from"""";
  private static final String sktroot = "§"; //{opt v}
  private static final String sktudatta = "«"; //{opt e space.  It precedes the sound it accents}
  private static final String sktsvarita = "^"; //{opt i space.  It precedes the sound it accents}
  private static final String sktudattaa = "";
  private static final String sktudattai = "";
  private static final String sktudattau = "";
  private static final String sktudattae = "";
  private static final String sktudattao = "";
  private static final String sktudattaaa = "§";
  private static final String sktudattaii = "ª";
  private static final String sktudattauu = "²";
  private static final String sktudattaai = "";
  private static final String sktudattaau = "®";
  private static final String sktsvaritaa = "	";
  private static final String sktsvaritai = "";
  private static final String sktsvaritau = "";
  private static final String sktsvaritae = "";
  private static final String sktsvaritao = "";
  private static final String sktsvaritaaa = "¥";
  private static final String sktsvaritaii = "«";
  private static final String sktsvaritauu = "³";
  private static final String sktsvaritaai = "¦";
  private static final String sktsvaritaau = "¯";
  private static final String sktk = "k";
  private static final String sktkh = "K";
  private static final String sktg = "g";
  private static final String sktgh = "G";
  private static final String sktkn = "N";
  private static final String sktc = "c";
  private static final String sktch = "C";
  private static final String sktj = "j";
  private static final String sktjh = "J";
  private static final String sktcn = "Y";
  private static final String sktretrot = "w";
  private static final String sktretroth = "W";
  private static final String sktretrod = "q";
  private static final String sktretrodh = "Q";
  private static final String sktretron = "R";
  private static final String sktt = "t";
  private static final String sktth = "T";
  private static final String sktd = "d";
  private static final String sktdh = "D";
  private static final String sktn = "n";
  private static final String sktp = "p";
  private static final String sktph = "P";
  private static final String sktb = "b";
  private static final String sktbh = "B";
  private static final String sktm = "m";
  private static final String skty = "y";
  private static final String sktr = "r";
  private static final String sktl = "l";
  private static final String sktv = "v";
  private static final String sktsch = "S";
  private static final String sktsh = "z";
  private static final String skts = "s";
  private static final String skth = "h";
 // Neutral characters
 private static final String newline = "\n";
 private static final String tab = "\t";
 private static final String space = " ";
 private static final String hyphen = "-";
 private static final String comma = ",";
 private static final String semicolon = ";";
 private static final String colon = ":";
 private static final String period = ".";
 private static final String star = "*";
 private static final String slash = "/";
 private static final String openparen = "(";
 private static final String closeparen = ")";
 // The 'CAntaPadary' is a list of Paninian affixes that end in 'c'.
 // It is coded as sets of chars,
 // The string is populated in init_CAntaPadary
 private static final int cantamax = 27;
 private static final String[] CAntaPadary = new String[1+cantamax];
 static {
 CAntaPadary[1] = "aqac";
 CAntaPadary[2] = "Awac";
 CAntaPadary[3] = "Alac";
 CAntaPadary[4] = "ec";
 CAntaPadary[5] = "Ac";
 CAntaPadary[6] = "ic";
 CAntaPadary[7] = "ilac";
 CAntaPadary[8] = "izRuc";
 CAntaPadary[9] = "Irac";
 CAntaPadary[10] = "ktic";
 CAntaPadary[11] = "KizRuc";
 CAntaPadary[12] = "Wac";
 CAntaPadary[13] = "Rac";
 CAntaPadary[14] = "tfc";
 CAntaPadary[15] = "daGnac";
 CAntaPadary[16] = "dvayasac";
 CAntaPadary[17] = "dvyac";
 CAntaPadary[18] = "nAwac";
 CAntaPadary[19] = "biqac";
 CAntaPadary[20] = "birIsac";
 CAntaPadary[21] = "mAtrac";
 CAntaPadary[22] = "yAc";
 CAntaPadary[23] = "vuc";
 CAntaPadary[24] = "vfc";
 CAntaPadary[25] = "SaNkawac";
 CAntaPadary[26] = "SAlac";
 CAntaPadary[27] = "zWac";
 }
 // Pradi array of strings: preverbs
 private static final int pradimax = 21;
 private static final String[] Pradi = new String[1+pradimax];
 static {
 Pradi[1] = "pra";
 Pradi[2] = "parA";
 Pradi[3] = "apa";
 Pradi[4] = "sam";
 Pradi[5] = "anu";
 Pradi[6] = "ava";
 Pradi[7] = "nis";
 Pradi[8] = "dus";
 Pradi[9] = "vi";
 Pradi[10] = "A";
 Pradi[11] = "ni";
 Pradi[12] = "aDi";
 Pradi[13] = "api";
 Pradi[14] = "ati";
 Pradi[15] = "su";
 Pradi[16] = "ud";
 Pradi[17] = "aBi";
 Pradi[18] = "prati";
 Pradi[19] = "pari";
 Pradi[20] = "upa";
 }
 // various character sets. Since Sanskrit01 uses 1 ascii character to
 // represent elements of the Sanskrit alphabet, these sets may be
 // represented as character strings.
 // Since the Sanskrit characters are represented as Java Strings,
 // the 'union' of sets may be uniformly represented with Java '+'
 // concatentaion of Strings.
 private static final String ru = "s";
 private static final String Avarna = skta + sktaa;
 private static final String Ivarna = skti + sktii;
 private static final String Uvarna = sktu + sktuu;
 private static final String Rvarna = sktri + sktrii;
 private static final String Lvarna = sktlri + sktlrii;
 private static final String Ku = sktk + sktkh + sktg + sktgh + sktkn;
 private static final String Cu = sktc + sktch + sktj + sktjh + sktcn;
 private static final String Retrotu = sktretrot + sktretroth + sktretrod + sktretrodh + sktretron;
 private static final String Tu = sktt + sktth + sktd + sktdh + sktn;
 private static final String Pu = sktp + sktph + sktb + sktbh + sktm;
 private static final String An = Avarna + Ivarna + Uvarna;
 private static final String Ak = Avarna + Ivarna + Uvarna + Rvarna + Lvarna;
 private static final String Ik = Ivarna + Uvarna + Rvarna + Lvarna;
 private static final String Uk = Uvarna + Rvarna + Lvarna;
 private static final String Ekn = skte + skto;
 private static final String Ec = skte + skto + sktai + sktau;  //PMS dipthongs
 private static final String Aic = sktai + sktau;
 private static final String Ac = Ak + Ec;
 private static final String Ic = diff_string(Ac,Avarna);
 private static final String At = Ac + skth + skty + sktv + sktr;
 private static final String Yan = skty + sktv + sktr + sktl; //PMS semivowels
 private static final String An2 = Ac + skth + Yan; //PMS vowels, h and semivowels
 private static final String In2 = diff_string(An2,Avarna);
 private static final String Yam = skty + sktv + sktr + sktl + sktcn + sktm + sktkn + sktretron + sktn; //PMS semivowels and nasals
 private static final String Am = Ac + skth + Yam; //PMS vowels, semivowels, nasals and h
 private static final String KNam = sktkn + sktretron + sktn;
 private static final String Yacn = Yam + sktjh + sktbh;
 private static final String Jhash = sktjh + sktbh + sktgh + sktretrodh + sktdh; //PMS voiced aspirated stops
 private static final String Bhash = sktbh + sktgh + sktretrodh + sktdh; //PMS voiced aspirated stops other than jh
 private static final String Jasch = sktj + sktb + sktg + sktretrod + sktd; //PMS unvoiced unaspirated stops
 private static final String Basch = sktb + sktg + sktretrod + sktd; //PMS unvoiced unaspirated stops other than j
 private static final String Jhasch = sktjh + sktbh + sktgh + sktretrodh + sktdh + sktj + sktb + sktg + sktretrod + sktd; //PMS voiced stops
 private static final String Hasch = skth + Yam + Jhasch; //PMS voiced consonants
 private static final String Vasch = diff_string(Hasch,skth + skty); //PMS voiced consonants other than h and y
 private static final String Asch = Ac + Hasch; //PMS voiced sounds
 private static final String Chav = sktch + sktretroth + sktth + sktc + sktretrot + sktt;
 private static final String Khay = sktkh + sktph + sktch + sktretroth + sktth + sktc + sktretrot + sktt + sktk + sktp; //PMS unvoiced stops
 private static final String Jhay = Jhasch + Khay; //PMS non-nasal stops both voiced and unvoiced
 private static final String Yay = Yam + Jhay; //PMS semivowels and stops
 private static final String May = sktm + sktkn + sktretron + sktn + Jhay; //PMS stops other than palatal n
 private static final String Cay = sktc + sktretrot + sktt + sktk + sktp;
 private static final String Khar = sktkh + sktph + sktch + sktretroth + sktth + sktc + sktretrot + sktt + sktk + sktp + sktsch + sktsh + skts; //PMS unvoiced sounds
 private static final String Car = sktc + sktretrot + sktt + sktk + sktp + sktsch + sktsh + skts;
 private static final String Schar = sktsch + sktsh + skts; //PMS unvoiced sylibants
 private static final String Jhar = Jhay + Schar;  //PMS non-nasal stops and unvoiced silibants
 private static final String Yar = Yam + Jhay + Schar; //PMS semivowels, stops and unvoiced silibants (consonants other than h)
 private static final String Schal = sktsch + sktsh + skts + skth;
 private static final String Jhal = Jhay + Schal; //PMS non-nasal stops and silibants
 private static final String Hal = skty + sktv + sktr + sktl + sktcn + sktm + sktkn + sktretron + sktn + sktjh + sktbh + sktgh + sktretrodh + sktdh + sktj + sktb + sktg + sktretrod + sktd + sktkh + sktph + sktch + sktretroth + sktth + sktc + sktretrot + sktt + sktk + sktp + sktsch + sktsh + skts + skth;
 private static final String Ral =  diff_string(Hal,skty + sktv); //PMS consonants other than y and v
 private static final String Val = diff_string(Hal, skty);  //PMS consonants other than y
 private static final String Al = Ac + Hal; //PMS all independent sounds
 private static final String Guna = skta + skte + skto;
 private static final String Vrddhi = sktaa + sktai + sktau;
 private static final String Sounds = Al + sktvisarga + sktanusvara;
 private static final String Linend = space + comma + semicolon + colon + period;

//----- ejf set constants
// These are sets that were referenced by inline Pascal
// set construction operators. In conversion to Perl,
// it was convenient to construct these initially and
// give them new names.
 private static final String Rvarna_and_Lvarna = Rvarna + Lvarna;
 private static final String Jhal_not_ru = diff_string(Jhal,ru);
 private static final String Hasch_and_skta = Hasch + skta;
 private static final String sktr_and_ru = sktr + ru;
 private static final String Khar_and_linend = Khar + Linend;
 private static final String Ku_and_Pu_and_Schar = Ku + Pu + Schar;
 private static final String Ku_and_Pu = Ku + Pu;
 private static final String Tu_and_skts = Tu + skts;
 private static final String Cu_and_sktsch = Cu + sktsch;
 private static final String Retrotu_sktsh = Retrotu + sktsh;
 private static final String Yay_not_Yan = diff_string(Yay,Yan);
 private static final String sktn_and_sktsh_and_skts = sktn + sktsh + skts;
 private static final String Hal_and_ru = Hal + ru;
 private static final String Al_and_Linend = Al + Linend;
 // initialize Soundary, and related constants
 private static final int maxyatna = 11;
 private static final int maxsthana = 5;
 // private static final String[] Pradi = new String[1+pradimax];
 private static final String[][] Soundary = new String[1+maxsthana][1+maxyatna];
 // constants for first coord of Soundary
 private static final int ikanthya = 1;
 private static final int italavya = 2;
 private static final int imurdhanya = 3;
 private static final int idantya = 4;
 private static final int iosthya = 5;
 // second coord of Soundary
 private static final int ihrasva = 1;
 private static final int idirgha = 2;
 private static final int iguna = 3;
 private static final int ivrddhi = 4;
 private static final int isparsa1 = 5;
 private static final int isparsa2 = 6;
 private static final int isparsa3 = 7;
 private static final int isparsa4 = 8;
 private static final int isparsa5 = 9;
 private static final int iantahstha = 10;
 private static final int iusmana = 11;
 //constants global to sandhi routine
 private static  int linmax ;
 private static final int pratipadmax = 20; //PMS Maximum length assumed for lexical items
 private static final int iapi = 13; //PMS api usually is not an upasarga so check it separately
 // variables global to sandhi routines
 private static String[] Linary ; //= new String[1+linmax]; //
 private static int Isthana1,Isthana2,Iyatna1,Iyatna2;
 private static String PurvaPada, Pada1,NxtPada1,Pada2; // usu. max len pratipadmax
 private static Boolean Upasarga,NoStoh,NoKNam,Exception,Pronoun,EkahPurvaParayoh;
 private static int Error,IEnd,Inextsp,IPrev,Inext,IPrevSpace,Index;
 private static Boolean Found,NoSpace,Dhralopa,OtherCloseSandhi,Pragrhya,Uttarapada,NxtUttarapada;
 private static String FldChr;
 private static Boolean Despace,External,Compound,Chandas,CloseUpasargaSandhi;
 private static Boolean PaninianText=false; // June 2010. Not reset.
 private static Boolean TukPadantat,ScharSchari,XkXpKupvoh,ChAti;
 private static Boolean ParaSavarna,Anunasika;
 private static String Padbound;
 private static Boolean dbg=false;

 static {
  // initialize Soundary
 Soundary[ikanthya][ihrasva] = skta;
 Soundary[ikanthya][idirgha] = sktaa;
 Soundary[ikanthya][iguna] = skta;
 Soundary[ikanthya][ivrddhi] = sktaa;
 Soundary[ikanthya][isparsa1] = sktk;
 Soundary[ikanthya][isparsa2] = sktkh;
 Soundary[ikanthya][isparsa3] = sktg;
 Soundary[ikanthya][isparsa4] = sktgh;
 Soundary[ikanthya][isparsa5] = sktkn;
 Soundary[ikanthya][iantahstha] = skth;
 Soundary[ikanthya][iusmana] = sktjihvamuliya;

 Soundary[italavya][ihrasva] = skti;
 Soundary[italavya][idirgha] = sktii;
 Soundary[italavya][iguna] = skte;
 Soundary[italavya][ivrddhi] = sktai;
 Soundary[italavya][isparsa1] = sktc;
 Soundary[italavya][isparsa2] = sktch;
 Soundary[italavya][isparsa3] = sktj;
 Soundary[italavya][isparsa4] = sktjh;
 Soundary[italavya][isparsa5] = sktcn;
 Soundary[italavya][iantahstha] = skty;
 Soundary[italavya][iusmana] = sktsch;

 Soundary[imurdhanya][ihrasva] = sktri;
 Soundary[imurdhanya][idirgha] = sktrii;
 Soundary[imurdhanya][iguna] = skta;
 Soundary[imurdhanya][ivrddhi] = sktaa;
 Soundary[imurdhanya][isparsa1] = sktretrot;
 Soundary[imurdhanya][isparsa2] = sktretroth;
 Soundary[imurdhanya][isparsa3] = sktretrod;
 Soundary[imurdhanya][isparsa4] = sktretrodh;
 Soundary[imurdhanya][isparsa5] = sktretron;
 Soundary[imurdhanya][iantahstha] = sktr;
 Soundary[imurdhanya][iusmana] = sktsh;

 Soundary[idantya][ihrasva] = sktlri;
 Soundary[idantya][idirgha] = sktlrii;
 Soundary[idantya][iguna] = skta;
 Soundary[idantya][ivrddhi] = sktaa;
 Soundary[idantya][isparsa1] = sktt;
 Soundary[idantya][isparsa2] = sktth;
 Soundary[idantya][isparsa3] = sktd;
 Soundary[idantya][isparsa4] = sktdh;
 Soundary[idantya][isparsa5] = sktn;
 Soundary[idantya][iantahstha] = sktl;
 Soundary[idantya][iusmana] = skts;

 Soundary[iosthya][ihrasva] = sktu;
 Soundary[iosthya][idirgha] = sktuu;
 Soundary[iosthya][iguna] = skto;
 Soundary[iosthya][ivrddhi] = sktau;
 Soundary[iosthya][isparsa1] = sktp;
 Soundary[iosthya][isparsa2] = sktph;
 Soundary[iosthya][isparsa3] = sktb;
 Soundary[iosthya][isparsa4] = sktbh;
 Soundary[iosthya][isparsa5] = sktm;
 Soundary[iosthya][iantahstha] = sktv;
 Soundary[iosthya][iusmana] = sktupadhmaniya;
 }
 static {
  init();

 }
 private static void init() {
  // currently this routine does nothing.
 }
 /**
  * 
  * @param x 
  * @param y
  * @return a String containing those characters of x which
  * are not in y.
  */
 private static String diff_string(String x,String y){
  StringBuffer b = new StringBuffer();
  char c;
  for(int i=0;i<x.length();i++){
   c=x.charAt(i);
   if (y.indexOf(c) == -1) {
    b.append(c);
   }
  }
  String ans = new String(b);
//  System.out.println("diff_string: x="+x + ", y=" + y + ", ans="+ ans);
  return ans;
 }
 private static Boolean set_memberP(String c,String set){
    // c is a char ,implemented as a string of length 1
    // set is a "set of char", implemented as a string.
  if (set.indexOf(c) == -1) {return false;}else{return true;}
 }
 private static String str_trim(String x){
  return x.trim();
 }
 /**
  * It returns 0 (ok) or 4 (error)
  * @param compound_ans C for compound sandhi, E for External sandhi
  * @param vedic_ans  Y or N
  * @param closeSandhi_ans N,Y,S
  * @param despace_ans Y or N
  */
 public static int sandhioptions(String compound_ans,String vedic_ans,String closeSandhi_ans,String despace_ans){
  String Answer;
  String Yes="Y";
  String No="N";
  int error = 0;
  // initialize external flags to false.
 Despace = false;
 External = false;
 Compound = false;
 Chandas = false;
 CloseUpasargaSandhi = false;
 TukPadantat = false; //PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
 ScharSchari = false; //PMS 8.3.36.  vA Sari
 XkXpKupvoh = false; //PMS 8.3.37.  kupvoH XkXpau ca.
 ChAti = false; //PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
 ParaSavarna = false; //PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
 Anunasika = false; //PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 Answer = compound_ans.toUpperCase();
 if (Answer.equals("")){
  Answer = "?";
 }
 if  (Answer.equals("C")) {
  Compound = true;
  Padbound = hyphen;
 }else if (Answer.equals("E")) {
  External = true;
  Padbound = space;
 }else {
  Error =4;
  return Error;
 }
 // process vedic answer
 // print "Is this a Vedic text (chandas)?\n";
// print "Default no: ";
// readln(Answer);
 Answer = vedic_ans.toUpperCase();
 if (Answer.equals("")){
  Answer = "?";
 }
 if  (Answer.equals("Y")) {
  Chandas = true;
 }else if (Answer.equals("N")) {
  Chandas = false;
 }else {
  Error =4;
  return Error;
 }
 //-- closeSandhi_ans
// print "Do you want to exercise close sandhi options?\n";
// print ""N" or "n" to decline\n";
// print ""Y" or "y" to accept\n";
// print ""S" or "s" to follow standard editorial practice\n";
// print "Any other character to select options individually: ";
// readln(Answer);
 Answer = closeSandhi_ans.toUpperCase();
 if (Answer.equals("")){
  Answer = "?";
 }
 if  (Answer.equals("Y")) {
  TukPadantat = true; //PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
  ScharSchari = true; //PMS 8.3.36.  vA Sari
  XkXpKupvoh = true; //PMS 8.3.37.  kupvoH XkXpau ca.
  ChAti = true; //PMS 8.4.63.  SaS cho "Ti. (jhayaH 62, anyatarasyAm 62)
  ParaSavarna = true; //PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
  Anunasika = true; //PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 }else if (Answer.equals("N")) {
  TukPadantat = false;
  ScharSchari = false;
  XkXpKupvoh = false;
  ChAti = false;
  ParaSavarna = false;
  Anunasika = false;
 }else if (Answer.equals("S")) {
  if ( Compound ) {
	 //PMS Close sandhi within compounds
	 TukPadantat = true; //PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
	 ScharSchari = true; //PMS 8.3.36.  vA Sari
	 //PMS technically, 8.3.37 should also apply but it is never seen
	 ChAti = true; //PMS 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
	 ParaSavarna = true; //PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
	 Anunasika = true; //PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
	 //PMS display standard editorial practice for compound sandhi
  }else {
 	 //PMS External: 8.4.63 and 8.4.45
	 ChAti = true; //PMS 8.4.63.  SaS cho "Ti. (jhayaH 62, anyatarasyAm 62)
	 Anunasika = true; //PMS 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
	  if (dbg) {
	     //print "The optional sandhi in the following sutras will apply:\n";
	     //print "     8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
	     //print "     8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62 ) . \n";
	     //PMS disabled Close sandhi between upasargas and their following verb forms
	     //PMS CloseUpasargaSandhi = true;
	     //PMS print "Close sandhi will be observed between upasargas and their following verb forms\n";
	     //PMS print "After the upasarga "sam",\n";
	     //PMS print "     8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
	  }

  }
}else { // non-functioning. old code shown for possible reuse elsewhere
  //PMS peruse options
  //print "Choose sandhi options ("Y" or "y" to accept):\n";
  //print "6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71).\n";
  //print "     Pada final long vowel augmented with c before ch ? ";
//  readln(Answer);
//  if ( Answer eq "" ) {
//   Answer = "?";
//  }
//  if (Answer eq "Y") {
//   TukPadantat = true;
//  }
//  //print "8.3.36.  vA Sari.\n";
//  print "     S, z or s before palatal, retroflex or dental stop respectively? ";
////  readln(Answer);
//  if ( Answer eq "" ) {
//   Answer = "?";
//  }
//  if (Answer eq "Y") {
//   ScharSchari = true;
//  }
//  print "8.3.37.  kupvoH XkXpau ca.\n";
//  print "      jihvamuliya, upadhmaniya before gutteral or labial stop respectively? ";
////  readln(Answer);
//  if ( Answer eq "" ) {
//   Answer = "?";
//  }
//  if (Answer eq "Y") {
//   XkXpKupvoh = true;
//  }
//  print "8.4.63.  SaS cho "wi . (jhayaH 62, anyatarasyAm 62\n";
//  print "    ch after stops ? ";
////  readln(Answer);
//  if ( Answer eq "" ) {
//   Answer = "?";
//  }
//  if (Answer eq "Y") {
//   ChAti = true;
//  }
//  print "8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
//  print "     AnusvAra  stop homogenous with following stop? ";
////  readln(Answer);
//  if ( Answer eq "" ) {
//   Answer = "?";
//  }
//  if (Answer eq "Y") {
//   ParaSavarna = true;
//  }
//  print "8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
//  print "(At present the program does not handle nasalized semivowels)\n";
//  print "(which, though rarely found in editions, go with this sandhi.)\n";
//  print "     Stops  corresponding nasal before a nasal? ";
////  readln(Answer);
//  if ( Answer eq "" ) {
//   Answer = "?";
//  }
//  if (Answer eq "Y") {
//   Anunasika = true;
//  }
//  if ( (not ParaSavarna) or (not Anunasika) ) {
//   print " Do you want to observe close sandhi after upasargas ? ";
////   readln(Answer);
//   if ( Answer eq "" ) {
//    Answer = "?";
//   }
//   if (Answer eq "Y") {
//    CloseUpasargaSandhi = true;
//   }
//  }
//  print "The optional sandhi in the following sutras will apply:\n";
//  if ( TukPadantat ) {
//   print "     6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71).\n";
//  }
//  if ( ScharSchari ) {
//   print "     8.3.36.  vA Sari.\n";
//  }
//  if ( XkXpKupvoh ) {
//   print "     8.3.37.  kupvoH XkXpau ca.\n";
//  }
//  if ( ChAti ) {
//   print "     8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62 ) . \n";
//  }
//  if ( ParaSavarna ) {
//   print "     8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
//  }
//  if ( Anunasika ) {
//   print "     8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
//  }
//  if ( CloseUpasargaSandhi ) {
//   //PMS close upasarga sandhi
//   print "Close sandhi will be observed after upasargas\n";
//   if ( not ParaSavarna ) {
//    print "After the upasarga "sam",\n";
//    print "     8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
//    }
//   if ( not Anunasika ) {
//    print "After the upasarga "ud",\n";
//    print "     8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)\n";
//    }
//   } //PMS close upasarga sandhi
  Error =4;
 return (Error);
  } //PMS peruse options
//PMS Choose spacing options
 if ( Compound ) {
//  print "Hyphens will be deleted between compound elements.\n";
 }else if ( External ) {
  //PMS spaceoptions
//  print "Spaces will be deleted where a single vowel replaces final and initial vowels.\n";
//  print "Do you wish to eliminate spaces between prefixes and verbs\n";
//  print "and between final consonants and a following sound?\n";
//  print "Y/y (yes) to delete spaces, any other character to keep.";
//  readln(Answer);
  Answer = despace_ans;
//     Answer = "Y"; //force despacing
  if ( Answer.equals("") ) {
   Answer = "?";
  }
  if (Answer.equals("Y")) {
   Despace = true;
  }else if (Answer.equals("N")) {
   Despace = false;
  }else {
   Error =4;
   return (Error);
 } //PMS spaceoptions

}
 Error=0;
 return Error;
 }
 /**
  * returns position in Linary of the last character which is not a space;
  * returns 0 of all elements of Linary are spaces.
  */
 private static int lengthary() {
  for (int I=linmax;1<=I;I--){
   if (!(Linary[I].equals(" "))){
    return I;
   }
  }
  return 0;
 }
 /**
  * Searches Linary for either chtr or fldch. Returns of match.
  * Discounts trailing spaces.
  * @param chtr
  * @param fldch
  * @param istart
  * @return Returns -1 if istart is < 1 or > linmax
  *  Returns 0 if no match found in Linary
  *  Returns index (istart to linmax) of first match found.
  */
 private static int nxtposary(String chtr,String fldch,int istart){
  int I,IEnd;
  if (istart < 1){return -1;}
  if (istart > linmax){return -1;}
  IEnd = lengthary();
  if (IEnd == 0){return 0;}
  for (I=istart;I<=IEnd;I++){
   if (Linary[I].equals(chtr)){return I;}
   if (Linary[I].equals(fldch)){return I;}
 }
  return 0;
 }
 /**
  * Searches backward in Linary for first occurrence of given character
  * @param chtr character to search for
  * @param istart starting position
  * @return return -1 if istart is inappropriate
  * return 0 if chtr not found in Linary
  * return I if nearest occurrence (from istart down to 1) of chtr is at index I
  */
 private static int lastposary(String chtr,int istart){
  int I;
  if (istart < 1){return -1;}
  if (istart > linmax){return -1;}

//error in conversion to Java  if (IEnd == 0){return 0;}
  for (I=istart;1<=I;I--){
   if (Linary[I].equals(chtr)){return I;}
 }
  return 0;
 }
 /**
  * Insert character at given position in Linary.
  * If the position is prior to first position, it resets to first position
  * If position is after the last non-space position, it resets to first ending
  * non-space position.
  * Linary may be augmented by spaces, if necessary. Thus NoSpace will not be set to true.
  * @param chtr character to insert
  * @param index position of insertion
  */
 private static void insertary(String chtr,int index){
  int I,Ipt,IEnd;
  NoSpace=false;
  IEnd = lengthary();
  if (IEnd == linmax){ // add some more space to Linary
//   System.out.println("insertary: Augmenting Linary: linmax starts as " + linmax);
   String s1 = join(Linary,"");
   s1 = s1 + "          ";
    Linary = s1.split(""); // this is what sandhimain modifies.
    linmax = Linary.length - 1;
    IEnd = lengthary();
//    System.out.println("insertary: linmax now " + linmax + ", IEnd= " + IEnd);
  }
  if (IEnd == linmax){
   NoSpace = true;
     System.out.println("WARNING: insertary: NoSpace now " + NoSpace);
   return;
  }
  Ipt = index;
  if ( Ipt < 1 ) {
	  Ipt = 1;
  }
  if ( Ipt > IEnd ) {
  	Ipt = IEnd + 1;
  }
  for (I = IEnd; Ipt <= I; I--) {
	  Linary[I + 1] = Linary[I];
  }
  Linary[Ipt] = chtr;
  return;
 }
 /**
  * remove the character at position 'index' from Linary.
  * If index indexes a position after the last non-space, no character is deleted
  * @param index
  */
 private static void deletary (int index){
  int I,IEnd;
  IEnd = lengthary();
  if ((index >= 1) && (index <= IEnd)){
   for (I = index;I < IEnd;I++){
    Linary[I] = Linary[I+1];
   }
   Linary[IEnd]="";
  }
 }
 /**
  * Returns a substring of Linary consisting of (index1-index2)+1 characters beginning at index1
  * @param index1
  * @param index2
  * @return
  */
 private static String substrary(int index1,int index2){
  int I,IEnd;
  StringBuffer Tempstr = new StringBuffer();
  String ans="";
  IEnd = lengthary();
  if ((index1 < 1) || (index1 > index2) || (index2 > IEnd)) {return ans;}
  if ( ((index2 - index1)+1) > pratipadmax){return ans;}
  if(dbg){
   System.out.println("substrary: index1="+index1+", index2="+index2);
  }
  for (I = index1; I <= index2; I++) {
   Tempstr.append(Linary[I]);
  }
  ans = new String(Tempstr);
  return ans;
 }
 /**
  * Returns positions (Isthana and Iyatna) in Soundary matrix
  * where the character 'aksara' is found.
  * Returns (0,0) if not found.
  * @param aksara
  * @return
  */
 private static int[] identify (String aksara){
  int I1,I2;
  int[] ans = new int[2];

  for (I1=1;I1 <= maxsthana; I1++) {
	  for (I2=1;I2 <=  maxyatna; I2++) {
	   if ( aksara.equals(Soundary[I1][I2]) ) {
     ans[0]=I1; ans[1]=I2;
		   return ans;
	   }
	  }
  }
  ans[0]=0; ans[1]=0;
		return ans;
 }
 /**
  * {1.1.9 vt. fkAraxkArayoH savarRavidhiH}
  * uses globals Linary,Index.
  * May modify Linary,Isthana1,Isthana2
  */
 private static void rlvarnayormithahsavarnyam() {
  if ( (set_memberP(Linary[Index - 1],Rvarna_and_Lvarna)) && (set_memberP(Linary[Index + 1],Rvarna_and_Lvarna)) ) {
   Linary[Index - 1] = sktri;
   Linary[Index + 1] = sktri;
   Isthana1 = imurdhanya;
   Isthana2 = imurdhanya;
   }
   chk_point("rlvarnayormithahsavarnyam");
 }
 /**
  * {6.1.101.  akaH savafRe dIrghaH}
  * Uses globals Linary,Index,Isthana1
  * Modifies Linary,EkahPurvaParayoh
  */
 private static void  akahsavarnedirghah() {
  Linary[Index - 1] = Soundary[Isthana1][idirgha];
  deletary(Index + 1); //{6.1.84.  ekaH pUrvaparayoH}
  EkahPurvaParayoh = true;
  chk_point("akahsavarnedirghah");
 }
 /**
  * 6.1.88.  vfddhir eci
  * Uses globals Linary,Index,Isthana2
  * Modifies Linary,EkahPurvaParayoh
  */
 private static void vrddhireci() {
  Linary[Index - 1] = Soundary[Isthana2][ivrddhi];
  deletary(Index + 1); //{6.1.84.  ekaH pUrvaparayoH}
  EkahPurvaParayoh = true;
 chk_point("vrddhireci");
 }
 /**
  * 6.1.87.  Ad guRaH
  * Uses globals Linary,Index,Isthana2
  * Modifies Linary,EkahPurvaParayoh
  */
private static void adgunah() {
  Linary[Index - 1] = Soundary[Isthana2][iguna];
  if ((Isthana2 == italavya) || (Isthana2 == iosthya)) {
	  deletary(Index + 1); //{6.1.84.  ekaH pUrvaparayoH}
  }else if (Isthana2 == imurdhanya) { //   imurdhanya:
  	Linary[Index + 1] = sktr; //{1.1.51.  uraR raparaH}
  }else if (Isthana2 == idantya) { //   idantya:
  	Linary[Index + 1] = sktl;
  }
  EkahPurvaParayoh = true;
  chk_point("adgunah");
}
 /**
  * 6.1.77.  iko yaR aci
  * Uses globals Linary,Index,Isthana1
  * Modifies Linary
  */
private static void ikoyanaci() {
  Linary[Index - 1] = Soundary[Isthana1][iantahstha];
  chk_point("ikoyanaci");
}
/**
 * 6.1.109.  eNaH padAntAd ati
  * Uses globals Linary,Index
  * Modifies Linary
  */
private static void enahpadantadati() {
   //{}
  Linary[Index + 1] = sktavagraha;
  chk_point("enahpadantadati");
}
/**
 * 6.1.78.  eco 'yavAyAvaH
  * Uses globals Linary,Index
  * Modifies Linary,Index. May set Error
  */
private static void ecoyavayavah() {
 if (Linary[Index - 1].equals(skte)) {
 	Linary[Index - 1] = skta;
	 insertary(skty, Index);
 }else if (Linary[Index - 1].equals(skto)) {
 	Linary[Index - 1] = skta;
	 insertary(sktv, Index);
 }else if (Linary[Index - 1].equals(sktai)) {
	 Linary[Index - 1] = sktaa;
	 insertary(skty, Index);
 }else if (Linary[Index - 1].equals(sktau)) {
	 Linary[Index - 1] = sktaa;
	 insertary(sktv, Index);
 }
 if ( NoSpace ) {
	 Error = 2;
	 return;
 }
 Index = Index + 1;
 chk_point("ecoyavayavah");
}
/**
  * Uses globals Linary,Index,Isthana1,Isthana2
  * Modifies Linary,Index.
 * Calls: rlvarnayormithahsavarnyam, akahsavarnedirghah,vrddhireci,
 * adgunah,ikoyanaci,enahpadantadati,ecoyavayavah
  */
private static void acsandhi() {
 rlvarnayormithahsavarnyam();
 String cprev=Linary[Index - 1];
 String cnext=Linary[Index + 1];
 if ( set_memberP(Linary[Index - 1],Ak) ) {
  if ( (set_memberP(Linary[Index + 1],Ak)) && (Isthana1 == Isthana2) ) {
   akahsavarnedirghah(); //{6.1.101.  akaH savafRe dIrghaH}
  }else if ( set_memberP(Linary[Index - 1],Avarna) ) {
   //PMS: && Linary[Index+1] not in Avarna
   if ( set_memberP(Linary[Index + 1],Ec) ) {
    vrddhireci();  //PMS: 6.1.88  vfddhir eci
   }else {
   //PMS: Linary[Index+1] in Ik
   adgunah(); //PMS: 6.1.87  Ad guRaH
   }
  }else {
   //PMS: Linary[Index-1] in Ik && not savarna with Linary[Index+1]
   ikoyanaci(); //PMS: 6.1.77.  iko yaR aci
  }
 }else {
  //PMS: Linary[Index-1] in Ec
  if ( (set_memberP(Linary[Index - 1],Ekn)) && (Linary[Index + 1].equals(skta)) ) {
   enahpadantadati(); //PMS: 6.1.109.  eNaH padAntAd ati
  }else {
   //PMS: set_memberP(Linary[Index-1],Ec) && set_memberP(Linary[Index+1],Ic)
   ecoyavayavah(); //PMS: 6.1.78.  eco "yavAyAvaH
  }
 }
 chk_point("acsandhi");
}

/**
 * The substring of 'x' specified by idx1,idx2 is replaced by the string y.
 * @param x input string
 * @param idx1  first character position at which to replace (inclusive)
 * @param idx2  last character position at which to replace (exclusive)
 * @param y  string for replacement.
 * @return string resulting from replacement.
 */
private static String strReplace(String x,int idx1,int idx2,String y){
 //char[] ax = x.toCharArray();
 StringBuffer b = new StringBuffer(x);
 b = b.replace(idx1, idx2, y);
 return new String(b);
}
/**
 * Uses globals Pada1,Linary,Index
 * Modifies Pada1,Linary
 */
private static void visargaprep() {
 int L = Pada1.length();
 if ( (Pada1.equals("ahaH")) || (Pada1.equals("svaH")) || (Pada1.equals("antaH")) || (Pada1.equals("prAtaH")) || (Pada1.equals("punaH")) || (Pada1.equals("mAtaH")) || (Pada1.equals("kOsalyAmAtaH")) || (Pada1.equals("sanutaH")) || (Pada1.equals("catuH")) || (Pada1.equals("prAduH")) ) {
  Linary[Index - 1] = sktr;
  Pada1 = strReplace(Pada1,L-1,L,sktr);
 } else {
 Linary[Index - 1] = skts;
 if ( !Pada1.equals("")) {
  Pada1 = strReplace(Pada1,L-1,L,skts);
 }
 }
 chk_point("visargaprep");
}
/**
 * 6.1.73.  che ca (tuk 71)
 * Uses globals Linary,Index,Iyatna1
 * Modifies Linary,Index,Error
 */
private static void checa() {
 if ( (Linary[Index + 1].equals(sktch)) && (Iyatna1 == ihrasva) ) {
  insertary(sktt, Index);
  if ( NoSpace ) {
   Error = 2;
   return;
  }
  Index = Index + 1;
 }
 chk_point("checa");
}
/**
 * 6.1.74.  ANmANoSca (che 73, tuk 71)
 * Uses globals Linary,Index,Pada1
 * Modifies Linary,Index,Error
 */
private static void anmanosca() {
 //PMS: you'll have to add the condition that these are AN && mAN when that info is available
 if ( (Linary[Index + 1].equals(sktch)) && ((Pada1.equals("A")) || (Pada1.equals("mA"))) ) {
  insertary(sktt, Index);
  if ( NoSpace ) {
   Error = 2;
   return;
  }
  Index = Index + 1;
 }
 chk_point("anmanosca");
}
/**
 * 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
 * Uses globals Linary,Index,
 * Modifies Linary,Index,Error,Isthana1,Iyatna1
 */
private static void padantadva() {
 int[] temp = identify(Linary[Index - 1]); //PMS: don"t want to do it if anmanosca just applied
 Isthana1 = temp[0];
 Iyatna1 = temp[1];

 if ( (Linary[Index + 1].equals(sktch)) && (Iyatna1 == idirgha) ) {
  insertary(sktt, Index);
  if ( NoSpace ) {
   Error = 2;
   return; // REPLACE exit(sandhi);
  }
 Index = Index + 1;
 }
 chk_point("padantadva");
}
/**
 * 6.1.132.  etattadoH sulopo 'kor anaYsamAse hali
 * Uses globals Linary,Index,Pada1
 * Modifies Linary,Index
 */
private static void etattadohsulopo() {
 if ( ((Pada1.equals("sas")) || (Pada1.equals("ezas"))) && (set_memberP(Linary[Index + 1],Hal)) ) {
  deletary(Index - 1);
  Index = Index - 1;
 }
 chk_point("etattadohsulopo");
}
/**
 * 8.2.39.  jhalAM jaSo 'nte
 * Uses globals Linary,Index,Pada1
 * Modifies Linary,Isthana1,Iyatna1
 */
private static void jhalamjasonte() {
 int[] temp = identify(Linary[Index - 1]);
 Isthana1 = temp[0];
 Iyatna1 = temp[1];
 if ( set_memberP(Linary[Index - 1],Jhal_not_ru) ) {
  //PMS: because ru =skts; I could choose another character
  Linary[Index - 1] = Soundary[Isthana1][isparsa3];
 } //PMS: jhalamjasonte
 chk_point("jhalamjasonte");
}
/**
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void sasajusoruh() {
 //PMS: 8.2.66.  sasajuzo ruH
 //PMS: exception to 8.2.39 so must apply before it
 if ( Index > 5 ) {
  if (substrary(Index - 5, Index - 1).equals("sajuz")) {
   Linary[Index - 1] = ru;
  }
 }
 if ( Linary[Index - 1].equals(skts) ) {
  Linary[Index - 1] = ru;
  }
 chk_point("sasajusoruh");
}

/**
 * 8.2.68.  ahan
 * Uses globals Linary,Index,Pada1,Pada2
 * Modifies Linary
 */
private static void ahan() {
 if ( Compound ) {
  if (Pada1.equals("ahan")) {
   if ( (Pada2.equals("rUpa")) || (Pada2.equals("rAtri")) || (Pada2.equals("rAtra")) ||
        (Pada2.equals("rAtre")) || (Pada2.equals("rAtrARAm")) || (Pada2.equals("raTantara")) ) {
    Linary[Index - 1] = ru; //PMS: vArttika, but had to add rAtra 21045, rAtre 24028, rAtrARAm 33137
    //PMS: if ahan is termed pada && Pada2 in Sup, so that Linary[Index+1]=sktbh || skts, ditto
   }else {
    Linary[Index - 1] = sktr; //PMS: 8.2.69.  ro "supi
   }
  }
 }
 chk_point("ahan");
}
/**
 * 8.2.70.  amnarUdharavarityubhayathA chandasi
 * Uses globals Linary,Index,Pada1
 * Modifies Linary
 */
private static void amnarudharavar() {
 if ( Chandas ) {
  if ( (Pada1.equals("amnas")) || (Pada1.equals("UDas")) || (Pada1.equals("avas")) ) {
   Linary[Index - 1] = sktr; //PMS: actually you get it both ways in chandas, ru too
  }
 }
 chk_point("amnarudharavar");
}
/**
 * 6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca
 * Uses globals Linary,Index
 * Modifies Linary,Index
 */
private static void atororhasica() {
 if ( Index > 2 ) {
  if ( (Linary[Index - 2].equals(skta)) && (Linary[Index - 1].equals(ru)) ) {
   if (set_memberP(Linary[Index + 1],Hasch_and_skta)) {
    Linary[Index - 2] = skto; //PMS: Linary[Index-1=sktu; adguna
    deletary(Index - 1);
    Index = Index - 1;
   }
  }
 }
 chk_point("atororhasica");
}
/**
 * 8.3.7.  naS chavy apraSAn
 * Uses globals Linary,Index,Pada1
 * Modifies Linary,Index,Error
 */
private static void naschavyaprasan() {
 if ( (Linary[Index - 1].equals(sktn) && (set_memberP(Linary[Index + 1],Chav)) && !(Pada1.equals("praSAn"))) ) {
  Linary[Index - 1] = ru;
  insertary(sktanusvara, Index - 1); //PMS: 8.3.4.  anunAsikAt paro "nusvAraH
  if ( NoSpace ) {
   Error = 2;
   return;
  }
  Index = Index + 1;
 }
 chk_point("naschavyaprasan");
}
/**
 * 8.3.14.  ro ri
 * Uses globals Linary,Index
 * Modifies Linary,Index,Dhralopa
 */
private static void rori() {
 Dhralopa = false;
 if ( (set_memberP(Linary[Index - 1],sktr_and_ru)) && (Linary[Index + 1].equals(sktr)) ) {
  deletary(Index - 1);
  Index = Index - 1;
  Dhralopa = true;
 }
 chk_point("rori");
}
/**
 * 6.3.111.  qhralope pUrvasya dIrgho 'RaH
 * Uses globals Linary,Index,Dhralopa
 * Modifies Linary
 */
private static void dhralope() {
 if ( Dhralopa ) {
  int[] temp = identify(Linary[Index - 1]);
  Isthana1 = temp[0];
  Iyatna1 = temp[1];
  if ( (set_memberP(Linary[Index - 1],An)) && (Iyatna1 == ihrasva) ) {
   Linary[Index - 1] = Soundary[Isthana1][idirgha];
  }
 }
 chk_point("dhralope");
}
/**
 * 8.3.17.  bhobhagoaghoapUrvasya yo 'Si
 * Uses globals Linary,Index,Pada1
 * Modifies Linary
 */
private static void bhobhago() {
 if ( (set_memberP(Linary[Index + 1],Asch)) && (Index > 2) ) {
  if ( (Pada1.equals("bhos")) || (Pada1.equals("bhagos")) || (Pada1.equals("aghos")) ||
       ((set_memberP(Linary[Index - 2],Avarna)) && (Linary[Index - 1].equals(ru))) ) {
   Linary[Index - 1] = skty;
  }
 }
 chk_point("bhobhago");
}
/**
 * 8.3.15.  kharavasAnayor visarjanIyaH
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void kharavasanayor() {
// System.out.println("kharachk: '" + Linary[Index - 1] + "', '"+Linary[Index + 1]+"'" );
 if ( set_memberP(Linary[Index - 1],sktr_and_ru) ) {
  if ( set_memberP(Linary[Index + 1],Khar_and_linend) ) {
   Linary[Index - 1] = sktvisarga;
  }else {
   Linary[Index - 1] = sktr;
  }
 }
 chk_point("kharavasanayor");
}
/**
 * 8.3.19.  lopaH SAkalyasya
 * Uses globals Linary,Index
 * Modifies Linary,Index
 */
private static void lopahsakalyasya() {
 if ( (set_memberP(Linary[Index + 1],Asch)) && (Index > 2) ) {
  if ( (set_memberP(Linary[Index - 2],Avarna)) && (Linary[Index - 1].equals(skty)) ) {
   deletary(Index - 1);
   Index = Index - 1;
  }
 }
 chk_point("lopahsakalyasya");
}
/**
 * 8.3.20.  oto gArgyasya
 * Uses globals Linary,Index
 * Modifies Linary,Index
 */
private static void otogargyasya() {
 if ( set_memberP(Linary[Index + 1],Asch) ) {
  if ( ((Pada1.equals("bhos")) || (Pada1.equals("bhagos")) || (Pada1.equals("aghos"))) ) {
   deletary(Index - 1);
   Index = Index - 1;
  }
 }
 chk_point("otogargyasya");
}
/**
 * 8.3.23.  mo 'nusvAraH
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void monusvarah() {
 if ( (Linary[Index - 1].equals(sktm)) && (set_memberP(Linary[Index + 1],Hal)) ) {
  Linary[Index - 1] = sktanusvara;
 }
 chk_point("monusvarah");
}
/**
 * 8.3.28.  NRoH kukwuk Sari (vA 26)
 * Uses globals Linary,Index
 * Modifies Linary,Index,Error
 * The following two rules 8.3.28 and 31 are optional, but implemented in standard sandhi.  To be consistent with 1991 procedure, we'd have a boolean to select the option and test for the boolean here.
 */
private static void nnohkuktuksari() {
 if (set_memberP(Linary[Index + 1],Schar)) {
  if (Linary[Index - 1].equals(sktkn)) {
   insertary(sktk, Index);
   if ( NoSpace ) {
    Error = 2;
    return;
   }
   Index = Index + 1;
  }
  else if (Linary[Index - 1].equals(sktretron)) {
   insertary(sktretrot, Index);
   if ( NoSpace ) {
    Error = 2;
    return;
   }
   Index = Index + 1;
  }
 }
 chk_point("nnohkuktuksari");
}
/**
 * 8.3.31.  Si tuk (naH 30, Sari 28, vA 26)
 * Uses globals Linary,Index
 * Modifies Linary,Index,Error
 */
private static void situk() {
 if ( (Linary[Index - 1].equals(sktn)) && (Linary[Index + 1].equals(sktsch)) ) {
  insertary(sktt, Index);
  if ( NoSpace ) {
   Error = 2;
   return;
  }
  Index = Index + 1;
 }
 chk_point("situk");
}
/**
 * 8.3.32.  Namo hrasvAd aci NamuR nityam
 * Uses globals Linary,Index
 * Modifies Linary,Index,Error
 */
private static void namohrasvad() {
 int Sthana,Yatna;
 chk_point("namohrasvad enters with Index="+Index+",NoSpace="+NoSpace);
 if ( (Index > 2) ) {
  int[] temp = identify(Linary[Index - 2]);
  Sthana = temp[0];
  Yatna = temp[1];
  if ( (Yatna == ihrasva) && (set_memberP(Linary[Index - 1],KNam)) &&
       (set_memberP(Linary[Index + 1],Ac)) ) {
   insertary(Soundary[Isthana1][isparsa5], Index);
   if ( NoSpace ) {
    Error = 2;
    return;
   }
   Index = Index + 1;
  }else {
   chk_point("namohrasvad Test fails");
   chk_point("Sthana="+Sthana+", Yatna="+Yatna);
   chk_point("penult.char="+Linary[Index - 2]+",Yatna=?ihrasva:"+(Yatna == ihrasva));
   chk_point("Prev char="+Linary[Index - 1]+",test="+set_memberP(Linary[Index - 1],KNam));
   chk_point("Next char="+Linary[Index + 1]+",test="+set_memberP(Linary[Index + 1],Ac));
  }
 }
 chk_point("namohrasvad");
}
/**
 * 8.3.34.  visarjanIyasya saH
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void visarjaniyasyasah() {
 boolean Apavada; // type = boolean;
 if ( (Linary[Index - 1].equals(sktvisarga)) && (set_memberP(Linary[Index + 1],Khar)) ) {
  Apavada = false;
  if ( (Index + 2) < linmax ) {
   if ( set_memberP(Linary[Index + 2],Schar) ) {
    Apavada = true; //PMS: 8.3.35.  Sarpare visarjanIyaH.
   }
  }
  if ( set_memberP(Linary[Index + 1],Ku_and_Pu_and_Schar) ) {
   Apavada = true; //PMS: 8.3.36.  vA Sari.  8.3.37.  kupvoH XkXpau ca.
  }
  if ( ! (Apavada) ) {
   Linary[Index - 1] = skts;
  }
 }
 chk_point("visarjaniyasyasah");
}
/**
 * 8.3.36.  vA Sari
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void vasari() {
 if ( (Linary[Index - 1].equals(sktvisarga)) && (set_memberP(Linary[Index + 1],Schar)) ) {
  Linary[Index - 1] = skts;
 }
 chk_point("vasari");
}
/**
 *  8.3.37.  kupvoH XkXpau ca (khari 15).
 *  8.3.41, 8.3.45 && 8.3.46 are apavAdas of this so must precede it.
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void kupvohXkXpau() {
 boolean Apavada;
 //PMS: by 8.3.15, kharavasAnayorvisarjanIyaH, visarga occurs before avasAna too.  but Xk && Xp don"t.
 if ( (Linary[Index - 1].equals(sktvisarga)) && (set_memberP(Linary[Index + 1],Khar)) ) {
  //PMS: Hence, khari is understood here too
  Apavada = false;
  if ( (Index + 2 < linmax) ) {
   if ( set_memberP(Linary[Index + 2],Schar) ) {
    Apavada = true; //PMS: 8.3.35.  Sarpare visarjanIyaH.
   }
  }
  if ( ! (Apavada) ) {
   if ( set_memberP(Linary[Index + 1],Ku) ) {
    Linary[Index - 1] = sktjihvamuliya;
   }else if ( set_memberP(Linary[Index + 1],Pu) ) {
    Linary[Index - 1] = sktupadhmaniya;
   }
  }
 }
 chk_point("kupvohXkXpau");
}
/**
 * 8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39
 * Uses globals Linary,Index,Pada1
 * Modifies Linary
 */
private static void idudupadhasya() {
 //PMS: exception to 8.3.36.  kupvoH XkaXpau ca, which is an exception to 8.3.34. visarjanIyasya saH,
 //PMS: so should accompany procedure visarjaniyasyasah.  Must follow 8.3.15.  kharavasAnayor visarjanIyaH
 if ( (Linary[Index - 1].equals(sktvisarga)) && (set_memberP(Linary[Index + 1],Ku_and_Pu)) ) {
  if ( (Pada1.equals("nis")) || (Pada1.equals("dus")) || (Pada1.equals("bahis")) ||
       (Pada1.equals("Avis")) || (Pada1.equals("catur")) || (Pada1.equals("prAdur")) ) {
   Linary[Index - 1] = sktsh; //PMS: bahis, Avis =exception to 8.3.46
  }
 }
 chk_point("idudupadhasya");
}
/**
 * 8.3.45. nityamsamAse 'nutarapadasthasya
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void nityamsamase() {
 if ( Compound ) {
  if ( (Linary[Index - 1].equals(sktvisarga)) && (set_memberP(Linary[Index + 1],Ku_and_Pu)) && (Index > 2) ) {
   if ( ((Linary[Index - 2].equals(skti)) || ((Linary[Index - 2].equals(sktu)) && (! Uttarapada))) ) {
    //PMS: Pada1­u.p.
    Linary[Index - 1] = sktsh;
   }
  }
 }
 chk_point("nityamsamase");
}
/**
 * 8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya (samAse 45)
 * Uses globals Linary,Index,Pada1,Pada2
 * Modifies Linary
 */
private static void atahkrkamikamsa() {
 if ( Compound ) {
  if ( (Linary[Index - 1].equals(sktvisarga)) && (set_memberP(Linary[Index + 1],Ku_and_Pu)) && (Index > 2) ) {
   if ( (Linary[Index - 2].equals(skta)) ) {
    if ( (Pada2.equals("kAra")) || (Pada2.equals("kAma")) || (Pada2.equals("kaMsa")) || (Pada2.equals("kumBa")) ||
         (Pada2.equals("kumBI")) || (Pada2.equals("pAtra")) || (Pada2.equals("kuSA")) || (Pada2.equals("karRI")) ) {
     if ( !((Pada1.equals("svar")) || (Pada1.equals("antar")) || (Pada1.equals("prAtar")) || (Pada1.equals("punar")) ||
            (Pada1.equals("sanutar")) || (Pada1.equals("hyas")) || (Pada1.equals("Svas")) || (Pada1.equals("avas")) ||
            (Pada1.equals("aDas")))
          && (! Uttarapada) ) {
      //PMS: miTas, namas, (tiraskAra by 8.3.42.  avaskara, namaskAra?) krtvasuc, suc, i.e. not avyaya
      Linary[Index - 1] = skts;
     }
    }
   }
  }
 }
 chk_point("atahkrkamikamsa");
}
/**
 * 8.4.40.  stoH ScunA ScuH
 * Uses globals Linary,Index
 * Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
 */
private static void stohscunascuh() {
 int Isthana,Iyatna;
 if ( (set_memberP(Linary[Index - 1],Tu_and_skts)) && (set_memberP(Linary[Index + 1],Cu_and_sktsch)) ) {
  int[] temp = identify(Linary[Index - 1]);
  Isthana1 = temp[0];
  Iyatna1 = temp[1];
  Linary[Index - 1] = Soundary[italavya][Iyatna1];
  // Test to see whether the penultimate dental also need to be palatalized, e.g. BavAn Sete (8.3.31)-> BavAnt Sete (8.4.40)-> BavAYc Sete (8.4.63)-> BavAYcCete (8.4.65)-> BavAYCete
  if ( (set_memberP(Linary[Index -2],Tu_and_skts)) && (set_memberP(Linary[Index - 1],Cu_and_sktsch)) ) {
  temp = identify(Linary[Index - 2]);
  Isthana1 = temp[0];
  Iyatna1 = temp[1];
  Linary[Index - 2] = Soundary[italavya][Iyatna1];
  }
 }else if ( (set_memberP(Linary[Index - 1],Cu_and_sktsch)) && (Linary[Index + 1].equals(skts)) ) {
  Linary[Index + 1] = sktsch;
  if ( (Index + 2 < linmax) ) {
   if (Linary[Index + 2].equals(skts)) {
    Linary[Index + 1] = sktsch;
   }
  }
 }else if ( (set_memberP(Linary[Index - 1],Cu)) && (set_memberP(Linary[Index + 1],Tu)) ) {
  //PMS: 8.4.44.  SAt. (na, toH)
  int[] temp = identify(Linary[Index + 1]);
  Isthana2 = temp[0];
  Iyatna2 = temp[1];
  Linary[Index + 1] = Soundary[italavya][Iyatna2];
  if ( (Index + 2 < linmax) ) {
   if (set_memberP(Linary[Index + 2],Tu_and_skts)) {
    temp = identify(Linary[Index + 2]);
    Isthana = temp[0];
    Iyatna = temp[1];
    Linary[Index + 2] = Soundary[italavya][Iyatna];
   }
  }
 }
 chk_point("stohscunascuh");
}
/**
 * 8.4.41.  zwunA zwuH
 * Uses globals Linary,Index
 * Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
 */
private static void stunastuh() {
 int Isthana,Iyatna;
 if ( ( (Linary[Index - 1].equals(sktsh)) && (set_memberP(Linary[Index + 1],Tu_and_skts)) )
      ||  (set_memberP(Linary[Index - 1],Retrotu) && (Pada2.equals("nAm"))) ) {
  //PMS: 8.4.42.  na padAntAwworanAm
  int[] temp = identify(Linary[Index + 1]);
  Isthana2 = temp[0];
  Iyatna2 = temp[1];
  Linary[Index + 1] = Soundary[imurdhanya][Iyatna2];
  if ( (Index + 2 < linmax) ) {
   if (set_memberP(Linary[Index + 2],Tu_and_skts)) {
    temp = identify(Linary[Index + 2]);
    Isthana = temp[0];
    Iyatna = temp[1];
    Linary[Index + 1] = Soundary[imurdhanya][Iyatna2];
    Linary[Index + 2] = Soundary[imurdhanya][Iyatna];
   }
  }
 }else if ( (set_memberP(Linary[Index - 1],Tu) && (set_memberP(Linary[Index + 1],Retrotu)) )
           || ((Linary[Index - 1].equals(skts)) && (set_memberP(Linary[Index + 1],Retrotu_sktsh))) ) {
  //PMS: 8.4.43.  toH zi. (na)
  int[] temp = identify(Linary[Index - 1]);
  Isthana1 = temp[0];
  Iyatna1 = temp[1];
  Linary[Index - 1] = Soundary[imurdhanya][Iyatna1];
 }
 chk_point("stunastuh");
}
/**
 * 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58)
 * Uses globals Linary,Index
 * Modifies Linary,Isthana2,Iyatna2
 */
private static void anusvarasya() {
 //PMS: don"t exercise the option for semivowels (yan) just now
 if ( (Linary[Index - 1].equals(sktanusvara)) && (set_memberP(Linary[Index + 1],Yay_not_Yan)) ) {
  int[] temp = identify(Linary[Index + 1]);
  Isthana2 = temp[0];
  Iyatna2 = temp[1];
 Linary[Index - 1] = Soundary[Isthana2][isparsa5];
 }
 chk_point("anusvarasya");
}
/**
 * 8.4.60.  tor li
 * Uses globals Linary,Index
 * Modifies Linary,Isthana1,Iyatna1,Index,Error
 */
private static void torli() {
 if ( (set_memberP(Linary[Index - 1],Tu)) && (Linary[Index + 1].equals(sktl)) ) {
  int[] temp = identify(Linary[Index - 1]);
  Isthana1 = temp[0];
  Iyatna1 = temp[1];
 Linary[Index - 1] = sktl;
 if ( Iyatna1 ==isparsa5 ) {
  insertary(sktnasalization, Index);
  if ( NoSpace ) {
  Error = 2;
  return;
  }
  Index = Index + 1;
 }
 }
 chk_point("torli");
}
/**
 * 8.4.62.  jhayo ho 'nyatarasyAm
 * Uses globals Linary,Index
 * Modifies Linary,Isthana1,Iyatna1
 */
private static void jhayoho() {
 if ( (set_memberP(Linary[Index - 1],Jhay)) && (Linary[Index + 1].equals(skth)) ) {
  int[] temp = identify(Linary[Index - 1]);
  Isthana1 = temp[0];
  Iyatna1 = temp[1];
 Linary[Index + 1] = Soundary[Isthana1][isparsa4];
 }
 chk_point("jhayoho");
}
/**
 * 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void saschoti() {
 if ( (set_memberP(Linary[Index - 1],Jhay)) && ((Index + 2) < linmax) ) {
  if ( (Linary[Index + 1].equals(sktsch)) && (set_memberP(Linary[Index + 2],At)) ) {
   Linary[Index + 1] = sktch;
  }
 }
 chk_point("saschoti");
}
/**
 * 8.4.63 vt [964].  Catvam amIti vaktavyam.  E.g. tacchlokena, tacchmaSruRA
 * Uses globals Linary,Index
 * Modifies Linary
 */
private static void chatvamami() {
 if ( (set_memberP(Linary[Index - 1],Jhay)) && ((Index + 2) < linmax) ) {
  if ( (Linary[Index + 1].equals(sktsch)) && (set_memberP(Linary[Index + 2],Am)) ) {
   Linary[Index + 1] = sktch;
  }
 }
 chk_point("chatvamami");
}
/**
 * 8.4.65.  Jaro Jari savarRe (halaH 64).
 * Uses globals Linary,Index,Isthana1,Isthana2
 * Modifies Linary
 */
private static void jharojharisavarne() {
 if ((Index + 2) < linmax) {
  if ( (set_memberP(Linary[Index - 2],Hal)) && (set_memberP(Linary[Index - 1],Jhar)) && (set_memberP(Linary[Index + 1],Jhar)) ) {
   int[] temp = identify(Linary[Index - 1]);
   Isthana1 = temp[0];
   temp = identify(Linary[Index + 1]);
   Isthana2 = temp[0];
   if (Isthana1 == Isthana2) {
   deletary(Index - 1);
   Index = Index - 1;
   }
  }
 }
 chk_point("jharojharisavarne");
}
/**
 * 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
 * Uses globals Linary,Index
 * Modifies Linary,Isthana1,Iyatna1,Isthana2,Iyatna2
 */
private static void yaronunasike() {
  int[] temp = identify(Linary[Index + 1]);
  Isthana2 = temp[0];
  Iyatna2 = temp[1];
 //PMS: if ( set_memberP(Linary[Index - 1],Yar) && (Index + 2 < linmax) then
 //PMS: if (Iyatna2 eq isparsa5) || (Linary[Index + 2].equals(sktanunasika) ) {
 //PMS: we wont exercise the nasalized option for the semivowels y, v && l; just for the stops
 if ( (set_memberP(Linary[Index - 1],Jhay)) && (Iyatna2 == isparsa5) ) {
  temp = identify(Linary[Index - 1]);
  Isthana1 = temp[0];
  Iyatna1 = temp[1];
  Linary[Index - 1] = Soundary[Isthana1][isparsa5];
 }
 chk_point("yaronunasike");
}
/**
 * 8.4.55.  khari ca. (jhalAm 53, car 54)
 * Uses globals Linary,Index
 * Modifies Linary,Isthana1,Iyatna1
 */
private static void kharica() {
 //PMS: there is no final  "h" after jhalAm jaSo "nte, but there is skts by 8.3.34 visarjanIyasya saH
 //PMS: && sktsch && sktsh by 8.4.40-41 stoH ScunA scuH, zwunA zwuH so must exclude Sar
 if ( set_memberP(Linary[Index - 1],Jhay) ) {
  //PMS: jhay=jhal-Sar
  int[] temp = identify(Linary[Index - 1]);
  Isthana1 = temp[0];
  Iyatna1 = temp[1];
  if ( set_memberP(Linary[Index + 1],Khar_and_linend) ) {
   //PMS: 8.4.56.  vavasane
   Linary[Index - 1] = Soundary[Isthana1][isparsa1];
  }
 }
 chk_point("kharica");
}
/**
 * 1.1.11. IdUdeddvivacanam pragfhyam
 * Uses globals Linary,Index,Pada1
 * Modifies Linary,Pragrhya
 */
private static void idudeddvivacanampragrhyam() {
 //PMS: 1.1.11. IdUdeddvivacanam pragfhyam
 Pragrhya = false;
 String c = Linary[Index - 1];
 if ( External ) {
  if(c.equals(sktii)) {
   if ( (Pada1.equals("amI")) || (Pada1.equals("aDiparI")) || (Pada1.equals("aBipratI")) || (Pada1.equals("manasI")) ) {
    Pragrhya = true;
   }
  }else if (c.equals(sktuu)) {
   if ( (Pada1.equals("amU")) ) {
    //PMS: 1.1.12.  adaso mAt
    Pragrhya = true;
   }
  }else if (c.equals(skte)) {
   if ( (Pada1.equals("SAlInakOpIne")) || (Pada1.equals("uBe")) ) {
    Pragrhya = true;
   }
  }else if (c.equals(skto)) {
   if ( (Pada1.equals("Aho")) || (Pada1.equals("utAho")) ) {
    //PMS: 1.1.15. ot
    Pragrhya = true;
   }
  }
 }
 chk_point("idudeddvivacanampragrhyam");
}
/**
 * This routine inadequately documented
*/
private static void sandhiPrep() {
 int L,IPada;
 boolean NoPrep;
 NoStoh = false;
 NoKNam = false;
 NoPrep = false;
 Exception = false;
 Pronoun = true; //PMS: saú is usually the pronoun tad
 OtherCloseSandhi = false;
 L = Pada1.length();
 if (L <= 1) {
 return;
 }
 String c = Pada1.substring(L-1,L); // last character of Pada1.
 if (dbg) {
  System.out.println("sandhiPrep: Pada1='"+Pada1+"', c="+c);
  System.out.println("Is c = skts? "+ c.equals(skts));
  System.out.println("is Pada1 = us? " + Pada1.equals("us"));
 }
 if (c.equals(sktkn)) {
  // RiN change made 20090801, PMS.
  if (Pada1.equals("RiN")) {
   Exception = true;
  }
 }else if (c.equals(sktc)) {
  for (IPada = 1; IPada <= cantamax;IPada++) {
   if ( Pada1.equals(CAntaPadary[IPada]) ) {
    NoPrep = true;
    NoStoh = true;
    IPada = cantamax; // leave loop
   }
  }
 }else if (c.equals(sktj)) {
  if ( (Pada1.equals("tij")) ) {
   Exception = true;
  }else if ( (Pada1.equals("tuj")) ) {
   NoPrep = true;
  }
 }else if (c.equals(sktcn)) {
  if ( (Pada1.equals("aY")) || (Pada1.equals("alaNkfY")) || (Pada1.equals("nirAkfY")) ||
       (Pada1.equals("naY")) || (Pada1.equals("wIwaY")) || (Pada1.equals("WaY")) ) {
   NoStoh = true;
  }
 }else if (c.equals(sktretron)) {
  if ( (Pada1.equals("aR")) || (Pada1.equals("uR")) || (Pada1.equals("yaR")) ) {
   Exception = true;
  }
 }else if (c.equals(sktdh)) {
  if ( (Pada1.equals("aD")) || (Pada1.equals("ruD")) ) {
   Exception = true;
  }
 }else if (c.equals(sktn)) {
  if ( (Pada1.equals("Wan")) || (Pada1.equals("tran")) || (Pada1.equals("dozan")) ||
       (Pada1.equals("yakan")) || (Pada1.equals("yUzan")) || (Pada1.equals("Sakan")) ||
       (Pada1.equals("zWan")) || (Pada1.equals("han")) ) {
   NoPrep = true;
  }else if ( (Pada1.equals("Ayan")) || (Pada1.equals("Gan")) ) {
// if (!PaninianText)
  //PMS (June 2010)The whole section of sandhiPrep up to "if Compound"
  // is aimed specifically at the Astadhyayi and perhaps other texts of
  //  Paninian grammar and should be excluded from general sandhi.
   if (PaninianText){
    NoPrep = true;
    NoKNam = true;
   }
  }else if ( (Pada1.equals("ktin")) || (Pada1.equals("kvin")) || (Pada1.equals("min")) || (Pada1.equals("vin")) ) {
   NoPrep = true;
  }else if ( (Pada1.equals("an")) || (Pada1.equals("in")) || (Pada1.equals("kan")) ||
             (Pada1.equals("kaDyEn")) || (Pada1.equals("qvun")) || (Pada1.equals("tan")) ||
             (Pada1.equals("dAn")) || (Pada1.equals("man")) || (Pada1.equals("vun")) ) {
   Exception = true;
  }else if ( Pada1.equals("tumun") ) {
   NoStoh = true;
  }
 }else if (c.equals(sktm)) {
  if ( (Pada1.equals("am")) || (Pada1.equals("Am")) || (Pada1.equals("num")) ) {
   Exception = true;
  }else if ( Compound ) {
   if ( ((Pada1.equals("puram")) && (Pada2.equals("dArO"))) ) {
    //PMS: purandrau
    OtherCloseSandhi = true;
   }
  }
 }else if (c.equals(skty)) {
  if ( (Pada1.equals("ay")) || (Pada1.equals("Ay")) ) {
   Exception = true;
  }
 }else if (c.equals(sktr)) {
  if ( (Pada1.equals("car")) || (Pada1.equals("kur")) || (Pada1.equals("Sar")) ) {
   Exception = true;
  }
 }else if (c.equals(sktsch)) {
  if ( (Pada1.equals("eS")) || (Pada1.equals("KaS")) || (Pada1.equals("jaS")) || (Pada1.equals("niS")) ) {
   Exception = true;
  }
 }else if (c.equals(sktsh)) {
  if ( (Pada1.equals("Jaz")) || (Pada1.equals("Baz")) ) {
   Exception = true;
  }
 }else if (c.equals(skts)) {
     chk_point("sandhiPrep at c=skts "+ Exception);

  if ( (Pada1.equals("as")) || (Pada1.equals("atus")) || (Pada1.equals("aTus")) ||
       (Pada1.equals("is")) || (Pada1.equals("us")) || (Pada1.equals("os")) ||
       (Pada1.equals("kas")) || (Pada1.equals("kAs")) || (Pada1.equals("Nas")) ||
       (Pada1.equals("tas")) || (Pada1.equals("tAs")) || (Pada1.equals("TAs")) ||
       (Pada1.equals("Bis")) || (Pada1.equals("Byas")) ) {
   Exception = true;
   chk_point("sandhiPrep setting Exception to "+ Exception);

  }
 }
 if ( Compound ) {
  //PMS: normal stem changes
  if ( (! Exception) && (! NoPrep) ) {
   c = Linary[Index - 1];
   if (c.equals(sktc)) {
    if ( Pada1.equals("aYc") ) {
     //PMS: aYc
     Linary[Index - 1] = sktk; //PMS: ak
     deletary(Index - 2);
     Index = Index - 1;
    } else {
     Linary[Index - 1] = sktk;
    }
   }else if (c.equals(sktch)) {
    Linary[Index - 1] = sktk;
   }else if (c.equals(sktj) ) {
    if ( (Pada1.equals("rAj")) ) {
     Linary[Index - 1] = sktretrot;
    }else {
     Linary[Index - 1] = sktk;
    }
   }else if (c.equals(sktjh)) {
    Linary[Index - 1] = sktk;
   }else if (c.equals(sktn)) {
    if ( Index > 2 ) {
     if ( (Linary[Index - 2].equals(skta)) || (Linary[Index - 2].equals(skti)) ) {
      //PMS: an-/in-
      if ( ((Pada1.equals("ahan")) && (!PurvaPada.equals("eka"))) ) {
       // noop
      }else {
       //PMS: normal "an-"/"in-"
       deletary(Index - 1);
       Index = Index - 1;
      }
     } //PMS: an-/in-
    }
   }else if (c.equals(sktr)) {
    if ( (Pada1.equals("pur")) || (Pada1.equals("Dur")) ) {
     Linary[Index - 2] = sktuu;
    }
   }else if (c.equals(sktsch)) {
    if ( Pada1.equals("viS") ) {
     Linary[Index - 1] = sktretrot;
    }else {
     Linary[Index - 1] = sktk;
    }
   }else if (c.equals(sktsh)) {
    if ( Pada1.equals("daDfz") ) {
     Linary[Index - 1] = sktk;
    }
   }else if (c.equals(skts)) {
    if ( (Pada1.equals("ASis")) ) {
     Linary[Index - 2] = sktii; //PMS: 82104
    }else if ( Pada1.equals("pums") ) {
     //PMS: "pum"
     deletary(Index - 1);
     Index = Index - 1;
     }
   }else {
    //PMS: no preparation necessary, normal sandhi will follow
   } //PMS: case statement
  } //PMS: astadhyayiSandhiPrep
 } //PMS: sandhiprep
}
/**
 * From a given input string, generate an array of strings.
 * The even elements (0,2,4...) of the array have value
 * "s" if the next array element is a string of Sanskrit characters
 * "o" if the next array element is a string of other non-Sanskrit characters
 * Sanskrit characters are according to the SLP1 spelling.
 * <p>
 * "- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/"
 * <p>
 * Note that the '/' is an artificial 'Sandhi-blocking' character.
*/

private static String[] sandhiSplit(String x) {
 ArrayList<String> a = new ArrayList<String>();
 int INITIAL = 0;
 int SKT = 1;
 int OTHER = 2;

 // The only non-alphabetic chars considered to be Sanskrit are
 // ~, -, space, apostrophe, "|" and "/"
 // 20090801, "/" is a sandhi-blocking character.

// String sanskrit_str = "- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/";
 // June 22: Added period to list of Sanskrit characters.
 String sanskrit_str = "~- '.aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/";
 String[] sanskrit_strs = sanskrit_str.split("");
 List sanskrit_strs_list = Arrays.asList(sanskrit_strs);
 HashSet<String> sanskrit_set = new HashSet<String>(sanskrit_strs_list);
 String[] xarr = x.split("");
 int len = xarr.length;
 int state = INITIAL;
 boolean more = true;
 StringBuffer y = new StringBuffer();
 String c;
 for(int ipos=0;ipos<len;ipos++) {
  c = xarr[ipos];
  if (state == INITIAL) {
   y = new StringBuffer();
   if (sanskrit_set.contains(c)) {
    state = SKT;
    y.append(c);
   }else {
    state = OTHER;
    y.append(c);
   }
  }else if (state == SKT) {
   if (sanskrit_set.contains(c)) {
    y.append(c);
   }else {
    a.add("s");
    a.add(new String(y));
    y = new StringBuffer();
    y.append(c);
    state = OTHER;
   }
  }else  { // state = OTHER
   if (sanskrit_set.contains(c)) {
    a.add("o");
    a.add(new String(y));
    y = new StringBuffer();
    y.append(c);
    state = SKT;
   }else  {
    y.append(c);
   }
  }
 }
 if (y.length() != 0) {
  if (state == SKT) {
   a.add("s");
   a.add(new String(y));
  }else if (state == OTHER) {
   a.add("o");
   a.add(new String(y));
  }else { // should not occur
  }
 }
 Object[] temp = a.toArray();
 int l = temp.length;
 String[] ans = new String[l];
 for(int i=0;i<l;i++){
  ans[i]=(String)a.get(i);
 }
 return ans;
}

/**
  * Prepare input for sandhimain
  * Accept string argument, to which sandhi is to be applied.
  * return a string argument as the answer
  * return a blank string if there is an error
  * print an informative message if there is an error.
 * Two special values of 's' are related to debugging: 'dbg' and 'off'
*/
private static String sandhi1(String s) {
 String s1 = s.trim();
 if ((s.equals("dbg")) || (s.equals("off"))) {
  if (! dbg) {
   System.out.println("Turning on debug. To turn off, enter 'off'");
   dbg = true;
  }else {
   System.out.println("Turning off debug. To turn on, enter 'dbg'");
   dbg = false;
  }
  return "";
 }
 s1 = " " + s1 + "    ";
 Linary = s1.split(""); // this is what sandhimain modifies.
 linmax = Linary.length - 1;
 chk_point("calling sandhimain with:'" + join(Linary,"")+"'");
 Error = 0;
 sandhimain();
 // change of June 22, 2010
 if (NoSpace && (Error == 2)){
  Error = 0;
 }
 if (Error != 0) {
// if ((Error != 0) && (!((NoSpace && (Error == 2))))){
  System.out.println("Sandhi error: " + Error + ", s = " + s);
  return "";
 }else {
 String ans = join(Linary,"");
 ans = ans.trim();
 return(ans);
 }
}
private static void sandhimain() {
 // initialize some global variables
 Isthana1 = 0;
 Isthana2 = 0;
 Iyatna1 = 0;
 Iyatna2 = 0;
 IEnd = 0;
 Index = 0;
 Found = false;
 NoSpace = false;
 Dhralopa = false;
 OtherCloseSandhi = false;
 Pragrhya = false;
 Uttarapada = false;
 NxtUttarapada = false;
 //  initialize some local variables
 int Inext = 0;
 int Inextsp = 0;
 int IPrev = 0;
 int IPrevSpace = 0;
 int I = 0;

 PurvaPada = "";
 Pada1 = "";
 Pada2 = "";
 Index = nxtposary(Padbound, FldChr, 2); //PMS: the first character in Linary should not be a word boundary
  chk_point("sandhimain. Initial Index = "+Index);
 
 Upasarga = false; // ejf.
 while (Index > 0)  {
//  System.out.println("Index="+Index);
  //PMS: while a padbound character is found
  EkahPurvaParayoh = false;
  //PMS: PurvaPada, Pada1, Pada2
  Uttarapada = false;
  if ( NxtUttarapada ) {
   Uttarapada = true; //PMS: Pada1 is an uttarapada
  }
  NxtUttarapada = false;
  //PMS: first Pada1 in Linary
  PurvaPada = Pada1;
  if ( IPrev == 0 ) {
   //PMS: first Pada1 in Linary
   if ( Compound ) {
    IPrev = lastposary(space, Index - 1);
   }else {
    //July 2010.  On the first pass, Pada1 is known to begin with
    // a blank, unless the following is done.
    IPrev = lastposary(space, Index - 1);
   }
   Pada1 = substrary(IPrev + 1, Index - 1);
   chk_point("sandhimain. Pada1='"+Pada1+"', Compound="+Compound+", IPrev="+IPrev+",Index="+Index);
   
  }else if ( External ) {
   //PMS: we've been through here before so
   Pada1 = Pada2;
  }else {
   //PMS: padbound=hyphen
   Pada1 = NxtPada1;
  }
  Inext = nxtposary(Padbound, FldChr, Index + 1);
  if ( Inext == 0 ) {
   //PMS: not found so last word
   Inext = lengthary() + 1;
  }
  if ( External ) {
   Pada2 = substrary(Index + 1, Inext - 1);
  }else {
   //PMS: for compound, Pada2, NxtPada1
   Inextsp = nxtposary(space, FldChr, Index + 1);
   if ( (Inextsp > 0) && (Inextsp < Inext) ) {
    Pada2 = substrary(Index + 1, Inextsp - 1);
   }else {
    Pada2 = substrary(Index + 1, Inext - 1);
   }
   //PMS: now the next Pada1 when padbound =hyphen
   IPrevSpace = lastposary(space, Inext - 1);
   if ( IPrevSpace > Index ) {
    NxtPada1 = substrary(IPrevSpace + 1, Inext - 1); // corrected
   }else {
    NxtPada1 = Pada2;
    NxtUttarapada = true;
   }
  } //PMS: Pada2, NxtPada1 hyphen
  //PMS: end of PurvaPada, Pada1, Pada2
  //PMS: determine whether Pada1 is an upasarga
  Upasarga = false;
  if ( External && (Pada1.equals("ut")) ) {
   Pada1 = "ud";
  }
  if ( Pada1.equals("api") ) {
   //PMS: more likely karmapravacanIya than upasarga
  }else {
   for (I = 1; I <= pradimax;I++) {
    if ( Pada1.equals(Pradi[I]) ) {
     Upasarga = true;
     I = pradimax; //to leave loop
    }
   }
  }
  //PMS: stem final sound changes for compound sandhi && some special sandhi for grammatical technical terms
  sandhiPrep();
  boolean doSandhi=true;
  chk_point("sandhimain, Exception = "+Exception);
  if (Exception ) {
   doSandhi=false;
  }else {
   if ( Upasarga && CloseUpasargaSandhi ) {
    OtherCloseSandhi = true; //PMS: initialized in sandhiPrep
   }
   //PMS: sandhi subroutines:  within compound && following an upasarga closer sandhi is observed when an option is allowed
   //PMS: otherwise (between syntactic units) looser sandhi is observed
   idudeddvivacanampragrhyam(); //PMS: kosher exceptions to sandhi
   if ( Pragrhya ) {
    doSandhi=false;
   }
  }
  if (doSandhi) {
   if ( (Linary[Index - 1].equals(sktvisarga)) ) {
    visargaprep();
   }
   int[] temp = identify(Linary[Index - 1]);
   Isthana1 = temp[0];
   Iyatna1 = temp[1];
   temp = identify(Linary[Index + 1]);
   Isthana2 = temp[0];
   Iyatna2 = temp[1];
   //PMS: must precede 8.4.40.  stoH ScunA ScuH
   checa(); //PMS: 6.1.73.  che ca
   anmanosca(); //PMS: 6.1.74.  ANmANoSca (che 73, tuk 71)
   if ( (TukPadantat) ) {
    padantadva(); //PMS: 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
   }
   //PMS: must precede vowel sandhi
   if ( set_memberP(Linary[Index - 1],sktn_and_sktsh_and_skts) ) {
    if ( Pronoun ) {
     etattadohsulopo(); //PMS: 6.1.132.  etattadoH sulopo "kor anaYsamAse hali
    }
    amnarudharavar(); //PMS: 8.2.70.  amnarUdharavarityubhayathA chandasi
    sasajusoruh(); //PMS: 8.2.66.  sasajuzo ruH
    if ( ! NoStoh ) {
     //PMS: exception in 63110
     ahan(); //PMS: 8.2.68.  ahan
    }
    atororhasica(); //PMS: 6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca.  Must precede 6.1.109.  eNaH padAntAd ati
   }
   if ( set_memberP(Linary[Index - 1],Ac) && set_memberP(Linary[Index + 1],Ac) ) {
    acsandhi();
   }else if ( (set_memberP(Linary[Index - 1],Hal_and_ru)) && (set_memberP(Linary[Index + 1],Al_and_Linend)) ) {
    jhalamjasonte(); //PMS: 8.2.39.  jhalAM jaSo "nte
    naschavyaprasan(); //PMS: 8.3.7.  naS chavy apraSAn
    rori(); //PMS: 8.3.14.  ro ri  ejf: Dhralopa is global
    dhralope(); //PMS: 6.3.111.  qhralope pUrvasya dIrgho "RaH
    bhobhago(); //PMS: 8.3.17.  bhobhagoaghoapUrvasya yo "Si
    kharavasanayor(); //PMS: 8.3.15.  kharavasAnayor visarjanIyaH
    otogargyasya(); //PMS: 8.3.20.  oto gArgyasya.  This cannot precede vowel sandhi
    monusvarah(); //PMS: 8.3.23.  mo "nusvAraH
    chk_point("NoKNam = "+NoKNam);
    if ( ! NoKNam ) {
     namohrasvad(); //PMS: 8.3.32.  Namo hrasvAd aci NamuR nityam
    }
    visarjaniyasyasah(); //PMS: 8.3.34.  visarjanIyasya saH
    if ( ScharSchari ) {
     vasari(); //PMS: 8.3.36.  vA Sari
    }
    //PMS: 8.3.41, 8.3.45 && 8.3.46 are apavAdas of 8.3.37 so they must precede it
    idudupadhasya(); //PMS: 8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39)
    nityamsamase(); //PMS: 8.3 .45. nitya samAse "nutarapadasthasya
    atahkrkamikamsa(); //PMS: 8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya
    if ( XkXpKupvoh ) {
     kupvohXkXpau(); //PMS: 8.3.37.  kupvoH XkXpau ca (khari 15).
    }
    nnohkuktuksari(); //PMS: 8.3.28.  NRoH kukwuk Sari
    situk(); //PMS: 8.3.31.  Si tuk
    if ( ! NoStoh ) {
     stohscunascuh(); //PMS: 8.4.40.  stoH ScunA ScuH
     stunastuh(); //PMS: 8.4.41.  zwunA zwuH
    }
    torli(); //PMS: 8.4.60.  tor li
    if ( ChAti ) {
     saschoti(); //PMS: 8.4.63.  SaS cho "wi. (jhayaH 62, anyatarasyAm 62)
     chatvamami(); //PMS: 8.4.63 vt. 964 chatvamamIti vaktavyam
    }
    jhayoho(); //PMS: 8.4.62.  jhayo ho "nyatarasyAm
    jharojharisavarne(); //PMS: 8.4.65 Jaro Jari savarRe
    kharica(); //PMS: 8.4.55.  khari ca
    if ( ParaSavarna || OtherCloseSandhi ) {
     anusvarasya(); //PMS: 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
    }
   }
   if ( (set_memberP(Linary[Index - 1],Hal)) && (set_memberP(Linary[Index + 1],Al)) ) {
    //PMS: must follow vowel sandhi
    lopahsakalyasya(); //PMS: 8.3.19.  lopaH SAkalyasya.  Must follow 6.1.78.  eco "yavAyAvaH
    //PMS: If made to include semivowels, 8.4.45 must follow 8.3.19-20.  In present form it needn"t.
    if ( Anunasika || OtherCloseSandhi ) {
     yaronunasike(); //PMS: 8.4.45.  yaro "nunAsike "nunAsiko vA. (padAnta 42)
    }
   }
  }
  chk_point("label7000a");
  //PMS: get rid of the space between words
  if ( EkahPurvaParayoh ) {
   //PMS: EkahPurvaParayoh set in acsandhi in subroutines: akahsavarnedirghah, adgunah, vrddhireci
   //PMS: do the same steps if two padbounds in a row because last sandhi eliminated single char word
   deletary(Index);
   Index = Index - 1; //PMS: the search for the next padbound begins at Index+1
  }else if ( (Index > 1) && Despace ) {
   if ( set_memberP(Linary[Index - 1],Hal) || Linary[Index - 1].equals(sktnasalization) || Upasarga ) {
    //PMS: Restored "or Upasarga"
    deletary(Index);
   }
  }
  if ( Linary[Index].equals(hyphen) ) {
   deletary(Index);
   Index = Index - 1;
  }
  IPrev = Index;
  Index = nxtposary(Padbound, FldChr, Index + 1); //PMS: find the next pada boundary
  chk_point("label7000b");
  if (dbg) {System.out.println( "Index = "+Index);}
 } //PMS: conclude while loop when padbound character is not found (Index=0)
}
/**
  * Accept string argument, to which sandhi is to be applied.
  * Return a string argument as the answer
  * Return a blank string if there is an error
  * Print an informative message if there is an error.
*/
public static String sandhi(String s) {
 String whitebeg,whiteend,x,y,ans;
 String[] split = sandhiSplit(s);
 int n = split.length;
 whitebeg="";
 ans=whitebeg;
 int i = 0;
 // the doubling '\\' is a Java quirk of string literals
 // \s is whitespace
 Pattern p1 = Pattern.compile("^(\\s+)(.*)$");
 Pattern p2 = Pattern.compile("(.*?)(\\s+)");
 Matcher m;
 boolean mFlag;
 while (i < n) {
  x = split[i+1];
  m = p1.matcher(x);
  if (m.matches()) {
   whitebeg=m.group(1);
   x = m.group(2);
  }else {
   whitebeg="";
  }
  m = p2.matcher(x);
  if (m.matches()) {
   whiteend=m.group(2);
   x = m.group(1);
  }else {
   whiteend="";
  }
  if (split[i].equals("s")) {
   y = sandhi1(x);
  }else {
   y = x;
  }
  y = whitebeg + y + whiteend;
  ans += y;
  i += 2;
 }
 return ans;
}
/**
 * 
 * @param strings
 * @param separator
 * @return
 */
public static String join(String[] strings, String separator) {
    StringBuffer sb = new StringBuffer();
    for (int i=0; i < strings.length; i++) {
        if (i != 0) sb.append(separator);
  	    sb.append(strings[i]);
  	}
  	return sb.toString();
}

 /**
  * a debugging routine. If global 'dbg' value is true, then
  * a debugging message is printed labeled with the parameter 's'
  * @param s
  */
 private static void chk_point(String s){
  if (dbg){
   System.out.println(s + "(" + Index + "," + linmax + "):"+NoSpace + ":" +join(Linary,""));
  }
 }
 public static void main(String[] args){
   if (0 == 1){
    int err = sandhioptions("C","N","S","");
    System.out.println("sandhioptions err="+err);
    err = sandhioptions("E","N","S","Y");
    System.out.println("sandhioptions err="+err);
    String x = "ABCDE";
    String y = strReplace(x,2,4,"XY");
    System.out.println("x="+x+" => "+y);
   }
   if (0 == 1){
    String s = "  rAmo 'gacCat . hari-rAmaH";
    System.out.println("s = "+ s);
    String[] split = sandhiSplit(s);
    for(int i=0;i<split.length;i++){
     System.out.println(i+":"+split[i]);
    }
   }
   if (0 == 1){
    String s = "  abc";
    Pattern p = Pattern.compile("^(\\s+)(.*)$");
    Matcher m = p.matcher(s);
    boolean b = m.matches();
    if (b){
     System.out.println("s="+s+",$1="+m.group(1)+",$2="+m.group(2));
    }else {
     System.out.println("No match");
    }
   }
   if (0 == 1){
    String[] s = new String[2];
    s[0]="abc"; s[1]="def";
    String s1 = join(s,"");
    System.out.println("s1="+s1);
   }
   if (0 == 1){
    sandhioptions("C","N","S","");
    String s = "tat-gam";
    String s1 = sandhi(s);
    System.out.println(s + " => " + s1);
    sandhioptions("E","N","S","Y");
    s = "rAmaH agacCat";
    s1 = sandhi(s);
    System.out.println(s + " => " + s1);
   }
   if (0 == 0){
    dbg=true;
    dbg=false;
    sandhioptions("E","N","S","Y");
    String s = "apa harati";
    System.out.println("-----------test of "+s);
    String s1 = sandhi(s);
    System.out.println(s + " => " + s1);

    s = "tasmin Socati";
    System.out.println("-----------test of "+s);
    s1 = sandhi(s);
    System.out.println(s + " => " + s1);
   }
    if (0 == 1){
//   dbg=true;
    sandhioptions("C","N","S","");
     String s = "us-kuus .";
    String s1 = sandhi(s);
    System.out.println(s + " => " + s1);
   }
 }
}
