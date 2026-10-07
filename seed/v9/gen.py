import json,glob,re,datetime,os,sys
S=sys.argv[1]; OUT=S+"/v9b"
CL="tracosdamor"; NOW="2026-10-07T15:00:00.000Z"
DIAS=["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]; DC=["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"]
its=[]
for f in sorted(glob.glob(S+"/hm/2026-*.json")):
  for x in json.load(open(f))["itens"]:
    d=x.get("data") or ""
    if not d or d>="2026-10-05" or re.match(r"^SEMANA",x.get("titulo") or "",re.I): continue
    its.append(x)
def clean(t):
  t=re.sub(r"!\[[^\]]*\]\([^)]*\)","",t)
  t=re.sub(r"\[([^\]]*)\]\((https?://[^)]+)\)",lambda m:m.group(2) if m.group(1).startswith("http") else f"{m.group(1)} {m.group(2)}",t)
  t=re.sub(r"(?m)^\s*-{3,}\s*$","",t); t=t.replace("**","")
  t=re.sub(r"(?m)^#+\s*","",t); t=re.sub(r"\n{3,}","\n\n",t)
  return t.strip()
def blocks(c):
  parts=re.split(r"(?m)^- \[[ x]\]\s+\*\*(.+?)\*\*\s*$",c or "")
  out=[("",parts[0])]
  for i in range(1,len(parts),2): out.append((parts[i].strip(),parts[i+1]))
  return out
H={"intenção":"intencao","estratégia":"estrategia","tema":"tema","como fazer":"comoFazer","texto":"texto","inspiração":"inspiracao"}
def secoes(t):
  r={}; cur=None; buf=[]; pre=[]
  for ln in t.split("\n"):
    m=re.match(r"^\s*(?:#+\s*|\*\*)\s*(Intenção|Estratégia|Tema|Como fazer|Texto|Inspiração)\s*:?\s*(?:\*\*)?\s*:?\s*(.*)$",ln,re.I)
    if m:
      if cur: r[cur]=clean("\n".join(buf))
      cur=H[m.group(1).lower()]; buf=[m.group(2)] if m.group(2).strip() else []
    elif cur: buf.append(ln)
    else: pre.append(ln)
  if cur: r[cur]=clean("\n".join(buf))
  p=clean("\n".join(pre))
  if p: r["comoFazer"]=(p+("\n\n"+r["comoFazer"] if r.get("comoFazer") else "")).strip()
  return r
def splitStories(t):
  ps=re.split(r"(?m)^\s*\*\*\s*Storie\s*\d*\s*:?\s*\*\*\s*:?\s*$|^\s*Storie\s*\d+\s*:",t)
  ps=[p for p in ps if clean(p)]
  return ps or ([t] if clean(t) else [])
def links(t,dom): return [u for u in re.findall(r"https?://[^\s)\]]+",t) if dom in u]
def uniq(l):
  o=[]; [o.append(x) for x in l if x not in o]; return o
def story(t):
  s=dict(intencao="",estrategia="",tema="",texto="",comoFazer="",inspiracao="",media="video",linkCriativo="",linkDrive="")
  s.update(secoes(t)); return s
ETAPA={"Publicado":"publicado","Aprovado":"aprovado","Copy":"criativo","Design":"criativo"}
def monday(d):
  x=datetime.date.fromisoformat(d); return (x-datetime.timedelta(days=x.weekday())).isoformat()
cards={}
for x in its:
  d=x["data"]; tit=x["titulo"].strip(); fmt=x.get("formato") or ""
  isSt = bool(re.match(r"^\s*stor",tit,re.I)) or (fmt=="Storie" and not re.search(r"feed",tit,re.I)) or (not fmt and re.search(r"stor(ie|y)",tit,re.I) and not re.search(r"feed",tit,re.I))
  if fmt=="Reels" or (not fmt and re.search(r"reel",tit,re.I)): formato="Reel"
  elif fmt=="Carrossel" or re.search(r"carross",tit,re.I): formato="Carrossel"
  else: formato="Estático"
  if isSt: formato=None
  bl=blocks(x.get("corpo") or "")
  get=lambda pat:[b for n,b in bl if re.search(pat,n,re.I)]
  design="\n".join(get(r"^Copy para Desig")+[bl[0][1]])
  stor="\n".join(get(r"Copy para Stor"))
  c=dict(cliente=CL,data=d,tipo="Storie" if isSt else "Feed",formato=formato,etapa=ETAPA.get(x.get("fase"),"ideia"),
    titulo=tit,intencao="",estrategia="",tema="",comoFazer="",inspiracao="",legenda="",linkCriativo="",linkDrive="",capaCriativo="",capaDrive="",
    stories=[],origem="notion",notionId=x.get("id"),semana=f"{CL}-{monday(d)}",criadoEm=NOW,atualizadoEm=NOW,
    historico=[{"em":NOW,"etapa":ETAPA.get(x.get("fase"),"ideia"),"por":"notion"}],
    funil=x.get("funil") or "",intencaoConteudo=x.get("intencaoConteudo") or "",acaoEsperada=x.get("acaoEsperada") or "")
  stLinks=uniq(sum([links(b,"drive.google") for n,b in bl if re.search(r"stor",n,re.I) and re.search(r"link",n,re.I)],[]))
  stCanva=uniq(sum([links(b,"canva") for n,b in bl if re.search(r"stor",n,re.I) and re.search(r"canva",n,re.I)],[]))
  if isSt:
    c["stories"]=[story(p) for p in splitStories(design)]
    if not c["stories"] and stor: c["stories"]=[story(p) for p in splitStories(stor)]
  else:
    c.update({k:v for k,v in secoes(design).items()})
    c["stories"]=[story(p) for p in splitStories(stor)] if clean(stor) else []
    c["linkDrive"]=(uniq(sum([links(b,"drive.google") for n,b in bl if re.search(r"link final",n,re.I) and not re.search(r"stor",n,re.I)],[]))+[""])[0]
    c["capaDrive"]=(uniq(sum([links(b,"drive.google") for n,b in bl if re.search(r"capa",n,re.I)],[]))+[""])[0]
    c["linkCriativo"]=(uniq(sum([links(b,"canva") for n,b in bl if re.search(r"canva",n,re.I) and not re.search(r"capa|stor",n,re.I)],[]))+[x.get("conteudoLink") or ""])[0]
    c["capaCriativo"]=(uniq(sum([links(b,"canva") for n,b in bl if re.search(r"capa",n,re.I) and re.search(r"canva",n,re.I)],[]))+[""])[0]
    c["legenda"]=clean("\n".join(get(r"^Legenda")))
  if isSt and not c["stories"]: c["stories"]=[story("")]
  for i,s in enumerate(c["stories"]):
    if i<len(stLinks): s["linkDrive"]=stLinks[i]
    if i<len(stCanva): s["linkCriativo"]=stCanva[i]
  extra=stLinks[len(c["stories"]):]
  if extra and c["stories"]: c["stories"][-1]["comoFazer"]=(c["stories"][-1]["comoFazer"]+"\n\nOutros vídeos: "+" ".join(extra)).strip()
  if isSt and x.get("conteudoLink") and c["stories"] and not c["stories"][0]["linkCriativo"]: c["stories"][0]["linkCriativo"]=x["conteudoLink"]
  cid=f"{CL}-{d}-n{(x.get('id') or str(len(cards)))[-8:]}"
  cards[cid]=c
# semanas
ws={}
d=datetime.date(2026,6,1)
while d<=datetime.date(2026,9,28):
  ini=d.isoformat(); fim=(d+datetime.timedelta(days=6)).isoformat()
  cs=sorted([c for c in cards.values() if ini<=c["data"]<=fim],key=lambda c:c["data"])
  def nome(c):
    t=re.sub(r"^\s*\d{1,2}(\s*de)?\s*(junho|julho|agosto|setembro|\.\d+)?\s*[-–:]?\s*","",c["titulo"],flags=re.I)
    t=re.sub(r"^(Reels?|Carrossel|Estático|Storie?s?|Foto)\s*","",t,flags=re.I).strip(" -–\"“”")
    if c["tema"]: return c["tema"].split("\n")[0][:60]
    if t and not re.match(r"^(Feed|\d+([.]\d+)?|\w+: ?Feed)$",t,re.I) and not re.match(r"^(Segunda|Terça|Quarta|Quinta|Sexta|S[aá]bado|Domingo)\b",t,re.I): return t[:60]
    for k in ("legenda","comoFazer","intencao"):
      l=[z for z in c[k].split("\n") if z.strip() and not z.strip().startswith("http")]
      if l: return re.sub(r"^[-•\s]+","",l[0]).strip()[:60]
    return t[:60]
  feed=[c for c in cs if c["tipo"]=="Feed"]; st=[c for c in cs if c["tipo"]=="Storie"]
  temas=[n for n in (nome(c) for c in feed) if n and not re.match(r"^(Feed|Reels?|\d+)$",n,re.I)]
  pub=sum(1 for c in cs if c["etapa"]=="publicado")
  ws[f"{CL}-{ini}"]=dict(cliente=CL,inicio=ini,fim=fim,origem="notion",
    titulo=(" · ".join(temas[:3])[:110] or ("Stories" if st else "Sem conteúdos no Notion")),
    objetivo=f"Semana importada do Notion. {len(cs)} conteúdos, {pub} publicados.",
    estrategiaFeed="\n".join(f"{DC[datetime.date.fromisoformat(c['data']).weekday()]}: {c['formato'] or 'Feed'}. {nome(c)}" for c in feed),
    estrategiaStories="\n".join(f"{DC[datetime.date.fromisoformat(c['data']).weekday()]}: {len(c['stories'])} storie(s). {(c['stories'][0]['tema'] or c['stories'][0]['comoFazer'] or '').split(chr(10))[0][:80]}" for c in st),
    oferta="",notas="Importado do Notion a 7 de outubro de 2026.")
  d+=datetime.timedelta(days=7)
for k,v in cards.items(): json.dump(v,open(f"{OUT}/cartoes/{k}.json","w"),ensure_ascii=False,indent=0)
for k,v in ws.items(): json.dump(v,open(f"{OUT}/semanas/{k}.json","w"),ensure_ascii=False,indent=0)
print(len(cards),"cartões",len(ws),"semanas")
import collections; print(collections.Counter((c["tipo"],c["formato"],c["etapa"]) for c in cards.values()))
for k,v in ws.items(): print(v["inicio"],"|",v["titulo"])
