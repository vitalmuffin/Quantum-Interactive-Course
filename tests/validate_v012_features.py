#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup
import json,re,sys
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)

pages=[]
for p in R.glob('*.html'):
    s=p.read_text(errors='ignore')
    if 'vendor/course-shell.js' in s:
        pages.append(p)
        need('vendor/course-enhancements.js' in s,f'{p.name}: missing course-enhancements.js')

all_html='\n'.join(p.read_text(errors='ignore') for p in R.glob('*.html'))
for phrase in [
    'Warum hier wichtig: Dieser Begriff wird direkt im folgenden Modell verändert oder ausgewertet.',
    'Die Formelzeichen und ihre Rollen stehen direkt unter der Gleichung.',
    'Why it matters here: this concept is directly changed or evaluated in the following model.',
]:need(phrase not in all_html,f'unwanted meta sentence remains: {phrase}')

primer=(R/'primer.html').read_text()
ps=BeautifulSoup(primer,'html.parser')
need(len(ps.select('.primer-foundation-head'))==7,'primer: expected seven foundation headers')
need(not ps.select('.primer-foundation-head p'),'primer: course-design prerequisite blurbs remain')
for key in ['wave','superposition','probability','complex','basis','calculus','eigen']:
    need(f"id==='{key}'" in (R/'vendor/course-enhancements.js').read_text(),f'primer visual missing: {key}')

idx=(R/'index.html').read_text()
need('function applyGraphSelection' in idx,'graph selection state missing')
need("e.target.closest('.node')" in idx,'graph node pointer handling missing')
need('.map-layout>.explorer,.map-layout>.detail' in idx,'equal-height graph/detail layout missing')

shell=(R/'vendor/course-shell.css').read_text()
enh=(R/'vendor/course-enhancements.js').read_text()
need('.qm-stage-rail' in shell and '.qm-stage-number' in shell,'persistent stage rail CSS missing')
need('qm-stage-frame' in shell and 'showFrame' in enh,'partial middle-view navigation missing')
need('.rail-arrow:disabled' in shell and 'buttons[0].disabled' in enh,'carousel boundary state missing')
need("setupFoundationVisuals();setupCarouselArrows();setupEmbeddedBridge()" in enh,'embedded content enhancements missing')

sr=(R/'source_reader.html').read_text()
need('window.QMMath?.render' in sr,'source equation renderer is not using the shared math renderer')
need('.translation-warning' in sr,'translation warning UI missing')
need('@media(max-width:900px)' in sr and '.tabs{position:sticky' in sr,'mobile source navigation CSS missing')
need('vendor/mathjax-tex-svg-full.js' in sr,'local SVG MathJax missing in source reader')

for name in ['index.html','primer.html','historical_core.html','foundations_tests.html','quantum_information.html']:
    text=(R/name).read_text()
    need('vendor/mathjax-tex-svg-full.js' in text,f'{name}: local MathJax missing')
    need('cdn.jsdelivr.net/npm/temml' not in text,f'{name}: remote Temml remains')

flagged={
'09_1925_Heisenberg_Quantum_Reinterpretation_EN',
'15_1926_Born_Collision_Processes_Probability_EN',
'16_1927_Heisenberg_Physical_Content_Uncertainty_EN'}
data=json.loads((R/'data/source_index.json').read_text())
for p in data['papers']:
    if p['folder'] in flagged:
        need(p.get('source_file_language')=='en',f"{p['folder']}: source language not corrected")
        need(p.get('original_work_language')=='de',f"{p['folder']}: original work language not retained")
        need(p.get('german_translation_available') is False,f"{p['folder']}: German full-text status not corrected")
        for rel in [p['summary_de_path'],p['german_path']]:
            t=(R/rel).read_text().lower()
            need('previous automated file' not in t,f'{rel}: English note remains')
            need(sum(t.count(w) for w in [' der ',' die ',' und ',' ist '])>20,f'{rel}: does not look German')

if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print(f'OK: v0.12 feature checks passed for {len(pages)} shell pages.')
