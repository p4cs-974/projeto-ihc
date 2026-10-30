# Feedback do Professor

> **Status da aplicação (27/10/2026):** [F] revisão aplicada por Lucas em T01, T02 e T03, com autorização expressa para as três tarefas e seus SVGs. As autorias originais foram preservadas. Branch `lab-7-robertinho`. O texto do professor permanece intacto; os blocos de citação registram o tratamento e os commits.
>
> | Item do parecer | Situação | Commit(s) |
> |---|---|---|
> | Correção 1: tabelas auxiliares dos HTAs | Aplicada nas três tarefas, conforme pertinência | [`8e9e68a`](https://github.com/p4cs-974/projeto-ihc/commit/8e9e68a) |
> | Correção 2: GOMS textuais e escolhas | Aplicada nas três tarefas, conforme pertinência | [`d585b2b`](https://github.com/p4cs-974/projeto-ihc/commit/d585b2b) |
> | Correção 3: operadores e verificações | Aplicada nas três tarefas, conforme pertinência | [`313e226`](https://github.com/p4cs-974/projeto-ihc/commit/313e226) |
> | Correção 4: motivação externa nos CTTs | Aplicada nas três tarefas, conforme pertinência | [`d867b11`](https://github.com/p4cs-974/projeto-ihc/commit/d867b11) |
> | Recomendações: legibilidade, navegação, consistência e limites | Aplicada nas três tarefas, conforme pertinência | [`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041) |
> | Pontos para as próximas entregas | Encaminhados à investigação, sem validação presumida | [`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041) |
> | Cabeçalho, histórico e rastreabilidade | Registrados | [`e56f59f`](https://github.com/p4cs-974/projeto-ihc/commit/e56f59f) |
>
> \- Lucas


Vejo uma boa preocupação em representar decisões, interrupções, falhas e continuidade do trabalho, em vez de apenas descrever o percurso de sucesso. Também há cuidado em distinguir o processo atual dos cenários da Entrega 4 do uso proposto nesta entrega. Os vínculos em `RASTREABILIDADE.md` ajudam a compreender por que as tarefas foram escolhidas e a quais necessidades respondem.

A entrega, contudo, ainda precisa de ajustes de formalização. Os principais estão na distribuição das informações nas tabelas auxiliares dos HTAs, na apresentação e no detalhamento dos GOMS e na representação da motivação externa que antecede o uso do sistema em dois CTTs. Essas correções devem preservar o conteúdo pertinente que vocês já construíram.

## Pontos positivos

- **Estrutura dos HTAs.** Os três modelos partem da tarefa zero e apresentam decomposição hierárquica, sem se reduzirem a fluxogramas. Nos diagramas inspecionados, os nós decompostos possuem dois ou mais filhos, as tarefas terminais estão sublinhadas e os planos indicam relações entre subtarefas. Os painéis de detalhamento preservam a numeração e integram a mesma hierarquia.
- **GOMS textuais existentes.** T01, T02 e T03 apresentam `GOAL 0` e organização indentada. Existem regras de seleção relacionadas a condições de uso. Em T02, por exemplo, a conferência dos arquivos na estação e a conferência junto ao editor constituem alternativas contextualizadas.
- **CTTs com categorias e relações.** Os nós decompostos estão representados como abstrações, e os modelos distinguem tarefas do usuário, de interação e do sistema. Há relações temporais e tratamento de alternativas, repetição e interrupção.
- **Processamento do sistema representado.** T01 inclui disponibilização de arquivos ou informação de falha; T02 inclui entrega da mensagem pelo chat; T03 inclui retorno do estado ou da indisponibilidade. Em T02, o chat é um sistema externo ao produto, coerente com o recorte declarado para Arnaldo.
- **Limites do projeto preservados.** A seleção editorial permanece humana, a correção externa não se transforma indevidamente em funcionalidade já implementada e o acompanhamento remoto não é apresentado como solução automática para todas as restrições de armazenamento de Jorginho.


> **ℹ️ Preservação dos pontos positivos** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): As estruturas hierárquicas, alternativas pertinentes, processamento do sistema e limites do projeto foram preservados durante a conferência entre os modelos.
>
> \- Lucas

## Correções prioritárias

### 1. Reorganizar as tabelas auxiliares dos três HTAs

A tarefa zero apresenta Input, Feedback e Plano, como esperado. O problema está na repetição de Input e Feedback nas tarefas filhas. Esses campos devem caracterizar a tarefa global; nas subtarefas, as informações sobre interação devem aparecer como ações ou recomendações, mantendo planos nos nós que possuem decomposição.

Em T01, isso aparece, por exemplo, na tarefa `1.3 — Recuperar finalidade, critérios e prazo` e no tratamento de interrupção. Em T02, ocorre em `1.1 — Consultar prioridades e prazos` e `2.1 — Conferir identificação e timecodes`. Em T03, aparece em `1.1 — Abrir lista` e `2.1 — Consultar estado`. A ocorrência é recorrente nas três tabelas, não um ajuste isolado.

Não apaguem informações úteis. Uma resposta exibida durante uma subtarefa pode ser descrita como recomendação para a interação ou como ação de conferir essa resposta. Reservem o Input da tarefa zero às condições e informações necessárias para iniciar a tarefa, e o Feedback ao resultado que permite reconhecer sua conclusão ou seu desfecho. Preservem a correspondência entre os números da tabela, os nós dos diagramas e os planos.


> **✅ Como foi tratado** ([`8e9e68a`](https://github.com/p4cs-974/projeto-ihc/commit/8e9e68a)): [F] As três tabelas HTA reservam Input e Feedback à tarefa 0. Condições locais e retornos intermediários aparecem como recomendações de informação/conferência ou ações; planos, IDs e conteúdo útil permanecem nas subtarefas. A nota comum diferencia desfecho global de resposta intermediária.
>
> \- Lucas

### 2. Consolidar o GOMS como representação textual

T01 e T03 possuem diagramas apresentados como “Diagrama GOMS”, além das versões textuais. A representação formal solicitada para GOMS é textual e indentada. Retirem esses diagramas da apresentação do modelo e mantenham o texto como referência, evitando duas representações que possam divergir nas próximas revisões. T02 já atende ao formato textual.

Revisem também a diferença entre uma condição necessária para começar e uma regra que seleciona entre métodos. Quando há apenas uma forma de executar uma meta, ela pode ser descrita diretamente por seus operadores. Por exemplo, condições como a partida estar disponível após T03 ou a lista estar acessível são precondições; por si sós, não justificam criar uma alternativa de execução.

Mantenham métodos e regras de seleção quando realmente existirem maneiras diferentes de alcançar a mesma meta. A distinção entre conferir os arquivos na própria estação e conferir junto ao editor, em T02, é um bom exemplo a preservar.


> **✅ Como foi tratado** ([`d585b2b`](https://github.com/p4cs-974/projeto-ihc/commit/d585b2b)): [F] T01/T02/T03 usam GOMS textual e indentado como referência; os diagramas de T01/T03 saem da apresentação. A meta 0 não recebe método. Metas de caminho único têm execução direta e precondições explícitas. Em T02, a submeta A distingue rotina e contingência; os métodos de inspeção 2.A/2.B permanecem.
>
> \- Lucas

### 3. Refinar os operadores e tornar explícita a verificação dos resultados

Alguns operadores agregam ações diferentes ou contêm alternativas internas. Em T01, `OP 3.C.2`, que reúne abrir o editor externo e localizar o trecho, pode ser separado em operações concretas. Em T02, `OP 3.A.2` reúne “digitar aprovação no chat ou comunicá-la presencialmente”. Essa escolha precisa estar associada a uma condição ou a métodos de comunicação distintos, coerentes com o contexto já descrito. A mesma revisão se aplica à comunicação de pedidos de ajuste.

Confiram, ainda, se cada sequência termina com uma verificação mental do efeito pretendido. Em T02, `OP 2.A.8` termina na anotação da referência e do motivo de eventual revisão; acrescentem a conferência de que a avaliação e as pendências foram registradas corretamente. Em T03, `OP 4.A.4` reúne decidir quais pendências consultar depois e encerrar a sessão; explicitem antes do encerramento como o usuário reconhece o que ficou concluído e o que continua pendente. Em T01, a retomada após interrupção deve evidenciar a conferência do contexto recuperado antes de prosseguir.

Há verificações bem construídas que devem ser mantidas, como conferir inclusão ou exclusão de um lance e verificar a comunicação da decisão editorial. Em T03, `OP 3.C.4` já verifica a aceitação ou rejeição da recuperação depois das alternativas. Portanto, o problema não é ausência completa dessa verificação: deixem explícito que ela se aplica aos dois caminhos e que acionar a confirmação não equivale a reconhecer o resultado.


> **✅ Como foi tratado** ([`313e226`](https://github.com/p4cs-974/projeto-ihc/commit/313e226)): [F] Abertura/localização do original e reprodução/avaliação do arquivo salvo têm operadores separados. T02 possui métodos condicionados para comunicar aprovação e ajustes por chat ou presencialmente e verifica os registros da avaliação. Os blocos terminam com conferência pelo usuário; T01 verifica contexto antes de retomar, e T03 identifica concluído/pendente antes de encerrar. 3.C.4 de T03 confere o desfecho tanto do reenvio quanto da nova tentativa e da pendência.
>
> \- Lucas

### 4. Representar a motivação externa inicial nos CTTs de T01 e T03

Os modelos possuem tarefas do usuário, mas a presença dessa categoria, sozinha, não assegura a representação da ação externa que motiva o início do uso do sistema.

Em T01, o percurso começa com abrir os resultados. A recuperação da finalidade, dos critérios e do prazo aparece depois dessa interação. Representem antes da abertura a situação motivadora: por exemplo, o editor receber uma demanda editorial e decidir revisar os lances daquela partida. Essa ação precisa fazer parte da árvore, com a relação temporal correspondente, sem ficar apenas na contextualização textual. A interrupção modelada durante a tarefa não substitui essa motivação inicial.

Em T03, o início também ocorre já na interface, com a abertura da lista. O texto menciona consulta por iniciativa do usuário ou por aviso, mas a árvore deve representar a ação externa que o leva a voltar ao acompanhamento, como interromper outra atividade e decidir consultar o andamento das partidas. Depois, devem vir a interação de consulta, a resposta do sistema e a interpretação pelo usuário.

T02 já apresenta a consulta de prioridades e prazos antes da consulta ao aviso, estabelecendo essa entrada contextual. Preservem essa qualidade. Nos três modelos já há processamento do sistema; a correção solicitada em T01 e T03 é completar a origem da interação, não acrescentar arbitrariamente um nó de sistema que já existe.


> **✅ Como foi tratado** ([`d867b11`](https://github.com/p4cs-974/projeto-ihc/commit/d867b11)): [F] Texto e árvores CTT de T01/T03 começam com M, ação do usuário fora da interface, seguida de M []>> U. Em T01, a demanda editorial motiva decidir revisar; em T03, o usuário interrompe outra atividade e decide consultar. A sessão U conserva consultas, respostas do sistema, decisões e encerramentos. A entrada contextual de T02 foi preservada.
>
> \- Lucas

## Recomendações de melhoria

- Revisem a legibilidade dos SVGs em `assets/05_tarefas/`. Há textos que ultrapassam caixas, como no detalhamento de `4.4.1` do HTA de T02 e de `3.2.3` do HTA de T03. No CTT de T03, alguns rótulos longos ficam próximos de nós vizinhos. Ajustem largura, quebra de linha e espaçamento.

  > **✅ Como foi tratado** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): [F] Ajustadas as quebras dos rótulos 4.4.1 do HTA de T02 e 3.2.3 do HTA de T03 e dos rótulos longos dos CTTs. Os seis HTA/CTT completos foram medidos no Chromium, sem texto fora das caixas ou sobreposição de rótulos; os recortes foram renderizados para conferência visual.
  >
  > \- Lucas

- Facilitem a navegação pelos CTTs extensos. Uma visão geral seguida de detalhamentos claramente identificados pode preservar a hierarquia e permitir leitura sem depender de ampliar uma imagem muito longa.

  > **✅ Como foi tratado** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): [F] Cada CTT tem visão geral e detalhamentos identificados pelos ramos, em blocos expansíveis. São recortes do SVG completo, com a mesma hierarquia, IDs e relações; o arquivo completo continua vinculado.
  >
  > \- Lucas

- Façam uma revisão cruzada dos três modelos de cada tarefa. Uma alternativa no GOMS deve ser compatível com as opções do HTA e com as relações do CTT; não é necessário que as três técnicas tenham a mesma aparência ou o mesmo nível de detalhe.

  > **✅ Como foi tratado** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): [F] A seção de correspondência relaciona as escolhas HTA aos métodos GOMS e às relações CTT. T02 representa comunicação por chat ou presencialmente; o retorno automático do chat permanece apenas no caminho por chat. As três técnicas mantêm níveis de detalhe próprios.
  >
  > \- Lucas

- Preservem o envio inicial como precondição quando esse for o recorte da tarefa. A ausência de um modelo específico de envio não invalida os três conjuntos entregues, mas essa fronteira deve continuar explícita na continuidade do projeto.

  > **✅ Como foi tratado** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): [F] O envio inicial permanece precondição de T03 e fora da modelagem específica desta entrega. O novo envio de uma partida afetada é recuperação condicionada; não equivale a remodelar A01 ou garantir sucesso.
  >
  > \- Lucas

- Mantenham frequência, criticidade e condições de trabalho como hipóteses enquanto não houver dados que as sustentem. A extensão da documentação não substitui a investigação com usuários.

  > **✅ Como foi tratado** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): [F] Frequência, criticidade e condições de trabalho permanecem hipóteses. A aplicação é documental; não altera o estado das hipóteses nem presume validação com usuários.
  >
  > \- Lucas


## Pontos que devem alimentar as próximas entregas

A revisão dos lances em T01 deve orientar a identificação da partida e do trecho, a compreensão do contexto, a diferenciação entre selecionado e descartado e a retomada depois de uma interrupção. Também deve ficar claro quando o usuário precisa retornar à gravação ou a um editor externo.

> **ℹ️ Encaminhamento** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): T01 orienta critérios de identificação, contexto, seleção/descarte e retomada, com retorno ao original/editor externo quando necessário. A seção Continuidade da investigação registra a avaliação futura desses critérios.
>
> \- Lucas


T02 deve orientar a qualidade dos cortes e metadados entregues ao supervisor: identificação, timecodes, contexto e referência precisa para pedir ajustes. A modelagem não implica criar uma área administrativa para Arnaldo sem justificar essa ampliação de escopo.

> **ℹ️ Encaminhamento** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): T02 orienta identificação, timecodes, contexto e referências para ajustes. O consumo externo por Arnaldo foi preservado, sem área administrativa proposta nesta revisão.
>
> \- Lucas


T03 deve orientar a apresentação de estados por partida, a compreensão de falhas, as possibilidades efetivamente disponíveis de recuperação e a preservação das demais partidas quando apenas uma apresenta problema. Diferenciem o pedido de recuperação de sua aceitação pelo sistema.

> **ℹ️ Encaminhamento** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): T03 diferencia estados, falhas, aceitação dos pedidos e preservação das demais partidas. Recuperação e avisos continuam condicionados às capacidades técnicas e à investigação.
>
> \- Lucas


Na investigação com usuários, verifiquem como reconhecem um resultado suficiente, que informações precisam recuperar após uma interrupção e como decidem entre aguardar, tentar novamente ou manter uma pendência. Esses pontos podem produzir critérios concretos para avaliar os futuros protótipos.

> **ℹ️ Encaminhamento** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): A seção Continuidade da investigação reúne reconhecimento de suficiência, contexto após interrupção e decisão entre aguardar, tentar novamente ou manter pendência. A coleta e a avaliação do protótipo são trabalho futuro, sem alterações nesta rodada na Entrega 7.
>
> \- Lucas


## Síntese das ações recomendadas

1. Manter Input e Feedback somente na tarefa zero de cada tabela HTA, realocando o conteúdo das tarefas filhas.
2. Apresentar os três GOMS em texto indentado, distinguindo precondições, métodos e regras de seleção.
3. Separar operações agregadas e explicitar as verificações finais, preservando as verificações comuns já existentes.
4. Incluir a motivação externa inicial nos CTTs de T01 e T03.
5. Ajustar a legibilidade dos diagramas e conferir a consistência entre os modelos e a rastreabilidade.


> **Situação** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): [F] As quatro correções e as recomendações estão aplicadas em T01/T02/T03. Os pontos empíricos estão encaminhados para investigação. Não ficam ajustes documentais atribuídos a outros integrantes nesta rodada.
>
> \- Lucas

De forma geral, considero a Entrega 5 consistente na escolha das tarefas, completa na distribuição entre os integrantes e cuidadosa ao representar exceções e limites do projeto. Os modelos oferecem uma base útil para as próximas decisões de interface, mas ainda precisam das correções de formalismo indicadas para que a documentação não apenas descreva o trabalho em detalhe, mas represente corretamente cada técnica. Espero que a próxima revisão preserve essa riqueza contextual e torne mais precisa a relação entre ação, decisão e verificação do resultado.

## Comentários adicionais fornecidos por Lucas

> **[F] Tratamento complementar (27/10/2026):** os comentários adicionais integram a mesma revisão autorizada nas três tarefas. Sua numeração de referência é a da versão recebida.
>
> \- Lucas

- “só o 0 tem feedback na tabela” e “trocar a palavra feedback pra recomendação”.

  > **✅ Como foi tratado** ([`8e9e68a`](https://github.com/p4cs-974/projeto-ihc/commit/8e9e68a)): [F] Input e Feedback estão restritos à tarefa 0. Recomendações locais indicam o que disponibilizar naquele momento ou o reconhecimento humano a apoiar; o Feedback global descreve o resultado que permite reconhecer o desfecho.
  >
  > \- Lucas

- “goal 0 não tem método” e “se vc só tem um jeito de fazer as coisas não precisa explicar os métodos”.

  > **✅ Como foi tratado** ([`d585b2b`](https://github.com/p4cs-974/projeto-ihc/commit/d585b2b)): [F] Os três GOAL 0 estão sem METHOD. Metas de caminho único usam operadores/submetas diretos. A escolha rotina/contingência de T02 pertence à submeta A.
  >
  > \- Lucas

- “o último operador do bloco de operadores precisa ser uma verificação do usuário (feedback positivo)”.

  > **✅ Como foi tratado** ([`313e226`](https://github.com/p4cs-974/projeto-ihc/commit/313e226)): [F] Os blocos terminam com verificação perceptiva/cognitiva pelo usuário. A verificação reconhece o efeito obtido; rejeição e pendência permanecem explícitas, sem inventar resultado positivo do sistema.
  >
  > \- Lucas

- “3.c.4.a.4 quebrar em 2 operadores”.

  > **✅ Como foi tratado** ([`313e226`](https://github.com/p4cs-974/projeto-ihc/commit/313e226)): [F] O antigo OP. 3.C.4.A.4 de T01 foi separado em reproduzir o arquivo salvo e verificar seu contexto. A separação prévia de abrir/localizar o original desloca a submeta para 3.C.5: os operadores correspondentes são 3.C.5.A.4 e 3.C.5.A.5.
  >
  > \- Lucas

- “quando for / ou +, precisa ter método” e “quando é > (sequencia) não precisa ter método”.

  > **✅ Como foi tratado** ([`73b9041`](https://github.com/p4cs-974/projeto-ihc/commit/73b9041)): [F] A seção de correspondência diferencia escolhas dos HTAs, métodos GOMS e relações CTT. Sequências de caminho único não recebem métodos GOMS; os planos HTA permanecem nos nós decompostos. Não há paralelismo + nestes recortes.
  >
  > \- Lucas
