/*
 * ScharfSandhiArg -  Command line program.
 * Usage:  java ScharfSandhiArg <C|E> <string>
 * 1: compound or external
 *  C : Apply Compound Sandhi where there is a hyphen
 *  E : Apply External Sandhi where there is a space
 * 2: Candas Y or N
 * 3: close sandhi Y, N or S for standard
 * 4: despace Y or N
 The String should normally be in double quotes. It should be written in SLP1 transliteration.
 * Output is printed to stdout.
 * Jim Funderburk
 * May 2015
 The directory in which this is run should have ScharfSandhi.class
 */

import java.util.*;
public final class ScharfSandhiArg {
 public static String esandhi(String s){
  String sopt = "E";
  int err;
  err=ScharfSandhi.sandhioptions("E","N","S","N");
  if (err == 0) {
   String ans = ScharfSandhi.sandhi(s);
   return ans;
  } else return "Error: " + err;
 }
 public static String csandhi(String s){
  String sopt = "C";
  int err;
  err=ScharfSandhi.sandhioptions("C","N","S","");
  if (err == 0) {
   String ans = ScharfSandhi.sandhi(s);
   return ans;
  } else return "Error: " + err;
 }
}
