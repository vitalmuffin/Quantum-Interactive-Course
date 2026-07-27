(()=>{
'use strict';
const tokens=new WeakMap();
const sleep=ms=>new Promise(resolve=>setTimeout(resolve,ms));
function normalizeTex(value){
  let source=String(value??'').trim();
  for(const [open,close] of [['\\[','\\]'],['$$','$$'],['\\(','\\)'],['$','$']]){
    if(source.startsWith(open)&&source.endsWith(close)&&source.length>=open.length+close.length){
      source=source.slice(open.length,source.length-close.length).trim();break;
    }
  }
  return source;
}
async function ready(timeoutMs=15000){
  const started=Date.now();
  while(!window.MathJax?.tex2svgPromise){
    try{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise}catch(error){console.warn('MathJax startup failed:',error)}
    if(window.MathJax?.tex2svgPromise)break;
    if(Date.now()-started>=timeoutMs)throw new Error('MathJax tex2svgPromise did not become available');
    await sleep(35);
  }
  return window.MathJax;
}
function resolveArguments(first,second,third){
  if(first instanceof Element)return{el:first,tex:second,options:typeof third==='boolean'?{displayMode:third}:(third||{})};
  return{tex:first,el:second,options:typeof third==='boolean'?{displayMode:third}:(third||{})};
}
function fallback(el,tex,error){
  if(!el?.isConnected)return false;
  el.classList.remove('qm-math-pending');el.classList.add('qm-math-error');
  el.textContent=`\\[${tex}\\]`;if(error)console.warn('Math rendering failed:',error);return false;
}
async function render(first,second,third={}){
  const {el,tex,options}=resolveArguments(first,second,third);
  if(!(el instanceof Element))return false;
  const source=normalizeTex(tex);const display=options.displayMode!==false;
  if(!source){el.replaceChildren();return true}
  if(el.dataset.qmRenderedTex===source&&el.querySelector('mjx-container,svg.math-fallback'))return true;
  const token=(tokens.get(el)||0)+1;tokens.set(el,token);
  el.dataset.qmRenderedTex=source;el.classList.add('qm-math-pending');el.classList.remove('qm-math-error');el.setAttribute('aria-label',source);
  let lastError;
  for(let attempt=0;attempt<3;attempt++){
    try{
      const mathjax=await ready();
      if(tokens.get(el)!==token||!el.isConnected)return false;
      const node=await mathjax.tex2svgPromise(source,{display});
      if(tokens.get(el)!==token||!el.isConnected)return false;
      el.replaceChildren(node);el.classList.remove('qm-math-pending','qm-math-error');return true;
    }catch(error){lastError=error;if(attempt<2)await sleep(90*(attempt+1))}
  }
  if(tokens.get(el)===token)return fallback(el,source,lastError);return false;
}
function texFromElement(el){
  const language=document.documentElement.lang?.startsWith('en')?'en':'de';
  if(language==='en'&&el.dataset.texEn)return el.dataset.texEn;
  if(language==='de'&&el.dataset.texDe)return el.dataset.texDe;
  if(el.dataset.tex||el.dataset.latex)return el.dataset.tex||el.dataset.latex;
  if(el.dataset.texDe||el.dataset.texEn)return el.dataset.texDe||el.dataset.texEn;
  const raw=el.textContent?.trim()||'';
  if(/^\\\[[\s\S]*\\\]$/.test(raw)||/^\$\$[\s\S]*\$\$$/.test(raw)||/^\\\([\s\S]*\\\)$/.test(raw))return raw;
  if(el.classList.contains('math-block')||el.classList.contains('math'))return raw;
  return'';
}
function collect(root=document){
  const candidates=new Set();
  const selector='[data-tex],[data-latex],[data-tex-de],[data-tex-en],.math,.math-block,[id$="Formula"]';
  if(root instanceof Element&&root.matches(selector))candidates.add(root);
  root.querySelectorAll?.(selector).forEach(el=>candidates.add(el));
  return candidates;
}
async function renderMarked(root=document,{force=false}={}){
  const jobs=[];
  for(const el of collect(root)){
    const tex=texFromElement(el);if(!tex)continue;
    if(!force&&el.dataset.qmRenderedTex===normalizeTex(tex)&&el.querySelector('mjx-container'))continue;
    jobs.push(render(tex,el,{displayMode:!el.classList.contains('math-inline')}));
  }
  return Promise.allSettled(jobs);
}
async function typeset(root=document){
  try{
    const mathjax=await ready();await renderMarked(root);
    if(mathjax.typesetPromise)await mathjax.typesetPromise([root]);
    root.classList?.add('math-ready');return true;
  }catch(error){console.warn('Document math typesetting failed:',error);return false}
}
window.QMMathCore=Object.freeze({normalizeTex,ready,render,renderMarked,typeset,texFromElement});
})();
