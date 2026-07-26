#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
EN=set("the and of to in is that for with as by from this are be or which an on was were it we can not have has had when where if into their these those more between while through only such also than then its our one two all any first second results equation theory quantum state states wave probability particle particles energy system measurement paper section physical".split())
DE=set("der die das und ist von zu in mit für auf ein eine einer eines als auch wird werden wurde wurden durch aus bei nach sich nicht oder sind den dem des im am zum zur über zwischen diese dieser diesem diesen dass wenn wobei sowie kann können hat haben vor ihre ihr ihren seiner deren damit welche welcher welches".split())

def score(path):
    text=path.read_text(errors='ignore')
    text=re.sub(r'```.*?```|`[^`]*`|\$\$.*?\$\$|\$[^$]*\$',' ',text,flags=re.S)
    words=re.findall(r'[A-Za-zÄÖÜäöüß]+',text.lower())
    en=sum(w in EN for w in words); de=sum(w in DE for w in words)
    english_sentences=0
    for sent in re.split(r'(?<=[.!?])\s+',text):
        ws=re.findall(r'[A-Za-zÄÖÜäöüß]+',sent.lower())
        if len(ws)>8 and sum(w in EN for w in ws)>=4 and sum(w in DE for w in ws)<=1:
            english_sentences+=1
    return en/(en+de or 1),english_sentences

bad=[]
for pattern in ('summaries/*/summary_german.md','sources/*/text_german.md'):
    for path in ROOT.glob(pattern):
        ratio,sents=score(path)
        if ratio>.55 or sents>=3:bad.append((path.relative_to(ROOT),ratio,sents))
if bad:
    for p,r,s in bad:print(f'FAIL {p}: English ratio={r:.3f}, English sentences={s}')
    sys.exit(1)
print('OK: no German translation file contains a dominant or repeated English passage.')
