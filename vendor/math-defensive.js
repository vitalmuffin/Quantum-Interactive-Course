(()=>{
'use strict';
let observer=null,timer=0;
const core=()=>window.QMMathCore;
function schedule(root=document,delay=45){clearTimeout(timer);timer=setTimeout(()=>core()?.renderMarked(root),delay)}
function start(mode='hybrid'){
  stop();
  if(mode==='explicit')return;
  const full=mode==='defensive';
  observer=new MutationObserver(records=>{
    if(full){
      if(records.some(record=>record.addedNodes.length||record.type==='characterData'))schedule(document);return;
    }
    const roots=[];
    for(const record of records){
      record.addedNodes.forEach(node=>{if(node.nodeType===Node.ELEMENT_NODE)roots.push(node)});
    }
    if(!roots.length)return;
    clearTimeout(timer);timer=setTimeout(()=>roots.forEach(root=>core()?.renderMarked(root)),35);
  });
  observer.observe(document.documentElement,{subtree:true,childList:true,characterData:full});
  setTimeout(()=>core()?.renderMarked(document),250);
  if(full)setTimeout(()=>core()?.renderMarked(document,{force:true}),1200);
}
function stop(){observer?.disconnect();observer=null;clearTimeout(timer)}
window.QMMathDefensive=Object.freeze({start,stop,schedule});
})();
