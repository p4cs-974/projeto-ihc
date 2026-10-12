# Entrega 5 — Análise de tarefas: HTA, GOMS e CTT

**Data:** 07/10/2026  
**Revisão de T02:** 09/10/2026, adequação aos modelos dos slides do professor\
**Status:** 🟨 em andamento; tarefa T02 (Lucas) concluída nas três técnicas (HTA, GOMS e CTT); tarefas T01 (Pedro) e T03 (Giovanni) aguardam elaboração por seus respectivos autores  
**Responsabilidade:** cada integrante modela pelo menos 1 HTA, 1 GOMS e 1 CTT. As três técnicas abordam a tarefa prioritária de cada membro da equipe, garantindo a cobertura dos três perfis identificados nas entregas anteriores.

---

## Objetivo da atividade

Modelar tarefas importantes sob perspectivas complementares: decomposição hierárquica de objetivos e planos ([HTA — Hierarchical Task Analysis](#hta--t02-supervisionar-processo-editorial)), estrutura cognitiva de metas, operadores, métodos e regras de seleção ([GOMS](#goms--t02-supervisionar-processo-editorial)) e relações temporais e lógicas entre tarefas de usuário, sistema e interação ([CTT — ConcurTaskTrees](#ctt--t02-supervisionar-processo-editorial)). Os diagramas são acompanhados de fundamentação conceitual, interpretação textual e rastreabilidade direta com os artefatos anteriores do projeto.

---

## Para projetos cujo TCC não previa interface

Em conformidade com as diretrizes da disciplina, a modelagem foca nas **tarefas humanas relacionadas ao uso da contribuição técnica**, e não no processamento algorítmico interno dos modelos de visão computacional.

O tema do TCC (*Identificação de Melhores Momentos em Partidas de Futebol Utilizando Sistemas Híbridos de Visão Computacional*, [Entrega 1, seção 0.2](01_conhecendo_o_problema.md#02-qual-é-o-tema-do-trabalho)) tem como saída computacional a detecção automatizada de eventos esportivos e a geração de cortes acompanhados de metadados ([RASTREABILIDADE.md, seção 1](../RASTREABILIDADE.md#1-derivação-do-escopo-de-ihc-a-partir-do-tcc)). As tarefas humanas analisadas descrevem:

- como o editor de vídeo esportivo submete vídeos brutos, gerencia a fila e revisa a pertinência dos trechos candidatos antes de baixá-los (T01);
- como o supervisor editorial / editor-chefe recebe, inspeciona e chancela esses resultados para publicação nas redes sociais da emissora, validando o contexto temporal dos lances capitais sob forte pressão de prazo (T02);
- como o criador amador decupa e compila lances específicos por jogador em estações de capacidade restrita (T03).

A análise não modela funções internas da rede neural ou etapas do pipeline de inferência, mas a **tomada de decisão, a inspeção de contexto, o fluxo de aprovação e o tratamento de contingências humanas**.

---

## Seleção das tarefas

A tabela abaixo consolida as tarefas prioritárias identificadas a partir dos cenários de problema ([Entrega 4](04_cenarios_problema.md)) e das necessidades registradas na matriz de rastreabilidade ([RASTREABILIDADE.md, seção 3](../RASTREABILIDADE.md#3-rastreabilidade-entre-contribuição-técnica-necessidades-e-artefatos)):

| ID | Tarefa | Persona / cenário de origem | Frequência / criticidade | Autor responsável | Status na entrega |
|---|---|---|---|---|---|
| **T01** | Localizar, selecionar e revisar lances de melhores momentos | [P01, Rafael](03_personas_contexto_jornada.md#persona-p01--rafael) / [C01](04_cenarios_problema.md#cenário-c01--seleção-manual-de-melhores-momentos-sob-pressão-de-prazo) | Alta frequência diária; alta criticidade (omissões involuntárias geram retrabalho na pós-produção) | Pedro Custódio — 22.123.016-2 | ⬜ Aguarda autor |
| **T02** | Supervisionar processo editorial e chancelar cortes esportivos | [P02, Arnaldo](03_personas_contexto_jornada.md#persona-p02--arnaldo) / [C02](04_cenarios_problema.md#cenário-c02--controle-do-processo-editorial-engessado) | Alta frequência em dias de rodada; altíssima criticidade editorial (portão final de controle antes do ar; risco de dano à reputação da emissora) | Lucas Roberto Boccia dos Santos — 22.123.012-1 | 🟩 Concluída (HTA, GOMS e CTT) |
| **T03** | Decupar e compilar lances por jogador sob restrições de hardware | [P03, Jorginho Jr.](03_personas_contexto_jornada.md#persona-p03--jorginho-jr) / [C03](04_cenarios_problema.md#cenário-c03--decupagem-manual-de-lances-por-jogador-sob-restrições-de-hardware) | Frequência média a alta semanal; média criticidade (dependência de processamento em nuvem) | Giovanni Chahin Morassi — 22.123.025-3 | ⬜ Aguarda autor |

### Justificativa da prioridade de T02 (Supervisão Editorial)

[H] A tarefa **T02 — Supervisionar processo editorial e chancelar cortes esportivos**, de Lucas Roberto, foi escolhida porque Arnaldo Rocha (P02) precisa decidir se o material recebido preserva a intenção editorial e o contexto dos lances sob pressão de prazo. O [cenário C02](04_cenarios_problema.md#cenário-c02--controle-do-processo-editorial-engessado) descreve a dificuldade de atender vários editores, o risco de aprovar cortes sem conferência suficiente e uma contingência de despublicação. São situações hipotéticas, derivadas de H10, H14, H22, H23 e H33, a investigar com profissionais.

**Recorte comum aos três modelos:** uso proposto dos cortes e metadados **fora da interface do produto**, após a revisão e o download pelo editor (A04). Arnaldo consulta os arquivos em sua estação ou ao lado do editor e comunica a decisão por canal externo. A pasta compartilhada e o chat são escolhas hipotéticas da jornada de P02 e de H40; a inspeção presencial é uma alternativa descrita em C02. A contingência retoma esse cenário como exceção ao uso proposto. Não se modela uma tela própria de aprovação, auditoria ou publicação no produto. H35 continua exploratória.

**Base e limites:** P02 é uma proto-persona, e os modelos não resultam de observação empírica. Critérios editoriais, canais, volume de partidas, duração do contexto temporal e benefício esperado precisam de validação na Entrega 7. O índice automático não comprova que todos os lances relevantes foram encontrados; uma suspeita de omissão exige conferência com o editor e, se necessário, com a gravação original.

**Referência de notação:** [CC8122-HTA](../slides_plinio/CC8122-HTA.pdf), slides 4–8 (objetivos, operações, planos e tabela detalhada), e [CC8122-GOMS-CTT](../slides_plinio/CC8122-GOMS-CTT.pdf), slides 3–13 (hierarquia GOMS) e 19–24 (tipos de tarefas e relações CTT). Os modelos abaixo foram adequados a esses exemplos somente para P02/T02.

---

## HTA — T02: Supervisionar processo editorial

**Autor(a):** Lucas Roberto Boccia dos Santos — 22.123.012-1\
**Persona relacionada:** [P02, Arnaldo Rocha](03_personas_contexto_jornada.md#persona-p02--arnaldo), editor-chefe, persona atendida\
**Cenário de origem:** [C02 — Controle do Processo Editorial Engessado](04_cenarios_problema.md#cenário-c02--controle-do-processo-editorial-engessado)\
**Rastreabilidade:** [R03](../RASTREABILIDADE.md#3-rastreabilidade-entre-contribuição-técnica-necessidades-e-artefatos); H10, H14, H16, H22, H23, H25, H33, H34, H35 e H40. H41 trata das interrupções do editor e não comprova uma rotina de retomada de Arnaldo.

### Descrição da tarefa

- **Objetivo central [H]:** avaliar a seleção recebida, preservar contexto e pertinência editorial e orientar sua continuidade para montagem externa ou revisão.
- **Entrada [H]:** lote de cortes e metadados identificado por partida, aviso do editor e prioridades da rodada. Um pedido presencial de ajuda pode iniciar a inspeção na ilha de edição.
- **Resultado [H]:** decisão comunicada ao editor, identificando o lote aprovado para montagem ou os ajustes necessários. Devolução é um resultado daquele ciclo, mas a chancela fica pendente até a versão corrigida ser conferida.
- **Exceção [H]:** alerta de publicação com falha de contexto; Arnaldo solicita retirada à equipe responsável, orienta correção e reavalia a nova versão. A remoção e a postagem são realizadas fora do produto.

### Diagrama HTA

![HTA T02 — objetivos, operações e planos de Arnaldo](../assets/05_tarefas/hta_t02.svg)

*Figura 1 — HTA de T02, por Lucas Roberto. A visão geral e os detalhamentos dos ramos 1–4 compõem a mesma hierarquia. [SVG editável](../assets/05_tarefas/hta_t02.svg).*

Como nos slides 5 e 6 de **CC8122-HTA**, retângulos representam objetivos e um traço abaixo do retângulo identifica **operações**, onde a decomposição termina. Os planos ficam nos objetivos decompostos. `>` indica sequência, `/` indica seleção segundo uma condição e `+` indicaria paralelismo. Não foi presumida execução simultânea por Arnaldo; vários editores trabalhando em paralelo não obrigam a usar `+` na sua tarefa. Nos planos, usam-se os IDs completos para evitar ambiguidade entre ramos.

### Decomposição e planos

A tabela segue o modelo do slide 8: **Objetivos/Operações** e **Problemas e Recomendações**, com entrada (*Input*), ação, avaliação do resultado (*Feedback*) e plano quando pertinente. Recomendações são propostas a investigar, não funcionalidades automaticamente incluídas.

| Objetivos / Operações | Problemas e Recomendações |
|---|---|
| **0. Supervisionar processo editorial e chancelar cortes** | **Input:** prioridades da rodada, lotes recebidos e eventuais alertas externos. **Plano 0:** `1 > 2 > 3` para cada lote. Se 3.2 for escolhido, aguardar nova versão e repetir `2 > 3`. Encerrar quando os lotes recebidos estiverem encaminhados ou ao fim do turno, deixando explícitas as pendências. Em caso de falha editorial publicada, interromper o ciclo e executar 4; os demais lotes permanecem pendentes e exigem um novo ciclo. **Feedback:** editor informado sobre a seleção aprovada ou sobre a revisão necessária. **Problema:** aprovações apressadas e material difícil de identificar, C02/H33. **Recomendação:** preservar identificação e contexto nos resultados baixados, RC05/RC09. |
| **1. Identificar e priorizar lote recebido** | **Plano 1:** `1.1 > 1.2 > 1.3`; se nenhum lote estiver disponível, aguardar a entrega. **Feedback:** partida, material e prioridade definidos. **Problema:** chamados simultâneos dificultam ordenar o atendimento, C02. **Recomendação:** investigar como o editor comunica andamento e entrega, H40. |
| 1.1. Consultar prioridades e prazos da rodada | **Input:** pauta e anotações externas. **Ação:** conferir prioridades combinadas com os editores. **Feedback:** critérios de atendimento recuperados. |
| 1.2. Consultar aviso e identificar lote da partida | **Input:** aviso no chat e arquivos na pasta compartilhada, H40. **Ação:** conferir partida de origem e lote recebido. **Problema:** arquivos misturados ou sem identificação, H25/H33. **Recomendação:** nomes e metadados legíveis fora da interface, RC05/RC09. |
| 1.3. Escolher lote prioritário | **Ação:** escolher o próximo lote considerando prazo, pauta e dúvidas sinalizadas. **Feedback:** lote a inspecionar definido. **Problema:** prioridade e quantidade de atendimentos ainda não validadas. |
| **2. Inspecionar seleção e contexto dos cortes** | **Plano 2:** `2.1 > 2.2 > 2.3`; em 2.2, assistir aos cortes da seleção e rever os trechos duvidosos. Se dados ou contexto forem insuficientes, apontar a pendência em 3.2. **Feedback:** avaliação do lote e eventuais lacunas identificadas. |
| 2.1. Conferir identificação e timecodes | **Input:** metadados disponíveis: partida, timecodes e tipo de lance. **Ação:** relacionar cada corte à sua origem; não presumir placar ou súmula como saídas asseguradas do backend. **Problema:** informação ausente ou inconsistente impede referência precisa. **Recomendação:** manter vínculo entre corte e original, H25/RC05. |
| 2.2. Assistir aos cortes com contexto temporal | **Ação:** reproduzir os trechos em player externo ou na ilha do editor, incluindo a construção e o desfecho da jogada. **Feedback:** contexto percebido para julgamento. **Problema:** limite truncado pode ocultar a falta anterior, C02. **Recomendação:** investigar quanto contexto cada tipo de lance exige, RC04; não fixar uma duração universal. |
| 2.3. Avaliar pertinência, contexto e possíveis omissões | **Ação:** confrontar a seleção com a pauta, os critérios editoriais e as informações do editor. Se houver dúvida de omissão, pedir conferência no original. **Feedback:** parecer sobre o lote ou pendência de verificação. **Problema:** o índice de eventos detectados não é prova de cobertura completa, H10/H16. |
| **3. Deliberar e comunicar decisão editorial** | **Plano 3:** `(3.1 / 3.2) > 3.3`. Escolher 3.1 somente se a seleção atender aos critérios e não houver pendência de conferência; caso contrário, escolher 3.2. **Feedback:** editor recebe orientação vinculada ao material avaliado. |
| 3.1. Chancelar seleção para montagem externa | **Ação:** aprovar a seleção conferida para continuidade pelo editor. **Feedback:** lote aprovado; montagem e publicação ainda cabem às equipes externas, H23/H33. |
| 3.2. Solicitar revisão com referência ao lance | **Ação:** indicar partida, corte, timecode disponível e motivo do ajuste ou da conferência solicitada. **Feedback:** seleção devolvida, com chancela pendente. **Recomendação:** reduzir ambiguidade da orientação com metadados identificáveis. |
| 3.3. Comunicar decisão ao editor responsável | **Ação:** comunicar aprovação ou revisão pelo chat, ou presencialmente na alternativa de inspeção na ilha. **Feedback:** decisão comunicada. **Problema:** utilidade de recuperar decisões anteriores ainda aberta, H35. **Recomendação:** investigar se os registros externos bastam; não criar auditoria no produto. |
| **4. Conduzir contingência pós-publicação** | **Input:** alerta externo e identificação da publicação com falha editorial. **Plano 4:** `4.1 > 4.2 > 4.3 > 4.4`. Acionar somente quando a falha justificar retirada; críticas isoladas não bastam para concluir que há erro. **Feedback:** decisão sobre a versão corrigida comunicada; demais lotes continuam pendentes. |
| 4.1. Solicitar retirada à equipe de publicação | **Ação:** identificar a publicação afetada e solicitar a remoção pelo canal externo. **Problema:** propagação de material sem contexto, C02. **Feedback:** solicitação encaminhada; a confirmação da retirada depende da equipe responsável. |
| 4.2. Examinar corte e localizar falha de contexto | **Ação:** relacionar o vídeo publicado ao corte e ao timecode original com ajuda do editor. **Feedback:** trecho e falha identificados para correção. |
| 4.3. Orientar correção e solicitar nova versão | **Ação:** apontar o contexto faltante e pedir a reedição em ferramenta externa. **Feedback:** orientação transmitida; aguardar a entrega corrigida antes de 4.4. |
| **4.4. Reavaliar versão corrigida** | **Plano 4.4:** `4.4.1 > 4.4.2`. Se a versão continuar insuficiente, solicitar novo ajuste e repetir `4.3 > 4.4`. **Feedback:** nova decisão comunicada, sem autorização automática de republicação. |
| 4.4.1. Conferir correção e pertinência editorial | **Ação:** assistir à nova versão e verificar o contexto e os critérios usados em 2. **Feedback:** aprovação possível ou ajuste ainda necessário. |
| 4.4.2. Comunicar aprovação ou novo ajuste | **Ação:** comunicar a decisão sobre a versão identificada. **Feedback:** continuidade externa autorizada ou revisão pendente. |

### Verificação do HTA

O objetivo 0 expressa a meta humana de supervisão. Os ramos 1–3 cobrem o ciclo regular e o ramo 4 trata a contingência de C02. Cada folha está marcada como operação, e os objetivos decompostos têm planos explícitos com sequência, seleção, repetição, espera e término. A decomposição termina na consulta, inspeção, avaliação e comunicação úteis ao projeto, sem detalhar inferência do backend. A suficiência desses passos é uma hipótese de modelagem a validar com P02.

---

## GOMS — T02: Supervisionar processo editorial

**Autor(a):** Lucas Roberto Boccia dos Santos — 22.123.012-1\
**Recorte:** mesmo uso proposto externo de P02, H33/H40, com alternativa presencial e contingência de C02.\
**Abordagem:** modelo GOMS hierárquico conforme os exemplos dos slides 4–13 de **CC8122-GOMS-CTT**. Não se estima tempo por KLM: julgamento editorial, reprodução de vídeo, espera por correção e deslocamento exigiriam dados específicos.

### Modelo hierárquico de metas, métodos e operadores

Como nos slides, cada método pertence a uma meta, sua regra de seleção aparece junto dele e seus operadores são identificados dentro da sequência. Os métodos de uma mesma meta atingem o mesmo objetivo em condições diferentes. As folhas `OP.` representam ações concretas ou primitivas cognitivas no nível adotado; os trechos de reprodução devem ser repetidos para os cortes a avaliar.

```text
GOAL 0: supervisionar processo editorial e chancelar cortes
  METHOD 0.A: avaliar um lote recebido
  (SEL. RULE: lote disponível e nenhuma contingência editorial prioritária)
    GOAL 1: identificar e priorizar lote
      METHOD 1.A: consultar prioridades e entrega externa
      (SEL. RULE: aviso de entrega disponível pelo canal combinado)
        OP. 1.A.1: ler prioridades e prazos nas anotações da rodada
        OP. 1.A.2: ler o aviso do editor no chat corporativo
        OP. 1.A.3: abrir a pasta indicada no aviso
        OP. 1.A.4: conferir identificação da partida e do lote
        OP. 1.A.5: escolher o lote a inspecionar segundo prazo e pauta
    GOAL 2: avaliar a seleção e o contexto dos cortes
      METHOD 2.A: inspecionar arquivos na estação de supervisão
      (SEL. RULE: arquivos acessíveis e dúvida avaliável nos cortes recebidos)
        OP. 2.A.1: abrir o arquivo de metadados disponível
        OP. 2.A.2: ler partida, tipo de lance e timecodes dos cortes
        OP. 2.A.3: apontar o cursor para o corte a conferir
        OP. 2.A.4: abrir o corte no player externo
        OP. 2.A.5: assistir ao trecho com contexto anterior e posterior
        OP. 2.A.6: confrontar o trecho com os critérios editoriais
        OP. 2.A.7: identificar lacunas de contexto ou suspeitas de omissão
        OP. 2.A.8: anotar a referência e o motivo de eventual revisão
      METHOD 2.B: inspecionar com o editor na ilha de edição
      (SEL. RULE: arquivos inacessíveis ou dúvida não resolvida em 2.A;
       chamado presencial pode iniciar diretamente esta meta)
        OP. 2.B.1: deslocar-se até a ilha do editor responsável
        OP. 2.B.2: pedir identificação da partida e do trecho duvidoso
        OP. 2.B.3: pedir ao editor a reprodução do corte e do contexto no original
        OP. 2.B.4: assistir à reprodução apresentada pelo editor
        OP. 2.B.5: confrontar o trecho com os critérios editoriais
        OP. 2.B.6: identificar o trecho e o motivo de eventual revisão
    GOAL 3: deliberar e comunicar decisão sobre o lote
      METHOD 3.A: chancelar a seleção
      (SEL. RULE: seleção atende aos critérios e não há conferência pendente)
        OP. 3.A.1: formular a aprovação do lote identificado
        OP. 3.A.2: digitar a aprovação no chat ou comunicá-la presencialmente
        OP. 3.A.3: enviar a mensagem, se usado o chat
        OP. 3.A.4: verificar o envio ou a compreensão pelo editor presente
      METHOD 3.B: devolver a seleção para revisão
      (SEL. RULE: contexto insuficiente, suspeita de omissão ou dado inconsistente)
        OP. 3.B.1: recuperar a referência do corte ou do lance a conferir
        OP. 3.B.2: formular o ajuste, indicando partida, timecode disponível e motivo
        OP. 3.B.3: digitar o pedido no chat ou comunicá-lo presencialmente
        OP. 3.B.4: enviar a mensagem, se usado o chat
        OP. 3.B.5: verificar o envio ou a compreensão pelo editor presente
        GOAL 3.B.6: reavaliar o lote após a nova entrega
          METHOD 3.B.6.A: repetir inspeção e deliberação
          (SEL. RULE: nova versão recebida; enquanto não recebida, chancela pendente)
            GOAL 2: avaliar a nova versão pelos métodos 2.A ou 2.B
            GOAL 3: deliberar novamente pelos métodos 3.A ou 3.B
  METHOD 0.B: tratar contingência de publicação
  (SEL. RULE: alerta externo e falha editorial que justifica retirada;
   substituir o método regular em andamento, mantendo os demais lotes pendentes)
    GOAL 4: orientar correção e reavaliar material publicado com falha
      METHOD 4.A: solicitar retirada e coordenar nova versão externa
      (SEL. RULE: publicação afetada e equipe responsável identificadas)
        OP. 4.A.1: ler ou ouvir o alerta e identificar a publicação afetada
        OP. 4.A.2: avaliar se a falha justifica a retirada
        OP. 4.A.3: comunicar pedido de retirada à equipe de publicação
        OP. 4.A.4: examinar o corte e localizar a falha com o editor
        OP. 4.A.5: apontar a referência e o contexto que precisa ser corrigido
        OP. 4.A.6: comunicar pedido de reedição e nova entrega
        GOAL 4.A.7: reavaliar a versão corrigida
          METHOD 4.A.7.A: inspecionar e comunicar nova deliberação
          (SEL. RULE: versão corrigida recebida)
            GOAL 2: avaliar a versão corrigida pelos métodos 2.A ou 2.B
            GOAL 3: comunicar aprovação ou novo ajuste pelos métodos 3.A ou 3.B
```

**Leitura das regras de seleção:** 0.A e 0.B distinguem rotina e contingência; 2.A e 2.B são maneiras alternativas de obter a mesma avaliação; 3.A e 3.B comunicam resultados alternativos da mesma deliberação. Se ambos os meios de inspeção estiverem disponíveis e a dúvida puder ser resolvida nos arquivos, adotar 2.A; recorrer a 2.B nas condições explicitadas. A seleção de método não é um operador temporal CTT.

**Operadores:** ler e assistir são perceptivos; apontar, abrir, digitar, enviar e deslocar-se são externos; confrontar critérios, identificar lacunas, recuperar referências e formular a decisão são cognitivos. Arnaldo não precisa operar a linha do tempo do NLE: na alternativa presencial, o editor controla a reprodução. A hipótese H34 precisa ser investigada antes de pressupor domínio técnico de P02.

---

## CTT — T02: Supervisionar processo editorial

**Autor(a):** Lucas Roberto Boccia dos Santos — 22.123.012-1\
**Abordagem:** árvore de tarefas e relações temporais conforme os slides 19–24 de **CC8122-GOMS-CTT**.\
**Fronteira dos sistemas:** as interações e tarefas automáticas são do **chat, da pasta compartilhada e do player externos**, usados no percurso proposto de P02. Arnaldo não recebe notificações diretamente do backend do TCC. O aviso no chat vem do editor após A04, H33/H40. A alternativa presencial é detalhada no GOMS.

### Diagrama CTT

![CTT T02 — árvore com tipos de tarefas e operadores entre irmãs](../assets/05_tarefas/ctt_t02.svg)

*Figura 2 — CTT de T02, por Lucas Roberto. Nuvem: abstrata; pessoa: usuário; computador: sistema; pessoa e computador com seta dupla: interação. Os painéis inferiores expandem os nós da visão geral. [SVG editável](../assets/05_tarefas/ctt_t02.svg).*

As ligações descendentes mostram **decomposição**. As ligações horizontais entre tarefas irmãs carregam as **relações temporais**, como nos slides 23 e 24; não são planos HTA nem setas de um fluxograma. Os identificadores dos ramos 1–4 facilitam a comparação com o HTA; `D` agrupa as decisões de 3 e `S` identifica uma resposta automática do chat, que complementa as operações humanas do HTA.

### Leitura da árvore e condições

1. **Ciclo regular:** `1 []>> 2 []>> 3`. O lote identificado alimenta a inspeção; a avaliação alimenta a deliberação. O marcador `*` indica repetição do ciclo para cada lote recebido, incluindo novas versões após devolução. Encerrar quando não houver lotes pendentes de atendimento ou ao fim do turno, declarando as revisões ainda aguardadas.
2. **Identificação e prioridade (1):** `1.1 >> 1.2 []>> 1.3`. Arnaldo consulta prioridades em suas anotações, consulta o aviso e a pasta externos, e escolhe o lote. Não se presume atenção simultânea a vários vídeos nem uma fila de supervisão no produto.
3. **Inspeção (2):** `2.1 >> 2.2 []>> 2.3`. Consulta os metadados, reproduz os cortes e usa o que viu para julgar contexto, pertinência e suspeitas de omissão. Repetir a reprodução para os cortes da seleção e rever trechos duvidosos antes de concluir a avaliação. Essa repetição fica marcada em 2.2; não representa várias decisões finais independentes para o mesmo lote.
4. **Deliberação (3):** `D []>> 3.3 []>> S`, com `D = (3.1 [] 3.2)`. A chancela e a devolução são decisões humanas; enviar a mensagem é interação; entregar a mensagem é processamento automático do chat. A opção 3.1 exige critérios atendidos e ausência de pendências; 3.2 cobre ajuste ou conferência necessária. A escolha não implica que uma seleção insuficiente possa ser aprovada indistintamente. Em 3.2, a próxima avaliação depende de nova versão recebida, conforme o plano 0 do HTA.
5. **Contingência:** `Ciclo regular* [> 4`. Um alerta com falha que justifique retirada habilita 4 e **encerra a instância** do ciclo interrompido. O operador `[>` não guarda um ponto de retomada. Os demais lotes continuam pendentes; atendê-los depois exige iniciar um novo ciclo. Não se usou `|>`, que significaria suspensão e retomada automática do ponto interrompido.
6. **Correção emergencial (4):** `4.1 >> 4.2 []>> 4.3 >> 4.4`, e `4.4 = (4.4.1 []>> 4.4.2)`. Solicitar retirada, examinar o erro e orientar a reedição são interações externas. A nova versão precisa chegar antes da reavaliação. Arnaldo confere a correção e comunica aprovação ou novo ajuste; repetir `4.3 > 4.4` se ainda insuficiente, conforme o plano HTA. A árvore não executa a despublicação nem a montagem pelo produto.

### Legenda e relações temporais usadas

| Relação CTT | Notação | Significado e ocorrência em T02 |
|---|---|---|
| Ativação | `T1 >> T2` | T2 inicia após T1 terminar. Ex.: consultar prioridades antes de identificar o lote. |
| Ativação com passagem de informação | `T1 []>> T2` | T1 termina e transmite informação a T2. Ex.: lote identificado para inspeção; avaliação para decisão. |
| Escolha | `T1 [] T2` | Iniciar uma alternativa desabilita a outra naquela decisão. Ex.: chancelar ou solicitar revisão do mesmo lote. |
| Desativação | `T1 [> T2` | T2 interrompe completamente T1. Ex.: contingência encerra o ciclo regular em andamento. |
| Iteração | `T*` | Marcador de repetição, usado no ciclo por lote e na reprodução dos cortes, com condições descritas acima. |

`|||`, `|[]|`, `|=|` e `|>` aparecem nos slides, mas não são necessários neste recorte. A concorrência das ilhas de edição é parte do contexto; não comprova execução concorrente das ações de Arnaldo.

### Tipos de tarefas

| Símbolo no diagrama | Tipo nos slides | Aplicação no modelo |
|---|---|---|
| Nuvem | Abstrata | Objetivo global, ciclo regular, ramos 1–4, decisão D e reavaliação 4.4; agrupam outras tarefas. |
| Pessoa | Usuário | Consultar prioridades em anotações, escolher lote, julgar pertinência, chancelar ou solicitar revisão como decisões, conferir a correção. Atividades fora dos sistemas externos, incluindo julgamentos mentais. |
| Pessoa e computador, com seta dupla | Interativa | Consultar aviso e arquivos, ler metadados, reproduzir cortes, enviar decisão e orientações pelo chat. Há diálogo com aplicações externas. |
| Computador | Sistema | Entregar a mensagem no chat, sem nova ação de Arnaldo. Ler ou perceber o aviso é ação do usuário, não tarefa automática do TCC. |

---

## Síntese da modelagem de T02 e implicações para o projeto

Os três modelos de P02 detalham uma **proposta a validar**, não demonstram redução de tempo nem prevenção comprovada de crises:

1. **Identificação externa:** partida, corte e timecodes precisam permanecer compreensíveis após o download para que Arnaldo possa referenciar uma dúvida ao editor, H25/H33/H40 e RC05/RC09.
2. **Contexto e cobertura:** a inspeção requer construção e desfecho dos lances. A duração deve ser investigada, RC04; nem uma margem fixa de 5–10 segundos nem a lista de eventos detectados asseguram contexto ou cobertura editorial suficiente, H10/H16.
3. **Decisão humana e correção:** aprovação e devolução são alternativas condicionadas à avaliação. Ajuste de limites, montagem, retirada e publicação continuam em ferramentas e equipes externas. A nova versão exige nova conferência.
4. **Investigação com P02:** validar canais, critérios de chancela, compreensão dos metadados, forma de apontar omissões e como a equipe lida com contingências. H35 exige investigar se os registros externos atendem à recuperação de decisões antes de propor auditoria no produto. A revisão e o download devem conservar as informações usadas pela supervisão, sem ampliar automaticamente o escopo de IHC.

---

## Checklist da Entrega 5

**Verificação deste preenchimento: P02/T02, de Lucas Roberto. T01 e T03 permanecem com seus autores.**

- [x] T02 identifica autor, persona, cenário, hipóteses e relação R03.
- [x] HTA usa objetivos retangulares, operações sublinhadas e planos nos objetivos decompostos, conforme os slides.
- [x] A tabela HTA apresenta entrada, ação, feedback, planos, problemas e recomendações pertinentes.
- [x] GOMS segue a hierarquia `GOAL / METHOD / SEL. RULE / OP.` e associa cada regra ao método correspondente.
- [x] CTT distingue as quatro categorias com ícones e coloca relações temporais entre tarefas irmãs.
- [x] Diagramas, tabelas e interpretação textual de T02 estão sincronizados; SVGs editáveis em `assets/05_tarefas/`.
- [x] Os modelos declaram uso proposto externo, alternativa presencial e contingência, preservando H33/H40.
- [x] Benefícios e critérios não validados continuam tratados como hipóteses; H35 não virou funcionalidade.

---

## Histórico de revisões

| Data | Versão | Descrição da alteração | Autor(es) |
|---|---|---|---|
| 29/09/2026 | 0.1 | Criação do esqueleto base da Entrega 5 a partir do template da disciplina. | Equipe 16 |
| 07/10/2026 | 1.0 | Elaboração completa da tarefa T02 (*Supervisionar processo editorial*): contextualização no escopo do TCC, tabela de seleção de tarefas, modelagem HTA com planos 0 a 4 e decisões de design, modelagem CMN-GOMS com métodos e regras de seleção, modelagem CTT com operadores formais e tipos de tarefas de Paternò, síntese de requisitos e criação dos diagramas vetoriais `hta_t02.svg` e `ctt_t02.svg`. T01 e T03 permanecem engatilhadas para seus respectivos autores. | Lucas Roberto Boccia dos Santos |
| 09/10/2026 | 1.1 | Adequação exclusiva de P02/T02 aos slides CC8122-HTA e CC8122-GOMS-CTT: operações sublinhadas e planos no HTA, tabela com Input/Ação/Feedback, hierarquia GOMS, ícones e relações entre irmãs no CTT. Corrigidos o consumo externo por Arnaldo, a reavaliação após ajustes e os limites das hipóteses de contexto, cobertura e auditoria. | Lucas Roberto Boccia dos Santos |
