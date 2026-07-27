#!/usr/bin/env python3
"""Regression checks for the v0.17 primer and interaction corrections."""
from __future__ import annotations
import re, sys
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)

primer=(R/'primer.html').read_text(encoding='utf-8')
enh=(R/'vendor/course-enhancements.js').read_text(encoding='utf-8')
api=(R/'vendor/page-api.js').read_text(encoding='utf-8')
css=(R/'vendor/styles/learning.css').read_text(encoding='utf-8')
soup=BeautifulSoup(primer,'html.parser')

# Wave graph: frequency changes must not derive the spatial phase from absolute time.
need('wavePhase' in primer and 'waveLastFrame' in primer,'phase-continuous wave state missing')
need('waveRun:false' in primer and 'id="wavePlay" type="button">Animation starten' in primer,'wave demonstration does not start paused')
need('state.waveTime' not in primer,'obsolete absolute wave time still causes frequency jumps')
need('fixedX/L-phase-f*tau' in primer,'relative time trace does not use frequency as repetition density')
need('state.wavePhase=(state.wavePhase+(+$("#freq").value)*dt*.42)%1' in primer,'wave phase is not integrated continuously')

# Wave packet: all curves must use the same scale and the total must be a literal sum.
need('const yScale=h*.36/maxSum' in primer,'wave packet common vertical scale missing')
need('py=h/2-vals[i]*yScale' in primer and 'py=h/2-sum[i]*yScale' in primer,'components and sum do not share one scale')
need('sum[i]+=v' in primer,'wave-packet pointwise summation missing')

# Foundation mini-plots are generated from actual functions, not hand-drawn approximations.
need('sampledPath(Math.sin)' in enh and 'sampledPath(Math.cos)' in enh,'sine/cosine plots are not sampled mathematically')
need('y0=125' in enh and 'yScale=80' in enh and 'M45 45H685M45 205H685' in enh,'sine and cosine do not share the centred −1…+1 scale')
need('const f=x=>.65*Math.sin(x)' in enh and 'const g=x=>.45*Math.sin(2*x+Math.PI/3)' in enh,'superposition components are not explicit functions')
need('sum=sampledPath(x=>f(x)+g(x),scale)' in enh,'red superposition curve is not computed as f(x)+g(x)')

# Complex plane starts from Cartesian components and derives polar data.
complex_section=soup.select_one('#complex')
need(complex_section is not None,'complex section missing')
need(complex_section.select_one('#realPart') is not None and complex_section.select_one('#imagPart') is not None,'real/imaginary component controls missing')
need(complex_section.select_one('#rotationDetails') is not None and not complex_section.select_one('#rotationDetails').has_attr('open'),'rotation is not an optional collapsed extension')
need(complex_section.select_one('#angle2').get('value')=='0','optional rotation does not start at zero')
need(complex_section.select_one('#radius') is None and complex_section.select_one('#angle') is None,'old radius/phase controls remain')
need('Math.hypot(a,b)' in primer and 'Math.atan2(b,a)' in primer,'magnitude and phase are not derived from a and b')
need('ctx.lineTo(ox+a*scale,oy)' in primer and 'ctx.lineTo(ox+a*scale,oy-b*scale)' in primer,'Cartesian component construction is not drawn explicitly')
need(r'i&=\sqrt{-1}' in primer and 'i=√(−1)' in primer,'definition i = sqrt(-1) is missing')
need('x²=−1 besitzt die beiden Lösungen +i und −i' in primer,'±i qualification is missing from the German primer')

# Range controls: larger thumbs plus a shared Pointer Events fallback.
need('function enhanceRange(input)' in api and "input.setPointerCapture" in api,'shared draggable-range fallback missing')
need("input.dispatchEvent(new Event('input'" in api and "input.dispatchEvent(new Event('change'" in api,'range fallback does not emit standard events')
need('input[type="range"]::-webkit-slider-thumb' in css and 'input[type="range"]::-moz-range-thumb' in css,'cross-browser range thumb styling missing')
need('touch-action:none' in css and 'width:22px' in css,'range touch handling or target size missing')

# Arrowheads are deliberately smaller in both static SVGs and canvases.
need('markerWidth="5.5"' in enh and 'markerHeight="5.5"' in enh,'foundation SVG arrowheads were not reduced')
need('Math.min(8,width*2)' in primer,'canvas arrowheads were not reduced')

# Cache/version coherence.
for page in R.glob('*.html'):
    text=page.read_text(encoding='utf-8')
    need('?v=0.16' not in text,f'{page.name}: stale v0.16 cache buster')

if errors:
    print('\n'.join('FAIL '+e for e in errors));sys.exit(1)
print('OK: v0.17 centred trigonometric plots, exact superposition, phase-continuous waves, Cartesian complex controls, draggable ranges, and smaller arrowheads passed.')
