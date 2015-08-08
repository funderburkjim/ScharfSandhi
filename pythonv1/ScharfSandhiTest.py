"""
 ScharfSandhiTest.py  May 22, 2015
 Python equivalent of ScharfSandhiTest.java
 
"""
from scharfsandhi import ScharfSandhi
#ScharfSandhi.dbg=True

def testfile(filein,fileknown,sopt):
 with open(filein,"r") as f:
  lines = [l.rstrip('\r\n ') for l in f]
 with open(fileknown,"r") as f:
  correct = [l.rstrip('\r\n ') for l in f]

 if sopt == "E":
  ScharfSandhi.sandhioptions("E","N","S","Y")
  soptPrint = "E,N,S,Y"
 elif sopt == "E1":
  ScharfSandhi.sandhioptions("E","N","S","")
  soptPrint = "E,N,S,"
 elif sopt == "C":
  ScharfSandhi.sandhioptions("C","N","S","")
  soptPrint = "C,N,S,"
 else:
  print "ERROR: sopt must be E, E1, or C, not",sopt
  exit(1)

 i=0
 nok = 0
 for line in lines:
  out = ScharfSandhi.sandhi(line)
  known = correct[i]
  ok = "?"
  if out == known:
   ok = "OK"
   nok = nok+1
  else:
   ok = "PROBLEM"
   print "Problem at line",i
   print "   input:",line
   print " options:",soptPrint
   print "computed:",out
   print "standard:",known
   print "========================================"
  i = i + 1
 print "Test Results:"
 print "Input:",filein
 print "Standard:",fileknown
 print nok,"input lines were ok out of",len(lines),"total lines."

if __name__ == '__main__':
 import sys
 sopt = sys.argv[1]
 filein = sys.argv[2]
 fileknown = sys.argv[3]
 testfile(filein,fileknown,sopt)
