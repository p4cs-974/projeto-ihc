# Feedback do Professor > Entrega 04 > Equipe 16

> **Status da aplicação (03/10/2026):** esta revisão cobre o cenário de Pedro (C01, Rafael) e as partes de grupo da entrega: cabeçalho, ligação com a ficha e o contexto de P01 e matriz de rastreabilidade. C02, de Lucas, e C03, de Giovanni, ficam com seus autores. Cada comentário abaixo traz uma anotação com o link para o commit correspondente, na branch `aplicar-feedback`. O texto original do professor foi preservado; as anotações aparecem em blocos de citação logo após cada item.
>
> | Item do parecer | Situação | Commit(s) |
> |---|---|---|
> | Correção 1: numerar as questões e indicar as respostas | aplicada em C01; C02 e C03 ficam com Lucas e Giovanni | [`df5f14e`](https://github.com/p4cs-974/projeto-ihc/commit/df5f14e) |
> | Correção 2: questões que investigam informação ausente | aplicada em C01; C02 e C03 ficam com Lucas e Giovanni | [`3e7d960`](https://github.com/p4cs-974/projeto-ihc/commit/3e7d960) |
> | Correção 3: planejamento, ações, eventos e avaliação | aplicada em C01; C02 fica com Lucas | [`68a2bf2`](https://github.com/p4cs-974/projeto-ihc/commit/68a2bf2) |
> | Correção 4: suposições e diagnóstico | aplicada em C01; C03 fica com Giovanni e C02 com Lucas | [`19ea7c5`](https://github.com/p4cs-974/projeto-ihc/commit/19ea7c5) |
> | Correção 5: necessidades sem solução presumida | aplicada em C01; C02 e C03 ficam com Lucas e Giovanni | [`0173b0c`](https://github.com/p4cs-974/projeto-ihc/commit/0173b0c) |
> | Recomendação: versões iniciais como episódios concretos | aplicada em C01 | [`06dd91a`](https://github.com/p4cs-974/projeto-ihc/commit/06dd91a) |
> | Recomendação: evitar adjetivos como "engessado" ou "caótico" | sem ocorrência em C01; C02 fica com Lucas | |
> | Recomendação: desfecho com conseguido, pendente e avaliação | aplicada em C01 | [`65bcb05`](https://github.com/p4cs-974/projeto-ihc/commit/65bcb05) |
> | Recomendação: sincronizar personas e contexto | aplicada entre C01 e P01 | [`daec541`](https://github.com/p4cs-974/projeto-ihc/commit/daec541) |
> | Pontos para as próximas entregas | registrados na matriz para C01 | [`d696e16`](https://github.com/p4cs-974/projeto-ihc/commit/d696e16) |
> | Registro da revisão | cabeçalho, matriz e índice do README | [`9fbbef5`](https://github.com/p4cs-974/projeto-ihc/commit/9fbbef5), [`c0bf81e`](https://github.com/p4cs-974/projeto-ihc/commit/c0bf81e) |
>
> \- Pedro

## Avaliação geral

A equipe apresenta três cenários, cada um com versão inicial, questões de refinamento e narrativa refinada. A distribuição atende à quantidade por integrante: Pedro desenvolveu C01, sobre Rafael; Lucas desenvolveu C02, sobre Arnaldo; e Giovanni desenvolveu C03, sobre Jorginho Jr. Os cenários têm nome, ator principal identificado e narrativa textual.

O trabalho consegue mostrar dificuldades atuais de seleção de lances, supervisão editorial e produção amadora com recursos limitados. As versões refinadas são mais concretas que as iniciais e explicitam consequências para a atividade. Entretanto, **o refinamento ainda não atende integralmente ao formalismo solicitado**: as perguntas não estão numeradas e a marcação genérica **[NOVO]** não identifica qual pergunta é respondida em cada trecho. Também há questões cuja informação já estava parcialmente na versão inicial e distinções conceituais que precisam ser mais precisas.

## Pontos positivos

- Os três integrantes possuem um cenário inicial e uma versão refinada correspondentes. Há sete linhas de questões por cenário, cobrindo nominalmente ambiente/contexto, ator, objetivo, planejamento, ações, eventos e avaliação.
- As narrativas se concentram predominantemente na situação atual, com ferramentas e práticas existentes, sem transformar o cenário de problema em uma sequência de telas do produto pretendido.
- C01 apresenta uma relação compreensível entre busca manual, atenção prolongada, pressão de prazo e risco de cortes sem contexto. A necessidade de rever a seleção aparece ligada ao trabalho do editor.
- C02 amplia a análise para a coordenação entre pessoas. As interrupções, a fila de aprovações e as consequências de uma publicação descontextualizada tornam visível um problema de trabalho coletivo.
- C03 descreve uma estratégia concreta para lidar com pouco armazenamento: trabalhar uma partida por vez e liberar espaço antes da próxima. O cenário também conecta busca visual, fadiga e qualidade da seleção.
- A equipe declara o caráter hipotético dos cenários e separa perguntas para investigação futura das respostas adotadas na construção narrativa.
- A rastreabilidade relaciona C01 a P01/R01, C02 a P02/R03 e C03 a P03/R04/R05. Essas conexões ajudam a preservar a continuidade do projeto.

## Correções prioritárias

### 1. Numerar as questões e indicar suas respostas na narrativa

Nas seções “Questões de refinamento”, as perguntas estão identificadas pelo elemento, mas não por números. Nas três narrativas refinadas, os parágrafos recebem apenas **[NOVO]**. Essa marca informa que houve desenvolvimento do texto, porém não permite verificar qual pergunta motivou cada informação acrescentada.

Numerem as perguntas de cada cenário e insiram o número correspondente entre colchetes no ponto da narrativa em que a resposta aparece. Se um trecho responder a mais de uma questão, indiquem as referências necessárias. Uma seção posterior de elementos extraídos não substitui essa ligação dentro do relato.

A finalidade é permitir que o leitor acompanhe o percurso entre lacuna, pergunta e informação nova. Preservem a situação inicial e mostrem como ela foi aprofundada; não é necessário marcar toda a narrativa como se cada detalhe fosse novo. Essa correção deve ocorrer nos três cenários.

> **🟨 Tratado em parte** ([`df5f14e`](https://github.com/p4cs-974/projeto-ihc/commit/df5f14e)): as questões de C01 estão numeradas de 1 a 7 e a narrativa refinada indica entre colchetes a questão respondida em cada trecho, com mais de uma referência quando o trecho responde a mais de uma questão, como **[5, 7]**. Os trechos que retomam a versão inicial ficam sem número. A marca **[NOVO]** saiu de C01.
>
> **⏭️ Fora desta revisão:** C02 e C03 continuam com **[NOVO]** e ficam com Lucas e Giovanni.
>
> \- Pedro

### 2. Garantir que cada questão investigue informação ausente do cenário inicial

A existência de uma pergunta por elemento atende à cobertura formal, mas não garante que todas sejam questões válidas de refinamento. É necessário conferir o conteúdo da versão inicial antes de formular cada uma.

Em C01, a pergunta sobre o que precisa estar pronto retoma o objetivo já apresentado de selecionar lances relevantes. A resposta acrescenta a necessidade de contexto suficiente para seguir à montagem; esse acréscimo é útil, mas a pergunta deve focalizar o critério ainda desconhecido, em vez de reapresentar o objetivo geral.

Em C02, o cenário inicial já informa que Arnaldo circula entre salas, acompanha editores e responde pelo conteúdo publicado. As perguntas sobre condições de trabalho e resultado final precisam distinguir esses dados conhecidos dos novos detalhes, como simultaneidade de demandas e critérios específicos de aprovação. Perguntar novamente pela situação ampla não deixa claro o que está sendo refinado.

Em C03, o equipamento limitado, o pouco armazenamento e o interesse por lances de um atleta já aparecem inicialmente. O refinamento pode explorar a organização de vários jogos, a estratégia de liberação de espaço e a forma de reconhecer uma seleção satisfatória. Há acréscimos efetivos na versão refinada; o problema é que algumas perguntas ainda são amplas demais para evidenciar a lacuna correspondente.

Revisem cada uma das sete perguntas de cada cenário. Mantenham pelo menos uma questão válida por elemento e verifiquem se sua resposta acrescenta informação que realmente não constava da narrativa inicial.

> **🟨 Tratado em parte** ([`3e7d960`](https://github.com/p4cs-974/projeto-ihc/commit/3e7d960), [`68a2bf2`](https://github.com/p4cs-974/projeto-ihc/commit/68a2bf2)): a tabela de C01 ganhou a coluna "Já informado na versão inicial", e cada questão parte do que a premissa não dizia. A questão 3 deixou de retomar o objetivo e passou a investigar o critério: lance relevante, corte aceitável (mostra a construção e o desfecho da jogada) e seleção de partida pronta. As questões 1 e 2 perguntam pelo que faltava: com quem e com que equipamento Rafael trabalha, o que depende da seleção e se a experiência explica a demora. As questões 4 a 7 foram reescritas no commit da correção 3.
>
> **⏭️ Fora desta revisão:** as perguntas de C02 e C03 ficam com Lucas e Giovanni.
>
> \- Pedro

### 3. Distinguir planejamento, ações, eventos e avaliação

A seção de elementos extraídos ajuda a reconhecer o método, mas algumas respostas do refinamento misturam categorias. O caso mais claro está em C02: a resposta à pergunta de **ações** descreve conhecimento das normas, experiência e autoridade para decidir. Isso caracteriza o ator e seu julgamento, mas não explica suficientemente o comportamento observável pelo qual ele aprova ou devolve um material.

A própria narrativa refinada oferece ações observáveis, como assistir a trechos, conversar, registrar pendências e ordenar a retirada de um vídeo. Usem essa precisão também na pergunta e na resposta de refinamento. Na linha de **eventos**, “aprovar às cegas” é uma ação de Arnaldo; a cobrança recebida, a chegada simultânea de solicitações ou a reação da audiência são acontecimentos externos que podem alterar a situação.

Em todos os cenários, diferenciem o plano que o personagem formula, aquilo que efetivamente faz e a avaliação que realiza depois de perceber uma situação. Por exemplo, descrever que alguém percorre as salas informa uma ação; explicar por que escolhe essa estratégia e como pretende distribuir sua atenção explicita planejamento. Essa distinção será necessária para modelar tarefas sem reduzir atividades cognitivas a uma lista de movimentos.

> **🟨 Tratado em parte** ([`68a2bf2`](https://github.com/p4cs-974/projeto-ihc/commit/68a2bf2)): em C01, o planejamento traz a decisão e o motivo (uma partida por vez para não acumular dúvidas, onde concentrar a atenção, por que adiar os candidatos duvidosos, H30). As ações são só comportamentos observáveis no editor. Os eventos passaram a ser acontecimentos externos: a pergunta de Arnaldo pelo chat que interrompe a busca, H41, e a reprodução do corte que começa no chute. A avaliação inclui o julgamento final. A tabela de elementos indica a questão de origem de cada linha, e o parágrafo seguinte explica a diferença com um exemplo do próprio cenário.
>
> **⏭️ Fora desta revisão:** a resposta de ações e a linha de eventos de C02 ficam com Lucas.
>
> \- Pedro

### 4. Manter as narrativas concretas sem transformar suposições em diagnóstico

C03 acrescenta muitos detalhes: tamanho elevado das gravações, aquecimento, esgotamento de memória, cache, corrupção do projeto e perdas de tempo. Detalhes hipotéticos podem enriquecer um cenário. O cuidado é não apresentar uma cadeia causal técnica específica como consequência inevitável de possuir um computador modesto.

Para esta análise, os sintomas percebidos pelo usuário e seus efeitos sobre a atividade são centrais: reprodução interrompida, dificuldade de identificar o atleta, fechamento inesperado, perda de trabalho e necessidade de refazer a seleção. Atribuir a ocorrência a uma causa técnica determinada exige fundamentação adicional ou uma indicação clara de que essa causa faz parte da situação fictícia adotada. A descrição do problema não depende de diagnosticar o computador.

Ajustem também a expressão de que o relato “reflete a realidade”, presente na apresentação de C03, para manter coerência com a declaração de cenário hipotético. Os tempos e volumes podem ser parâmetros narrativos, mas não devem ser reutilizados nas próximas entregas como medições obtidas com usuários. O mesmo cuidado vale para a sequência de reações da audiência e da direção em C02: é uma situação possível construída pela equipe, não um caso observado.

> **🟨 Tratado em parte** ([`19ea7c5`](https://github.com/p4cs-974/projeto-ihc/commit/19ea7c5)): as implicações de C01 dizem que a coleta testa a plausibilidade da situação sem confirmar o episódio, e que quantidades, durações e a sequência de acontecimentos são parâmetros narrativos, não medições. C01 não atribui causa técnica a nenhum problema.
>
> **⏭️ Fora desta revisão:** a cadeia causal técnica e o "reflete a realidade" de C03 ficam com Giovanni; as reações da audiência e da direção em C02 ficam com Lucas.
>
> \- Pedro

### 5. Derivar necessidades sem presumir que a solução já as resolve

As implicações estão separadas das narrativas, o que é adequado. Ainda assim, a ligação entre problema e solução precisa de limites mais claros, principalmente em C03.

O objetivo de localizar ações de um jogador não equivale automaticamente a receber os melhores momentos gerais de uma partida. A detecção de destaques pode omitir ações que interessam à compilação do personagem. O processamento remoto também não elimina, por si só, o armazenamento necessário para obter gravações e baixar resultados. Mantenham essas relações como questões de adequação e viabilidade, preservando H36 e H37 com seu caráter hipotético.

No encerramento de C03, a referência a receber lances já recortados aproxima o desfecho de uma solução específica. Centrem o fechamento na dificuldade de manter a produção, no retrabalho e no resultado insuficiente; discutam alternativas na seção de implicações.

C02, por sua vez, é válido para compreender o problema editorial mesmo com a participação externa de Arnaldo no produto proposto. Não é necessário inserir telas futuras para justificar o cenário. Esclareçam quais necessidades podem ser apoiadas pelos cortes e metadados entregues, sem presumir que o projeto passará a administrar toda a supervisão da emissora.

> **🟨 Tratado em parte** ([`0173b0c`](https://github.com/p4cs-974/projeto-ihc/commit/0173b0c)): as implicações de C01 listam três necessidades derivadas do problema, sem solução associada: localizar candidatos com menos esforço, preservar construção e desfecho e saber quanto da partida foi conferido. A ligação com A04 por R01 aparece como questão de adequação: a detecção automática pode omitir lances ou cortá-los sem a construção da jogada, e a revisão de cortes gerados pode deslocar o esforço em vez de reduzi-lo.
>
> **⏭️ Fora desta revisão:** H36, H37 e o encerramento de C03 ficam com Giovanni; as necessidades de C02 ficam com Lucas.
>
> \- Pedro

## Recomendações de melhoria

- Aproximem as versões iniciais de episódios concretos, com início, atividade e dificuldade identificáveis. Elas já são narrativas, mas algumas passagens descrevem a rotina de forma bastante geral. A versão refinada deverá aprofundar o mesmo episódio.

  > **🟨 Tratado em parte** ([`06dd91a`](https://github.com/p4cs-974/projeto-ihc/commit/06dd91a)): a versão inicial de C01 narra um dia de trabalho com início, atividade e dificuldade, sem antecipar o que as questões investigam. As de C02 e C03 ficam com Lucas e Giovanni.
  >
  > \- Pedro

- Evitem repetir adjetivos como “engessado” ou “caótico” quando o próprio acontecimento pode demonstrar o problema. A fila de decisões, as interrupções e o retrabalho comunicam melhor a dificuldade.

  > **ℹ️ Encaminhamento:** C01 não usa esses adjetivos; o problema aparece pela interrupção, pelo corte sem contexto e pelo retrabalho. "Engessado" e "caótico" estão em C02, que fica com Lucas.
  >
  > \- Pedro

- Façam cada desfecho indicar o que o personagem conseguiu, o que ficou pendente e como avaliou o resultado. Isso ajuda a distinguir objetivo, consequência e avaliação.

  > **🟨 Tratado em parte** ([`65bcb05`](https://github.com/p4cs-974/projeto-ihc/commit/65bcb05)): o desfecho de C01 diz o que Rafael conseguiu (cortes revisados e corrigidos, entregues a Arnaldo), o que ficou pendente (conferência dos trechos avançados) e como avalia o resultado (cortes compreensíveis, sem segurança sobre a cobertura). C02 e C03 ficam com Lucas e Giovanni.
  >
  > \- Pedro

- Atualizem as características das personas e do contexto quando novos detalhes narrativos forem adotados. Mantenham a origem hipotética e evitem atribuir à ficha anterior informações que foram introduzidas somente no refinamento.

  > **🟨 Tratado em parte** ([`daec541`](https://github.com/p4cs-974/projeto-ihc/commit/daec541)): C01 adota o contexto de P01 da Entrega 3 revisada: sala dividida com outros dois editores, seleção entregue no mesmo dia em uma pasta e aviso a Arnaldo pelo chat, que decide o que segue para a montagem (H39, H40 e H41). A ficha de P01 cita a estratégia atual detalhada em C01 como escolha narrativa do cenário. A sincronização de C02 com P02 e de C03 com P03 fica com Lucas e Giovanni.
  >
  > \- Pedro

## Pontos que devem alimentar as próximas entregas

C01 deve apoiar a análise das tarefas de localizar, selecionar e revisar lances, incluindo decisões diante de dúvidas e omissões. C02 deve contribuir para compreender o repasse de informações, os critérios de aprovação e a responsabilidade editorial. C03 deve alimentar a investigação sobre seleção temática por atleta, restrições de equipamento e continuidade do trabalho em ferramentas externas.

A investigação com usuários deverá testar a plausibilidade e a relevância dessas situações, sem precisar confirmar exatamente os episódios fictícios narrados. Registrem os aspectos a investigar em `RASTREABILIDADE.md` e mantenham separados o problema humano, as necessidades decorrentes e as alternativas de interação que serão elaboradas posteriormente.

> **🟨 Tratado em parte** ([`d696e16`](https://github.com/p4cs-974/projeto-ihc/commit/d696e16)): a matriz ganhou a seção 2.2, com os aspectos de C01 a investigar na Entrega 7, ligados às questões numeradas, às hipóteses e à tarefa afetada na Entrega 5. As implicações de C01 apontam para essa seção e separam problema, necessidades e alternativas. A tarefa de origem passou a ser localizar, selecionar e revisar lances, incluindo decisões diante de dúvidas e omissões. As linhas de C02 e C03 ficam com Lucas e Giovanni.
>
> \- Pedro

## Síntese das ações recomendadas

1. Numerar as questões dos três cenários e inserir as referências entre colchetes nos trechos que as respondem.
2. Revisar a novidade de cada pergunta, preservando pelo menos uma questão válida para cada um dos sete elementos.
3. Corrigir as distinções entre planejamento, ações, eventos e avaliação, especialmente no refinamento de C02.
4. Ajustar as afirmações causais e a apresentação de detalhes hipotéticos em C03.
5. Revisar as implicações e sincronizar cenários, personas, contexto e rastreabilidade.

> **Situação:** os cinco itens estão aplicados em C01, com registro no cabeçalho e na matriz ([`9fbbef5`](https://github.com/p4cs-974/projeto-ihc/commit/9fbbef5)). C02 e C03 ficam com Lucas e Giovanni (ver tabela no início).
>
> \- Pedro

De modo geral, considero que a equipe cumpriu a quantidade de cenários e construiu situações pertinentes, com versões refinadas que tornam os problemas mais compreensíveis. A entrega ainda precisa de revisão para atender ao processo de refinamento solicitado: as perguntas devem revelar lacunas reais, as respostas precisam ser localizáveis na narrativa e os elementos do método devem permanecer conceitualmente distintos. Com esses ajustes, o material poderá sustentar a análise de tarefas com mais clareza e coerência, sem depender de soluções antecipadas ou de benefícios presumidos.
