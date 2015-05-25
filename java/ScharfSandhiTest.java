import java.util.*;
import java.io.*;
/**
 * This program reads 3 parameters from command-line, performs the
   test indicated by these parameters, and prints results of the
   test to stdout.
   The 3 parameters are:
   1) abbreviated sandhi-option code:
      C = compound : sandhioptions("C","N","S","")
      E = external : sandhioptions("E","N","S","Y")
      E1= external1: sandhioptions("E","N","S","")
   2) Path to test file, which read as a sequence of lines
   3) Path to standard file, which is viewed as a sequence of lines.
      This file is generated manually.

   Here is how the tests are performed:
      Each line of the test file is viewed as a test input string 's';
      sandhi is applied to 's' to generate a new string 's1'.
      The corresponding line of the standard file is viewed as the 
      correct answer, 's2', and is compared to the generated answer 's1'.
      If the two differ, a message is printed to indicate the difference.
      If the two are the same,  1 is added to the number of 'ok' test lines.
      
      When all tests have been applied, output is logged to indicate the total
      number of tests and the number of tests that passed.
      
      
 * 
 */
public class ScharfSandhiTest {
    //private static String dir = "scharfsandhitest/testfiles";
    //private static String dir = "testfiles";
 //
 private static void testFile(String filein,String fileknown,String sopt){
  String filename = filein;
  //System.out.println("dir="+dir);
  ArrayList<String> lines = loadFile(filename);
  int len = lines.size();
//  System.out.println(len+" lines in "+filename);
  String fileout = fileknown;
  ArrayList<String> correct = loadFile(fileout);
  String soptPrint="";
  if (sopt.equals("E")) {
   ScharfSandhi.sandhioptions("E","N","S","Y");
   soptPrint = "E,N,S,Y";
  }else if (sopt.equals("E1")) {
   ScharfSandhi.sandhioptions("E","N","S","");
   soptPrint = "E,N,S,";
  }else if (sopt.equals("C")) {
   ScharfSandhi.sandhioptions("C","N","S","");
   soptPrint = "C,N,S,";
  }else {
   System.out.println("ERROR: sopt must be E or C, not " + sopt);
   System.exit(1);
  }
  Iterator it = lines.iterator();
  int i=0;
  int nok=0;
  while(it.hasNext()){
   String in = (String) it.next();
   in = in.trim();
   String out = ScharfSandhi.sandhi(in);
   String known = correct.get(i);
   known = known.trim();
   String ok="?";
   if (out.equals(known)) {
    ok="OK";
    nok++;
   }else {
    ok="PROBLEM";
    System.out.println("Problem at line "+i);
    System.out.println("   input:"+in);
    System.out.println(" options:"+soptPrint);
    System.out.println("computed:"+out);
    System.out.println("standard:"+known);
    System.out.println("========================================");
   }
   i++;
  }
  System.out.println("Test Results:");
  System.out.println("Input: "+filein);
  System.out.println("Standard: "+fileknown);
  System.out.println(nok +" input lines were ok out of " + len + " total lines.");
 }
 public static void main(String[] args){
     String sopt = args[0];
     String filein = args[1];
     String fileknown = args[2];
     testFile(filein,fileknown,sopt);
     //testFile("TestIn.txt","TestOut.txt","E");
     //testFile("Testnn.txt","TestnnOut.txt","E1");
     //testFile("TestSandhiC.txt","TestSandhiCOut.txt","C");
     //testFile("PascalSandhiTest3-nl.txt","PascalSandhiTest3S-nl.txt","C");
 }
 public static ArrayList loadFile(String fileName)
    {
        if ((fileName == null) || (fileName.equals("")))
            throw new IllegalArgumentException();

        String line;
        ArrayList file = new ArrayList();

        try
        {
            BufferedReader in = new BufferedReader(new FileReader(fileName));

            if (!in.ready())
                throw new IOException();

            while ((line = in.readLine()) != null)
                file.add(line);

            in.close();
        }
        catch (IOException e)
        {
            System.out.println(e);
            return null;
        }

        return file;
    }
}
