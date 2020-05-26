# ScharfSandhi
Software to apply sandhi to Sanskrit text.


## History
Approximately in 1992-2000, Peter Scharf [sanskritlibrary.org](http://sanskritlibrary.org/) wrote a computer program in the Pascal language to 'do sandhi'. This is the base form of the sandhi programs in this repository. See also
[paniniSandhi](https://sanskritlibrary.org/software/paniniSandhi.html).

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
  * See [readme-2020](https://github.com/funderburkjim/ScharfSandhi/tree/master/java/2020/readme-2020.md) for Scharf's notes on the January 2020 changes.
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
* [**pythonv4**](https://github.com/funderburkjim/ScharfSandhi/blob/master/pythonv4/readme.md) is the latest python version.
  * now compatible with python3 (version 3 of the Python language)
  * See [readme-tests](https://github.com/funderburkjim/ScharfSandhi/tree/master/pythonv4/readme-tests.md).
  * slight adjustment of the 'standard' regarding test suites.  Ref [#6](https://github.com/funderburkjim/ScharfSandhi/issues/6).

## Current status of tests
The Java and Python versions 'pass' all the tests of the testsuite.
The Perl program passes *almost all* of the tests.
Currently, I am not interested in discovering how the Perl program differs
from the Java and Python versions.
Some variations to the 'standard' were made so that the pythonv4 tests would *pass*.

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

