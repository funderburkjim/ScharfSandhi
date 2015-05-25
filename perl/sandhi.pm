package sandhi;
use Exporter ();
@ISA = qw(Exporter);
@EXPORT = qw(sandhi sandhioptions);

# sandhi.pm
# implementation of 'sandhi' routine from SandhiGen.pp (PMS 2000/10/14)
# This is derived from sandhi-inc/sandhi.pl, by directly including all the
# 'plinc' files.
# Perl implementation Feb 9, 2009  ejf 
# April 22, 2009 ejf : split string into Sanskrit/non-Sanskrit before sandhi
#PMS 1999/9 added to procedure visarga prep the words: punaH, $mAtaH, $kOsalyAmAtaH
#PMS 2000/9/4 changed procedure torli to insert $sktnasalization before $sktl rather than $sktanunasika after it.
#PMS 2000/9/4 added line to procedure ahan to restrict it to compounds.  Did not insert "elsif ( ($Pada2 in $Linend) ) {" to assume that clause-final ahan is not the noun.
#PMS 2000/9/4 added ahaH to visargaprep procedure.
#PMS 2000/10/14 disabled removal of space after upasargas ($Removed "or Upasarga") and close sandhi option for upasargas.

#ejf: open question: How to handle return; # REPLACE exit($sandhi);

#require "./sanskrit01.plinc";
# sanskrit01.plinc, from TransliterateAll.pp
# perl stub that defines the '$skt*' constants
#{The Sanskrit sounds represented in $the font Sanskrit01}
  $skta = 'a';
  $sktaa = 'A';
  $skti = 'i';
  $sktii = 'I';
  $sktu = 'u';
  $sktuu = 'U';
  $sktri = 'f';
  $sktrii = 'F';
  $sktlri = 'x';
  $sktlrii = 'X';
  $skte = 'e';
  $sktai = 'E';
  $skto = 'o';
  $sktau = 'O';
  $sktvisarga = 'H';
  $sktjihvamuliya = '»'; #{opt k}
  $sktupadhmaniya = '¹'; #{opt p}
  $sktanusvara = 'M';
  $sktanunasika = 'µ'; #{opt m.  It should follow the sound it nasalizes}
  $sktnasalization = '~'; #{shift `.  It precedes the sound it nazalizes}
  $sktavagraha = "'"; # changed from'''';
  $sktroot = '§'; #{opt v}
  $sktudatta = '«'; #{opt e space.  It precedes the sound it accents}
  $sktsvarita = '^'; #{opt i space.  It precedes the sound it accents}
  $sktudattaa = '';
  $sktudattai = '';
  $sktudattau = '';
  $sktudattae = '';
  $sktudattao = '';
  $sktudattaaa = '§';
  $sktudattaii = 'ª';
  $sktudattauu = '²';
  $sktudattaai = '';
  $sktudattaau = '®';
  $sktsvaritaa = '	';
  $sktsvaritai = '';
  $sktsvaritau = '';
  $sktsvaritae = '';
  $sktsvaritao = '';
  $sktsvaritaaa = '¥';
  $sktsvaritaii = '«';
  $sktsvaritauu = '³';
  $sktsvaritaai = '¦';
  $sktsvaritaau = '¯';
  $sktk = 'k';
  $sktkh = 'K';
  $sktg = 'g';
  $sktgh = 'G';
  $sktkn = 'N';
  $sktc = 'c';
  $sktch = 'C';
  $sktj = 'j';
  $sktjh = 'J';
  $sktcn = 'Y';
  $sktretrot = 'w';
  $sktretroth = 'W';
  $sktretrod = 'q';
  $sktretrodh = 'Q';
  $sktretron = 'R';
  $sktt = 't';
  $sktth = 'T';
  $sktd = 'd';
  $sktdh = 'D';
  $sktn = 'n';
  $sktp = 'p';
  $sktph = 'P';
  $sktb = 'b';
  $sktbh = 'B';
  $sktm = 'm';
  $skty = 'y';
  $sktr = 'r';
  $sktl = 'l';
  $sktv = 'v';
  $sktsch = 'S';
  $sktsh = 'z';
  $skts = 's';
  $skth = 'h';
#require "./neutralchar.plinc";
# neutralchar.plinc, from TransliterateAll.pp
# perl stub defines constants for certain characters.
# {Neutral characters}
 $return = "\r";
 $newline = "\n";
 $tab = "\t";
 $space = ' ';
 $hyphen = '-';
 $comma = ',';
 $semicolon = ';';
 $colon = ':';
 $period = '.';
 $star = '*';
 $slash = '/';
 $openparen = '(';
 $closeparen = ')';
# ejf added
 $true = 1;
 $false = 0;

#require "./cantapadary.plinc";
# cantapadary.plinc
# from sandhiPrepLists in SandhiPrep.pp
 $cantamax = 27; #const
 @CAntaPadary; # type = $array[1..cantamax] of string[10];
 $CAntaPadary[1] = 'aqac';
 $CAntaPadary[2] = 'Awac';
 $CAntaPadary[3] = 'Alac';
 $CAntaPadary[4] = 'ec';
 $CAntaPadary[5] = 'Ac';
 $CAntaPadary[6] = 'ic';
 $CAntaPadary[7] = 'ilac';
 $CAntaPadary[8] = 'izRuc';
 $CAntaPadary[9] = 'Irac';
 $CAntaPadary[10] = 'ktic';
 $CAntaPadary[11] = 'KizRuc';
 $CAntaPadary[12] = 'Wac';
 $CAntaPadary[13] = 'Rac';
 $CAntaPadary[14] = 'tfc';
 $CAntaPadary[15] = 'daGnac';
 $CAntaPadary[16] = 'dvayasac';
 $CAntaPadary[17] = 'dvyac';
 $CAntaPadary[18] = 'nAwac';
 $CAntaPadary[19] = 'biqac';
 $CAntaPadary[20] = 'birIsac';
 $CAntaPadary[21] = 'mAtrac';
 $CAntaPadary[22] = 'yAc';
 $CAntaPadary[23] = 'vuc';
 $CAntaPadary[24] = 'vfc';
 $CAntaPadary[25] = 'SaNkawac';
 $CAntaPadary[26] = 'SAlac';
 $CAntaPadary[27] = 'zWac';
#require "./pradi.plinc";
# pradi.plinc
# from SandhiGen.pp (routine gana)
 $pradimax = 20; #const
 @Pradi; # type = $array[1..pradimax] of string[5];
 $Pradi[1] = 'pra';
 $Pradi[2] = 'parA';
 $Pradi[3] = 'apa';
 $Pradi[4] = 'sam';
 $Pradi[5] = 'anu';
 $Pradi[6] = 'ava';
 $Pradi[7] = 'nis';
 $Pradi[8] = 'dus';
 $Pradi[9] = 'vi';
 $Pradi[10] = 'A';
 $Pradi[11] = 'ni';
 $Pradi[12] = 'aDi';
 $Pradi[13] = 'api';
 $Pradi[14] = 'ati';
 $Pradi[15] = 'su';
 $Pradi[16] = 'ud';
 $Pradi[17] = 'aBi';
 $Pradi[18] = 'prati';
 $Pradi[19] = 'pari';
 $Pradi[20] = 'upa';
#require "./sets.plinc";
# sets.plinc
# from SandhiGen.pp
# Also, contains routine diff_string used in defining the 'extra' sets
#   defined at bottom of file.
##require "./neutralchar.plinc";
##require "./sanskrit01.plinc";
sub diff_string {
 # assumes two arguments, which are scalar strings.
 # returns a string which contains all characters of the
 # first string which are NOT characters of the second string.
 my ($x,$y)=@_;
 my $ans='';
 my @a = split('',$x);
 my $c;
 foreach(@a) {
  $c = $_;
  if (!($y =~ /$c/)) {
   $ans .= $c;
  }
 }
 return $ans;
}
#PMS load the sets: 

 $ru = 's'; #const

# In Perl, these are just strings, got by concatenating other strings.
 $Avarna = $skta . $sktaa;
 $Ivarna = $skti . $sktii;
 $Uvarna = $sktu . $sktuu;
 $Rvarna = $sktri . $sktrii;
 $Lvarna = $sktlri . $sktlrii;
 $Ku = $sktk . $sktkh . $sktg . $sktgh . $sktkn;
 $Cu = $sktc . $sktch . $sktj . $sktjh . $sktcn;
 $Retrotu = $sktretrot . $sktretroth . $sktretrod . $sktretrodh . $sktretron;
 $Tu = $sktt . $sktth . $sktd . $sktdh . $sktn;
 $Pu = $sktp . $sktph . $sktb . $sktbh . $sktm;
 $An = $Avarna . $Ivarna . $Uvarna;
 $Ak = $Avarna . $Ivarna . $Uvarna . $Rvarna . $Lvarna;
 $Ik = $Ivarna . $Uvarna . $Rvarna . $Lvarna;
 $Uk = $Uvarna . $Rvarna . $Lvarna;
 $Ekn = $skte . $skto;
 $Ec = $skte . $skto . $sktai . $sktau;  #PMS dipthongs
 $Aic = $sktai . $sktau;
 $Ac = $Ak . $Ec;
 $Ic = diff_string($Ac,$Avarna);
 $At = $Ac . $skth . $skty . $sktv . $sktr;
 $Yan = $skty . $sktv . $sktr . $sktl; #PMS semivowels
 $An2 = $Ac . $skth . $Yan; #PMS vowels, $h and semivowels
 $In2 = diff_string($An2,$Avarna);
 $Yam = $skty . $sktv . $sktr . $sktl . $sktcn . $sktm . $sktkn . $sktretron . $sktn; #PMS semivowels and nasals
 $Am = $Ac . $skth . $Yam; #PMS vowels, $semivowels, nasals and h
 $KNam = $sktkn . $sktretron . $sktn;
 $Yacn = $Yam . $sktjh . $sktbh;
 $Jhash = $sktjh . $sktbh . $sktgh . $sktretrodh . $sktdh; #PMS voiced aspirated stops
 $Bhash = $sktbh . $sktgh . $sktretrodh . $sktdh; #PMS voiced aspirated stops other than jh
 $Jasch = $sktj . $sktb . $sktg . $sktretrod . $sktd; #PMS unvoiced unaspirated stops
 $Basch = $sktb . $sktg . $sktretrod . $sktd; #PMS unvoiced unaspirated stops other than j
 $Jhasch = $sktjh . $sktbh . $sktgh . $sktretrodh . $sktdh . $sktj . $sktb . $sktg . $sktretrod . $sktd; #PMS voiced stops
 $Hasch = $skth . $Yam . $Jhasch; #PMS voiced consonants
 $Vasch = diff_string($Hasch,$skth . $skty); #PMS voiced consonants other than h and y
 $Asch = $Ac . $Hasch; #PMS voiced sounds
 $Chav = $sktch . $sktretroth . $sktth . $sktc . $sktretrot . $sktt;
 $Khay = $sktkh . $sktph . $sktch . $sktretroth . $sktth . $sktc . $sktretrot . $sktt . $sktk . $sktp; #PMS unvoiced stops
 $Jhay = $Jhasch . $Khay; #PMS non-nasal stops both voiced and unvoiced
 $Yay = $Yam . $Jhay; #PMS semivowels and stops
 $May = $sktm . $sktkn . $sktretron . $sktn . $Jhay; #PMS stops other than palatal n
 $Cay = $sktc . $sktretrot . $sktt . $sktk . $sktp;
 $Khar = $sktkh . $sktph . $sktch . $sktretroth . $sktth . $sktc . $sktretrot . $sktt . $sktk . $sktp . $sktsch . $sktsh . $skts; #PMS unvoiced sounds
 $Car = $sktc . $sktretrot . $sktt . $sktk . $sktp . $sktsch . $sktsh . $skts;
 $Schar = $sktsch . $sktsh . $skts; #PMS unvoiced sylibants
 $Jhar = $Jhay . $Schar;  #PMS non-nasal stops and unvoiced silibants
 $Yar = $Yam . $Jhay . $Schar; #PMS semivowels, $stops and unvoiced silibants (consonants other than h)
 $Schal = $sktsch . $sktsh . $skts . $skth;
 $Jhal = $Jhay . $Schal; #PMS non-nasal stops and silibants
 $Hal = $skty . $sktv . $sktr . $sktl . $sktcn . $sktm . $sktkn . $sktretron . $sktn . $sktjh . $sktbh . $sktgh . $sktretrodh . $sktdh . $sktj . $sktb . $sktg . $sktretrod . $sktd . $sktkh . $sktph . $sktch . $sktretroth . $sktth . $sktc . $sktretrot . $sktt . $sktk . $sktp . $sktsch . $sktsh . $skts . $skth;
 $Ral =  diff_string($Hal,$skty . $sktv); #PMS consonants other than y and v
 $Val = diff_string($Hal, $skty);  #PMS consonants other than y
 $Al = $Ac . $Hal; #PMS all independent sounds
 $Guna = $skta . $skte . $skto;
 $Vrddhi = $sktaa . $sktai . $sktau;
 $Sounds = $Al . $sktvisarga . $sktanusvara;
 $Linend = $space . $comma . $semicolon . $colon . $period;

#----- ejf set constants
# These are sets that were referenced by inline Pascal 
# set construction operators. In conversion to Perl,
# it was convenient to construct these initialially and
# given then new names.
 $Rvarna_and_Lvarna = $Rvarna . $Lvarna;
 $Jhal_not_ru = diff_string($Jhal,$ru);
 $Hasch_and_skta = $Hasch . $skta;
 $sktr_and_ru = $sktr . $ru;
 $Khar_and_linend = $Khar . $Linend;
 $Ku_and_Pu_and_Schar = $Ku . $Pu . $Schar;
 $Ku_and_Pu = $Ku . $Pu;
 $Tu_and_skts = $Tu . $skts;
 $Cu_and_sktsch = $Cu . $sktsch;
 $Retrotu_sktsh = $Retrotu . $sktsh;
 $Yay_not_Yan = diff_string($Yay,$Yan);
 $sktn_and_sktsh_and_skts = $sktn . $sktsh . $skts;
 $Hal_and_ru = $Hal . $ru;
 $Al_and_Linend = $Al . $Linend;
#require "./Soundary.plinc";
# Soundary.plinc. 
# Global constants related to Soundary
# from SandhiGen.pp
#require "./sanskrit01.plinc";
#PMS load the array Soundary
 $maxyatna = 11; #const
 $maxsthana = 5; #const 
 @Soundary; # type = $array[1..maxsthana, 1..maxyatna] of char;

 # first coord of Soundary
 $ikanthya = 1; #const
 $italavya = 2; #const
 $imurdhanya = 3; #const
 $idantya = 4; #const
 $iosthya = 5; #const
 # second coord of Soundary
 $ihrasva = 1; #const
 $idirgha = 2; #const
 $iguna = 3; #const
 $ivrddhi = 4; #const
 $isparsa1 = 5; #const
 $isparsa2 = 6; #const
 $isparsa3 = 7; #const
 $isparsa4 = 8; #const
 $isparsa5 = 9; #const
 $iantahstha = 10; #const
 $iusmana = 11; #const

 $Soundary[$ikanthya][$ihrasva] = $skta;
 $Soundary[$ikanthya][$idirgha] = $sktaa;
 $Soundary[$ikanthya][$iguna] = $skta;
 $Soundary[$ikanthya][$ivrddhi] = $sktaa;
 $Soundary[$ikanthya][$isparsa1] = $sktk;
 $Soundary[$ikanthya][$isparsa2] = $sktkh;
 $Soundary[$ikanthya][$isparsa3] = $sktg;
 $Soundary[$ikanthya][$isparsa4] = $sktgh;
 $Soundary[$ikanthya][$isparsa5] = $sktkn;
 $Soundary[$ikanthya][$iantahstha] = $skth;
 $Soundary[$ikanthya][$iusmana] = $sktjihvamuliya;

 $Soundary[$italavya][$ihrasva] = $skti;
 $Soundary[$italavya][$idirgha] = $sktii;
 $Soundary[$italavya][$iguna] = $skte;
 $Soundary[$italavya][$ivrddhi] = $sktai;
 $Soundary[$italavya][$isparsa1] = $sktc;
 $Soundary[$italavya][$isparsa2] = $sktch;
 $Soundary[$italavya][$isparsa3] = $sktj;
 $Soundary[$italavya][$isparsa4] = $sktjh;
 $Soundary[$italavya][$isparsa5] = $sktcn;
 $Soundary[$italavya][$iantahstha] = $skty;
 $Soundary[$italavya][$iusmana] = $sktsch;

 $Soundary[$imurdhanya][$ihrasva] = $sktri;
 $Soundary[$imurdhanya][$idirgha] = $sktrii;
 $Soundary[$imurdhanya][$iguna] = $skta;
 $Soundary[$imurdhanya][$ivrddhi] = $sktaa;
 $Soundary[$imurdhanya][$isparsa1] = $sktretrot;
 $Soundary[$imurdhanya][$isparsa2] = $sktretroth;
 $Soundary[$imurdhanya][$isparsa3] = $sktretrod;
 $Soundary[$imurdhanya][$isparsa4] = $sktretrodh;
 $Soundary[$imurdhanya][$isparsa5] = $sktretron;
 $Soundary[$imurdhanya][$iantahstha] = $sktr;
 $Soundary[$imurdhanya][$iusmana] = $sktsh;

 $Soundary[$idantya][$ihrasva] = $sktlri;
 $Soundary[$idantya][$idirgha] = $sktlrii;
 $Soundary[$idantya][$iguna] = $skta;
 $Soundary[$idantya][$ivrddhi] = $sktaa;
 $Soundary[$idantya][$isparsa1] = $sktt;
 $Soundary[$idantya][$isparsa2] = $sktth;
 $Soundary[$idantya][$isparsa3] = $sktd;
 $Soundary[$idantya][$isparsa4] = $sktdh;
 $Soundary[$idantya][$isparsa5] = $sktn;
 $Soundary[$idantya][$iantahstha] = $sktl;
 $Soundary[$idantya][$iusmana] = $skts;

 $Soundary[$iosthya][$ihrasva] = $sktu;
 $Soundary[$iosthya][$idirgha] = $sktuu;
 $Soundary[$iosthya][$iguna] = $skto;
 $Soundary[$iosthya][$ivrddhi] = $sktau;
 $Soundary[$iosthya][$isparsa1] = $sktp;
 $Soundary[$iosthya][$isparsa2] = $sktph;
 $Soundary[$iosthya][$isparsa3] = $sktb;
 $Soundary[$iosthya][$isparsa4] = $sktbh;
 $Soundary[$iosthya][$isparsa5] = $sktm;
 $Soundary[$iosthya][$iantahstha] = $sktv;
 $Soundary[$iosthya][$iusmana] = $sktupadhmaniya;

#----- constants global to sandhi.pl
my $linmax = 1000; #const
my $pratipadmax = 20; #PMS Maximum length assumed for lexical items
#----- informational Pascal declarations
#   $lenrange = 1..linmax;
#   $lenrange0 = 0..linmax;
#   $lenrangeE = -1..linmax;
#   $linetype = $array[$lenrange] of char;
#   $stringrange = 1..255;
#----- variables global to sandhi.pl
my @Linary; # type = $linetype;
my ($Isthana1,$Isthana2,$Iyatna1,$Iyatna2);
my $iapi = 13; #PMS api usually is not an upasarga so check it separately #const
#   $padatype = $string[$pratipadmax];
# pratipadmax defined in sub sandhi in
my $PurvaPada; # type = $padatype;
my $Pada1; # type = $padatype;
my $NxtPada1; # type = $padatype;
my $Pada2; # type = $padatype;

my $Upasarga; # type = $boolean; #PMS for sandhiPrep
my $NoStoh; # type = $boolean; #PMS for sandhiPrep
my $NoKNam; # type = $boolean; #PMS for sandhiPrep
my $Exception; # type = $boolean; #PMS for sandhiPrep
my $Pronoun; # type = $boolean; #PMS for sandhiPrep
my $EkahPurvaParayoh; # type = $boolean; #PMS 
my $Error;
my $IEnd; # type = $lenrange0;
##my $Inextsp; # type = $lenrangeE;
##my $IPrev; # type = $lenrangeE;
##my $Inext; # type = $lenrangeE;
##my $IPrevSpace; # type = $lenrangeE;
my $Index; # type = $lenrangeE;
#my $I; # type = $lenrangeE;
my $Found; # type = $boolean;
my $NoSpace; # type = $boolean;
my $Dhralopa; # type = $boolean;
my $OtherCloseSandhi; # type = $boolean;
my $Pragrhya; # type = $boolean;
my $Uttarapada; # type = $boolean;
my $NxtUttarapada; # type = $boolean;

my $FldChr;
# globals set in sandhioptions routine
my $Despace; # type = $boolean; #PMS Despace set in sandhioptions
my $External; # type = $boolean; #PMS Sandhi Options
my $Compound; # type = $boolean; #PMS Sandhi Options
my $Chandas; # type = $boolean; #PMS Sandhi Options
my $CloseUpasargaSandhi; # type = $boolean; #PMS Sandhi Options
my $TukPadantat; # type = $boolean; #PMS Sandhi Options
my $ScharSchari; # type = $boolean; #PMS Sandhi Options
my $XkXpKupvoh; # type = $boolean; #PMS Sandhi Options
my $ChAti; # type = $boolean; #PMS Sandhi Options
my $ParaSavarna; # type = $boolean; #PMS Sandhi Options
my $Anunasika; # type = $boolean; #PMS Sandhi Options

my $Padbound; # type = $char;

# ejf constants
my $dbg = $false; #$true; #$false;
#----------------- ejf helper routines
sub set_memberP {
    # boolean function implements the Pascal $c in $set dialect.
    # $c is a char ,implemented as a string of length 1
    # $set is a 'set of char', implemented as a string.
    my ($c,$set)=@_;
    ($set =~ /$c/) ? $true : $false;
}
sub arr_str { 
    my @a = @_;
    my $s = join('',@a);
    my $s1 = str_trim($s);
    return $s1;
}
sub str_trim {
    # trim whitespace from start and end of s1.
    my ($s1) = @_;
    $s1 =~ s/^\s+//;
    $s1 =~ s/\s+$//;
    return $s1;
}
sub chk_point {
    my ($s) = @_;
    if($dbg) {print "($s): " . (arr_str(@Linary)) . "\n";}
}
#-----------------sandhioptions routine from SandhiGen.pp
sub sandhioptions {
# sets $Error. 0 = ok. 4 = error with $compound_ans,
#     
 my ($compound_ans,$vedic_ans,$closeSandhi_ans,$despace_ans) = @_;
 # $compound_ans should be 'C' for sandhi at compounds, 'E' for External 
 # $vedic_ans should be 'Y' or 'N'.
 # $closeSandhi_ans should be N,Y,S
 # $despace_ans should be Y,N.  default is 
 my $Answer;
 my $Error = 0;
 my $Yes;
 my $No;
 $Yes = 'Yy';
 $No = 'Nn';
 $Answer = '';
 # initialize external flags to false.
 $Despace = $false;
 $External = $false;
 $Compound = $false;
 $Chandas = $false;
 $CloseUpasargaSandhi = $false;
 $TukPadantat = $false; #PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
 $ScharSchari = $false; #PMS 8.3.36.  vA Sari
 $XkXpKupvoh = $false; #PMS 8.3.37.  kupvoH XkXpau ca.
 $ChAti = $false; #PMS 8.4.63.  SaS cho 'wi. (jhayaH 62, anyatarasyAm 62)
 $ParaSavarna = $false; #PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
 $Anunasika = $false; #PMS 8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)
# hideall();
# showtext();
# Process $compound_ans
# print "Do you want to do sandhi within compounds (at hyphens)\n";
# print "or external (at spaces)?\n";
# print "     C/c for compound\n";
# print "     E/e for external\n";
# print "     Any other character to quit: ";
# readln($Answer);
 $Answer = uc($compound_ans);
 if ( $Answer eq '' ) {
  $Answer = '?';
 }
 if  ($Answer eq 'C') {
  $Compound = $true;
  $Padbound = $hyphen;
  }
 elsif ($Answer eq 'E') {
  $External = $true;
  $Padbound = $space;
  }
 else {
  #PMS neither so quit
  $Error = 4;
  return($Error); # REPLACE exit($sandhioptions);
  }
#--process $vedic_ans
# print "Is this a Vedic text ($chandas)?\n";
# print "Default no: ";
# readln($Answer);
 $Answer = uc($vedic_ans);
 if ( $Answer eq '' ) {
  $Answer = '?';
 }
 if  ($Answer eq 'Y') {
  $Chandas = $true;
 }
 if ($dbg) {
     print "Compound = $Compound, External = $External, Padbound = $Padbound\n";
     print "Chandas = $Chandas\n";
 }
#-- closeSandhi_ans
# print "Do you want to exercise close sandhi options?\n";
# print ""N" or "n" to decline\n";
# print ""Y" or "y" to accept\n";
# print ""S" or "s" to follow standard editorial practice\n";
# print "Any other character to select options individually: ";
# readln($Answer);
 $Answer = $closeSandhi_ans;
 if ( $Answer eq '' ) {
  $Answer = '?';
 }
 if  ($Answer eq "Y") {
  $TukPadantat = $true; #PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
  $ScharSchari = $true; #PMS 8.3.36.  vA Sari
  $XkXpKupvoh = $true; #PMS 8.3.37.  kupvoH XkXpau ca.
  $ChAti = $true; #PMS 8.4.63.  SaS cho 'Ti. (jhayaH 62, anyatarasyAm 62)
  $ParaSavarna = $true; #PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
  $Anunasika = $true; #PMS 8.4.45.  yaro 'nunAsike 'nunAsiko vA. ($padAnta 42)
  }elsif ($Answer eq "N") {
  #PMS No close sandhi, $logicals remain $false
# } elsif  ($Answer eq "S") { # ejf change
  #PMS Standard editorial practice
#  print " Current version does not allow to select options individually\n";
#  print " Assuming 'Decline'\n";

 } elsif ($Answer eq "S") { # not executed. ejf change.
#-------------
     if ( $Compound ) {
	 #PMS Close sandhi within compounds
	 $TukPadantat = $true; #PMS 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
	 $ScharSchari = $true; #PMS 8.3.36.  vA Sari
	 #PMS technically, 8.3.37 should also apply but it is never seen
	 $ChAti = $true; #PMS 8.4.63.  SaS cho 'wi. (jhayaH 62, anyatarasyAm 62)
	 $ParaSavarna = $true; #PMS 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
	 $Anunasika = $true; #PMS 8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)
	 #PMS display standard editorial practice for compound sandhi
	 if ($dbg) {
	     print "The optional sandhi in the following sutras will apply:\n";
	     print "TukPadantat = $TukPadantat, ScharSchari = $ScharSchari\n";
	     print "ChAti = $ChAti, ParaSavarna = $ParaSavarna, Anunasika = $Anunasika\n";
	 }
	 if ( $TukPadantat and $false ) {
	     print "     6.1.76.  padAntAdvA ($dIrghAt 75, che 73, tuk 71).\n";
	 }
	 if ( $ScharSchari and $false ) {
	     print "     8.3.36.  vA Sari.\n";
	 }
	 if ( $XkXpKupvoh and $false ) {
	     print "     8.3.37.  kupvoH XkXpau ca.\n";
	 }
	 if ( $ChAti and $false ) {
	     print "     8.4.63.  SaS cho 'wi. (jhayaH 62, anyatarasyAm 62 ) . \n";
	 }
	 if ( $ParaSavarna and $false ) {
	     print "     8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
	 }
	 if ( $Anunasika and $false ) {
	     print "     8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)\n";
	 }
     } #PMS Close sandhi within compounds
     else {
	 #PMS External: 8.4.63 and 8.4.45
	 $ChAti = $true; #PMS 8.4.63.  SaS cho 'Ti. (jhayaH 62, anyatarasyAm 62)
	 $Anunasika = $true; #PMS 8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)
	 if ($dbg) {
	     print "The optional sandhi in the following sutras will apply:\n";
	     print "     8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)\n";
	     print "     8.4.63.  SaS cho 'wi. (jhayaH 62, anyatarasyAm 62 ) . \n";
	     #PMS disabled Close sandhi between upasargas and their following verb forms
	     #PMS CloseUpasargaSandhi = $true;
	     #PMS print "Close sandhi will be observed between upasargas and their following verb forms\n";
	     #PMS print "After the upasarga 'sam',\n";
	     #PMS print "     8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
	 }
     } #PMS External.  End of standard editorial practice
 }else {
  #PMS peruse options
  print "Choose sandhi options ('Y' or 'y' to accept):\n";
  print "6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71).\n";
  print "     Pada final long vowel augmented with c before ch ? ";
#  readln($Answer);
  if ( $Answer eq '' ) {
   $Answer = '?';
  }
  if ($Answer eq "Y") {
   $TukPadantat = $true;
  }
  print "8.3.36.  vA Sari.\n";
  print "     S, z or s before palatal, retroflex or dental stop respectively? ";
#  readln($Answer);
  if ( $Answer eq '' ) {
   $Answer = '?';
  }
  if ($Answer eq "Y") {
   $ScharSchari = $true;
  }
  print "8.3.37.  kupvoH XkXpau ca.\n";
  print "      jihvamuliya, upadhmaniya before gutteral or labial stop respectively? ";
#  readln($Answer);
  if ( $Answer eq '' ) {
   $Answer = '?';
  }
  if ($Answer eq "Y") {
   $XkXpKupvoh = $true;
  }
  print "8.4.63.  SaS cho 'wi . (jhayaH 62, anyatarasyAm 62\n";
  print "    ch after stops ? ";
#  readln($Answer);
  if ( $Answer eq '' ) {
   $Answer = '?';
  }
  if ($Answer eq "Y") {
   $ChAti = $true;
  }
  print "8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
  print "     AnusvAra  stop homogenous with following stop? ";
#  readln($Answer);
  if ( $Answer eq '' ) {
   $Answer = '?';
  }
  if ($Answer eq "Y") {
   $ParaSavarna = $true;
  }
  print "8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)\n";
  print "(At present the program does not handle nasalized semivowels)\n";
  print "(which, $though rarely found in editions, go with this sandhi.)\n";
  print "     Stops  corresponding nasal before a nasal? ";
#  readln($Answer);
  if ( $Answer eq '' ) {
   $Answer = '?';
  }
  if ($Answer eq "Y") {
   $Anunasika = $true;
  }
  if ( (not $ParaSavarna) or (not $Anunasika) ) {
   print " Do you want to observe close sandhi after upasargas ? ";
#   readln($Answer);
   if ( $Answer eq '' ) {
    $Answer = '?';
   }
   if ($Answer eq "Y") {
    $CloseUpasargaSandhi = $true;
   }
  }
  print "The optional sandhi in the following sutras will apply:\n";
  if ( $TukPadantat ) {
   print "     6.1.76.  padAntAdvA ($dIrghAt 75, che 73, tuk 71).\n";
  }
  if ( $ScharSchari ) {
   print "     8.3.36.  vA Sari.\n";
  }
  if ( $XkXpKupvoh ) {
   print "     8.3.37.  kupvoH XkXpau ca.\n";
  }
  if ( $ChAti ) {
   print "     8.4.63.  SaS cho 'wi. (jhayaH 62, anyatarasyAm 62 ) . \n";
  }
  if ( $ParaSavarna ) {
   print "     8.4.59.  vA padAntasya ($anusvArasya yayi parasavarRaH 58).\n";
  }
  if ( $Anunasika ) {
   print "     8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)\n";
  }
  if ( $CloseUpasargaSandhi ) {
   #PMS close upasarga sandhi
   print "Close sandhi will be observed after upasargas\n";
   if ( not $ParaSavarna ) {
    print "After the upasarga 'sam',\n";
    print "     8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).\n";
    }
   if ( not $Anunasika ) {
    print "After the upasarga 'ud',\n";
    print "     8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)\n";
    }
   } #PMS close upasarga sandhi
  } #PMS peruse options
#PMS Choose spacing options
 if ( $Compound ) {
#  print "Hyphens will be deleted between compound elements.\n";
 }elsif ( $External ) {
  #PMS spaceoptions
#  print "Spaces will be deleted where a single vowel replaces final and initial vowels.\n";
#  print "Do you wish to eliminate spaces between prefixes and verbs\n";
#  print "and between final consonants and a following sound?\n";
#  print "Y/y (yes) to delete spaces, any other character to keep.";
#  readln($Answer);
     $Answer = $despace_ans;
#     $Answer = 'Y'; #force despacing
  if ( $Answer eq '' ) {
   $Answer = '?';
  }
  if ($Answer eq "Y") {
   $Despace = $true;
  }
 } #PMS spaceoptions
 return ($Error);
} #PMS sandhioptions

#-----------------subroutines from ChararayRoutines.pp
# In Pascal, these are always called with the array Linary as a
# variable parameter.  This causes two difficulties in Perl,
#  related to how Perl handles arguments passed to procedures.
#  1. When the procedure has multiple arguments, and Linary is not
#     the last one, special coding is required to pull out the arguments
#     after the array.
#  2. Several of these array routines modify Linary. But Perl copies
#     the array before passing it, so the caller routine does not
#     see the modifications to Linary.
# I solve these technical problems by removing Linary from the argument
#     list.  Thus, the routines are acting on the global array variable
#     @Linary, which is what is desired. I also change the coding of the
#     routines to use Linary rather than Charary.
#     
sub lengthary {
#{no arguments}
#{returns an integer value in $the range 0..linmax = $the position of the last character which is not a space in $a character array}
#{if the array is all space characters it returns zero}
     my $I;
     for ($I = $linmax; 1<=$I;$I--) {
	 if ( $Linary[$I] ne ' ' ) {
	     return $I;
	 }
     }
     return 0;
 }

sub nxtposary {
#function nxtposary ($chtr: char; fldch: char; $istart: lenrange): lenrangeE;
#{passed a character, $a character array[1..linmax], $an integer 1..linmax}
#{returns the position of the first occurrence of the character in $the array beginning with $Linary[$Index]}
#{returns zero if the character is not found; returns -1 if $istart is out of bounds}
    my ($chtr,$fldch,$istart) = @_;
    my $I; # type = $integer;
    my $IEnd; # type = $lenrange0;
    if ( ($istart < 1) or ($istart > $linmax) ) {
	return(-1);
    }
    $IEnd = lengthary();
    for ($I = $istart; $I<=$IEnd;$I++){
	if ( ($Linary[$I] eq $chtr) or ($Linary[$I] eq $fldch) ) {
	    return($I);
	}
    }
    return(0); 
}

sub lastposary {
#function lastposary ($chtr: char; $istart: lenrange): lenrangeE;
#{passed a character, $a character array[1..linmax], $an integer 1..linmax}
#{returns the position of the first previous occurrence of the character found searching backwards from $Linary[$Index]}
#{returns zero if the character is not found; returns -1 if $istart is greater than the size of the array}
    my ($chtr,$istart) = @_;
    my $I;
    if ( ($istart < 1) or ($istart > $linmax) ) {
	return(-1);
    }
    for ($I = $istart; 1<=$I; $I--) {
	if ( $Linary[$I] eq $chtr ) {
	    return($I);
	}
    }
    return(0);
}

sub insertary {
# ($chtr: char;  $index: lenrange);
#{passed an actual character value,and an actual value $index of an integer in $the range 1..linmax}
#{returns the array with the character inserted at position $index and the rest of the array moved over}
#{If $index indexes a position after the last non-space, the character is inserted just after the last non-space character}
#{It is an error if there is no space in $Linary[$linmax]}
# ejf: The global variable $NoSpace is also adjusted, as well as @Linary
    my ($chtr,$index) = @_;
    my $I; # type = $integer;
    my $Ipt; # type = $lenrange;
    my $IEnd; # type = $lenrange0;
    $NoSpace = $false;
    $IEnd = lengthary();
    if ( $IEnd eq $linmax ) {
	$NoSpace = $true;
	return;
    }
    $Ipt = $index;
    if ( $Ipt < 1 ) {
	$Ipt = 1;
    }
    if ( $Ipt > $IEnd ) {
	$Ipt = $IEnd + 1;
    }
    for ($I = $IEnd; $Ipt <= $I; $I--) {
	$Linary[$I + 1] = $Linary[$I];
    }
    $Linary[$Ipt] = $chtr;
#    print "insertary: $chtr,$index " . (arr_str(@arr)) . " => " .  (arr_str(@Linary)) . "\n";

}


sub deletary {
# ($index: lenrange);
#{modifies @Linary with the character at position $index deleted and the rest of the array moved in}
#{If $index indexes a position after the last non-space, no character is deleted}
    my ($index) = @_;
    my $I; # type = $integer;
    my $IEnd; # type = $lenrange0;
    $IEnd = lengthary();
    my @arr = @Linary;
    if ( ($index >= 1) and ($index <= $IEnd) ) {
	for ($I = $index; $I < $IEnd; $I++) { 
	    $Linary[$I] = $Linary[$I + 1];
	}
	$Linary[$IEnd] = ' ';
    }
#    print "deletary: $index " . (arr_str(@arr)) . " => " .  (arr_str(@Linary)) . "\n";
}
sub substrary {
#{integer values $index1 and $index2}
#{returns a string consisting of ($index1-index2)+1 characters beginning at $index1, a substring of the character array,@Linary}
# may return an empty string.
    my ($index1,$index2) = @_;
    my $I;
    my $IEnd;
    my $Tempstr; # type = $string[255];
    $Tempstr = '';
    $IEnd = lengthary();
    # ejf added some other condition checking 
    if ( ($index1 < 1) or ($index1 > $index2) or ($index2 > $IEnd) ) {
	return($Tempstr);
    }
    # In Perl, this condition not needed, but, leave it for now.
    if ( (($index2 - $index1) + 1) <= $pratipadmax ) {
	for ($I = $index1; $I <= $index2; $I++) {
	    $Tempstr = $Tempstr . $Linary[$I]; # concat
	}
    }
    return($Tempstr);
}


#
#-----------------subroutines from sandhi
#--- in Pascal, these were defined within sandhi routine.
sub identify {
    my $aksara = shift; # a string with one character
#{Searches the  sound array Soundary for the character passed in $aksara.}
#{Returns its position in the index variables Isthana and Iyatna.}
#{If not found Isthana and $Iyatna =0.}
    my ($I1,$I2);
    for ($I1=1;$I1 <= $maxsthana; $I1++) {
	for ($I2=1;$I2 <=  $maxyatna; $I2++) {
	    if ( $aksara eq $Soundary[$I1][$I2] ) {
		if ($dbg) {print "identify: $aksara, $I1, $I2\n";}
		return ($I1,$I2);
	    }
	}
    }
    if ($dbg) {print "identify not found: '$aksara'\n";}
    return (0,0);
}

sub rlvarnayormithahsavarnyam {
    #{1.1.9 vt. fkAra kArayoH savarRavidhiH}

  if ( (set_memberP($Linary[$Index - 1],$Rvarna_and_Lvarna)) and (set_memberP($Linary[$Index + 1],$Rvarna_and_Lvarna)) ) {
   $Linary[$Index - 1] = $sktri;
   $Linary[$Index + 1] = $sktri;
   $Isthana1 = $imurdhanya;
   $Isthana2 = $imurdhanya;
   }
   chk_point('rlvarnayormithahsavarnyam');
} #{rlvarnayormithahsavarnyam}

sub akahsavarnedirghah {
   ; #{6.1.101.  akaH savafRe dIrghaH}
  $Linary[$Index - 1] = $Soundary[$Isthana1][$idirgha];
  deletary($Index + 1); #{6.1.84.  ekaH pUrvaparayoH}
  $EkahPurvaParayoh = $true;
   chk_point('akahsavarnedirghah');
} #{akahsavarnedirghah}

sub vrddhireci {
   #{6.1.88.  vfddhir eci}
  $Linary[$Index - 1] = $Soundary[$Isthana2][$ivrddhi];
  deletary($Index + 1); #{6.1.84.  ekaH pUrvaparayoH}
  $EkahPurvaParayoh = $true;
   chk_point('vrddhireci');
} #{vrddhireci}

sub adgunah {
    #{6..1.87.  Ad guRaH}
    $Linary[$Index - 1] = $Soundary[$Isthana2][$iguna];
#begin case:   case $Isthana2 of
    if (($Isthana2 eq $italavya) or ($Isthana2 eq $iosthya)) {
	deletary($Index + 1); #{6.1.84.  ekaH pUrvaparayoH}
    }elsif ($Isthana2 eq $imurdhanya) { #   imurdhanya: 
	$Linary[$Index + 1] = $sktr; #{1.1.51.  uraR raparaH}
    }elsif ($Isthana2 eq $idantya) { #   idantya: 
	$Linary[$Index + 1] = $sktl;
    }
    $EkahPurvaParayoh = $true;
   chk_point('adgunah');
} #{adgunah}


sub ikoyanaci {
   #{6.1.77.  iko yaR aci}
  $Linary[$Index - 1] = $Soundary[$Isthana1][$iantahstha];
   chk_point('ikoyanaci');
} #{ikoyanaci}

sub enahpadantadati {
   #{6.1.109.  eNaH padAntAd ati}
  $Linary[$Index + 1] = $sktavagraha;
  chk_point('enahpadantadati');
} #{enahpadantadati}

sub ecoyavayavah {
   #{6.1.109.  eNaH padAntAd ati}
#begin case:   case $Linary[$Index - 1] of
    if ($Linary[$Index - 1] eq $skte) { 
	$Linary[$Index - 1] = $skta;
	insertary($skty, $Index);
    }elsif ($Linary[$Index - 1] eq $skto) {
	$Linary[$Index - 1] = $skta;
	insertary($sktv, $Index);
    }elsif ($Linary[$Index - 1] eq $sktai) {
	$Linary[$Index - 1] = $sktaa;
	insertary($skty, $Index);
    }elsif ($Linary[$Index - 1] eq $sktau) {
	$Linary[$Index - 1] = $sktaa;
	insertary($sktv, $Index);
    }
    if ( $NoSpace ) {
	$Error = 2;
	return; # REPLACE exit($sandhi);
    }
    $Index = $Index + 1;
    chk_point('ecoyavayavah');
} #{ecoyavayavah}

sub acsandhi {
    rlvarnayormithahsavarnyam();
    my $cprev=$Linary[$Index - 1];
    my $cnext=$Linary[$Index + 1];
    if ( set_memberP($Linary[$Index - 1],$Ak) ) {
	if ( (set_memberP($Linary[$Index + 1],$Ak)) and ($Isthana1 eq $Isthana2) ) {
#	    print "$cprev in $Ak, and $cnext in $Ak, and $Isthana1 = $Isthana2\n";
	    akahsavarnedirghah(); #{6.1.101.  akaH savafRe dIrghaH}
	}elsif ( set_memberP($Linary[$Index - 1],$Avarna) ) {
	    #PMS: and $Linary[$Index+1] not in $Avarna
	    if ( set_memberP($Linary[$Index + 1],$Ec) ) {
		vrddhireci();  #PMS: 6.1.88  vfddhir eci
	    }else {
	    #PMS: Linary[$Index+1] in $Ik
		adgunah(); #PMS: 6.1.87  Ad guRaH
	    }
	}else {
	    #PMS: Linary[$Index-1] in $Ik and not savarna with $Linary[$Index+1]
	    ikoyanaci(); #PMS: 6.1.77.  iko yaR aci
	}
    }else {
	#PMS: Linary[$Index-1] in $Ec
	if ( (set_memberP($Linary[$Index - 1],$Ekn)) and ($Linary[$Index + 1] eq $skta) ) {
	    enahpadantadati(); #PMS: 6.1.109.  eNaH padAntAd ati
	}else {
	    #PMS: set_memberP($Linary[$Index-1],$Ec) and set_memberP($Linary[$Index+1],$Ic)
	    ecoyavayavah(); #PMS: 6.1.78.  eco 'yavAyAvaH
	}
    }
    chk_point('acsandhi');
} #{acsandhi}


sub visargaprep {
    my $L = length($Pada1);
    if ( ($Pada1 eq 'ahaH') or ($Pada1 eq 'svaH') or ($Pada1 eq 'antaH') or ($Pada1 eq 'prAtaH') or ($Pada1 eq 'punaH') or ($Pada1 eq 'mAtaH') or ($Pada1 eq 'kOsalyAmAtaH') or ($Pada1 eq 'sanutaH') or ($Pada1 eq 'catuH') or ($Pada1 eq 'prAduH') ) {
	$Linary[$Index - 1] = $sktr;
	substr($Pada1,$L-1,$L) = $sktr;
    } else {
	$Linary[$Index - 1] = $skts;
	if ( $Pada1 ne '' ) {
	    substr($Pada1,$L-1,$L) = $skts;
	}
    }
    chk_point('visargaprep');
}


sub checa {
    #PMS: 6.1.73.  che ca ($tuk 71)
    if ($false) { # debug
	print "chk checa: Index = $Index, c+1 = " . $Linary[$Index + 1] . "\n";
	print "Iyatna1 = $Iyatna1, ihrasva = $ihrasva, NoSpace = $NoSpace\n";
	
    }
    if ($false) {
	my $dbg1 = $dbg;
	$dbg = $true;
	chk_point('checa (before)');
    }
    if ( ($Linary[$Index + 1] eq $sktch) and ($Iyatna1 eq $ihrasva) ) {
	insertary($sktt, $Index);
	if ( $NoSpace ) {
	    $Error = 2;
	    return; # REPLACE exit($sandhi);
	}
	$Index = $Index + 1;
    }
    if ($false) {
	chk_point('checa (after)');
	$dbg = $dbg1;
    }
    chk_point('checa');
} #PMS: checa


sub anmanosca {
    #PMS: 6.1.74.  ANmANoSca ($che 73, $tuk 71)
    #PMS: you'll have to add the condition that these are AN and mAN when that info is available
    if ( ($Linary[$Index + 1] eq $sktch) and (($Pada1 eq 'A') or ($Pada1 eq 'mA')) ) {
	insertary($sktt, $Index);
	if ( $NoSpace ) {
	    $Error = 2;
	    return; # REPLACE exit($sandhi);
	}
	$Index = $Index + 1;
    }
    chk_point('anmanosca');
} #PMS: anmanosca

sub padantadva {
    #PMS: 6.1.76.  padAntAdvA ($dIrghAt 75, $che 73, $tuk 71)
    ($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]); #PMS: don't want to do it if anmanosca just applied
    if ( ($Linary[$Index + 1] eq $sktch) and ($Iyatna1 eq $idirgha) ) {
	insertary($sktt, $Index);
	if ( $NoSpace ) {
	    $Error = 2;
	    return; # REPLACE exit($sandhi);
	}
	$Index = $Index + 1;
    }
    chk_point('padantadva');
} #PMS: padantadva

sub etattadohsulopo {
    #PMS: 6.1.132.  etattadoH sulopo 'kor anaYsamAse hali
    if ( (($Pada1 eq 'sas') or ($Pada1 eq 'ezas')) and (set_memberP($Linary[$Index + 1],$Hal)) ) {
	deletary($Index - 1);
	$Index = $Index - 1;
    }
    chk_point('etattadohsulopo');
} #PMS: etattadohsulopo

sub jhalamjasonte {
    #PMS: 8.2.39.  jhalAM jaSo 'nte
    ($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
    if ($false) { #debug
	print "chk: jhalamjasonte\n";
	print "'" . $Linary[$Index - 1] . " => $Isthana1,$Iyatna1\n";
	print "Jhal_not_ru = $Jhal_not_ru\n";
	print "isparsa3 = $isparsa3\n";
	my $dbg1 = $dbg;
	$dbg = $true;
	chk_point('jhalamjasonte: before');
    }
    if ( set_memberP($Linary[$Index - 1],$Jhal_not_ru) ) {
	#PMS: because $ru =skts; I could choose another character
	$Linary[$Index - 1] = $Soundary[$Isthana1][$isparsa3];
    } #PMS: jhalamjasonte
    if ($false) {
	chk_point('jhalamjasonte: after');
	$dbg =$dbg1;
    }
    chk_point('jhalamjasonte');
}

sub sasajusoruh {
    #PMS: 8.2.66.  sasajuzo ruH
    #PMS: exception to 8.2.39 so must apply before it
    if ( $Index > 5 ) {
	if (substrary($Index - 5, $Index - 1) eq 'sajuz') {
	    $Linary[$Index - 1] = $ru;
	}
    }
    if ( $Linary[$Index - 1] eq $skts ) {
	$Linary[$Index - 1] = $ru;
    }
    chk_point('sasajusoruh');
} #PMS: sasajusoruh

sub ahan {
    #PMS: 8.2.68.  ahan
    if ( $Compound ) {
	if ($Pada1 eq 'ahan') {
	    if ( ($Pada2 eq 'rUpa') or ($Pada2 eq 'rAtri') or ($Pada2 eq 'rAtra') or ($Pada2 eq 'rAtre') or ($Pada2 eq 'rAtrARAm') or ($Pada2 eq 'raTantara') ) {
		$Linary[$Index - 1] = $ru #PMS: vArttika, $but had to add rAtra 21045, $rAtre 24028, $rAtrARAm 33137
#PMS: if ahan is termed pada and Pada2 in $Sup, $so that $Linary[$Index+1]=sktbh or $skts, $ditto
		}else {
		    $Linary[$Index - 1] = $sktr; #PMS: 8.2.69.  ro 'supi
		}
	}
    }
    chk_point('ahan');
} #PMS: ahan

sub amnarudharavar {
    #PMS: 8.2.70.  amnarUdharavarityubhayathA chandasi
    if ( $chandas ) {
	if ( ($Pada1 eq 'amnas') or ($Pada1 eq 'UDas') or ($Pada1 eq 'avas') ) {
	    $Linary[$index - 1] = $sktr; #PMS: actually you get it both ways in $chandas, $ru too
	}
    }
    chk_point('amnarudharavar');
}

sub atororhasica {
    #PMS: 6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca
    if ( $Index > 2 ) {
	if ( ($Linary[$Index - 2] eq $skta) and ($Linary[$Index - 1] eq $ru) ) {
	    if (set_memberP($Linary[$Index + 1],$Hasch_and_skta)) {
		$Linary[$Index - 2] = $skto; #PMS: Linary[$Index-1=sktu; adguna
		deletary($Index - 1);
		$Index = $Index - 1;
	    }
	}
    }
    chk_point('atororhasica');
} #PMS: atororhasica

sub naschavyaprasan {
    #PMS: 8.3.7.  naS chavy apraSAn
    if ( ($Linary[$Index - 1] eq $sktn) and (set_memberP($Linary[$Index + 1],$Chav)) and ($Pada1 ne 'praSAn') ) {
	$Linary[$Index - 1] = $ru;
	insertary($sktanusvara, $Index - 1); #PMS: 8.3.4.  anunAsikAt paro 'nusvAraH
	if ( $NoSpace ) {
	    $Error = 2;
	    return; # REPLACE exit($sandhi);
	}
	$Index = $Index + 1;
    }
    chk_point('naschavyaprasan');
} #PMS: naschavyaprasan

sub rori {
    # ($var Dhralopa: boolean); This variable assumed global 
    #PMS: 8.3.14.  ro ri
    $Dhralopa = $false;
    if ( (set_memberP($Linary[$Index - 1],$sktr_and_ru)) and ($Linary[$Index + 1] eq $sktr) ) {
	deletary($Index - 1);
	$Index = $Index - 1;
	$Dhralopa = $true;
    }
    chk_point('rori');
} #PMS: rori

sub dhralope {
    #PMS: 6.3.111.  qhralope pUrvasya dIrgho 'RaH
    if ( $Dhralopa ) {
	($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
	if ( (set_memberP($Linary[$Index - 1],$An)) and ($Iyatna1 eq $ihrasva) ) {
	    $Linary[$Index - 1] = $Soundary[$Isthana1][$idirgha];
	}
    }
    chk_point('dhralope');
} #PMS: dhralope

sub bhobhago {
    #PMS: 8.3.17.  bhobhagoaghoapUrvasya yo 'Si
    if ($false) {
	print "bhobhago: Index = $Index, Asch = $Asch, Pada1 = $Pada1, Avarna = $Avarna, ru = $ru\n";
	my ($c,$c1);
	$c = $Linary[$Index + 1];
	print "next char = '$c'\n";
	$c = $Linary[$Index - 1];
	$c1 = $Linary[$Index - 2];
	print "prev two chars = '$c1', '$c'\n";
    }
    if ( (set_memberP($Linary[$Index + 1],$Asch)) and ($Index > 2) ) {
	if ( ($Pada1 eq 'bhos') or ($Pada1 eq 'bhagos') or ($Pada1 eq 'aghos') or ((set_memberP($Linary[$Index - 2],$Avarna)) and ($Linary[$Index - 1] eq $ru)) ) {
	    $Linary[$Index - 1] = $skty;
	}
    }
    chk_point('bhobhago');
} #PMS: bhobhago

sub kharavasanayor {
    #PMS: 8.3.15.  kharavasAnayor visarjanIyaH
    if ( set_memberP($Linary[$Index - 1],$sktr_and_ru) ) {
	if ( set_memberP($Linary[$Index + 1],$Khar_and_linend) ) {
	    $Linary[$Index - 1] = $sktvisarga;
	}else {
	    $Linary[$Index - 1] = $sktr;
	}
    }
    chk_point('kharavasanayor');
} #PMS: kharavasanayor

sub lopahsakalyasya {
    #PMS: 8.3.19.  lopaH SAkalyasya
    if ( (set_memberP($Linary[$Index + 1],$Asch)) and ($Index > 2) ) {
	if ( (set_memberP($Linary[$Index - 2],$Avarna)) and ($Linary[$Index - 1] eq $skty) ) {
	    deletary($Index - 1);
	    $Index = $Index - 1;
	}
    }
    chk_point('lopahsakalyasya');
} #PMS: lopahsakalyasya

sub otogargyasya {
    #PMS: 8.3.20.  oto gArgyasya
    if ( set_memberP($Linary[$Index + 1],$Asch) ) {
	if ( (($Pada1 eq 'bhos') or ($Pada1 eq 'bhagos') or ($Pada1 eq 'aghos')) ) {
	    deletary($Index - 1);
	    $Index = $Index - 1;
	}
    }
    chk_point('otogargyasya');
} #PMS: oto gargyasya

sub monusvarah {
    #PMS: 8.3.23.  mo 'nusvAraH
    if ( ($Linary[$Index - 1] eq $sktm) and (set_memberP($Linary[$Index + 1],$Hal)) ) {
	$Linary[$Index - 1] = $sktanusvara;
    }
    chk_point('monusvarah');
} #PMS: monusvarah

sub namohrasvad {
    #PMS: 8.3.32.  Namo hrasvAd aci NamuR nityam
    my $Sthana; # type = $sthanatype;
    my $Yatna; # type = $yatnatype;
    if ( ($Index > 2) ) {
	($Sthana,$Yatna) = identify($Linary[$Index - 2]);
	if ( ($Yatna eq $ihrasva) and (set_memberP($Linary[$Index - 1],$KNam)) and (set_memberP($Linary[$Index + 1],$Ac)) ) {
	    insertary($Soundary[$Isthana1][$isparsa5], $Index);
	    if ( $NoSpace ) {
		$Error = 2;
		return; # REPLACE exit($sandhi);
	    }
	    $Index = $Index + 1;
	}
    }
    chk_point('namohrasvad');
} #PMS: namohrasvad

sub visarjaniyasyasah {
    #PMS: 8.3.34.  visarjanIyasya saH
    my $Apavada; # type = $boolean;
    if ( ($Linary[$Index - 1] eq $sktvisarga) and (set_memberP($Linary[$Index + 1],$Khar)) ) {
	$Apavada = $false;
	if ( ($Index + 2) < $linmax ) {
	    if ( set_memberP($Linary[$Index + 2],$Schar) ) {
		$Apavada = $true; #PMS: 8.3.35.  Sarpare visarjanIyaH.
	    }
	}
	if ( set_memberP($Linary[$Index + 1],$Ku_and_Pu_and_Schar) ) {
	    $Apavada = $true; #PMS: 8.3.36.  vA Sari.  8.3.37.  kupvoH XkXpau ca.
	}
	if ( not ($Apavada) ) {
	    $Linary[$Index - 1] = $skts;
	}
    }
    chk_point('visarjaniyasyasah');
} #PMS: visarjaniyasyasah

sub vasari {
    #PMS: 8.3.36.  vA Sari
    if ( ($Linary[$Index - 1] eq $sktvisarga) and (set_memberP($Linary[$Index + 1],$Schar)) ) {
	$Linary[$Index - 1] = $skts;
    }
    chk_point('vasari');
} #PMS: vasari

sub kupvohXkXpau {
    #PMS: 8.3.37.  kupvoH XkXpau ca ($khari 15).
    #PMS: 8.3.41, 8.3.45 and 8.3.46 are apavAdas of this so must precede it.
    my $Apavada; # type = $boolean;
    #PMS: by 8.3.15, $kharavasAnayorvisarjanIyaH, $visarga occurs before avasAna too.  but Xk and Xp don't.
    if ( ($Linary[$Index - 1] eq $sktvisarga) and (set_memberP($Linary[$Index + 1],$Khar)) ) {
	#PMS: Hence, $khari is understood here too
	$Apavada = $false;
	if ( ($Index + 2 < $linmax) ) {
	    if ( set_memberP($Linary[$Index + 2],$Schar) ) {
		$Apavada = $true; #PMS: 8.3.35.  Sarpare visarjanIyaH.
	    }
	}
	if ($dbg) {print "in kupvohXkXpau, Apavada = $Apavada\n";}
	if ( not ($Apavada) ) {
	    if ( set_memberP($Linary[$Index + 1],$Ku) ) {
		$Linary[$Index - 1] = $sktjihvamuliya;
	    }elsif ( set_memberP($Linary[$Index + 1],$Pu) ) {
		$Linary[$Index - 1] = $sktupadhmaniya;
	    }
	}
    }
    chk_point('kupvohXkXpau');
} #PMS: kupvohXkXpau

sub idudupadhasya {
    #PMS: 8.3.41.  idudupadhasya cApratyayasya ($kupvoH 37, $iRaH zaH 39
    #PMS: exception to 8.3.36.  kupvoH XkaXpau ca, $which is an exception to 8.3.34. visarjanIyasya saH,
    #PMS: so should accompany procedure visarjaniyasyasah.  Must follow 8.3.15.  kharavasAnayor visarjanIyaH
    if ( ($Linary[$Index - 1] eq $sktvisarga) and (set_memberP($Linary[$Index + 1],$Ku_and_Pu)) ) {
	if ( ($Pada1 eq 'nis') or ($Pada1 eq 'dus') or ($Pada1 eq 'bahis') or ($Pada1 eq 'Avis') or ($Pada1 eq 'catur') or ($Pada1 eq 'prAdur') ) {
	    $Linary[$Index - 1] = $sktsh; #PMS: bahis, $Avis =exception to 8.3.46
	}
    }
    chk_point('idudupadhasya');
}

sub nityamsamase {
    #PMS: 8.3.45. nityamsamAse 'nutarapadasthasya
    if ( $Compound ) {
	if ( ($Linary[$Index - 1] eq $sktvisarga) and (set_memberP($Linary[$Index + 1],$Ku_and_Pu)) and ($Index > 2) ) {
	    if ( (($Linary[$Index - 2] eq $skti) or ($Linary[$Index - 2] eq $sktu)) and (not $Uttarapada) ) {
		#PMS: Pada1­u.p.
		$Linary[$Index - 1] = $sktsh;
	    }
	}
    }
    chk_point('nityamsamase');
} #PMS: nityamsamase

sub atahkrkamikamsa {
    #PMS: 8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya ($samAse 45)
    if ( $Compound ) {
	if ( ($Linary[$Index - 1] eq $sktvisarga) and (set_memberP($Linary[$Index + 1],$Ku_and_Pu)) and ($Index > 2) ) {
	    if ( ($Linary[$Index - 2] eq $skta) ) {
		if ( ($Pada2 eq 'kAra') or ($Pada2 eq 'kAma') or ($Pada2 eq 'kaMsa') or ($Pada2 eq 'kumBa') or ($Pada2 eq 'kumBI') or ($Pada2 eq 'pAtra') or ($Pada2 eq 'kuSA') or ($Pada2 eq 'karRI') ) {
		    if ( not (($Pada1 eq 'svar') or ($Pada1 eq 'antar') or ($Pada1 eq 'prAtar') or ($Pada1 eq 'punar') or ($Pada1 eq 'sanutar') or ($Pada1 eq 'hyas') or ($Pada1 eq 'Svas') or ($Pada1 eq 'avas') or ($Pada1 eq 'aDas')) and (not $Uttarapada) ) {
			#PMS: miTas, $namas, (tiraskAra by 8.3.42.  avaskara, namaskAra?) krtvasuc, suc, i.e. not avyaya
			$Linary[$Index - 1] = $skts;
		    }
		}
	    }
	}
    }
    chk_point('atahkrkamikamsa');
} #PMS: atahkrkamikamsa

sub stohscunascuh {
    #PMS: 8.4.40.  stoH ScunA ScuH
    my $Isthana; # type = $sthanatype;
    my $Iyatna; # type = $yatnatype;
    if ( (set_memberP($Linary[$Index - 1],$Tu_and_skts)) and (set_memberP($Linary[$Index + 1],$Cu_and_sktsch)) ) {
	($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
	$Linary[$Index - 1] = $Soundary[$italavya][$Iyatna1];
    }elsif ( (set_memberP($Linary[$Index - 1],$Cu_and_sktsch)) and ($Linary[$Index + 1] eq $skts) ) {
	$Linary[$Index + 1] = $sktsch;
	if ( ($Index + 2 < $linmax) ) {
	    if ($Linary[$Index + 2] eq $skts) {
		$Linary[$Index + 1] = $sktsch;
	    }
	}
    }elsif ( (set_memberP($Linary[$Index - 1],$Cu)) and (set_memberP($Linary[$Index + 1],$Tu)) ) {
	#PMS: 8.4.44.  SAt. ($na, $toH)
	($Isthana2,$Iyatna2) = identify($Linary[$Index + 1]);
	$Linary[$Index + 1] = $Soundary[$italavya][$Iyatna2];
	if ( ($Index + 2 < $linmax) ) {
	    if (set_memberP($Linary[$Index + 2],$Tu_and_skts)) {
		($Isthana,$Iyatna) = identify($Linary[$Index + 2]);
		$Linary[$Index + 2] = $Soundary[$italavya][$Iyatna];
	    }
	}
    }
    chk_point('stohscunascuh');
} #PMS: stohscunascuh

sub stunastuh {
    #PMS: 8.4.41.  zwunA zwuH
    my $Isthana; # type = $sthanatype;
    my $Iyatna; # type = $yatnatype;
    if ( ( ($Linary[$Index - 1] eq $sktsh) and (set_memberP($Linary[$Index + 1],$Tu_and_skts)) ) or (set_memberP($Linary[$Index - 1],$Retrotu) and ($Pada2 eq 'nAm')) ) {
	#PMS: 8.4.42.  na padAntAwworanAm
	($Isthana2,$Iyatna2) = identify($Linary[$Index + 1]);
	$Linary[$Index + 1] = $Soundary[$imurdhanya][$Iyatna2];
	if ( ($Index + 2 < $linmax) ) {
	    if (set_memberP($Linary[$Index + 2],$Tu_and_skts)) {
		($Isthana,$Iyatna) = identify($Linary[$Index + 2]);
		$Linary[$Index + 2] = $Soundary[$imurdhanya][$Iyatna];
	    }
	}
    }elsif ( (set_memberP($Linary[$Index - 1],$Tu) and (set_memberP($Linary[$Index + 1],$Retrotu)) ) or (($Linary[$Index - 1] eq $skts) and (set_memberP($Linary[$Index + 1],$Retrotu_sktsh))) ) {
	#PMS: 8.4.43.  toH zi. ($na)
	($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
	$Linary[$Index - 1] = $Soundary[$imurdhanya][$Iyatna1];
    }
    chk_point('stunastuh');
} #PMS: stunastuh

sub anusvarasya {
    #PMS: 8.4.59.  vA padAntasya ($anusvArasya yayi parasavarRaH 58).
    #PMS: don't exercise the option for semivowels ($yan) just now
    if ( ($Linary[$Index - 1] eq $sktanusvara) and (set_memberP($Linary[$Index + 1],$Yay_not_Yan)) ) {
	($Isthana2,$Iyatna2) = identify($Linary[$Index + 1]);
	$Linary[$Index - 1] = $Soundary[$Isthana2][$isparsa5];
    }
    chk_point('anusvarasya');
} #PMS: anusvarasya

sub torli {
    #PMS: 8.4.60.  tor li
    if ( (set_memberP($Linary[$Index - 1],$Tu)) and ($Linary[$Index + 1] eq $sktl) ) {
	($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
	$Linary[$Index - 1] = $sktl;
	if ( $Iyatna1 eq $isparsa5 ) {
	    insertary($sktnasalization, $Index - 1);
	    if ( $NoSpace ) {
		$Error = 2;
		return; # REPLACE exit($sandhi);
	    }
	    $Index = $Index + 1;
	}
    }
    chk_point('torli');
} #PMS: torli


sub jhayoho {
    #PMS: 8.4.62.  jhayo ho 'nyatarasyAm
    if ( (set_memberP($Linary[$Index - 1],$Jhay)) and ($Linary[$Index + 1] eq $skth) ) {
	($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
	$Linary[$Index + 1] = $Soundary[$Isthana1][$isparsa4];
    }
    chk_point('jhayoho');
} #PMS: jhayoho

sub saschoti {
    #PMS: 8.4.63.  SaS cho 'wi. (jhayaH 62, anyatarasyAm 62)
    if ($false) {
	my ($cp,$c1,$c,$c2);
	$cp = $Linary[$Index - 1];
	$c1 =  $Linary[$Index + 1];
	$c2 = $Linary[$Index + 2];
	print "saschoti: chars = '$cp', '$c1', '$c2'\n";
	print "Jhay = $Jhay, sktsch = '$sktsch', At = '$At':  sktch = '$sktch'\n";
    }
    if ( (set_memberP($Linary[$Index - 1],$Jhay)) and (($Index + 2) < $linmax) ) {
	if ( ($Linary[$Index + 1] eq $sktsch) and (set_memberP($Linary[$Index + 2],$At)) ) {
	    #PMS: vt. chatvamamIti vaktavyam:  Am instead of At.  tacchlokena, $tacchmaSruRA
	    $Linary[$Index + 1] = $sktch;
	}
    }
    chk_point('saschoti');
} #PMS: saschoti

sub yaronunasike {
    #PMS: 8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)

    ($Isthana2,$Iyatna2) = identify($Linary[$Index + 1]);
    #PMS: if ( set_memberP($Linary[$Index - 1],$Yar) and ($Index + 2 < $linmax) then
    #PMS: if ($Iyatna2 eq $isparsa5) or ($Linary[$Index + 2] eq $sktanunasika) ) {
    #PMS: we wont exercise the nasalized option for the semivowels y, $v and l; just for the stops
    if ( (set_memberP($Linary[$Index - 1],$Jhay)) and ($Iyatna2 eq $isparsa5) ) {
	($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
	$Linary[$Index - 1] = $Soundary[$Isthana1][$isparsa5];
    }
    chk_point('yaronunasike');
} #PMS: yaronunasike

sub kharica {
    #PMS: 8.4.55.  khari ca. ($jhalAm 53, $car 54)
    #PMS: there is no final  'h' after jhalAm jaSo 'nte, $but there is $skts by 8.3.34 visarjanIyasya saH
    #PMS: and $sktsch and $sktsh by 8.4.40-41 stoH ScunA scuH, $zwunA zwuH so must exclude Sar
    if ( set_memberP($Linary[$Index - 1],$Jhay) ) {
	#PMS: jhay=jhal-Sar
	($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
	if ( set_memberP($Linary[$Index + 1],$Khar_and_linend) ) {
	    #PMS: 8.4.56.  vavasane
	    $Linary[$Index - 1] = $Soundary[$Isthana1][$isparsa1];
	}
    }
    chk_point('kharica');
} #PMS: kharica

sub idudeddvivacanampragrhyam {
    #PMS: 1.1.11. IdUdeddvivacanam pragfhyam
    $Pragrhya = $false;
    my $c = $Linary[$Index - 1];
    if ( $External ) {
	if($c eq $sktii) {
	    if ( ($Pada1 eq 'amI') or ($Pada1 eq 'aDiparI') or ($Pada1 eq 'aBipratI') or ($Pada1 eq 'manasI') ) {
		$Pragrhya = $true;
	    }
	}elsif ($c eq $sktuu) { 
	    if ( ($Pada1 eq 'amU') ) {
		#PMS: 1.1.12.  adaso mAt
		$Pragrhya = $true;
	    }
	}elsif ($c eq $skte) { 
	    if ( ($Pada1 eq 'SAlInakOpIne') or ($Pada1 eq 'uBe') ) {
		$Pragrhya = $true;
	    }
	}elsif ($c eq $skto) { 
	    if ( ($Pada1 eq 'Aho') or ($Pada1 eq 'utAho') ) {
		#PMS: 1.1.15. ot
		$Pragrhya = $true;
	    }
	}else {
	} #PMS: case
    }
    chk_point('idudeddvivacanampragrhyam');
} #PMS: pragrhya

#-------------------------sandhiPrep routine from SandhiPrepGen.pp
sub sandhiPrep {
#	procedure sandhiPrep (var Linary: linetype; var Index: lenrangeE; var PurvaPada, Pada1, Pada2: padatype; var NoStoh, NoKNam, Exception, Pronoun, CloseSandhi: boolean);
# ejf: all the argument list variables (Linary .. CloseSandhi)  are global variables.
    my $L; # type = $lenrange0;
    my $IPada; # type = $lenrangeE;
    my $NoPrep; # type = $boolean;
#    my $NoSpace; # type = $boolean;  global
    $NoStoh = $false;
    $NoKNam = $false;
    $NoPrep = $false;
    $Exception = $false;
    $Pronoun = $true; #PMS: saú is usually the pronoun tad
    $OtherCloseSandhi = $false;
    $L = length($Pada1);
    if ($L <= 1) {
	return;
    }
    my $c = substr($Pada1,$L-1,$L); # last character of $Pada1.
    if (0 eq 1) {print STDOUT " in sandhiPrep, c = $c, Pada1 ='$Pada1'\n";}
    if ($c eq $sktkn) {
	# RiN change made 20090801, PMS.
	if ($Pada1 eq 'RiN') {
	    $Exception = $true;
	}
    }elsif ($c eq $sktc) { 
	for ($IPada = 1; $IPada <= $cantamax;$IPada++) {
	    if ( $Pada1 eq $CAntaPadary[$IPada] ) {
		$NoPrep = $true;
		$NoStoh = $true;
		$IPada = $cantamax; # leave loop
	    }
	}
    }elsif ($c eq $sktj) {
	if ( ($Pada1 eq 'tij') ) {
	    $Exception = $true;
	}elsif ( ($Pada1 eq 'tuj') ) {
	    $NoPrep = $true;
	}
    }elsif ($c eq $sktcn) {
	if ( ($Pada1 eq 'aY') or ($Pada1 eq 'alaNkfY') or ($Pada1 eq 'nirAkfY') or ($Pada1 eq 'naY') or ($Pada1 eq 'wIwaY') or ($Pada1 eq 'WaY') ) {
	    $NoStoh = $true;
	}
    }elsif ($c eq $sktretron) {
	if ( ($Pada1 eq 'aR') or ($Pada1 eq 'uR') or ($Pada1 eq 'yaR') ) {
	    $Exception = $true;
	}
    }elsif ($c eq $sktdh) {
	if ( ($Pada1 eq 'aD') or ($Pada1 eq 'ruD') ) {
	    $Exception = $true;
	}
    }elsif ($c eq $sktn) {
	if ( ($Pada1 eq 'Wan') or ($Pada1 eq 'tran') or ($Pada1 eq 'dozan') or ($Pada1 eq 'yakan') or ($Pada1 eq 'yUzan') or ($Pada1 eq 'Sakan') or ($Pada1 eq 'zWan') or ($Pada1 eq 'han') ) {
	    $NoPrep = $true;
	}elsif ( ($Pada1 eq 'Ayan') or ($Pada1 eq 'Gan') ) {
	    $NoPrep = $true;
	    $NoKNam = $true;
	}elsif ( ($Pada1 eq 'ktin') or ($Pada1 eq 'kvin') or ($Pada1 eq 'min') or ($Pada1 eq 'vin') ) {
	    $NoPrep = $true;
	}elsif ( ($Pada1 eq 'an') or ($Pada1 eq 'in') or ($Pada1 eq 'kan') or ($Pada1 eq 'kaDyEn') or ($Pada1 eq 'qvun') or ($Pada1 eq 'tan') or ($Pada1 eq 'dAn') or ($Pada1 eq 'man') or ($Pada1 eq 'vun') ) {
	    $Exception = $true;
	}elsif ( $Pada1 eq 'tumun' ) {
	    $NoStoh = $true;
	}
    }elsif ($c eq $sktm) {
	if ( ($Pada1 eq 'am') or ($Pada1 eq 'Am') or ($Pada1 eq 'num') ) {
	    $Exception = $true;
	}elsif ( $Compound ) {
	    if ( (($Pada1 eq 'puram') and ($Pada2 eq 'dArO')) ) {
		#PMS: purandrau
		$OtherCloseSandhi = $true;
	    }
	}
    }elsif ($c eq $skty) {
	if ( ($Pada1 eq 'ay') or ($Pada1 eq 'Ay') ) {
	    $Exception = $true;
	}
    }elsif ($c eq $sktr) {
	if ( ($Pada1 eq 'car') or ($Pada1 eq 'kur') or ($Pada1 eq 'Sar') ) {
	    $Exception = $true;
	}
    }elsif ($c eq $sktsch) {
	if ( ($Pada1 eq 'eS') or ($Pada1 eq 'KaS') or ($Pada1 eq 'jaS') or ($Pada1 eq 'niS') ) {
	    $Exception = $true;
	}
    }elsif ($c eq $sktsh) {
	if ( ($Pada1 eq 'Jaz') or ($Pada1 eq 'Baz') ) {
	    $Exception = $true;
	}
    }elsif ($c eq $skts) {
	if ( ($Pada1 eq 'as') or ($Pada1 eq 'atus') or ($Pada1 eq 'aTus') or ($Pada1 eq 'is') or ($Pada1 eq 'us') or ($Pada1 eq 'os') or ($Pada1 eq 'kas') or ($Pada1 eq 'kAs') or ($Pada1 eq 'Nas') or ($Pada1 eq 'tas') or ($Pada1 eq 'tAs') or ($Pada1 eq 'TAs') or ($Pada1 eq 'Bis') or ($Pada1 eq 'Byas') ) {
	    $Exception = $true;
	}
    }else {
    } #PMS: case

    if ( $Compound ) {
	#PMS: normal stem changes
	if ( (not $Exception) and (not $NoPrep) ) {
	    $c = $Linary[$Index - 1];
	    if ($c eq $sktc) {
		if ( $Pada1 eq 'aYc' ) {
		    #PMS: aYc
		    $Linary[$Index - 1] = $sktk; #PMS: ak
		    deletary($Index - 2);
		    $Index = $Index - 1;
		} else {
		    $Linary[$Index - 1] = $sktk;
		}
	    }elsif ($c eq $sktch) {
		$Linary[$Index - 1] = $sktk;
	    }elsif ($c eq $sktj ) {
		if ( ($Pada1 eq 'rAj') ) {
		    $Linary[$Index - 1] = $sktretrot;
		}else {
		    $Linary[$Index - 1] = $sktk;
		}
	    }elsif ($c eq $sktjh) {
		$Linary[$Index - 1] = $sktk;
	    }elsif ($c eq $sktn) {
		if ( $Index > 2 ) {
		    if ( ($Linary[$Index - 2] eq $skta) or ($Linary[$Index - 2] eq $skti) ) {
			#PMS: an-/in-
			if ( (($Pada1 eq 'ahan') and ($PurvaPada ne 'eka')) ) {
			    # noop
			}else {
			    #PMS: normal 'an-'/'in-'
			    deletary($Index - 1);
			    $Index = $Index - 1;
			}
		    } #PMS: an-/in-
		}
	    }elsif ($c eq $sktr) {
		if ( ($Pada1 eq 'pur') or ($Pada1 eq 'Dur') ) {
		    $Linary[$Index - 2] = $sktuu;
		}
	    }elsif ($c eq $sktsch) {
		if ( $Pada1 eq 'viS' ) {
		    $Linary[$Index - 1] = $sktretrot;
		}else {
		    $Linary[$Index - 1] = $sktk;
		}
	    }elsif ($c eq $sktsh) {
		if ( $Pada1 eq 'daDfz' ) {
		    $Linary[$Index - 1] = $sktk;
		}
	    }elsif ($c eq $skts) {
		if ( ($Pada1 eq 'ASis') ) {
		    $Linary[$Index - 2] = $sktii #PMS: 82104
		    }elsif ( $Pada1 eq 'pums' ) {
			#PMS: 'pum'
			deletary($Index - 1);
			$Index = $Index - 1;
		    } #PMS: 'pum'
	    }else {
		#PMS: no preparation necessary, $normal sandhi will follow
	    } #PMS: case $statement
	} #PMS: astadhyayiSandhiPrep
    } #PMS: sandhiprep
}

# ---------------- sandhi routine from SandhiGen.pp
sub sandhi {
    # ejf. Accept string argument, to which sandhi is to be applied.
    # return a string argument as the answer
    # return a blank string if there is an error
    # print an informative message if there is an error.
    my ($s) = @_;
    my ($whitebeg,$whiteend,$x,$y);
    my @split = sandhiSplit($s);
    my $n = $#split;
    my $ans=$whitebeg;
    my $i = 0;
    while ($i < $n) {
#	print $j,"  ", $split[$i],"  \"",$split[$i+1],"\"\n";
	$x = $split[$i+1];
	if ($x =~ /^(\s+)(.*)$/) {
	    $whitebeg=$1;
	    $x = $2;
	}else {
	    $whitebeg='';
	}
	if ($x =~ /(.*?)(\s+)$/) {
	    $whiteend=$2;
	    $x = $1;
	}else {
	    $whiteend='';
	}
	if ($split[$i] eq 's') {
	    $y = sandhi1($x);
	}else {
	    $y = $x;
	}
	$y = $whitebeg . $y . $whiteend;
	$ans .= $y;
	$i += 2;
    }
#   $ans .= $whiteend;
    return $ans;
}
sub sandhiSplit {
# Apr 21, 2009
# from a given input string, generate an array,
# The even elements (0,2,4...) have value
# 's' if the next array element is a string of Sanskrit characters
# 'o' if the next array element is a string of non-Sanskrit characters
    my $x = shift;
    my @a;
    my $na=0;
    my $INITIAL = 0;
    my $SKT = 1;
    my $OTHER = 2;

    my $state = $INITIAL;
    my $more = 1;
    my $y="";
    # Only non-alphabetic chars are - and space and apostrophe and '|'
#    my $sanskrit = "[- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|]";
    # 20090801, '#' is a sandhi-blocking character.
    my $sanskrit = "[- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|#]";
    while ($more) {
	if ($state eq $INITIAL) {
	    $y = "";
	    if ($x =~ /\G($sanskrit)/gc) {
		$state = $SKT;
		$y = $&;
		next;
	    }elsif ($x =~ /\G./gc) {
		$state = $OTHER;
		$y = $&;
		$next;
	    }else { # no chars left
		goto DONE;
	    }
	}elsif ($state eq $SKT) {
	    if ($x =~ /\G($sanskrit)/gc) {
		$y .= $&;
		next;
	    }else {
		$a[$na]='s';
		$na++;
		$a[$na]=$y;
		$na++;
		$state = $INITIAL;
		$next;
	    }
	}else  { # $state = $OTHER
	    if ($x =~ /\G($sanskrit)/gc) {
		$a[$na]='o';
		$na++;
		$a[$na]=$y;
		$na++;
		$state = $SKT;
		$y=$&;
		$next;
	    }elsif ($x =~ /\G./gc) {
		$y .= $&;
		next;
	    }else {
		goto DONE;
	    }
	}
    }
DONE:
    if ($y ne '') {
	if ($state eq $SKT) {
	    $a[$na]='s';
	    $na++;
	    $a[$na]=$y;
	}elsif ($state eq $OTHER) {
	    $a[$na]='o';
	    $na++;
	    $a[$na]=$y;
	}else { # should not occur
	}
    }
    return @a;
}
sub sandhi1 {
    # ejf. Accept string argument, to which sandhi is to be applied.
    # return a string argument as the answer
    # return a blank string if there is an error
    # print an informative message if there is an error.
    my ($s) = @_;
    
    my $s1 = str_trim($s);
    if (($s eq 'dbg') or ($s eq 'off')) {
	if (not $dbg) {
	    print "Turning on debug. To turn off, enter 'off'\n";
	    $dbg = $true;
	}else {
	    print "Turning off debug. To turn on, enter 'dbg'\n";
	    $dbg = $false;
	}
	return;
    }
#    $s1 = '  ' . $s1 . '          ';
    # change of 20090801, PMS,ejf
    $s1 = ' ' . $s1 . '          ';
#    $s1 = ' . ' . $s1 . '          ';
    @Linary = split('',$s1); # this is what sandhimain modifies.
    if (0 eq 1) {print STDOUT "Linary = '",join(',',@Linary),"'\n";}
    $linmax = length($s1) - 1;
#    print "linmax = $linmax\n";
    chk_point('calling sandhimain');
#    return;
    $Error = 0;
    sandhimain();
    if ($Error ne 0) {
	print "sandhi error($Error): $s\n";
	return '';
    }else {
	my $ans = join('',@Linary);
	$ans = str_trim($ans);
	return($ans);
    }
}
sub sandhimain {
    # ejf: following variables declared with 'var' in 
    # procedure sandhi; in SandhiGen.pp. Pascal compiler probably
    # gives all these a default value at each call of sandhi();
    # So, I will do the same here.
    # Isthana1, Isthana2: sthanatype;
    # Iyatna1, Iyatna2: yatnatype;
    # IEnd: lenrange0;
    # Inext, Inextsp, IPrev, IPrevSpace, Index, I: lenrangeE;
    # Found, NoSpace, Dhralopa: boolean;
    # OtherCloseSandhi, Pragrhya, Uttarapada, NxtUttarapada: boolean;
    $Isthana1 = 0;
    $Isthana2 = 0;
    $Iyatna1 = 0;
    $Iyatna2 = 0;
    $IEnd = 0;
    $Index = 0;
    $Found = $false;
    $NoSpace = $false;
    $Dhralopa = $false;
    $OtherCloseSandhi = $false;
    $Pragrhya = $false;
    $Uttarapada = $false;
    $NxtUttarapada = $false;
    # - these appear to be used only with the body of Sandhi.
    #   so declare with 'my'
    my $Inext = 0;
    my $Inextsp = 0;
    my $IPrev = 0;
    my $IPrevSpace = 0;
    my $I = 0;

    $PurvaPada = '';
    $Pada1 = '';
    $Pada2 = '';
    $Index = nxtposary($Padbound, $FldChr, 2); #PMS: the first character in $Linary should not be a word boundary
    $Upasarga = $false; # ejf.
    if (0 eq 1) {print STDOUT "Index = $Index, Padbound = $Padbound, FldChr=$FldChr\n";}
    while ($Index > 0)  {
	#PMS: while a padbound character is found
	$EkahPurvaParayoh = $false;
	#PMS: PurvaPada, $Pada1, $Pada2
	$Uttarapada = $false;
	if ( $NxtUttarapada ) {
	    $Uttarapada = $true; #PMS: Pada1 is an uttarapada
	}
	$NxtUttarapada = $false;
	#PMS: first $Pada1 in $Linary
	$PurvaPada = $Pada1;
	if (0 eq 1) {
	    print STDOUT "PurvaPada = $PurvaPada, Pada1 = $Pada1, NxtPada1 = $NxtPada1, Pada2 = $Pada2, Uttarapada = $Uttarapada, NxtUttarapada = $NxtUttarapada,Compound = $Compound, External = $External , IPrev = $IPrev, Index = $Index  \n";
	}
	if ( $IPrev eq 0 ) {
	    #PMS: first $Pada1 in $Linary
	    if ( $Compound ) {
		$IPrev = lastposary($space, $Index - 1);
	    }
	    $Pada1 = substrary($IPrev + 1, $Index - 1);
	}elsif ( $External ) {
	    #PMS: we been through here before so
	    $Pada1 = $Pada2;
	}else {
	    #PMS: padbound=hyphen
	    $Pada1 = $NxtPada1;
	}
	if (0 eq 1) {
	    print STDOUT "NOW Pada1 = $Pada1\n";
	}
	$Inext = nxtposary($Padbound, $FldChr, $Index + 1);
	if (0 eq 1) {print "Inext = $Inext\n";}
	if ( $Inext eq 0 ) {
	    #PMS: not found so last word
	    $Inext = lengthary() + 1;
	}
	if (0 eq 1) {
	    print STDOUT "PurvaPada = $PurvaPada, Pada1 = $Pada1, NxtPada1 = $NxtPada1, Pada2 = $Pada2, Uttarapada = $Uttarapada, NxtUttarapada = $NxtUttarapada,Compound = $Compound, External = $External , IPrev = $IPrev, Index = $Index  \n, FldChr = $FldChr, Inextsp = $Inextsp, ";
	}
	if ( $External ) {
	    $Pada2 = substrary($Index + 1, $Inext - 1);
	}else {
	    #PMS: for compound, $Pada2, $NxtPada1
	    $Inextsp = nxtposary($space, $FldChr, $Index + 1);
	    if ( ($Inextsp > 0) and ($Inextsp < $Inext) ) {
		$Pada2 = substrary($Index + 1, $Inextsp - 1);
	    }else {
		$Pada2 = substrary($Index + 1, $Inext - 1);
	    }
	    #PMS: now the next $Pada1 when $padbound =hyphen
	    $IPrevSpace = lastposary($space, $Inext - 1);
	    if (0 eq 1) {print STDOUT "IPrevSpace = $IPrevSpace\n";}
	    if ( $IPrevSpace > $Index ) {
		$NxtPada1 = substrary($IPrevSpace + 1, $Inext - 1); # corrected
	    }else {
		$NxtPada1 = $Pada2;
		$NxtUttarapada = $true;
	    }
	} #PMS: Pada2, $NxtPada1 hyphen
	if (0 eq 1) {
	    print STDOUT "PurvaPada = $PurvaPada, Pada1 = $Pada1, NxtPada1 = $NxtPada1, Pada2 = $Pada2, Uttarapada = $Uttarapada, NxtUttarapada = $NxtUttarapada \n";
	}
	#PMS: end of PurvaPada, $Pada1, $Pada2
	#PMS: determine whether $Pada1 is an upasarga
	$Upasarga = $false;
	if ( $External and ($Pada1 eq 'ut') ) {
	    $Pada1 = 'ud';
	}
	if ( $Pada1 eq 'api' ) {
	    #PMS: more likely karmapravacanIya than upasarga
	}else {
	    for ($I = 1; $I <= $pradimax;$I++) {
		if ( $Pada1 eq $Pradi[$I] ) {
		    $Upasarga = $true;
		    $I = $pradimax; #to leave loop
		}
	    }
	}
	#PMS: stem final sound changes for compound sandhi and some special sandhi for grammatical technical terms
	# ejf: args are globals: ($Linary, $Index, $PurvaPada, $Pada1, $Pada2, $NoStoh, $NoKNam, $Exception, $Pronoun, $OtherCloseSandhi)
	# ejf note: OtherCloseSandhi.  This was called 'CloseSandhi' in
	# sandhiPrep; I changed name in routine to OtherCloseSandhi.
	if (0 eq 1) {print STDOUT "calling sandhiPrep: Exception=$Exception, Pada1 = $Pada1\n";}
	sandhiPrep();
	if (0 eq 1) {
	    print STDOUT "Back from sandhiPrep: NoStoh = $NoStoh, NoKNam = $NoKNam,  Exception = $Exception, Pronoun = $Pronoun, OtherCloseSandhi = $OtherCloseSandhi \n";
	}
	if ( $Exception ) {
	    goto label7000; #PMS: skip sandhi
	}
	if ( $Upasarga and $CloseUpasargaSandhi ) {
	    $OtherCloseSandhi = $true; #PMS: initialized in $sandhiPrep
	}
	#PMS: sandhi subroutines:  within compound and following an upasarga closer sandhi is observed when an option is allowed
	#PMS: otherwise (between syntactic units) looser sandhi is observed
	idudeddvivacanampragrhyam(); #PMS: kosher exceptions to sandhi
	if ( $Pragrhya ) {
	    goto label7000; #PMS: skip sandhi
	}
	if ( ($Linary[$Index - 1] eq $sktvisarga) ) {
	    visargaprep();
	}
	($Isthana1,$Iyatna1) = identify($Linary[$Index - 1]);
	($Isthana2,$Iyatna2) = identify($Linary[$Index + 1]);
	#PMS: must precede 8.4.40.  stoH ScunA ScuH
	checa(); #PMS: 6.1.73.  che ca
	anmanosca(); #PMS: 6.1.74.  ANmANoSca (che 73, tuk 71)
	if ( ($TukPadantat) ) {
	    padantadva(); #PMS: 6.1.76.  padAntAdvA (dIrghAt 75, che 73, tuk 71)
	}
	#PMS: must precede vowel sandhi
	if ( set_memberP($Linary[$Index - 1],$sktn_and_sktsh_and_skts) ) {
	    if ( $Pronoun ) {
		etattadohsulopo(); #PMS: 6.1.132.  etattadoH sulopo 'kor anaYsamAse hali
	    }
	    amnarudharavar(); #PMS: 8.2.70.  amnarUdharavarityubhayathA chandasi
	    sasajusoruh(); #PMS: 8.2.66.  sasajuzo ruH
	    if ( not $NoStoh ) {
		#PMS: exception in 63110
		ahan(); #PMS: 8.2.68.  ahan
	    }
	    atororhasica(); #PMS: 6.1.13.  ato ror aplutad aplute.  6.1.14.  haSi ca.  Must precede 6.1.109.  eNaH padAntAd ati
	}
	if ( set_memberP($Linary[$Index - 1],$Ac) and set_memberP($Linary[$Index + 1],$Ac) ) {
	    acsandhi();
	} elsif ( (set_memberP($Linary[$Index - 1],$Hal_and_ru)) and (set_memberP($Linary[$Index + 1],$Al_and_Linend)) ) {
	    jhalamjasonte(); #PMS: 8.2.39.  jhalAM jaSo 'nte
	    naschavyaprasan(); #PMS: 8.3.7.  naS chavy apraSAn
	    rori(); #PMS: 8.3.14.  ro ri  ejf: $Dhralopa is global
	    dhralope(); #PMS: 6.3.111.  qhralope pUrvasya dIrgho 'RaH
	    bhobhago(); #PMS: 8.3.17.  bhobhagoaghoapUrvasya yo 'Si
	    kharavasanayor(); #PMS: 8.3.15.  kharavasAnayor visarjanIyaH
	    otogargyasya(); #PMS: 8.3.20.  oto gArgyasya.  This cannot precede vowel sandhi
	    monusvarah(); #PMS: 8.3.23.  mo 'nusvAraH
	    if ( not $NoKNam ) {
		namohrasvad(); #PMS: 8.3.32.  Namo hrasvAd aci NamuR nityam
	    }
	    visarjaniyasyasah(); #PMS: 8.3.34.  visarjanIyasya saH
	    if ( $ScharSchari ) {
		vasari(); #PMS: 8.3.36.  vA Sari
	    }
	    #PMS: 8.3.41, 8.3.45 and 8.3.46 are apavAdas of 8.3.37 so they must precede it
	    idudupadhasya(); #PMS: 8.3.41.  idudupadhasya cApratyayasya (kupvoH 37, iRaH zaH 39)
	    nityamsamase(); #PMS: 8.3 .45. nitya samAse 'nutarapadasthasya
	    atahkrkamikamsa(); #PMS: 8.3.46.  ataH kfkamikaMsakumbhapAtrakuSAkarRIzvanavyayasya
	    if ( $XkXpKupvoh ) {
		kupvohXkXpau(); #PMS: 8.3.37.  kupvoH XkXpau ca (khari 15).
	    }
	    if ( not $NoStoh ) {
		stohscunascuh(); #PMS: 8.4.40.  stoH ScunA ScuH
		stunastuh(); #PMS: 8.4.41.  zwunA zwuH
	    }
	    torli(); #PMS: 8.4.60.  tor li
	    if ( $ChAti ) {
		saschoti(); #PMS: 8.4.63.  SaS cho 'wi. (jhayaH 62, anyatarasyAm 62)
	    }
	    jhayoho(); #PMS: 8.4.62.  jhayo ho 'nyatarasyAm
	    kharica(); #PMS: 8.4.55.  khari ca
	    if ( $ParaSavarna or $OtherCloseSandhi ) {
		anusvarasya(); #PMS: 8.4.59.  vA padAntasya (anusvArasya yayi parasavarRaH 58).
	    }
	}
	if ( (set_memberP($Linary[$Index - 1],$Hal)) and (set_memberP($Linary[$Index + 1],$Al)) ) {
	    #PMS: must follow vowel sandhi
	    lopahsakalyasya(); #PMS: 8.3.19.  lopaH SAkalyasya.  Must follow 6.1.78.  eco 'yavAyAvaH
	    #PMS: If made to include semivowels, 8.4.45 must follow 8.3.19-20.  In present form it needn't.
	    if ( $Anunasika or $OtherCloseSandhi ) {
		yaronunasike(); #PMS: 8.4.45.  yaro 'nunAsike 'nunAsiko vA. (padAnta 42)
	    }
	}
label7000:
	chk_point('label7000a');
	if ($dbg) {print "Index = $Index\n";};
	#PMS: get rid of the space between words
	if ( $EkahPurvaParayoh ) {
	    #PMS: EkahPurvaParayoh set in $acsandhi in $subroutines: akahsavarnedirghah, $adgunah, $vrddhireci
	    #PMS: do the same steps if two padbounds in $a row because last sandhi eliminated single char word
	    deletary($Index);
	    $Index = $Index - 1; #PMS: the search for the next padbound begins at $Index+1
	}elsif ( ($Index > 1) and $Despace ) {
	    if ( set_memberP($Linary[$Index - 1],$Hal) ) {
		#PMS: Removed "or Upasarga"
		deletary($Index);
	    }
	}
	if ( $Linary[$Index] eq $hyphen ) {
	    deletary($Index);
	    $Index = $Index - 1;
	}
	$IPrev = $Index;
	$Index = nxtposary($Padbound, $FldChr, $Index + 1); #PMS: find the next pada boundary
	chk_point('label7000b');
	if ($dbg) {print "Index = $Index\n";};
    } #PMS: conclude while loop when padbound character is not found ($Index=0)
} #PMS: sandhimain

1; #
