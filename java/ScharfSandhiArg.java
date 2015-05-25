/*
 * ScharfSandhiArg -  Command line program.
 * Usage:  java ScharfSandhiArg <C|E> <string>
 *  C : Apply Compound Sandhi where there is a hyphen
 *  E : Apply External Sandhi where there is a space
 The String should normally be in double quotes. It should be written in SLP1 transliteration.
 * Output is printed to stdout.
 * Jim Funderburk
 * May 2015
 The directory in which this is run should have ScharfSandhi.class
 */

import java.util.*;
public class ScharfSandhiArg {
 public static void main(String[] args){
     String s = args[1];
     String sopt = args[0];
     //System.out.println("args[0] = " + sopt);
     //System.out.println("args[1] = " + s);
     int err;
     if (sopt.equals("C")) {
      err=ScharfSandhi.sandhioptions("C","N","S","");
     }else if (sopt.equals("E")) {
      err=ScharfSandhi.sandhioptions("E","N","S","Y");
     } else {
       System.out.println("Sandhi option must be 'C' or 'E', not '" + sopt + "'");
       err=1;  
     }
     if (err == 0) {
	 String ans = ScharfSandhi.sandhi(s);
         System.out.println(ans);
     }
 }
}

