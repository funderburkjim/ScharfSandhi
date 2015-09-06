"""prep_vowel.py
 Aug 10, 2015.
 Convert External sandhi vowel rules from table in Bucknell, p. 75
 to form used by ScharfSandhiTest2.py.
 See pythonv4/notes.org
"""
# table codes Sanskrit in slp1
vowel_table="""
-a/-A:-i/-I:-u/-U:-f:-O:-E:-e:-o::C-^8
-A-:-ya-:-va-:-ra-:-Ava-:-A a-:-e '-:-o '-::a-
-A-:-yA-:-vA-:-rA-:-AvA-:-A A-:-a A-:-a A-::A-
-e-:-I-:-vi-:-ri-:-Avi-:-A i-:-a i-:-a i-::i-
-e-:-I-:-vI-:-rI-:-AvI-:-A I-:-a I-:-a I-::I-
-o-:-yu-:-U-:-ru-:-Avu-:-A u-:-a u-:-a u-::u-
-o-:-yU-:-U-:-rU-:-AvU-:-A U-:-a U-:-a U-::U-
-ar-:-yf-:-vf-:-F-:-Avf-:-A f-:-a f-:-a f-::f-
-E-:-ye-:-ve-:-re-:-Ave-:-A e-:-a e-:-a e-::e-
-E-:-yE-:-vE-:-rE-:-AvE-:-A E-:-a E-:-a E-::E-
-O-:-yo-:-vo-:-ro-:-Avo-:-A o-:-a o-:-a o-::o-
-O-:-yO-:-vO-:-rO-:-AvO-:-A O-:-a O-:-a O-::O-
"""
import re

class Case(object):
 def __init__(self,head1,head2,result):
  self.word1=head1
  self.word2=head2
  self.result=result

def parse_vowel_table(t):
 recs=[]
 lines = t.splitlines()
 lines = [l for l in lines if l.strip()!='']
 (body,dummy) = re.split(r'::',lines[0])
 headparts = re.split(r':',body) # column titles
 heads1 = []
 for part in headparts:
  # for first 3 vowels, long/short give same result. Generate 2 cases
  vowels = re.split(r'/',part)
  head1=[]
  for vowel in vowels:
   m = re.search(r'^-(.)$',vowel)
   if not m:
    print "ERROR 1. vowel=",vowel,"\nbody=",body
    exit(1)
   vowel = m.group(1)
   head1.append(vowel)
  heads1.append(head1)

 for line in lines[1:]:
  (body,head2) = re.split(r'::',line)
  m = re.search(r'^(.)-',head2)
  if not m:
   print "ERROR 4. head2=",head2,"\nline=",line
  head2=m.group(1)
  results = re.split(r':',body)
  if len(results)!=len(heads1):
   print "ERROR 2, line=",line
   exit(1)
  for i in xrange(0,len(heads1)):
   head1 = heads1[i]
   result = results[i]
   m = re.search(r'^-(.*)-$',result)
   if not m:
    print "ERROR 3",result," in line",body
    exit(1)
   result = m.group(1)
   for vowel in head1:
    case = Case(vowel,head2,result)
    recs.append(case)
 return recs

def prep_vowel(sopt,fileout):
 recs = parse_vowel_table(vowel_table)
 fout = open(fileout,"w")
 for case in recs:
  fout.write("%s:%s %s:%s\n" %(sopt,case.word1,case.word2,case.result))
 fout.close()
 print len(recs),"lines written to",fileout
if __name__ == '__main__':
 import sys
 sopt = sys.argv[1]
 fileout = sys.argv[2]
 prep_vowel(sopt,fileout)
