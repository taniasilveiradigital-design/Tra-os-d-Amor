import json, datetime, sys
OUT = sys.argv[1]

resumo = dict(
  veredito="Participar com condições",
  frase="O inverno fica a preço cheio. O verão que sobrou passa a preço de conjunto, para o próximo verão. Quem entra na lista escolhe primeiro.",
  objetivo="Proposta: 25 encomendas online e 120 inscritas na lista VIP entre 16 e 30 de novembro. Número de partida sem dados de stock nem da Black Friday passada: fecha-se no Raio-X com a Sílvia.",
  prioridades=["Clientes novas (lista VIP e primeira compra online)", "Libertar o stock de verão", "Caixa"],
  porque="A Traços ainda não vende online com regularidade. A Black Friday serve para criar a lista de quem compra e fazer as primeiras encomendas sem estragar o preço da coleção nova.",
  naoFazer=[
    "Não há desconto em nada da coleção de inverno: Casaco Trilha, camisa e calças ficam a preço cheio.",
    "Não há percentagens no feed nem a palavra \"saldos\". O preço aparece como aquilo que é: preço de conjunto.",
    "Não baixamos o verão abaixo do preço de despedida de outubro (ex.: 90 € no conjunto de 129,90 €). Se baixássemos, ensinávamos a cliente a esperar."
  ],
  conflito="Atenção ao preço de referência: o conjunto Trilha + camisa + calças tem condição até 1 de novembro. Como fica a preço cheio na Black Friday, não há problema. Se a Sílvia quiser pôr alguma peça de inverno em promoção a 27 de novembro, o preço de referência passa a ser o mais baixo dos 30 dias antes (desde 28 de outubro), ou seja, o preço da condição. Mais um motivo para o inverno ficar fora."
)

faltam = [
  ["Ficheiro de produtos: SKU, cor, tamanho, custo sem IVA, PVP, stock, vendas dos últimos 90 dias", "Sílvia", "Sem custo e stock não há margem real nem triagem por peça. Tudo o que é número na calculadora é exemplo até chegar este ficheiro."],
  ["Regime de IVA (23% ou isenta art. 53.º)", "Sílvia / contabilista", "Muda a receita líquida de cada peça."],
  ["Black Friday de 2025: fizeram? Que desconto, quantas peças, quanto faturaram, quanto em anúncios?", "Sílvia", "Para o Raio-X. Se não fizeram, partimos do zero e dizemos isso."],
  ["Portes, embalagem, taxa de pagamento, % de devoluções", "Sílvia", "Entram no lucro real de cada encomenda."],
  ["Encomendas que consegue enviar por dia e dias em que a transportadora recolhe", "Sílvia", "Define o teto da campanha."],
  ["Preço de cada peça de inverno (Trilha, camisa, calças) e tamanhos", "Sílvia", "Já estava em falta para a semana de 26 de outubro."],
  ["Prazo da fábrica e mínimo por cor", "Sílvia", "Saber se dá para repor alguma peça antes do Natal."],
  ["Lista de emails atual (quantos contactos, que ferramenta)", "Sílvia", "Define se o email é canal principal ou se começamos a lista agora."],
  ["Última data de encomenda para chegar antes do Natal", "Sílvia / transportadora", "Entra no calendário, no FAQ e nas respostas rápidas."]
]

passos = [
 dict(n="0", titulo="Conhecer a marca", estado="preenchido em parte",
  oQueFiz="Preenchi o prompt 0 com o que já sabemos da Traços. O que está entre [ ] tem de vir da Sílvia.",
  texto="""MARCA
Nome: Traços D'Amor
O que vende: moda infantil autoral, peças e conjuntos (coleção SS26 Jardim das Descobertas; inverno: Casaco Trilha, camisa e calças)
Onde vende: site tracosdamor.pt, Instagram @tracosdamor.pt, [lojas físicas?]

CLIENTE IDEAL
Quem compra: mães conscientes, que compram com intenção e querem algo que distinga
Idade: [ ]
O que valoriza: design autoral, qualidade que dura, peça com significado
Ticket médio (€): [ ]
Peças por encomenda, em média: [ ]

TOM DE MARCA
3 palavras: afetuosa, sensorial, intencional
Uma frase típica nossa: "Criado para durar mais do que uma estação — para durar memórias."

REGIME DE IVA: [ ]
CUSTOS DE VENDA: portes [ ] · portes grátis a partir de [ ] · embalagem [ ] · taxa de pagamento [ ] · devoluções [ ] · custo de devolução [ ] · anúncios [proposta: 5 a 10 € por dia, já previsto na estratégia] · unidades a vender [ ]
FÁBRICA: prazo [ ] · mínimo por cor [ ]
PISO DE MARGEM: [ ]"""),
 dict(n="1", titulo="Raio-X", estado="sem dados da BF passada",
  oQueFiz="Defini a prioridade e o objetivo com o que sabemos. A margem real da última Black Friday fica por calcular.",
  texto="""PRIORIDADE (proposta, confirma)
1.º Clientes novas: a marca ainda não tem vendas online regulares. Cada inscrita na lista é uma cliente que se pode trabalhar no Natal e em 2027.
2.º Libertar stock de verão: os conjuntos SS26 que sobraram.
3.º Caixa.

O QUE JÁ SABEMOS QUE CORRE MAL (do histórico de junho a outubro)
- 0 de 105 conteúdos publicados de junho a agosto tinham preço.
- Pedido de mensagem em 1 conteúdo em junho e 0 em julho e agosto.
- Muito conteúdo de identidade, pouco de decisão.
Se repetirmos isto na Black Friday, temos alcance sem encomendas.

OBJETIVO ÚNICO (proposta)
25 encomendas online e 120 inscritas na lista VIP entre 16 e 30 de novembro.

MAIOR MEDO (o que eu ponho, confirma com a Sílvia)
Parecer uma marca de saldos e perder o valor que se construiu.

CAPACIDADE: [encomendas por dia] × 4 dias de campanha = [ ] encomendas. Comparar com o objetivo antes de abrir anúncios."""),
 dict(n="2", titulo="Triagem de stock", estado="por peça, sem números",
  oQueFiz="Classifiquei as famílias de peças pelas regras do prompt. Os números entram quando houver ficheiro.",
  tabela=[
   ["Casaco Trilha", "OI26 (coleção atual)", "ESTRELA ou REVER", "Fica fora do desconto. Preço cheio com presente."],
   ["Camisa e calças de outono", "OI26 (coleção atual)", "ESTRELA ou REVER", "Fica fora do desconto."],
   ["Conjuntos SS26 (polo + calção, camisa + calção, vestido + camisa)", "PV, coleção anterior", "PARADA (provável)", "Entra como preço de conjunto. Aviso: é verão e linho, o desconto sozinho não escoa em novembro. Ângulo: próximo verão, um tamanho acima, e presente."],
   ["Peças soltas SS26 (t-shirts, jardineiras, vestido girafa)", "PV, coleção anterior", "PARADA ou ROTAÇÃO", "Pack com outra peça ou brinde. Decidir quando houver vendas dos 90 dias."]
  ],
  texto="Regra de cálculo: cobertura = stock ÷ (vendas dos 90 dias ÷ 3). Menos de 2 meses ESTRELA, 2 a 6 ROTAÇÃO, mais de 6 ou 0 vendas PARADA. Coleção atual com mais de 6 meses fica em REVER EM DEZEMBRO, nunca em desconto."),
 dict(n="3", titulo="Desconto vs. margem", estado="calculadora pronta, custos por preencher",
  oQueFiz="A calculadora abaixo usa as fórmulas do prompt 3. Os PVP dos conjuntos são os que já usámos em outubro. Custos e custos de venda são exemplos: muda-os e os números atualizam.",
  texto="O preço de despedida de outubro (129,90 € → 90 €) é um desconto de 31%. Na Black Friday o teto é esse. Se a calculadora mostrar que a 31% a margem fica abaixo do piso, o verão sai em pack ou com brinde, não com mais desconto."),
 dict(n="4", titulo="Desenha a oferta", estado="recomendação",
  oQueFiz="Três mecânicas comparadas. Recomendo a B.",
  tabela=[
   ["A · 30% em tudo", "Todas as peças", "Lucro baixo, margem incerta", "Má: liquidação", "Fácil", "Descartada"],
   ["B · Inverno a preço cheio, verão a preço de conjunto", "Inverno com presente; conjuntos SS26 ao preço de despedida", "Inverno com margem cheia; verão igual a outubro", "Boa: nada da coleção nova baixa", "Média: duas regras", "Recomendada"],
   ["C · Sem desconto, só presente e portes", "Todas as peças a preço cheio + embrulho de Natal e portes grátis", "Margem cheia", "Ótima", "Fácil", "Segura, mas não escoa o verão"]
  ],
  texto="""PORQUÊ A B
A coleção de inverno acabou de chegar: baixar agora é dizer que vale menos. O verão que sobrou precisa de uma razão para sair em novembro, e a razão é o próximo verão e o presente, não a percentagem. E quem já comprou o verão a 90 € em outubro não se sente enganada.

REGRAS
- Datas: lista VIP de 16 a 25 nov · acesso VIP 26 nov às 10h · aberto a todas 27 nov às 10h · fecha 30 nov às 23h59.
- Entram: conjuntos SS26 a preço de conjunto [preços por conjunto]. Inverno a preço cheio com embrulho de Natal e cartão escrito pela Sílvia.
- Ficam fora: tudo o que for ESTRELA ou REVER. Nada de inverno com desconto.
- Limite: preço de conjunto nunca abaixo do de outubro. Stock só o que existe, sem reposição.
- Trocas: online a cliente tem sempre 14 dias para devolver depois de receber.
- VIP: escolhe primeiro (24 horas antes) e recebe o embrulho de Natal em qualquer encomenda.
- Envio: [encomendas por dia], contando com os dias sem recolha [ ].
- Preço de referência: os conjuntos estiveram a 90 € até 11 de outubro. A 27 de novembro, o preço de referência é o mais baixo desde 28 de outubro: se até lá estiverem a preço cheio, é o preço cheio. Confirmar com a contabilidade.

FRASE DA OFERTA (18 palavras)
O inverno fica como é. O verão que guardámos passa a preço de conjunto, para crescer até julho.

CARTÃO DE DECISÃO
Participar com condições.
Objetivo: 25 encomendas online e 120 inscritas na lista VIP.
Não vou: baixar o inverno · gritar percentagens · descer abaixo do preço de outubro.""")
]

fases = [
 dict(fase="Preparar", datas="até 1 nov", objetivo="Lançar o inverno e fechar outubro com a condição das três peças.", mensagem="Já está no quadro: Casaco Trilha, camisa e calças.", canais="Instagram"),
 dict(fase="Aquecer", datas="2 a 15 nov", objetivo="Mostrar as peças, o presente e o porquê da marca. Zero desconto.", mensagem="O que se oferece a uma criança devia durar mais do que o embrulho.", canais="Instagram, Facebook, email à lista atual"),
 dict(fase="Lista VIP", datas="16 a 25 nov", objetivo="Encher a lista: quem entra escolhe primeiro e recebe embrulho de Natal.", mensagem="Este ano há uma porta que abre um dia antes.", canais="Instagram (comentar VIP, link na bio), stories, email"),
 dict(fase="Acesso VIP", datas="26 nov, 10h", objetivo="Primeiras encomendas com a lista.", mensagem="A porta abriu. É só para quem pediu.", canais="Email + WhatsApp à lista VIP"),
 dict(fase="Abrir", datas="27 a 29 nov", objetivo="Encomendas de quem não entrou na lista.", mensagem="Preço de conjunto no verão que guardámos. O inverno, como sempre.", canais="Instagram, Facebook, email, anúncios"),
 dict(fase="Fechar", datas="30 nov, até 23h59", objetivo="Última chamada com data real.", mensagem="Hoje à noite fecha. Depois o verão volta ao preço dele.", canais="Email, stories, WhatsApp VIP"),
 dict(fase="Depois", datas="1 a 6 dez", objetivo="Natal a preço cheio, trocas, agradecer.", mensagem="O que ficou é para o Natal, ao preço de sempre.", canais="Instagram, email às clientes")
]

emails = [
 dict(id="e1", data="2026-11-16", fase="Lista VIP", assunto="Este ano há uma porta que abre um dia antes", preview="Para quem quer escolher primeiro.",
  corpo="""Olá,

Este ano não vamos encher o site de percentagens.

Guardámos alguns conjuntos do Jardim das Descobertas. Vão passar a preço de conjunto, para vestirem o próximo verão um tamanho acima. O inverno — o Casaco Trilha, a camisa e as calças — fica como é.

Quem entrar na lista escolhe primeiro: a 26 de novembro, às 10h, um dia antes de todos. E qualquer encomenda segue com embrulho de Natal.

[Quero entrar na lista]

Há poucos tamanhos de cada conjunto. Não vamos repor.

Com carinho,
Sílvia
Traços D'Amor"""),
 dict(id="e2", data="2026-11-26", fase="Acesso VIP", assunto="A porta abriu (só para ti, até amanhã às 10h)", preview="Escolhe primeiro. Embrulho de Natal incluído.",
  corpo="""Olá,

Como prometido, abriu primeiro para ti.

O que há:
- Conjuntos do Jardim das Descobertas a preço de conjunto: [conjunto 1] [preço] · [conjunto 2] [preço] · [conjunto 3] [preço]
- O inverno a preço de sempre: Casaco Trilha [preço] · camisa [preço] · calças [preço]
- Embrulho de Natal e um cartão escrito à mão em todas as encomendas.

[Ver os conjuntos]

Para escolher o tamanho: se a criança veste hoje 4 anos, no próximo verão vai vestir 5. Se tiveres dúvidas, responde a este email com a idade e a altura e eu digo-te qual.

As condições, para não haver surpresas:
- Envio em [n.º] dias úteis.
- Tens 14 dias depois de receberes para devolver, sem precisares de explicar.
- Trocas de tamanho [condição].

Amanhã às 10h abre para todos.

Sílvia"""),
 dict(id="e3", data="2026-11-30", fase="Fechar", assunto="Fecha hoje às 23h59", preview="Depois o verão volta ao preço dele.",
  corpo="""Olá,

Hoje à noite fechamos.

Os conjuntos do Jardim das Descobertas voltam amanhã ao preço deles. Neste momento restam [n.º] tamanhos no total — vês quais no site.

[Ver o que resta]

Se é para oferecer no Natal, encomenda até [data] para chegar a tempo. Segue com embrulho e cartão.

Obrigada por terem estado deste lado nesta semana.

Sílvia""")
]

legendas = [
 dict(data="2026-11-04", fase="Aquecer", texto="""Há presentes que ficam na gaveta.
E há os que ela pede para vestir outra vez.

O Casaco Trilha foi feito para os dias de frio que ainda são de brincar lá fora.
[preço] € · tamanhos [ ] · link na bio

Comenta TRILHA e envio-te as medidas."""),
 dict(data="2026-11-16", fase="Lista VIP", texto="""Este ano não vamos encher o site de percentagens.

Guardámos alguns conjuntos do verão. Vão passar a preço de conjunto — para vestirem julho um tamanho acima.

Quem entrar na lista escolhe primeiro, a 26 de novembro.
Comenta VIP e eu envio-te o link para entrares."""),
 dict(data="2026-11-26", fase="Acesso VIP", texto="""Hoje abriu primeiro para quem pediu.

Se ainda não estás na lista, amanhã às 10h abre para todos.
O verão que guardámos fica a preço de conjunto. O inverno, como sempre.

Todas as encomendas seguem com embrulho de Natal."""),
 dict(data="2026-11-27", fase="Abrir", texto="""Polo verde e calção zebra. [preço de conjunto] €.
Para o verão que vem, um tamanho acima.

Escolhemos não baixar o inverno.
Escolhemos dar uma segunda vida ao verão que guardámos.

Até segunda, 30, às 23h59. Link na bio."""),
 dict(data="2026-11-30", fase="Fechar", texto="""Último dia.

À meia-noite, o verão volta ao preço dele.
Restam [n.º] tamanhos — estão todos no site.

Se é presente, segue embrulhado e com cartão.""")
]

whatsapp = dict(data="2026-11-26", texto="""Olá [nome], é a Sílvia da Traços D'Amor.

Como prometido, abriu primeiro para ti: [link]

Conjuntos do verão a preço de conjunto e o inverno a preço de sempre. Tudo segue com embrulho de Natal.

Amanhã às 10h abre para todos. Se precisares de ajuda com o tamanho, responde aqui com a idade e a altura.""")

# calendário dia a dia
L = {x["data"]: x["texto"] for x in legendas}
def row(data, hora, fase, canal, formato, tema, peca, gancho, cta, imagem, texto=""):
    return dict(data=data, hora=hora, fase=fase, canal=canal, formato=formato, tema=tema, peca=peca, gancho=gancho, cta=cta, imagem=imagem, texto=texto)
cal = [
 row("2026-11-02","19h","Aquecer","Instagram","Reel","Do frio ao recreio","Casaco Trilha","\"Ela não tira o casaco. Nem dentro de casa.\"","Comenta TRILHA","Sessão A: criança a brincar no exterior com o Trilha",
   "Ela não tira o casaco.\nNem dentro de casa.\n\nO Casaco Trilha foi feito para os dias que ainda são de brincar lá fora.\n[preço] € · link na bio\n\nComenta TRILHA e envio-te as medidas."),
 row("2026-11-03","12h","Aquecer","Stories","2 stories","Medidas reais","Casaco Trilha","Fita métrica no casaco","Caixa de pergunta: idade e altura","Sessão A: detalhe das medidas",
   "Story 1: vídeo da fita métrica no casaco. Texto: \"Medidas em cm, para não haver dúvidas.\"\nStory 2: caixa \"Diz-me a idade e a altura, eu digo-te o tamanho.\""),
 row("2026-11-04","19h","Aquecer","Instagram","Carrossel","Presente que não fica na gaveta","Trilha + camisa + calças","\"Há presentes que ficam na gaveta.\"","Comenta TRILHA","Sessão A: as três peças em flat lay e numa criança", L["2026-11-04"]),
 row("2026-11-05","12h","Aquecer","Stories","2 stories","Bastidores","Atelier","A Sílvia a dobrar uma peça","Sondagem \"Já pensaste nos presentes de Natal?\"","Sessão B: bastidores com a Sílvia",
   "Story 1: a Sílvia a dobrar e embrulhar uma peça. Texto: \"Cada encomenda sai daqui.\"\nStory 2: sondagem \"Já pensaste nos presentes de Natal?\" Sim / Ainda não."),
 row("2026-11-06","19h","Aquecer","Instagram","Reel","Um dia inteiro","Camisa + calças","\"8h escola. 17h parque. 19h jantar dos avós.\"","Link na bio","Sessão A: a mesma criança em três momentos",
   "8h escola. 17h parque. 19h jantar dos avós.\nA mesma camisa. As mesmas calças.\n\nFeitas para acompanhar o dia, não para ficar bem numa foto.\nCamisa [preço] € · calças [preço] € · link na bio"),
 row("2026-11-07","11h","Aquecer","Stories","2 stories","Textura","Camisa","Mão a passar no tecido","Link da camisa","Sessão A: close da textura",
   "Story 1: vídeo de 5 segundos da mão no tecido. Texto: \"Toca-lhe.\"\nStory 2: foto da camisa com preço e sticker de link."),
 row("2026-11-08","11h","Aquecer","Stories","2 stories","Mães reais","Peças de clientes","Foto de uma cliente","Responder com a foto","Fotos enviadas por clientes [pedir autorização]",
   "Story 1: foto de cliente com a peça (com autorização). Texto: \"Foi assim que a [nome] vestiu.\"\nStory 2: \"Tens uma foto com uma peça nossa? Envia-nos.\""),
 row("2026-11-09","19h","Aquecer","Instagram","Reel","A Sílvia apresenta","Marca","\"Eu sou a Sílvia e isto começou com um desenho.\"","Seguir a conta","Sessão B: Sílvia a falar para a câmara (30 s)",
   "Eu sou a Sílvia.\nA Traços começou com um desenho: uma criança num baloiço, com balões em forma de coração.\n\nAinda hoje desenhamos assim: devagar, com tempo, para durar.\nwe are dreamers"),
 row("2026-11-10","12h","Aquecer","Stories","2 stories","Como cuidar","Todas","\"Lava assim e dura anos.\"","Guardar o story","Sessão B: máquina, roupa a secar",
   "Story 1: \"30 graus, do avesso, a secar à sombra.\"\nStory 2: \"É por isso que passam para o irmão.\""),
 row("2026-11-11","19h","Aquecer","Instagram","Carrossel","O verão que guardámos","Conjuntos SS26","\"Guardámos isto para julho.\"","Seguir para não perder","Fotos SS26 que já existem (Drive)",
   "Slide 1: Guardámos isto para julho.\nSlide 2-4: os três conjuntos, um por slide, sem preço.\nSlide 5: Se hoje veste 4 anos, em julho veste 5.\nLegenda: Há peças que esperam pelo verão certo. Em breve contamos-te como.\n(Sem preço, sem desconto: é aquecimento.)"),
 row("2026-11-12","12h","Aquecer","Stories","2 stories","Tabela de tamanhos","Conjuntos SS26","\"Um tamanho acima, como sabes?\"","Caixa de pergunta","Tabela de medidas em design",
   "Story 1: tabela de medidas por idade.\nStory 2: caixa \"Diz-me a idade, eu digo-te o tamanho para julho.\""),
 row("2026-11-13","19h","Aquecer","Instagram","Reel","Fotos de família no Natal","Trilha + conjunto","\"A foto que vais guardar.\"","Comenta NATAL","Sessão A: família, luz de fim de tarde",
   "A foto que vais guardar daqui a vinte anos não é a do sofá.\nÉ a do passeio de dezembro.\n\nComenta NATAL e ajudo-te a escolher o look."),
 row("2026-11-14","11h","Aquecer","Stories","2 stories","Prova social","Clientes","Mensagem de uma cliente","Link na bio","Print de mensagem [autorização]",
   "Story 1: print de mensagem de cliente (sem nome).\nStory 2: \"Obrigada. É por isto que fazemos.\""),
 row("2026-11-15","11h","Aquecer","Stories","2 stories","Spoiler da lista","Lista VIP","\"Amanhã conto-te uma coisa.\"","Ativar notificações","Story simples, fundo terracota",
   "Story 1: \"Amanhã conto-te uma coisa. Só para quem quer escolher primeiro.\"\nStory 2: sticker de lembrete."),
 row("2026-11-16","19h","Lista VIP","Instagram + email","Reel + email","Abre a lista VIP","Conjuntos SS26","\"Este ano não vamos encher o site de percentagens.\"","Comenta VIP","Sessão B: Sílvia a falar (15 s) + conjuntos", L["2026-11-16"]),
 row("2026-11-17","12h","Lista VIP","Stories","2 stories","Como entrar","Lista VIP","\"Três segundos para entrares.\"","Link da lista","Gravação de ecrã do formulário",
   "Story 1: gravação do ecrã a preencher o formulário.\nStory 2: sticker de link \"Entrar na lista\"."),
 row("2026-11-18","19h","Lista VIP","Instagram","Carrossel","O que ganha quem está na lista","Lista VIP","\"Três coisas para quem entra.\"","Link na bio","Design: 4 slides tipográficos",
   "Slide 1: Três coisas para quem entra na lista.\nSlide 2: Escolhes primeiro, a 26 de novembro, às 10h.\nSlide 3: Embrulho de Natal em qualquer encomenda.\nSlide 4: Ajuda com o tamanho, por mensagem, comigo.\nLegenda: A lista fecha a 25 de novembro. Link na bio."),
 row("2026-11-19","12h","Lista VIP","Stories","2 stories","Tamanhos que existem","Conjuntos SS26","\"Isto é o que há. Não repomos.\"","Entrar na lista","Foto do stock real por tamanho",
   "Story 1: \"Isto é o que há de cada conjunto. Não vamos repor.\" (só se for verdade)\nStory 2: link da lista."),
 row("2026-11-20","19h","Lista VIP","Instagram","Reel","Para crescer até julho","Conjunto girafa","\"Em julho vai servir.\"","Comenta VIP","Fotos SS26 + criança a crescer (marca na parede)",
   "Em julho vai servir.\nE vai lembrar-te deste inverno.\n\nO verão que guardámos passa a preço de conjunto. Quem está na lista escolhe primeiro.\nComenta VIP."),
 row("2026-11-21","11h","Lista VIP","Stories","2 stories","Inverno a preço cheio","Casaco Trilha","\"Porque o inverno não baixa.\"","Sondagem","Sessão A",
   "Story 1: \"O inverno não baixa. Acabou de chegar.\"\nStory 2: sondagem \"Concordas?\" Sim / Prefiro desconto. (lemos as respostas)"),
 row("2026-11-22","11h","Lista VIP","Stories","2 stories","Contagem","Lista VIP","\"Faltam 4 dias.\"","Link da lista","Story simples",
   "Story 1: contagem decrescente para 26 de novembro.\nStory 2: link da lista."),
 row("2026-11-23","19h","Lista VIP","Instagram","Reel","Embrulho de Natal","Embrulho","\"Chega assim.\"","Link na bio","Sessão B: abrir uma encomenda",
   "Chega assim.\nPapel, fita, um cartão escrito à mão.\n\nNa próxima semana, todas as encomendas seguem embrulhadas para o Natal.\nA lista fecha quarta. Link na bio."),
 row("2026-11-24","12h","Lista VIP","Stories","2 stories","Perguntas","Lista VIP","\"Perguntaram-me…\"","Caixa de pergunta","Story simples",
   "Story 1 e 2: respostas às 2 perguntas mais feitas por mensagem."),
 row("2026-11-25","19h","Lista VIP","Instagram + email","Carrossel","Último dia da lista","Lista VIP","\"Hoje fecha a lista.\"","Link na bio","Design",
   "Slide 1: Hoje fecha a lista.\nSlide 2: Amanhã às 10h escolhes primeiro.\nSlide 3: Link na bio.\nEmail curto à lista atual: \"A lista fecha hoje às 23h59.\""),
 row("2026-11-26","10h","Acesso VIP","Email + WhatsApp + Instagram","Email, WhatsApp, story","Abre para a lista","Conjuntos + inverno","\"A porta abriu.\"","Link exclusivo","—", L["2026-11-26"]),
 row("2026-11-27","10h","Abrir","Instagram + Facebook + email","Reel + email","Aberto a todos","Conjunto zebra","\"Polo verde e calção zebra.\"","Link na bio","Fotos SS26", L["2026-11-27"]),
 row("2026-11-28","11h","Abrir","Stories","3 stories","O que resta","Conjuntos","\"Atualização de tamanhos.\"","Link do conjunto","Story com stock real",
   "Story 1: tamanhos que restam, por conjunto (só se for verdade).\nStory 2: foto de uma encomenda embrulhada.\nStory 3: link."),
 row("2026-11-29","11h","Abrir","Stories","2 stories","A Sílvia a embrulhar","Encomendas","\"Já saíram [n.º] encomendas.\"","Link na bio","Sessão B",
   "Story 1: a Sílvia a embrulhar. Texto: \"Obrigada. Já saíram [n.º].\"\nStory 2: \"Fecha amanhã às 23h59.\""),
 row("2026-11-30","19h","Fechar","Instagram + email + WhatsApp VIP","Estático + email","Último dia","Conjuntos","\"Último dia.\"","Link na bio","Foto SS26", L["2026-11-30"]),
 row("2026-12-01","12h","Depois","Stories","2 stories","Obrigada","Marca","\"Obrigada.\"","—","Sessão B",
   "Story 1: \"Obrigada a todas. Estamos a embrulhar tudo.\"\nStory 2: \"Trocas e devoluções: tens 14 dias depois de receberes.\""),
 row("2026-12-02","19h","Depois","Instagram","Carrossel","Natal a preço cheio","Trilha + camisa + calças","\"Para o Natal, o inverno inteiro.\"","Comenta NATAL","Sessão A",
   "Slide 1: Para o Natal, o inverno inteiro.\nSlides 2-4: as três peças com preço.\nSlide 5: Encomenda até [data] para chegar antes do Natal.\nLegenda: Ao preço de sempre. Segue embrulhado."),
 row("2026-12-03","12h","Depois","Stories","2 stories","Data limite de Natal","Todas","\"Até [data] chega a tempo.\"","Link na bio","Story simples", "Story 1: data limite.\nStory 2: link."),
 row("2026-12-04","19h","Depois","Instagram","Reel","O que esgotou","Peças esgotadas","\"Já não há.\"","Seguir para a próxima coleção","Fotos das peças esgotadas",
   "Já não há.\nE não vamos repetir.\n\nObrigada a quem levou estas peças para casa. A próxima coleção chega em [mês]."),
 row("2026-12-05","11h","Depois","Stories","2 stories","Fotos de clientes","Clientes","\"Chegou assim.\"","Enviar foto","Fotos de clientes [autorização]", "Story 1 e 2: fotos de clientes com as encomendas."),
 row("2026-12-06","11h","Depois","Stories","2 stories","Natal","Inverno","\"Ainda vais a tempo.\"","Link na bio","Story simples", "Story 1: \"Ainda vais a tempo do Natal.\"\nStory 2: link.")
]

producao = [
 dict(sessao="Sessão A · exterior com criança", quando="até 30 out", oQue="Casaco Trilha a brincar no exterior; camisa + calças em três momentos do dia; família com luz de fim de tarde; textura e medidas.", para="2, 3, 4, 6, 7, 13, 21 nov e 2 dez"),
 dict(sessao="Sessão B · Sílvia e atelier", quando="até 6 nov", oQue="Sílvia a falar para a câmara (30 s e 15 s); a embrulhar; abrir uma encomenda; cuidados de lavagem.", para="5, 9, 10, 16, 23, 29 nov e 1 dez"),
 dict(sessao="Design (sem fotografia)", quando="até 13 nov", oQue="Tabela de medidas; slides tipográficos da lista VIP; contagem decrescente; story do stock real.", para="12, 15, 18, 22, 25, 28 nov"),
 dict(sessao="Pedir às clientes", quando="desde já", oQue="Fotos de crianças com peças da Traços, com autorização por escrito.", para="8, 14 nov e 5 dez")
]

kit = dict(
 respostas=[
  ["Como funciona a oferta", "O inverno fica a preço de sempre. Os conjuntos do verão passam a preço de conjunto até 30 de novembro às 23h59. Todas as encomendas seguem com embrulho de Natal."],
  ["Posso juntar a outro desconto", "Não acumula com outros códigos [confirmar]. O preço de conjunto já é o preço final."],
  ["Tamanhos", "Diz-me a idade e a altura da criança e eu digo-te o tamanho. Para o próximo verão, aconselho um tamanho acima."],
  ["Stock", "O que está no site é o que existe. Não vamos repor estes conjuntos."],
  ["Prazos", "Enviamos em [n.º] dias úteis. Recebes o número de seguimento por email."],
  ["Portes", "Portes [valor] €, grátis a partir de [valor] €."],
  ["Trocas", "Trocas de tamanho [condição e prazo]. Escreve-nos e tratamos de tudo."],
  ["Devoluções", "Tens 14 dias depois de receberes para devolver, sem precisares de explicar. Os portes de devolução são [pagos por quem]."],
  ["O desconto não aparece no carrinho", "Obrigada por avisares. Diz-me que conjunto estás a ver e eu confirmo já o preço."],
  ["Encomenda atrasada", "Peço desculpa. Vou ver agora com a transportadora e respondo-te hoje com o ponto de situação."],
  ["Pagamento pendente", "A referência Multibanco é válida durante [n.º] horas. Se expirar, envio-te uma nova."],
  ["Peça esgotada", "Esse tamanho esgotou e não vamos repor. Posso mostrar-te o conjunto mais parecido no tamanho certo?"]
 ],
 faq=[
  ["Até quando posso comprar?", "Até 30 de novembro, às 23h59."],
  ["O inverno tem desconto?", "Não. O Casaco Trilha, a camisa e as calças ficam a preço de sempre, com embrulho de Natal."],
  ["Que tamanho escolho para o próximo verão?", "Normalmente um acima do que veste hoje. Se tiveres dúvidas, envia-nos a idade e a altura."],
  ["Chega antes do Natal?", "Encomendas até [data] chegam antes do Natal."],
  ["Posso devolver?", "Sim. Tens 14 dias depois de receberes."],
  ["Vão repor?", "Não. O que está no site é o que existe."]
 ],
 politica="""Trocas e devoluções · Black Friday 2026
- Tens 14 dias depois de receberes a encomenda para devolver, sem precisares de dar motivo. Devolvemos o valor pago, pelo mesmo meio, até 14 dias depois de recebermos a peça.
- A peça tem de vir sem uso e com a etiqueta.
- Trocas de tamanho: [prazo, ex.: até 15 de janeiro] · [custo].
- Se compraste um conjunto a preço de conjunto e devolves só uma peça: [opção 1: devolvemos o valor proporcional da peça · opção 2: só aceitamos o conjunto completo — confirmar com jurista, a 2 pode não ser válida].
- Portes de devolução: [pagos por quem].
Nota: confirmar com a contabilidade ou um jurista antes de publicar.""",
 checklist=dict(
  antes7=["Preços de conjunto e de inverno confirmados no site", "Stock por tamanho atualizado no site", "Formulário da lista VIP a funcionar e testado", "Emails 1, 2 e 3 agendados", "Embrulhos e cartões preparados para [n.º] encomendas", "Respostas rápidas guardadas no Instagram"],
  vespera=["Link exclusivo VIP testado", "Mensagem de WhatsApp pronta com a lista", "Anúncios aprovados", "Transportadora avisada do volume"],
  durante=["Responder a mensagens em menos de 1 hora", "Atualizar o stock nos stories só se for verdade", "Contar encomendas por dia vs capacidade", "Parar anúncios se a capacidade encher"],
  depois=["Repor preços às 00h01 de 1 de dezembro", "Enviar email 1 do pós-campanha", "Registar devoluções", "Preencher as 3 métricas a 31 de dezembro"]
 ),
 atraso="""Olá [nome],

A tua encomenda está a demorar mais do que te prometemos e não queria que tivesses de perguntar.

[Motivo, em uma frase.] Sai daqui até [data] e envio-te o seguimento assim que sair.

Peço desculpa. Obrigada pela paciência.
Sílvia"""
)

pos = dict(
 emails=[
  dict(quando="1 dia depois da entrega", assunto="Chegou. Como cuidar para durar", corpo="Obrigada por teres escolhido a Traços.\n\nPara durar: 30 graus, do avesso, a secar à sombra. Passar a ferro do avesso.\n\nSe alguma coisa não estiver bem, responde a este email."),
  dict(quando="7 dias depois", assunto="Três formas de usar o que escolheste", corpo="O mesmo conjunto, três dias diferentes. [3 fotos com combinações.]\n\nSe precisares de ajuda para combinar, responde-me."),
  dict(quando="16 dias depois (depois dos 14 de devolução)", assunto="Como ficou?", corpo="Gostávamos de ver. Se quiseres, envia-nos uma foto. Com autorização, partilhamos.\n\nE se tiveres um minuto, conta-nos o que achaste: [link de avaliação]."),
  dict(quando="25 dias depois", assunto="Isto começou com um desenho", corpo="Uma criança num baloiço, com balões em forma de coração. Foi assim que a Traços começou.\n\n[História da Sílvia em 5 frases.]\n\nwe are dreamers"),
  dict(quando="Quando abre a próxima coleção", assunto="Antes de todos", corpo="A próxima coleção chega a [data]. Quem já comprou vê primeiro. [link]\n\nSem códigos. Só primeiro.")
 ],
 grupos=[
  dict(nome="Novas que compraram com preço de conjunto", como="Export de encomendas: email sem encomendas antes de 26 nov + encomenda entre 26 e 30 nov com produto SS26 a preço de conjunto.", recebe="Os 5 emails. Convite para a próxima coleção.", naoRecebe="Nenhum código de desconto."),
  dict(nome="Antigas que compram a preço cheio", como="Email com encomenda antes de 26 nov a preço cheio.", recebe="Agradecimento pessoal da Sílvia e acesso antecipado à próxima coleção.", naoRecebe="Emails de oferta."),
  dict(nome="Antigas que só compram com desconto", como="Email com encomendas só em outubro (despedida) ou na Black Friday.", recebe="Emails de história e de produto.", naoRecebe="Avisos de promoção antes do tempo.")
 ],
 notaGrupos="As novas que compraram a preço cheio (inverno) entram no grupo 2: já mostraram que compram pelo valor.",
 metricas=[
  dict(nome="Margem líquida real", formula="Lucro real ÷ receita líquida, com devoluções e anúncios reais (fórmula do passo 3)", dados="Encomendas, peças, custos reais, anúncios gastos, devoluções"),
  dict(nome="Devolução", formula="Peças devolvidas ÷ peças vendidas na campanha", dados="Registo de devoluções até 14 de dezembro"),
  dict(nome="Recompra", formula="Clientes novas com segunda compra sem desconto ÷ clientes novas", dados="Export de encomendas a 31 de março de 2027")
 ],
 relatorio="Objetivo: 25 encomendas e 120 na lista → resultado [ ]\nRepetir: [ ]\nMudar: [ ]\nNunca mais: [ ]\nComeçar a preparar a Black Friday 2027 em: setembro de 2027."
)

calc = dict(
 iva=23, portes=4.9, portesGratis=None, pecasEnc=2, embalagem=1.5, taxa=2.5, devol=8, custoDevol=6, anuncios=150, unidades=40, piso=30,
 pecas=[
  dict(nome="Conjunto polo verde + calção zebra", pvp=135.9, custo=None, stock=None, precoBF=95),
  dict(nome="Conjunto camisa azul + calção salmão", pvp=129.9, custo=None, stock=None, precoBF=90),
  dict(nome="Conjunto vestido + camisa menina", pvp=176.9, custo=None, stock=None, precoBF=123),
  dict(nome="Casaco Trilha (fica fora)", pvp=None, custo=None, stock=None, precoBF=None)
 ]
)

bf = dict(versao=1, criadoEm="2026-10-09T12:00:00.000Z", resumo=resumo, faltam=faltam, passos=passos,
  comunicacao=dict(fases=fases, emails=emails, legendas=legendas, whatsapp=whatsapp),
  calendario=cal, producao=producao, kit=kit, pos=pos, calc=calc, revisao={})
json.dump(bf, open(OUT, "w"), ensure_ascii=False)
print(len(json.dumps(bf, ensure_ascii=False)), "chars,", len(cal), "dias")
