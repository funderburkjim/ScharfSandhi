# pythonv4/readme-tests

There are three parts in the documentation below:
* ScharfSandhiTest.py
* ScharfSandhiTest2.py
* comparison to Bucknell Sandhi tables

## ScharfSandhiTest.py
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

## ScharfSandhiTest2.py
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

## External sandhi comparisons to Bucknell  
Aug/Sep, 2015

The `Sanskrit Manual` by Roderick Bucknell succinctly describes external
sandhi rules in a tabular form that facilitates comparison.  Programs were
developed to do this comparison.  With very few exceptions, the analysis
shows that scharfsandhi.py computes results identical to those of Bucknell.  
See the [bucknell readme](https://github.com/funderburkjim/ScharfSandhi/tree/master/pythonv4/scharfsandhi_bucknell.md) for a description of the analysis.
