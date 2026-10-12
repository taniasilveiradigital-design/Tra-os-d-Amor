const { chromium } = require('/opt/node22/lib/node_modules/playwright'); const fs=require('fs');
// capas 1080x1080: fundo liso do manual, aro fino, ícone em traço único (mesma espessura em todos)
const D=[["Comprar","#E0A18A","#FFFFFF","bag"],["Tamanhos","#CBD2CA","#7A5E50","ruler"],["Outono 26","#AA867D","#FFFFFF","leaf"],["Clientes","#AABDD4","#FFFFFF","heart"],["A Marca","#F0E2B2","#AA867D","swing"],["Envios e trocas","#E0A18A","#FFFFFF","box"],["Natal","#AA867D","#F0E2B2","star"]];
(async()=>{ const b=await chromium.launch(); const p=await b.newPage();
const imgs=[];
for (const [nome,bg,ink,ic] of D) {
  const url=await p.evaluate(([bg,ink,ic])=>{ const S=1080,c=document.createElement('canvas'); c.width=c.height=S; const x=c.getContext('2d');
    x.fillStyle=bg; x.fillRect(0,0,S,S);
    x.strokeStyle=ink; x.globalAlpha=.55; x.lineWidth=6; x.beginPath(); x.arc(S/2,S/2,S*0.40,0,Math.PI*2); x.stroke(); x.globalAlpha=1;
    x.lineWidth=22; x.lineCap='round'; x.lineJoin='round'; x.fillStyle=ink;
    const C=S/2; x.save(); x.translate(C,C);
    const heart=(cx,cy,s)=>{x.beginPath();x.moveTo(cx,cy+s*0.85);x.bezierCurveTo(cx-s*1.5,cy-s*0.1,cx-s*0.75,cy-s*1.25,cx,cy-s*0.45);x.bezierCurveTo(cx+s*0.75,cy-s*1.25,cx+s*1.5,cy-s*0.1,cx,cy+s*0.85);x.stroke();};
    if(ic==='bag'){x.beginPath();x.moveTo(-150,-60);x.lineTo(150,-60);x.lineTo(130,190);x.lineTo(-130,190);x.closePath();x.stroke();x.beginPath();x.arc(0,-60,80,Math.PI,0);x.stroke();}
    if(ic==='ruler'){x.rotate(-Math.PI/5);x.beginPath();x.roundRect(-230,-70,460,140,22);x.stroke();for(let i=-170;i<=170;i+=68){x.beginPath();x.moveTo(i,-70);x.lineTo(i,i%136===0?10:-20);x.stroke();}}
    if(ic==='leaf'){x.rotate(-Math.PI/4);x.beginPath();x.moveTo(0,230);x.bezierCurveTo(-210,90,-170,-160,0,-240);x.bezierCurveTo(170,-160,210,90,0,230);x.stroke();x.beginPath();x.moveTo(0,280);x.lineTo(0,-150);x.stroke();for(const y of [-60,30,120]){x.beginPath();x.moveTo(0,y);x.lineTo(-80,y-70);x.moveTo(0,y);x.lineTo(80,y-70);x.stroke();}}
    if(ic==='heart'){heart(0,10,170);}
    if(ic==='swing'){x.beginPath();x.moveTo(-200,-260);x.lineTo(200,-260);x.stroke();x.beginPath();x.moveTo(-90,-260);x.lineTo(-90,120);x.moveTo(90,-260);x.lineTo(90,120);x.stroke();x.beginPath();x.moveTo(-140,120);x.lineTo(140,120);x.stroke();heart(-150,-120,48);heart(175,-150,48);}
    if(ic==='box'){x.beginPath();x.rect(-170,-60,340,250);x.stroke();x.beginPath();x.moveTo(-170,-60);x.lineTo(-110,-170);x.lineTo(230,-170);x.lineTo(170,-60);x.moveTo(230,-170);x.lineTo(230,80);x.lineTo(170,190);x.stroke();x.beginPath();x.moveTo(-40,-60);x.lineTo(20,-170);x.stroke();}
    if(ic==='star'){x.beginPath();for(let i=0;i<10;i++){const r=i%2?95:230,a=-Math.PI/2+i*Math.PI/5;x.lineTo(Math.cos(a)*r,Math.sin(a)*r);}x.closePath();x.stroke();}
    x.restore(); return c.toDataURL('image/png');},[bg,ink,ic]);
  const f='capa-'+nome.normalize('NFD').replace(/[^A-Za-z0-9]+/g,'')+'.png'; fs.writeFileSync(f, Buffer.from(url.split(',')[1],'base64')); imgs.push([nome,f]);
}
// folha de pré-visualização como no Instagram (círculos pequenos) e grande
await p.setViewportSize({width:1100,height:420});
await p.setContent(`<body style="margin:0;background:#fff;font-family:sans-serif"><div style="padding:24px"><div style="font:600 15px sans-serif;margin-bottom:14px">Como fica no perfil</div><div style="display:flex;gap:18px">${imgs.map(([n,f])=>`<div style="text-align:center;width:78px"><img src="data:image/png;base64,${fs.readFileSync(f).toString('base64')}" style="width:66px;height:66px;border-radius:50%;border:2px solid #ddd;padding:2px"><div style="font-size:12px;margin-top:4px">${n}</div></div>`).join('')}</div>
<div style="font:600 15px sans-serif;margin:22px 0 10px">Em grande</div><div style="display:flex;gap:14px">${imgs.map(([n,f])=>`<img src="data:image/png;base64,${fs.readFileSync(f).toString('base64')}" style="width:130px;height:130px;border-radius:50%">`).join('')}</div></div></body>`);
await p.screenshot({path:'folha.png'}); await b.close(); })();
