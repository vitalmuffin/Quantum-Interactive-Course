(()=>{
  'use strict';

  const renderTokens=new WeakMap();
  const sleep=ms=>new Promise(resolve=>setTimeout(resolve,ms));

  function normalizeTex(value){
    let source=String(value??'').trim();
    const pairs=[['\\[','\\]'],['$$','$$'],['\\(','\\)'],['$','$']];
    for(const [open,close] of pairs){
      if(source.startsWith(open)&&source.endsWith(close)&&source.length>=open.length+close.length){
        source=source.slice(open.length,source.length-close.length).trim();
        break;
      }
    }
    return source;
  }

  function resolveArguments(first,second,third){
    if(first instanceof Element){
      return {el:first,tex:second,options:typeof third==='boolean'?{displayMode:third}:(third||{})};
    }
    return {tex:first,el:second,options:typeof third==='boolean'?{displayMode:third}:(third||{})};
  }

  async function ready(timeoutMs=12000){
    const started=Date.now();
    while(!window.MathJax?.tex2svgPromise){
      const startupPromise=window.MathJax?.startup?.promise;
      if(startupPromise){
        try{await startupPromise}catch(error){console.warn('MathJax startup failed:',error)}
      }
      if(window.MathJax?.tex2svgPromise)break;
      if(Date.now()-started>=timeoutMs)throw new Error('MathJax tex2svgPromise did not become available');
      await sleep(30);
    }
    return window.MathJax;
  }

  function fallback(el,tex,error){
    if(!el?.isConnected)return;
    el.classList.remove('qm-math-pending');
    el.classList.add('qm-math-error');
    el.textContent=`\\[${tex}\\]`;
    if(error)console.warn('Math rendering failed:',error);
  }

  async function render(first,second,third={}){
    const {tex,el,options}=resolveArguments(first,second,third);
    if(!(el instanceof Element))return false;
    const display=options.displayMode!==false;
    const source=normalizeTex(tex);
    if(!source){el.replaceChildren();return true}

    const old=el.dataset.qmRenderedTex;
    if(old===source&&el.querySelector('mjx-container,svg.math-fallback'))return true;

    const token=(renderTokens.get(el)||0)+1;
    renderTokens.set(el,token);
    el.dataset.qmRenderedTex=source;
    el.classList.add('qm-math-pending');
    el.classList.remove('qm-math-error');
    el.setAttribute('aria-label',source);

    let lastError;
    for(let attempt=0;attempt<3;attempt++){
      try{
        const mathjax=await ready();
        if(renderTokens.get(el)!==token||!el.isConnected)return false;
        const node=await mathjax.tex2svgPromise(source,{display});
        if(renderTokens.get(el)!==token||!el.isConnected)return false;
        el.replaceChildren(node);
        el.classList.remove('qm-math-pending','qm-math-error');
        return true;
      }catch(error){
        lastError=error;
        if(attempt<2)await sleep(80*(attempt+1));
      }
    }
    if(renderTokens.get(el)===token)fallback(el,source,lastError);
    return false;
  }

  function texFromElement(el){
    if(el.dataset.tex)return el.dataset.tex;
    if(el.dataset.latex)return el.dataset.latex;
    const language=document.documentElement.lang?.startsWith('en')?'en':'de';
    if(language==='en'&&el.dataset.texEn)return el.dataset.texEn;
    if(language==='de'&&el.dataset.texDe)return el.dataset.texDe;
    if(el.dataset.texDe||el.dataset.texEn)return el.dataset.texDe||el.dataset.texEn;
    const raw=el.textContent?.trim()||'';
    if(/^\\\[[\s\S]*\\\]$/.test(raw)||/^\$\$[\s\S]*\$\$$/.test(raw)||/^\\\([\s\S]*\\\)$/.test(raw))return raw;
    if(el.classList.contains('math-block')||el.classList.contains('math'))return raw;
    return '';
  }

  async function renderMarked(root=document){
    if(!root)return;
    const scope=root===document?document:root;
    const candidates=new Set();
    if(scope instanceof Element&&scope.matches('[data-tex],[data-latex],.math,.math-block,[id$="Formula"]'))candidates.add(scope);
    scope.querySelectorAll?.('[data-tex],[data-latex],.math,.math-block,[id$="Formula"]').forEach(el=>candidates.add(el));
    const jobs=[];
    for(const el of candidates){
      if(el.querySelector('mjx-container')&&!el.classList.contains('qm-math-error'))continue;
      const tex=texFromElement(el);
      if(!tex)continue;
      const display=!el.classList.contains('math-inline');
      jobs.push(render(tex,el,{displayMode:display}));
    }
    await Promise.allSettled(jobs);
  }

  async function typeset(root=document){
    try{
      const mathjax=await ready();
      if(!root?.isConnected&&root!==document)return;
      await renderMarked(root);
      if(mathjax.typesetPromise)await mathjax.typesetPromise([root]);
      root.classList?.add('math-ready');
    }catch(error){
      console.warn('Document math typesetting failed:',error);
    }
  }

  let mutationTimer=0;
  function scheduleScan(root=document){
    clearTimeout(mutationTimer);
    mutationTimer=setTimeout(()=>renderMarked(root),40);
  }

  window.temml={
    render(first,second,third={}){return render(first,second,third)}
  };
  window.QMMath={render,typeset,ready,renderMarked,normalizeTex};

  const start=()=>{
    renderMarked(document);
    const observer=new MutationObserver(records=>{
      if(records.some(record=>record.addedNodes.length||record.type==='characterData'))scheduleScan(document);
    });
    observer.observe(document.documentElement,{subtree:true,childList:true,characterData:true});
    window.__qmMathObserver=observer;
    setTimeout(()=>renderMarked(document),250);
    setTimeout(()=>renderMarked(document),1200);
  };
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
})();
