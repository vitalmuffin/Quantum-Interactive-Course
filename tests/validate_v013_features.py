#!/usr/bin/env python3
from pathlib import Path
import re,sys
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)

need((R/'docs').is_dir(),'docs directory missing')
need((R/'docs/RELEASE_NOTES_v0.13.md').exists(),'v0.13 release notes missing')
need(not [p for p in R.glob('*.md') if p.name!='README.md'],'documentation markdown remains at project root')

shell=(R/'vendor/course-shell.js').read_text()
css=(R/'vendor/course-shell.css').read_text()
enh=(R/'vendor/course-enhancements.js').read_text()
idx=(R/'index.html').read_text()
all_html='\n'.join(p.read_text(errors='ignore') for p in R.glob('*.html'))
need('data-role="menu"' not in shell,'course-shell still creates top Etappen button')
need(not re.search(r'data-role=["\']menu["\']',all_html),'static top Etappen button remains')
need('align-content:start' in css and 'grid-auto-rows:50px' in css,'stage rail rows are still stretched')
need("type:'qm-embedded-navigate'" in enh and "d.type==='qm-embedded-navigate'" in enh,'embedded links are not routed to parent shell')
need('setupCourseLinkRouting()' in enh,'top-level course links are not routed through middle frame')
need('template.content.cloneNode(true)' in idx,'graph SVG is still reparsed with innerHTML')
need('const pointers=new Map()' in idx and 'pointers.size>=2' in idx,'mobile graph pinch/pointer handling missing')
need('suppressClickUntil' in idx,'graph drag can still trigger accidental node clicks')
need('height:min(66vh,560px)' in idx,'mobile graph sizing missing')
need(('v0.13' in shell or 'v0.14' in shell) and ('v0.13' in idx or 'v0.14' in idx),'runtime version not updated')
if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: v0.13 navigation, layout, mobile graph, and folder-structure checks passed.')
