# Feedback do Professor > Entrega 01 > Equipe 16

> **Status da aplicação (02/10/2026):** todas as correções prioritárias e recomendações deste parecer foram aplicadas na branch `aplicar-feedback`. Cada comentário abaixo traz uma anotação **✅ Como foi tratado** com o link para o commit correspondente. O texto original do professor foi preservado; as anotações aparecem em blocos de citação logo após cada item.
>
> | Item do parecer | Commit(s) |
> |---|---|
> | Correção 1 — referências, afirmações e limitações (4.6) | [`81c38a0`](https://github.com/p4cs-974/projeto-ihc/commit/81c38a0) |
> | Correção 2 — julgamento editorial × erro × esforço | [`51d6d90`](https://github.com/p4cs-974/projeto-ihc/commit/51d6d90) |
> | Correção 3 — processo atual e informações das decisões | [`86eeb39`](https://github.com/p4cs-974/projeto-ihc/commit/86eeb39) |
> | Correção 4 — benefício técnico × de uso; H05 | [`1d88573`](https://github.com/p4cs-974/projeto-ihc/commit/1d88573), [`ae39933`](https://github.com/p4cs-974/projeto-ihc/commit/ae39933) |
> | Correção 5 — responsabilidades e identificadores | [`7366be7`](https://github.com/p4cs-974/projeto-ihc/commit/7366be7) |
> | Recomendação — stakeholders | [`faab8d7`](https://github.com/p4cs-974/projeto-ihc/commit/faab8d7) |
> | Recomendação — frequência, prioridade e criticidade | [`c4b5c99`](https://github.com/p4cs-974/projeto-ihc/commit/c4b5c99) |
> | Recomendação — "perda de arquivos" | [`62b20ff`](https://github.com/p4cs-974/projeto-ihc/commit/62b20ff) |
> | Recomendação — incerteza nas sínteses | [`a48af73`](https://github.com/p4cs-974/projeto-ihc/commit/a48af73) |
> | Recomendação — impacto possível × capacidade assegurada | [`d6d008e`](https://github.com/p4cs-974/projeto-ihc/commit/d6d008e) |
> | Recomendação — acessibilidade | [`de14e9f`](https://github.com/p4cs-974/projeto-ihc/commit/de14e9f) |
> | Recomendação — data de revisão | [`e834ef6`](https://github.com/p4cs-974/projeto-ihc/commit/e834ef6) |


## Avaliação geral

A equipe apresenta uma base consistente para o projeto de IHC. O trabalho identifica uma contribuição técnica, escolhe um usuário plausível e delimita um fluxo compreensível: enviar partidas gravadas, acompanhar o processamento, revisar os resultados e baixar cortes e metadados para continuar a produção em ferramentas externas. A distinção entre o backend previsto no TCC e o protótipo demonstrativo da disciplina está clara.

A entrega atende amplamente à estrutura solicitada e demonstra cuidado em registrar hipóteses e lacunas. As principais revisões estão na confiabilidade da tabela de evidências, na compreensão do julgamento editorial e na consistência entre informações distribuídas pelo documento. O problema central não é a falta de telas ou de implementação: é tornar mais precisa a justificativa das decisões que orientarão essas telas posteriormente.

Esta atividade exige uma solução consolidada por equipe. Os três integrantes estão identificados; não há exigência de três entregas individuais nesta etapa. A matriz contém registros posteriores, inclusive de personas e cenários, mas esses artefatos não são avaliados neste parecer nem considerados comprovação empírica das hipóteses iniciais. Também não se exige pesquisa com usuários já concluída na Entrega 01.


## Pontos positivos

- **Transferência da contribuição técnica para uma situação de uso.** As seções 7.1 a 7.4 explicam quem utilizaria os resultados, com que objetivo e em qual contexto. O editor não aparece apenas como alguém que “usa o algoritmo”.
- **Recorte viável e limites explícitos.** Edição detalhada, publicação, parâmetros técnicos do modelo e administração de usuários permanecem fora do escopo. Essa delimitação permite aprofundar a interação central durante o semestre.
- **Situação concreta centrada no problema.** H11, na seção 4.5, apresenta pessoa, atividade, pressão de prazo, dificuldade e consequência sem transformar a narrativa em propaganda da futura solução.
- **Reconhecimento de incertezas.** Local de trabalho, dispositivos, papéis organizacionais, formatos e limites de arquivos aparecem como questões abertas. Na seção 6.5, vocês corretamente evitam inventar defeitos de usabilidade dos concorrentes.
- **Atenção à compreensão e à recuperação de falhas.** H25 e H26 contemplam resultados vazios, cortes incorretos, interrupções e indisponibilidade de download. A seção 5.6 reconhece que o resultado automático não deve ser apresentado como editorialmente infalível.
- **Padrões tratados como possibilidades.** Dashboard, filtros e alertas aparecem com objetivos e hipóteses associados, sem serem adotados automaticamente. A diferenciação entre histórico compreensível e logs técnicos também é pertinente.
- **Rastreabilidade inicial existente.** H01–H29 estão registradas na matriz, com estado e encaminhamento. A matriz distingue refinamentos de projeto de validação empírica, cuidado que deve ser preservado.

## Correções prioritárias

### 1. Corrigir a correspondência entre referências, afirmações e limitações

**Natureza: conformidade com o registro de evidências e consistência da argumentação. Seção 4.6.**

A tabela apresenta incompatibilidades internas que precisam ser conferidas. A referência de Yin, Sinnott e Jayaputra é identificada como um artigo de revisão em periódico, mas sua limitação diz “Fonte institucional e promocional”. A referência de Seweryn, Wróblewska e Łukasik também é apresentada como artigo de revisão, enquanto a limitação afirma “Fonte institucional e comercial”. Já a linha de Akan e Varlı associa um levantamento bibliográfico a um “estudo acadêmico com 25 partidas”, sem esclarecer a origem desse recorte.

Isso não permite concluir, por si só, que os artigos estejam errados ou que não discutam os temas indicados. Permite concluir que a tabela não torna verificável qual fonte sustenta cada afirmação. Se um artigo relata outro estudo, essa relação também precisa estar explícita.

A equipe precisa conferir cada linha e manter alinhados: referência efetivamente consultada, afirmação sustentada e limitação correspondente. Se uma informação veio das páginas de WSC Sports ou Magnifi, registrem essas páginas na linha apropriada. Se veio de um artigo, indiquem a passagem ou seção relevante como apoio à revisão. A alegação sobre as 25 partidas deve ter sua origem esclarecida ou deixar de ser apresentada como evidência estabelecida.

Essa correção é prioritária porque uma associação documental incorreta pode sustentar decisões sobre usuários e atividades com uma evidência que trata de outro assunto. Não é necessário ampliar a revisão bibliográfica agora; é necessário corrigir a relação entre o que já foi citado e o que se afirma a partir disso.

> **✅ Como foi tratado** ([`81c38a0`](https://github.com/p4cs-974/projeto-ihc/commit/81c38a0)): a tabela da seção 4.6 ganhou a coluna "Tipo de fonte". As três referências acadêmicas foram mantidas como artigos de revisão, e suas limitações deixaram de dizer "fonte institucional/promocional": agora descrevem o foco técnico de cada levantamento. A origem do recorte de 25 partidas foi esclarecida: trata-se de um estudo relatado pelo próprio survey de Akan e Varlı, usado como referência indireta, não como coleta dos autores nem como evidência sobre editores. As afirmações sobre funcionalidades da WSC Sports e da Magnifi passaram a citar as páginas oficiais em linhas próprias, com a limitação de fonte promocional e a remissão às análises C06 e C07 da Entrega 2. Uma nota abaixo da tabela explicita qual tipo de fonte sustenta cada tipo de afirmação. A bibliografia não foi ampliada.

### 2. Diferenciar julgamento editorial de erro e de esforço operacional

**Natureza: problema conceitual de IHC. Seções 1.2, 1.4, 4.2, 4.4 e 9.1.**

A expressão “Redução da subjetividade”, na seção 9.1, reúne interpretação humana, cansaço e falhas como se fossem um único problema. Entretanto, a própria entrega atribui ao editor a decisão sobre quais cortes selecionar e baixar. É preciso distinguir uma omissão involuntária de uma escolha editorial deliberada.

Automatizar a detecção não demonstra, por si só, que os resultados serão mais adequados ao objetivo de uma compilação. A questão de IHC é compreender como o editor julga a utilidade do material e como a interface apoia esse julgamento. Caso contrário, o projeto corre o risco de tratar discordância com o sistema como erro do usuário.

Revisem o benefício pretendido e explicitem o que vocês desejam reduzir: esforço repetitivo, omissões por distração, retrabalho ou outro problema a investigar. Mantenham a redução de tempo e de falhas como hipóteses. Investiguem quais critérios tornam um lance relevante para a finalidade editorial, sem presumir que existe uma única seleção correta para todas as situações. A interface deve apoiar o editor; ela ainda não ganhou a última palavra sobre o jogo.

> **✅ Como foi tratado** ([`51d6d90`](https://github.com/p4cs-974/projeto-ihc/commit/51d6d90)): "Redução da subjetividade" foi removida da seção 9.1. A tabela agora separa economia de tempo, redução do esforço repetitivo, redução de omissões involuntárias e retrabalho, e apoio ao julgamento editorial sem substituí-lo. H01 (1.2), H02 (1.4), H09 (4.2) e H10 (4.4) foram reescritas para distinguir omissão involuntária de descarte editorial deliberado; H10 afirma que a divergência entre o editor e uma sugestão automática não é erro do usuário. Em 4.2 foi registrada a lacuna `[?]` sobre os critérios que tornam um lance relevante para cada compilação, sem presumir uma seleção única correta. A redução de tempo e de falhas continua como hipótese. As mesmas formulações foram levadas à seção 10 e à matriz.

### 3. Completar a descrição do processo atual e das informações usadas nas decisões

**Natureza: atendimento parcial às perguntas da entrega e precisão conceitual. Seções 3.2, 4.1 e 4.3.**

A seção 4.1 apresenta plataformas de mercado e delimita a pós-produção, mas não descreve diretamente como o profissional do recorte escolhido trabalha hoje. A narrativa de H11 e a seção 6.1 já oferecem elementos para essa resposta; portanto, não há ausência completa do processo atual, mas uma articulação insuficiente entre as seções.

Retomem esse processo de forma breve em 4.1, identificando-o como hipótese enquanto não houver investigação: como o editor recebe o material, identifica trechos, decide limites e prepara a seleção. Na seção 3.2, esclareçam que processamento em lote e acompanhamento de estados são atividades previstas para a aplicação potencial. Isso evita apresentá-las como práticas atuais já conhecidas do público.

Em 4.3, “[F] Contexto da partida de futebol” é amplo demais para orientar a interação e não identifica a origem dessa afirmação sobre o trabalho do editor. Não se trata de uma simples definição interna do TCC. Explicitem quais informações vocês supõem que ele precisa interpretar e para qual decisão. Por exemplo, perguntem se conhecer o tipo de lance e observar o que ocorre antes e depois do trecho altera a seleção. São questões de investigação, não uma lista de requisitos já confirmados.

Sem essa ligação entre informação e decisão, a apresentação de timecodes, classificações e metadados pode acabar reproduzindo a saída técnica do modelo sem demonstrar sua utilidade para o usuário.

> **✅ Como foi tratado** ([`86eeb39`](https://github.com/p4cs-974/projeto-ihc/commit/86eeb39)): a seção 4.1 passou a descrever o processo atual como **detalhamento hipotético de H11**, em quatro passos: receber o material, identificar trechos, decidir limites e preparar a seleção, com validação prevista para a Entrega 7. A seção 3.2 ganhou uma nota esclarecendo que A01–A04 são atividades da aplicação potencial, não práticas atuais conhecidas. Na seção 4.3, "[F] Contexto da partida de futebol" foi substituído por uma tabela que liga cada informação suposta (tipo de lance, o que acontece antes e depois, placar e minuto, jogadores, finalidade da compilação) à decisão que apoiaria, com status `[H]`/`[?]` e a pergunta a investigar. A matriz registra o detalhamento em H11.

### 4. Separar benefício técnico, benefício de uso e conhecimento do usuário

**Natureza: problema conceitual e consistência entre registros. Seções 1.5, 2.4 e 9.1; hipótese H05.**

Na segunda linha de 1.5, “Evidenciar a capacidade de generalização do conhecimento e aplicabilidade dos modelos de linguagem” continua descrevendo uma contribuição técnica ou científica. Ainda não explica o valor em uso para o editor. A equipe deve refletir sobre qual atividade humana poderia ser favorecida por essa capacidade e registrar a relação como hipótese, quando aplicável. Não é necessário inventar um benefício diferente para cada tecnologia.

Também é preciso tornar H05 mais precisa. “Baixo conhecimento técnico de software e computação” pode sugerir pouca familiaridade com ferramentas digitais, enquanto H17 prevê experiência com softwares de edição. Essas hipóteses não são necessariamente incompatíveis: alguém pode dominar edição e desconhecer programação ou modelos de IA.

A matriz já registra esse refinamento de H05, mas ele não aparece com a mesma clareza em 2.4. Atualizem a formulação, preservando seu caráter hipotético. Essa distinção afeta linguagem, ajuda e controles: simplificar termos internos do modelo não significa tratar o editor como iniciante em sua profissão.

> **✅ Como foi tratado** ([`1d88573`](https://github.com/p4cs-974/projeto-ihc/commit/1d88573), [`ae39933`](https://github.com/p4cs-974/projeto-ihc/commit/ae39933)): na seção 1.5, a generalização dos LLMs foi movida para a coluna de mérito técnico/científico. O valor em uso virou hipótese ligada a uma atividade do editor: localizar e filtrar cortes por tipo de lance, relacionada a H02 e H28 e condicionada aos critérios da seção 4.3. Uma nota explica a distinção. H05 foi reformulada em 2.4, na seção 10 e na matriz: "o editor domina ferramentas de edição de vídeo, mas tem pouco ou nenhum conhecimento de programação, de modelos de IA e de parâmetros de inferência". A matriz preserva a versão original, e o texto observa que simplificar termos do modelo não significa tratar o editor como iniciante.

### 5. Harmonizar responsabilidades e identificadores com o recorte adotado

**Natureza: consistência documental e rastreabilidade. Seções 0.1, 8 e 9.2; seção 4 da matriz.**

A divisão de responsabilidades inclui “Tela de Logs/Rastreabilidade”, mas a seção 8 exclui logs técnicos do fluxo do editor e mantém histórico e busca como possibilidades a validar. Esclareçam se essa responsabilidade se refere ao estudo do histórico de trabalhos e mensagens de estado, à manutenção documental da rastreabilidade ou a outra atividade. A divisão de tarefas não deve consolidar uma tela antes de sua necessidade estar justificada.

Há também uma colisão concreta de identificadores. Na seção 9.2, F01 significa envio de vídeos; na tabela de padrões da matriz, F01 significa dashboard. F02 e F03 igualmente designam coisas diferentes nos dois documentos. Além disso, a matriz ainda contém exemplos com `{{...}}`, incluindo administração/CRUD, que está fora do recorte inicial.

Identifiquem essas linhas como exemplos não adotados ou substituam-nas por registros coerentes, preservando `PENDENTE` para relações ainda não construídas. Diferenciem os identificadores das ações daqueles das telas ou explicitem sua correspondência. Não se exige desenhar telas, produzir MoLIC ou preencher modelos futuros agora; exige-se evitar que um exemplo do template seja confundido com decisão da equipe.

> **✅ Como foi tratado** ([`7366be7`](https://github.com/p4cs-974/projeto-ihc/commit/7366be7)): na seção 0.1 e no README, as responsabilidades deixaram de ser telas e passaram a ser atividades: Pedro com o envio de partidas (A01); Lucas com revisão, seleção e download (A04); Giovanni com acompanhamento e histórico de processamento (A02/A03) e manutenção da matriz de rastreabilidade. Uma nota esclarece que logs técnicos seguem fora do fluxo do editor. As ações da seção 9.2 deixaram de usar F01–F04 e adotaram os mesmos IDs das atividades (A01–A04); os IDs `F` ficam reservados às telas da Entrega 11. Na seção 4 da matriz, as linhas `{{...}}` foram substituídas: dashboard e histórico ficaram `PENDENTE`, ligados a A02/A03 e H29/H15, e administração/CRUD foi marcada como "não adotado". Uma nota registra o conteúdo anterior.

## Recomendações de melhoria

- **Consolidar os stakeholders já mencionados.** A seção 2.3 lista empresas de mídia esportiva, enquanto 5.4 e 7.1 acrescentam produtores e responsáveis editoriais como destinatários e decisores externos. Reunir esses papéis tornaria a visão das pessoas mais consistente, sem criar novos usuários diretos ou telas de aprovação.

  > **✅ Como foi tratado** ([`faab8d7`](https://github.com/p4cs-974/projeto-ihc/commit/faab8d7)): a seção 2.3 passou a reunir organizações (H04/H20) e produtores e responsáveis editoriais (H14/H22/H23) como destinatários e decisores externos, com nota remetendo à P02 da Entrega 3. Nenhum usuário direto nem tela de aprovação foi criado.
- **Distinguir frequência, prioridade e criticidade.** A04 tem hipótese de maior frequência e prioridade alta, enquanto H08 aponta o processamento em lote como mais crítico. Isso pode ser coerente, mas expliquem a diferença. A justificativa de H07 informa para que os resultados serão usados, sem sustentar ainda por que essa seria a atividade mais frequente. Não são necessários números inventados.

  > **✅ Como foi tratado** ([`c4b5c99`](https://github.com/p4cs-974/projeto-ihc/commit/c4b5c99)): a seção 3.4 define frequência, criticidade e prioridade e explica por que A04 pode ser a mais frequente e A01 a mais crítica sem contradição. A tabela 3.2 foi alinhada a H07/H08. Em 3.3, a equipe admite que a finalidade dos resultados não sustenta sozinha a frequência e registra o raciocínio provisório, sem números inventados.
- **Delimitar “perda de arquivos”.** Em H08, esclareçam se vocês se referem a perda do original, indisponibilidade dos resultados ou necessidade de repetir o processamento. Essas situações produzem consequências diferentes e não devem ser presumidas indistintamente.

  > **✅ Como foi tratado** ([`62b20ff`](https://github.com/p4cs-974/projeto-ihc/commit/62b20ff)): H08 (seção 3.4) desdobra "perda de arquivos" em perda do original, indisponibilidade dos resultados e reprocessamento, cada uma com sua consequência, e deixa como lacuna `[?]` se o editor mantém cópia local. Seção 10 e matriz atualizadas.
- **Preservar a incerteza nas sínteses.** As seções 11 e 13 resumem como estabelecido um processo que continua hipotético. Uma indicação de que se trata do recorte inicial ajuda a evitar que a comunicação pública transforme hipóteses em fatos. A existência de alternativas automatizadas também recomenda restringir H01 ao público e ao contexto investigados, sem generalizar toda a produção de melhores momentos.

  > **✅ Como foi tratado** ([`a48af73`](https://github.com/p4cs-974/projeto-ihc/commit/a48af73)): as linhas da seção 11 sobre usuário, problema, processo atual e contexto passaram a ser marcadas `[H]` e a citar as hipóteses de origem. O item 1 da seção 13 passou a falar em "recorte inicial que estamos investigando", com nota contra apresentar o problema como fato em comunicação pública. H01 foi restringida a editores na pós-produção de partidas encerradas, com menção explícita às alternativas automatizadas da seção 6.1, em 1.2, na seção 10 e na matriz.
- **Não transformar impacto possível em capacidade assegurada.** A seção 9.3 propõe estimativas de progresso e indicação de quando houve custo. Registrem o que o TCC realmente fornece e o que ainda precisa ser investigado para comunicar essas informações de maneira confiável. A definição técnica interna pode ser aceita como tal; sua implicação para o usuário precisa de justificativa.

  > **✅ Como foi tratado** ([`d6d008e`](https://github.com/p4cs-974/projeto-ihc/commit/d6d008e)): a seção 9.3 ganhou uma nota que aceita a definição técnica e trata sua implicação para o usuário como hipótese. As linhas de processamento e custo agora separam o que o TCC fornece (estados de execução) do que ainda precisa ser investigado: progresso parcial, estimativa confiável de duração e medição/atribuição do custo. Sem essas informações, a interface comunica apenas estados, sem prometer porcentagens ou prazos.
- **Registrar acessibilidade como questão a investigar.** A seção 2.4 pode explicitar o desconhecimento sobre necessidades que afetem leitura, navegação e inspeção de vídeos. O capítulo 3 relaciona qualidade de uso às características e ao contexto das pessoas; não é preciso produzir uma avaliação completa de acessibilidade nesta etapa.

  > **✅ Como foi tratado** ([`de14e9f`](https://github.com/p4cs-974/projeto-ihc/commit/de14e9f)): a seção 2.4 ganhou uma lacuna `[?]` sobre necessidades que afetem leitura, navegação e inspeção de vídeos, encaminhada à Entrega 7, sem avaliação completa de acessibilidade nesta etapa.
- **Identificar a revisão do documento.** A data de 13/08/2026 convive com mudanças posteriores registradas na matriz. Preservem a data original e acrescentem, se pertinente, a data de revisão. Isso facilita compreender qual versão está sendo avaliada.

  > **✅ Como foi tratado** ([`e834ef6`](https://github.com/p4cs-974/projeto-ihc/commit/e834ef6)): o cabeçalho preserva a data de 13/08/2026 como versão original e acrescenta "Revisão: 02/10/2026" com link para este parecer. A aplicação do feedback foi registrada no registro de mudanças de escopo (seção 5) e no histórico da matriz.

## Pontos que devem alimentar as próximas entregas

Os encaminhamentos abaixo orientam a continuidade; não são artefatos adicionais exigidos para concluir a Entrega 01.

> **ℹ️ Encaminhamento:** esta tabela não exige alteração na Entrega 01. Os pontos serão retomados nas entregas indicadas. As hipóteses citadas continuam abertas na [matriz de rastreabilidade](../RASTREABILIDADE.md), com as reformulações feitas nesta revisão.

| Etapa | Questão a retomar | Ligação com a Entrega 01 |
|---|---|---|
| Entrega 02 - alternativas | Diferenciar funcionalidades anunciadas, interação efetivamente observada e adequação ainda desconhecida ao editor escolhido. | Seção 6; H17–H20. |
| Entregas 03 e 04 - perfis e situações | Refinar experiência em edição, responsabilidade editorial, pressão de prazo e processo atual, preservando o caráter hipotético quando não houver dados. | H03, H05, H11, H12, H14 e H27. |
| Entregas 05 e 06 - tarefas e exploração | Relacionar envio, acompanhamento e revisão ao objetivo de obter material aproveitável; explorar falhas e retomada sem ampliar automaticamente o escopo. | A01–A04; H07, H08, H15, H25 e H26. |
| Entrega 07 - investigação | Investigar como profissionais selecionam lances, o que precisam conferir, como lidam com omissões e quais termos compreendem. | H01, H05, H09–H11, H17, H19 e H28. |
| Entrega 08 - metas de usabilidade | Transformar os benefícios esperados em critérios observáveis, distinguindo qualidade da interação de desempenho do detector. | H02 e seção 9.1. |
| Entregas 12–14 - avaliação | Verificar compreensão dos estados e resultados, seleção do material desejado e recuperação diante de falhas; avaliar ganhos de uso com tarefas e critérios definidos. | H02, H16, H25 e H26. |

Personas, cenários e análise de concorrentes ajudam a organizar e refinar hipóteses, mas não comprovam sozinhos o comportamento do público. Da mesma forma, uma entrevista pode investigar a expectativa de economia de tempo; demonstrar essa economia exige observação ou comparação adequada em etapa posterior. O capítulo 7 oferece a base para planejar essas investigações, e o capítulo 8 ajuda a representar seus resultados sem confundir elaboração de modelos com evidência empírica.

## Síntese das ações recomendadas

1. Conferir a tabela 4.6 e corrigir a associação entre cada referência, afirmação e limitação.
2. Rever “redução da subjetividade”, separando julgamento editorial, omissão involuntária e esforço repetitivo.
3. Articular processo atual e atividades futuras; especificar as informações e decisões de 4.3, com classificação adequada.
4. Ajustar o valor em uso em 1.5 e atualizar H05 sem presumir inexperiência em edição.
5. Harmonizar a responsabilidade por logs/histórico e eliminar ambiguidades dos identificadores F01–F03 e dos exemplos da matriz.
6. Manter as hipóteses abertas e encaminhadas às etapas pertinentes, sem antecipar telas, modelos ou validações que ainda não são exigidos.

> **✅ Como foi tratado:** itens 1 a 5 correspondem às correções prioritárias 1 a 5 acima ([`81c38a0`](https://github.com/p4cs-974/projeto-ihc/commit/81c38a0), [`51d6d90`](https://github.com/p4cs-974/projeto-ihc/commit/51d6d90), [`86eeb39`](https://github.com/p4cs-974/projeto-ihc/commit/86eeb39), [`1d88573`](https://github.com/p4cs-974/projeto-ihc/commit/1d88573), [`7366be7`](https://github.com/p4cs-974/projeto-ihc/commit/7366be7)). Item 6: nenhuma hipótese foi marcada como validada; todas as reformulações mantêm `[H]`/`[?]` e estado "aberta" na matriz. Nenhuma tela, MoLIC ou modelo futuro foi antecipado: as linhas de padrões de interface continuam `PENDENTE`.

**Parecer geral:** A Entrega 01 demonstra compreensão satisfatória da passagem de uma contribuição técnica para um projeto de IHC e apresenta um recorte pertinente, delimitado e viável para a disciplina. O trabalho oferece uma base adequada para continuidade, mas precisa de revisão pontual da sustentação documental e de alguns conceitos antes de ser considerado plenamente consolidado. Preservando o foco no editor e corrigindo a relação entre evidências, julgamento humano, benefícios e rastreabilidade, a equipe terá melhores condições de justificar as próximas decisões de interação sem ampliar desnecessariamente o projeto ou tratar resultados automáticos como garantia de qualidade editorial.
