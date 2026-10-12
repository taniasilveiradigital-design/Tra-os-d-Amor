import json,sys,os
F=sys.argv[1]; MAP=json.load(open(sys.argv[2])); OUT=sys.argv[3]; os.makedirs(OUT,exist_ok=True)
C="tracosdamor"; NOW="2026-10-11T23:00:00.000Z"; m=json.load(open(F+"/out/meta.json"))
docs={}
for t in m["tiles"]:
  docs[f"feed/{C}-a-{t['ordem']:02d}"]=dict(cliente=C,semana="antes",asset=MAP[t["file"]],ordem=t["ordem"],titulo={1:"O sonho tornou-se real",2:"A nossa Essência",3:"Caixas (reel)"}.get(t["ordem"],""),parcial=t["parcial"],criadoEm=NOW)
old=[]
for d in m["destaques"]:
  i=f"{C}-d-{__import__('unicodedata').normalize('NFD',d['nome']).encode('ascii','ignore').decode().replace(' ','').lower()}"; old.append(i)
  docs[f"destaques/{i}"]=dict(cliente=C,nome=d["nome"],asset=MAP[d["file"]],criadoEm="2026-10-01T00:00:00.000Z")
new=[]
for nome in ["Comprar","Tamanhos","Outono 26","Clientes","A Marca","Envios e trocas"]:
  k=''.join(ch for ch in __import__('unicodedata').normalize('NFD',nome) if ch.isalnum()); i=f"{C}-d-novo-{k.lower()}"; new.append(i)
  docs[f"destaques/{i}"]=dict(cliente=C,nome=nome,asset=MAP[f"novo-{k}.png"],proposta=True,criadoEm=NOW)
fix=[f"{C}-a-01",f"{C}-a-02"]
docs[f"feedcfg/antes"]=dict(cliente=C,inicio="",fixos=fix,destaques=old)
docs[f"feedcfg/{C}-2026-10-19"]=dict(cliente=C,inicio="2026-10-19",fixos=fix,destaques=new)
for k,v in docs.items():
  col,i=k.split("/"); os.makedirs(f"{OUT}/{col}",exist_ok=True); json.dump(v,open(f"{OUT}/{col}/{i}.json","w"),ensure_ascii=False)
print(len(docs))
