""" test_sandhiSplit.py
    Jul 27, 2015
    Exercise the sandhiSplit routine
    usage: python test_sandhiSplit.py test_sandhiSplit_in.txt test_sandhiSplit_out.txt

"""
from scharfsandhi import sandhiSplit
import sys,codecs

def test_sandhiSplit(filein,fileout):
 f = codecs.open(filein,"r","utf-8")
 fout = codecs.open(fileout,"w","utf-8")
 n = 0
 for line in f:
  line = line.rstrip('\r\n')
  n = n + 1
  split = sandhiSplit(line)
  outar= []
  outar.append("Case %s" % n)
  outar.append(line)
  i=0
  while (i<len(split)):
   outar.append('(%s,%s):%s' %(i,split[i],split[i+1]))
   i = i+2
  out = '\n'.join(outar)
  fout.write(out + "\n")
  out = "-"*72
  fout.write("%s\n" % out)
 f.close()
 fout.close()

if __name__ == '__main__':
 filein = sys.argv[1]
 fileout = sys.argv[2]
 test_sandhiSplit(filein,fileout)
