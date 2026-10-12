const { chromium } = require('/opt/node22/lib/node_modules/playwright'); const fs=require('fs');
const D=[["Comprar","#E0A18A","bag"],["Tamanhos","#CBD2CA","ruler"],["Outono 26","#AA867D","leaf"],["Clientes","#AABDD4","heart"],["A Marca","#F0E2B2","balloons"],["Envios e trocas","#E0A18A","box"]];
(async()=>{ const b=await chromium.launch(); const p=await b.newPage();
for (const [nome,cor,ic] of D) {
  const url=await p.evaluate(([cor,ic])=>{ const c=document.createElement('canvas'); c.width=c.height=320; const x=c.getContext('2d');
    x.fillStyle=cor; x.fillRect(0,0,320,320); const ink=(cor==='#F0E2B2'||cor==='#CBD2CA')?'#AA867D':'#FFFFFF'; x.strokeStyle=ink; x.fillStyle=ink; x.lineWidth=7; x.lineCap='round'; x.lineJoin='round';
    x.beginPath(); x.arc(160,160,128,0,Math.PI*2); x.lineWidth=3; x.stroke(); x.lineWidth=7;
    const heart=(cx,cy,s)=>{x.beginPath();x.moveTo(cx,cy+s*0.9);x.bezierCurveTo(cx-s*1.6,cy-s*0.1,cx-s*0.7,cy-s*1.3,cx,cy-s*0.4);x.bezierCurveTo(cx+s*0.7,cy-s*1.3,cx+s*1.6,cy-s*0.1,cx,cy+s*0.9);x.stroke();};
    x.beginPath();
    if(ic==='bag'){x.strokeRect(110,140,100,80);x.beginPath();x.arc(160,140,26,Math.PI,0);x.stroke();}
    if(ic==='ruler'){x.save();x.translate(160,160);x.rotate(-Math.PI/4);x.strokeRect(-80,-24,160,48);for(let i=-60;i<=60;i+=20){x.beginPath();x.moveTo(i,-24);x.lineTo(i,i%40===0?2:-8);x.stroke();}x.restore();}
    if(ic==='leaf'){x.beginPath();x.moveTo(110,210);x.quadraticCurveTo(100,110,215,105);x.quadraticCurveTo(220,215,110,210);x.stroke();x.beginPath();x.moveTo(110,210);x.lineTo(185,140);x.stroke();}
    if(ic==='heart'){heart(160,160,48);}
    if(ic==='balloons'){heart(130,120,26);heart(190,115,26);x.beginPath();x.moveTo(130,145);x.quadraticCurveTo(140,190,160,225);x.moveTo(190,140);x.quadraticCurveTo(178,190,160,225);x.stroke();}
    if(ic==='box'){x.strokeRect(112,135,96,80);x.beginPath();x.moveTo(112,135);x.lineTo(135,108);x.lineTo(231,108);x.lineTo(208,135);x.moveTo(231,108);x.lineTo(231,188);x.lineTo(208,215);x.stroke();}
    return c.toDataURL('image/png');},[cor,ic]);
  fs.writeFileSync('out/novo-'+nome.normalize('NFD').replace(/[^A-Za-z0-9]+/g,'')+'.png', Buffer.from(url.split(',')[1],'base64'));
}
await b.close(); })();
