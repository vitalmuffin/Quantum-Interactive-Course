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
function initializeSettings(){
  const settings=window.QMState?.settings||{};
  setLanguage(settings.language==='en'?'en':'de');
  setTheme(settings.theme==='light'?'light':'dark');
}
window.QMPage=Object.freeze({CHANNEL,stages,language,register,setLanguage,setTheme,stageFromLocation,stageForCourseLink,cleanUrl,embeddedUrl,targetOrigin,trustedMessage,post,notifyLocation,initializeSettings,fileFromUrl});
})();
