#!/usr/bin/env python3
from pathlib import Path
import sys

R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)

math=(R/'vendor/math-offline.js').read_text(encoding='utf-8')
need('function normalizeTex' in math,'outer TeX delimiter normalization missing')
need('function resolveArguments' in math,'legacy/reversed render argument compatibility missing')
need('for(let attempt=0;attempt<3;attempt++)' in math,'MathJax retry loop missing')
need('MutationObserver' in math and 'renderMarked(document)' in math,'dynamic formula rescanning missing')
need("return render(first,second,third)" in math,'temml compatibility adapter does not return render promise')
need("el.textContent=`\\\\[${tex}\\\\]`" in math,'readable final fallback missing')

pages=['index.html','primer.html','historical_core.html','foundations_tests.html','quantum_information.html','source_reader.html']
for name in pages:
    text=(R/name).read_text(encoding='utf-8')
    need('vendor/mathjax-tex-svg-full.js?v=0.15' in text,f'{name}: cache-busted MathJax bundle missing')
    need('vendor/math-offline.js?v=0.15' in text,f'{name}: cache-busted shared math adapter missing')
    need('v0.15' in text or name=='index.html',f'{name}: visible version not updated')

index=(R/'index.html').read_text(encoding='utf-8')
primer=(R/'primer.html').read_text(encoding='utf-8')
sr=(R/'source_reader.html').read_text(encoding='utf-8')
need('window.QMMath.render(latex,el,{displayMode:display})' in index,'index large equations do not use shared renderer')
need('window.QMMath.render(latex,el,{displayMode:display})' in primer,'primer large equations do not use shared renderer')
need("window.QMMath?.render(tex,e,{displayMode:e.classList.contains('math-block')})" in sr,'source reader still calls renderer with wrong argument order')
need((R/'docs/RELEASE_NOTES_v0.15.md').exists(),'v0.15 release notes missing')
need((R/'docs/VALIDATION_REPORT_v0.15.md').exists(),'v0.15 validation report missing')

if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: v0.15 dynamic and large-equation rendering checks passed.')
