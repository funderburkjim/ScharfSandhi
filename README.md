# ScharfSandhi
Software to apply sandhi to Sanskrit text.


## History
Approximately in 1992-2000, Peter Scharf [sanskritlibrary.org](http://sanskritlibrary.org/) wrote a computer program in the Pascal language to 'do sandhi'. This is the base form of the sandhi programs in this repository. See also
[paniniSandhi](http://sanskritlibrary.org/software/paniniSandhi.html).

In 2009, I (Jim Funderburk) translated the Pascal programs to first Perl and
then to Java.  Recently (May 2015), I further translated the Java sandhi programs to Python (version 2.7).

Scharf developed a 'test suite' for the Pascal version, and this (with perhaps a few additional tests) is accessible to the Perl, Java, and Python programs.
Currently, I do not know how to run the original Pascal program;  the 
translated programs work in current computer environments.

## Descriptions of Directories
* `PMSPascal` contains Scharf's Pascal programs, as a collection of 6 files,
   with two versions of one of the files.

* `perl` contains the translation to Perl:
  * sandhi.pm is the Perl module containing the translation of all of 
    Scharf's Pascal code.
  * scharfsandhitest.pl contains a program used for testing sandhi.pm
  * testsuite.sh  is a Bash script which applies the scharfsandhitest.pl 
    test program using the files in the `testfiles` directory (see below)
  * testlog.txt shows the stdout output of testsuite.sh

* `java` contains the translation to Java:
  * ScharfSandhi.java is the Java source code for the Java class containing
    a translation of Pascal code.
  * ScharfSandhiTest.java, testsuite.sh, and testlog.txt are Java versions as
    described above
  * ScharfSandhiArg.java is a simple command-line program that can do one
    sandhi transformation (See below).
  * ScharfSandhiString.java is a second simple command-line program, that
    applies compound sandhi and then external sandhi to an input string
  * The 2020 directory contains revised ScharfSandhi.java and ScharfSandhiArg.java as described in sandhiRepairs.txt

* `Python` contains the translation to Python.
  * scharfsandhi.py is the Python module.  It was generated from the Java code.
  * ScharfSandhiTest.py, testlog.txt, and testsuite.sh are Python analogs of 
    the tests, as described above.
  * ScharfSandhiArg.py is the Python analogue of ScharfSandhiArg.java.

* `testfiles`  contains 4 pairs of files. In each pair of files, the two
   files contain the same number of lines; when sandhi is applied to a line
   of the first file, the result should be the corresponding line of the
   second file.  Also, as discussed below, some details of sandhi application
   depend on certain `sandhi options` (basically, compound sandhi or 
   external sandhi). 
  * Compound sandhi: PascalSandhiTest3-nl.txt, PascalSandhiTest3S-nl.txt
  * Compound sandhi: TestSandhiC.txt, TestSandhiCOut.txt
  * External sandhi: TestIn.txt, TestOut.txt
  * External sandhi variant: Testnn.txt, TestnnOut.txt

* See the `Further Work` section below 

## Current status of tests
The Java and Python versions 'pass' all the tests of the testsuite.
The Perl program passes *almost all* of the tests.
Currently, I am not interested in discovering how the Perl program differs
from the Java and Python versions.

## Very brief description of the programs
The Pascal program was written as a command-line program. A user would first
set various `sandhi options` by answering a sequence of questions. Then, 
lines of text would be read from a file, and, after application of sandhi,
would be written to another file.

The conversions of the Pascal program were written so that the sandhi function
would be 'callable'. There are two primary funcitonal entry points,
`sandhioptions` and `sandhi`.  
* `sandhioptions` sets `sandhi options` using four parameters.  This is 
  similar to the question/answer format of the Pascal program. Essentially,
  one set of options is used for compound sandhi, and another set for
  external sandhi.  As I recall, there are some option combinations (perhaps
  related to isses of Vedic Sanskrit) which are present in the Pascal program
  but not implemented in the translations.
* `sandhi`  which takes one string (line) of Sanskrit text, transforms the
  string according to the current sandhi options, and returns the transformed
  string.   The Sanskrit text is assumed to be presented in the SLP1 
  transliteration scheme developed by Scharf.

## ScharfSandhiArg program
This program, available in both Java and Python versions, provides a 
simple but relatively flexible way to experiment with the sandhi transformations. Each is a command-line program, which should be run in a terminal.

To use the Java version, you need to have a Java runtime installed.
* change to the `java` directory
* java ScharfSandhiArg {sandhi-opt} "{string}"
  The answer will be printed to the terminal
  *  sandhi-opt : 
    * C (Compound Sandhi)  Use hyphen '-' to separate compound fragments
    * E (External Sandhi)  use space ' ' to separate words
  * string:  Code Sanskrit in SLP1 transliteration. Use '-' and ' ' as noted
* 2020/ScharfSandhiArg.java is designed to be called as a function, for example from XSLT.

The use of the Python version is similar.  This has been tested only with
version 2.7 of Python, but will likely work with other Python 2 versions.
* Change to the `python` directory
* python ScharfSandhiArg.py {sandhi-opt} "{string}"
  Same command-line options as for Java version
* Example 1:
  * python ScharfSandhiArg.py E "sitA ca rAmaH ca agacCatAm"
  * sitA ca rAmaScAgacCatAm
* Example 2:
  * python ScharfSandhiArg.py C "aDas-upAsana"
  * aDaupAsana

There is currently no Perl version of ScharfSandhiArg.

## TODO 
The current programs are functional, and ready to use.
Of the versions available, I am most interested in doing further work with
the Python version.  
* The Python version was constructed in a two step process:
  * scharfsandhi.py was first constructed from ScharfSandhi.java using the
    java2python module: https://github.com/natural/java2python
  * This conversion was incomplete in several ways.  By manual tinkering,
    the current version came about.
* As a byproduct, there are many awkward aspects of scharfsandhi.py:
  * Many of Peter's comments were moved, and need to be put where they belong.
  * Most routines are written as class functions, but need to be rewritten
    as normal class methods.  
* The 'logic' is quite complicated, and hard to understand.  For such an
  important functionality as sandhi computations,  a clear documentation 
  is desireable.
* This documentation should include a fuller understanding of the import of
  the sandhi options.
* Some of the sandhi options available in the Pascal version may be missing
  in the Java and Python versions. I think there are still other option choices
  that are not implemented. (e.g., compound sandhi niH-sanDi -> nissanDi, but
  maybe also niHsanDi is a valid option).
* The test coverage is extensive, but is it complete?
  Tests of each individual routine is a goal.
* It should be able to extend the functionality so that sandhi can be
  applied in other contexts, notably that of combining stems and endings in
  inflections (declensions, conjugations).  
* Bucknell describes sandhi in a quite different way, which may be amenable
  to programmatic implementation. 
* The program can be used to generate 'inverse sandhi' data. Scharf and I 
  briefly worked on this at one time.  This should be brought into this form.
* The program currently requires SLP1 data. Existing transcoding routines
  can be incorporated so that sandhi of Devanagari text is easy.



## Further Work

### August/Sep 2015 pythonv4 

Directories pythonv1, pythonv2, pythonv3 and pythonv4 refine the Python
version.  The versions in pythonv1, pythonv2, and pythonv3 are created by
a 'refactor' program.  The intentions are:
* reposition the comments which the java2python conversion misplaced
* Change class methods to class instance methods
* Represent many class constants as module constants
* Add a 'wrapper' decorator to the instance methods.  This wrapper can
  be used to provide 'history' information.

All of these first three versions should be viewed as intermediate steps
with probably little independent interest now that they are completed.
They all give the same results to the testsuite as does the initial version
in the python directory.

The pythonv4 version of scharfsandhi.py began with the pythonv3 version, and
was changed manually in many ways. For the most part, these changes 
involved adding comments to the methods.  However,  some refactoring was
also done to make the extremely complex logic somewhat less complex.
In a small number of spots, some details were changed by way of corrections.
These are mentioned in the notes.org file, and will be further mentioned
in the Issues.

### Usage of pythonv4 version

* To be called by another program:
```
# Both scharfsandhi.py and scharfsandhiWrapper.py modules are require;
# the latter is imported by the former and provides a Python 'decorator'.
# See discussion of ScharfSandhiArg.py for more on the wrapper decorator.
# ScharfSandhi is a class implementing the sandhi methods.
from scharfsandhi import ScharfSandhi
# instantiate the class
sandhi = ScharfSandhi()
# Options control various details of the sandhi logic.  Some useful
# collections of these options are provided by the
# simple_sandhioptions method, which takes one argument, a string, which
# as of this writing (Sep 6, 2015) should be one of:
# C compound sandhi, applied at the '-' separator
# E External sandhi, applied at the ' ' (space) separator
# E1 A variant of External sandhi
# E2 Another variant of External sandhi, tailored to agree with Bucknell
# So, for instance:
err = sandhi.simple_sandhioptions('E2')  # non-zero code indicates code problem
# Now, apply sandhi to whatever Sanskrit strings are of interest.
# The Sanskrit must be encoded in the SLP1 transliteration.
# For instance,
s = 'rAmaH gacCati'
s1 = sandhi.sandhi(s)  # answer: rAmo gacCati
```

* ScharfSandhiArg.py
  This command-line program does a single example, 
  given a sandhi option and a string.
  For instance:
```
$ python ScharfSandhiArg.py 'E' 'rAmaH gacCati'
sandhi: START: "rAmaH gacCati"
sandhimain: START: "rAmaH gacCati"
visargaprep: "rAmas gacCati"
atororhasica: "rAmo gacCati"
sandhimain: DONE: "rAmo gacCati"
sandhi: DONE: "rAmo gacCati"
ScharfSandhiArg: ans="rAmo gacCati"

$ python ScharfSandhiArg.py 'C' 'deva-fzi'
sandhi: START: "deva-fzi"
sandhimain: START: "deva-fzi"
adgunah: "deva-rzi"
sandhimain: DONE: "devarzi"
sandhi: DONE: "devarzi"
ScharfSandhiArg: ans="devarzi"
```
 The output shows us that the `visargaprep` method changes the
 visarga 'H' to 's' at the end of 'rAmaH', and then
 the method 'atororhasica' changes 'rAmas' to 'rAmo'.
 This information is provided by the particular choice of the Python
 decorator function 'wrapper' in module scharfsandhiWrapper.py.
 I hope to enhance this wrapper into a pedogical tools to help myself
 and others better understand the way Paninian grammer is thinking of
 the sandhi process.

* ScharfSandhiTest.py
This program permits testing of a batch of known examples.  Several 
instances of it are in the shell script testsuite.sh.

The usage is as follows:

```
python ScharfSandhiTest.py <sandhioption> <input> <answer>
where
<sandhioption> is one of the simple sandhi options mentioned above (C, E, etc.)
<input> is a text file of examples, one per line, to which the particular
   sandhi option is to be applied
<answer> is a text file of answers, one per line.  Applying the particular
  sandhi option to a given line from <input> should give the result shown
  on the corresponding line of from <answer>
The two files, <input> and <answer>, must be supplied by the user.
Information regarding sucessful and unsuccessful test results is printed
to stdout.
```

* ScharfSandhiTest2.py
This provides an alternate method for batch testing of the sandhi methods.
The usage is as follows:

```
python ScharfSandhiTest2.py <testfile>
where <testfile> is a file of lines with a test and its result on each line.
The format of a line is that of three colon-delimited fields:
<sandhioption>:<test>:<answer>
where,
<sandhioption> is one of the simple sandhi options (C, E, etc.)
<test> is the example to which the sandhi option is to be applied
<answer> is the desired result of applying the sandhi option to the example.

Results are printed to stdout.

This program was used to compare scharfsandhi to Bucknell's table. For
instance,
$ python ScharfSandhiTest2.py bucknell/vowel_test2.txt > bucknell/log_vowel_tes
t2.txt

The test file, in this case vowel_test2.txt, was constructed by another
program, using Bucknell's tables.

```

### External sandhi comparisons to Bucknell  (
Aug/Sep, 2015

The `Sanskrit Manual` by Roderick Bucknell succinctly describes external
sandhi rules in a tabular form that facilitates comparison.  Programs were
developed to do this comparison.  With very few exceptions, the analysis
shows that scharfsandhi.py computes results identical to those of Bucknell.  
See the [bucknell readme](https://github.com/funderburkjim/ScharfSandhi/tree/master/pythonv4/scharfsandhi_bucknell.md) for a description of the analysis.

### Scharf revisions to the java code January 2020
I have revised the Scharf Sandhi Java routines by adding several subroutines to handle sandhi where there is a following S.  I also fixed nasalized l to have tilde following rather than preceding in accordance with SLP1.

Input	Desired output
tasmAt liKati	tasmAlliKati
tasmin liKati	tasmil~liKati	[tilde after l = nasalized l]
tasmAt Socati	tasmAcCocati
tasmin Socati	tasmiYCocati	[C not S]
tasmAt SfRoti	tasmAcCfRoti
tasmin SfRoti	tasmiYCfRoti	[C not S]
tasmAt SlAGaH	tasmAcClAGaH	[C not S]
tasmin SlAGaH	tasmiYClAGaH	[C not S]

Sutras	Subroutines added
8.3.28.  NRoH kukwuk Sari	nnohkuktuksari
8.3.31.  Si tuk	situk
8.4.40 stoH ScunA ScuH	stohscunascuh
8.4.63 vt. 964 chatvamamIti vaktavyam	chatvamami
8.4.65 Jaro Jari savarRe	jharojharisavarne

A note on the comparison with Bucknell.  His sandhi of tasmin liKati > tasmiM liKati:

In scharfsandhi_bucknell.md Funderburk summarize the differences in comparison of Buknell sandhi with ScharfSandhi on lines 419--427.  The revised java program gives the same results as Bucknell for footnotes 1, 2, and 4.  Footnote 3 produces the same result as the nasalized l option of Bucknell.  The other option, namely, n l -> M l (Bucknell) is not correct.  I suspect that Bucknell wrote candrabindu l as the result mimicking a common fault of Devanagari typeface: putting the candrabindu on the preceding vowel instead of on the consonant l.  This is just a fault of limited font flexibility and not a correct sandhi.

# Future work
It would now be desirable to bring these revisions to the Java into the latest Python.  A comparison of the old java with the revised would reveal the precise revisions to the java.  I did not insert the detailed options for these revisions I had put in the original Pascal code however.  I just wrote the code assuming the standard package of options for external sandhi.

