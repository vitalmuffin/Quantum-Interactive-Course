#!/usr/bin/env python3
"""Architecture and build invariants for the v0.16 stabilization release."""
from __future__ import annotations
import json,re,subprocess,sys,tempfile
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)
config=json.load(open(R/'data/course.config.json',encoding='utf-8'))
data=json.load(open(R/'data/course_data.json',encoding='utf-8'))
compat=json.load(open(R/'data/papers_index.json',encoding='utf-8'))
need(config.get('courseVersion')=='0.16','canonical config version is not 0.16')
need(config.get('progress',{}).get('key')=='qm_course_progress_v1','canonical progress key is wrong')
need(set(config.get('progress',{}).get('legacyKeys',[]))=={'quantum_course_progress_v011','qm_course_progress_v07'},'legacy migration keys are incomplete')
need(data==compat,'compatibility papers_index.json drifted from canonical course_data.json')
need(data.get('course_version')==config.get('courseVersion'),'course data version drift')
stages=config.get('stages',[])
need(len(stages)==10 and len({s['id'] for s in stages})==10,'stage config is incomplete or duplicated')
need(len(config.get('advancedQuizQuestions',{}))>=8,'advanced quiz bank is too small')
need({'number','multi','order','prediction'} <= {q.get('type') for q in config.get('advancedQuizQuestions',{}).values()},'new quiz types are missing')

index=(R/'index.html').read_text(encoding='utf-8')
need((R/'index.html').stat().st_size<450_000,'index.html was not split below 450 kB')
need('data/course_overview.bundle.js?v=0.16' in index,'index does not load the lightweight overview data')
need('vendor/course-data-loader.js?v=0.16' in index,'index does not configure lazy full-detail loading')
need('data/course_data.bundle.js?v=0.16' not in index,'full paper data is still eagerly loaded by index')
need('<script id="courseData"' not in index and 'const DATA = JSON.parse' not in index,'large JSON remains embedded in index')
need((R/'data/course_data.bundle.js').stat().st_size>1_000_000,'file:// full-detail fallback missing')
need((R/'data/course_overview.bundle.js').stat().st_size<100_000,'initial overview bundle exceeds 100 kB')

shared=['vendor/course-config.js?v=0.16','vendor/qm-state.js?v=0.16','vendor/page-api.js?v=0.16','vendor/course-shell.js?v=0.16','vendor/course-enhancements.js?v=0.16']
for page in [p for p in R.glob('*.html') if p.name!='progress.html']:
    text=page.read_text(encoding='utf-8'); soup=BeautifulSoup(text,'html.parser')
    for asset in shared: need(text.count(asset)==1,f'{page.name}: shared asset count for {asset} is not one')
    mounts=soup.select('header.course-shell')
    need(len(mounts)==1 and not mounts[0].get_text(strip=True),f'{page.name}: shell mount must be one empty element')

shell=(R/'vendor/course-shell.js').read_text(); enh=(R/'vendor/course-enhancements.js').read_text(); api=(R/'vendor/page-api.js').read_text()
need(not re.search(r'\bconst\s+stages\s*=\s*\[',shell,re.I),'shell duplicates stage data')
need(not re.search(r'\bconst\s+(stages|STAGES)\s*=\s*\[',enh),'enhancements duplicate stage data')
need("CHANNEL='qm-course-v1'" in api,'unified iframe protocol missing')
need('trustedMessage' in api and 'event.source' in api and 'event.origin' in api,'iframe message validation missing')
need('QMPage.register' in api or 'function register' in api,'common page adapter interface missing')
need('type="number"' in shell and 'type="checkbox"' in shell and "q.type==='order'" in shell,'number/multi/order quiz rendering missing')
need('Math.abs(value-Number(q.answer))<=Number(q.tolerance||0)' in shell,'numeric quiz tolerance check missing')

entry=(R/'vendor/course-shell.css').read_text()
for name in ['tokens.css','shell.css','learning.css','rail.css','math.css']:
    need(name in entry,f'modular CSS entry point misses {name}')
math_config=config.get('math',{})
need(set(math_config.get('modes',[]))=={'explicit','hybrid','defensive'},'dual/defensive math modes not configured')
for name in ['math-core.js','math-defensive.js','math-offline.js']:
    need((R/'vendor'/name).exists(),f'math layer missing: {name}')
plotly=(R/'vendor/plotly-loader.js').read_text()
need("script.src='vendor/plotly-3.3.1.min.js'" in plotly and 'window.QMPlotly={ready:load}' in plotly,'Plotly is not lazy-loaded')

# Syntax-check first-party JavaScript. The two vendored minified libraries are deliberately excluded.
for path in sorted((R/'vendor').glob('*.js')):
    if path.name in {'plotly-3.3.1.min.js','mathjax-tex-svg-full.js'}: continue
    result=subprocess.run(['node','--check',str(path)],capture_output=True,text=True)
    need(result.returncode==0,f'JavaScript syntax error in {path.name}: {result.stderr.strip()}')

# Execute the real migration service in Node with both historical progress formats.
node_script=f"""
const fs=require('fs'),vm=require('vm');
const store=new Map([
 ['quantum_course_progress_v011',JSON.stringify({{stages:{{photons:{{scroll:0.5}}}},papers:{{'1':true}}}})],
 ['qm_course_progress_v07',JSON.stringify({{stages:{{photons:{{scroll:0.8}}}},quizzes:{{planck:{{passed:true}}}}}})]
]);
const localStorage={{getItem:k=>store.has(k)?store.get(k):null,setItem:(k,v)=>store.set(k,String(v)),removeItem:k=>store.delete(k)}};
const context={{window:null,localStorage,CustomEvent:class{{constructor(type,init){{this.type=type;this.detail=init?.detail}}}},dispatchEvent:()=>{{}},console,Date,JSON,Object,Boolean,Number,String,Map,Set}};context.window=context;
vm.createContext(context);
vm.runInContext(fs.readFileSync({json.dumps(str(R/'vendor/course-config.js'))},'utf8'),context);
vm.runInContext(fs.readFileSync({json.dumps(str(R/'vendor/qm-state.js'))},'utf8'),context);
const state=context.QMState.load();
if(context.QMState.KEY!=='qm_course_progress_v1'||state.stages.photons.scroll!==0.8||!state.papers['1']||!state.quizzes.planck.passed||!store.has('qm_course_progress_v1'))process.exit(2);
context.QMState.reset();const reset=context.QMState.load();if(reset.papers['1']||store.has('quantum_course_progress_v011')||store.has('qm_course_progress_v07'))process.exit(3);
console.log('migration and reset ok');
"""
result=subprocess.run(['node','-e',node_script],capture_output=True,text=True)
need(result.returncode==0,f'progress migration execution failed: {result.stderr or result.stdout}')

# Generated artifacts must be reproducible from canonical JSON (manifest checked after final build).
result=subprocess.run([sys.executable,str(R/'tools/build_course.py'),'--check','--no-manifest'],cwd=R,capture_output=True,text=True)
need(result.returncode==0,f'build output drift: {result.stdout}{result.stderr}')

if errors:
    print('\n'.join('FAIL '+x for x in errors));sys.exit(1)
print('OK: v0.16 canonical data, migration, iframe API, modular CSS, split loading, math modes, quizzes, and build invariants passed.')
