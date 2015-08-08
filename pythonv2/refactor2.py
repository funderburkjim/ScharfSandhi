# coding=utf-8
""" refactor2.py 
 python refactor2.py ../pythonv1/scharfsandhi.py scharfsandhi.py 

"""
import re,sys,codecs

def get_class_methods(lines):
 """ return list of (i,methname) into lines for '@classmethod' statements,
     and check that the next line is a 'def' of the class method.
 """
 methods=[]
 for i in xrange(0,len(lines)):
  line = lines[i]
  if line.startswith(' @classmethod'):
   line1 = lines[i+1]
   m = re.search(r'^ def ([a-zA-Z0-9_]*)\(cls',line1)
   if m:
    methname=m.group(1)
    methods.append((i,methname))
   else:
    print "ERROR 1:",i,line1
 return methods

def check_method_usage(methods,outlines):
 # search for unused methods
 methnames = {}
 for (i,methname) in methods:
  methnames[methname]=0
 alllines='\n'.join(outlines)
 pattern = 'self[.]([a-zA-Z0-9_]+)\('
 for m in re.finditer(pattern,alllines):
  methname = m.group(1)
  if methname not in methnames:
   print "unexpected methname=",methname
   continue
  methnames[methname] = methnames[methname]+1
 for methname in methnames:
  print methnames[methname],methname

def module_functions(methods,lines):
 inserts=[] # lines to insert as module functions
 for j in xrange(0,len(methods)):
  (i0,methname0) = methods[j]
  if methname0 not in ['sandhiSplit',  'set_memberP', 'strReplace']:
   continue
  (i1,methname1) = methods[j+1]
  for i in xrange(i0,i1):
   line = lines[i]
   line = line[1:]
   if line.startswith('def'):
    line = line.replace('(self,','(')
   inserts.append(line) # remove initial space so module function ok
   lines[i]='' # will later be removed
 outlines=[]
 # insert lines before first 'def'
 for i in xrange(0,len(lines)):
  line = lines[i]
  if line.startswith('def dbgPrint'): 
   for newline in inserts:
    outlines.append(newline)
   # then a blank line 
   outlines.append('')
  # append line
  outlines.append(line)
 # Now, change self.sandhisplit to sandhisplit, and ditto for set_memberP
 for i in xrange(0,len(outlines)):
  outlines[i] = re.sub('self[.]sandhiSplit','sandhiSplit',outlines[i])
  outlines[i] = re.sub('self[.]set_memberP','set_memberP',outlines[i])
  outlines[i] = re.sub('self[.]strReplace','strReplace',outlines[i])
 return outlines

def drop(i,drop_lines):
 j = i+1
 for (l,h) in drop_lines:
  if (l<=j<=h):
   return True
 return False

def init(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines0 = [line.rstrip('\r\n') for line in f]
 return lines0

def refactor(filein,fileout1):
 lines=init(filein)
 print len(lines),"lines in",filein
 f1 = codecs.open(fileout1,"w","utf-8")
 methods = get_class_methods(lines)
 print len(methods)," methods found"
 methlines = [i for (i,methname) in methods]
 outlines=[] # the refactored file
 for i in xrange(0,len(lines)):
  line = lines[i]
  # minor edit to some lines
  line = re.sub(r'generated source for method','method',line)
  # change 'cls.' to 'self.' for everthing, methods and variables
  line = re.sub(r'cls[.]','self.',line)
  if i in methlines:
   # exclude all lines starting with the 'main' method. 'i' is
   # the last element of methlines
   if i == methlines[-1]:
    break
   # replace lines[i] with a blank line, and
   # alter lines[i+1]
   outlines.append('')
   lines[i+1] = re.sub(r'\(cls','(self',lines[i+1])
  else:
   outlines.append(line)
 #check_method_usage(methods,outlines)
 # from this we found that init, str_trim, join, main are unused
 # also sandhioptions and sandhi are unused, but these are needed
 # as entry from client code.
 # Replace these three methods with empty lines
 # Actually, 'main' has already been deleted above
 for j in xrange(0,len(methods)):
  (i0,methname0) = methods[j]
  if methname0 not in ['init','str_trim','join']:
   continue
  (i1,methname1) = methods[j+1] # assume j is not last one
  for i in xrange(i0,i1):
   outlines[i]=''
 # There are a few functions which should be module functions rather
 # than class methods
 outlinesa = module_functions(methods,outlines)
 outlines = outlinesa
 # outlines1 - drop consecutive blank lines
 outlines1 = []
 for i in xrange(0,len(outlines)):
  line = outlines[i]
  if line == '' and outlines[i-1]=='':
   pass
  else:
   outlines1.append(line)
 # print outlines
 for line in outlines1:
  f1.write("%s\n" %line)
 f1.close()
if __name__ == '__main__':
 filein = sys.argv[1]
 fileout1 = sys.argv[2]
 refactor(filein,fileout1)
