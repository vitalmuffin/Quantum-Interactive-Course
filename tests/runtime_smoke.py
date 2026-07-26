
from pathlib import Path
from bs4 import BeautifulSoup
import json,subprocess,sys
R=Path(__file__).resolve().parents[1]
P={"primer.html":"void 0","historical_core.html":"renderAll()","foundations_tests.html":"renderAll()","quantum_information.html":"renderAll()"}
M=r"""
const vm=require('vm'),raw=RAW,no=()=>{};
const cx=new Proxy({},{get:(t,p)=>p==='measureText'?(s=>({width:String(s).length*7})):p==='createLinearGradient'?(()=>({addColorStop:no})):no});
let dummy;
function el(id,p={}){return new Proxy({id,value:p.value||'',checked:!!p.checked,textContent:p.text||'',innerHTML:p.html||'',clientWidth:800,clientHeight:420,width:800,height:420,max:p.max||'',min:p.min||'',style:{setProperty:no},dataset:p.dataset||{},classList:{add:no,remove:no,toggle:()=>false,contains:()=>false},addEventListener:no,removeEventListener:no,setAttribute:no,getAttribute:k=>p[k]||null,appendChild:no,prepend:no,insertBefore:no,remove:no,focus:no,click:no,querySelector:()=>dummy,querySelectorAll:()=>[],getBoundingClientRect:()=>({width:800,height:420}),getContext:()=>cx},{get:(t,k)=>t[k],set:(t,k,v)=>(t[k]=v,true)})}
const E={};for(const [i,p] of Object.entries(raw))E[i]=el(i,p);dummy=el('dummy');
const de=el('html',{dataset:{theme:'dark'}});de.lang='de';de.style={setProperty:no};const body=el('body');
const document={readyState:'loading',documentElement:de,body,getElementById:i=>E[i]||dummy,querySelector:s=>s&&s[0]==='#'?(E[s.slice(1)]||dummy):dummy,querySelectorAll:()=>[],createElement:t=>el(t),createElementNS:(n,t)=>el(t),addEventListener:no};
const C={console,Math,JSON,Date,URLSearchParams,Array,Object,Number,String,Boolean,RegExp,Map,Set,Float64Array,Uint8ClampedArray,document,location:{pathname:'/x.html',hash:'',search:''},history:{replaceState:no},navigator:{language:'de'},localStorage:{getItem:()=>null,setItem:no,removeItem:no},performance:{now:()=>1000},requestAnimationFrame:()=>0,cancelAnimationFrame:no,setTimeout:()=>0,clearTimeout:no,setInterval:()=>0,clearInterval:no,ResizeObserver:class{observe(){}},IntersectionObserver:class{observe(){} disconnect(){}},MutationObserver:class{observe(){}},CustomEvent:class{},getComputedStyle:()=>new Proxy({},{get:(t,p)=>p==='getPropertyValue'?(()=> '#6ee7c2'):'#6ee7c2'}),Plotly:{react:()=>Promise.resolve()},temml:{render:no},confirm:()=>true,Image:class{},Path2D:class{},devicePixelRatio:1};C.window=C;C.window.addEventListener=no;C.window.matchMedia=()=>({matches:false,addEventListener:no});for(const [i,e] of Object.entries(E))C[i]=e;vm.createContext(C);vm.runInContext(CODE,C,{timeout:10000,filename:NAME});
"""
bad=[]
for name,call in P.items():
 s=BeautifulSoup((R/name).read_text(encoding="utf-8"),"html.parser");d={}
 for x in s.find_all(id=True):
  d[x["id"]]={"value":((x.find("option",selected=True) or x.find("option")).get("value","") if x.name=="select" and x.find("option") else x.get("value","")),"checked":x.has_attr("checked"),"text":x.get_text(),"html":"".join(map(str,x.contents)),"max":x.get("max",""),"min":x.get("min",""),"dataset":{k[5:]:v for k,v in x.attrs.items() if k.startswith("data-")}}
 code="\n".join((x.string or x.get_text()) for x in s.find_all("script") if not x.get("src") and (not x.get("type") or x.get("type") in ("text/javascript","application/javascript","module")))
 code+=f'\n{call};console.log("SMOKE_OK {name}")'
 js=M.replace("RAW",json.dumps(d)).replace("CODE",json.dumps(code)).replace("NAME",json.dumps(name))
 js=js.replace("readyState:'loading'","readyState:'complete'") if name=="primer.html" else js
 q=Path("/tmp")/("smoke_"+name.replace(".html",".js"));q.write_text(js)
 r=subprocess.run(["node",str(q)],capture_output=True,text=True)
 print(name,"PASS" if r.returncode==0 else "FAIL")
 if r.returncode: print(r.stderr[-1500:]);bad.append(name)
sys.exit(bool(bad))
