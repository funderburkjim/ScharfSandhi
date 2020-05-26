/*
 * ScharfSandhiArg -  Command line program.
 * Usage:  java ScharfSandhiArg <C|E> <Y|N> <string>
 * 1: compound or external
 *  C : Apply Compound Sandhi where there is a hyphen
 *  E : Apply External Sandhi where there is a space
 * Skip 2 default N: Candas Y or N
 * Skip 3 degault S: close sandhi Y, N or S for standard
 * 4: despace Y or N
 The String should normally be in double quotes. It should be written in SLP1 transliteration.
 * Output is printed to stdout.
 * Peter Scharf
 * May 2020
 The directory in which this is run should have ScharfSandhi.class
 */

import java.util.*;
public final class ScharfSandhiArgFunction {
 public static String sandhi(String ec, String despace, String s){
  int err;
  err=ScharfSandhi.sandhioptions(ec,"N","S",despace);
  if (err == 0) {
   String ans = ScharfSandhi.sandhi(s);
   return ans;
  } else return "Error: " + err;
 }
}
