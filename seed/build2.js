const fs=require('fs');
const html=fs.readFileSync('calendario-outubro-2026.html','utf8');
const a=html.indexOf('const W = [');const b=html.indexOf('\n];',a);
const W=eval('('+html.slice(a+10,b+2)+')');
const C='tracosdamor', ini={s1:'2026-10-05',s2:'2026-10-12',s3:'2026-10-19',s4:'2026-10-26'};
const add=(s,n)=>{const d=new Date(s+'T12:00:00Z');d.setUTCDate(d.getUTCDate()+n);return d.toISOString().slice(0,10)};
const DL=["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"];
const writes=[];const dir='/home/user/Tra-os-d-Amor/seed/v2/';fs.mkdirSync(dir,{recursive:true});
const put=(col,id,data)=>{const f=dir+`${col}__${id}.json`;fs.writeFileSync(f,JSON.stringify(data));writes.push({op:'set',collection:col,doc_id:id,file_path:f});};
const now='2026-09-28T18:00:00.000Z';
for(const w of W){const i0=ini[w.id];
 w.d.forEach((d,i)=>{const data=add(i0,i);const feed=d.f!=="2 stories";
  const st=s=>({intencao:"",estrategia:"",tema:s,texto:"",comoFazer:"",media:/foto/i.test(s)?"foto":"video",linkCriativo:"",linkDrive:""});
  put('cartoes',`${C}-${data}`,{cliente:C,data,semana:`${C}-${i0}`,tipo:feed?"Feed":"Storie",formato:feed?(d.f==="Foto"?"Estático":d.f):null,
   titulo:`${DL[i]}: ${feed?"Feed":"Storie"}`,intencao:"",estrategia:"",tema:feed?d.tema:"",comoFazer:feed?`Gancho: ${d.hook}`:"",inspiracao:"",legenda:feed?d.cap:"",
   stories:d.st.map(st),linkCriativo:"",capaCriativo:"",linkDrive:"",capaDrive:"",etapa:"ideia",historico:[{etapa:"ideia",por:null,em:now}],criadoEm:now,metricas:{}});
 });}
// delete old conteudos
for(const w of W){const i0=ini[w.id]; w.d.forEach((d,i)=>{const data=add(i0,i); if(d.f!=="2 stories") writes.push({op:'delete',collection:'conteudos',doc_id:`${C}-${data}-feed`}); d.st.forEach((s,j)=>writes.push({op:'delete',collection:'conteudos',doc_id:`${C}-${data}-story${j+1}`}));});}
fs.writeFileSync('seed/v2/b1.json',JSON.stringify(writes.slice(0,45)));
fs.writeFileSync('seed/v2/b2.json',JSON.stringify(writes.slice(45)));
console.log(writes.length);
