const { chromium } = require('/opt/node22/lib/node_modules/playwright'); const fs=require('fs');
const heart=(cx,cy,s)=>`M${cx},${cy+s*0.85} C${cx-s*1.5},${cy-s*0.1} ${cx-s*0.75},${cy-s*1.25} ${cx},${cy-s*0.45} C${cx+s*0.75},${cy-s*1.25} ${cx+s*1.5},${cy-s*0.1} ${cx},${cy+s*0.85} Z`;
const star=()=>{let d='';for(let i=0;i<10;i++){const r=i%2?95:230,a=-Math.PI/2+i*Math.PI/5;d+=(i?'L':'M')+(Math.cos(a)*r).toFixed(1)+','+(Math.sin(a)*r).toFixed(1)+' ';}return d+'Z';};
const ICON={
 bag:`<path d="M-150,-60 L150,-60 L130,190 L-130,190 Z"/><path d="M-80,-60 A80,80 0 0 1 80,-60"/>`,
 ruler:`<g transform="rotate(-36)"><rect x="-230" y="-70" width="460" height="140" rx="22"/>${[-170,-102,-34,34,102,170].map(i=>`<path d="M${i},-70 L${i},${Math.abs(i)%136===34||Math.abs(i)===34?-20:10}"/>`).join('')}</g>`,
 leaf:`<g transform="rotate(-45)"><path d="M0,230 C-210,90 -170,-160 0,-240 C170,-160 210,90 0,230 Z"/><path d="M0,280 L0,-150"/>${[-60,30,120].map(y=>`<path d="M0,${y} L-80,${y-70} M0,${y} L80,${y-70}"/>`).join('')}</g>`,
 heart:`<path d="${heart(0,10,170)}"/>`,
 swing:`<path d="M-200,-260 L200,-260 M-90,-260 L-90,120 M90,-260 L90,120 M-140,120 L140,120"/><path d="${heart(-150,-120,48)}"/><path d="${heart(175,-150,48)}"/>`,
 box:`<rect x="-170" y="-60" width="340" height="250"/><path d="M-170,-60 L-110,-170 L230,-170 L170,-60 M230,-170 L230,80 L170,190 M-40,-60 L20,-170"/>`,
 star:`<path d="${star()}"/>`,
 flower:`<g transform="translate(0,-30)">${[0,1,2,3,4].map(i=>`<ellipse cx="0" cy="-105" rx="62" ry="95" transform="rotate(${i*72})"/>`).join('')}<circle r="42"/><path d="M0,190 C10,240 0,280 -10,320 M-4,265 C-60,230 -110,240 -130,270"/></g>`};
const D=[["Comprar","#E0A18A","#FFFFFF","bag"],["Tamanhos","#CBD2CA","#7A5E50","ruler"],["Outono 26","#AA867D","#FFFFFF","leaf"],["Jardim","#F0E2B2","#AA867D","flower"],["Clientes","#AABDD4","#FFFFFF","heart"],["A Marca","#FBF6EC","#AA867D","boneco"],["Envios e trocas","#E0A18A","#FFFFFF","box"],["Natal","#AA867D","#F0E2B2","star"]];
const BON='data:image/png;base64,'+fs.readFileSync('../logo/boneco-limpo.png').toString('base64');
const svg=([n,bg,ink,ic])=>ic==='boneco'?`<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1080" height="1080" viewBox="0 0 1080 1080"><rect width="1080" height="1080" fill="${bg}"/><circle cx="540" cy="540" r="432" fill="none" stroke="${ink}" stroke-opacity="0.55" stroke-width="6"/><image href="${BON}" x="190" y="162" width="721" height="756"/></svg>`:`<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080" viewBox="0 0 1080 1080"><rect width="1080" height="1080" fill="${bg}"/><circle cx="540" cy="540" r="432" fill="none" stroke="${ink}" stroke-opacity="0.55" stroke-width="6"/><g transform="translate(540,540)" fill="none" stroke="${ink}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round">${ICON[ic]}</g></svg>`;
D.forEach(d=>fs.writeFileSync('capa-'+d[0].normalize('NFD').replace(/[^A-Za-z0-9]+/g,'')+'.svg', svg(d)));
(async()=>{ const b=await chromium.launch(); const p=await b.newPage();
await p.setContent(`<style>@page{size:1080px 1080px;margin:0}body{margin:0}.pg{width:1080px;height:1080px;page-break-after:always}</style>${D.map(d=>`<div class="pg">${svg(d)}</div>`).join('')}`);
await p.pdf({path:'destaques-tracosdamor-v2.pdf', width:'1080px', height:'1080px', printBackground:true});
await p.setViewportSize({width:1080,height:1080}); await p.setContent(svg(D[1])); await p.screenshot({path:'chk.png'}); await b.close(); })();
