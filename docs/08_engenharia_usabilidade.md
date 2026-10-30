# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 28/10/2026
**Status:** 🟩 completa
**Responsabilidade:** 1 solução consolidada por equipe, Equipe 16

## Objetivo da atividade

Definir princípios e metas verificáveis para preparar gravações, acompanhar a análise e obter cortes e metadados para edição externa. Esta entrega avalia a interação proposta na disciplina. A qualidade do detector e seu tempo real de processamento pertencem à avaliação técnica do TCC.

### Base e limites das evidências

| Base | O que sustenta | Limite |
|---|---|---|
| [Entregas 1](01_conhecendo_o_problema.md), [3](03_personas_contexto_jornada.md), [4](04_cenarios_problema.md) e [matriz de rastreabilidade](../RASTREABILIDADE.md) | Público, contexto e necessidades adotados; hipóteses H02, H05, H13, H14, H24, H26, H27 e H28 | Proto-personas, contexto profissional e benefício esperado ainda precisam de investigação |
| [Tarefas T01–T03 da Entrega 5](05_analise_tarefas.md#seleção-das-tarefas) | T01/A04, revisar e obter candidatos; T03/A02, acompanhar e tratar falhas; T02, continuidade editorial externa | Modelos do uso proposto, sem medições de desempenho humano |
| [Código do protótipo](../assets/06_prototipos/PROTOTIPO_fluxo_highlights.html), [manifesto](../assets/06_prototipos/media/manifest.json) e [documentação técnica](../site/README.md) | Capacidades e restrições inspecionáveis da demonstração | A existência de um controle não comprova que o participante o encontre ou compreenda |
| [Transcrição da sessão de 22/10](../artifacts/entrega6/sessao-2026-10-22/transcricao.txt) e [respostas de U01](../artifacts/entrega6/sessao-2026-10-22/feedback-producao.json) | Dúvidas sobre continuidade, labels, tempo, cores e obtenção do material | Um colega sem experiência em edição, com ajuda. Áudio sem tela, tempos aproximados e autorrelato não comprovam sucesso independente |
| [Entrega 7](07_coleta_dados.md) | Planejamento da coleta, dados a investigar, critérios de participação e procedimentos éticos | I01 e I03 especificados em texto, sem aplicação; I02 publicado no fim do guia, sem análise das respostas. Não fornece resultados empíricos nem linha de base de desempenho profissional |

A Entrega 7 contém o planejamento da coleta e o I02 publicado no guia, sem respostas analisadas ou medições por tarefa. Os limites da seção 3.2 foram confirmados por Pedro em 29/10/2026 como critérios de aceitação desta versão; essa decisão não representa resultado atingido nem validação empírica dos limites.

A [síntese da Entrega 3](03_personas_contexto_jornada.md#síntese) previa metas voltadas a reduzir o tempo de decupagem e minimizar omissões. Esses benefícios continuam como hipóteses a investigar. Sua medição depende de uma linha de base, comparação adequada e critérios para distinguir omissão involuntária de escolha editorial. Nesta iteração, as metas verificam operações e compreensão no protótipo, sem demonstrar esses benefícios no trabalho completo.

## Delimitação do sistema interativo

| Camada | O que pertence ao projeto | O que será avaliado em IHC |
|---|---|---|
| Contribuição técnica do TCC | Sistema híbrido de visão computacional para identificar eventos e gerar cortes e metadados | Compreensão dos resultados apresentados. Precisão, cobertura de eventos e desempenho computacional exigem avaliação técnica própria |
| Camada de interação da disciplina | Preparar vídeos, acompanhar o lote, consultar candidatos, selecionar e baixar material para continuar em ferramentas externas | Compreensão, conclusão sem ajuda, esforço de localização, erros de operação, satisfação e acessibilidade |
| Dados e processamento da demonstração | Quatro arquivos de origem, um por tempo de duas partidas do SoccerNet-v2; oito cortes reais em MP4 e anotações do dataset | A análise revela eventos previamente anotados, sem executar o modelo. Não mede detecção, upload, processamento de partidas completas ou redução de tempo de decupagem |
| Continuidade externa | Ajustar limites dos cortes, montar vídeos, publicar e obter a chancela editorial de P02/T02 | Reconhecer o material obtido e o trabalho que ainda falta. Essas atividades externas não são funções da interface |

A01, preparar e enviar arquivos, é parcialmente representada pela escolha e remoção dos exemplos. T03 cobre acompanhamento, mas não recuperação de falhas de análise. T01 cobre consulta, seleção e obtenção, com limites de revisão e retomada descritos na [Entrega 6, seção 3.3](06_prototipacao_papel.md#33-cobertura-e-lacunas-identificadas-na-revisão). A03, histórico de trabalhos anteriores, não está implementada.

## 1. Características da plataforma

As capacidades abaixo foram conferidas no código e no manifesto locais em 28/10/2026. Requisitos decorrentes são orientações para avaliação ou revisão, sem afirmar que já estão atendidos.

| Característica | Situação demonstrada e incerteza | Consequência para IHC |
|---|---|---|
| Software | Protótipo web em HTML, CSS e JavaScript, servido por HTTP local ou HTTPS no site. Lê um manifesto e reproduz MP4 | Informar indisponibilidade de mídia e distinguir demonstração de operação real. Fixar a versão usada em cada avaliação |
| Hardware e dispositivos | Recorte adotado em computador com tela ampla, H13. Equipamento real do público ainda não investigado | Registrar navegador, resolução, zoom e dispositivos de entrada. Conferir legibilidade, foco e operação por teclado; não presumir adequação ao celular |
| Capacidades | Carregar os exemplos, remover entradas antes de iniciar, acompanhar prévias e progresso, consultar três visualizações, reproduzir cortes, selecionar e retirar itens, exportar CSV e baixar MP4 individual | Verificar se a pessoa entende o lote, a origem dos candidatos e a diferença entre seleção, metadados e vídeo |
| Restrições | Não envia arquivos próprios, executa modelo, ajusta limites de cortes, monta vídeo único ou publica. Formatos e limites do sistema futuro continuam desconhecidos, H24/H26 | Declarar as simulações antes da sessão. Não atribuir falha da pessoa a uma função ausente nem prometer suporte a arquivos não definido |
| Conectividade e latência | Busca manifesto e cortes. A Cache API pode reutilizar a mídia; a seleção não é persistida com ela | Distinguir espera pela rede de dificuldade de operação. Registrar cache e falhas técnicas; não concluir desempenho de upload a partir dos exemplos |
| Segurança e privacidade | O fluxo de exemplos não envia vídeos pessoais. O formulário do guia, I02 da Entrega 7, grava respostas e versão no D1; pode receber nome opcional e texto livre | Separar dados de feedback dos resultados esportivos. Aplicar os procedimentos éticos da Entrega 7, sem solicitar identificação desnecessária nem publicar falas identificáveis |
| Volume de dados e histórico | Quatro tempos e oito candidatos, conforme manifesto. A base contém o lote atual, sem histórico persistente | Testar localização neste conjunto. A preocupação de U01 com o carrossel em grande volume é hipótese a investigar, não falha comprovada |
| Tempo de processamento | Progresso vinculado à reprodução dos cortes anotados, não à análise real. Entrar na base conclui imediatamente o restante da simulação | Verificar percepção de estado e continuidade. Separar duração da simulação de tempo de interação; não usar o atalho como evidência de acesso a resultados parciais |
| Papéis e permissões | Um perfil de uso no protótipo, sem autenticação ou aprovação interna. Papéis organizacionais permanecem abertos, H14 | Não criar metas de administração ou autorização sem necessidade demonstrada. Selecionar um corte não significa chancelar sua publicação |
| Interrupção e retomada | Seleção mantida ao alternar visualizações, mas perdida ao recarregar. Filtro e detalhe não têm preservação completa. Ao ocultar a aba, a simulação pausa; o player do detalhe é encerrado e exige nova reprodução, sem preservar a posição | Informar os limites de persistência e retomada e verificar expectativas. Recuperação após recarga e continuidade entre sessões não podem ser declaradas atendidas |

## 2. Princípios gerais do projeto

| Princípio ou referência | Aplicabilidade ao contexto | Decisão ou requisito decorrente | Fonte |
|---|---|---|---|
| Usabilidade no contexto de uso | O objetivo é obter material para edição em computador. P01 e P03 são personas primárias, conforme a Entrega 3; seus contextos ainda precisam de validação | Aplicar as metas aos dois perfis e relatar eficácia, eficiência e satisfação separadamente, sem inferir ganho profissional a partir de U01 | [ISO 9241-11:2018, apresentação oficial](https://www.iso.org/standard/63500.html); Entregas 1, 3 e 5 |
| Visibilidade de estado e continuidade | U01 não soube se deveria esperar ou avançar depois do processamento, E06-O01 | Tornar conclusão e próximo passo compreensíveis. Verificar a passagem para os resultados sem indicação do facilitador | [E06-O01 e E06-D01](06_prototipacao_papel.md#43-resultados-e-observações) |
| Julgamento editorial e origem identificável | T01 envolve decidir pertinência e contexto. Rever candidatos não demonstra cobertura completa da partida | Apresentar origem e referências temporais. Permitir decisão humana e explicitar a continuidade externa, sem tratar discordância editorial como erro | T01; R01/R04; E06-O06 e E06-D06 |
| Saídas com significado explícito | A fala sobre CSV pode ter influenciado U01; o download de MP4 não foi comprovado, E06-O04 | Explicar as duas saídas e verificar cada arquivo separadamente. Não prometer montagem de vídeo único | [E06-O04 e E06-D05](06_prototipacao_papel.md#5-decisões-após-a-simulação) |
| Acessibilidade visual | Labels e contraste motivaram comentários, sem medição, E06-O02 | Conferir contraste de texto pelos critérios 1.4.3 e de controles pelo 1.4.11. Usar rótulos além da cor, 1.4.1 | [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/) |
| Operação e feedback acessíveis | Navegação, seleção e reprodução precisam ser verificadas além do uso de mouse | Inspecionar teclado, 2.1.1, foco visível, 2.4.7, e mensagens de estado, 4.1.3. Examinar pausa das prévias automáticas pelo 2.2.2 | [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/) |
| Privacidade na coleta acadêmica | Nome opcional e texto livre no I02, publicado no guia, voz e respostas podem identificar participantes. Finalidade acadêmica tem regime específico, com ressalva aos arts. 7º e 11 | Adotar os procedimentos de consentimento, gravação, minimização, acesso e descarte definidos na Entrega 7, conferindo com o docente as exigências institucionais e a base legal adequada antes da aplicação. Adequar os formulários ao protocolo; o aviso atual do guia não comprova seu atendimento | [LGPD, art. 4º, II, b, e arts. 7º e 11](https://www.presidencia.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm); [guia da ANPD para fins acadêmicos](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-tratamento-de-dados-pessoais-para-fins-academicos-e-para-a-realizacao-de-estudos-e-pesquisas) |

As referências externas foram consultadas em 28/10/2026. A seleção de critérios WCAG orienta inspeções específicas, sem declarar conformidade integral. A necessidade de alternativas para conteúdo audiovisual também deverá ser examinada conforme o uso desse conteúdo. Não houve medição de contraste nem teste com tecnologia assistiva nesta entrega.

## 3. Metas de usabilidade

### Contexto comum de verificação

P01, editor de vídeo esportivo, e P03, criador amador, são personas primárias, conforme a [composição das personas na Entrega 3](03_personas_contexto_jornada.md#composição-e-prioridade-das-personas). MQ01–MQ04 e MU01–MU06 se aplicam aos dois perfis, com resultados e cálculo das métricas separados por perfil. A compreensão de rótulos e mensagens deve ser verificada também com criadores amadores, conforme RC07. Se o recrutamento usar colegas como participantes proxy, registrar essa condição e limitar as conclusões à interação observada, sem usá-los como validação dos perfis finais.

Usar computador, os mesmos exemplos e uma versão identificada do protótipo. A visualização A é a entrada atual, conforme E06-D03, sem escolha definitiva entre A, B e C. As metas abaixo não exigem comparar as alternativas nem adotar uma nova direção visual.

Informar previamente apenas o contexto e os limites da demonstração, inclusive ausência de upload real e montagem. Registrar qualquer instrução de navegação, como as setas. Uma ação ensinada não conta como descoberta espontânea. Não revelar o caminho da tarefa nem explicar os metadados antes de registrar a resposta inicial.

O [guia usado na Entrega 6](../assets/06_prototipos/GUIA_simulacao.html) ensina navegação, significado dos tempos e caminhos de download. Ele não deve ser reutilizado integralmente antes das tarefas que verificam essas descobertas. Preparar uma versão de instruções sem essas respostas na Entrega 12. Se a pessoa já tiver recebido tais explicações, registrar a exposição como ajuda prévia nas tentativas afetadas. Essas tentativas permanecem no denominador, mas não contam como sucesso independente.

Em MU01/MQ02, na versão atual, contam tanto a seta para a direita quanto **Ir para o lance**, desde que usados após a conclusão natural da simulação. A dica de setas exibida pela própria interface faz parte do artefato avaliado e não é ajuda externa. Instruções do facilitador ou do guia contam como ajuda prévia. Se E06-D01 alterar a navegação, registrar os caminhos da nova versão antes da avaliação, sem misturar resultados de versões diferentes.

### 3.1 Metas qualitativas

| ID | Meta e tarefa | Evidência desejada | Justificativa e origem |
|---|---|---|---|
| MQ01 | Conferir quais gravações entrarão no lote, A01, precondição de T03 | Identifica partida e tempo da partida, 1º ou 2º, retira a entrada indicada no cenário e explica que usou exemplos, sem afirmar que enviou um arquivo próprio | Evitar iniciar com entrada indevida ou confundir demonstração com upload; H08/H13/H24; PF01 da Entrega 6 |
| MQ02 | Compreender estado e continuidade, T03 → T01 | Distingue espera, andamento e conclusão e encontra o acesso à base sem orientação externa de caminho | E06-O01/D01. A simulação não representa falhas de análise ou recuperação localizada |
| MQ03 | Interpretar origem, tempo e contexto do candidato, T01 | Localiza partida e tempo da partida, 1º ou 2º, distingue relógio do jogo de posição no arquivo em um candidato do segundo tempo e explica se precisa rever o original antes de decidir | E06-O02/O06; T01. Discordância de pertinência não é erro. Os exemplos não validam suficiência de contexto para profissionais |
| MQ04 | Compreender seleção e saídas para continuidade externa, T01 → T02 | Retira um candidato sem interpretar a ação como exclusão da origem; diferencia CSV de MP4 e reconhece que montagem e chancela são externas | E06-O04/D05; R01/R03. Seleção não equivale a publicação |

Registrar a primeira explicação, a ação observada e eventuais dúvidas com referência ao item e à tela. Falas após ajuda devem ficar separadas. Não substituir evidência de compreensão pela preferência por uma visualização.

### 3.2 Metas quantitativas confirmadas

**Os limites de MU01–MU06 foram confirmados por Pedro em 29/10/2026.** São critérios de aceitação definidos para o projeto, sem derivação de U01 ou de exigência normativa. O limite de 100% expressa a ambição de que ninguém na pequena amostra fique bloqueado nessas tarefas delimitadas. Não estima uma taxa para toda a população. A calibração no piloto fica para a Entrega 12.

| ID | Dimensão e métrica | Público e tarefa delimitada | Limite confirmado | Como medir e verificar | Justificativa do limite |
|---|---|---|---|---|---|
| MU01 | Eficácia: proporção de conclusão independente | P01 e P03, separadamente; T03 → T01. Na tela de acompanhamento, após o fim natural da simulação, continuar até a base de resultados | 100% dos participantes avaliáveis de cada perfil, n/n | Sucesso ao abrir a base sem dica externa de caminho ou atalho antecipado. Registrar estado final, caminho usado e ajuda | O bloqueio apareceu em E06-O01. Continuar é precondição da revisão |
| MU02 | Compreensão: proporção de respostas inteiramente corretas | P01 e P03, separadamente; T01. Em um candidato do segundo tempo, identificar partida, tempo da partida, 1º ou 2º, e distinção entre relógio do jogo e posição no arquivo | 100% dos participantes avaliáveis de cada perfil, n/n | Fixar candidato e gabarito pelo manifesto antes da sessão, sem usar um exemplo previamente explicado à pessoa. Cada pessoa precisa acertar os três itens sem explicação prévia | E06-O06 registra perguntas e explicações, sem prova de compreensão independente. No segundo tempo, a diferença entre os relógios fica visível |
| MU03 | Eficácia: proporção de obtenção correta do CSV | P01 e P03, separadamente; T01/A04. Incluir dois candidatos indicados, retirar um terceiro previamente incluído e obter a relação final | 100% dos participantes avaliáveis de cada perfil, n/n | Abrir o CSV salvo. Deve conter exatamente os dois IDs previstos, sem o terceiro. Conferir origem e reconhecer que o arquivo contém metadados e links, sem vídeo incorporado | E06-O04/D05; verifica seleção, retirada e resultado efetivo, em vez de contar o clique em baixar |
| MU04 | Eficácia: proporção de obtenção correta do MP4 | P01 e P03, separadamente; T01/A04. Obter o vídeo de um candidato indicado, em condição inicial padronizada | 100% dos participantes avaliáveis de cada perfil, n/n | Conferir o arquivo salvo e reproduzi-lo, comparando o lance ao candidato solicitado. Um link ou CSV não satisfaz o critério | MP4 já existe no protótipo, mas sua obtenção não foi comprovada na sessão de U01 |
| MU05 | Eficiência: tempo mediano de localização e abertura | P01 e P03, separadamente; T01. Da base A com oito candidatos, sem filtro ou detalhe aberto, localizar um lance pela partida, tempo da partida, minuto do jogo e tipo e abrir seu detalhe | Mediana do tempo descontadas as esperas técnicas identificadas ≤ 90 s, entre conclusões independentes de cada perfil | Fixar um alvo único pelo manifesto. Iniciar após leitura e confirmação do cenário e com a base pronta. Encerrar ao abrir o candidato correto. Registrar todos os tempos, falhas e esperas técnicas | Orçamento inicial de exploração de um conjunto de oito itens. Não é benchmark profissional. O piloto deve verificar se 90 s permite diferenciar procura fluida de desorientação |
| MU06 | Satisfação: mediana da facilidade percebida por tarefa | P01 e P03, separadamente; após as tarefas de MU01, MU03 e MU04, separadamente | Mediana ≥ 4 em escala de 1 a 5 para cada tarefa e perfil | Perguntar: "Quão fácil ou difícil foi realizar esta tarefa?" Usar 1, muito difícil; 2, difícil; 3, nem fácil nem difícil; 4, fácil; 5, muito fácil. Registrar resposta e motivo antes da discussão | Complementa a observação. Escala local, sem equivalência a instrumento padronizado ou comprovação de sucesso |

Os IDs MU identificam métricas, não tarefas novas. Usar como referência os critérios da Entrega 7: participantes com 18 anos ou mais e experiência em seleção ou recorte de lances de partidas encerradas nos últimos seis meses, distinguindo editores profissionais e criadores amadores. Confirmar na Entrega 12 a adequação desses critérios e o tamanho da amostra para a avaliação de usabilidade; as amostras de entrevista, questionário e brainstorming não determinam a amostra do teste. Não juntar P01, P03 e participantes proxy no cálculo das métricas. Se um perfil não estiver representado, registrar suas metas como não avaliadas para esse perfil. A aplicação dos mesmos limites aos dois perfis foi confirmada nesta versão e será revista no piloto, sem presumir familiaridade igual com edição.

#### Regras de registro e cálculo

- **Sucesso independente:** cumpre todo o critério sem dica externa sobre caminho, controle ou significado, inclusive instrução prévia no material entregue. Rótulos e dicas da própria interface fazem parte do artefato avaliado. Repetir literalmente o cenário não é ajuda. Explicar onde agir ou como interpretar é ajuda e deve ser transcrito ou descrito.
- **Conclusão com ajuda:** atinge o resultado depois de orientação. Relatar separadamente e não incluir no numerador de sucesso independente. Resultado incompleto é parcial; abandono ou término sem resultado é falha.
- **Erro de operação:** uma ação produz resultado contrário ao cenário, como retirar outro vídeo ou exportar seleção errada. Uma tentativa corrigida continua registrada como erro, mesmo com sucesso final. Dúvida é hesitação ou pergunta registrada; não presumir dúvida apenas pelo tempo decorrido.
- **Escolha editorial:** discordar da seleção automática ou considerar o contexto insuficiente não é erro. Os candidatos predefinidos das tarefas medem localização e operação, sem impor um julgamento editorial correto.
- **Taxas:** dividir sucessos independentes pelo total de tentativas avaliáveis de cada tarefa e perfil. Ajuda, falha e abandono permanecem no denominador. Registrar contagens absolutas e percentual. Com três tentativas avaliáveis de um mesmo perfil, o limite de 100% exige 3/3, sem generalização estatística.
- **Problema técnico:** se a mídia não carregar ou a sessão for interrompida por fator externo, marcar a tentativa como não avaliável, explicar a razão e informar quantas foram excluídas. Não esconder a ocorrência como sucesso ou falha da pessoa.
- **Tempo:** usar duração entre os eventos definidos em MU05, incluindo leitura da interface e exploração. Para cada tentativa, subtrair do tempo total a soma das esperas técnicas identificadas durante a sessão. Comparar a mediana desses tempos ajustados aos 90 s. Preservar também tempos totais e descontos por tentativa. Não estimar descontos depois da sessão. Em MU01, a espera do processamento não mede tempo de interação.
- **Mediana de tempo:** calcular apenas para conclusões independentes e informar quantos casos a compõem, ao lado das falhas e ajudas. Se ninguém concluir independentemente, não calcular mediana. Um tempo baixo entre poucos sucessos não compensa baixa eficácia.
- **Satisfação:** perguntar também após dificuldade ou falha, respeitando recusa. Informar respostas individuais, mediana e ausências por tarefa. Uma nota alta não transforma falha em sucesso.

Antes da avaliação, definir os candidatos e gabaritos pelo manifesto, a versão e condição inicial de cada tarefa, o tratamento de repetições e um limite de interrupção. MU03 e MU04 devem ter preparação equivalente entre pessoas, sem ensinar o caminho de download durante a preparação. MU05 deve preceder tarefas que revelem a localização do mesmo candidato; se houver repetição, usar alvo equivalente e registrar aprendizagem.

Se MQ01 remover um tempo do lote, restaurar os quatro tempos e concluir a simulação antes das tarefas da base. Conferir os oito candidatos e os IDs previstos no gabarito antes de cada tarefa. Em MU03, preparar apenas o terceiro candidato como selecionado; em MU05, iniciar sem seleção, filtro ou detalhe aberto. A preparação deve ocorrer sem demonstrar à pessoa os caminhos que serão avaliados.

O limite confirmado de 90 s é um critério de desempenho, sem interrupção automática da tentativa. Se a pessoa ultrapassá-lo, o tempo continua registrado até conclusão, abandono ou limite de sessão previamente definido. Não há medições novas nesta entrega, e os aproximadamente 4min36s de áudio de U01 não são tempo de execução de nenhuma dessas tarefas.

### 3.3 Prioridades e decisões confirmadas

A recomendação inicial é tratar continuidade, compreensão e obtenção efetiva como prioridades antes de otimizar tempo. Essa ordem decorre dos bloqueios e dúvidas registrados, sem medição de severidade ou frequência no público profissional.

Não foi localizada, nos materiais consultados do repositório, exigência específica de pesos para esta entrega. Se o docente os solicitar, a equipe deverá atribuir pesos que somem 100%. Pesos representam prioridade, não taxa de sucesso.

| Decisão | Critério adotado | Estado |
|---|---|---|
| Limites de eficácia e compreensão | MU01–MU04: 100% na amostra de cada perfil, com resultados por tarefa | Confirmado por Pedro em 29/10/2026; calibração na Entrega 12 |
| Limite de eficiência | MU05: mediana de até 90 s por perfil, descontadas as esperas técnicas identificadas, com os oito candidatos | Confirmado por Pedro em 29/10/2026; calibração na Entrega 12 |
| Limite de satisfação | MU06: mediana de pelo menos 4/5, por tarefa e perfil | Confirmado por Pedro em 29/10/2026; calibração na Entrega 12 |
| Pesos de prioridade | Não adotados nesta versão; atribuir se houver exigência do docente | Inclusão condicionada à orientação da disciplina |

A confirmação dos critérios encerra a definição das metas desta entrega. Os limites podem ser refinados com a coleta e o piloto da Entrega 12, registrando o motivo. A equipe deve fixar a versão dos critérios antes da avaliação principal. Uma alteração posterior não pode reclassificar silenciosamente os resultados já obtidos.

## 4. Como o ciclo será iterado

| Etapa ou evidência | Artefatos a revisitar | Critério para a revisão |
|---|---|---|
| Coleta da Entrega 7 | Hipóteses em RASTREABILIDADE, personas, cenários e tarefas das Entregas 1 e 3–5; plataforma e metas desta entrega | Confirmar ou refinar perfil, vocabulário, condições de uso e necessidade das funções. Não presumir validação do contexto profissional por U01 |
| Próxima iteração do protótipo | E06-D01, D02, D05 e D06; modelo conceitual, MoLIC e protótipo das Entregas 9–11 | Revisar continuidade, legibilidade e significado de saídas e metadados. Esta entrega não implementa mudanças de interface |
| Piloto e planejamento da Entrega 12 | Instruções adaptadas do guia, gabaritos, condições iniciais, critérios de ajuda, registro de tempo e limites confirmados | Verificar aplicação dos critérios por outro avaliador e cobertura de P01/P03. Registrar a manutenção ou alteração dos limites antes do teste principal. Manter a investigação de maior volume, E06-D04, como questão futura; os oito candidatos não a resolvem |
| Inspeção da Entrega 13 | Telas e estados pertinentes, operação por teclado, contraste e mensagens | Relacionar achados às metas afetadas. Inspeção pode revelar obstáculos, mas não comprova satisfação ou desempenho com usuários |
| Observação da Entrega 14 | MU01–MU06, MQ01–MQ04, evidências e decisões de revisão | Confrontar arquivos, ações e respostas com os critérios fixados. Separar participantes finais de proxies e desempenho técnico de dificuldade de interação |
| Nova versão após avaliação | Protótipo, tarefas afetadas, matriz e histórico desta entrega | Ligar cada mudança ao achado e reaplicar a tarefa afetada. Mudança implementada só conta como melhoria verificada após nova evidência |

Falhas de análise, recuperação localizada, acesso a resultados parciais, histórico e retomada após recarga permanecem lacunas do protótipo. Quando houver estados suficientes para demonstrá-las, suas metas devem ser especificadas antes da avaliação correspondente. A ausência atual não justifica construir backend, aprovação editorial ou edição detalhada dentro da disciplina.

## Checklist

- [x] Capacidades e restrições têm impacto de IHC explicitado.
- [x] Está claro o limite entre contribuição técnica do TCC e camada interativa da disciplina.
- [x] Dados e processamento simulados foram explicitados.
- [x] Metas de usabilidade avaliam a interação, sem substituir métricas técnicas do TCC.
- [x] Normas e princípios estão contextualizados e têm fontes identificadas.
- [x] Métricas têm tarefa, público e procedimento de verificação.
- [x] Eficácia, eficiência, compreensão e satisfação foram consideradas.
- [x] Há ligação com as avaliações futuras e com os limites da evidência atual.
- [x] Limites quantitativos confirmados por Pedro em 29/10/2026; calibração prevista na Entrega 12.
- [x] Pesos de prioridade tratados como condicionais à exigência do docente, sem atribuição nesta versão.

## Histórico

| Data | Alteração | Responsabilidade |
|---|---|---|
| 28/10/2026 | Preenchimento a partir das tarefas, código e evidências da Entrega 6. Inclusão de metas reproduzíveis, fontes oficiais e limites quantitativos propostos, sem aprovação ou avaliação empírica nova | Equipe 16, elaboração assistida a pedido de Pedro |
| 29/10/2026 | Revisão de coerência após auditoria das análises de Opus 5.5 medium e GPT 6.1 Sol high. Cobertura das duas personas primárias, distinção entre pausa e encerramento do player e esclarecimentos de instruções, alvos, condições iniciais e cálculo de tempo. Limites numéricos continuam propostos, sem nova avaliação empírica | Equipe 16, elaboração assistida a pedido de Pedro |
| 29/10/2026 | Pedro confirmou os limites de MU01–MU06. Entrega marcada como completa; calibração no piloto mantida na Entrega 12 e pesos condicionados à exigência do docente. Não foram declarados resultados de avaliação | Equipe 16, confirmação de Pedro |
| 30/10/2026 | Alinhamento com a Entrega 7: inclusão do planejamento na base de evidências, referência aos procedimentos éticos e critérios de participação já especificados e identificação do formulário do guia como I02. Metas quantitativas preservadas, sem nova evidência empírica | Equipe 16; revisão documental assistida pelo Codex a pedido da equipe |
