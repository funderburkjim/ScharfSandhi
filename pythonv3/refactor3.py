# coding=utf-8
""" refactor3.py 
 python refactor3.py ../pythonv2/scharfsandhi.py scharfsandhi.py 

"""
import re,sys,codecs


def get_class_methods(lines):
 """ return list of (i,methname) into lines for '@classmethod' statements,
     and check that the next line is a 'def' of the class method.
 """
 methods=[]
 inclass=False
 for i in xrange(0,len(lines)):
  line = lines[i]
  if line.startswith('class ScharfSandhi'):
   inclass=True
   continue
  if not inclass:
   continue
  if line.startswith(' def '):
   m = re.search(r'^ def ([a-zA-Z0-9_]*)\(self',line)
   if m:
    methname=m.group(1)
    methods.append((i,methname))
   else:
    print "ERROR 1:",i,line
 return methods

def add_init_method(lines):
 # assume this is done AFTER the @wrapper decorators
 outlines=[]
 inclass=False
 for i in xrange(0,len(lines)):
  line = lines[i]
  # Change int(), bool(), str() to more standard constants
  line = line.replace(r'int()','0')
  line = line.replace(r'bool()','False')
  line = line.replace(r'str()','""')
  if line.startswith('class ScharfSandhi'):
   inclass=True
   outlines.append(line)
   firstmeth=False
   outlines.append('')
   outlines.append(' def __init__(self):')
   continue
  if not inclass:
   outlines.append(line)
   continue
  # now line is in the ScharfSandhi class definition
  if (not firstmeth) and (line.startswith(' @wrapper')):
    firstmeth = True
    outlines.append(line)
    continue
  if (not firstmeth):
   # insert a line of __init__
   # If a constant assignment, ' X = Y' change to ' self.X = Y'
   line = re.sub(r'^ ([a-zA-Z0-9]+) +=',' self.\g<1> =',line)
   # indent one extra space
   line = ' ' + line;
   # Change int(), bool(), str() to more standard constants
   #line = line.replace(r'int()','0')
   #line = line.replace(r'bool()','False')
   #line = line.replace(r'str()','""')
   outlines.append(line)
  else:  # everything else in class
   outlines.append(line)
 return outlines

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



def init(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines0 = [line.rstrip('\r\n') for line in f]
 return lines0

def insert_wrapper(lines,methods):
 methlines = [i for (i,methname) in methods]
 outlines=[] # the refactored file Add wrapper decorator
 for i in xrange(0,len(lines)):
  line = lines[i]
  if line == 'import re':
   # insert wrapper import
   outlines.append('from wrapper import wrapper')
  elif i in methlines:
   # insert decorator, before the method definition
   outlines.append(' @wrapper')
  #always insert the original line
  outlines.append(line)
 return outlines

def remove_chk(lines):
 outlines=[]
 # 1. remove chk_point method (assume it's the last method)
 j=-1
 for i in xrange(0,len(lines)):
  line = lines[i]
  if line.startswith(r' def chk_point'):
   j = i-1
   break
 for i in xrange(0,j):
  outlines.append(lines[i])
 # 2. remove calls to chk_point
 for i in xrange(0,len(outlines)):
  line = outlines[i]
  if re.search(r'self[.]chk_point',line):
   # special case in method namohrasvad.  A final 'else' clause
   # contains just a sequence of self.chk_point calls.
   # The 'else:' is at index 1420, and the first chk_point is 1421
   #print "DBG, lines[%s]=%s" % (i,lines[i])
   if i == 1421:
    outlines[i-1]='' # remove the 'else:' line
   outlines[i]=''
 # 3. Also, remove calls to dbgPrint 
 for i in xrange(0,len(outlines)):
  line = outlines[i]
  if re.search(r'dbgPrint',line):
   if line.startswith('def dbgPrint'):
    # delete the 3 lines of definition
    for j in xrange(0,3):
     outlines[i+j]=''
   else:
    # delete the call to dbgPrint
    outlines[i]=''
 # 4. Also, remove some debug print statements
 for i in xrange(0,len(outlines)):
  line = outlines[i]
  if line.startswith('   print "substrary:'):
   # delete this line and prev line (if self.dbg)
   outlines[i-1]=''
   outlines[i]=''
  elif line.startswith('   print "sandhiPrep:'):
   # delete this line, prev. line and next 2 lines
   for j in xrange(-1,3):
    outlines[i+j]=''
  elif line.startswith('   print "WARNING: insertary:'):
   outlines[i]=''
  elif line.startswith('    print "Turning on debug. '):
   outlines[i]=''
  elif line.startswith('    print "Turning off debug.'):
   outlines[i]=''
  elif line.startswith('   print "Sandhi error: " '):
   outlines[i]=''
  elif line.startswith('    print "label7000b(1) '):
   # delete this line and prev line (if self.dbg)
   outlines[i-1]=''
   outlines[i]=''
 return outlines

def remove_misc(lines):
 outlines=[]
 remove=[
  "  This Java method replaces the characters in a substring of this",
  "    StringBuffer with characters in the specified String.",
  " # char[] ax = x.toCharArray();",
  " #b = list(x)",
  " # b = b.replace(idx1, idx2, y)",
  "'' # list[] # ArrayList()",
  " #  String sanskrit_str = \"- 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|/\";",
  " #HashSet(sanskrit_strs_list)",
  '  # Java x.split("") has empty string as first element of return',
  "   StringBuffer()",
  " #c = str()",
  "    #y.append(c)",
  " #.append(c)",
  " # (str(y))",
  " #.append(c)",
  " #temp = a.toArray()",
  " #l = len(temp)",
  ' #ans = " " # ejf[None]*l',
  " #i = 0",
  " #while i < l:",
  " # ans[i] = str(a.get(i))",
  " # i += 1",
  " #return ans",
  "# * These are Strings of length 1, so could have been declared 'char'",
  "# * However, it was felt that treating them as String objects was conceptually",
  "# * simpler, and probably insignificantly less efficient.",
  "# (ejf)What is 'CAntaPadary' supposed to be? It is coded as sets of chars",
  "# The string is populated in init_CAntaPadary",
  "# Since the Sanskrit characters are represented as Java Strings,",
  "# the 'union' of sets may be uniformly represented with Java '+'",
  "# concatentaion of Strings.",
  " In conversion to Perl,",
  "# it was convenient to construct these initialially and",
  "# given then new names.",
  "# private static final String[] Pradi = new String[1+pradimax];",
  '#Soundary = " "*maxsthana # ejf [None]*1 + maxsthana',
  "  # = new String[1+linmax]; #",
  "# resolves to 0 in Python",
  "# Resolves to empty string in Python",
  "  #  usu. max len pratipadmax",
  "  # Resolves to False in Python",
  " # \"\"  Java is String FldChr, whose (default) value is 'null'",
  "  #  June 2010. Not reset.",
  "  #Answer = str()",
  "     # if self.dbg:  // ejf commented out",
  "  # error in conversion to Java  if (IEnd == 0){return 0;}",
  '   #print "insertary: Augmenting Linary: linmax starts as ", self.linmax,len(self.Linary)',
  '   #print "Linary=",self.Linary',
  '   #print "s1=\'%s\'"% s1',
  '   #print "s1 length=",len(s1)',
  '   #print "s1 length (after padding)=",len(s1)',
  '   #self.Linary = list(s1) #s1.split("")',
  '   #print "new length of Linary=",len(self.Linary)',
  '   #print "s1 length=",len(s1)',
  '   #print "linmax now = ",self.linmax',
  '   #print "IEnd now = ",IEnd',
  " #StringBuffer()",
  "  #ans = str(Tempstr)",
  " #  REPLACE exit(sandhi);",
  "  # print \"kharachk: '\" + Linary[Index - 1] + \"', '\"+Linary[Index + 1]+\"'\" ;",
  " #  type = boolean;",
  '  #self.Linary = s1.split("")',
  "  #self.Linary = list(s1)",
  '  # Java adds an empty string at the beginning with s1.split("")',
  '  #print "sandhi1: s=%s, s1=%s" %(s,s1)',
  '  #print "Linary=[" + ",".join(self.Linary) + "]"',
  '   # print "Index="+Index;',
  "     # ejf: Dhralopa is global",
  "   Print an informative message if there is an error.",
  r"  #  the doubling '\\' is a Java quirk of string literals",
  r'  #p1 = Pattern.compile("^(\\s+)(.*)$")',
  r'  #p2 = Pattern.compile("(.*?)(\\s+)")',
  "  # ScharfSandhi.java doesn't have '^','$'",
  "  #m = Matcher()",
  " #p2.matcher(x)",
  ". # self.Pada1.substring(L - 1, L)"
 ]
 replaces = [
  ('  @param fldch','  @param fldch  Always None, never used'),
  ('  self.FldChr = None','  self.FldChr = None # Never changed.')
 ]
 for i in xrange(0,len(lines)):
  line = lines[i]
  for r in remove:
   line = line.replace(r,'') # replace by empty string
  for (r,s) in replaces:
   line = line.replace(r,s)
  outlines.append(line)
 return outlines

def remove_extra_empty(lines):
 outlines=[]
 outlines.append(lines[0])
 for i in xrange(1,len(lines)):
  line = lines[i]
  if (line == '') and (lines[i-1]==''):
   continue
  outlines.append(line)
 return outlines

def refactor(filein,fileout1):
 lines=init(filein)
 print len(lines),"lines in",filein
 f1 = codecs.open(fileout1,"w","utf-8")
 # add __init__ method to ScharfSandhi, and put the initialization of
 # class constants therein
 methods = get_class_methods(lines)
 print len(methods)," methods found"
 outlines = insert_wrapper(lines,methods)
 # construct __init__ method for ScharfSandhi class
 outlines1 = add_init_method(outlines)
 # remove the 'chk_point' lines
 outlines2 = remove_chk(outlines1)
 # remove misc strings (whole or partial lines)
 outlines3 = remove_misc(outlines2)
 # replace multiple blank lines with just one blank line
 outlines4 = remove_extra_empty(outlines3)
 # print result
 for line in outlines4:
  f1.write("%s\n" %line)
 f1.close()
if __name__ == '__main__':
 filein = sys.argv[1]
 fileout1 = sys.argv[2]
 refactor(filein,fileout1)
