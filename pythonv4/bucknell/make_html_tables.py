""" make_html_tables.py
   Prepare html tables for vowel_table and consonant_table in
   prep_vowel.py and prep_consonant.py, respectively.
   Usage: python make_html_tables.py html_tables.txt
"""
import codecs, re

vowel_table="""
-a/-A:-i/-I:-u/-U:-f:-O:-E:-e:-o::C-8
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
-O-:-yO-:-vO-:-rO-:-AvO-:-A O-:-a O-:-a o-::O-
"""

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

def superscript_number(e):
 e = re.sub(r'([0-9]+)',r'<sup>\1</sup>',e)
 return e

def make_html_row(irow,row):
 n = len(row)
 ans=[]
 ans.append(' <tr>')
 for i in xrange(0,n):
  e = row[i]
  e = superscript_number(e)
  if (irow == 0) or (i==(n-1)): # bold
   e = "<b>%s</b>" %e
  e = "  <td>%s</td>" % e
  ans.append(e)
 ans.append(' </tr>')
 return ans
  
def make_vowel_table(f):
 tablestr = vowel_table
 outarr=[]
 outarr.append('<table>')
 # Github markdown doesn't support caption
 #outarr.append('<caption>Word-final vowels</caption>')
 table = [t.strip() for t in tablestr.splitlines() if t != '']
 for i in xrange(0,len(table)):
  print i,table[i]
  rowstr = table[i]
  (bodystr,head) = re.split(r'::',rowstr)
  row = re.split(r':',bodystr)
  row.append(head)
  html_row=make_html_row(i,row)
  for x in html_row:
   outarr.append(x)
 # closing tag
 outarr.append('</table>')
 # write outarr to file
 for out in outarr:
  f.write('%s\n' % out)

def make_consonant_table(f):
 tablestr = consonant_table
 outarr=[]
 outarr.append('<table>')
 # Github markdown doesn't support caption
 #outarr.append('<caption>Word-final vowels</caption>')
 table = [t.strip() for t in tablestr.splitlines() if t != '']
 for i in xrange(0,len(table)):
  print i,table[i]
  rowstr = table[i]
  (bodystr,head) = re.split(r'::',rowstr)
  bodystr = bodystr.strip()
  row = re.split(r' +',bodystr)
  row = [x.strip() for x in row]
  row.append(head)
  html_row=make_html_row(i,row)
  for x in html_row:
   outarr.append(x)
 # closing tag
 outarr.append('</table>')
 # write outarr to file
 for out in outarr:
  f.write('%s\n' % out)

if __name__ == '__main__':
 import sys
 fileout = sys.argv[1]
 f = codecs.open(fileout,"w","utf-8")
 make_vowel_table(f)
 make_consonant_table(f)
 f.close()

