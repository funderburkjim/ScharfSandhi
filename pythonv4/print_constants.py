# coding=utf-8
""" print_constants.py 
 python print_constants.py scharfsandhi.py print_constants.txt
 Reads the various character sets from scharfsandhi.py.  
 Prints these in a 'standardized' form, namely
 sorted in Sanskrit alphabetical order.
"""
import re,sys,codecs
import scharfsandhi

import string
# Note 'L' and '|' and 'Z' and 'V' are not present
# Not sure where they go
tranfrom="aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh"
tranto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw"
trantable = string.maketrans(tranfrom,tranto)

def slp_cmp_pairs(a,b):
 return slp_cmp(a[1],b[1]) # normalized

def slp_cmp(a,b):
 a1 = string.translate(a,trantable)
 b1 = string.translate(b,trantable)
 return cmp(a1,b1)

# Assume 'a' is list of strings
#b = sorted(a,cmp=slp_cmp)
def sortval(x):
 """ x is a string of Sanskrit characters (in slp1)
  sort the characters into alphabetical order
 """
 y = list(x) # list of strings of length 1
 z = sorted(y,cmp=slp_cmp)
 ans = ''.join(z)
 return ans

def init(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines0 = [line.rstrip('\r\n') for line in f]
 return lines0

def main(filein,fileout):
 lines=init(filein)
 print len(lines),"lines in",filein
 fout = codecs.open(fileout,"w","utf-8")
 firstflag=False
 save = []
 for line in lines:
  if line.startswith('ru'):
   firstflag=True
   print "firstflag"
  if not firstflag:
   continue
  m = re.search(r'^([a-zA-Z0-9_]+) *= *(.*)$',line)
  if not m:
   continue
  name = m.group(1)
  if name == 'maxyatna':  #stop looking here
   break
  valcode = m.group(2)
  val = getattr(scharfsandhi,name)
  save.append((name,valcode,val))
 # 
 for (name,valcode,val) in save:
  fout.write("%s = %s\n" %(name,valcode))
  fout.write("%s = %s\n" %(name,val))
  val1 = sortval(val)
  fout.write("%s = %s\n" %(name,val1))
  fout.write("\n")
 print len(save),"records written to",fileout
 fout.close()
if __name__ == '__main__':
 filein = sys.argv[1]
 fileout = sys.argv[2]
 main(filein,fileout)
