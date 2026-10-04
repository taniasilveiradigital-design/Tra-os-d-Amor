(function(){
const params=new URLSearchParams(location.search); const role=params.get('role')||'dona';
const ME={dona:{id:'u_W9YKuxRMYfhPLeEFPI5OiQ',isOwner:true,name:'Tânia'},equipa:{id:'u_angela',isOwner:false,name:'Ângela'},cliente:{id:'u_silvia',isOwner:false,name:'Sílvia'}}[role];
const store=__STORE__; const listeners=[];
window.__store=store; window.__errors=[];
const clone=o=>JSON.parse(JSON.stringify(o));
function priv(path){return path.startsWith('privado')&&!ME.isOwner || (path.startsWith('data/users/')&&!path.startsWith('data/users/'+ME.id))}
function snapDoc(path){const ex=(path in store)&&!priv(path);return {id:path.split('/').pop(),exists:ex,data:()=>ex?clone(store[path]):undefined,metadata:{fromCache:false,hasPendingWrites:false}}}
function colDocs(col,filters){const n=col.split('/').length;return Object.keys(store).filter(p=>p.startsWith(col+'/')&&p.split('/').length===n+1&&!priv(p)).filter(p=>filters.every(([f,op,v])=>store[p][f]===v)).sort().map(snapDoc)}
function notify(){setTimeout(()=>listeners.forEach(l=>l()),5)}
function check(path){ if(priv(path)) throw {code:'invalid_argument',message:'denied'}; if(!ME.isOwner && /^(semanas|clientes|relatorios)\//.test(path) && role!=='admin') throw {code:'invalid_argument',message:'rule'} }
function docRef(path){return {id:path.split('/').pop(),path,
 get:async()=>snapDoc(path),
 set:async(d)=>{check(path);store[path]=clone(d);notify()},
 update:async(d)=>{check(path);if(!(path in store))throw{code:'invalid_argument'};const m=(a,b)=>{for(const k in b){if(b[k]&&typeof b[k]==='object'&&!Array.isArray(b[k])&&a[k]&&typeof a[k]==='object'&&!Array.isArray(a[k]))m(a[k],b[k]);else a[k]=clone(b[k])}};m(store[path],d);notify()},
 delete:async()=>{check(path);delete store[path];notify()},
 onSnapshot:(n,e)=>{const l=()=>n(snapDoc(path));listeners.push(l);setTimeout(l,10);return()=>{}},
 collection:(c)=>colRef(path+'/'+c)}}
function colRef(col,filters=[]){const q={path:col,
 where:(f,op,v)=>colRef(col,[...filters,[f,op,v]]),orderBy:()=>q,limit:()=>q,
 get:async()=>{const docs=colDocs(col,filters);return{docs,size:docs.length,empty:!docs.length}},
 onSnapshot:(n,e)=>{const l=()=>{const docs=colDocs(col,filters);n({docs,size:docs.length,empty:!docs.length,docChanges:()=>[],metadata:{}})};listeners.push(l);setTimeout(l,10);return()=>{}},
 doc:(id)=>docRef(col+'/'+(id||Math.random().toString(36).slice(2))),add:async(d)=>{const r=docRef(col+'/'+Math.random().toString(36).slice(2));await r.set(d);return r}};return q}
const db={doc:docRef,collection:(c)=>colRef(c)};
const user={me:async()=>({...ME,avatarUrl:'',color:'#000',email:null,canEdit:ME.isOwner}),isOwner:async()=>ME.isOwner,id:async()=>ME.id,profiles:async(ids)=>Object.fromEntries(ids.map(i=>[i,{id:i,name:i==='u_angela'?'Ângela R':''}]))};
const sample=Object.assign(async(input)=>({text:'Resposta de teste.',truncated:false}),{json:async(input)=>({cartoes:[{data:'2026-10-12',tipo:'Feed',formato:'Reel',titulo:'Segunda: Feed',intencao:'i',estrategia:'e',tema:'t',comoFazer:'c',inspiracao:'',legenda:'l',stories:[{tema:'s',texto:'x',media:'video'}]}],notaParaTania:'nota'})});
window.claude={use:async(n)=>({db,user,sample:ME.isOwner?sample:null}[n]??null)};
window.addEventListener('error',e=>window.__errors.push(String(e.message)));
window.addEventListener('unhandledrejection',e=>window.__errors.push('rej:'+String(e.reason&&e.reason.message||e.reason)));
})();
