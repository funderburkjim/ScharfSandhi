"""
 ScharfSandhiArg.py  May 25, 2015
 Jul 26, 2015. 
 
"""
from scharfsandhi import ScharfSandhi

if __name__ == '__main__':
 import sys
 sopt = sys.argv[1]
 s = sys.argv[2]
 sandhi = ScharfSandhi()
 sandhi.dbg=True
 if sopt == "E":
  err=sandhi.sandhioptions("E","N","S","Y")
  soptPrint = "E,N,S,Y"
 elif sopt == "E1":
  err=sandhi.sandhioptions("E","N","S","")
  soptPrint = "E,N,S,"
 elif sopt == "C":
  err=sandhi.sandhioptions("C","N","S","")
  soptPrint = "C,N,S,"
 else:
  print "ERROR: sopt must be E, E1, or C, not",sopt
  exit(1)
 ans = sandhi.sandhi(s)
 print (ans)
