(()=>{
  'use strict';
  const queueTypeset=(el)=>{
    if(window.MathJax?.Hub){
      window.MathJax.Hub.Queue(['Typeset',window.MathJax.Hub,el]);
      return true;
    }
    return false;
  };
  if(!window.temml){
    window.temml={
      render(tex,el,options={}){
        const display=options.displayMode!==false;
        el.textContent=display?`\\[${tex}\\]`:`\\(${tex}\\)`;
        el.classList.add('qm-math-pending');
        const run=()=>{
          if(queueTypeset(el)) el.classList.remove('qm-math-pending');
          else setTimeout(run,40);
        };
        run();
      }
    };
  }
  window.QMMath={
    render(el,tex,display=true){
      window.temml.render(tex,el,{displayMode:display,throwOnError:false});
    },
    typeset(root=document){
      if(window.MathJax?.Hub) window.MathJax.Hub.Queue(['Typeset',window.MathJax.Hub,root]);
    }
  };
})();
