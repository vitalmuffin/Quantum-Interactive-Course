#!/usr/bin/env python3
"""Regression checks for robust large/dynamic equation rendering."""
from pathlib import Path
import sys
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)
core=(R/'vendor/math-core.js').read_text(); defensive=(R/'vendor/math-defensive.js').read_text(); facade=(R/'vendor/math-offline.js').read_text()
need('function normalizeTex' in core,'outer TeX delimiter normalization missing')
need('function resolveArguments' in core,'legacy/reversed render argument compatibility missing')
need('attempt<3' in core,'MathJax retry loop missing')
need('el.textContent=' in core and 'qm-math-error' in core,'readable final fallback missing')
need('renderMarked' in core,'marked equation scan API missing')
need('MutationObserver' in defensive and 'characterData' in defensive,'full defensive observer missing')
need('return core.render(first,second,third)' in facade or 'core.render' in facade,'compatibility facade missing')
for name in ['index.html','primer.html','historical_core.html','foundations_tests.html','quantum_information.html','source_reader.html']:
    text=(R/name).read_text()
    need('v=0.16' in text,f'{name}: cache-buster not current')
index=(R/'index.html').read_text(); primer=(R/'primer.html').read_text(); sr=(R/'source_reader.html').read_text()
need('window.QMMath.render(latex,el,{displayMode:display})' in index,'index large equations do not use shared renderer')
need('window.QMMath.render(latex,el,{displayMode:display})' in primer,'primer large equations do not use shared renderer')
need("window.QMMath?.render(tex,e,{displayMode:e.classList.contains('math-block')})" in sr,'source reader dynamic render call is wrong')
if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: robust large and dynamic equation rendering regressions remain fixed.')
