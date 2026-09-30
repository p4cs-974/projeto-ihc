# Feedback do Professor > Entrega 01 > Equipe 16


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

### 2. Diferenciar julgamento editorial de erro e de esforço operacional

**Natureza: problema conceitual de IHC. Seções 1.2, 1.4, 4.2, 4.4 e 9.1.**

A expressão “Redução da subjetividade”, na seção 9.1, reúne interpretação humana, cansaço e falhas como se fossem um único problema. Entretanto, a própria entrega atribui ao editor a decisão sobre quais cortes selecionar e baixar. É preciso distinguir uma omissão involuntária de uma escolha editorial deliberada.

Automatizar a detecção não demonstra, por si só, que os resultados serão mais adequados ao objetivo de uma compilação. A questão de IHC é compreender como o editor julga a utilidade do material e como a interface apoia esse julgamento. Caso contrário, o projeto corre o risco de tratar discordância com o sistema como erro do usuário.

Revisem o benefício pretendido e explicitem o que vocês desejam reduzir: esforço repetitivo, omissões por distração, retrabalho ou outro problema a investigar. Mantenham a redução de tempo e de falhas como hipóteses. Investiguem quais critérios tornam um lance relevante para a finalidade editorial, sem presumir que existe uma única seleção correta para todas as situações. A interface deve apoiar o editor; ela ainda não ganhou a última palavra sobre o jogo.

### 3. Completar a descrição do processo atual e das informações usadas nas decisões

**Natureza: atendimento parcial às perguntas da entrega e precisão conceitual. Seções 3.2, 4.1 e 4.3.**

A seção 4.1 apresenta plataformas de mercado e delimita a pós-produção, mas não descreve diretamente como o profissional do recorte escolhido trabalha hoje. A narrativa de H11 e a seção 6.1 já oferecem elementos para essa resposta; portanto, não há ausência completa do processo atual, mas uma articulação insuficiente entre as seções.

Retomem esse processo de forma breve em 4.1, identificando-o como hipótese enquanto não houver investigação: como o editor recebe o material, identifica trechos, decide limites e prepara a seleção. Na seção 3.2, esclareçam que processamento em lote e acompanhamento de estados são atividades previstas para a aplicação potencial. Isso evita apresentá-las como práticas atuais já conhecidas do público.

Em 4.3, “[F] Contexto da partida de futebol” é amplo demais para orientar a interação e não identifica a origem dessa afirmação sobre o trabalho do editor. Não se trata de uma simples definição interna do TCC. Explicitem quais informações vocês supõem que ele precisa interpretar e para qual decisão. Por exemplo, perguntem se conhecer o tipo de lance e observar o que ocorre antes e depois do trecho altera a seleção. São questões de investigação, não uma lista de requisitos já confirmados.

Sem essa ligação entre informação e decisão, a apresentação de timecodes, classificações e metadados pode acabar reproduzindo a saída técnica do modelo sem demonstrar sua utilidade para o usuário.

### 4. Separar benefício técnico, benefício de uso e conhecimento do usuário

**Natureza: problema conceitual e consistência entre registros. Seções 1.5, 2.4 e 9.1; hipótese H05.**

Na segunda linha de 1.5, “Evidenciar a capacidade de generalização do conhecimento e aplicabilidade dos modelos de linguagem” continua descrevendo uma contribuição técnica ou científica. Ainda não explica o valor em uso para o editor. A equipe deve refletir sobre qual atividade humana poderia ser favorecida por essa capacidade e registrar a relação como hipótese, quando aplicável. Não é necessário inventar um benefício diferente para cada tecnologia.

Também é preciso tornar H05 mais precisa. “Baixo conhecimento técnico de software e computação” pode sugerir pouca familiaridade com ferramentas digitais, enquanto H17 prevê experiência com softwares de edição. Essas hipóteses não são necessariamente incompatíveis: alguém pode dominar edição e desconhecer programação ou modelos de IA.

A matriz já registra esse refinamento de H05, mas ele não aparece com a mesma clareza em 2.4. Atualizem a formulação, preservando seu caráter hipotético. Essa distinção afeta linguagem, ajuda e controles: simplificar termos internos do modelo não significa tratar o editor como iniciante em sua profissão.

### 5. Harmonizar responsabilidades e identificadores com o recorte adotado

**Natureza: consistência documental e rastreabilidade. Seções 0.1, 8 e 9.2; seção 4 da matriz.**

A divisão de responsabilidades inclui “Tela de Logs/Rastreabilidade”, mas a seção 8 exclui logs técnicos do fluxo do editor e mantém histórico e busca como possibilidades a validar. Esclareçam se essa responsabilidade se refere ao estudo do histórico de trabalhos e mensagens de estado, à manutenção documental da rastreabilidade ou a outra atividade. A divisão de tarefas não deve consolidar uma tela antes de sua necessidade estar justificada.

Há também uma colisão concreta de identificadores. Na seção 9.2, F01 significa envio de vídeos; na tabela de padrões da matriz, F01 significa dashboard. F02 e F03 igualmente designam coisas diferentes nos dois documentos. Além disso, a matriz ainda contém exemplos com `{{...}}`, incluindo administração/CRUD, que está fora do recorte inicial.

Identifiquem essas linhas como exemplos não adotados ou substituam-nas por registros coerentes, preservando `PENDENTE` para relações ainda não construídas. Diferenciem os identificadores das ações daqueles das telas ou explicitem sua correspondência. Não se exige desenhar telas, produzir MoLIC ou preencher modelos futuros agora; exige-se evitar que um exemplo do template seja confundido com decisão da equipe.

## Recomendações de melhoria

- **Consolidar os stakeholders já mencionados.** A seção 2.3 lista empresas de mídia esportiva, enquanto 5.4 e 7.1 acrescentam produtores e responsáveis editoriais como destinatários e decisores externos. Reunir esses papéis tornaria a visão das pessoas mais consistente, sem criar novos usuários diretos ou telas de aprovação.
- **Distinguir frequência, prioridade e criticidade.** A04 tem hipótese de maior frequência e prioridade alta, enquanto H08 aponta o processamento em lote como mais crítico. Isso pode ser coerente, mas expliquem a diferença. A justificativa de H07 informa para que os resultados serão usados, sem sustentar ainda por que essa seria a atividade mais frequente. Não são necessários números inventados.
- **Delimitar “perda de arquivos”.** Em H08, esclareçam se vocês se referem a perda do original, indisponibilidade dos resultados ou necessidade de repetir o processamento. Essas situações produzem consequências diferentes e não devem ser presumidas indistintamente.
- **Preservar a incerteza nas sínteses.** As seções 11 e 13 resumem como estabelecido um processo que continua hipotético. Uma indicação de que se trata do recorte inicial ajuda a evitar que a comunicação pública transforme hipóteses em fatos. A existência de alternativas automatizadas também recomenda restringir H01 ao público e ao contexto investigados, sem generalizar toda a produção de melhores momentos.
- **Não transformar impacto possível em capacidade assegurada.** A seção 9.3 propõe estimativas de progresso e indicação de quando houve custo. Registrem o que o TCC realmente fornece e o que ainda precisa ser investigado para comunicar essas informações de maneira confiável. A definição técnica interna pode ser aceita como tal; sua implicação para o usuário precisa de justificativa.
- **Registrar acessibilidade como questão a investigar.** A seção 2.4 pode explicitar o desconhecimento sobre necessidades que afetem leitura, navegação e inspeção de vídeos. O capítulo 3 relaciona qualidade de uso às características e ao contexto das pessoas; não é preciso produzir uma avaliação completa de acessibilidade nesta etapa.
- **Identificar a revisão do documento.** A data de 13/08/2026 convive com mudanças posteriores registradas na matriz. Preservem a data original e acrescentem, se pertinente, a data de revisão. Isso facilita compreender qual versão está sendo avaliada.

## Pontos que devem alimentar as próximas entregas

Os encaminhamentos abaixo orientam a continuidade; não são artefatos adicionais exigidos para concluir a Entrega 01.

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

**Parecer geral:** A Entrega 01 demonstra compreensão satisfatória da passagem de uma contribuição técnica para um projeto de IHC e apresenta um recorte pertinente, delimitado e viável para a disciplina. O trabalho oferece uma base adequada para continuidade, mas precisa de revisão pontual da sustentação documental e de alguns conceitos antes de ser considerado plenamente consolidado. Preservando o foco no editor e corrigindo a relação entre evidências, julgamento humano, benefícios e rastreabilidade, a equipe terá melhores condições de justificar as próximas decisões de interação sem ampliar desnecessariamente o projeto ou tratar resultados automáticos como garantia de qualidade editorial.
