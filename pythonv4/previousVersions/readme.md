# previous versions of various files.

## scharfsandhiPreSandhiRepairs.py
  Version of scharfsandhi.py at 
  Almost the same as scharfsandhi.py at commit 0cfbe848  of Fri May 8, 2020.

  scharfsandhiPreSandhiRepairs.py has python3 compatibility adjustments 

git show 0cfbe848582e58a1da6d488bb1dcb2ff6fbffe7e:../scharfsandhi.py > temp.py

diff -w scharfsandhiPreSandhiRepairs.py temp.py

```
229c229
< CAntaPadary = ["" for x in range(0,cantamax+1)]
---
> CAntaPadary = ["" for x in xrange(0,cantamax+1)]
260c260
< Pradi = [" " for x in range(0,27+1)]
---
> Pradi = [" " for x in xrange(0,27+1)]
418,419c418,419
< for i in range(0,1+maxsthana):
<  Soundary.append(['' for j in range(0,1+maxyatna)])
---
> for i in xrange(0,1+maxsthana):
>  Soundary.append(['' for j in xrange(0,1+maxyatna)])
2089,2090c2089,2090
<    print("Linary=",self.Linary)
<    for j in range(0,len(self.Linary)):
---
>    print "Linary=",self.Linary
>    for j in xrange(0,len(self.Linary)):
2094c2094
<    print("sandhimain, j0=",j0)
---
>    print "sandhimain, j0=",j0
```

## scharfsandhiSingleOpt.py
Same as scharfsandhi.py at commit 3ff9768986c9f72f7dfac5ebea0df6aad5000b99

git show 3ff9768986c9f72f7dfac5ebea0df6aad5000b99:../scharfsandhi.py > temp.py

diff -w scharfsandhiSingleOpt.py temp.py

`No output. files are identical`

## ScharfSandhiArgSingleOpt.py
Same as ScharfSandhiArg.py at commit 93b44f1c7aa8612974838e61b312e1243c12cb31

git show 93b44f1c7aa8612974838e61b312e1243c12cb31:../ScharfSandhiArg.py > temp.py

diff -w ScharfSandhiArgSingleOpt.py temp.py

`No output. files are identical`
