# Relatório semanal Traços D'Amor (rotina de segunda-feira)

Guião que a rotina automática segue todas as segundas às 05:00 (Lisboa).
Só é ativada depois de o Instagram estar ligado através do conector Metricool.

App: https://claude.ai/artifact/D3MiggwcKrr8yggsoKk3vz
Base de dados da app: coleções `clientes`, `semanas`, `cartoes`, `comentarios`, `metricas`, `relatorios` (campo `cliente` = `tracosdamor`).

## Passos

1. Semana analisada: segunda a domingo anterior. `inicio` = segunda (AAAA-MM-DD), id = `tracosdamor-<inicio>`.
2. Ler da app (ArtifactData): `clientes/tracosdamor` (regras, metas), `semanas/<id>`, todos os `cartoes` dessa semana (feed + `stories[]`), `metricas` e `relatorios` da semana anterior.
3. Tirar do Metricool os números da conta @tracosdamor.pt para a semana: seguidores, novos seguidores, alcance, visualizações, interações, visitas ao perfil, cliques no link. E por publicação (posts, reels, carrosséis, stories): alcance, visualizações, gostos, comentários, partilhas, guardados, cliques no link, respostas.
4. Escrever `metricas/<id>` com `fonte: "metricool"`, sem apagar `dms`, `vendasOnline` e `receita` (são preenchidos à mão).
5. Associar cada publicação ao cartão do mesmo dia. Atualizar `metricas`, `linkPost` e `etapa: "publicado"`. O que foi publicado sem estar planeado fica registado nas notas do relatório.
6. Escrever `relatorios/<id>`:
   - `veredito`: bom | atencao | critico (face às metas de cliques, DMs e vendas).
   - `titulo`: uma frase que diz o que aconteceu.
   - `resumo`: 3 a 5 linhas diretas.
   - `kpis`: [{nome, valor, anterior, meta}] com alcance, cliques no link, visitas ao perfil, novos seguidores, DMs, vendas.
   - `porFormato`: {stories:{funcionou:[],naoFuncionou:[]}, reels:{...}, estaticos:{...}}.
   - `melhorias`: [{acao, porque, como}], o bloco principal, com 3 a 5 melhorias concretas para a semana seguinte.
   - `mostrarMais` / `mostrarMenos`: o que a audiência pediu com os números e o que não funciona.
   - `acoes`: 3 a 5 ações concretas para a semana que começa.
7. Nunca inventar números. O que não vier do Metricool fica `null` e é assinalado nas notas.
