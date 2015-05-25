#!/usr/bin/perl
use sandhi;
my $sopt = $ARGV[0];
my $filein = $ARGV[1];
my $fileknown = $ARGV[2];

my $compound_ans,$vedic_ans,$close_ans,$despace_ans;
if ($sopt eq "C") {
 $compound_ans="C";
 $vedic_ans="N";
 $close_ans="S";
 $despace_ans="";
}elsif ($sopt eq "E") {
 $compound_ans="E";
 $vedic_ans="N";
 $close_ans="S";
 $despace_ans="Y";
}elsif ($sopt eq "E1") {
 $compound_ans="E";
 $vedic_ans="N";
 $close_ans="S";
 $despace_ans="";
}else {
 die "ERROR: sopt must be E, E1, or C, not $sopt\n"
}

$err = sandhioptions($compound_ans,$vedic_ans,$close_ans,$despace_ans);
if ($err ne 0) {
    die "sandhioptions returns err = $err\n";
}
# Slurp filein into @lines
open my $handle, '<', $filein;
chomp(my @lines = <$handle>);
close $handle;
# slurp fileknown into @correct
open my $handle, '<', $fileknown;
chomp(my @correct = <$handle>);
close $handle;
my $nlines = @lines;
my $i = 0;
$nok = 0;
for($i=0;$i<$nlines;$i++){
 $line = @lines[$i];
 $line =~ s/[\n\r]//;
 $ans = sandhi($line);
 $known = @correct[$i];
 $known =~ s/[\n\r]//;
 # remove trailing space(s) from both
 $ans =~ s/ +$//;
 $known =~ s/ +$//;
 if ($known eq $ans) {
  $nok = $nok + 1;
 }else {
     print "Problem at line $i\n";
     print "   input:$line\n";
     print " options:$sopt\n";
     print "computed:$ans\n";
     print "standard:$known\n";
     print "========================================";
 }

}
print "Test Results:\n";
print "Input: $filein\n";
print "Standard: $fileknown\n";
print "$nok input lines were ok out of $nlines total lines\n";

