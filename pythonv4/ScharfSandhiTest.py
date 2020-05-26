"""
 ScharfSandhiTest.py  May 22, 2015
 Jul 20, 2015
 May 11, 2020. Revise for python3
 
"""
from scharfsandhi import ScharfSandhi

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

def testfile(filein,fileknown,sopt):
 with open(filein,"r") as f:
  lines = [l.rstrip('\r\n ') for l in f]
 with open(fileknown,"r") as f:
  correct = [l.rstrip('\r\n ') for l in f]
 sandhi = ScharfSandhi()
 err = simple_sandhioptions(sopt,sandhi)
 #err = sandhi.simple_sandhioptions(sopt)
 if err != 0: 
  print("ERROR",err," sopt must be E, E1, or C, not",sopt)
  exit(1)

 i=0
 nok = 0
 for line in lines:
  out = sandhi.sandhi(line)
  known = correct[i]
  ok = "?"
  if out == known:
   ok = "OK"
   nok = nok+1
  else:
   ok = "PROBLEM"
   print("Problem at line",i)
   print("   input:",line)
   print(" options:",sopt)
   print("computed:",out)
   print("standard:",known)
   print("========================================")
  i = i + 1
 print("Test Results:")
 print("Input:",filein)
 print("Standard:",fileknown)
 print(nok,"input lines were ok out of",len(lines),"total lines.")

if __name__ == '__main__':
 import sys
 sopt = sys.argv[1]
 filein = sys.argv[2]
 fileknown = sys.argv[3]
 testfile(filein,fileknown,sopt)
