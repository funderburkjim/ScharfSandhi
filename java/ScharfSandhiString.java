
import java.util.*;
import java.io.*;
//import org.sanskritlibrary.scharfsandhi.*;

import java.util.*;
import java.io.*;
/**
 *
 * @author Jim Funderburk
 * 
 */
public class ScharfSandhiString {
 public static void main(String[] args){
     String sin = args[0];
     // do compound sandhi first
     ScharfSandhi.sandhioptions("C","N","S","");
     String sout = ScharfSandhi.sandhi(sin);
     // do external sandhi
     ScharfSandhi.sandhioptions("E","N","S","Y");
     String sout1 = ScharfSandhi.sandhi(sout);
     // print result to console
     System.out.println(sout1 + "\n");
 }
}