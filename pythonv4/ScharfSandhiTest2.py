"""
 ScharfSandhiTest2.py  
 Aug 9, 2015
 Read one file. Each line has a test, represented in 3 colon-separated
 Print output to stdout
 fields.
  field1 =  (sandhi options, usu. C or E)
  field2 = input of the test
  field3 = expected output of the test
 May 11, 2020. Change print statements for python3 
"""
from scharfsandhi import ScharfSandhi
import re

def simple_sandhioptions(code,sandhi):
  if (code == 'C'):
   sandhi.sandhioptions("C","N","S","")
  elif (code == 'E'):
   sandhi.sandhioptions("E","N","S","Y")
  elif (code == 'E1'):
   sandhi.sandhioptions("E","N","S","")
  elif (code == 'E2'):
   sandhi.sandhioptions("E","N","S","Y")
   sandhi.lopah_v=True
  else:
   sandhi.Error = 5
  return sandhi.Error

class Case(object):
 def __init__(self,line):
  line = line.rstrip('') # remove ending whitespace
  self.line=line
  (self.sopt,self.input,self.answer) = re.split(r':',line)

def testfile2(filein):
 with open(filein,"r") as f:
  cases = [Case(l.rstrip('\r\n ')) for l in f]
 sandhi = ScharfSandhi()

 i=0
 nok = 0
 icase=0
 for case in cases:
  icase=icase+1
  (sopt,line,known) = (case.sopt,case.input,case.answer)
  err = simple_sandhioptions(sopt,sandhi)
  #err = sandhi.simple_sandhioptions(sopt)
  if err != 0: 
   print("ERROR",err," sopt must be E, E1, E2, or C, not",sopt)
   print("line",icase,"of file",filein)
   exit(1)
  out = sandhi.sandhi(line)
  ok = "?"
  if out == known:
   ok = "OK"
   nok = nok+1
  else:
   ok = "PROBLEM"
   print("Problem at case",i)
   print(" options:",sopt)
   print("   input:",line)
   print("computed:",out)
   print("standard:",known)
   print("========================================")
  i = i + 1
 print("Test Results for file:",filein)
 print(nok,"input case were ok out of",len(cases),"total cases.")

if __name__ == '__main__':
 import sys
 filein = sys.argv[1]
 testfile2(filein)
