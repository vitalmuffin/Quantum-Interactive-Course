(()=>{
'use strict';
const page=(document.body?.dataset.coursePage||location.pathname.split('/').pop()||'index.html').replace(/^\//,'');
const state=window.QMState;
if(!state){console.warn('QMState is unavailable; progress tracking is disabled.');return}
state.markPageOpened(page);
window.QMProgress=Object.freeze({
  load:state.load,
  save:state.save,
  markPaper:id=>state.markPaper(id,true),
  markQuiz:(id,ok)=>state.markQuiz(id,ok),
  markComplete:(id=page,value=true)=>state.markPageComplete(id,value),
  reset:state.reset
});
})();
