const { chromium } = require('/opt/node22/lib/node_modules/playwright'); const fs=require('fs');
const IMG='/tmp/claude-0/-home-user-Tra-os-d-Amor/01a18d04-a9ab-530c-a88c-e8485bc8e2e0/images/';
const COLS=[[0,293],[298,592],[597,890]];
// [screenshot, y0, y1, partial]
const ROWS=[[6,1206,1598,0],[7,390,782,0],[7,788,1180,0],[7,1184,1576,0],[7,1581,1895,1],[8,372,763,0],[8,768,1161,0],[8,1165,1557,0],[8,1561,1896,1],[9,391,783,0],[9,787,1179,0],[9,1184,1577,0],[9,1581,1896,1],[10,365,760,0],[10,765,1157,0],[10,1162,1554,0],[10,1559,1895,1]];
const DEST=[[105,'Encomendas'],[306,'A Coleção'],[507,'A Marca'],[708,'Bastidores']];
(async()=>{ const b=await chromium.launch(); const p=await b.newPage(); const meta={tiles:[],destaques:[]};
const crop=async(n,x0,y0,w,h,file)=>{ const data='data:image/webp;base64,'+fs.readFileSync(IMG+n+'.webp').toString('base64');
  const url=await p.evaluate(async([src,x0,y0,w,h])=>{const im=new Image();im.src=src;await im.decode();const c=document.createElement('canvas');c.width=w;c.height=h;c.getContext('2d').drawImage(im,x0,y0,w,h,0,0,w,h);return c.toDataURL('image/jpeg',0.9);},[data,x0,y0,w,h]);
  fs.writeFileSync('out/'+file, Buffer.from(url.split(',')[1],'base64')); };
let k=0; for (const [n,y0,y1,part] of ROWS) for (const [x0,x1] of COLS) { k++; const f=`antes-${String(k).padStart(2,'0')}.jpg`; await crop(n,x0,y0,x1-x0+1,y1-y0+1,f); meta.tiles.push({file:f,ordem:k,parcial:!!part,fixo:k<=2}); }
for (const [cx,nome] of DEST) { const f=`dest-${nome.replace(/\W+/g,'')}.jpg`; await crop(6,cx-75,868,150,150,f); meta.destaques.push({file:f,nome}); }
fs.writeFileSync('out/meta.json',JSON.stringify(meta)); console.log(k); await b.close(); })();
