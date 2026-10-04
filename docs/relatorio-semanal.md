# Relatório semanal Traços D'Amor (rotina de segunda-feira)

Guião que a rotina automática segue todas as segundas às 08:00 (Lisboa).
Só é ativada depois de o Instagram estar ligado através do conector Metricool.

App: https://claude.ai/artifact/D3MiggwcKrr8yggsoKk3vz
Base de dados da app: coleções `clientes`, `semanas`, `cartoes`, `comentarios`, `metricas`, `relatorios` (campo `cliente` = `tracosdamor`).

## Passos

1. Semana analisada: segunda a domingo anterior. `inicio` = segunda (AAAA-MM-DD), id = `tracosdamor-<inicio>`.
2. Ler da app (ArtifactData): `clientes/tracosdamor` (regras, metas), `semanas/<id>`, todos os `cartoes` dessa semana (feed + `stories[]`), `metricas` e `relatorios` da semana anterior.
3. Tirar do Metricool os números da conta @tracosdamor.pt para a semana: seguidores, novos seguidores, alcance, visualizações, interações, visitas ao perfil, cliques no link. E por publicação (posts, reels, carrosséis, stories): alcance, visualizações, gostos, comentários, partilhas, guardados, cliques no link, respostas.
4. Escrever `privado/tracosdamor/metricas/<id>` com `fonte: "metricool"` e as duas redes em separado: `{inicio, fim, instagram:{seguidores, novosSeguidores, alcance, visualizacoes, interacoes, visitasPerfil, cliquesLink, mensagens}, facebook:{mesmas chaves}, vendasOnline, receita}`. Não apagar `mensagens`, `vendasOnline` e `receita` se foram preenchidos à mão. Documentos antigos com chaves soltas contam como Instagram.
5. Associar cada publicação ao cartão do mesmo dia. Atualizar `metricas`, `linkPost` e `etapa: "publicado"`. O que foi publicado sem estar planeado fica registado nas notas do relatório.
6. Escrever `relatorios/<id>`:
   - `veredito`: bom | atencao | critico (face às metas de cliques, DMs e vendas).
   - `titulo`: uma frase que diz o que aconteceu.
   - `resumo`: 3 a 5 linhas diretas.
   - Tudo Instagram vs Facebook. `kpis`: [{nome, meta, instagram:{valor, anterior}, facebook:{valor, anterior}}] para alcance, cliques no link, visitas ao perfil, novos seguidores e mensagens/DMs; vendas online e receita ficam em total: {nome, valor, anterior, meta}.
   - `porFormato`: {stories:{funcionou:[], naoFuncionou:[], numeros:{instagram:{publicacoes, alcanceMedio, cliques, respostas}, facebook:{...}}}, reels:{...}, estaticos:{...}}.
   - `porRede`: {instagram:{alcance, cliquesLink, mensagens, novosSeguidores}, facebook:{...}, anterior:{instagram:{...}, facebook:{...}}, leitura:"o que a comparação Instagram vs Facebook diz e o que fazer em cada rede"}.
   - `melhorias`: [{acao, porque, como}], o bloco principal, com 3 a 5 melhorias concretas para a semana seguinte.
   - `mostrarMais` / `mostrarMenos`: o que a audiência pediu com os números e o que não funciona.
   - `acoes`: 3 a 5 ações concretas para a semana que começa.
7. Nunca inventar números. O que não vier do Metricool fica `null` e é assinalado nas notas.

## Avaliação diária dos publicados

Etapas do quadro: Ideia → Criativo → Revisão estratégica → Aprovação cliente → Aprovado → Publicado.

Todos os dias (rotina diária, depois de o Metricool estar ligado):
1. Ler os `cartoes` com `etapa: "publicado"` que ainda não têm documento em `privado/tracosdamor/resultados/<id do cartão>`, ou cuja avaliação tem menos de 48 horas.
2. No Metricool, encontrar a publicação do mesmo dia e formato (feed) e os stories do mesmo dia.
3. Escrever `privado/tracosdamor/resultados/<id>` com `{feed:{alcance, visualizacoes, gostos, comentarios, partilhas, guardados, cliques, respostas}, stories:[{...}], linkPost, feedFb:{...}, storiesFb:[{...}], linkPostFb, atualizadoEm}` (sem sufixo = Instagram, `Fb` = Facebook). O que não existir fica `null`.
4. Stories: avaliar no próprio dia ou no dia seguinte, antes de desaparecerem.
5. Feed: reavaliar 48 horas depois de publicar. Os números ainda crescem.

## Relatório (visível à cliente e à equipa)
Campos extra: `conclusoes` (o que os dados dizem, 3 a 5 frases) e `melhorias` [{acao, porque, como, autor:"claude"}].
O relatório mostra números, conclusões e melhorias. Nada da estratégia interna.

## Sugestões da semana (só a Tânia vê)
Escrever `privado/tracosdamor/sugestoes/tracosdamor-<inicio>` com:
{inicio, geradoEm, titulo, resumo, itens:[{area: instagram|comunicacao|email|vendas|atracao, titulo, porque, como, prioridade: alta|media|baixa, estado:"aplicar"}]}
Entre 8 e 12 sugestões concretas, aplicáveis nessa semana, baseadas nos dados e no que foi publicado.

## Dados (só a Tânia vê)
Tudo ao pormenor: `privado/tracosdamor/metricas/<semana>` e `privado/tracosdamor/resultados/<cartão>`.
