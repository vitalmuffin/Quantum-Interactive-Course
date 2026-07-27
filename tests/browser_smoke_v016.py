#!/usr/bin/env python3
"""Real Chromium smoke tests that do not depend on local URL navigation.

The environment used to build this archive may block http://localhost and file://
through a browser policy. These tests therefore use Playwright's set_content and
inject the real first-party scripts and local MathJax bundle. They still execute
actual DOM, CSS, MutationObserver, FormData, SVG rendering, and mobile layout.
"""
from __future__ import annotations
import asyncio,sys
from pathlib import Path
from playwright.async_api import async_playwright
R=Path(__file__).resolve().parents[1]
CHROMIUM='/usr/bin/chromium'

async def add_scripts(page,names):
    for name in names:
        await page.add_script_tag(path=str(R/name))

async def add_course_css(page):
    for name in ['tokens.css','shell.css','learning.css','rail.css','math.css']:
        await page.add_style_tag(path=str(R/'vendor/styles'/name))

async def math_mode(browser,mode):
    page=await browser.new_page(viewport={'width':900,'height':700})
    errors=[]
    page.on('pageerror',lambda e: errors.append(str(e)))
    await page.set_content('''<!doctype html><html lang="de"><body>
      <div id="small" class="math" data-tex="E=h\\nu"></div>
      <div id="large" class="math-block" data-tex="\\[B_\\lambda(T)=\\frac{2hc^2}{\\lambda^5}\\frac{1}{\\exp(hc/(\\lambda kT))-1}\\]"></div>
      <div id="dynamic-root"></div>
    </body></html>''')
    await page.add_script_tag(content=f"window.QM_COURSE_CONFIG={{math:{{defaultMode:'{mode}',modes:['explicit','hybrid','defensive'],queryParameter:'math'}}}}")
    await add_scripts(page,['vendor/mathjax-tex-svg-full.js','vendor/math-core.js','vendor/math-defensive.js','vendor/math-offline.js'])
    await page.wait_for_function("document.querySelectorAll('mjx-container svg').length>=2",timeout=30000)
    if mode!='explicit':
        await page.evaluate("""() => {const el=document.createElement('div');el.className='math-block';el.dataset.tex='\\\\psi(x,t)=\\\\sum_{n=1}^{N}A_n\\\\cos(k_nx-\\\\omega_nt)';document.querySelector('#dynamic-root').append(el)}""")
        await page.wait_for_function("document.querySelector('#dynamic-root mjx-container svg')",timeout=15000)
    else:
        await page.evaluate("""async () => {const el=document.createElement('div');el.className='math-block';el.dataset.tex='\\\\psi(x,t)=\\\\sum_{n=1}^{N}A_n\\\\cos(k_nx-\\\\omega_nt)';document.querySelector('#dynamic-root').append(el);await window.QMMath.renderMarked(el)}""")
        await page.wait_for_function("document.querySelector('#dynamic-root mjx-container svg')",timeout=15000)
    rendered=await page.locator('mjx-container svg').count()
    active=await page.evaluate('window.QMMath.mode')
    await page.close()
    if errors: raise AssertionError(f'{mode} page errors: {errors}')
    if rendered<3 or active!=mode: raise AssertionError(f'{mode}: rendered={rendered}, active={active}')

async def shell_fixture(browser,viewport):
    page=await browser.new_page(viewport=viewport)
    errors=[]
    page.on('pageerror',lambda e: errors.append(str(e)))
    page.on('console',lambda m: errors.append(m.text) if m.type=='error' else None)
    await page.set_content('''<!doctype html><html lang="de" data-theme="dark"><body data-course-page="index.html">
      <header class="course-shell" aria-label="Course navigation"></header>
      <main id="main-content"><section id="intro" style="min-height:900px"><h1>Fixture</h1></section></main>
    </body></html>''')
    await page.evaluate("""() => {
      const values=new Map();
      const storage={getItem:key=>values.has(key)?values.get(key):null,setItem:(key,value)=>values.set(key,String(value)),removeItem:key=>values.delete(key),clear:()=>values.clear(),key:index=>[...values.keys()][index]||null,get length(){return values.size}};
      Object.defineProperty(window,'localStorage',{value:storage,configurable:true});
    }""")
    await add_course_css(page)
    await add_scripts(page,['vendor/course-config.js','vendor/qm-state.js','vendor/page-api.js','vendor/course-shell.js','vendor/course-enhancements.js'])
    await page.wait_for_function("document.querySelector('.qm-stage-rail') && document.querySelector('.course-shell-inner')")
    if await page.locator('.qm-stage-rail').count()!=1: raise AssertionError('rail duplicated')
    if await page.locator('header.course-shell').count()!=1: raise AssertionError('shell duplicated')
    if await page.locator('header.course-shell [data-role="menu"]').count(): raise AssertionError('top Etappen button returned')
    if await page.locator('.qm-stage-link').count()!=10: raise AssertionError('stage list not generated from config')
    if await page.locator('.qm-overlay').count()!=1: raise AssertionError('overlay duplicated')
    # Advanced question types execute through the real quiz renderer.
    await page.evaluate("window.QMCourseShell.openQuiz('photons')")
    await page.wait_for_selector('.qm-overlay.open input[type="number"]')
    await page.evaluate("window.QMCourseShell.openQuiz('formalism')")
    await page.wait_for_selector('.qm-overlay.open input[type="checkbox"]')
    await page.evaluate("window.QMCourseShell.openQuiz('prehistory')")
    await page.wait_for_selector('.qm-overlay.open .qm-order-answer select')
    await page.evaluate("document.querySelector('.qm-overlay').classList.remove('open')")
    if viewport['width']<=760:
        trigger=page.locator('.qm-stage-mobile-trigger')
        if not await trigger.is_visible(): raise AssertionError('mobile stage trigger hidden')
        if 'qm-rail-expanded' in (await page.locator('body').get_attribute('class') or ''): raise AssertionError('mobile rail starts open')
        await trigger.click(timeout=5000)
        await page.wait_for_function("document.body.classList.contains('qm-rail-expanded')")
        await page.locator('.qm-stage-scrim').click(position={'x':380,'y':400},timeout=5000)
        await page.wait_for_function("!document.body.classList.contains('qm-rail-expanded')")
    if errors: raise AssertionError(f'shell fixture errors: {errors}')
    await page.close()

async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,executable_path=CHROMIUM,args=['--no-sandbox','--disable-dev-shm-usage'])
        for mode in ('explicit','hybrid','defensive'):
            await math_mode(browser,mode)
        await shell_fixture(browser,{'width':1440,'height':900})
        await shell_fixture(browser,{'width':390,'height':844})
        await browser.close()
    print('OK: Chromium rendered all three math modes, generated one shell/rail, exposed numeric, multi-select, and ordering quizzes, and passed mobile off-canvas interaction.')

try:
    asyncio.run(main())
except Exception as error:
    print(f'FAIL: {error}')
    raise SystemExit(1)
