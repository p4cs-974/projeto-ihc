# Feedback do Professor

Vejo uma boa preocupação em representar decisões, interrupções, falhas e continuidade do trabalho, em vez de apenas descrever o percurso de sucesso. Também há cuidado em distinguir o processo atual dos cenários da Entrega 4 do uso proposto nesta entrega. Os vínculos em `RASTREABILIDADE.md` ajudam a compreender por que as tarefas foram escolhidas e a quais necessidades respondem.

A entrega, contudo, ainda precisa de ajustes de formalização. Os principais estão na distribuição das informações nas tabelas auxiliares dos HTAs, na apresentação e no detalhamento dos GOMS e na representação da motivação externa que antecede o uso do sistema em dois CTTs. Essas correções devem preservar o conteúdo pertinente que vocês já construíram.

## Pontos positivos

- **Estrutura dos HTAs.** Os três modelos partem da tarefa zero e apresentam decomposição hierárquica, sem se reduzirem a fluxogramas. Nos diagramas inspecionados, os nós decompostos possuem dois ou mais filhos, as tarefas terminais estão sublinhadas e os planos indicam relações entre subtarefas. Os painéis de detalhamento preservam a numeração e integram a mesma hierarquia.
- **GOMS textuais existentes.** T01, T02 e T03 apresentam `GOAL 0` e organização indentada. Existem regras de seleção relacionadas a condições de uso. Em T02, por exemplo, a conferência dos arquivos na estação e a conferência junto ao editor constituem alternativas contextualizadas.
- **CTTs com categorias e relações.** Os nós decompostos estão representados como abstrações, e os modelos distinguem tarefas do usuário, de interação e do sistema. Há relações temporais e tratamento de alternativas, repetição e interrupção.
- **Processamento do sistema representado.** T01 inclui disponibilização de arquivos ou informação de falha; T02 inclui entrega da mensagem pelo chat; T03 inclui retorno do estado ou da indisponibilidade. Em T02, o chat é um sistema externo ao produto, coerente com o recorte declarado para Arnaldo.
- **Limites do projeto preservados.** A seleção editorial permanece humana, a correção externa não se transforma indevidamente em funcionalidade já implementada e o acompanhamento remoto não é apresentado como solução automática para todas as restrições de armazenamento de Jorginho.

## Correções prioritárias

### 1. Reorganizar as tabelas auxiliares dos três HTAs

A tarefa zero apresenta Input, Feedback e Plano, como esperado. O problema está na repetição de Input e Feedback nas tarefas filhas. Esses campos devem caracterizar a tarefa global; nas subtarefas, as informações sobre interação devem aparecer como ações ou recomendações, mantendo planos nos nós que possuem decomposição.

Em T01, isso aparece, por exemplo, na tarefa `1.3 — Recuperar finalidade, critérios e prazo` e no tratamento de interrupção. Em T02, ocorre em `1.1 — Consultar prioridades e prazos` e `2.1 — Conferir identificação e timecodes`. Em T03, aparece em `1.1 — Abrir lista` e `2.1 — Consultar estado`. A ocorrência é recorrente nas três tabelas, não um ajuste isolado.

Não apaguem informações úteis. Uma resposta exibida durante uma subtarefa pode ser descrita como recomendação para a interação ou como ação de conferir essa resposta. Reservem o Input da tarefa zero às condições e informações necessárias para iniciar a tarefa, e o Feedback ao resultado que permite reconhecer sua conclusão ou seu desfecho. Preservem a correspondência entre os números da tabela, os nós dos diagramas e os planos.

### 2. Consolidar o GOMS como representação textual

T01 e T03 possuem diagramas apresentados como “Diagrama GOMS”, além das versões textuais. A representação formal solicitada para GOMS é textual e indentada. Retirem esses diagramas da apresentação do modelo e mantenham o texto como referência, evitando duas representações que possam divergir nas próximas revisões. T02 já atende ao formato textual.

Revisem também a diferença entre uma condição necessária para começar e uma regra que seleciona entre métodos. Quando há apenas uma forma de executar uma meta, ela pode ser descrita diretamente por seus operadores. Por exemplo, condições como a partida estar disponível após T03 ou a lista estar acessível são precondições; por si sós, não justificam criar uma alternativa de execução.

Mantenham métodos e regras de seleção quando realmente existirem maneiras diferentes de alcançar a mesma meta. A distinção entre conferir os arquivos na própria estação e conferir junto ao editor, em T02, é um bom exemplo a preservar.

### 3. Refinar os operadores e tornar explícita a verificação dos resultados

Alguns operadores agregam ações diferentes ou contêm alternativas internas. Em T01, `OP 3.C.2`, que reúne abrir o editor externo e localizar o trecho, pode ser separado em operações concretas. Em T02, `OP 3.A.2` reúne “digitar aprovação no chat ou comunicá-la presencialmente”. Essa escolha precisa estar associada a uma condição ou a métodos de comunicação distintos, coerentes com o contexto já descrito. A mesma revisão se aplica à comunicação de pedidos de ajuste.

Confiram, ainda, se cada sequência termina com uma verificação mental do efeito pretendido. Em T02, `OP 2.A.8` termina na anotação da referência e do motivo de eventual revisão; acrescentem a conferência de que a avaliação e as pendências foram registradas corretamente. Em T03, `OP 4.A.4` reúne decidir quais pendências consultar depois e encerrar a sessão; explicitem antes do encerramento como o usuário reconhece o que ficou concluído e o que continua pendente. Em T01, a retomada após interrupção deve evidenciar a conferência do contexto recuperado antes de prosseguir.

Há verificações bem construídas que devem ser mantidas, como conferir inclusão ou exclusão de um lance e verificar a comunicação da decisão editorial. Em T03, `OP 3.C.4` já verifica a aceitação ou rejeição da recuperação depois das alternativas. Portanto, o problema não é ausência completa dessa verificação: deixem explícito que ela se aplica aos dois caminhos e que acionar a confirmação não equivale a reconhecer o resultado.

### 4. Representar a motivação externa inicial nos CTTs de T01 e T03

Os modelos possuem tarefas do usuário, mas a presença dessa categoria, sozinha, não assegura a representação da ação externa que motiva o início do uso do sistema.

Em T01, o percurso começa com abrir os resultados. A recuperação da finalidade, dos critérios e do prazo aparece depois dessa interação. Representem antes da abertura a situação motivadora: por exemplo, o editor receber uma demanda editorial e decidir revisar os lances daquela partida. Essa ação precisa fazer parte da árvore, com a relação temporal correspondente, sem ficar apenas na contextualização textual. A interrupção modelada durante a tarefa não substitui essa motivação inicial.

Em T03, o início também ocorre já na interface, com a abertura da lista. O texto menciona consulta por iniciativa do usuário ou por aviso, mas a árvore deve representar a ação externa que o leva a voltar ao acompanhamento, como interromper outra atividade e decidir consultar o andamento das partidas. Depois, devem vir a interação de consulta, a resposta do sistema e a interpretação pelo usuário.

T02 já apresenta a consulta de prioridades e prazos antes da consulta ao aviso, estabelecendo essa entrada contextual. Preservem essa qualidade. Nos três modelos já há processamento do sistema; a correção solicitada em T01 e T03 é completar a origem da interação, não acrescentar arbitrariamente um nó de sistema que já existe.

## Recomendações de melhoria

- Revisem a legibilidade dos SVGs em `assets/05_tarefas/`. Há textos que ultrapassam caixas, como no detalhamento de `4.4.1` do HTA de T02 e de `3.2.3` do HTA de T03. No CTT de T03, alguns rótulos longos ficam próximos de nós vizinhos. Ajustem largura, quebra de linha e espaçamento.
- Facilitem a navegação pelos CTTs extensos. Uma visão geral seguida de detalhamentos claramente identificados pode preservar a hierarquia e permitir leitura sem depender de ampliar uma imagem muito longa.
- Façam uma revisão cruzada dos três modelos de cada tarefa. Uma alternativa no GOMS deve ser compatível com as opções do HTA e com as relações do CTT; não é necessário que as três técnicas tenham a mesma aparência ou o mesmo nível de detalhe.
- Preservem o envio inicial como precondição quando esse for o recorte da tarefa. A ausência de um modelo específico de envio não invalida os três conjuntos entregues, mas essa fronteira deve continuar explícita na continuidade do projeto.
- Mantenham frequência, criticidade e condições de trabalho como hipóteses enquanto não houver dados que as sustentem. A extensão da documentação não substitui a investigação com usuários.

## Pontos que devem alimentar as próximas entregas

A revisão dos lances em T01 deve orientar a identificação da partida e do trecho, a compreensão do contexto, a diferenciação entre selecionado e descartado e a retomada depois de uma interrupção. Também deve ficar claro quando o usuário precisa retornar à gravação ou a um editor externo.

T02 deve orientar a qualidade dos cortes e metadados entregues ao supervisor: identificação, timecodes, contexto e referência precisa para pedir ajustes. A modelagem não implica criar uma área administrativa para Arnaldo sem justificar essa ampliação de escopo.

T03 deve orientar a apresentação de estados por partida, a compreensão de falhas, as possibilidades efetivamente disponíveis de recuperação e a preservação das demais partidas quando apenas uma apresenta problema. Diferenciem o pedido de recuperação de sua aceitação pelo sistema.

Na investigação com usuários, verifiquem como reconhecem um resultado suficiente, que informações precisam recuperar após uma interrupção e como decidem entre aguardar, tentar novamente ou manter uma pendência. Esses pontos podem produzir critérios concretos para avaliar os futuros protótipos.

## Síntese das ações recomendadas

1. Manter Input e Feedback somente na tarefa zero de cada tabela HTA, realocando o conteúdo das tarefas filhas.
2. Apresentar os três GOMS em texto indentado, distinguindo precondições, métodos e regras de seleção.
3. Separar operações agregadas e explicitar as verificações finais, preservando as verificações comuns já existentes.
4. Incluir a motivação externa inicial nos CTTs de T01 e T03.
5. Ajustar a legibilidade dos diagramas e conferir a consistência entre os modelos e a rastreabilidade.

De forma geral, considero a Entrega 5 consistente na escolha das tarefas, completa na distribuição entre os integrantes e cuidadosa ao representar exceções e limites do projeto. Os modelos oferecem uma base útil para as próximas decisões de interface, mas ainda precisam das correções de formalismo indicadas para que a documentação não apenas descreva o trabalho em detalhe, mas represente corretamente cada técnica. Espero que a próxima revisão preserve essa riqueza contextual e torne mais precisa a relação entre ação, decisão e verificação do resultado.
