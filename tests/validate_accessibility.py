#!/usr/bin/env python3
"""Static accessibility invariants for form controls and shared interaction layers."""
from pathlib import Path
from bs4 import BeautifulSoup
import sys
R=Path(__file__).resolve().parents[1]
errors=[]
for page in sorted(R.glob('*.html')):
    soup=BeautifulSoup(page.read_text(errors='ignore'),'html.parser')
    for control in soup.find_all(['input','select','textarea']):
        if control.get('type')=='hidden' or control.has_attr('hidden'): continue
        cid=control.get('id')
        labelled=(control.get('aria-label') or control.get('aria-labelledby') or control.find_parent('label') or (cid and soup.find('label',attrs={'for':cid})))
        if not labelled: errors.append(f'{page.name}: unlabeled {control.name}#{cid or "?"}')
    for button in soup.find_all('button'):
        if button.has_attr('hidden'): continue
        name=button.get('aria-label') or button.get('aria-labelledby') or button.get('title') or button.get_text(' ',strip=True)
        image=button.find('img',alt=True)
        if not name and not image: errors.append(f'{page.name}: unnamed button {button.get("id") or button.get("class") or "?"}')
    for image in soup.find_all('img'):
        if not image.has_attr('alt'): errors.append(f'{page.name}: image without alt {image.get("src","")}')
styles='\n'.join(p.read_text() for p in (R/'vendor/styles').glob('*.css'))
shell=(R/'vendor/course-shell.js').read_text(); index=(R/'index.html').read_text()
if 'prefers-reduced-motion:reduce' not in styles: errors.append('shared CSS: reduced-motion handling missing')
if 'aria-modal="true"' not in shell or "e.key==='Tab'" not in shell: errors.append('course drawer: modal focus management missing')
if "aria-hidden','true'" not in shell or "aria-hidden','false'" not in shell: errors.append('course drawer: visibility state is not exposed')
if 'node.setAttribute("tabindex","0")' not in index: errors.append('system graph nodes are not keyboard focusable')
if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: form labels, button names, image alternatives, modal focus, graph keyboard access, and reduced motion passed.')
