"""
 ScharfSandhiArg.py  May 25, 2015
 Jul 26, 2015. 
 Jul 27, 2015
 9 May 2020 PMS added parenthesis for python 3 compatibility
"""
from scharfsandhi import ScharfSandhi

if __name__ == '__main__':
 import sys
 sopt = sys.argv[1]
 s = sys.argv[2]
 sandhi = ScharfSandhi()
 sandhi.history=[] # init history.  It is modified by wrapper
 sandhi.dbg=True
 err = sandhi.simple_sandhioptions(sopt)
 if err != 0:
  print("ERROR: sopt must be E, E1, or C, not",sopt)
  exit(1)
 ans = sandhi.sandhi(s)
 for h in sandhi.history:
  print(h)
 print('ScharfSandhiArg: ans="%s"' % ans)
