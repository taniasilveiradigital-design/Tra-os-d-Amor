import json,sys
O=sys.argv[1]; C="tracosdamor"; NOW="2026-10-09T18:00:00.000Z"
bf=dict(nome="Black Friday", inicio="2026-11-02", fim="2026-12-06", estado="ativa", plano="plano",
 objetivo="25 encomendas online e 120 inscritas na lista VIP entre 16 e 30 de novembro (número de partida, confirmar no Raio-X).",
 oferta="Inverno (Casaco Trilha, camisa, calças) a preço cheio com embrulho de Natal e cartão escrito pela Sílvia. Conjuntos de verão SS26 a preço de conjunto, nunca abaixo do preço de despedida de outubro. Lista VIP compra 24 horas antes.",
 publico="Mães que escolhem com intenção; avós, madrinhas e padrinhos à procura de um presente que fica; quem já reagiu ou perguntou nas últimas semanas.",
 mensagem="O inverno fica como é. O verão que guardámos passa a preço de conjunto, para crescer até julho.",
 regras="Na fase Aquecer (2 a 15 nov) não se fala de desconto nem de Black Friday.\nO inverno aparece sempre a preço cheio.\nO preço de conjunto aparece como aquilo que é, nunca como liquidação nem com percentagens.\nUrgência só verdadeira: data real ou stock real.\nWhatsApp e email só para quem pediu ou subscreveu.\nPelo menos um email diz as condições de troca e os 14 dias para devolver.\nNo máximo uma exclamação por texto.",
 naoFazer="Não há desconto em nada da coleção de inverno.\nNão há percentagens no feed nem a palavra saldos.\nNão descemos o verão abaixo do preço de outubro.",
 fases=[
  dict(fase="Aquecer", inicio="2026-11-02", fim="2026-11-15", objetivo="Mostrar as peças, o presente e o porquê da marca. Zero desconto.", mensagem="O que se oferece a uma criança devia durar mais do que o embrulho.", canais="Instagram, Facebook, canal do Instagram"),
  dict(fase="Lista VIP", inicio="2026-11-16", fim="2026-11-25", objetivo="Encher a lista: quem entra escolhe primeiro e recebe embrulho de Natal.", mensagem="Este ano há uma porta que abre um dia antes.", canais="Instagram, email, canal do Instagram"),
  dict(fase="Acesso VIP", inicio="2026-11-26", fim="2026-11-26", objetivo="Primeiras encomendas com a lista.", mensagem="A porta abriu. É só para quem pediu.", canais="Email, WhatsApp VIP, canal do Instagram"),
  dict(fase="Abrir", inicio="2026-11-27", fim="2026-11-29", objetivo="Encomendas de quem não entrou na lista.", mensagem="Preço de conjunto no verão que guardámos. O inverno, como sempre.", canais="Instagram, Facebook, email, anúncios"),
  dict(fase="Fechar", inicio="2026-11-30", fim="2026-11-30", objetivo="Última chamada com data real.", mensagem="Hoje à noite fecha. Depois o verão volta ao preço dele.", canais="Email, stories, WhatsApp VIP"),
  dict(fase="Depois", inicio="2026-12-01", fim="2026-12-06", objetivo="Natal a preço cheio, trocas, agradecer.", mensagem="O que ficou é para o Natal, ao preço de sempre.", canais="Instagram, email às clientes")],
 notas="O plano completo (9 passos da Imersão, calculadora, calendário dia a dia, kit e pós-campanha) está nesta campanha.", criadoEm=NOW, atualizadoEm=NOW)
natal=dict(nome="Natal", inicio="2026-12-01", fim="2026-12-24", estado="rascunho",
 objetivo="Proposta: vender o inverno a preço cheio como presente que fica, com data limite de envio real. Rever com a Sílvia.",
 oferta="Sem desconto. Embrulho de Natal e cartão escrito à mão em todas as encomendas. Ajuda com o tamanho por mensagem.",
 publico="Mães, avós, madrinhas e padrinhos que querem oferecer uma peça com significado.",
 mensagem="Há presentes que se abrem. E há os que se vestem até ao próximo Natal.",
 regras="Preço cheio em tudo.\nA data limite de encomenda para chegar antes do Natal aparece em todos os conteúdos da última semana.\nNada de urgência inventada: só a data real da transportadora.\nOs clientes da Black Friday recebem o email de Natal sem oferta.",
 naoFazer="Não fazemos códigos de Natal.\nNão prometemos entregas que não dependem de nós.",
 fases=[
  dict(fase="Natal a preço de sempre", inicio="2026-12-01", fim="2026-12-06", objetivo="Fechar a Black Friday e virar para o Natal sem desconto.", mensagem="O que ficou é para o Natal, ao preço de sempre.", canais="Instagram, email"),
  dict(fase="Presentes com significado", inicio="2026-12-07", fim="2026-12-15", objetivo="Ajudar quem oferece: por idade, por ocasião, para avós e madrinhas.", mensagem="Um presente que fica.", canais="Instagram, email, canal do Instagram"),
  dict(fase="Última data de envio", inicio="2026-12-16", fim="2026-12-20", objetivo="Encomendas antes da data limite real.", mensagem="Até [data] chega a tempo.", canais="Instagram, email, WhatsApp VIP"),
  dict(fase="Chega a tempo", inicio="2026-12-21", fim="2026-12-24", objetivo="Agradecer e mostrar as encomendas a sair. Sem vender à pressa.", mensagem="Obrigada por levarem a Traços para o vosso Natal.", canais="Instagram, canal do Instagram")],
 notas="Rascunho meu. Falta: data limite da transportadora, se há loja física ou entrega em mão, peças de Natal.", criadoEm=NOW, atualizadoEm=NOW)
json.dump(bf,open(O+"/campanhas/blackfriday.json","w"),ensure_ascii=False)
json.dump(natal,open(O+"/campanhas/natal.json","w"),ensure_ascii=False)
com=dict(
 recomendacao="Recomendo email marketing em três camadas, e não só newsletter: uma newsletter mensal que mantém a lista viva, emails de campanha com datas (Black Friday, Natal, primavera) e duas automações que trabalham sozinhas. Uma newsletter só, para uma marca que está a começar a vender online, não chega para vender e cansa se for só promoção. No Instagram, um canal de transmissão para as mais próximas. No WhatsApp, uma lista de transmissão VIP, não um grupo: o grupo mostra os números de todas, enche-se de conversa e a marca perde o controlo do tom.",
 email=dict(nome="Carta da Traços + campanhas + automações", porque="Dono da relação: o Instagram pode mudar, a lista é da marca. Leva a cliente do conteúdo à compra e traz quem comprou de volta sem desconto.", cadencia="Newsletter na primeira terça de cada mês, às 10h. Emails de campanha: no máximo 1 por semana fora da campanha e 3 na semana forte. Automações sempre ligadas.",
  tipos="Newsletter \"Carta da Traços\": uma história da Sílvia, uma peça em destaque com preço, um cuidado ou uma dica de tamanho\nEmails de campanha: convite, abertura, última chamada (com datas reais)\nAutomação de boas-vindas: 2 emails (a história da marca; o guia de tamanhos)\nAutomação de pós-compra: os 5 emails do pós-campanha, enviados pela data de entrega",
  regras="Só para quem subscreveu\nNa newsletter nunca há códigos de desconto\nAssunto curto, sem emojis e sem maiúsculas a gritar\nAssinado pela Sílvia\nUm pedido por email\nFerramenta: [confirmar a plataforma do site]"),
 instagram=dict(nome="Traços por dentro", porque="Canal de transmissão para as seguidoras mais próximas: sabem primeiro, veem os bastidores e entram antes nas campanhas. É onde se cria a lista VIP sem pedir email.", cadencia="2 a 3 mensagens por semana. Em campanha, 1 por dia na semana forte.",
  tipos="Bastidores em foto ou vídeo curto (atelier, tecidos, embrulhos)\nÁudio da Sílvia (até 30 segundos)\nSondagem rápida (cor, tamanho, próxima peça)\nPrimeira a saber: peça nova ou campanha 1 hora antes do feed\nLink direto nas campanhas",
  regras="Nunca repetir o feed tal e qual\nUma mensagem, uma ideia\nNas campanhas o canal sabe sempre primeiro\nSem exclamações em série nem emojis a mais"),
 whatsapp=dict(nome="Lista VIP Traços (WhatsApp Business)", porque="Contacto pessoal da Sílvia com quem pediu para entrar. Serve para o acesso antecipado, ajuda com tamanhos e avisos de reposição. É o canal que mais vende, por isso é o que menos se usa.", cadencia="1 a 2 mensagens por mês fora de campanha. Na Black Friday, no máximo 3 (convite, acesso VIP, último dia).",
  tipos="Convite pessoal para a lista VIP\nAcesso antecipado com link\nAviso de tamanho ou reposição a quem perguntou\nResposta a dúvidas de tamanho, com foto e medidas",
  regras="Lista de transmissão, não grupo: ninguém vê o número das outras\nSó entra quem pediu (comentou VIP, respondeu ou preencheu o formulário)\nSó chega a quem tem o número da Traços guardado: pedir isso no convite\nSempre na primeira pessoa, assinado pela Sílvia\nSaída fácil: \"Se não quiseres receber, responde SAIR\""))
json.dump(com,open(O+"/comunicacao.json","w"),ensure_ascii=False)
W=[("2026-11-02","O inverno e o presente","Mostrar o Casaco Trilha, a camisa e as calças como o presente que fica. Sem falar de Black Friday."),
   ("2026-11-09","A infância não se apressa","A marca e a Sílvia: porquê, como se faz, como cuidar. O verão que guardámos aparece sem preço."),
   ("2026-11-16","Lista VIP","Abrir a lista: quem entra escolhe primeiro e recebe embrulho de Natal."),
   ("2026-11-23","Black Friday","Embrulho, acesso VIP a 26, abertura a 27 de novembro."),
   ("2026-11-30","Último dia e Natal","Fecho a 30 de novembro às 23h59. Depois, o Natal a preço de sempre."),
   ("2026-12-07","Presentes com significado","Ajudar quem oferece: por idade, por ocasião, para avós e madrinhas."),
   ("2026-12-14","Chega a tempo","A data limite real para chegar antes do Natal."),
   ("2026-12-21","Obrigada","As encomendas a sair e o agradecimento.")]
import datetime
for ini,t,obj in W:
  fim=(datetime.date.fromisoformat(ini)+datetime.timedelta(days=6)).isoformat()
  json.dump(dict(cliente=C,inicio=ini,fim=fim,titulo=t,objetivo=obj,oferta="",palavraChave="",estrategiaFeed="",estrategiaStories="",notas=""),open(f"{O}/semanas/{C}-{ini}.json","w"),ensure_ascii=False)
print("ok")
