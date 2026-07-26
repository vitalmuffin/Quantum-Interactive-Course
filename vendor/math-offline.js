(()=>{
  'use strict';

  const renderTokens=new WeakMap();
  const ready=()=>Promise.resolve(window.MathJax?.startup?.promise);

  function fallback(el,tex,error){
    if(!el?.isConnected)return;
    el.classList.remove('qm-math-pending');
    el.classList.add('qm-math-error');
    el.textContent=tex;
    if(error)console.warn('Math rendering failed:',error);
  }

  async function render(tex,el,options={}){
    if(!el)return;
    const display=options.displayMode!==false;
    const source=String(tex??'').trim();
    const old=el.dataset.qmRenderedTex;
    if(old===source&&el.querySelector('mjx-container,svg.math-fallback'))return;

    const token=(renderTokens.get(el)||0)+1;
    renderTokens.set(el,token);
    el.dataset.qmRenderedTex=source;
    el.classList.add('qm-math-pending');
    el.classList.remove('qm-math-error');
    el.setAttribute('aria-label',source);

    try{
      await ready();
      if(renderTokens.get(el)!==token||!el.isConnected)return;
      if(!window.MathJax?.tex2svgPromise)throw new Error('MathJax tex2svgPromise is unavailable');
      const node=await window.MathJax.tex2svgPromise(source,{display});
      if(renderTokens.get(el)!==token||!el.isConnected)return;
      el.replaceChildren(node);
      el.classList.remove('qm-math-pending');
    }catch(error){
      if(renderTokens.get(el)===token)fallback(el,source,error);
    }
  }

  async function typeset(root=document){
    try{
      await ready();
      if(!root?.isConnected&&root!==document)return;
      if(window.MathJax?.typesetPromise)await window.MathJax.typesetPromise([root]);
      root.classList?.add('math-ready');
    }catch(error){
      console.warn('Document math typesetting failed:',error);
    }
  }

  window.temml={
    render(tex,el,options={}){render(tex,el,options)}
  };
  window.QMMath={render,typeset,ready};
})();
