(()=>{
'use strict';
const config=window.QM_COURSE_CONFIG||{};
const stages=config.stages||[];
const CHANNEL='qm-course-v1';
let adapter={};
const $=(selector,root=document)=>root.querySelector(selector);
const fileFromUrl=url=>{try{return new URL(url,location.href).pathname.split('/').pop()||'index.html'}catch(_){return'index.html'}};
function language(){return document.documentElement.lang?.startsWith('en')?'en':(window.QMState?.settings?.language||'de')}
function stageFromLocation(path=fileFromUrl(location.href),hash=location.hash){
  const clean=String(hash||'').replace(/^#/,'');
  for(const stage of stages){
    if(!(stage.pages||[]).includes(path))continue;
    if(path!=='historical_core.html')return stage.id;
    if((stage.anchors||[]).includes(clean))return stage.id;
  }
  if(path==='historical_core.html')return'photons';
  return stages.find(s=>(s.pages||[]).includes(path))?.id||'intro';
}
function stageForCourseLink(raw){
  let url;try{url=new URL(raw,location.href)}catch(_){return null}
  if(location.protocol!=='file:'&&url.origin!==location.origin)return null;
  const path=fileFromUrl(url.href);
  if(path==='index.html'&&url.hash&&!['','#top'].includes(url.hash))return null;
  if(!stages.some(stage=>(stage.pages||[]).includes(path)))return null;
  return stageFromLocation(path,url.hash);
}
function cleanUrl(raw){
  const url=new URL(raw,location.href);url.searchParams.delete('embedded');
  return fileFromUrl(url.href)+(url.search||'')+(url.hash||'');
}
function embeddedUrl(raw){
  const url=new URL(raw,location.href);url.searchParams.set('embedded','1');
  return fileFromUrl(url.href)+url.search+(url.hash||'');
}
function targetOrigin(){return location.protocol==='file:'?'*':location.origin}
function trustedMessage(event,expectedSource){
  if(expectedSource&&event.source!==expectedSource)return false;
  if(location.protocol==='file:')return event.origin==='null'||event.origin==='';
  return event.origin===location.origin;
}
function post(target,type,payload={}){target?.postMessage?.({channel:CHANNEL,type,...payload},targetOrigin())}
function applyTranslatedText(next){
  document.documentElement.lang=next;
  document.querySelectorAll('[data-de][data-en]').forEach(node=>{
    const value=node.dataset[next];if(value!==undefined)node.textContent=value;
  });
}
function legacyLanguage(next){
  const selector=next==='de'?'#langDE,#deBtn':'#langEN,#enBtn';
  const button=$(selector);if(button){button.click();return true}return false;
}
function setLanguage(next){
  if(next!=='de'&&next!=='en')return;
  window.QMState?.setLanguage(next);
  if(typeof adapter.setLanguage==='function')adapter.setLanguage(next);
  else if(!legacyLanguage(next))applyTranslatedText(next);
  document.documentElement.lang=next;
  dispatchEvent(new CustomEvent('qm-language-change',{detail:{language:next}}));
}
function legacyTheme(next){
  const button=$('#themeToggle,#themeBtn,#theme');
  if(!button)return false;
  const current=document.documentElement.dataset.theme||'dark';
  if(current!==next)button.click();return true;
}
function setTheme(next){
  if(next!=='dark'&&next!=='light')return;
  window.QMState?.setTheme(next);
  if(typeof adapter.setTheme==='function')adapter.setTheme(next);
  else if(!legacyTheme(next))document.documentElement.dataset.theme=next;
  dispatchEvent(new CustomEvent('qm-theme-change',{detail:{theme:next}}));
}
function register(next={}){adapter={...adapter,...next};return()=>{adapter={}}}
function notifyLocation(){
  if(parent===window)return;
  post(parent,'location',{url:location.href,stage:stageFromLocation()});
}

function decimalsForStep(step){
  const raw=String(step);
  if(raw.includes('e-'))return Number(raw.split('e-')[1])||0;
  return (raw.split('.')[1]||'').length;
}
function enhanceRange(input){
  const InputCtor=window.HTMLInputElement;
  if(!InputCtor||!(input instanceof InputCtor)||input.type!=='range'||input.dataset.qmRangeEnhanced)return;
  input.dataset.qmRangeEnhanced='1';
  input.classList.add('qm-range-enhanced');
  let activePointer=null;
  const updateFromPointer=event=>{
    const rect=input.getBoundingClientRect();
    if(!rect.width)return;
    const min=Number(input.min||0),max=Number(input.max||100);
    const stepRaw=input.step&&input.step!=='any'?Number(input.step):null;
    let ratio=Math.min(1,Math.max(0,(event.clientX-rect.left)/rect.width));
    if(getComputedStyle(input).direction==='rtl')ratio=1-ratio;
    let value=min+ratio*(max-min);
    if(stepRaw&&Number.isFinite(stepRaw)&&stepRaw>0){
      value=min+Math.round((value-min)/stepRaw)*stepRaw;
      value=Number(value.toFixed(decimalsForStep(stepRaw)));
    }
    value=Math.min(max,Math.max(min,value));
    if(String(input.value)!==String(value)){
      input.value=String(value);
      input.dispatchEvent(new Event('input',{bubbles:true}));
    }
  };
  input.addEventListener('pointerdown',event=>{
    if(event.button!==0||activePointer!==null)return;
    activePointer=event.pointerId;
    input.focus?.({preventScroll:true});
    input.setPointerCapture?.(event.pointerId);
    updateFromPointer(event);
    event.preventDefault();
  });
  input.addEventListener('pointermove',event=>{
    if(event.pointerId!==activePointer)return;
    updateFromPointer(event);
    event.preventDefault();
  });
  const finish=event=>{
    if(event.pointerId!==activePointer)return;
    updateFromPointer(event);
    input.releasePointerCapture?.(event.pointerId);
    activePointer=null;
    input.dispatchEvent(new Event('change',{bubbles:true}));
    event.preventDefault();
  };
  input.addEventListener('pointerup',finish);
  input.addEventListener('pointercancel',event=>{
    if(event.pointerId===activePointer){activePointer=null;input.dispatchEvent(new Event('change',{bubbles:true}))}
  });
}
function enhanceRanges(root=document){
  const InputCtor=window.HTMLInputElement;
  if(InputCtor&&root instanceof InputCtor)enhanceRange(root);
  root.querySelectorAll?.('input[type="range"]').forEach(enhanceRange);
}
function initializeRangeControls(){
  enhanceRanges(document);
  if(typeof MutationObserver==='undefined'||!document.documentElement)return;
  new MutationObserver(records=>{
    for(const record of records)for(const node of record.addedNodes)if(node.nodeType===1)enhanceRanges(node);
  }).observe(document.documentElement,{childList:true,subtree:true});
}
function initializeSettings(){
  const settings=window.QMState?.settings||{};
  setLanguage(settings.language==='en'?'en':'de');
  setTheme(settings.theme==='light'?'light':'dark');
}
window.QMPage=Object.freeze({CHANNEL,stages,language,register,setLanguage,setTheme,stageFromLocation,stageForCourseLink,cleanUrl,embeddedUrl,targetOrigin,trustedMessage,post,notifyLocation,initializeSettings,enhanceRanges,fileFromUrl});
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initializeRangeControls,{once:true});else initializeRangeControls();
})();
