# Entrega 10 — MoLIC

**Data:** 08/11/2026\
**Status:** 🟨 M01 e M02 propostos; revisão individual de Pedro e Lucas pendente; M03, de Giovanni, não iniciado\
**Responsabilidade:** 1 solução completa por integrante. Esta versão contém M01 e M02; a entrega da equipe só estará completa com M03 e com a revisão de cada autor.

## Objetivo da atividade

Modelar a interação como uma **conversa entre usuário e preposto do designer**, oferecendo visão global dos caminhos que permitem ao usuário atingir seus objetivos, incluindo alternativas e rupturas relevantes. MoLIC não deve ser reduzida a um fluxograma de telas.

Cada integrante modela **um objetivo grande**, com abertura e encerramento próprios, e detalha as cenas com tópico, diálogos e signos. Essas duas exigências estão no vídeo *Introdução ao MoLIC*, de Plínio Aquino (YouTube `c15Rr3Q-PKw`), em 03:37–04:07 e 17:37–18:08. As legendas consultadas são automáticas, em blocos de cerca de 30 s.

### Base da notação, autoria e limites

A notação segue os slides [CC8122-Molic-ParteA](../slides_plinio/CC8122-Molic-ParteA.pdf) e [CC8122-Molic-ParteB](../slides_plinio/CC8122-Molic-ParteB.pdf), baseados em Barbosa e Silva (2010), e os vídeos *Introdução ao MoLIC* (`c15Rr3Q-PKw`) e *Prática de Modelagem MoLIC* (`Bp0eQkL1Ub4`). Nas referências abaixo, A e B indicam a parte; o número indica o slide.

| Elemento | Representação nos diagramas | Fonte |
|---|---|---|
| Abertura | Círculo preto preenchido, seguido da fala do usuário que inicia a conversa | A9; B3, caso (a) |
| Encerramento | Círculo preto com anel externo | A9 e A10 |
| Cena | Retângulo arredondado com o tópico no cabeçalho e diálogos no corpo: `nome do diálogo { d: … }` | A8 e A14; detalhamento exigido no vídeo, 17:37 |
| Processo do sistema | Quadrado preto. Entra por fala `u:` e sai por falas `d:` | A11; *Prática*, 06:11 |
| Fala de transição | Seta contínua com `u:` ou `d:`; `precond:` indica condição para a fala existir | A6 e B5 |
| Ruptura ou recuperação | Seta tracejada | A11–A13; vídeo, 25:19 e 30:26; *Prática*, 15:40 |
| Diálogo `d+u:` | Preposto apresenta e usuário informa ou escolhe. Pode apoiar prevenção ativa, conforme o vídeo, 39:22 | A8 e A14 |

**Notação não utilizada.** As marcas `[SR]`, `[SP]` e `[TA]` aparecem em A15, B4 e B5, mas nenhum slide ou legenda consultada as define; os mecanismos de prevenção e recuperação são indicados nas tabelas com as siglas PP, PA, AL, RA e CE da [Entrega 9](09_modelo_conceitual.md#convenções-e-relações). `gco`/`gcc` são opcionais segundo o vídeo, 45:39, e não foram usados. Não há acesso ubíquo: nenhum tópico destes objetivos precisa estar disponível a partir de qualquer cena. Não há cena de alerta: incluir, retirar e baixar são reversíveis ou repetíveis, sem consequência que exija confirmação.

**Identificadores.** Em cada diagrama, `a` é abertura, `c` é cena, `p` é processo, `e` é encerramento e `f` é fala de transição. Eles valem dentro do próprio MoLIC: M01·c1 e M02·c1 são cenas diferentes. Cada diagrama se lê sozinho, sem depender de cena ou fala do outro. Objetivos O00–O10 e signos S01–S34 são os da [Entrega 9](09_modelo_conceitual.md). Notas em itálico marrom nos diagramas descrevem atividades fora do sistema e não pertencem à notação.

**Proposta e demonstração.** Os diagramas descrevem a interação proposta. O [protótipo atual](../assets/06_prototipos/PROTOTIPO_fluxo_highlights.html), publicado em <https://ihc.p4cs.com.br>, usa quatro tempos de exemplo de duas partidas, oito cortes MP4 e análise simulada; não aceita arquivos próprios nem executa o detector. Diferenças entre o modelo e a demonstração estão em [Preparação para prototipagem](#preparação-para-prototipagem).

**Autoria.** Os autores de referência são os donos dos recortes CI01/T01 e CI02/T02 da Entrega 9. Esta proposta foi redigida com assistência de IA (Claude Code), a pedido da equipe. Pedro e Lucas ainda não revisaram nem apresentaram seus modelos, e nenhuma sessão com usuários os validou.

## O que este MoLIC modela

O MoLIC não modela o detector por dentro. Ele modela a conversa necessária para usar a contribuição: consultar candidatos com limites conhecidos, conferir o contexto de um corte, decidir a seleção e obter CSV e MP4. Ajustar cortes, montar, publicar, transferir material e decidir a publicação continuam fora do sistema; aparecem como encerramentos com nota, não como cenas. Autenticação, administração, histórico persistente, parâmetros de IA, reconhecimento automático de atletas, aprovação editorial e garantia de arquivo salvo não fazem parte dos modelos.

## M01 — Revisar candidatos e obter o material da partida

**Autor(a) de referência:** Pedro Alexandre Custódio Silva — 22.123.049-3. Proposta assistida por IA; revisão do autor pendente.\
**Cenário de interação de origem:** [CI01](09_modelo_conceitual.md#ci01--revisar-e-obter-candidatos-com-contexto-sob-pressão-de-prazo)\
**Objetivo(s):** O04, O05, O06 e O07, com O08 na retomada. O02 é precondição; O01–O03 ficam fora deste modelo. O10 é saída externa.\
**Tarefa(s) relacionada(s):** [T01](05_analise_tarefas.md#hta--t01-localizar-selecionar-e-revisar-lances-de-melhores-momentos), A04; continuidade em T02.\
**Signos relevantes:** S01–S03, S12, S16–S29, S32–S34; S30 aparece só nas notas externas.

### Diagrama

![MoLIC M01: revisar candidatos e obter o material da partida](../assets/10_molic/molic_m01.svg)

**Fonte editável:** [molic_m01.svg](../assets/10_molic/molic_m01.svg), SVG em texto com um grupo por elemento, editável em editor de texto ou vetorial.

### Leitura do diagrama

| ID | Tópico ou função | Objetivo |
|---|---|---|
| c1 | Localizar candidatos: alcance dos resultados, critérios, lista e contexto preservado | O04, O08 |
| c2 | Conferir pertinência e contexto de um candidato e decidir sua inclusão | O05, O06 |
| c3 | Conferir a seleção, os tamanhos e as saídas | O06, O07 |
| p1 | Responder a uma consulta por critérios | O04 |
| p2 | Carregar o corte para reprodução | O05 |
| p3 | Disponibilizar um MP4 | O07 |
| p4 | Gerar o CSV da seleção | O07 |

#### Caminho principal

1. `a1 → f1 → c1`: com resultados acessíveis, Rafael inicia a revisão. c1 informa partida, tempo, disponibilidade e limites S12 e, se identificável, a tentativa S32.
2. `c1 → f3 → p1 → f4 → c1`: restringe a consulta por partida, tempo ou tipo S22; recebe os candidatos correspondentes, com a seleção mantida.
3. `c1 → f6 → c2`: examina um candidato pela origem S01–S03 e pelas referências S17–S21.
4. `c2 → f8 → p2 → f9 → c2`: reproduz o corte, julga construção e desfecho e inclui o candidato na seleção S23, no diálogo `d+u`.
5. `c2 → f7 → c1`: volta aos candidatos e repete os passos 3 e 4 enquanto houver prazo.
6. `c1 → f14 → c3`: confere a seleção, a quantidade S24, a duração somada S25 e os tamanhos S33/S34.
7. `c3 → f18 → p4 → f19 → c3`: com seleção não vazia, baixa o CSV com metadados e endereços, sem vídeos.
8. `c3 → f16 → c2 → f11 → p3 → f12 → c2`: baixa o MP4 de cada item necessário e volta por `c2 → f17 → c3`.
9. `c3 → f20 → e1`: encerra. Fora do sistema, abre o CSV, reproduz os MP4 salvos, copia ao servidor e avisa Arnaldo; pendências S30 continuam com ele.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Caminho de recuperação/saída |
|---|---|---|---|
| Consulta sem candidatos | `c1 → f3 → p1 → f5 → c1` | d: nenhum candidato com estes critérios; S24 mostra que a seleção continua | Revê ou limpa os critérios S22 em c1. RA |
| Nenhum candidato acessível ou útil | c1 | S12 informa ausência de candidatos ou limites conhecidos. Lista vazia não prova ausência de lances | `c1 → f21 → e2`: interrompe a revisão, mesmo sem seleção; a busca no original (O10) fica pendente fora do sistema. CE |
| Contexto insuficiente | c2 | Pela reprodução e por S20/S21, Rafael julga que o corte começa tarde ou corta o desfecho | Retira ou não inclui o candidato (`d+u` S23) e segue por `c2 → f7 → c1`. Se precisar do lance, interrompe por `c1 → f21 → e2` para ajustar no original. O sistema não edita limites |
| Suspeita de omissão | c1; de c2, volta antes por f7 | O lance esperado não aparece; S01, S02, S18 e S19 delimitam onde procurar | Interrompe por `c1 → f21 → e2` para conferir a gravação (O10). A cobertura completa não é afirmada; a dúvida fica como pendência S30 |
| Pergunta de Arnaldo sobre outra partida | c1 ou c2, sem encerrar a conversa | Rafael muda de assunto dentro da revisão: de c2 volta por `c2 → f7 → c1` e consulta a outra partida por `c1 → f3 → p1 → f4 → c1`. S24 mostra que a seleção S23 continua | Aplica de novo os critérios anteriores por `c1 → f3 → p1 → f4 → c1` e segue. Não há encerramento nem nova abertura |
| Interrupção e retomada | c1, por `c1 → f21 → e2`; mais tarde, `a2 → f2 → c1` | e2 encerra a conversa de revisão, não necessariamente a aplicação nem a sessão. Ao reabrir por a2, S29 e S24 mostram o que a sessão preservou, se algo foi preservado | O estado anterior não é garantido. Se a seleção se perdeu, por exemplo após recarga, reconstrói pelos critérios e por `c1 → f6 → c2`. Não há recuperação automática |
| Corte não carrega | `c2 → f8 → p2 → f10 → c2` | d: corte não pôde ser carregado; tentar de novo | Repete f8. Se persistir, decide sem reprodução ou mantém a pendência; o MP4 continua sujeito a `precond` próprio |
| MP4 indisponível ou falha na obtenção | `c2 → f11 → p3 → f13 → c2` | A `precond` de f11 impede pedir mídia sabidamente indisponível (PA, S27). Se a disponibilização falhar, d: falha na obtenção (S28) | Repete f11 ou mantém o item pendente. RA quando houver nova tentativa; CE quando o problema estiver fora do sistema |
| Arquivo salvo não abre ou não aparece | Após f12 ou f19, fora do sistema | O sistema informa disponibilização, não salvamento local (S28); Rafael confere o arquivo | Repete f11 ou f18 enquanto o item estiver acessível; senão verifica destino e espaço por conta própria. CE |
| Seleção esvaziada | c3, diálogo `retirar item` | S24 fica 0; a `precond` de f18 deixa de valer e o CSV não é oferecido. MP4 continua obtenível sem seleção (S27) | Volta por `c3 → f15 → c1 → f6 → c2` para incluir de novo ou baixar MP4 individuais; ou encerra por f20 sem CSV |
| Tamanho indisponível ou total incompleto | c3, diálogo `planejar obtenção` | S33 aparece como conhecido, estimado ou indisponível; S34 não é apresentado como total se faltar algum tamanho e não inclui o CSV | Rafael confere o espaço por meios próprios e obtém item a item. PP |

## M02 — Obter material identificável para a supervisão editorial externa

**Autor(a) de referência:** Lucas Roberto Boccia dos Santos — 22.123.012-1. Proposta assistida por IA; revisão do autor pendente.\
**Cenário de interação de origem:** [CI02](09_modelo_conceitual.md#ci02--obter-material-identificável-para-a-supervisão-editorial-externa)\
**Objetivo(s):** O06 e O07, conduzidos pelo editor, e O04 restrito a localizar item faltante. O09 e O10 são externos. Resultados acessíveis (O02) são precondição.\
**Tarefa(s) relacionada(s):** [T02](05_analise_tarefas.md#hta--t02-supervisionar-processo-editorial) como continuidade externa; obtenção em T01/A04.\
**Signos relevantes:** S01–S03, S16–S29, S31, S33 e S34.

Quem conversa com o sistema é o editor, Rafael no CI02. Arnaldo, P02, recebe os arquivos e decide fora do sistema, como a Entrega 9 já registra nas conversas marcadas como externas. Por isso não há cena de aprovação. A seleção costuma chegar pronta da revisão de M01, mas M02 não depende disso: no próprio modelo, a cena c3 localiza um item que falta ou que o supervisor pediu, e a cena c2 permite incluí-lo.

### Diagrama

![MoLIC M02: obter material identificável para a supervisão editorial externa](../assets/10_molic/molic_m02.svg)

**Fonte editável:** [molic_m02.svg](../assets/10_molic/molic_m02.svg), SVG em texto com um grupo por elemento, editável em editor de texto ou vetorial.

### Leitura do diagrama

| ID | Tópico ou função | Objetivo |
|---|---|---|
| c1 | Preparar material para a supervisão: identificação da seleção, retirada de item, saídas, tamanhos e limites | O06, O07 |
| c2 | Conferir identificação e referências temporais de um corte, decidir se ele segue na seleção e obter seu MP4 | O06, O07 |
| c3 | Localizar por critérios um item que falta ou que o supervisor pediu, sem perder a seleção | O04, O06 |
| p1 | Carregar o corte para reprodução | O06 |
| p2 | Disponibilizar um MP4 | O07 |
| p3 | Gerar o CSV da seleção | O07 |
| p4 | Responder a uma consulta por critérios | O04 |

#### Caminho principal

1. `a1 → f1 → c1`: com resultados acessíveis e a seleção já montada, o editor confere a identificação de cada item: id S16, partida S01, tempo S02, tipo S17, relógio S18 e intervalo S20, além de S24 e S25.
2. `c1 → f3 → c2`: abre um corte e confere vídeo de origem S03, instante no arquivo S19 e duração S21. Se quiser revê-lo, usa `c2 → f5 → p1 → f6 → c2`.
3. `c2 → f8 → p2 → f9 → c2`: baixa o MP4 e volta por `c2 → f4 → c1`; repete os passos 2 e 3 para cada corte necessário.
4. `c1 → f11 → p3 → f12 → c1`: baixa o CSV, que leva as mesmas referências dos cortes.
5. `c1 → f19 → e1`: encerra. Fora do sistema, confere os arquivos salvos, transfere-os e avisa Arnaldo pelo chat. A decisão S31 ocorre em O09.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Caminho de recuperação/saída |
|---|---|---|---|
| Seleção vazia, incompleta ou não preservada | c1 | S24 fica 0 ou falta um corte; S29 informa que a seleção vale só nesta sessão; a `precond` de f11 impede o CSV vazio. PA | Localiza o item por `c1 → f13 → c3 → f14 → p4 → f15 → c3 → f17 → c2`, inclui-o em `decidir inclusão` (`d+u` S23) e volta por `c2 → f4 → c1`. O CSV passa a ser oferecido: `c1 → f11 → p3 → f12 → c1`. RA |
| Pedido de item fora da seleção | Depois de e1; o editor volta por `a2 → f2 → c1` | O item pedido por Arnaldo não aparece em c1 | Mesmo caminho da linha anterior. Se Arnaldo pediu só o vídeo, não é preciso incluir: `c1 → f13 → c3 → f17 → c2 → f8 → p2 → f9 → c2` |
| Consulta sem candidatos | `c3 → f14 → p4 → f16 → c3` | d: nenhum candidato com estes critérios; S24 mostra que a seleção continua | Revê os critérios em c3. Se o item não aparece, volta por `c3 → f18 → c1` e encerra por `c1 → f20 → e2`; a conferência do original (O10) fica pendente fora do sistema. RA; CE |
| Item que não deve seguir | c1, diálogo `retirar item`, ou c2, diálogo `decidir inclusão` | S24 diminui. Se chega a 0, a `precond` de f11 deixa de valer e o CSV não é oferecido | O MP4 continua obtenível sem seleção (S27), por `c1 → f13 → c3 → f17 → c2 → f8 → p2 → f9 → c2`. Para voltar a oferecer o CSV, inclui um item pelo caminho da seleção vazia |
| Referência insuficiente para o supervisor | Fora do sistema; volta por `a2 → f2 → c1` | Arnaldo pede identificação; o editor confere S16, S01, S02 e S18–S20 em c1 e c2. Dado ausente aparece como indisponível, sem ser inventado | Gera o CSV de novo por `c1 → f11 → p3 → f12 → c1` e responde pelo canal externo |
| Arquivo recebido não abre | Fora do sistema; volta por `a2 → f2 → c1` | Arnaldo avisa pelo chat | Baixa de novo por `c2 → f8 → p2 → f9 → c2` e confere antes de reenviar. Se f10 se repetir, mantém a pendência. CE |
| Corte não carrega | `c2 → f5 → p1 → f7 → c2` | d: corte não pôde ser carregado; tentar de novo | Repete f5; a identificação em c2 continua disponível |
| MP4 indisponível ou falha na obtenção | `c2 → f8 → p2 → f10 → c2` | A `precond` de f8 impede pedir mídia sabidamente indisponível; d: falha na obtenção (S28) | Repete f8 ou registra a pendência fora do sistema |
| Tamanho indisponível ou total incompleto | c1, diálogo `planejar obtenção` | S33 por item; S34 só como total se todos forem conhecidos; não comprova espaço livre | Confere o espaço antes de baixar item a item. PP |
| Corte sem o contexto necessário, como o gol sem a falta anterior | O09/O10, fora do sistema | Arnaldo julga o corte insuficiente | Ajuste no original fora do sistema; o trecho corrigido circula pelo canal externo e não volta ao sistema. Se o prazo terminar, `c1 → f20 → e2` |
| Seleção não conferida no prazo | c1 | O editor reconhece itens sem conferência | `c1 → f20 → e2`, com pendência explícita; nenhuma aprovação é registrada |

## Checklist específico de modelagem

- [x] Existe **ponto de abertura** coerente com o início do objetivo: M01 a1, com `precond` O02, e a2 para retomada; M02 a1, com resultados acessíveis, e a2 para pedido do supervisor.
- [x] As **cenas de conversa** representam tópicos da Entrega 9, não páginas: os títulos vêm das tabelas de conversa de CI01 e CI02.
- [x] As transições deixam claro quem fala: o script de conferência exige `u:` em toda fala que sai de cena ou abertura e `d:` em toda saída de processo.
- [x] Há **pontos de encerramento** para material obtido (e1) e para interrupção ou pendência (e2) nos dois modelos.
- [x] Processos não recebem `d:` nem emitem `u:`: M01 p1–p4 e M02 p1–p4, conferidos pelo script.
- [x] Rupturas têm feedback e caminho de volta: M01 f5, f10 e f13; M02 f7, f10 e f16. Pendências sem solução no sistema saem por e2 com nota.
- [x] Cada modelo se lê sozinho. M02 localiza itens em c3 e permite incluí-los em c2. O script confere em cada SVG os caminhos de seleção vazia até o CSV, MP4 sem seleção e falha seguida de nova tentativa ou saída.
- [x] Acessos ubíquos não foram usados, pela justificativa em [Base da notação](#base-da-notação-autoria-e-limites).
- [x] O diagrama cobre consulta vazia, contexto insuficiente, omissão, seleção vazia, item faltante, mídia indisponível, tamanho desconhecido e retomada.
- [x] Nomes e IDs de objetivos e signos existem na Entrega 9, conferidos pelo script.
- [x] O diagrama é legível em largura reduzida: renderização local no Chromium a 880 px, com texto de cerca de 12 px. A página do GitHub não foi aberta nesta verificação.
- [x] O MoLIC representa a conversa usuário–sistema, não o detector nem a sequência de telas.
- [x] Filtros e obtenção têm retornos e rupturas.
- [ ] Pedro e Lucas revisaram e apresentaram seus modelos.
- [ ] M03, de Giovanni, foi elaborado.

## Consolidação da equipe

Esta consolidação cobre só M01 e M02. Não registra conclusão da equipe.

### Cobertura dos objetivos

| Objetivo | MoLIC que cobre | Lacunas/duplicidades | Decisão |
|---|---|---|---|
| O00 | M01 e M02, em parte | Preparação e acompanhamento da análise ficam fora | Propósito global; benefício a validar |
| O01 | — | Envio e conferência das gravações | Precondição dos dois modelos; previsto para M03, CI03/T03, pendente |
| O02 | — | Acompanhamento da análise | Precondição de M01 f1 e de M02 f1; acompanhamento previsto para M03 |
| O03 | — | Falha da análise | Previsto para M03 |
| O04 | M01 c1 e p1; M02 c3 e p4 | Sobreposição legítima e restrita: M02 localiza um item que falta ou foi pedido, sem revisar pertinência (O05) | M02·c3 repete os diálogos de consulta de M01·c1 (A4), para que M02 se leia sozinho |
| O05 | M01 c2 e p2 | M02·c2 confere identificação, não pertinência editorial | Sem duplicação |
| O06 | M01 c2 e c3; M02 c1, c2 e c3 | Sobreposição legítima: M01 define a seleção; M02 a confere, completa ou corrige para encaminhar | Cenas análogas mantêm os mesmos diálogos, para consistência entre caminhos semelhantes (A4) |
| O07 | M01 c2, c3, p3 e p4; M02 c1, c2, p2 e p3 | Sobreposição legítima: a mesma obtenção encerra objetivos diferentes | M01 termina em material para a edição; M02, em material identificável para a supervisão e no retorno por a2 |
| O08 | M01 a2 e c1; M02 a2 e c1, via S29 | Retomada limitada à sessão | Não se modela histórico persistente |
| O09 | — | Decisão editorial de Arnaldo | Fora do sistema; nota em M02·e1 |
| O10 | — | Conferência do original e ajuste | Fora do sistema; notas em M01·e2 e M02·e2 |

### Preparação para prototipagem

O protótipo continua sendo o HTML/JS da Entrega 6. Figma é opcional e não foi usado. A tabela compara o que os modelos pedem com o que a demonstração faz hoje, conforme a leitura do código em `assets/06_prototipos/PROTOTIPO_fluxo_highlights.html` e a verificação no site descrita depois da tabela. A coluna da direita lista propostas, não funcionalidades implementadas.

| Estado ou feedback | Origem no MoLIC | Protótipo atual | Proposta para a próxima versão |
|---|---|---|---|
| Resultados acessíveis e seus limites | M01 a1 e c1, S12/S32 | Tela 4, “Base de highlights”, mostra a contagem de lances e partidas. Abrir a Tela 4 durante a simulação conclui o restante na hora, com aviso | Informar limites conhecidos e a tentativa, quando houver, sem afirmar cobertura |
| Critérios e consulta vazia | M01 f3–f5; M02 f14–f16 | Variante A filtra por tipo, tempo e busca textual em título, partida, times e arquivo e mostra “Nenhum lance encontrado” com “Limpar busca e filtros”. Variante B filtra só por tipo e mostra “0 lances” sem orientação. Variante C não filtra | Mesma mensagem de consulta vazia nas variantes, dizendo que a seleção foi mantida. A busca textual não é reconhecimento de atleta |
| Detalhe do candidato | M01 c2; M02 c2 | Partida, data, tempo, relógio do jogo, início, fim e duração no arquivo e instante da anotação no corte | Mostrar o id S16 que vai no CSV, para a conversa com o supervisor |
| Reprodução e falha | M01 p2; M02 p1 | “Carregando corte (x MB)…” e “Não deu para carregar (…). Tentar de novo” | Manter |
| Inclusão e retirada | M01 c2 e c3; M02 c1 e c2 | “+ Incluir” e “✓ No CSV”; marcação nas três variantes; o mesmo botão retira o item | Manter |
| Revisão da seleção | M01 c3; M02 c1 | Não há lista própria; a seleção aparece como marcação nos itens e como contagem em “Baixar CSV (n)” | Lista da seleção com S24, S25, S33 e S34 e retirada de item |
| Tamanhos | M01 c3; M02 c1 | Tamanho de cada MP4 no link “Baixar MP4 (x MB)”, vindo do manifesto; não há soma S34 nem duração somada S25 | Mostrar S34 como conhecido, estimado ou indisponível |
| CSV | M01 f18 e f19; M02 f11 e f12 | Botão desativado com seleção vazia; aviso de que o CSV lista os cortes com o link de cada MP4 | Manter; lembrar que o salvamento é conferido pela pessoa |
| MP4 | M01 f11–f13; M02 f8–f10 | Link de download direto no detalhe, disponível também sem seleção e sem resposta da aplicação. O arquivo salvo leva o nome do arquivo no servidor, como `suarez.mp4`, sem partida nem tempo | Comunicar a disponibilização (S28) e falhas detectáveis. Avaliar nome de arquivo identificável para M02 |
| Retomada | M01 a2 e c1; M02 a2 e c1, S29 | A seleção se mantém ao trocar de variante e de tela na mesma aba. Ela fica só na memória da página: num carregamento novo, a seleção se perde sem aviso e a demonstração volta à tela de entrada, com exemplos e análise a carregar de novo. Pelo código, carregar os exemplos de novo também esvazia a seleção | Informar o alcance da preservação; não prometer persistência |
| Encerramento e pendências | M01 e1 e e2; M02 e1 e e2 | Sem suporte, como previsto: pendências, transferência e decisão ficam fora | Nenhuma tela de aprovação, histórico ou registro de pendências |

**Verificação no site publicado.** Em 08/11/2026, duas revisões assistidas por IA, independentes da redação, usaram <https://ihc.p4cs.com.br> e confirmaram a coluna “Protótipo atual” nos fluxos principais: exemplos e análise simulada, filtros e consulta vazia nas variantes, detalhe, inclusão e retirada, seleção mantida ao trocar de variante e de tela, reprodução do corte, CSV com id, partida, arquivo de origem, tempos e endereço do MP4, CSV desativado com seleção vazia e MP4 disponível sem seleção. A perda da seleção foi observada ao abrir de novo o endereço dos resultados num carregamento novo; a recarga por F5 não foi testada. Os estados “Carregando corte…”, a falha de carregamento e a falha do MP4 não foram provocados, e essas linhas vêm só da leitura do código. Pedro e Lucas ainda não revisaram seus modelos, e nenhum usuário os validou.

## Erros frequentes a evitar

- desenhar apenas caixas com nomes de telas e setas de navegação;
- não modelar falhas, cancelamento, volta ou recuperação;
- usar rótulos genéricos (“Tela 1”, “Processo 2”) sem tópico de conversa;
- criar no protótipo fluxos que não existem no MoLIC;
- diagrama sem legenda/fonte editável e com texto ilegível.

## Histórico de revisões

| Data | Alteração | Responsabilidade |
|---|---|---|
| 08/11/2026 | Proposta de M01 e M02, legenda com fontes, leitura dos caminhos, consolidação parcial e preparação para o protótipo HTML/JS. Sem nova coleta, sessão com usuários ou mudança no protótipo | Elaboração assistida por IA (Claude Code) a pedido da equipe; revisão de Pedro e Lucas pendente; M03 pendente |
| 08/11/2026 | Correções após revisão independente: M02 localiza itens na própria cena c3 e permite incluí-los em c2, em vez de remeter a uma cena de M01; M01 separa troca de assunto de interrupção e retomada e usa uma só fala de interrupção (f21); retirada de item em M02; recarga do protótipo descrita como observada; verificação no site registrada | Elaboração assistida por IA (Claude Code); revisão de Pedro e Lucas pendente |
