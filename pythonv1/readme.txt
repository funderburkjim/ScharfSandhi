
First refactoring of scharfsandhi.py
python refactor.py ../python/scharfsandhi.py scharfsandhi.py 

This refactoring still passes all the tests of testsuite.sh.

Basically, this refactoring changes to module variables 
all the CONSTANTS definied in class ScharfSandhi.  Thus, they may
be referened without the 'cls.' prefix.

One odd thing encountered were the values for sktudattau and sktsvaritau.
The solution was to comment out all the sktudattaX and sktsvartaX constants,
as these are not used elsewhere.

It might be useful to see if any of the other constants are unused.
