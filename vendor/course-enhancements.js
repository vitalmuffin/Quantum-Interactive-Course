(()=>{
'use strict';
const CONFIG=window.QM_COURSE_CONFIG||{};
const STAGES=CONFIG.stages||[];
const API=window.QMPage;
const $=(selector,root=document)=>root.querySelector(selector);
const $$=(selector,root=document)=>[...root.querySelectorAll(selector)];
const lang=()=>API?.language?.()||(document.documentElement.lang?.startsWith('en')?'en':'de');
const file=()=>API?.fileFromUrl?.(location.href)||(location.pathname.split('/').pop()||'index.html');
const isEmbedded=()=>new URLSearchParams(location.search).get('embedded')==='1';
let rail=null,frame=null,currentId=null,mobileTrigger=null,railScrim=null;
function stageFromLocation(path=file(),hash=location.hash){return API?.stageFromLocation?.(path,hash)||'intro'}
function stageFromScroll(){
  if(file()!=='historical_core.html')return stageFromLocation();
  const y=scrollY+innerHeight*.35;
  const born=$('#born'),matrix=$('#matrix'),matter=$('#matterwave');
  if(born&&y>=born.offsetTop)return'applications';
  if(matrix&&y>=matrix.offsetTop)return'formalism';
  if(matter&&y>=matter.offsetTop)return'matter';
  return'photons';
}
const cleanUrl=raw=>API?.cleanUrl?.(raw)||raw;
const embeddedUrl=raw=>API?.embeddedUrl?.(raw)||raw;
const stageForCourseLink=raw=>API?.stageForCourseLink?.(raw)||null;
function routeCourseLink(raw,stageId=stageForCourseLink(raw)){if(!stageId)return false;showFrame(cleanUrl(raw),stageId);return true}
function setupCourseLinkRouting(){
  document.addEventListener('click',event=>{
    if(event.defaultPrevented||event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
    const anchor=event.target.closest?.('a[href]');if(!anchor||anchor.target==='_blank'||anchor.hasAttribute('download'))return;
    const stageId=stageForCourseLink(anchor.href);if(!stageId)return;
    event.preventDefault();routeCourseLink(anchor.href,stageId);
    if(innerWidth<760)setExpanded(false);
  });
}
function updateRail(id=stageFromScroll()){
  currentId=id;if(!rail)return;
  const currentIndex=STAGES.findIndex(stage=>stage.id===id);
  $$('.qm-stage-link',rail).forEach((anchor,index)=>{
    const active=STAGES[index]?.id===id;
    anchor.classList.toggle('active',active);
    if(active)anchor.setAttribute('aria-current','step');else anchor.removeAttribute('aria-current');
    const status=$('.qm-stage-state',anchor);if(status)status.textContent=active?'●':index<currentIndex?'✓':'○';
  });
  const label=$('.qm-stage-current',rail),stage=STAGES.find(item=>item.id===id);
  if(label&&stage)label.textContent=stage[lang()];
}
function setExpanded(open){
  const mobile=matchMedia('(max-width:760px)').matches;
  document.body.classList.toggle('qm-rail-expanded',open);rail?.classList.toggle('expanded',open);
  if(!mobile)window.QMState?.setRailExpanded?.(open);
  const button=$('.qm-stage-toggle',rail);
  if(button){button.setAttribute('aria-expanded',String(open));button.title=open?(lang()==='de'?'Etappen einklappen':'Collapse stages'):(lang()==='de'?'Etappen ausklappen':'Expand stages')}
  if(mobileTrigger){mobileTrigger.setAttribute('aria-expanded',String(open));mobileTrigger.setAttribute('aria-label',lang()==='de'?(open?'Etappen schließen':'Etappen öffnen'):(open?'Close stages':'Open stages'))}
  railScrim?.classList.toggle('open',mobile&&open);
}
function sendShellState(){
  if(!frame?.contentWindow)return;
  API?.post?.(frame.contentWindow,'shell-state',{language:lang(),theme:document.documentElement.dataset.theme||'dark'});
}
function ensureFrame(){
  if(frame?.isConnected)return frame;
  frame=document.querySelector('.qm-stage-frame');
  if(!frame){
    frame=document.createElement('iframe');frame.className='qm-stage-frame';frame.name='qm-stage-frame';frame.title=lang()==='de'?'Kursinhalt':'Course content';
    document.body.appendChild(frame);
  }
  document.body.classList.add('qm-stage-frame-active');
  if(!frame.dataset.qmBound){
    frame.dataset.qmBound='1';
    frame.addEventListener('load',()=>{
      try{
        const locationInFrame=frame.contentWindow.location;
        updateRail(stageFromLocation(API.fileFromUrl(locationInFrame.href),locationInFrame.hash));
        history.replaceState({qmFrame:true},'',cleanUrl(locationInFrame.href));
        sendShellState();
      }catch(error){console.warn('Could not synchronize embedded course page:',error)}
    });
  }
  return frame;
}
function showFrame(url,stageId){
  currentId=stageId;updateRail(stageId);
  const target=embeddedUrl(url),courseFrame=ensureFrame();
  try{
    const wanted=new URL(target,location.href),inside=courseFrame.contentWindow?.location;
    const same=inside&&API.fileFromUrl(inside.href)===API.fileFromUrl(wanted.href)&&inside.search===wanted.search;
    if(same){inside.hash=wanted.hash;history.pushState({qmFrame:true},'',cleanUrl(url));setTimeout(()=>updateRail(stageId),50);return}
  }catch(_){/* first navigation or inaccessible transitional document */}
  courseFrame.src=target;history.pushState({qmFrame:true},'',cleanUrl(url));
}
function navigateStage(event,stage){
  event.preventDefault();
  const target=new URL(stage.url,location.href),targetFile=API.fileFromUrl(target.href);
  if(!frame&&targetFile===file()){
    currentId=stage.id;updateRail(stage.id);
    const anchor=target.hash.slice(1);if(anchor)document.getElementById(anchor)?.scrollIntoView({behavior:'smooth',block:'start'});else scrollTo({top:0,behavior:'smooth'});
    history.pushState(null,'',stage.url);
  }else showFrame(stage.url,stage.id);
  if(innerWidth<760)setExpanded(false);
}
function buildRail(){
  document.querySelectorAll('.qm-stage-rail,.qm-stage-mobile-trigger,.qm-stage-scrim').forEach(node=>node.remove());
  rail=document.createElement('aside');rail.id='qmStageRail';rail.className='qm-stage-rail';rail.setAttribute('aria-label',lang()==='de'?'Kurs-Etappen':'Course stages');
  rail.innerHTML=`<button class="qm-stage-toggle" type="button" aria-expanded="false"><span class="qm-toggle-icon" aria-hidden="true">☰</span><span class="qm-toggle-label">${lang()==='de'?'Etappen':'Stages'}</span></button><div class="qm-stage-current"></div><nav>${STAGES.map((stage,index)=>`<a class="qm-stage-link" href="${stage.url}" data-stage="${stage.id}"><span class="qm-stage-number">${index+1}</span><span class="qm-stage-name">${stage[lang()]}</span><span class="qm-stage-state" aria-hidden="true">○</span></a>`).join('')}</nav><button class="qm-rail-progress" type="button"><span aria-hidden="true">◔</span><span>${lang()==='de'?'Fortschritt':'Progress'}</span></button>`;
  mobileTrigger=document.createElement('button');mobileTrigger.className='qm-stage-mobile-trigger';mobileTrigger.type='button';mobileTrigger.innerHTML='<span aria-hidden="true">☰</span>';mobileTrigger.setAttribute('aria-controls',rail.id);
  railScrim=document.createElement('button');railScrim.className='qm-stage-scrim';railScrim.type='button';railScrim.tabIndex=-1;railScrim.setAttribute('aria-label',lang()==='de'?'Etappen schließen':'Close stages');
  document.body.append(railScrim,rail,mobileTrigger);
  $('.qm-stage-toggle',rail).onclick=()=>setExpanded(!document.body.classList.contains('qm-rail-expanded'));
  mobileTrigger.onclick=()=>setExpanded(true);railScrim.onclick=()=>setExpanded(false);
  $$('.qm-stage-link',rail).forEach((anchor,index)=>anchor.onclick=event=>navigateStage(event,STAGES[index]));
  $('.qm-rail-progress',rail).onclick=()=>window.QMCourseShell?.openProgress?.();
  const saved=Boolean(window.QMState?.settings?.railExpanded);setExpanded(innerWidth<=760?false:(innerWidth>=1280?saved:true));updateRail();
  addEventListener('resize',()=>{if(innerWidth<=760&&document.body.classList.contains('qm-rail-expanded'))setExpanded(false)},{passive:true});
}
function refreshRailLanguage(){
  if(!rail)return;
  $('.qm-toggle-label',rail).textContent=lang()==='de'?'Etappen':'Stages';
  $$('.qm-stage-name',rail).forEach((node,index)=>node.textContent=STAGES[index][lang()]);
  $('.qm-rail-progress span:last-child',rail).textContent=lang()==='de'?'Fortschritt':'Progress';
  rail.setAttribute('aria-label',lang()==='de'?'Kurs-Etappen':'Course stages');
  updateRail(currentId||stageFromScroll());sendShellState();
}
function setupCarouselArrows(){
  const wrap=$('.rail-carousel'),track=wrap?.querySelector('.rail'),buttons=wrap?$$('.rail-arrow',wrap):[];if(!track||buttons.length<2)return;
  const update=()=>{const max=Math.max(0,track.scrollWidth-track.clientWidth-2);buttons[0].disabled=track.scrollLeft<=2;buttons[1].disabled=track.scrollLeft>=max};
  track.addEventListener('scroll',update,{passive:true});addEventListener('resize',update,{passive:true});requestAnimationFrame(update);setTimeout(update,250);
}

function sampledPath(fn,{x0=45,x1=685,y0=125,xMin=-2*Math.PI,xMax=2*Math.PI,yScale=80,points=256,maxAbs=Infinity}={}){
  let d='',drawing=false;
  for(let index=0;index<=points;index++){
    const x=xMin+(xMax-xMin)*index/points,value=fn(x);
    if(!Number.isFinite(value)||Math.abs(value)>maxAbs){drawing=false;continue}
    const px=x0+(x1-x0)*index/points,py=y0-value*yScale;
    d+=`${drawing?'L':'M'}${px.toFixed(1)} ${py.toFixed(1)}`;
    drawing=true;
  }
  return d;
}
function compactArrowMarker(id){
  return `<defs><marker id="${id}" markerWidth="5.5" markerHeight="5.5" refX="5.1" refY="2.75" orient="auto"><path d="M0 0L5.5 2.75L0 5.5Z"/></marker></defs>`;
}
function visualSvg(id){
  const common='viewBox="0 0 720 250" role="img"';
  const axes='<path class="fv-axis" d="M45 125H685M365 25V225"/><path class="fv-tick" d="M205 120v10M525 120v10"/>';
  if(id==='wave'){
    const sine=sampledPath(Math.sin);
    const cosine=sampledPath(Math.cos);
    const tangent=sampledPath(Math.tan,{maxAbs:1.16});
    const waveAxes='<path class="fv-grid" d="M45 45H685M45 205H685"/><path class="fv-axis" d="M45 125H685M365 25V225"/><text x="14" y="49">+1</text><text x="25" y="129">0</text><text x="14" y="209">−1</text>';
    return `<svg ${common} aria-label="Sinus, Kosinus und Tangens auf derselben Skala">${waveAxes}<path class="fv-a" d="${sine}"/><path class="fv-b" d="${cosine}"/><path class="fv-c" d="${tangent}"/></svg><div class="foundation-legend"><span class="fv-a-dot">sin(x)</span><span class="fv-b-dot">cos(x)</span><span class="fv-c-dot">tan(x)</span></div>`;
  }
  if(id==='superposition'){
    const f=x=>.65*Math.sin(x);
    const g=x=>.45*Math.sin(2*x+Math.PI/3);
    const scale={yScale:62};
    const first=sampledPath(f,scale),second=sampledPath(g,scale),sum=sampledPath(x=>f(x)+g(x),scale);
    return `<svg ${common} aria-label="Zwei Funktionen und ihre punktweise Summe">${axes}<path class="fv-a" d="${first}"/><path class="fv-b" d="${second}"/><path class="fv-sum" d="${sum}"/></svg><div class="foundation-legend"><span class="fv-a-dot">f(x)</span><span class="fv-b-dot">g(x)</span><span class="fv-sum-dot">f(x)+g(x)</span></div>`;
  }
  if(id==='probability')return `<svg ${common} aria-label="Wahrscheinlichkeitsdichte und Fläche"><path class="fv-axis" d="M45 215H685M365 30V225"/><path class="fv-fill" d="M45 215 C160 215 210 200 260 150 C305 105 325 50 365 42 C405 50 425 105 470 150 C520 200 570 215 685 215 Z"/><path class="fv-a" d="M45 215 C160 215 210 200 260 150 C305 105 325 50 365 42 C405 50 425 105 470 150 C520 200 570 215 685 215"/><text x="480" y="85">∫ p(x) dx = 1</text></svg>`;
  if(id==='complex')return `<svg ${common} aria-label="Komplexe Zahl aus Real- und Imaginärteil"><path class="fv-axis" d="M70 125H650M360 25V225"/><circle class="fv-circle" cx="360" cy="125" r="82"/><path class="fv-a" marker-end="url(#fvArrow)" d="M360 125L425 75"/><path class="fv-dash" d="M425 75V125M425 75H360"/><text x="432" y="70">z = a + bi</text><text x="392" y="143">a = Re(z)</text><text x="280" y="75">b = Im(z)</text>${compactArrowMarker("fvArrow")}</svg>`;
  if(id==='basis')return `<svg ${common} aria-label="Vektor und Projektionen"><path class="fv-axis" d="M80 205H660M180 225V30"/><path class="fv-a" marker-end="url(#fvArrow2)" d="M180 205L525 65"/><path class="fv-dash" d="M525 65V205M525 65H180"/><path class="fv-b" d="M180 205H525"/><path class="fv-c" d="M180 205V65"/><text x="535" y="65">|ψ⟩</text><text x="340" y="225">Komponente 1</text><text x="90" y="120">Komponente 2</text>${compactArrowMarker("fvArrow2")}</svg>`;
  if(id==='calculus')return `<svg ${common} aria-label="Ableitung und Integral"><path class="fv-axis" d="M45 210H685M130 25V225"/><path class="fv-fill" d="M220 210 C270 190 315 150 360 105 C405 60 455 45 510 70 L510 210Z"/><path class="fv-a" d="M45 215 C160 215 220 205 280 170 C340 135 365 90 430 60 C500 28 570 55 685 130"/><path class="fv-b" d="M295 175L490 42"/><circle class="fv-point" cx="390" cy="88" r="6"/><text x="500" y="42">Tangente: f′(x)</text><text x="330" y="195">Fläche: ∫f(x)dx</text></svg>`;
  if(id==='eigen')return `<svg ${common} aria-label="Operator und Eigenrichtungen"><path class="fv-axis" d="M80 205H660M180 225V30"/><path class="fv-a" marker-end="url(#fvArrow3)" d="M180 205L350 205"/><path class="fv-b" marker-end="url(#fvArrow3)" d="M180 205L180 80"/><path class="fv-sum" marker-end="url(#fvArrow3)" d="M180 205L450 205"/><path class="fv-c" marker-end="url(#fvArrow3)" d="M180 205L180 125"/><path class="fv-dash" marker-end="url(#fvArrow3)" d="M180 205L390 75"/><path class="fv-dash2" marker-end="url(#fvArrow3)" d="M180 205L505 125"/><text x="465" y="225">Eigenrichtung: nur skaliert</text><text x="400" y="70">allgemeiner Vektor: gedreht</text>${compactArrowMarker("fvArrow3")}</svg>`;
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
  const notify=()=>API?.post?.(parent,'location',{url:location.href,stage:stageFromScroll()});
  addEventListener('hashchange',notify);addEventListener('load',notify);
  let ticking=false;addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(()=>{notify();ticking=false});ticking=true}},{passive:true});
  document.addEventListener('click',event=>{
    if(event.defaultPrevented||event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
    const anchor=event.target.closest?.('a[href]');if(!anchor||anchor.target==='_blank'||anchor.hasAttribute('download'))return;
    const stageId=stageForCourseLink(anchor.href);if(!stageId)return;
    event.preventDefault();API?.post?.(parent,'navigate',{url:cleanUrl(anchor.href),stage:stageId});
  });
  addEventListener('message',event=>{
    if(!API?.trustedMessage?.(event,parent))return;
    const message=event.data||{};if(message.channel!==API.CHANNEL||message.type!=='shell-state')return;
    if(message.language)API.setLanguage(message.language);
    if(message.theme)API.setTheme(message.theme);
  });
  notify();
}
function init(){
  if(isEmbedded()){setupFoundationVisuals();setupCarouselArrows();setupEmbeddedBridge();return}
  buildRail();setupCourseLinkRouting();setupCarouselArrows();setupFoundationVisuals();
  let ticking=false;addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(()=>{updateRail(stageFromScroll());ticking=false});ticking=true}},{passive:true});
  addEventListener('hashchange',()=>updateRail(stageFromScroll()));
  addEventListener('message',event=>{
    if(!frame?.contentWindow||!API?.trustedMessage?.(event,frame.contentWindow))return;
    const message=event.data||{};if(message.channel!==API.CHANNEL)return;
    if(message.type==='navigate'){routeCourseLink(message.url,message.stage||stageForCourseLink(message.url));return}
    if(message.type!=='location')return;
    currentId=message.stage||currentId;updateRail(currentId);
    try{history.replaceState({qmFrame:true},'',cleanUrl(message.url))}catch(_){}
  });
  addEventListener('popstate',()=>{if(frame)frame.src=embeddedUrl(location.href)});
  addEventListener('qm-language-change',refreshRailLanguage);
  addEventListener('qm-theme-change',sendShellState);
  new MutationObserver(refreshRailLanguage).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();
