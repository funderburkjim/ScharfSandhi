# coding=utf-8
""" refactor.py 
 python refactor.py ../python/scharfsandhi.py scharfsandhi.py 

"""
import re,sys,codecs

def get_class_constants(lines):
 # iclass1 is index into lines for 'class ScharfSandhi'
 # iclass2 is index into lines for first '#  variables global to sandhi routines'
 iclass1=-1
 iclass2=-1
 for i in xrange(0,len(lines)):
  line = lines[i]
  if False and ((i+1) in[68,74]):
   out = "check lines[%s]=%s" % (i+1,line)
   print out.encode('utf-8')
  if re.search(r'^class ScharfSandhi',line):
   iclass1=i
  elif re.search(r'^ #  variables global to sandhi routines',line):
   iclass2=i
   break
 if iclass1==-1:
  print "ERROR 1"
  exit(1)
 if iclass2==-1:
  print "ERROR 2"
  exit(1)
 # gather constants defined between indexes iclass1 and iclass2
 constants=[]
 # use iclass1+2 to skip 'class ScharfSandhi' and next line after
 for i in xrange(iclass1+2,iclass2):
  line = lines[i]
  m = re.search(r'^ ([^ ]+) *=',line)
  if m:
   constants.append((i,m.group(1)))
   line = re.sub(r'^ ',' #constant ',line)
   lines[i]=line
  else:
   line = re.sub(r'^ #','#keepcon',line)
   if line.startswith(' '):
    line = re.sub(r'^ ','',line)  # Soundary initialization, two lines
   lines[i]=line
   constants.append((i,''))
 return constants

def drop(i,drop_lines):
 j = i+1
 for (l,h) in drop_lines:
  if (l<=j<=h):
   return True
 return False

def init(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines0 = [line.rstrip('\r\n') for line in f]
 # line 'linmax = int()' is misplaced (line # 424)
 # it should occur after line 431
 # due to the odd encoding, we have to add 2 to the line numbers!
 lines = []
 for i in xrange(0,len(lines0)):
  line = lines0[i]
  if (i+1) == 426:
   save = line
  elif (i+1) == 433:
   lines.append(line)
   lines.append(save)
   print "check",len(lines),save
  else:
   lines.append(line)
 return lines

def refactor(filein,fileout1):
 lines=init(filein)
 print len(lines),"lines in",filein
 f1 = codecs.open(fileout1,"w","utf-8")
 constants = get_class_constants(lines)
 print len(constants)," constants found"
 outlines=[] # the refactored file
 drop_lines = [(3,14),(16,17)]
 for i in xrange(0,len(lines)):
  line = lines[i]
  if drop(i,drop_lines):
   continue
  if re.search(r'^ #constant ',line):
   continue
  if re.search(r'^#keepcon',line):
   continue
  if line.startswith('class ScharfSandhi'):
   # save this line to insert after the constants
   saveline=line
   #insert the constants here as module constants
   for (j,con) in constants:
    cline = lines[j]
    # There is something odd going on with some of the 
    # sktudattaX and sktsvaritaX lines; some encoding problem.
    # Since these are used nowhere else,  just leave them commented out
    if re.search('(sktudatta|sktsvarita)',cline):
     # for some reason, some lines are not properly read
     # leave these commented out for now
     cline = re.sub(r'^ #constant ','#constant ',cline)
    else: 
     # process normally
     if cline.startswith('#keepcon'):
      cline = re.sub('#keepcon *','',cline)
      if not cline.startswith('#'):
       cline = '# '+cline
     else:
      cline = re.sub(r'^ #constant ','',cline)
    outlines.append(cline)
   # insert saveline
   outlines.append('')
   outlines.append(saveline)
  else:
   # otherwise, just copy line
   outlines.append(line)

 # related to the sktudattaX, etc problems, two lines in outlines
 # currently are just a single double quote.  Comment these
 for i in xrange(0,len(outlines)):
  line = outlines[i]
  if line == '"':
   #outlines[i-1]=outlines[i-1]+'"'
   outlines[i]=''
 # outlines1
 # find 'class ScharfSandhi' line, and delete all subsequent lines
 #  up to '@classmethod
 outlines1=[]
 i1=-1
 for i in xrange(0,len(outlines)):
  line = outlines[i]
  if line.startswith('class ScharfSandhi'):
   outlines1.append(line)
   i1 = i+1
   break
  else:
   outlines1.append(line)
 i2 = -1
 for i in xrange(i1,len(outlines)):
  line = outlines[i]
  if line.startswith(' #  variables global to sandhi routines'):
   outlines1.append(line)
   i2 = i+1
   break
  else:
   pass  # don't append this line
 for i in xrange(i2,len(outlines)):
  line = outlines[i]
  outlines1.append(line)
 # outlines2  change 'cls.X' to 'X' for all the constants
 # first, get all the constants in a dict
 d={}
 for (j,con) in constants:
  if con != '':
   d[con]=True
 outlines2=[]
 for i in xrange(0,len(outlines1)):
  line = outlines1[i]
  if not re.search(r'cls[.]',line):
   outlines2.append(line)
   continue
  parts = re.split(r'(cls[.].+?\b)',line)
  x = [] # parts of replacement
  for part in parts:
   m = re.search(r'^cls[.](.+)$',part)
   if not m:
    x.append(part)
    continue
   c = m.group(1) 
   if c in d:
    x.append(c) # remove the cls.
   else:
    x.append(part) # presumably a class method
  newline = ''.join(x) # reconstruct the line
  outlines2.append(newline)
 # write outlines2 to f1
 for line in outlines2:
  f1.write("%s\n" %line)
 # process
 f1.close()
if __name__ == '__main__':
 filein = sys.argv[1]
 fileout1 = sys.argv[2]
 refactor(filein,fileout1)
