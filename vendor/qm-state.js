(()=>{
'use strict';
const config=window.QM_COURSE_CONFIG||{};
const progressConfig=config.progress||{};
const KEY=progressConfig.key||'qm_course_progress_v1';
const LEGACY=progressConfig.legacyKeys||['quantum_course_progress_v011','qm_course_progress_v07'];
const empty=()=>({
  schemaVersion:progressConfig.schemaVersion||1,
  courseVersion:config.courseVersion||'0.16',
  stages:{},sections:{},quizzes:{},papers:{},pages:{},
  settings:{language:'de',theme:'dark',railExpanded:false},
  migrations:{}
});
const clone=value=>JSON.parse(JSON.stringify(value));
function parse(key){try{return JSON.parse(localStorage.getItem(key)||'null')}catch(_){return null}}
function merge(target,source){
  if(!source||typeof source!=='object')return target;
  for(const [key,value] of Object.entries(source)){
    if(value&&typeof value==='object'&&!Array.isArray(value)){
      target[key]=merge(target[key]&&typeof target[key]==='object'?target[key]:{},value);
    }else if(key==='scroll'&&typeof value==='number'){
      target[key]=Math.max(Number(target[key])||0,value);
    }else if(typeof value==='boolean'){
      target[key]=Boolean(target[key])||value;
    }else if(target[key]===undefined||target[key]===null||target[key]===''){
      target[key]=value;
    }else if(key==='lastTest'||key==='opened'||key==='updatedAt'){
      target[key]=String(target[key])>String(value)?target[key]:value;
    }
  }
  return target;
}
function migrate(){
  const canonical=parse(KEY);
  const state=merge(empty(),canonical||{});
  for(const legacyKey of LEGACY){
    if(state.migrations?.[legacyKey])continue;
    const legacy=parse(legacyKey);
    if(!legacy)continue;
    merge(state,legacy);
    state.migrations[legacyKey]={importedAt:new Date().toISOString()};
  }
  const language=localStorage.getItem(config.settings?.languageKey||'qm_language');
  const theme=localStorage.getItem(config.settings?.themeKey||'qm_theme');
  const rail=localStorage.getItem(config.settings?.railKey||'qm_stage_rail_expanded');
  if(language==='de'||language==='en')state.settings.language=language;
  if(theme==='dark'||theme==='light')state.settings.theme=theme;
  if(rail!==null)state.settings.railExpanded=rail==='1';
  state.schemaVersion=progressConfig.schemaVersion||1;
  state.courseVersion=config.courseVersion||state.courseVersion;
  save(state,{silent:true});
  return state;
}
function normalize(state){return merge(empty(),state||{})}
function load(){return normalize(parse(KEY)||migrate())}
function save(state,{silent=false}={}){
  const next=normalize(clone(state));
  next.schemaVersion=progressConfig.schemaVersion||1;
  next.courseVersion=config.courseVersion||next.courseVersion;
  next.updatedAt=new Date().toISOString();
  try{
    localStorage.setItem(KEY,JSON.stringify(next));
    if(!silent)dispatchEvent(new CustomEvent('qm-progress-change',{detail:{state:clone(next)}}));
    return true;
  }catch(error){console.warn('Could not save course state:',error);return false}
}
function update(mutator){const state=load();mutator(state);save(state);return state}
function setSetting(name,value){
  return update(state=>{state.settings[name]=value;});
}
function setLanguage(language){
  if(language!=='de'&&language!=='en')return load();
  try{localStorage.setItem(config.settings?.languageKey||'qm_language',language)}catch(_){}
  return setSetting('language',language);
}
function setTheme(theme){
  if(theme!=='dark'&&theme!=='light')return load();
  try{localStorage.setItem(config.settings?.themeKey||'qm_theme',theme)}catch(_){}
  return setSetting('theme',theme);
}
function setRailExpanded(expanded){
  try{localStorage.setItem(config.settings?.railKey||'qm_stage_rail_expanded',expanded?'1':'0')}catch(_){}
  return setSetting('railExpanded',Boolean(expanded));
}
function markPageOpened(page){return update(s=>{s.pages[page]=s.pages[page]||{};s.pages[page].opened=new Date().toISOString()})}
function markPageComplete(page,value=true){return update(s=>{s.pages[page]=s.pages[page]||{};s.pages[page].complete=Boolean(value)})}
function markPaper(id,value=true){return update(s=>{s.papers[String(id)]=Boolean(value)})}
function markQuiz(id,correct){return update(s=>{s.quizzes[id]=s.quizzes[id]||{};s.quizzes[id].attempted=true;s.quizzes[id].passed=Boolean(correct);s.quizzes[id].lastTest=new Date().toISOString()})}
function markSection(id,correct){return update(s=>{s.sections[id]=s.sections[id]||{};s.sections[id].attempted=true;s.sections[id].passed=Boolean(correct);s.sections[id].lastTest=new Date().toISOString()})}
function updateStageScroll(id,fraction){
  const state=load(),next=Math.max(0,Math.min(1,Number(fraction)||0));
  state.stages[id]=state.stages[id]||{};
  const current=Number(state.stages[id].scroll)||0;
  if(next<=current||next-current<0.004&&next<0.995)return state;
  state.stages[id].scroll=next>=0.995?1:next;
  save(state,{silent:true});return state;
}
function reset(){
  try{localStorage.removeItem(KEY);LEGACY.forEach(key=>localStorage.removeItem(key))}catch(_){}
  const state=empty();LEGACY.forEach(key=>{state.migrations[key]={clearedAt:new Date().toISOString()}});save(state);return state;
}
const initial=migrate();
window.QMState=Object.freeze({KEY,LEGACY,load,save,update,reset,setLanguage,setTheme,setRailExpanded,markPageOpened,markPageComplete,markPaper,markQuiz,markSection,updateStageScroll,get settings(){return load().settings}});
})();
