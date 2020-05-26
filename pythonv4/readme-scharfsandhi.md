## usage of scharfsandhi (pythonv4 version)

## Usage of pythonv4 version

* To be called by another program:
```
# Both scharfsandhi.py and scharfsandhiWrapper.py modules are required;
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
