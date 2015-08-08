# coding=utf-8
""" print_identify.py 
 python print_identify.py print_identify.txt
 For each Sanskrit character, calls identify and prints the 
 isthana and iyatna 
"""
import re,sys,codecs
from  scharfsandhi import identify,sktavagraha,sktnasalization

base_alphabet="aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh" # 49
alphabet = base_alphabet + sktavagraha + sktnasalization # 51
# We ignore sktjihvamuliya, sktupadhmaniya, sktanunasika, sktroot which
# PMS mentions as being required to fill Soundary, but otherwise unused

# constants for first coord of Soundary
ikanthya = 1
italavya = 2
imurdhanya = 3
idantya = 4
iosthya = 5

# second coord of Soundary
ihrasva = 1
idirgha = 2
iguna = 3
ivrddhi = 4
isparsa1 = 5
isparsa2 = 6
isparsa3 = 7
isparsa4 = 8
isparsa5 = 9
iantahstha = 10
iusmana = 11
isthana_vals = ("?","ikanthya","italavya","imurdhanya","idantya","iosthya")
iyatna_vals=('?','ihrasva','idirgha','iguna','ivrddhi','isparsa1','isparsa2','isparsa3','isparsa4','isparsa5','iantahstha','iusmana')


def main(fileout):
 fout = codecs.open(fileout,"w","utf-8")
 firstflag=False
 save = []
 for c in alphabet:
  (isthana,iyatna) = identify(c)
  jsthana = isthana_vals[isthana]
  jyatna = iyatna_vals[iyatna]
  save.append((c,jsthana,jyatna))
 # 
 for (name,jsthana,jyatna) in save:
  fout.write("%s => %s,%s\n" %(name,jsthana,jyatna))
 print len(save),"records written to",fileout
 fout.close()
if __name__ == '__main__':
 fileout = sys.argv[1]
 main(fileout)
