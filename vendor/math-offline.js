(()=>{
'use strict';
const config=window.QM_COURSE_CONFIG?.math||{};
const requested=new URLSearchParams(location.search).get(config.queryParameter||'math');
const mode=(config.modes||[]).includes(requested)?requested:(config.defaultMode||'hybrid');
const core=window.QMMathCore;
window.QMMath=Object.freeze({
  mode,
  render:(...args)=>core.render(...args),
  typeset:(...args)=>core.typeset(...args),
  ready:(...args)=>core.ready(...args),
  renderMarked:(...args)=>core.renderMarked(...args),
  normalizeTex:core.normalizeTex,
  setMode(next){if(!(config.modes||[]).includes(next))throw new Error(`Unknown math mode: ${next}`);window.QMMathDefensive?.start(next);return next}
});
window.temml={render:(...args)=>core.render(...args)};
function start(){core.renderMarked(document);window.QMMathDefensive?.start(mode)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
})();
