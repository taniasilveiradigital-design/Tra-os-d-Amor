const fs=require('fs');
const html=fs.readFileSync('calendario-outubro-2026.html','utf8');
const a=html.indexOf('const W = [');const b=html.indexOf('\n];',a);
const W=eval('('+html.slice(a+10,b+2)+')');
const C='tracosdamor';
const semanaInicio={s1:'2026-10-05',s2:'2026-10-12',s3:'2026-10-19',s4:'2026-10-26'};
const add=(s,n)=>{const d=new Date(s+'T12:00:00Z');d.setUTCDate(d.getUTCDate()+n);return d.toISOString().slice(0,10)};
const stor={
 s1:"Terças, quintas e sábados: 2 stories. Story 1 abre conversa (sondagem, pergunta ou fundadora). Story 2 fecha com link direto para o conjunto.\nNos dias de feed: 1 story a partilhar o post com link.\nDomingo: teaser do Casaco Trilha e abertura da lista VIP (responder 🧡).",
 s2:"Lista VIP recebe o link por DM 2 horas antes do reel de segunda.\nStories de detalhe em vídeo (fecho, forro, bolsos). Uma sondagem de cor. A Sílvia conta a história do nome Trilha.\nCaixa de perguntas ao sábado e resposta com link.",
 s3:"Textura em vídeo, tabela de medidas, bastidores de produção.\nPrimeira menção ao Natal ao sábado: sondagem sobre fotos de família.\nDomingo: teaser do Look Trilha completo com condição até 1 de novembro.",
 s4:"Contas à vista (look completo vs. peças separadas) e contagem decrescente até 1 de novembro em todos os stories.\nProva social à quinta. Stock real por tamanho ao sábado, só se for verdade."};
const feed={
 s1:"Seg: reel 1 conjunto, 3 momentos. Qua: carrossel sobre o preço. Sex: reel guia de tamanhos. Dom: carrossel catálogo com preços.",
 s2:"Seg: reel de lançamento. Qua: carrossel com 6 detalhes. Sex: reel teste do recreio ou reel de criadora. Dom: foto de styling com os conjuntos.",
 s3:"Seg: reel de lançamento camisa + calça. Qua: carrossel 3 formas de usar. Sex: reel um dia inteiro. Dom: carrossel de perguntas frequentes.",
 s4:"Seg: reel transição pijama → look. Qua: carrossel fotos de Natal. Sex: reel da fundadora. Dom: foto último dia."};
const oferta={s1:"Portes grátis e embrulho de oferta em todas as encomendas online até 1 de novembro. Preço por conjunto.",s2:"Portes grátis e embrulho de oferta. Lista VIP vê o casaco 2 horas antes.",s3:"Portes grátis e embrulho de oferta.",s4:"Look Trilha completo (casaco + camisa + calça) com [condição] até 1 de novembro, às 23h59. Portes grátis e embrulho de oferta."};
const docs=[];
docs.push({collection:'clientes',doc_id:C,data:{
 nome:"Traços D'Amor",instagram:"@tracosdamor.pt",site:"tracosdamor.pt",ligacaoInstagram:"manual",
 objetivo:"Primeiras vendas online. Cada conteúdo mostra a peça, diz o preço e pede a compra.",
 diagnostico:"1. Fala de sentimento, não de produto: não diz o que é, quanto custa e onde se compra.\n2. Não pede a venda: sem preço à vista e sem pedido claro.\n3. Não há alcance: sem anúncios, o orgânico não chega a quem compra.\n4. Falta prova: peça numa criança real, em movimento, com medidas e opinião de outras mães.\n\n(Diagnóstico feito sem acesso à conta. Confirmar com os dados reais.)",
 regras:["Preço sempre visível: legenda, última imagem do carrossel e story.","Um pedido por publicação: \"Comenta [PALAVRA] e envio-te os tamanhos e o link.\" A palavra muda por semana.","Todos os stories vendem: link direto para a peça, sondagem ou caixa de pergunta.","DMs respondidas em menos de 1 hora, com foto, medidas em cm e link.","Oferta sem cheiro a saldo: portes grátis e embrulho de oferta até 1 de novembro.","Anúncios: 5 a 10 € por dia no reel da semana + remarketing.","Três mães criadoras de conteúdo (3 a 15 mil seguidores) nas semanas 2 e 3.","A fundadora aparece pelo menos uma vez por semana."],
 ritmo:"Feed às segundas, quartas, sextas e domingos, com 1 story.\nTerças, quintas e sábados: 2 stories, sem feed.",
 tom:"Usar: frases curtas, sensação primeiro, depois a peça e o preço. Palavras da marca: amor, traço, liberdade, crescer, descoberta, cuidado.\nEvitar: \"imperdível\", \"corra já\", percentagens gritadas, excesso de emojis, infantilizar.",
 metas:{cliquesLink:50,dms:15,vendasOnline:2,alcance:null}}});
for(const w of W){
 const ini=semanaInicio[w.id];const sid=`${C}-${ini}`;
 docs.push({collection:'semanas',doc_id:sid,data:{cliente:C,inicio:ini,fim:add(ini,6),titulo:w.t.replace(/^Semana \d · /,''),objetivo:w.o,palavraChave:w.kw,oferta:oferta[w.id],estrategiaStories:stor[w.id],estrategiaFeed:feed[w.id],notas:""}});
 w.d.forEach((d,i)=>{
  const data=add(ini,i);
  const base={cliente:C,data,semana:sid,estado:"ideia",link:"",notas:"",metricas:{}};
  if(d.f!=="2 stories"){
   const f=d.f==="Reel"?"Reel":d.f==="Carrossel"?"Carrossel":"Foto";
   docs.push({collection:'conteudos',doc_id:`${C}-${data}-feed`,data:{...base,formato:f,ordem:1,tema:d.tema,gancho:d.hook,legenda:d.cap,cta:`Comenta ${w.kw} e envio-te o link.`}});
  }
  d.st.forEach((s,j)=>docs.push({collection:'conteudos',doc_id:`${C}-${data}-story${j+1}`,data:{...base,formato:"Story",ordem:10+j,tema:s,gancho:"",legenda:"",cta:/link/i.test(s)?"Link sticker para a peça":(/sondagem|caixa|responde/i.test(s)?"Interação (sondagem/pergunta)":"")}}));
 });
}
docs.forEach(d=>{const p=`seed/${d.collection}__${d.doc_id}.json`;fs.writeFileSync(p,JSON.stringify(d.data));d.file_path='/home/user/Tra-os-d-Amor/'+p;});
const writes=docs.map(d=>({op:'set',collection:d.collection,doc_id:d.doc_id,file_path:d.file_path}));
fs.writeFileSync('seed/batch1.json',JSON.stringify(writes.slice(0,40)));
fs.writeFileSync('seed/batch2.json',JSON.stringify(writes.slice(40)));
console.log(docs.length, docs.filter(d=>d.collection==='conteudos').length);
