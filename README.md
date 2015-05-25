# ScharfSandhi
Software to apply sandhi to Sanskrit text.


## History
Approximately in 1992-2000, Peter Scharf [sanskritlibrary.org](http://sanskritlibrary.org/) wrote a computer program in the Pascal language to 'do sandhi'. This is the base form of the sandhi programs in this repository.

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
would be 'callable' functions. There are two primary funcitonal entry points,
`sandhioptions` and `sandhi`.  
* `sandhioptions` sets `sandhi options` using four parameters.  This is 
  similar to the question/answer format of the Pascal program. Essentially,
  one set of options is used for compound sandhi, and another set for
  external sandhi.  As I recall, there are some option combinations (perhaps
  related to isses of Vedic Sanskrit) which are not implemented in the
  translations.
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

The use of the Python version is similar.  This has been tested only with
version 2.7 of Python, but will likely work with other Python 2 versions.
* Change to the `python` directory
* python ScharfSandhiArg.py {sandhi-opt} "{string}"
  Same command-line options as for Java version

There is currently no Perl version




  