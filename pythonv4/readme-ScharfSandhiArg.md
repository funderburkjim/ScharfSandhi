## ScharfSandhiArg.py program  (pythonv4 version)
This program provides a 
simple but relatively flexible way to experiment with the sandhi transformations. 

It is a command-line program, which should be run in a terminal.

To use the python version, you need to have python installed.
The current version has been tested  with version 3 of Python language.


* python ScharfSandhiArg.py {sandhi-opt} {despace-opt} "{string}"
  The answer will be printed to the terminal
  *  sandhi-opt: 
    * C (Compound Sandhi)  Use hyphen '-' to separate compound fragments
    * E (External Sandhi)  use space ' ' to separate words
  * despace-opt:  Relevant only for External Sandhi
    * N (or "") default.  Space separators are retained
    * Y Space separators are not retained, in some circumstances.
      (i.e., the output is `de-spaced`).
  * string:  Code Sanskrit in SLP1 transliteration. Use '-' and ' ' as noted
* History output.  As written, the python version of ScharfSandhiArg generates a
  'trace' of the sandhi functions used.

## Examples
```
python ScharfSandhiArg.py E N 'rAmaH gacCati'
sandhi: START: "rAmaH gacCati"
sandhimain: START: "rAmaH gacCati"
visargaprep: "rAmas gacCati"
atororhasica: "rAmo gacCati"
sandhimain: DONE: "rAmo gacCati"
sandhi: DONE: "rAmo gacCati"
ScharfSandhiArg: ans="rAmo gacCati"

```

```
python ScharfSandhiArg.py E Y 'tasmAt gaRAt'
sandhi: START: "tasmAt gaRAt"
sandhimain: START: "tasmAt gaRAt"
jhalamjasonte: "tasmAd gaRAt"
non_acsandhi: "tasmAd gaRAt"
sandhimain: DONE: "tasmAdgaRAt"
sandhi: DONE: "tasmAdgaRAt"
ScharfSandhiArg: ans="tasmAdgaRAt"

```

```
python ScharfSandhiArg.py C '' 'tat-rAmaH'
sandhi: START: "tat-rAmaH"
sandhimain: START: "tat-rAmaH"
jhalamjasonte: "tad-rAmaH"
non_acsandhi: "tad-rAmaH"
sandhimain: DONE: "tadrAmaH"
sandhi: DONE: "tadrAmaH"
ScharfSandhiArg: ans="tadrAmaH"
```

```
python ScharfSandhiArg.py 'C' 'N' 'deva-fzi'
sandhi: START: "deva-fzi"
sandhimain: START: "deva-fzi"
adgunah: "deva-rzi"
sandhimain: DONE: "devarzi"
sandhi: DONE: "devarzi"
ScharfSandhiArg: ans="devarzi"
```
