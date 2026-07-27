#!/usr/bin/env python3
"""Regression checks for the content/design fixes first introduced in v0.12."""
from pathlib import Path
from bs4 import BeautifulSoup
import sys
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)
pages=[p for p in R.glob('*.html') if p.name!='progress.html']
all_html='\n'.join(p.read_text(errors='ignore') for p in pages)
for phrase in [
    'Warum hier wichtig: Dieser Begriff wird direkt im folgenden Modell verändert oder ausgewertet.',
    'Die Formelzeichen und ihre Rollen stehen direkt unter der Gleichung.',
    'Why it matters here: this concept is directly changed or evaluated in the following model.',
]: need(phrase not in all_html,f'unwanted course-design sentence remains: {phrase}')
primer=(R/'primer.html').read_text(); ps=BeautifulSoup(primer,'html.parser')
need(len(ps.select('.primer-foundation-head'))==7,'primer: expected seven foundation headers')
need(not ps.select('.primer-foundation-head p'),'primer: prerequisite blurbs remain in headings')
enh=(R/'vendor/course-enhancements.js').read_text()
for key in ['wave','superposition','probability','complex','basis','calculus','eigen']:
    need(f"id==='{key}'" in enh,f'primer visual missing: {key}')
idx=(R/'index.html').read_text()
need('function applyGraphSelection' in idx,'graph selection state missing')
need("e.target.closest('.node')" in idx,'graph node pointer handling missing')
styles='\n'.join(p.read_text() for p in (R/'vendor/styles').glob('*.css'))
need('.qm-stage-rail' in styles and '.qm-stage-number' in styles,'stage rail CSS missing')
need('qm-stage-frame' in styles and 'showFrame' in enh,'middle-view navigation missing')
need('.rail-arrow:disabled' in styles and 'buttons[0].disabled' in enh,'carousel boundary state missing')
if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: v0.12 content, graph, stage-rail, and carousel regressions remain fixed.')
