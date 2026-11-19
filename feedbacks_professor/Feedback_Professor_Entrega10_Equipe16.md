# Feedback do Professor > Entrega 10 > Equipe 16

> **Status da aplicação (18/11/2026).** A revisão cobre os recortes individuais e a consolidação da equipe. [?] As apresentações, a confirmação de cada autor e a validação com usuários seguem pendentes.
>
> | Item do parecer | Situação | Commit |
> |---|---|---|
> | Correção 1 · Abertura e fechamento do objetivo | Aplicada | [`8ffb4ad`](https://github.com/p4cs-974/projeto-ihc/commit/8ffb4adaa66db415f65dcd40da43dd7bd9e4e635) |
> | Correção 2 · Estrutura de M03 | Aplicada | [`eb8379f`](https://github.com/p4cs-974/projeto-ihc/commit/eb8379fa4ce2732c3a6a36e87da764c3774205c6) |
> | Correção 3 · Emissores no M03 | Aplicada | [`153e585`](https://github.com/p4cs-974/projeto-ihc/commit/153e585b37b3c7efb8da4c77f6cfc40733d57464) |
> | Correção 4 · Coerência entre M03 e Entrega 9 | Aplicada | [`4a1b9e6`](https://github.com/p4cs-974/projeto-ihc/commit/4a1b9e66bebd6d700b0c73625fc4482b3cace418) |
> | Correção 5 · Alertas e acessos | Aplicada | [`3e0e56f`](https://github.com/p4cs-974/projeto-ihc/commit/3e0e56fb098bfac4c7595537dd3bbc42f0b79b9c) |
> | Recomendação 1 · Leitura das cenas de M01 e M02 | Aplicada | [`9cf1f13`](https://github.com/p4cs-974/projeto-ihc/commit/9cf1f1395d527b4c3a0c034333856a77ebf3f58b) |
> | Recomendação 2 · Sucesso e pendência | Aplicada | [`c949829`](https://github.com/p4cs-974/projeto-ihc/commit/c949829854ddcd1de36422b1211c90c188cacb11) |
> | Recomendação 3 · Linguagem gráfica de M03 | Aplicada | [`1aed092`](https://github.com/p4cs-974/projeto-ihc/commit/1aed09291761c2f0aa80b16fcd1c62be2ebb5694) |
> | Recomendação 4 · Status e checklists | Parcial | [`a794201`](https://github.com/p4cs-974/projeto-ihc/commit/a79420121d65e41a2b6088488d397a043caaa40d) |
> | Próximas entregas 1 · Estados no protótipo | Parcial | [`a14f442`](https://github.com/p4cs-974/projeto-ihc/commit/a14f442f5c8f64e22609f70880fbac00173c094b) |
> | Próximas entregas 2 · Seleção, obtenção e decisão editorial | Aplicada | [`41f685d`](https://github.com/p4cs-974/projeto-ihc/commit/41f685d99c082be28428caaa4499dd4afb5a9a96) |
> | Próximas entregas 3 · Limites de escopo | Aplicada | [`8727e28`](https://github.com/p4cs-974/projeto-ihc/commit/8727e28ea50f729047c2bb36385d78942650bbd0) |
> | Próximas entregas 4 · Retomada limitada | Aplicada | [`a5c1bc3`](https://github.com/p4cs-974/projeto-ihc/commit/a5c1bc3c6410c5f17390f060010109e76c19fb99) |
>
> \- Pedro

A equipe entregou três modelos, um para cada integrante, com autoria, matrícula, cenário, tarefa, objetivos e signos declarados. Portanto, a quantidade mínima foi atendida e não se aplica divisão da nota por um único diagrama coletivo. M01 e M02 apresentam uma modelagem consistente da conversa entre usuário e sistema e usam adequadamente cenas, processamentos, aberturas, encerramentos e caminhos de ruptura. M03 foi entregue, mas permanece incompleto e traz inconsistências formais e de escopo já reconhecidas pela própria documentação. A principal falha comum aos três modelos é a ausência das marcações GCO e GCC.

## Pontos positivos

- A responsabilidade individual está clara: Pedro responde por M01, Lucas por M02 e Giovanni por M03.

- M01 e M02 derivam de CI01 e CI02 e mantêm boa continuidade com os objetivos O04 a O08, as tarefas e o esquema conceitual de signos da Entrega 9.

- Em M01 e M02, as cenas representam tópicos de conversa, e não simples nomes de telas. Os diálogos incluem signos identificados por S01, S02, S16 e outros IDs definidos anteriormente.

- Os processamentos de M01 e M02 são representados por caixas pretas. As falas de entrada são motivadas pelo usuário e as respostas que saem do processamento são marcadas com `d:`, como esperado.

- M01 e M02 apresentam abertura por círculo preenchido e encerramentos por círculo com anel. Como esses modelos possuem início explícito, a ausência de acesso ubíquo não invalida a entrada no modelo.

- Os dois primeiros modelos não ficam restritos ao caminho feliz: há setas tracejadas para consulta vazia, falha no carregamento do corte e falha na obtenção do MP4. As rupturas retornam a uma cena ou permitem uma saída compreensível.

- M03 também procura representar envio, processamento, progresso, resultados, erro, download, cancelamento e exclusão. A tentativa de incluir caminhos alternativos é pertinente; o problema está na ligação e na notação de parte desses caminhos.

- O documento registra limites e pendências em vez de declarar M03 como concluído. Essa transparência é adequada, embora os pontos pendentes ainda precisem ser corrigidos para que a entrega seja considerada finalizada.

## Correções prioritárias

### 1. Incluir GCO e GCC nos três diagramas

Nenhum dos três MoLIC apresenta as marcações GCO e GCC. Essas marcações não são meras etiquetas decorativas: GCO identifica a abertura de uma conversa orientada a um objetivo, enquanto GCC indica a conclusão correspondente. Sem elas, fica mais difícil verificar onde cada objetivo começa, onde termina e se uma saída realmente representa sua conclusão.

A equipe deve revisar cada objetivo modelado e posicionar GCO e GCC de forma coerente com as falas de abertura e encerramento. Em M01 e M02, os círculos `a1`, `a2`, `e1` e `e2` ajudam a leitura, mas não substituem essa semântica. Em M03, a correção também ajudará a distinguir conclusão, abandono, cancelamento e simples mudança de assunto.

> **✅ Como foi tratado** ([`8ffb4ad`](https://github.com/p4cs-974/projeto-ihc/commit/8ffb4adaa66db415f65dcd40da43dd7bd9e4e635)). [F] Os três diagramas marcam GCO nas aberturas de O00 e GCC na conclusão em e1. O01 a O08 aparecem como objetivos instrumentais das cenas e precondições. As saídas por pendência ficam identificadas no percurso.
>
> \- Pedro

### 2. Finalizar estruturalmente o M03

O M03 possui trechos desconectados e becos sem saída. O login começa em um ponto de abertura, mas não conduz ao percurso principal. A cena “Registro do erro” recebe a comunicação da falha, porém não oferece uma fala de recuperação, reenvio, retorno ou encerramento. A cena de progresso não apresenta uma continuidade clara para nova consulta ou para a chegada aos resultados. O acesso de saída também aparece isolado do restante da conversa.

Um MoLIC precisa mostrar como a conversa prossegue depois que o sistema comunica uma condição. A equipe deve conectar os percursos e decidir, em cada ruptura, se o usuário pode tentar novamente, corrigir uma entrada, adiar, voltar a uma cena anterior ou encerrar com a pendência explicitada. Apenas registrar o erro não caracteriza tratamento de erro.

> **✅ Como foi tratado** ([`eb8379f`](https://github.com/p4cs-974/projeto-ihc/commit/eb8379fa4ce2732c3a6a36e87da764c3774205c6)). [F] O modelo liga o preparo ao acompanhamento e aos resultados. A falha permite corrigir, pedir nova tentativa ou adiar. O diagrama distingue saída antes do envio, pendência na análise, material obtido e pendência na obtenção.
>
> \- Pedro

### 3. Corrigir os emissores das falas no M03

Há transições em que a fala não corresponde ao agente que toma a decisão. No caminho de cancelamento, a confirmação aparece como `d: cancelar processamento`, embora a confirmação de uma decisão de cancelamento deva partir do usuário. Depois do processamento, “processamento cancelado” aparece sem o prefixo `d:`. A resposta `d: res deleted` está em inglês e não mantém a linguagem conceitual usada no restante do projeto.

A equipe deve revisar todas as setas do M03: falas que saem de cenas devem indicar a iniciativa do usuário com `u:` quando ele escolhe mudar de tópico; respostas automáticas do sistema devem usar `d:`; toda saída de uma caixa preta deve comunicar, com `d:`, o resultado do processamento para o usuário.

> **✅ Como foi tratado** ([`153e585`](https://github.com/p4cs-974/projeto-ihc/commit/153e585b37b3c7efb8da4c77f6cfc40733d57464)). [F] As decisões e mudanças de tópico têm falas u:. As saídas de processamento são respostas d: em português. O retorno distingue envio aceito, entrada rejeitada e o resultado do pedido de nova tentativa.
>
> \- Pedro

### 4. Reconciliar o M03 com a Entrega 9

O M03 introduz login, credenciais, exclusão de resultado e cancelamento efetivo do processamento. Esses conceitos não estavam definidos no escopo nem no esquema conceitual de signos da Entrega 9. Ao mesmo tempo, aspectos previstos para CI03 permanecem incompletos: correção de entrada inválida, recuperação da falha, seleção para CSV, conferência do arquivo obtido e retomada do contexto.

O próximo passo não é apenas acrescentar mais caixas. A equipe precisa escolher se as novas capacidades são realmente necessárias e, se forem, justificar a mudança e atualizar cenário, conversa, objetivos, signos e rastreabilidade. Se não forem sustentadas pelo projeto, devem ser retiradas do MoLIC. Os signos do diagrama precisam usar a mesma semântica e os mesmos IDs consolidados na Entrega 9.

> **✅ Como foi tratado** ([`4a1b9e6`](https://github.com/p4cs-974/projeto-ihc/commit/4a1b9e66bebd6d700b0c73625fc4482b3cace418)). [F] M03 usa os objetivos e signos de CI03. Inclui correção de entrada, recuperação condicionada, seleção para CSV, obtenção de MP4, conferência dos arquivos e retomada. Login, exclusão e cancelamento efetivo estão fora do modelo.
>
> \- Pedro

### 5. Ajustar alertas e acessos ubíquos do M03

As caixas tracejadas de confirmação atendem à intenção de representar alerta, mas uma delas se chama “Confirmar exclusão” dentro do caminho de cancelamento da análise. Isso torna incerto qual objeto está sendo afetado e quais consequências estão sendo confirmadas. Os acessos ubíquos aparecem como barras cinzas, porém precisam representar falas que podem ocorrer em qualquer cena e conduzir a um tópico bem definido. No desenho atual, algumas barras e a saída global não estabelecem essa relação com clareza.

A equipe deve renomear cada alerta pelo compromisso que o usuário está prestes a assumir, explicitar o alvo da ação e justificar cada acesso ubíquo. Um acesso ubíquo não serve apenas para evitar desenhar setas; ele expressa uma mudança de tópico disponível durante toda a conversa.

> **✅ Como foi tratado** ([`3e0e56f`](https://github.com/p4cs-974/projeto-ihc/commit/3e0e56fb098bfac4c7595537dd3bbc42f0b79b9c)). [F] O alerta de nova tentativa identifica a entrada, a tentativa quando conhecida e a consequência. Confirmar inicia o pedido. Voltar leva à falha. As duas entradas abrem conversas de preparo e retomada, e os demais acessos partem de cenas que dão contexto à decisão.
>
> \- Pedro


## Recomendações de melhoria

- Em M01 e M02, preservem a estrutura atual, mas simplifiquem textos muito densos dentro das cenas. O diagrama está legível em ampliação, porém a quantidade de informação pode dificultar sua consulta no GitHub em tamanho normal.

  > **✅ Como foi tratado** ([`9cf1f13`](https://github.com/p4cs-974/projeto-ihc/commit/9cf1f1395d527b4c3a0c034333856a77ebf3f58b)). [F] O texto das cenas foi reduzido e ampliado. Os caminhos e os signos pertinentes continuam identificados.
  >
  > \- Pedro

- Diferenciem visualmente e semanticamente uma conclusão bem-sucedida de uma interrupção com pendência. Os encerramentos e1/e2 já iniciam essa distinção; GCO/GCC e falas mais diretas podem completá-la.

  > **✅ Como foi tratado** ([`c949829`](https://github.com/p4cs-974/projeto-ihc/commit/c949829854ddcd1de36422b1211c90c188cacb11)). [F] O modelo marca e1 como conclusão de O00 após obtenção confirmada pela pessoa. As demais saídas informam a partida ou o material pendente.
  >
  > \- Pedro

- No M03, usem a mesma linguagem gráfica e o mesmo nível de acabamento adotados em M01 e M02. A notação básica está presente, mas a distribuição dos elementos, as conexões e os rótulos ainda produzem uma leitura fragmentada.

  > **✅ Como foi tratado** ([`1aed092`](https://github.com/p4cs-974/projeto-ihc/commit/1aed09291761c2f0aa80b16fcd1c62be2ebb5694)). [F] O SVG usa a mesma gramática visual de M01 e M02. A revisão separou os rótulos das conexões e alinhou os retornos de recuperação.
  >
  > \- Pedro

- Atualizem o status da entrega e os checklists somente depois da revisão pelos responsáveis. O documento ainda declara a atividade “em andamento” e deixa várias verificações sem confirmação.

  > **🟨 Tratado em parte** ([`a794201`](https://github.com/p4cs-974/projeto-ihc/commit/a79420121d65e41a2b6088488d397a043caaa40d)). [F] Os checklists registram os pontos conferidos nos artefatos. [?] Pedro, Lucas e Giovanni ainda precisam apresentar e confirmar seus modelos e consolidar a revisão em equipe.
  >
  > \- Pedro

## Pontos que devem alimentar as próximas entregas

- O protótipo precisa representar estados derivados dos MoLIC, especialmente consulta vazia, falha de mídia, falha de análise, retorno após cancelamento e confirmação de obtenção.

  > **🟨 Tratado em parte** ([`a14f442`](https://github.com/p4cs-974/projeto-ihc/commit/a14f442f5c8f64e22609f70880fbac00173c094b)). [F] A Entrega 11 vincula consulta vazia, falha de mídia, falha de análise, desistência da confirmação de nova tentativa e obtenção de arquivos. A conferência dos arquivos salvos é humana. [?] Recuperação real e reenvio dependem da definição técnica.
  >
  > \- Pedro

- O projeto deve preservar a diferença entre seleção de candidatos, obtenção de arquivos e decisão editorial. Baixar um MP4 ou gerar um CSV não significa aprovar o conteúdo.

  > **✅ Como foi tratado** ([`41f685d`](https://github.com/p4cs-974/projeto-ihc/commit/41f685d99c082be28428caaa4499dd4afb5a9a96)). [F] A seleção determina o conteúdo do CSV. Cada MP4 é disponibilizado por corte. A decisão de Arnaldo começa após a passagem externa para T02.
  >
  > \- Pedro

- A equipe ainda precisa decidir, com rastreabilidade, se autenticação, exclusão e cancelamento do processamento pertencem ao escopo real. Essas capacidades não devem avançar para o protótipo apenas porque apareceram em M03.

  > **✅ Como foi tratado** ([`8727e28`](https://github.com/p4cs-974/projeto-ihc/commit/8727e28ea50f729047c2bb36385d78942650bbd0)). [F] A matriz registra o escopo de M03 e a ausência de tarefa e signos consolidados para autenticação, exclusão de resultados ou cancelamento efetivo. Adiar mantém a partida pendente.
  >
  > \- Pedro

- A retomada de contexto continua limitada: o trabalho não deve prometer histórico persistente ou recuperação automática sem que essa capacidade esteja definida e sustentada.

  > **✅ Como foi tratado** ([`a5c1bc3`](https://github.com/p4cs-974/projeto-ihc/commit/a5c1bc3c6410c5f17390f060010109e76c19fb99)). [F] Os modelos usam o contexto acessível ao retomar. Se ele faltar, a pessoa refaz a consulta ou a seleção. [?] A persistência após recarga continua em investigação.
  >
  > \- Pedro

## Síntese das ações recomendadas

1. Inserir GCO e GCC em todos os diagramas.
2. Corrigir conexões, falas e recuperações do M03.
3. Alinhar o M03 aos cenários, objetivos e signos da Entrega 9.
4. Justificar ou remover login, exclusão e cancelamento não consolidados.
5. Revisar alertas e acessos ubíquos do M03.
6. Realizar a revisão individual pendente e atualizar o status da entrega.

> **Situação.** [F] As mudanças documentais estão registradas acima. [?] Faltam as apresentações e a confirmação de Pedro, Lucas e Giovanni.
>
> \- Pedro

De forma geral, a entrega demonstra bom domínio da ideia de MoLIC em M01 e M02, que modelam conversas, alternativas e rupturas com consistência e rastreabilidade. A quantidade individual foi cumprida, mas a entrega ainda não pode ser considerada plenamente consolidada porque a ausência de GCO/GCC afeta os três modelos e o M03 permanece incompleto, desconectado em pontos importantes e parcialmente incompatível com o modelo conceitual anterior. Com a revisão formal dos três diagramas e uma reconstrução cuidadosa do M03, a equipe terá uma base adequada para orientar o protótipo e as avaliações seguintes.
