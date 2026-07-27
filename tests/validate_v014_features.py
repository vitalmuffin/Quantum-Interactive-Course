#!/usr/bin/env python3
"""Regression checks for local MathJax and mobile off-canvas navigation."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)
bundle=R/'vendor/mathjax-tex-svg-full.js'
need(bundle.exists() and bundle.stat().st_size>1_000_000,'self-contained MathJax SVG bundle missing')
core=(R/'vendor/math-core.js').read_text(); defensive=(R/'vendor/math-defensive.js').read_text(); facade=(R/'vendor/math-offline.js').read_text()
need('tex2svgPromise' in core and 'startup?.promise' in core,'MathJax readiness/rendering missing')
need('qm-math-error' in core,'math fallback state missing')
need('MutationObserver' in defensive,'defensive dynamic formula handling missing')
need('config.modes' in facade and 'defaultMode' in facade and 'setMode' in facade,'selectable math modes missing')
version=json.loads((R/'data/course.config.json').read_text(encoding='utf-8'))['courseVersion']
pages=['index.html','primer.html','historical_core.html','foundations_tests.html','quantum_information.html','source_reader.html']
for name in pages:
    text=(R/name).read_text()
    for asset in [f'vendor/mathjax-tex-svg-full.js?v={version}',f'vendor/math-core.js?v={version}',f'vendor/math-defensive.js?v={version}',f'vendor/math-offline.js?v={version}']:
        need(asset in text,f'{name}: missing {asset}')
styles='\n'.join(p.read_text() for p in (R/'vendor/styles').glob('*.css'))
enh=(R/'vendor/course-enhancements.js').read_text()
for token in ['.qm-stage-mobile-trigger','.qm-stage-scrim','transform:translateX(-104%)','transform:translateX(0)']:
    need(token in styles,f'mobile rail CSS missing {token}')
need("mobileTrigger=document.createElement('button')" in enh and "railScrim=document.createElement('button')" in enh,'mobile rail controls not created')
need('setExpanded(innerWidth<=760?false:' in enh,'mobile rail does not start collapsed')
if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: local MathJax and mobile off-canvas regressions remain fixed.')
