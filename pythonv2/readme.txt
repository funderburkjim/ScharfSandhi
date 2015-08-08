
This refactors pythonv1/scharfsandhi.py, to use normal methods (not
class methods).  This change requires some changes in the usage
 (e.g., ScharfSandhiArg.py and ScharfSandhiTest.py).

python refactor2.py ../pythonv1/scharfsandhi.py scharfsandhi.py

This passes the tests according to testsuite.sh.
