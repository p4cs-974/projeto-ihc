# Feedback do Professor > Entrega 06 > Equipe 16

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

### 2. Corrigir a continuidade entre acompanhamento, resultados e obtenção do material

O01 identifica um problema central: depois da análise, U01 não sabia se deveria esperar ou avançar. A transcrição registra a pergunta sobre a ausência de um botão e a explicação do facilitador. Portanto, a dica de usar setas não foi suficiente naquela sessão.

A equipe precisa tornar reconhecíveis a conclusão e a ação de continuar. Os atalhos da demonstração não devem substituir a comunicação da própria interface. Há ainda uma diferença importante em relação a T03: a passagem para a base conclui artificialmente o restante da análise, em vez de representar a consulta aos resultados já disponíveis enquanto outras entradas continuam em processamento. Escolham um percurso representativo dessa situação e mostrem como o usuário entende o que está pronto e o que permanece em andamento.

Na obtenção, O04 também merece prioridade. U01 esperava vídeos, enquanto o diálogo enfatizou o CSV. O protótipo já prevê MP4 individual; a questão é tornar clara a distinção entre obter a relação dos cortes e obter os vídeos. Mantenham a montagem final fora do produto, conforme o escopo, mas deixem evidente o que cada ação entrega e o que o usuário ainda precisa fazer para continuar a edição externa.

### 3. Representar exceções relevantes, além do percurso principal

A seção 3.3 reconhece corretamente que falhas de processamento e recuperação localizada ainda não estão representadas. Essa declaração é transparente, mas não substitui os estados de erro e retorno solicitados na atividade, sobretudo porque T03 tem justamente o tratamento de falhas como parte importante de sua finalidade.

A busca sem correspondência, o bloqueio do CSV sem seleção e as mensagens de carregamento de mídia são estados úteis. Eles não representam, contudo, uma entrada que falhou enquanto as demais foram preservadas. “Reiniciar análise” para o lote inteiro também não demonstra a recuperação localizada prevista na análise de tarefas.

Acrescentem um pequeno percurso simulado que permita reconhecer a entrada afetada, compreender a situação e decidir o próximo passo, preservando a referência às demais. Diferenciem também uma busca sem correspondência de uma análise sem candidatos. Essas situações podem ser representadas por telas estáticas e transições encenadas; não dependem de funcionamento real do processamento.

### 4. Ajustar a condução do walkthrough e preservar seus limites

O requisito mínimo de uma simulação com alguém de fora da elaboração está documentado. O uso de um colega é adequado para esta iteração formativa, e a ausência de experiência em edição não invalida a sessão. O cuidado necessário está na interpretação dos resultados.

O formulário registra “Consegui” nas quatro tarefas, mas a transcrição contém orientações durante o percurso. Vocês já reconhecem isso no texto. Preservem essa distinção e registrem, nas próximas sessões, o momento em que houve ajuda e o que a pessoa conseguiu fazer antes dela.

Há um ponto específico a corrigir: entre aproximadamente 02:23 e 02:42, e novamente na discussão do download, o diálogo apresenta a saída como sendo apenas metadados, embora a versão documentada ofereça MP4 individual. Essa orientação pode ter influenciado a expectativa registrada. Alinhem a explicação do facilitador ao artefato utilizado e separem a verificação de obtenção do CSV da obtenção e reprodução de um vídeo, como vocês já propõem em D05.

Uma nova verificação breve das telas alteradas é recomendável para saber se as dificuldades persistem. Não é necessário antecipar a avaliação final da disciplina nem transformar esta rodada em um estudo quantitativo. Também não atribuam sucesso independente ao download de MP4 com base apenas na resposta geral do formulário.

### 5. Manter as evidências e os acessos do projeto dentro do GitHub

A nota de procedência em `artifacts/entrega6/sessao-2026-10-22/README.md` informa expressamente que o áudio original permanece fora do repositório. Nesse ponto, a equipe não seguiu a regra da disciplina de manter os arquivos do projeto no GitHub. A transcrição e o JSON preservados são evidências úteis, mas a fonte citada continua dependendo de material externo.

Regularizem a preservação da evidência autorizada, com o cuidado de anonimização correspondente, e vinculem o registro à sessão. Caso a transcrição permaneça como único registro disponível, explicitem esse limite sem apresentá-la como equivalente à conferência do áudio original.

O mesmo cuidado deve ser aplicado aos acessos operacionais: o botão “Abrir o protótipo” do guia aponta para o domínio publicado, embora exista um HTML no próprio projeto. Para a entrega da disciplina, usem referências internas aos artefatos e não tornem a análise dependente de uma hospedagem externa. Essa correção se refere aos materiais do projeto, não à eliminação de referências bibliográficas de procedência.

### 6. Evidenciar a participação dos três integrantes na atividade integrada

O documento identifica Pedro na condução da sessão e nas decisões de preparação. O README distribui responsabilidades gerais entre Pedro, Lucas e Giovanni, mas a Entrega 6 não esclarece suficientemente o que cada um realizou nesta rodada.

Registrem de forma breve as contribuições efetivas: elaboração do esboço, exploração das alternativas, preparação do roteiro, observação, consolidação dos achados ou revisão das telas. Não é necessário criar três protótipos nem exigir que todos tenham conduzido a mesma sessão. É necessário demonstrar a participação de todos na solução integrada, sem substituir essa informação por uma atribuição genérica à equipe.

## Recomendações de melhoria

Sugiro exportar imagens da versão principal para `assets/06_prototipos/`, identificando as alternativas A, B e C e os estados revisados. O esboço já atende à existência de representação visual, mas suas interrogações na base de resultados registram uma fase anterior. As capturas em `artifacts/media-review/` também documentam uma configuração anterior com quatro lances de uma partida, enquanto a versão descrita na entrega usa oito lances de duas partidas. Identificar data e versão evita confundir evolução técnica com alteração decorrente do walkthrough.

Revisem a comunicação dos termos “highlight”, “corte”, “seleção” e “CSV”. O guia explica essas expressões antes da atividade; por isso, a compreensão posterior não pode ser tratada como descoberta espontânea. Nas próximas verificações, distingam o que a interface comunica sozinha do que depende de instrução recebida.

Na comparação das alternativas, mantenham objetivos equivalentes e registrem a ordem de apresentação. A preocupação de U01 com um carrossel cheio é uma hipótese de uso com maior volume, não uma falha já observada. Explorem essa questão com mais candidatos antes de descartar o mosaico.

O acabamento digital mais avançado não é um problema em si. O cuidado é não investir em detalhes visuais enquanto a passagem entre estados e a compreensão das saídas continuam exigindo explicações do facilitador.







De forma geral, considero que a equipe construiu uma base consistente de prototipação e fez uma leitura cuidadosa dos limites da sessão formativa. A entrega apresenta telas, alternativas e observações concretas relacionadas ao projeto. O avanço necessário agora é fechar o ciclo: os problemas encontrados precisam aparecer resolvidos, ou ao menos explorados por uma nova proposta visível, e não permanecer somente como compromissos para a próxima etapa. Com essa revisão, a documentação passará a demonstrar com mais clareza como a observação do uso modificou as decisões de interface.
