## ScharfSandhi/readme-todo.md


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
