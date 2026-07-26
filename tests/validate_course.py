
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,parse_qs,unquote
import json,re,sys
root=Path(__file__).resolve().parents[1]
htmls=list(root.glob("*.html"))
soups={p.name:BeautifulSoup(p.read_text(encoding="utf-8"),"html.parser") for p in htmls}
ids={n:{x.get("id") for x in s.find_all(id=True)} for n,s in soups.items()}
papers={p["folder"] for p in json.load(open(root/"data/source_index.json",encoding="utf-8"))["papers"]}
errors=[];warnings=[];links=0
for name,soup in soups.items():
 for tag in soup.find_all(True):
  for attr in ("href","src","data"):
   val=tag.get(attr)
   if not val or val.startswith(("http:","https:","mailto:","javascript:","data:")):continue
   if val.startswith("#"):
    if val[1:] and val[1:] not in ids[name]: errors.append(f"{name}: missing anchor {val}")
    continue
   u=urlsplit(val); path=unquote(u.path); frag=u.fragment
   if not path: continue
   links+=1
   target=(root/path).resolve()
   try: target.relative_to(root.resolve())
   except ValueError: warnings.append(f"{name}: outside path {val}");continue
   if not target.exists(): errors.append(f"{name}: missing {val}")
   if path.endswith(".html") and frag and Path(path).name in ids and frag not in ids[Path(path).name]:
    errors.append(f"{name}: missing cross anchor {val}")
   if Path(path).name=="source_reader.html":
    q=parse_qs(u.query); paper=(q.get("paper") or [None])[0]
    if paper and paper not in papers: errors.append(f"{name}: unknown paper {paper}")
# source-index assets
data=json.load(open(root/"data/source_index.json",encoding="utf-8"))["papers"]
for p in data:
 for k in ["pdf_path","summary_de_path","summary_en_path","original_path","german_path","english_path"]:
  v=p.get(k)
  if v and not (root/v).exists(): errors.append(f"source_index {p['folder']}: missing {k} {v}")
 for e in p.get("equations",[]):
  pg=e.get("page")
  if pg and not (root/f"sources/{p['folder']}/pages/page-{pg}/markdown.md").exists():
   warnings.append(f"{p['folder']}: equation page {pg} missing markdown")
# structural
expect={"primer.html":7,"historical_core.html":15,"foundations_tests.html":9,"quantum_information.html":9}
for n,c in expect.items():
 if "course-shell.js" not in (root/n).read_text(): errors.append(f"{n}: shell missing")
 if n=="primer.html":
  if len(soups[n].select(".primer-foundation"))!=7:errors.append("primer foundations !=7")
  if len(soups[n].select(".lab-after"))!=7:errors.append("primer formula blocks !=7")
 else:
  if len(soups[n].select(".lab-card"))!=c:errors.append(f"{n}: lab count")
  if len(soups[n].select(".source-inline-card"))!=c:errors.append(f"{n}: source cards")
  if len(soups[n].select(".formula-symbols"))!=c:errors.append(f"{n}: symbol legends")
  if any("\\underbrace" in (m.get("data-tex-de") or "") for m in soups[n].select(".formula-card .math")): errors.append(f"{n}: underbrace remains")
# index
idx=soups["index.html"]
for x in ["intro","map","labs"]:
 if x not in ids["index.html"]:errors.append(f"index missing {x}")
for mid in ["blackbodyFormula","waveFormula"]:
 m=idx.find(id=mid); art=m.find_parent("article") if m else None
 kids=[x for x in art.children if getattr(x,"name",None)] if art else []
 vi=max((i for i,x in enumerate(kids) if x.get("id") in ("blackbodyPlot",) or "canvas-wrap" in (x.get("class") or [])),default=-1)
 fi=next((i for i,x in enumerate(kids) if "formula-box" in (x.get("class") or [])), -1)
 if fi<=vi:errors.append(f"index {mid}: formula not after visual")
# v0.10 integration checks
for n in ["index.html","primer.html","prehistory.html","historical_core.html","foundations_tests.html","quantum_information.html","source_reader.html"]:
 if not soups[n].select_one("header.course-shell-static"): errors.append(f"{n}: pre-rendered shell missing")
 if "vendor/course-shell.css" not in (root/n).read_text(encoding="utf-8"): errors.append(f"{n}: blue shell CSS missing")
if not (root/"data/source_offline_bundle.js").exists(): errors.append("offline source bundle missing")
sr=(root/"source_reader.html").read_text(encoding="utf-8")
if "source_offline_bundle.js" not in sr or "source_index_bundle.js" in sr: errors.append("source reader not using offline bundle")
if soups["source_reader.html"].select_one("#fullSummary").has_attr("open"): errors.append("full summary open by default")
if len(soups["primer.html"].select(".foundation-item .plain-explanation")) < 20: errors.append("primer explanations not expanded")
if any(a.get("href","").startswith("index.html#map") for a in soups["primer.html"].select(".mini-map a")): errors.append("primer bridge still returns to intro")
if not soups["historical_core.html"].find(id="oscillator"): errors.append("harmonic oscillator missing")
print(f"HTML={len(htmls)} links={links} papers={len(papers)}")
print(f"errors={len(errors)} warnings={len(warnings)}")
for e in errors[:100]:print("ERROR",e)
for w in warnings[:30]:print("WARN",w)
sys.exit(1 if errors else 0)
