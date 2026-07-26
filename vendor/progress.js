(()=>{
'use strict';
const KEY='qm_course_progress_v07';
const page=(document.body.dataset.coursePage||location.pathname.split('/').pop()||'index.html').replace(/^\//,'');
function load(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')}catch(_){return{}}}
function save(s){try{localStorage.setItem(KEY,JSON.stringify(s));dispatchEvent(new CustomEvent('qm-progress-change'));return true}catch(_){return false}}
let s=load();s.pages=s.pages||{};s.papers=s.papers||{};s.quizzes=s.quizzes||{};s.pages[page]=s.pages[page]||{opened:Date.now(),complete:false};s.pages[page].opened=Date.now();save(s);
window.QMProgress={load,save,markPaper(id){const x=load();x.papers=x.papers||{};x.papers[id]=true;save(x)},markQuiz(id,ok){const x=load();x.quizzes=x.quizzes||{};x.quizzes[id]=!!ok;save(x)},markComplete(id=page,value=true){const x=load();x.pages=x.pages||{};x.pages[id]=x.pages[id]||{};x.pages[id].complete=!!value;save(x)}};
})();
