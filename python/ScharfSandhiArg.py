"""
 ScharfSandhiArg.py  May 25, 2015
 Python equivalent of ScharfSandhiArg.java
 
"""
from scharfsandhi import ScharfSandhi

if __name__ == '__main__':
 import sys
 sopt = sys.argv[1]
 s = sys.argv[2]
 if sopt == "E":
  err=ScharfSandhi.sandhioptions("E","N","S","Y")
  soptPrint = "E,N,S,Y"
 elif sopt == "E1":
  err=ScharfSandhi.sandhioptions("E","N","S","")
  soptPrint = "E,N,S,"
 elif sopt == "C":
  err=ScharfSandhi.sandhioptions("C","N","S","")
  soptPrint = "C,N,S,"
 else:
  print "ERROR: sopt must be E, E1, or C, not",sopt
  exit(1)
 ans = ScharfSandhi.sandhi(s)
 print (ans)
