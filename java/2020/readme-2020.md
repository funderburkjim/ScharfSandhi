## Scharf revisions to the java code January 2020

(in the following, 'I' == Peter Scharf)

I have revised the Scharf Sandhi Java routines by adding several subroutines to handle sandhi where there is a following S.  I also fixed nasalized l to have tilde following rather than preceding in accordance with SLP1.
Both a command-line program ScharfSandhiArg and a function ScharfSandhiArgFunction now take three arguments:
1. E/C external or compound sandhi
2. Y/N despace or not
3. The string to which to do sandhi
```
Input	Desired output
tasmAt liKati	tasmAlliKati
tasmin liKati	tasmil~liKati	[tilde after l = nasalized l]
tasmAt Socati	tasmAcCocati
tasmin Socati	tasmiYCocati	[C not S]
tasmAt SfRoti	tasmAcCfRoti
tasmin SfRoti	tasmiYCfRoti	[C not S]
tasmAt SlAGaH	tasmAcClAGaH	[C not S]
tasmin SlAGaH	tasmiYClAGaH	[C not S]
```

```
Sutras	Subroutines added
8.3.28.  NRoH kukwuk Sari	nnohkuktuksari
8.3.31.  Si tuk	situk
8.4.40 stoH ScunA ScuH	stohscunascuh
8.4.63 vt. 964 chatvamamIti vaktavyam	chatvamami
8.4.65 Jaro Jari savarRe	jharojharisavarne
```

A note on the comparison with Bucknell.  His sandhi of tasmin liKati > tasmiM liKati:

In scharfsandhi_bucknell.md Funderburk summarize the differences in comparison of Buknell sandhi with ScharfSandhi on lines 419--427.  The revised java program gives the same results as Bucknell for footnotes 1, 2, and 4.  Footnote 3 produces the same result as the nasalized l option of Bucknell.  The other option, namely, n l -> M l (Bucknell) is not correct.  I suspect that Bucknell wrote candrabindu l as the result mimicking a common fault of Devanagari typeface: putting the candrabindu on the preceding vowel instead of on the consonant l.  This is just a fault of limited font flexibility and not a correct sandhi.

## Future work
It would now be desirable to bring these revisions to the Java into the latest Python.  A comparison of the old java with the revised would reveal the precise revisions to the java.  I did not insert the detailed options for these revisions I had put in the original Pascal code however.  I just wrote the code assuming the standard package of options for external sandhi.

