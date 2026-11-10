# Feedback do Professor > Entrega 06 > Equipe 16


> **Status da aplicação (10/11/2026):** [F] revisão das partes de grupo da Entrega 6: `docs/06_prototipacao_papel.md`, protótipo principal, capturas, mapa do fluxo e evidências da sessão, na branch `docs/e06-prototype-feedback`. A consolidação posterior, na branch `feedback/entregas-06-07-08`, alinhou o guia, `README.md` e `RASTREABILIDADE.md` a esta revisão. O texto do professor foi preservado; as anotações aparecem em blocos de citação após cada item.
>
> | Item do parecer | Situação | Commit(s) |
> |---|---|---|
> | Correção 1: revisão concreta das telas e status | Aplicada; verificação com participante pendente | [`b087c06`](https://github.com/p4cs-974/projeto-ihc/commit/b087c06) |
> | Correção 2: continuidade e obtenção | Aplicada no protótipo e no documento | [`9c67289`](https://github.com/p4cs-974/projeto-ihc/commit/9c67289) |
> | Correção 3: exceções | Aplicada com percursos encenados | [`9ed3753`](https://github.com/p4cs-974/projeto-ihc/commit/9ed3753) |
> | Correção 4: condução do walkthrough | Aplicada no documento; nova sessão pendente | [`d09b9c3`](https://github.com/p4cs-974/projeto-ihc/commit/d09b9c3) |
> | Correção 5: evidências e acessos | Em parte: referências internas no documento; áudio fora do repositório por falta de autorização registrada; guia com link interno | [`d5d9f71`](https://github.com/p4cs-974/projeto-ihc/commit/d5d9f71), [`fb259aa`](https://github.com/p4cs-974/projeto-ihc/commit/fb259aa) |
> | Correção 6: participação dos integrantes | Em parte: Pedro registrado; Lucas e Giovanni sem registro, marcados `[?]` | [`0d0ac88`](https://github.com/p4cs-974/projeto-ihc/commit/0d0ac88) |
> | Recomendações | Aplicadas: capturas por versão, mapa do fluxo, nota em media-review; termos, ordem e volume de C no roteiro 5.3 | [`576d03b`](https://github.com/p4cs-974/projeto-ihc/commit/576d03b), [`d09b9c3`](https://github.com/p4cs-974/projeto-ihc/commit/d09b9c3) |
> | Cabeçalho e histórico | Registrados | [`b7cfe44`](https://github.com/p4cs-974/projeto-ihc/commit/b7cfe44) |
> | Consolidação: guia, documento, README e matriz | Aplicada; verificação com participante, áudio e contribuições de Lucas e Giovanni continuam pendentes | [`fb259aa`](https://github.com/p4cs-974/projeto-ihc/commit/fb259aa), [`14f6c1d`](https://github.com/p4cs-974/projeto-ihc/commit/14f6c1d), [`dfbe0f5`](https://github.com/p4cs-974/projeto-ihc/commit/dfbe0f5), [`0dff068`](https://github.com/p4cs-974/projeto-ihc/commit/0dff068), [`e84eb25`](https://github.com/p4cs-974/projeto-ihc/commit/e84eb25), [`da5ebf5`](https://github.com/p4cs-974/projeto-ihc/commit/da5ebf5) |
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)

A equipe apresenta uma solução integrada coerente com o projeto de identificação de melhores momentos: preparar gravações, acompanhar a análise, examinar candidatos e obter material para continuidade da edição. Há imagens do protótipo em `assets/06_prototipos/`, incluindo `esboco_original.png`, além do mapa `prototipo_fluxo_01.svg`, dos arquivos HTML e das mídias utilizadas. Portanto, a exigência de representação visual está atendida; não se trata de uma entrega composta apenas por descrição textual ou endereço de um site.

As seções do modelo foram desenvolvidas: escopo, fluxos, telas e estados, simulação e decisões posteriores. A escolha das famílias de interface aparece concretamente no fluxo de entrada, acompanhamento e consulta de resultados, sem necessidade de reproduzir a lista de possibilidades do modelo. O principal atendimento parcial está na seção 5: vocês registraram decisões e alteraram o roteiro, mas as mudanças de interface decorrentes da observação ainda estão previstas para outra iteração.

O walkthrough de 22/10/2026 está documentado com um colega que, segundo o registro, não participou do desenho. A equipe distingue autorrelato, comentários reconhecíveis na transcrição e ajuda do facilitador. Essa distinção é importante e deve ser preservada. Entretanto, antes de considerar a entrega inteiramente encerrada, é necessário transformar os problemas observados em uma versão revisada das telas, representar exceções relevantes das tarefas e regularizar a organização das evidências no GitHub.

## Pontos positivos

- **Continuidade com o projeto.** O editor Rafael permanece como referência principal, Jorginho compartilha parte dos fluxos e Arnaldo recebe os resultados externamente. Não foi criada uma área de aprovação, administração ou login apenas para ampliar a quantidade de telas.
- **Exploração de alternativas.** Busca, trilhas por partida e mosaico por tipo respondem a questões diferentes de organização dos mesmos resultados. A preferência de U01 pela alternativa A não foi apresentada como comprovação de superioridade para todos os editores.
- **Identificação dos artefatos.** Os códigos `E06-Pxx` distinguem telas de personas, e os fluxos PF01 a PF04 permitem localizar a finalidade de cada etapa. O esboço inicial, as alternativas e a versão principal estão diferenciados.
- **Contexto para decidir.** As capturas de detalhe apresentam partida de origem, tempo do jogo, limites do corte e reprodução do trecho. A documentação distingue o relógio da partida da posição dentro do arquivo, informação relevante para localizar e conferir os lances.
- **Simulação efetivamente documentada.** Há data, perfil do participante, identificação do facilitador, roteiro, respostas preservadas e observações relacionadas a decisões. A seção 4 vai além de afirmar genericamente que alguém “testou e gostou”.
- **Limites reconhecidos.** A equipe explica que a análise é simulada, que os exemplos não demonstram o funcionamento do algoritmo e que uma sessão com um colega sem experiência em edição não valida o contexto profissional nem ganhos de produtividade.
- **Rastreabilidade atualizada.** A seção 3.1 de `RASTREABILIDADE.md` relaciona os fluxos e as observações da Entrega 6 a R01–R05. Também registra que as melhorias de interface ainda não foram implementadas.

## Correções prioritárias

### 1. Completar a seção 5 com uma revisão concreta das telas

A seção “Decisões após a simulação” é útil, mas não equivale integralmente a “Alterações após a simulação”. D01 e D02, por exemplo, encaminham mudanças de navegação e legibilidade para a próxima iteração. O que foi efetivamente alterado nesta rodada foi principalmente o roteiro de avaliação, nos passos 2 e 6.

A atividade propõe construir, simular, observar e revisar. Vocês já têm evidências suficientes para realizar pelo menos uma revisão focalizada: U01 não compreendeu como sair do acompanhamento para os resultados, e a leitura das trilhas exigiu esclarecimentos. Mostrem como a interface passa a responder a esses problemas. Não é necessário refazer todo o protótipo, implementar o backend ou transformar a entrega em um produto completo.

Registrem o estado anterior, o problema observado, a tela revisada e a justificativa vinculada a O01/D01 ou O02/D02. Indiquem também quais decisões representam manutenção fundamentada da solução, como conservar alternativas, e quais continuam sendo investigação futura. Até que esse passo seja apresentado, ajustem o status de conclusão para não confundir decisões documentadas com revisão de interface concluída.

> **✅ Como foi tratado** ([`b087c06`](https://github.com/p4cs-974/projeto-ihc/commit/b087c06), com a continuidade de [`9c67289`](https://github.com/p4cs-974/projeto-ihc/commit/9c67289)): [F] a seção 5.1 traz, para O01/D01, O02 e O06/D02 e O04/D05, o estado anterior na versão 1, o problema observado com o tempo da transcrição, a tela revisada na versão 2 e a justificativa, com capturas antes e depois e o contraste calculado das etiquetas de B. A seção 5.2 classifica D03 e D04 como manutenção fundamentada, o volume maior de C como investigação futura e D01, D02 e D05 como revisão aplicada. O status do cabeçalho e o checklist dizem que as telas revisadas ainda não foram verificadas com participante.
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


### 2. Corrigir a continuidade entre acompanhamento, resultados e obtenção do material

O01 identifica um problema central: depois da análise, U01 não sabia se deveria esperar ou avançar. A transcrição registra a pergunta sobre a ausência de um botão e a explicação do facilitador. Portanto, a dica de usar setas não foi suficiente naquela sessão.

A equipe precisa tornar reconhecíveis a conclusão e a ação de continuar. Os atalhos da demonstração não devem substituir a comunicação da própria interface. Há ainda uma diferença importante em relação a T03: a passagem para a base conclui artificialmente o restante da análise, em vez de representar a consulta aos resultados já disponíveis enquanto outras entradas continuam em processamento. Escolham um percurso representativo dessa situação e mostrem como o usuário entende o que está pronto e o que permanece em andamento.

Na obtenção, O04 também merece prioridade. U01 esperava vídeos, enquanto o diálogo enfatizou o CSV. O protótipo já prevê MP4 individual; a questão é tornar clara a distinção entre obter a relação dos cortes e obter os vídeos. Mantenham a montagem final fora do produto, conforme o escopo, mas deixem evidente o que cada ação entrega e o que o usuário ainda precisa fazer para continuar a edição externa.

> **✅ Como foi tratado** ([`9c67289`](https://github.com/p4cs-974/projeto-ihc/commit/9c67289)): [F] a tela 3 mostra os lances prontos e **Ver resultados prontos (n) →**, e ao fim **✓ Análise concluída** e **Ver os 8 lances na base →**; as setas passaram a ser apresentadas como atalho. A base abre os resultados prontos enquanto os outros vídeos continuam, com o estado de cada vídeo (E06-P04L) e inclusão dos lances novos por decisão da pessoa. **Obter seleção** separa a lista CSV, que informa não conter vídeo, dos MP4, um por lance, e indica o próximo passo no editor externo. A seleção deixou de ser chamada de CSV. [F] O percurso foi verificado no Chromium local com reprodução real; o andamento fora da tela 3 é encenado.
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


### 3. Representar exceções relevantes, além do percurso principal

A seção 3.3 reconhece corretamente que falhas de processamento e recuperação localizada ainda não estão representadas. Essa declaração é transparente, mas não substitui os estados de erro e retorno solicitados na atividade, sobretudo porque T03 tem justamente o tratamento de falhas como parte importante de sua finalidade.

A busca sem correspondência, o bloqueio do CSV sem seleção e as mensagens de carregamento de mídia são estados úteis. Eles não representam, contudo, uma entrada que falhou enquanto as demais foram preservadas. “Reiniciar análise” para o lote inteiro também não demonstra a recuperação localizada prevista na análise de tarefas.

Acrescentem um pequeno percurso simulado que permita reconhecer a entrada afetada, compreender a situação e decidir o próximo passo, preservando a referência às demais. Diferenciem também uma busca sem correspondência de uma análise sem candidatos. Essas situações podem ser representadas por telas estáticas e transições encenadas; não dependem de funcionamento real do processamento.

> **✅ Como foi tratado** ([`9ed3753`](https://github.com/p4cs-974/projeto-ihc/commit/9ed3753)): [F] a tela 2 permite escolher o percurso **Falha em um vídeo** ou **Vídeo sem lances**. Na falha, o 1º tempo de Bayern x Real Madrid para em 35:19; a tela 3 nomeia a entrada afetada, os outros vídeos seguem, e a base explica o ponto da falha, o lance preservado, o trecho não analisado e oferece nova tentativa só desse vídeo, com confirmação, ou pendência (E06-P03F e E06-P04F, ligados a T03 3.3). O vídeo sem lances (E06-P04Z) tem mensagem distinta da busca sem correspondência (E06-P04V). Tudo é encenado e identificado assim.
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


### 4. Ajustar a condução do walkthrough e preservar seus limites

O requisito mínimo de uma simulação com alguém de fora da elaboração está documentado. O uso de um colega é adequado para esta iteração formativa, e a ausência de experiência em edição não invalida a sessão. O cuidado necessário está na interpretação dos resultados.

O formulário registra “Consegui” nas quatro tarefas, mas a transcrição contém orientações durante o percurso. Vocês já reconhecem isso no texto. Preservem essa distinção e registrem, nas próximas sessões, o momento em que houve ajuda e o que a pessoa conseguiu fazer antes dela.

Há um ponto específico a corrigir: entre aproximadamente 02:23 e 02:42, e novamente na discussão do download, o diálogo apresenta a saída como sendo apenas metadados, embora a versão documentada ofereça MP4 individual. Essa orientação pode ter influenciado a expectativa registrada. Alinhem a explicação do facilitador ao artefato utilizado e separem a verificação de obtenção do CSV da obtenção e reprodução de um vídeo, como vocês já propõem em D05.

Uma nova verificação breve das telas alteradas é recomendável para saber se as dificuldades persistem. Não é necessário antecipar a avaliação final da disciplina nem transformar esta rodada em um estudo quantitativo. Também não atribuam sucesso independente ao download de MP4 com base apenas na resposta geral do formulário.

> **🟨 Tratado em parte** ([`d09b9c3`](https://github.com/p4cs-974/projeto-ihc/commit/d09b9c3)): [F] a seção 4.3 registra que a fala de 02:23 a 02:42 e de 03:47 a 03:57 descrevia só o CSV, embora a versão usada oferecesse MP4, e que não se atribui sucesso independente ao download de MP4. A seção 5.3 traz o roteiro de revalidação, com fala de referência sobre as duas saídas, registro do momento da ajuda e do que a pessoa fez antes dela, ordem das alternativas e passos separados para CSV e MP4. [?] A nova verificação com participante não foi realizada e fica com a equipe.
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


### 5. Manter as evidências e os acessos do projeto dentro do GitHub

A nota de procedência em `artifacts/entrega6/sessao-2026-10-22/README.md` informa expressamente que o áudio original permanece fora do repositório. Nesse ponto, a equipe não seguiu a regra da disciplina de manter os arquivos do projeto no GitHub. A transcrição e o JSON preservados são evidências úteis, mas a fonte citada continua dependendo de material externo.

Regularizem a preservação da evidência autorizada, com o cuidado de anonimização correspondente, e vinculem o registro à sessão. Caso a transcrição permaneça como único registro disponível, explicitem esse limite sem apresentá-la como equivalente à conferência do áudio original.

O mesmo cuidado deve ser aplicado aos acessos operacionais: o botão “Abrir o protótipo” do guia aponta para o domínio publicado, embora exista um HTML no próprio projeto. Para a entrega da disciplina, usem referências internas aos artefatos e não tornem a análise dependente de uma hospedagem externa. Essa correção se refere aos materiais do projeto, não à eliminação de referências bibliográficas de procedência.

> **🟨 Tratado em parte** ([`d5d9f71`](https://github.com/p4cs-974/projeto-ihc/commit/d5d9f71)): [F] o documento aponta para o protótipo e o guia do repositório, sem depender do domínio publicado. A nota da sessão identifica o áudio original por formato, duração, data de criação e SHA-256, e declara a transcrição como único registro do diálogo no repositório, sem equivalência com o áudio. [?] O áudio não foi versionado: contém as vozes de U01 e de Pedro, o repositório é público e não há registro de autorização de U01. A inclusão depende dessa autorização ou de uma versão com vozes alteradas, decisão de Pedro.
>
> **✅ Guia** ([`fb259aa`](https://github.com/p4cs-974/projeto-ihc/commit/fb259aa)): [F] o botão **Abrir o protótipo** de `GUIA_simulacao.html` aponta para `PROTOTIPO_fluxo_highlights.html` na mesma pasta; `site/build.sh` ajusta o link na cópia publicada. O link da Entrega 6 no `README.md` também aponta para o protótipo do repositório ([`0dff068`](https://github.com/p4cs-974/projeto-ihc/commit/0dff068)).
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


### 6. Evidenciar a participação dos três integrantes na atividade integrada

O documento identifica Pedro na condução da sessão e nas decisões de preparação. O README distribui responsabilidades gerais entre Pedro, Lucas e Giovanni, mas a Entrega 6 não esclarece suficientemente o que cada um realizou nesta rodada.

Registrem de forma breve as contribuições efetivas: elaboração do esboço, exploração das alternativas, preparação do roteiro, observação, consolidação dos achados ou revisão das telas. Não é necessário criar três protótipos nem exigir que todos tenham conduzido a mesma sessão. É necessário demonstrar a participação de todos na solução integrada, sem substituir essa informação por uma atribuição genérica à equipe.

> **🟨 Tratado em parte** ([`0d0ac88`](https://github.com/p4cs-974/projeto-ihc/commit/0d0ac88)): [F] a seção 6 registra as contribuições de Pedro comprovadas pelo Git e pelo documento. [?] Não há registro de Lucas nem de Giovanni nos arquivos da Entrega 6; a seção não atribui tarefas a eles e pede que cada um registre a própria contribuição.
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


## Recomendações de melhoria

Sugiro exportar imagens da versão principal para `assets/06_prototipos/`, identificando as alternativas A, B e C e os estados revisados. O esboço já atende à existência de representação visual, mas suas interrogações na base de resultados registram uma fase anterior. As capturas em `artifacts/media-review/` também documentam uma configuração anterior com quatro lances de uma partida, enquanto a versão descrita na entrega usa oito lances de duas partidas. Identificar data e versão evita confundir evolução técnica com alteração decorrente do walkthrough.

> **✅ Como foi tratado** ([`576d03b`](https://github.com/p4cs-974/projeto-ihc/commit/576d03b)): [F] capturas das alternativas A, B e C e dos estados revisados em `assets/06_prototipos/capturas/`, em pastas com versão e data, com README. O mapa do fluxo foi atualizado para a versão 2. `artifacts/media-review/README.md` ganhou nota de que suas capturas são de 21/10/2026, de uma etapa intermediária com quatro cortes de uma partida. Os scripts de verificação estão em `artifacts/entrega6/verificacao-2026-11-10/`.
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


Revisem a comunicação dos termos “highlight”, “corte”, “seleção” e “CSV”. O guia explica essas expressões antes da atividade; por isso, a compreensão posterior não pode ser tratada como descoberta espontânea. Nas próximas verificações, distingam o que a interface comunica sozinha do que depende de instrução recebida.

> **✅ Como foi tratado** ([`9c67289`](https://github.com/p4cs-974/projeto-ihc/commit/9c67289), [`d09b9c3`](https://github.com/p4cs-974/projeto-ihc/commit/d09b9c3)): [F] a interface passou a usar **Selecionar** e **Obter seleção**, e o painel diz o que o CSV e os MP4 contêm. O roteiro 5.3 pede que se registre o que a interface comunicou e o que veio do guia ou do facilitador. [F] O glossário do guia foi mantido. A seção 4.1 do documento e a Entrega 8 registram que quem leu o guia recebeu "highlight ou lance", "corte", "tempo no arquivo", "anotação", CSV e MP4 como instrução, e não como descoberta espontânea ([`dfbe0f5`](https://github.com/p4cs-974/projeto-ihc/commit/dfbe0f5), [`050a480`](https://github.com/p4cs-974/projeto-ihc/commit/050a480)). A dica das setas deixou de dizer que a seta termina a análise, sem acrescentar instrução de caminho ([`14f6c1d`](https://github.com/p4cs-974/projeto-ihc/commit/14f6c1d)).
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


Na comparação das alternativas, mantenham objetivos equivalentes e registrem a ordem de apresentação. A preocupação de U01 com um carrossel cheio é uma hipótese de uso com maior volume, não uma falha já observada. Explorem essa questão com mais candidatos antes de descartar o mosaico.

> **✅ Como foi tratado** ([`d09b9c3`](https://github.com/p4cs-974/projeto-ihc/commit/d09b9c3), [`b087c06`](https://github.com/p4cs-974/projeto-ihc/commit/b087c06)): [F] o roteiro 5.3 define o mesmo objetivo nas três alternativas e alterna a ordem entre pessoas. D04 trata o carrossel cheio como hipótese de uso com mais volume e mantém C. [?] Explorar C com mais candidatos exige cortes além dos oito do manifesto e fica pendente.
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)


O acabamento digital mais avançado não é um problema em si. O cuidado é não investir em detalhes visuais enquanto a passagem entre estados e a compreensão das saídas continuam exigindo explicações do facilitador.

> **ℹ️ Encaminhamento:** [F] a revisão usou o estilo visual existente e mudou apenas o que respondia às observações: ação de continuar, estado do lote, etiquetas de B, saídas e exceções.
>
> \- Pedro (aplicação por automação a pedido de Pedro; fatos novos não confirmados por ele)








De forma geral, considero que a equipe construiu uma base consistente de prototipação e fez uma leitura cuidadosa dos limites da sessão formativa. A entrega apresenta telas, alternativas e observações concretas relacionadas ao projeto. O avanço necessário agora é fechar o ciclo: os problemas encontrados precisam aparecer resolvidos, ou ao menos explorados por uma nova proposta visível, e não permanecer somente como compromissos para a próxima etapa. Com essa revisão, a documentação passará a demonstrar com mais clareza como a observação do uso modificou as decisões de interface.
