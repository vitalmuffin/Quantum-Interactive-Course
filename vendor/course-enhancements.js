(()=>{
'use strict';
const STAGES=[
 {id:'intro',url:'index.html',de:'Überblick',en:'Overview'},
 {id:'primer',url:'primer.html',de:'Grundlagen & Primer',en:'Foundations & primer'},
 {id:'prehistory',url:'prehistory.html',de:'Klassische Grenzen',en:'Classical limits'},
 {id:'photons',url:'historical_core.html#planck',de:'Energiequanten & Photonen',en:'Energy quanta & photons'},
 {id:'matter',url:'historical_core.html#matterwave',de:'Materiewellen & Statistik',en:'Matter waves & statistics'},
 {id:'formalism',url:'historical_core.html#matrix',de:'Operatoren & Wellenmechanik',en:'Operators & wave mechanics'},
 {id:'applications',url:'historical_core.html#born',de:'Wahrscheinlichkeit, Bindung & Felder',en:'Probability, bonding & fields'},
 {id:'tests',url:'foundations_tests.html',de:'Deutung & Tests',en:'Interpretations & tests'},
 {id:'info',url:'quantum_information.html',de:'Quanteninformation',en:'Quantum information'},
 {id:'sources',url:'source_reader.html',de:'Quellen',en:'Sources'}
];
const $=(s,r=document)=>r.querySelector(s);
const $$=(s,r=document)=>[...r.querySelectorAll(s)];
const lang=()=>document.documentElement.lang?.startsWith('en')?'en':'de';
const file=()=>location.pathname.split('/').pop()||'index.html';
const isEmbedded=()=>new URLSearchParams(location.search).get('embedded')==='1';
let rail,frame,currentId,mobileTrigger,railScrim;

function stageFromLocation(path=file(),hash=location.hash){
  if(path==='index.html')return'intro';
  if(path==='primer.html'||path==='math_foundations.html')return'primer';
  if(path==='prehistory.html')return'prehistory';
  if(path==='historical_core.html'){
    const h=String(hash||'').replace(/^#/,'');
    if(['matterwave','statistics'].includes(h))return'matter';
    if(['matrix','schrodinger','oscillator'].includes(h))return'formalism';
    if(['born','uncertainty','molecule','field','dirac'].includes(h))return'applications';
    return'photons';
  }
  if(path==='foundations_tests.html')return'tests';
  if(path==='quantum_information.html')return'info';
  if(path==='source_reader.html')return'sources';
  return'intro';
}
function stageFromScroll(){
  if(file()!=='historical_core.html')return stageFromLocation();
  const y=scrollY+innerHeight*.35;
  const born=$('#born'),matrix=$('#matrix'),matter=$('#matterwave');
  if(born&&y>=born.offsetTop)return'applications';
  if(matrix&&y>=matrix.offsetTop)return'formalism';
  if(matter&&y>=matter.offsetTop)return'matter';
  return'photons';
}
function cleanUrl(raw){
  const u=new URL(raw,location.href);u.searchParams.delete('embedded');return u.pathname.split('/').pop()+(u.search?u.search:'')+(u.hash||'');
}
function embeddedUrl(raw){
  const u=new URL(raw,location.href);u.searchParams.set('embedded','1');return u.pathname.split('/').pop()+u.search+(u.hash||'');
}
function stageForCourseLink(raw){
  let u;try{u=new URL(raw,location.href)}catch(_){return null}
  if(u.origin!==location.origin)return null;
  const path=u.pathname.split('/').pop()||'index.html';
  if(path==='index.html'&&u.hash&&!['','#top'].includes(u.hash))return null;
  if(!['index.html','primer.html','math_foundations.html','prehistory.html','historical_core.html','foundations_tests.html','quantum_information.html','source_reader.html'].includes(path))return null;
  return stageFromLocation(path,u.hash);
}
function routeCourseLink(raw,stageId=stageForCourseLink(raw)){
  if(!stageId)return false;
  showFrame(cleanUrl(raw),stageId);return true;
}
function setupCourseLinkRouting(){
  document.addEventListener('click',e=>{
    if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    const a=e.target.closest?.('a[href]');if(!a||a.target==='_blank'||a.hasAttribute('download'))return;
    const id=stageForCourseLink(a.href);if(!id)return;
    e.preventDefault();routeCourseLink(a.href,id);
    if(innerWidth<760)setExpanded(false);
  });
}
function updateRail(id=stageFromScroll()){
  currentId=id; if(!rail)return;
  $$('.qm-stage-link',rail).forEach((a,i)=>{
    const active=STAGES[i].id===id;a.classList.toggle('active',active);a.setAttribute('aria-current',active?'step':'false');
    const status=$('.qm-stage-state',a);if(status)status.textContent=active?'●':i<STAGES.findIndex(s=>s.id===id)?'✓':'○';
  });
  const label=$('.qm-stage-current',rail),s=STAGES.find(x=>x.id===id);if(label&&s)label.textContent=s[lang()];
}
function setExpanded(open){
  const mobile=matchMedia('(max-width:760px)').matches;
  document.body.classList.toggle('qm-rail-expanded',open);rail?.classList.toggle('expanded',open);
  if(!mobile)localStorage.setItem('qm_stage_rail_expanded',open?'1':'0');
  const b=$('.qm-stage-toggle',rail);if(b){b.setAttribute('aria-expanded',String(open));b.title=open?(lang()==='de'?'Etappen einklappen':'Collapse stages'):(lang()==='de'?'Etappen ausklappen':'Expand stages')}
  if(mobileTrigger){mobileTrigger.setAttribute('aria-expanded',String(open));mobileTrigger.setAttribute('aria-label',lang()==='de'?(open?'Etappen schließen':'Etappen öffnen'):(open?'Close stages':'Open stages'))}
  railScrim?.classList.toggle('open',mobile&&open);
}
function showFrame(url,stageId){
  currentId=stageId;updateRail(stageId);
  const target=embeddedUrl(url);
  if(!frame){
    frame=document.createElement('iframe');frame.className='qm-stage-frame';frame.name='qm-stage-frame';frame.title=lang()==='de'?'Kursinhalt':'Course content';document.body.appendChild(frame);
    document.body.classList.add('qm-stage-frame-active');
    frame.addEventListener('load',()=>{
      try{
        const w=frame.contentWindow,loc=w.location;
        const id=stageFromLocation(loc.pathname.split('/').pop(),loc.hash);updateRail(id);
        history.replaceState({qmFrame:true},'',cleanUrl(loc.href));
        w.postMessage({type:'qm-shell-state',lang:lang(),theme:document.documentElement.dataset.theme||'dark'},'*');
      }catch(_){/* same-origin is expected on the static course */}
    });
  }
  try{
    const u=new URL(target,location.href),cw=frame.contentWindow;
    if(frame.src&&cw&&cw.location.pathname.endsWith(u.pathname.split('/').pop())&&cw.location.search===u.search){cw.location.hash=u.hash;updateRail(stageId);history.pushState({qmFrame:true},'',cleanUrl(url));setTimeout(()=>updateRail(stageId),60);return;}
  }catch(_){/* initial frame navigation */}
  frame.src=target;history.pushState({qmFrame:true},'',cleanUrl(url));
}
function navigateStage(e,s){
  const target=new URL(s.url,location.href),targetFile=target.pathname.split('/').pop();
  if(!frame&&targetFile===file()){
    e.preventDefault();currentId=s.id;updateRail(s.id);
    const id=target.hash.slice(1);if(id)document.getElementById(id)?.scrollIntoView({behavior:'smooth',block:'start'});else scrollTo({top:0,behavior:'smooth'});
    history.pushState(null,'',s.url);return;
  }
  e.preventDefault();showFrame(s.url,s.id);
  if(innerWidth<760)setExpanded(false);
}
function buildRail(){
  rail=document.createElement('aside');rail.className='qm-stage-rail';rail.setAttribute('aria-label',lang()==='de'?'Kurs-Etappen':'Course stages');
  rail.innerHTML=`<button class="qm-stage-toggle" type="button" aria-expanded="false"><span class="qm-toggle-icon">☰</span><span class="qm-toggle-label">${lang()==='de'?'Etappen':'Stages'}</span></button><div class="qm-stage-current"></div><nav>${STAGES.map((s,i)=>`<a class="qm-stage-link" href="${s.url}" data-stage="${s.id}"><span class="qm-stage-number">${i+1}</span><span class="qm-stage-name">${s[lang()]}</span><span class="qm-stage-state">○</span></a>`).join('')}</nav><button class="qm-rail-progress" type="button"><span>◔</span><span>${lang()==='de'?'Fortschritt':'Progress'}</span></button>`;
  mobileTrigger=document.createElement('button');mobileTrigger.className='qm-stage-mobile-trigger';mobileTrigger.type='button';mobileTrigger.innerHTML='<span aria-hidden="true">☰</span>';mobileTrigger.setAttribute('aria-controls','qmStageRail');
  rail.id='qmStageRail';
  railScrim=document.createElement('button');railScrim.className='qm-stage-scrim';railScrim.type='button';railScrim.tabIndex=-1;
  document.body.append(railScrim,rail,mobileTrigger);
  $('.qm-stage-toggle',rail).onclick=()=>setExpanded(!document.body.classList.contains('qm-rail-expanded'));
  mobileTrigger.onclick=()=>setExpanded(true);railScrim.onclick=()=>setExpanded(false);
  $$('.qm-stage-link',rail).forEach((a,i)=>a.onclick=e=>navigateStage(e,STAGES[i]));
  $('.qm-rail-progress',rail).onclick=()=>window.QMCourseShell?.openProgress?.();
  const saved=localStorage.getItem('qm_stage_rail_expanded');setExpanded(innerWidth<=760?false:(saved===null?innerWidth>=1280:saved==='1'));updateRail();
  addEventListener('resize',()=>{if(innerWidth<=760&&document.body.classList.contains('qm-rail-expanded'))setExpanded(false)},{passive:true});
}
function refreshRailLanguage(){
  if(!rail)return;$('.qm-toggle-label',rail).textContent=lang()==='de'?'Etappen':'Stages';
  $$('.qm-stage-name',rail).forEach((n,i)=>n.textContent=STAGES[i][lang()]);
  $('.qm-rail-progress span:last-child',rail).textContent=lang()==='de'?'Fortschritt':'Progress';
  if(mobileTrigger)mobileTrigger.setAttribute('aria-label',lang()==='de'?'Etappen öffnen':'Open stages');
  updateRail(currentId||stageFromScroll());
}
function setupCarouselArrows(){
  const wrap=$('.rail-carousel'),track=wrap?.querySelector('.rail'),buttons=wrap?$$('.rail-arrow',wrap):[];if(!track||buttons.length<2)return;
  const update=()=>{const max=Math.max(0,track.scrollWidth-track.clientWidth-2);buttons[0].disabled=track.scrollLeft<=2;buttons[1].disabled=track.scrollLeft>=max};
  track.addEventListener('scroll',update,{passive:true});addEventListener('resize',update,{passive:true});requestAnimationFrame(update);setTimeout(update,250);
}
function visualSvg(id){
  const common='viewBox="0 0 720 250" role="img"';
  const axes='<path class="fv-axis" d="M45 125H685M365 25V225"/><path class="fv-tick" d="M205 120v10M525 120v10"/>';
  if(id==='wave')return `<svg ${common} aria-label="Sinus, Kosinus und Tangens">${axes}<path class="fv-a" d="M45 125 C85 45 125 45 165 125 S245 205 285 125 S365 45 405 125 S485 205 525 125 S605 45 685 125"/><path class="fv-b" d="M45 45 C85 45 125 125 165 125 S245 45 285 45 S365 125 405 125 S485 45 525 45 S605 125 685 125"/><path class="fv-c" d="M55 215 C95 190 125 160 155 125 C185 90 215 55 245 35 M285 215 C325 190 345 160 365 125 C395 80 425 50 455 35 M505 215 C545 185 575 155 605 110 C630 72 655 45 680 35"/></svg><div class="foundation-legend"><span class="fv-a-dot">sin(x)</span><span class="fv-b-dot">cos(x)</span><span class="fv-c-dot">tan(x)</span></div>`;
  if(id==='superposition')return `<svg ${common} aria-label="Funktionen und ihre Summe">${axes}<path class="fv-a" d="M45 125 C95 55 145 55 195 125 S295 195 345 125 S445 55 495 125 S595 195 685 125"/><path class="fv-b" d="M45 125 C70 90 95 90 120 125 S170 160 195 125 S245 90 270 125 S320 160 345 125 S395 90 420 125 S470 160 495 125 S545 90 570 125 S620 160 685 125"/><path class="fv-sum" d="M45 125 C90 25 145 35 195 125 S300 225 345 125 S445 25 495 125 S600 225 685 125"/></svg><div class="foundation-legend"><span class="fv-a-dot">f(x)</span><span class="fv-b-dot">g(x)</span><span class="fv-sum-dot">f(x)+g(x)</span></div>`;
  if(id==='probability')return `<svg ${common} aria-label="Wahrscheinlichkeitsdichte und Fläche"><path class="fv-axis" d="M45 215H685M365 30V225"/><path class="fv-fill" d="M45 215 C160 215 210 200 260 150 C305 105 325 50 365 42 C405 50 425 105 470 150 C520 200 570 215 685 215 Z"/><path class="fv-a" d="M45 215 C160 215 210 200 260 150 C305 105 325 50 365 42 C405 50 425 105 470 150 C520 200 570 215 685 215"/><text x="480" y="85">∫ p(x) dx = 1</text></svg>`;
  if(id==='complex')return `<svg ${common} aria-label="Komplexe Zahlenebene"><path class="fv-axis" d="M70 125H650M360 25V225"/><circle class="fv-circle" cx="360" cy="125" r="82"/><path class="fv-a" marker-end="url(#fvArrow)" d="M360 125L425 75"/><path class="fv-dash" d="M425 75V125M425 75H360"/><text x="432" y="70">z = r·e^{iθ}</text><text x="430" y="143">Re</text><text x="325" y="45">Im</text><defs><marker id="fvArrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z"/></marker></defs></svg>`;
  if(id==='basis')return `<svg ${common} aria-label="Vektor und Projektionen"><path class="fv-axis" d="M80 205H660M180 225V30"/><path class="fv-a" marker-end="url(#fvArrow2)" d="M180 205L525 65"/><path class="fv-dash" d="M525 65V205M525 65H180"/><path class="fv-b" d="M180 205H525"/><path class="fv-c" d="M180 205V65"/><text x="535" y="65">|ψ⟩</text><text x="340" y="225">Komponente 1</text><text x="90" y="120">Komponente 2</text><defs><marker id="fvArrow2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z"/></marker></defs></svg>`;
  if(id==='calculus')return `<svg ${common} aria-label="Ableitung und Integral"><path class="fv-axis" d="M45 210H685M130 25V225"/><path class="fv-fill" d="M220 210 C270 190 315 150 360 105 C405 60 455 45 510 70 L510 210Z"/><path class="fv-a" d="M45 215 C160 215 220 205 280 170 C340 135 365 90 430 60 C500 28 570 55 685 130"/><path class="fv-b" d="M295 175L490 42"/><circle class="fv-point" cx="390" cy="88" r="6"/><text x="500" y="42">Tangente: f′(x)</text><text x="330" y="195">Fläche: ∫f(x)dx</text></svg>`;
  if(id==='eigen')return `<svg ${common} aria-label="Operator und Eigenrichtungen"><path class="fv-axis" d="M80 205H660M180 225V30"/><path class="fv-a" marker-end="url(#fvArrow3)" d="M180 205L350 205"/><path class="fv-b" marker-end="url(#fvArrow3)" d="M180 205L180 80"/><path class="fv-sum" marker-end="url(#fvArrow3)" d="M180 205L450 205"/><path class="fv-c" marker-end="url(#fvArrow3)" d="M180 205L180 125"/><path class="fv-dash" marker-end="url(#fvArrow3)" d="M180 205L390 75"/><path class="fv-dash2" marker-end="url(#fvArrow3)" d="M180 205L505 125"/><text x="465" y="225">Eigenrichtung: nur skaliert</text><text x="400" y="70">allgemeiner Vektor: gedreht</text><defs><marker id="fvArrow3" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z"/></marker></defs></svg>`;
  return'';
}
function setupFoundationVisuals(){
  if(file()!=='primer.html')return;
  ['wave','superposition','probability','complex','basis','calculus','eigen'].forEach(id=>{
    const foundation=$(`#${id} .primer-foundation`);if(!foundation||foundation.querySelector('.foundation-visual'))return;
    const box=document.createElement('figure');box.className='foundation-visual';box.innerHTML=visualSvg(id);const grid=foundation.querySelector('.foundation-grid');foundation.insertBefore(box,grid||null);
  });
}
function setupEmbeddedBridge(){
  document.documentElement.classList.add('qm-embedded');
  const notify=()=>parent.postMessage({type:'qm-embedded-location',url:location.href,stage:stageFromScroll()},'*');
  addEventListener('hashchange',notify);addEventListener('load',notify);let tick=false;addEventListener('scroll',()=>{if(!tick){requestAnimationFrame(()=>{notify();tick=false});tick=true}},{passive:true});
  document.addEventListener('click',e=>{
    if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    const a=e.target.closest?.('a[href]');if(!a||a.target==='_blank'||a.hasAttribute('download'))return;
    const stage=stageForCourseLink(a.href);if(!stage)return;
    e.preventDefault();parent.postMessage({type:'qm-embedded-navigate',url:cleanUrl(a.href),stage},'*');
  });
  addEventListener('message',e=>{const d=e.data||{};if(d.type!=='qm-shell-state')return;if(d.lang){localStorage.setItem('qm_language',d.lang);const b=$(d.lang==='de'?'#langDE,#deBtn':'#langEN,#enBtn');b?.click()}if(d.theme&&document.documentElement.dataset.theme!==d.theme){const b=$('#themeToggle,#themeBtn,#theme');b?.click()}});
}
function init(){
  if(isEmbedded()){setupFoundationVisuals();setupCarouselArrows();setupEmbeddedBridge();return}
  buildRail();setupCourseLinkRouting();setupCarouselArrows();setupFoundationVisuals();
  let ticking=false;addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(()=>{updateRail(stageFromScroll());ticking=false});ticking=true}},{passive:true});
  addEventListener('hashchange',()=>updateRail(stageFromScroll()));
  addEventListener('message',e=>{const d=e.data||{};if(d.type==='qm-embedded-navigate'){routeCourseLink(d.url,d.stage||stageForCourseLink(d.url));return}if(d.type!=='qm-embedded-location')return;currentId=d.stage||currentId;updateRail(currentId);requestAnimationFrame(()=>updateRail(currentId));try{history.replaceState({qmFrame:true},'',cleanUrl(d.url))}catch(_){}});
  addEventListener('popstate',()=>{if(frame)frame.src=embeddedUrl(location.href)});
  new MutationObserver(refreshRailLanguage).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
  const themeObserver=new MutationObserver(()=>{try{frame?.contentWindow?.postMessage({type:'qm-shell-state',lang:lang(),theme:document.documentElement.dataset.theme||'dark'},'*')}catch(_){}});themeObserver.observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
