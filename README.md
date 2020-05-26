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
    sandhi transformation .
  * ScharfSandhiString.java is a second simple command-line program, that
    applies compound sandhi and then external sandhi to an input string
* `java/2020` contains revised ScharfSandhi.java and ScharfSandhiArg.java as described in sandhiRepairs.txt
  * As of May 25, 2020,  there is a slight incompatibility between ScharfSandhiArg.java and the python4 version.
  * See [readme.md](https://github.com/funderburkjim/ScharfSandhi/tree/master/java/2020/). 
    
* `python` contains the translation to Python.
  * This is the FIRST translation to Python.  It is written for version 2 of the Python language (Python2.7)
  * scharfsandhi.py is the Python module.  It was generated from the Java code.
  * ScharfSandhiTest.py, testlog.txt, and testsuite.sh are Python analogs of 
    the tests, as described above.
  * ScharfSandhiArg.py is the Python analogue of ScharfSandhiArg.java.
  * `sh testsuite.sh` runs the various tests with this version.
    * this version requires python2 and uses TestSandhiCOutv0.txt. Ref [#5](https://github.com/funderburkjim/ScharfSandhi/issues/5).

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

* `pythonv1` refactors programs in `python`
   This passes the tests according to testsuite.sh.  Ref [#5](https://github.com/funderburkjim/ScharfSandhi/issues/5).
* `pythonv2` refactors programs in `pythonv1`
  This passes the tests according to testsuite.sh.  Ref [#5](https://github.com/funderburkjim/ScharfSandhi/issues/5).
* `pythonv3` refactors programs in `pythonv2`
  This passes the tests according to testsuite.sh.  Ref [#5](https://github.com/funderburkjim/ScharfSandhi/issues/5).
* **pythonv4**  This is the latest python version. [see](https://github.com/funderburkjim/ScharfSandhi/blob/master/pythonv4/readme.md)
  * now compatible with python3 (version 3 of the Python language)
  * slight adjustment of the 'standard' regarding test suites.  Ref [#6](https://github.com/funderburkjim/ScharfSandhi/issues/6).
  * [Reference]

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
simple but relatively flexible way to experiment with the sandhi transformations.

For Java versions, see:
* https://github.com/funderburkjim/ScharfSandhi/tree/master/java
* https://github.com/funderburkjim/ScharfSandhi/tree/master/java/2020  

For latest python version, see [readme-ScharfSandhiArg](https://github.com/funderburkjim/ScharfSandhi/tree/master/pythonv4/readme-ScharfSandhiArg.md)

There is currently no Perl version of ScharfSandhiArg.

## TODO 
See [readme-todo.md](https://github.com/funderburkjim/ScharfSandhi/tree/master/readme-todo.md) for some thoughts on
additional possible additional improvements.




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

