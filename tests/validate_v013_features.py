#!/usr/bin/env python3
"""Regression checks for mobile graph and embedded navigation behavior."""
from pathlib import Path
import re,sys
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)
need((R/'docs').is_dir(),'docs directory missing')
need(not [p for p in R.glob('*.md') if p.name!='README.md'],'documentation markdown remains at project root')
shell=(R/'vendor/course-shell.js').read_text(); styles='\n'.join(p.read_text() for p in (R/'vendor/styles').glob('*.css'))
enh=(R/'vendor/course-enhancements.js').read_text(); idx=(R/'index.html').read_text()
all_html='\n'.join(p.read_text(errors='ignore') for p in R.glob('*.html'))
need('data-role="menu"' not in shell and not re.search(r'data-role=["\']menu["\']',all_html),'redundant top Etappen button remains')
need('grid-auto-rows:50px' in styles and 'align-content:start' in styles,'stage rail rows can stretch')
need("'navigate'" in enh and "message.type==='navigate'" in enh,'embedded navigation protocol missing')
need('setupCourseLinkRouting()' in enh,'top-level course links are not routed through the middle frame')
need('template.content.cloneNode(true)' in idx,'graph SVG is reparsed with innerHTML')
need('const pointers=new Map()' in idx and 'pointers.size>=2' in idx,'mobile graph pinch/pointer handling missing')
need('suppressClickUntil' in idx,'graph drag can trigger accidental node clicks')
need('height:min(66vh,560px)' in idx,'mobile graph sizing missing')
need('0.16' in shell and '0.16' in idx,'runtime version not current')
if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: embedded navigation and mobile graph regressions remain fixed.')
