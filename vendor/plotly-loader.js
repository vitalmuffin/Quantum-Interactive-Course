(()=>{
'use strict';
let real=null,pending=null;
function load(){
  if(real)return Promise.resolve(real);
  if(pending)return pending;
  const shim=window.Plotly;
  pending=new Promise((resolve,reject)=>{
    const script=document.createElement('script');
    script.src='vendor/plotly-3.3.1.min.js';
    script.async=true;
    script.onload=()=>{
      if(window.Plotly===shim){reject(new Error('Plotly bundle did not replace the loader shim'));return}
      real=window.Plotly;resolve(real);
    };
    script.onerror=()=>reject(new Error('Could not load local Plotly bundle'));
    document.head.appendChild(script);
  });
  return pending;
}
const call=(name,args)=>load().then(api=>api[name](...args));
const shim={
  react(...args){return call('react',args)},
  newPlot(...args){return call('newPlot',args)},
  purge(...args){return call('purge',args)},
  Plots:{resize(...args){return load().then(api=>api.Plots.resize(...args))}},
  ready:load
};
window.Plotly=shim;
window.QMPlotly={ready:load};
})();
