const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const url = 'file://' + path.resolve('index.html');
  const log = []; process.on('exit',()=>console.log(log.join('\n'))); process.on('unhandledRejection',e=>{log.push('SCRIPT FAIL: '+e.message.split('\n')[0]);process.exit(1)});
  for (const role of ['dona','equipa','cliente']) {
    const page = await browser.newPage({ viewport: { width: 1300, height: 900 } });
    page.on('console', m => { if (m.type()==='error') log.push(`[${role}] console: ${m.text()}`); });
    page.on('pageerror', e => log.push(`[${role}] pageerror: ${e.message}`));
    await page.goto(url + '?role=' + role);
    await page.waitForTimeout(600);
    const tabs = await page.$$eval('#tabs [data-tab]', b => b.map(x => x.dataset.tab));
    log.push(`[${role}] tabs: ${tabs.join(',')} | chips: ${(await page.textContent('#statusChips')).trim()}`);
    for (const t of tabs) {
      await page.click(`#tabs [data-tab="${t}"]`); await page.waitForTimeout(250);
      const txt = (await page.textContent('#main')).slice(0,80).replace(/\s+/g,' ');
      log.push(`[${role}] ${t}: ${txt}`);
      await page.screenshot({ path: `shot-${role}-${t}.png`, fullPage: false });
    }
    // quadro: vista etapas too
    await page.click('#tabs [data-tab="quadro"]'); await page.waitForTimeout(200);
    const tiles = await page.$$('.tile'); log.push(`[${role}] tiles visible (semanas view): ${tiles.length}`);
    if (tiles.length) { await tiles[0].click(); await page.waitForTimeout(300); await page.screenshot({ path:`shot-${role}-card.png`});
      const acts = await page.$$eval('#mActions button', b=>b.map(x=>x.textContent)); log.push(`[${role}] card actions: ${acts.join(' | ')}`);
      // comment
      await page.fill('#novoCom','teste '+role); await page.click('[data-act=comentar]'); await page.waitForTimeout(200);
      const coms = await page.$$eval('#mComs .com', c=>c.map(x=>x.textContent.replace(/\s+/g,' ').trim()));
      log.push(`[${role}] comments: ${coms.slice(-1)}`);
      await page.keyboard.press('Escape'); await page.waitForTimeout(150);
    }
    await page.click('[data-act=vista][data-v=etapas]'); await page.waitForTimeout(200);
    log.push(`[${role}] etapas cols: ${(await page.$$eval('.col .colhd span:first-child', s=>s.map(x=>x.textContent))).join(',')}`);
    await page.screenshot({ path:`shot-${role}-etapas.png`});
    await page.click('[data-act=vista][data-v=semanas]');
    // semanas: add inspiration + comment
    await page.click('#tabs [data-tab="semanas"]'); await page.waitForTimeout(200);
    await page.fill('#inspUrl','https://exemplo.pt/x'); await page.fill('#inspNota','nota '+role); await page.click('[data-act=addInsp]'); await page.waitForTimeout(200);
    await page.fill('#semCom','comentário semana '+role); await page.click('[data-act=comSemana]'); await page.waitForTimeout(200);
    log.push(`[${role}] semana insp: ${(await page.$$('.insp a.il')).length} coms: ${(await page.$$('.coms .com')).length}`);
    await page.screenshot({ path:`shot-${role}-semanas2.png`, fullPage:true });
    const errs = await page.evaluate(()=>window.__errors); if (errs.length) log.push(`[${role}] window errors: ${errs.join(' || ')}`);
    await page.close();
  }
  // owner flows
  const page = await browser.newPage({ viewport: { width: 1300, height: 900 } });
  page.on('pageerror', e => log.push(`[flow] pageerror: ${e.message}`));
  await page.goto(url + '?role=dona'); await page.waitForTimeout(500);
  // open a card in ideia, move through stages
  await page.click('#tabs [data-tab="quadro"]'); await page.click('[data-act=vista][data-v=etapas]'); await page.waitForTimeout(200);
  const ideia = await page.$('.col.ideia .tile'); await ideia.click(); await page.waitForTimeout(200);
  for (let i=0;i<5;i++){ const b = await page.$('#mActions button.primary'); if(!b) break; const t=await b.textContent(); await b.click(); await page.waitForTimeout(250); log.push(`[flow] clicked: ${t} -> ${await page.textContent('#mEtapa')}`); }
  // pedir alterações path on another card at cliente
  await page.keyboard.press('Escape');
  // edit card and save
  const t2 = await page.$('.col.ideia .tile:has-text("Feed")'); if (t2){ await t2.click(); await page.waitForTimeout(200); await page.fill('#fld-legenda','Legenda nova'); await page.click('#cardForm button[type=submit]'); await page.waitForTimeout(200); log.push('[flow] saved legenda: '+ await page.inputValue('#fld-legenda')); await page.keyboard.press('Escape'); }
  // new week
  await page.click('#tabs [data-tab="quadro"]'); await page.click('[data-act=vista][data-v=semanas]'); await page.waitForTimeout(200);
  await page.click('[data-act=novaSemana]'); await page.waitForTimeout(300);
  log.push('[flow] after novaSemana tab: '+ await page.$eval('#tabs [aria-selected=true]', e=>e.textContent) + ' editing form: ' + !!(await page.$('#semForm')));
  await page.fill('#s-tit','Semana teste'); await page.fill('#s-objetivo','obj'); await page.click('button[form=semForm]'); await page.waitForTimeout(300);
  log.push('[flow] week saved hero: '+ (await page.textContent('.wkhero')).replace(/\s+/g,' ').slice(0,80));
  await page.click('#tabs [data-tab="quadro"]'); await page.waitForTimeout(200);
  log.push('[flow] covers: '+(await page.$$eval('.cover .art span', s=>s.map(x=>x.textContent))).join(','));
  await page.screenshot({ path:'shot-flow-quadro.png' });
  // add card in a week
  await page.click('[data-act=novoCartao]'); await page.waitForTimeout(300); log.push('[flow] new card modal: '+ !!(await page.$('.drawer'))); await page.keyboard.press('Escape');
  // oficina
  await page.click('#tabs [data-tab="oficina"]'); await page.waitForTimeout(200);
  await page.click('[data-act=gerar]'); await page.waitForTimeout(500);
  log.push('[flow] oficina proposals: '+(await page.$$('[data-act=enviarUm]')).length);
  await page.fill('#ret-0-0','muda a legenda'); await page.click('[data-act=retificar]'); await page.waitForTimeout(400);
  log.push('[flow] after retificar pedidos: '+(await page.$$('.com')).length);
  await page.click('[data-act=guardarRasc]'); await page.waitForTimeout(200);
  await page.click('[data-act=enviarTodos]'); await page.waitForTimeout(300);
  log.push('[flow] rascunhos: '+(await page.$$('[data-act=abrirRasc]')).length);
  await page.screenshot({ path:'shot-flow-oficina.png', fullPage:true });
  // dados: pergunta
  await page.click('#tabs [data-tab="dados"]'); await page.waitForTimeout(200);
  await page.fill('#qaTxt','pergunta?'); await page.click('[data-act=perguntar]'); await page.waitForTimeout(400);
  log.push('[flow] qa answers: '+(await page.$$('.qa .a')).length);
  await page.screenshot({ path:'shot-flow-dados.png', fullPage:true });
  // relatorio melhorias edit
  await page.click('#tabs [data-tab="relatorios"]'); await page.waitForTimeout(200);
  await page.click('[data-act=editMelh]'); await page.click('[data-act=addMelh]'); await page.fill('#m-a-1','Minha melhoria'); await page.click('[data-act=saveMelh]'); await page.waitForTimeout(300);
  log.push('[flow] melhorias: '+(await page.$$('.melhoria')).length);
  await page.screenshot({ path:'shot-flow-relatorio.png', fullPage:true });
  // estrategia edit + pessoas
  await page.click('#tabs [data-tab="estrategia"]'); await page.waitForTimeout(200);
  await page.screenshot({ path:'shot-flow-estrategia.png', fullPage:true });
  log.push('[flow] errors: '+(await page.evaluate(()=>window.__errors)).join(' || '));
  // mobile
  const m = await browser.newPage({ viewport:{width:390,height:844} }); m.on('pageerror', e => log.push(`[mobile] pageerror: ${e.message}`));
  await m.goto(url+'?role=dona'); await m.waitForTimeout(500); await m.screenshot({path:'shot-mobile-quadro.png'});
  const sw = await m.evaluate(()=>document.documentElement.scrollWidth); log.push('[mobile] scrollWidth '+sw);
  await m.click('#tabs [data-tab="calendario"]'); await m.waitForTimeout(200); await m.screenshot({path:'shot-mobile-cal.png'});
  await browser.close();
})();
