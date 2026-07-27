(()=>{
'use strict';
let pending=null;
function ready(){
  if(window.QM_COURSE_DATA)return Promise.resolve(window.QM_COURSE_DATA);
  if(pending)return pending;
  pending=new Promise((resolve,reject)=>{
    const script=document.createElement('script');
    const version=window.QM_COURSE_CONFIG?.courseVersion||'0.16';
    script.src=`data/course_data.bundle.js?v=${encodeURIComponent(version)}`;
    script.async=true;
    script.onload=()=>window.QM_COURSE_DATA?resolve(window.QM_COURSE_DATA):reject(new Error('Full course data bundle loaded without data'));
    script.onerror=()=>reject(new Error('Could not load full paper details'));
    document.head.appendChild(script);
  });
  return pending;
}
window.QMData=Object.freeze({ready,get overview(){return window.QM_COURSE_OVERVIEW},get loaded(){return Boolean(window.QM_COURSE_DATA)}});
})();
