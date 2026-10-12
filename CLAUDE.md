# Estúdio Traços D'Amor

App de gestão de conteúdos da marca Traços D'Amor (moda infantil), feita para a Tânia Silveira (estrategista). Português de Portugal em tudo: código, textos, commits.

- App publicada (artifact do claude.ai): https://claude.ai/artifact/D3MiggwcKrr8yggsoKk3vz
- Código: `app/estudio.html` (um ficheiro, HTML + JS sem build). Publicar sempre no mesmo URL e **omitir `capabilities`** ao republicar (passam para a frente). Se for preciso mudar capacidades, repetir o conjunto todo: db (regras abaixo), user {scopes:["profile"]}, sample {}, mcp Gmail send_message, assets {}.
- Branch: `claude/tracos-amor-content-strategy-gm97ps`.

## Quem usa
- **Tânia (dona)**: vê tudo. Separadores privados 🔒: Estratégia (geral + Campanhas), Dados, Histórico, Feed, Oficina.
- **Equipa (Ângela, criativa)**: quadro, links, checks.
- **Cliente (Sílvia, fundadora)**: vê resultado final: Quadro, Calendário, Semanas (com Ações da semana e "Como fica o feed"), Email marketing, Canais, Relatórios. Nunca vê estratégia nem raciocínio.

## Base de dados (ArtifactData)
Regras: `privado` read/write owner · `semanas`, `clientes`, `relatorios`, `feed`, `destaques`, `feedcfg` write admin. Restantes coleções escrevíveis por quem tem acesso.
- `cartoes` (quadro), `semanas`, `comentarios`, `pessoas`, `relatorios` (publicados), `emails`, `mensagens` (canais), `tarefas` (ações da semana), `feed` / `destaques` / `feedcfg` (antes e depois do Instagram; `feedcfg/antes.desde` = data do feed real registado).
- `privado/tracosdamor`: estratégia geral + `comunicacao`; subcoleções `campanhas` (blackfriday com plano completo em `blackfriday/plano`, natal), `historico` (Notion jun–out), `avaliacoes`, `relatorios` (rascunhos: nunca publicar sem validação da Tânia), `metricas`, `resultados`, `sugestoes`.
- `data/users/<id>`: rascunhos da Oficina.
- Imagens: capacidade `assets`, ids guardados nos documentos, servidas em `/_blob/<id>`.

## Regras de trabalho
- Relatórios: nunca entregar final sem validação da Tânia.
- Conteúdo: manual de marca em `docs/manual-de-marca.md` (constante `MARCA` na app). Nunca inventar preços, tamanhos ou tecidos: usar [parênteses retos].
- Ritmo: feed segunda, quarta e sexta com 1 story; restantes dias 2 stories.
- A Oficina gera um dia de cada vez e lê campanhas, ações da semana e memória de tudo o que foi feito.
- Antes de publicar: extrair o `<script>` e correr `node --check`; testar com Playwright (Chromium em /opt/pw-browsers) e um mock de `window.claude` (db/user/sample/assets).
- A página nunca redesenha a meio de um clique (`UI.ptrDown`); manter isto ao mexer em `onData`.

## Em falta (dados da cliente)
Preços e tamanhos de outono, custos e stock (Black Friday), plataforma do site e ferramenta de email, exportação Meta (Instagram/Facebook), data limite de envio de Natal.
