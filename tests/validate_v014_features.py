#!/usr/bin/env python3
from pathlib import Path
import re,sys
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)

bundle=R/'vendor/mathjax-tex-svg-full.js'
need(bundle.exists() and bundle.stat().st_size>1_000_000,'self-contained MathJax 3 SVG bundle missing')
need(not (R/'vendor/MathJax').exists(),'obsolete MathJax 2 directory remains')
math=(R/'vendor/math-offline.js').read_text(encoding='utf-8')
need('tex2svgPromise' in math,'dynamic TeX-to-SVG rendering missing')
need('startup?.promise' in math,'MathJax startup synchronization missing')
need('qm-math-error' in math,'math failure state missing')

pages=['index.html','primer.html','historical_core.html','foundations_tests.html','quantum_information.html','source_reader.html']
for name in pages:
    t=(R/name).read_text(encoding='utf-8')
    need('vendor/mathjax-tex-svg-full.js' in t,f'{name}: MathJax 3 bundle missing')
    need('vendor/math-offline.js' in t,f'{name}: shared math adapter missing')
    need('MathJax.Hub' not in t,f'{name}: active MathJax 2 API remains')

sr=(R/'source_reader.html').read_text(encoding='utf-8')
need('window.QMMath?.render' in sr,'source reader does not render dynamic equations directly')
need("script.type=e.classList.contains('math-block')" not in sr,'source reader still creates MathJax 2 script nodes')

css=(R/'vendor/course-shell.css').read_text(encoding='utf-8')
enh=(R/'vendor/course-enhancements.js').read_text(encoding='utf-8')
need('.qm-stage-mobile-trigger' in css and '.qm-stage-scrim' in css,'mobile off-canvas controls missing')
need('padding-left:0!important' in css,'mobile content does not recover full width')
need('transform:translateX(-104%)' in css and 'transform:translateX(0)' in css,'mobile rail is not off canvas')
need('.qm-stage-frame{left:0!important;width:100%!important}' in css,'embedded mobile content does not use full width')
need("mobileTrigger=document.createElement('button')" in enh,'mobile stage trigger is not created')
need("railScrim=document.createElement('button')" in enh,'mobile rail scrim is not created')
need('setExpanded(innerWidth<=760?false:' in enh,'mobile rail does not start collapsed')
need('v0.14' in (R/'index.html').read_text(encoding='utf-8'),'course version not updated')
need((R/'docs/RELEASE_NOTES_v0.14.md').exists(),'v0.14 release notes missing')

if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: v0.14 mobile off-canvas navigation and MathJax 3 checks passed.')
