"""prep_consonant.py
 Aug 10, 2015.
 Convert External sandhi consonant rules from table in Bucknell, p. 74
 to form used by ScharfSandhiTest2.py.
 See pythonv4/notes.org
"""
# table codes Sanskrit in slp1
consonant_table="""
k  w  t  p  N  m  n  aH  AH  iH1 IH2::0
k  w  t  p  N  M  n  aH3 AH3 iH3 IH3::k K p P z s
k  w  c* p  N  M  Y* aH3 AH3 iH3 IH3::S {*S->C}4 {*S->C}
k  w  c  p  N  M  MS aS  AS  iS  IS ::c C
k  w  w  p  N  M  Mz az  Az  iz  Iz ::w W
k  w  t  p  N  M  Ms as  As  is  Is ::t T
g  q  d  b  N  M  n  o   A   I   I  ::r
g  q  d  b  N  M  n  o   A   ir  Ir ::g G d D b B y v
g  q  j  b  N  M  Y  o   A   ir  Ir ::j J
g  q  q  b  N  M  R  o   A   ir  Ir ::q Q
g  q  l  b  N  M  M5 o   A   ir  Ir ::l
g* q* d* b* N  M  n  o   A   ir  Ir ::h {*h->G} {*h->Q} {*h->D} {*h->B}
N  R  n  m  N  M  n  o   A   ir  Ir ::n m
g  q  d  b  N6 m  n6 o*  A   ir  Ir ::a {*a->'}
g  q  d  b  N6 m  n6 a   A   ir  Ir ::A i I u U f O E e o
"""
import re

class Case(object):
 def __init__(self,head1,head2,result,result2=None):
  self.word1=head1
  self.word2=head2
  # the space is consistent with sopt=E1.
  if result2:
   self.result2=result2
  else:
   self.result2 = head2
  self.result="%s %s" %(result,self.result2)  

def parse_consonant_table(t):
 recs=[]
 lines = t.splitlines()
 lines = [l for l in lines if l.strip()!='']
 # first line
 (body,dummy) = re.split(r'::',lines[0])
 headparts = re.split(r' +',body) # column titles
 
 heads1 = []
 for part in headparts:
  if part == 'iH1':
   head1 = ['iH','uH']
  elif part == 'IH2':
   head1 = ['IH','UH','eH','oH','EH','OH']
  else:
   head1 = [part]
  heads1.append(head1)
 print heads1
 
 for line in lines[1:]:
  (body,head2str) = re.split(r'::',line)
  heads2 = re.split(r' +',head2str.strip())
  results = re.split(r' +',body.strip())
  if len(results)!=len(heads1):
   print "ERROR 2, line=",line
   print len(results),len(heads1)
   exit(1)
  (linedict,heads2alt) = generate_line_dict(heads2,results)
  for i in xrange(0,len(heads1)):
   head1list = heads1[i]
   result = results[i]
   cases = generate_cases(head1list,heads2alt,result,linedict)
   for case in cases:
    recs.append(case)
 return recs

def generate_line_dict(heads2,results):
 """
 """
 d = {}
 keys = [r[0] for r in results if r.endswith('*')]
 values = []
 h = heads2[0]
 heads2alt = [h]
 for x in heads2[1:]:
  # does x have form {*h->.} ?
  m = re.search(r'^\{\*%s->(.)\}'%h,x)
  if m:
   # yes. m.group(1) is next value
   values.append(m.group(1))
  else:
   # just a normal alternate head2
   # actually, never occurs if there are '*'
   heads2alt.append(x)
 if len(keys) != len(values):
  print "generate_line_dict ERROR"
  print "heads2=",heads2
  print "results=",results
  print "keys=",keys
  print "values=",values
  exit(1)
 for i in xrange(0,len(keys)):  # usually, no cases
  d[keys[i]] = values[i]
 #if len(keys)>0: # dbg
 # print "heads2=",heads2
 # print "heads2alt=",heads2alt
 return (d,heads2alt)

def generate_cases(head1list,heads2,result,linedict):
 cases=[]
 head1multiFlag = (len(head1list)>1)
 for head1 in head1list:
  for head2 in heads2:
   m = re.search(r'([1-9])$',result)
   if m:
    # indicates optional results. Ignore these for now
    result = re.sub(r'([1-9])$','',result)
   if head1multiFlag:
    # in table, iH1, iH2.
    # result is shown as iX or IX.
    # alter result so first letter matches first letter of head1
    x = head1[0] # first letter of head1
    y = result[0] # first letter of result
    if (x in ['i','u']) and (y == 'I'): # case of head2='r'
     x = x.upper()
    result = x + result[1:]
   if result.endswith('*'):
    word2 = linedict[result[0]]
    result= re.sub(r'[*]$','',result)
    case = Case(head1,head2,result,result2=word2)
   else:
    case = Case(head1,head2,result)
   cases.append(case)
 return cases

def prep_consonant(sopt,fileout):
 recs = parse_consonant_table(consonant_table)
 fout = open(fileout,"w")
 for case in recs:
  fout.write("%s:%s %s:%s\n" %(sopt,case.word1,case.word2,case.result))
 fout.close()
 print len(recs),"lines written to",fileout
if __name__ == '__main__':
 import sys
 sopt = sys.argv[1]
 fileout = sys.argv[2]
 prep_consonant(sopt,fileout)
