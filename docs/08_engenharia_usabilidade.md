# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 28/10/2026 (versão original)
**Revisão:** 10/11/2026, aplicação do [feedback do professor](../feedbacks_professor/Feedback_Professor_Entrega08_Equipe16.md)
**Status:** 🟨 revisada após o parecer; pesos de prioridade, MU07 e MU08 propostos, a confirmar pela equipe
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

A01, preparar e enviar arquivos, é parcialmente representada pela escolha e remoção dos exemplos. T03 cobre acompanhamento; a falha de um vídeo e a nova tentativa localizada aparecem só como percurso encenado na versão 2 do protótipo, sem processamento real. T01 cobre consulta, seleção e obtenção, com limites de revisão e retomada descritos na [Entrega 6, seção 3.3](06_prototipacao_papel.md#33-cobertura-e-lacunas-identificadas-na-revisão). A03, histórico de trabalhos anteriores, não está implementada.

## 1. Características da plataforma

As capacidades abaixo foram conferidas no código e no manifesto locais em 28/10/2026 e atualizadas para a versão 2 do protótipo, de 10/11/2026, descrita na [Entrega 6, seção 5.1](06_prototipacao_papel.md#51-telas-revisadas-na-versão-2). Requisitos decorrentes são orientações para avaliação ou revisão, sem afirmar que já estão atendidos.

| Característica | Situação demonstrada e incerteza | Consequência para IHC |
|---|---|---|
| Software | Protótipo web em HTML, CSS e JavaScript, servido por HTTP local ou HTTPS no site. Lê um manifesto e reproduz MP4 | Informar indisponibilidade de mídia e distinguir demonstração de operação real. Fixar a versão usada em cada avaliação |
| Hardware e dispositivos | Recorte adotado em computador com tela ampla, H13. Equipamento real do público ainda não investigado | Registrar navegador, resolução, zoom e dispositivos de entrada. Conferir legibilidade, foco e operação por teclado; não presumir adequação ao celular |
| Capacidades | Carregar os exemplos, remover entradas antes de iniciar, acompanhar prévias e progresso, abrir os resultados prontos durante a análise, consultar três visualizações, reproduzir cortes, selecionar e retirar itens e obter a seleção em um painel que separa a lista CSV dos MP4. Percursos encenados mostram a falha de um vídeo com nova tentativa localizada e um vídeo sem lances | Verificar se a pessoa entende o lote, a origem dos candidatos e a diferença entre seleção, metadados e vídeo |
| Restrições | Não envia arquivos próprios, executa modelo, ajusta limites de cortes, monta vídeo único ou publica. Formatos e limites do sistema futuro continuam desconhecidos, H24/H26 | Declarar as simulações antes da sessão. Não atribuir falha da pessoa a uma função ausente nem prometer suporte a arquivos não definido |
| Conectividade e latência | Busca manifesto e cortes. A Cache API pode reutilizar a mídia; a seleção não é persistida com ela | Distinguir espera pela rede de dificuldade de operação. Registrar cache e falhas técnicas; não concluir desempenho de upload a partir dos exemplos |
| Segurança e privacidade | O fluxo de exemplos não envia vídeos pessoais. O formulário do guia, I02 da Entrega 7, grava respostas e versão no D1. A versão publicada, `2026-10-21`, pode receber nome opcional e texto livre; a fonte local, `2026-11-10`, não pede nome e mantém texto livre | Separar dados de feedback dos resultados esportivos. Aplicar os procedimentos éticos da Entrega 7, sem solicitar identificação desnecessária nem publicar falas identificáveis |
| Volume de dados e histórico | Quatro tempos e oito candidatos, conforme manifesto. A base contém o lote atual, sem histórico persistente | Testar localização neste conjunto. A preocupação de U01 com o carrossel em grande volume é hipótese a investigar, não falha comprovada |
| Tempo de processamento | Progresso vinculado à reprodução dos cortes anotados, não à análise real. [F] Na versão 2, entrar na base durante a análise mostra só os lances prontos e o estado de cada vídeo; fora da tela 3, a demonstração conclui um vídeo a cada 6 segundos. Só o acesso direto por `?tela=4`, antes de iniciar, conclui o lote na hora | Verificar percepção de estado e continuidade. Separar duração da simulação de tempo de interação; o ritmo encenado fora da tela 3 não representa a espera real |
| Papéis e permissões | Um perfil de uso no protótipo, sem autenticação ou aprovação interna. Papéis organizacionais permanecem abertos, H14 | Não criar metas de administração ou autorização sem necessidade demonstrada. Selecionar um corte não significa chancelar sua publicação |
| Interrupção e retomada | Seleção mantida ao alternar visualizações, mas perdida ao recarregar. Filtro e detalhe não têm preservação completa. Ao ocultar a aba, a simulação pausa; o player do detalhe é encerrado e exige nova reprodução, sem preservar a posição | Informar os limites de persistência e retomada e verificar expectativas. Recuperação após recarga e continuidade entre sessões não podem ser declaradas atendidas |

## 2. Princípios gerais do projeto

Os princípios estão em dois grupos. Os princípios direcionados ao negócio expressam regras e restrições do domínio que governam o serviço: quem decide, o que o serviço entrega e quais dados pode tratar. Os princípios direcionados à interface orientam como o serviço é apresentado e operado pela pessoa. Cada referência normativa está no grupo da finalidade que cumpre.

### 2.1 Princípios direcionados ao negócio

| ID | Princípio ou referência | Aplicabilidade ao contexto | Decisão ou requisito decorrente | Fonte |
|---|---|---|---|---|
| PN01 | Decisão editorial humana | [H] T01 envolve decidir pertinência e contexto. O serviço sugere candidatos; a escolha do que entra no vídeo é de quem edita e, quando houver, da chancela editorial de P02 | Tratar cada candidato como sugestão. Permitir incluir e retirar livremente e não tratar discordância editorial como erro. Selecionar um corte não significa aprová-lo para publicação | T01; R01/R04; [E06-O06 e E06-D06](06_prototipacao_papel.md#43-resultados-e-observações) |
| PN02 | Limites entre seleção, montagem e publicação | [F] O serviço entrega cortes candidatos e metadados. [H] Ajuste fino dos limites, montagem do vídeo único, publicação e chancela de P02/T02 ocorrem em ferramentas e canais externos | Oferecer apenas CSV de metadados e MP4 individual. Não prometer montagem nem publicação. Explicitar o trabalho que continua fora do serviço | [Delimitação do sistema interativo](#delimitação-do-sistema-interativo); T02; R01/R03; [E06-D05](06_prototipacao_papel.md#5-decisões-após-a-simulação) |
| PN03 | Origem rastreável dos candidatos | [F] Cada corte deriva de uma partida e de um tempo da partida. [H] Rever os candidatos não demonstra cobertura completa da partida | Vincular cada candidato a partida, tempo da partida e referência temporal no arquivo de origem, inclusive no CSV. Não apresentar o conjunto como lista completa de lances | T01; MQ03; [manifesto](../assets/06_prototipos/media/manifest.json) |
| PN04 | Privacidade na coleta acadêmica | [F] Nome opcional na versão publicada do I02, `2026-10-21`, texto livre nas duas versões, voz e respostas podem identificar participantes. Finalidade acadêmica tem regime específico, com ressalva aos arts. 7º e 11 | Adotar os procedimentos de consentimento, gravação, minimização, acesso e descarte definidos na Entrega 7, conferindo com o docente as exigências institucionais e a base legal adequada antes da aplicação. Adequar os formulários ao protocolo; o aviso atual do guia não comprova seu atendimento | [LGPD, art. 4º, II, b, e arts. 7º e 11](https://www.presidencia.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm); [guia da ANPD para fins acadêmicos](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-tratamento-de-dados-pessoais-para-fins-academicos-e-para-a-realizacao-de-estudos-e-pesquisas) |

### 2.2 Princípios direcionados à interface

| ID | Princípio ou referência | Aplicabilidade ao contexto | Decisão ou requisito decorrente | Fonte |
|---|---|---|---|---|
| PI01 | Usabilidade no contexto de uso | [H] O objetivo é obter material para edição em computador. P01 e P03 são personas primárias, conforme a Entrega 3; seus contextos ainda precisam de validação | Aplicar as metas aos dois perfis e relatar eficácia, eficiência e satisfação separadamente, organizadas pelas metas de Nielsen da seção 3.3, sem inferir ganho profissional a partir de U01. A norma orienta a avaliação da interação, sem definir regras do serviço | [ISO 9241-11:2018, apresentação oficial](https://www.iso.org/standard/63500.html); Entregas 1, 3 e 5 |
| PI02 | Visibilidade de estado e continuidade | [F] U01 não soube se deveria esperar ou avançar depois do processamento, E06-O01 | Tornar andamento, conclusão e próximo passo compreensíveis. Verificar a passagem para os resultados sem indicação do facilitador | [E06-O01 e E06-D01](06_prototipacao_papel.md#43-resultados-e-observações); [Princípios e Diretrizes para o Design de IHC](../slides_plinio/Principios%20Diretrizes%20Design.pdf), slides 12–13 |
| PI03 | Clareza das saídas | [F] A fala sobre CSV pode ter influenciado U01; o download de MP4 não foi comprovado, E06-O04 | Nomear e explicar as duas saídas na interface e verificar cada arquivo separadamente, conforme os limites de PN02 | [E06-O04 e E06-D05](06_prototipacao_papel.md#5-decisões-após-a-simulação) |
| PI04 | Consistência de termos e referências | [F] Labels de tempo motivaram perguntas, E06-O02/O06. [H] As visualizações A, B e C e o CSV podem nomear partida, tempo e minuto de formas diferentes | Usar os mesmos termos para partida, tempo da partida, relógio do jogo e posição no arquivo nas telas e no CSV. Manter a mesma ação de seleção e retirada nas três visualizações | [E06-O02 e E06-O06](06_prototipacao_papel.md#43-resultados-e-observações); [Princípios e Diretrizes para o Design de IHC](../slides_plinio/Principios%20Diretrizes%20Design.pdf), slides 8–9 |
| PI05 | Acessibilidade visual | [F] Labels e contraste motivaram comentários, sem medição, E06-O02 | Conferir contraste de texto pelos critérios 1.4.3 e de controles pelo 1.4.11. Usar rótulos além da cor, 1.4.1 | [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/) |
| PI06 | Operação e feedback acessíveis | [H] Navegação, seleção e reprodução precisam ser verificadas além do uso de mouse | Inspecionar teclado, 2.1.1, foco visível, 2.4.7, e mensagens de estado, 4.1.3. Examinar pausa das prévias automáticas pelo 2.2.2 | [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/) |

As referências externas foram consultadas em 28/10/2026. A seleção de critérios WCAG orienta inspeções específicas, sem declarar conformidade integral. A necessidade de alternativas para conteúdo audiovisual também deverá ser examinada conforme o uso desse conteúdo. Não houve medição de contraste nem teste com tecnologia assistiva nesta entrega.

## 3. Metas de usabilidade

### Contexto comum de verificação

P01, editor de vídeo esportivo, e P03, criador amador, são personas primárias, conforme a [composição das personas na Entrega 3](03_personas_contexto_jornada.md#composição-e-prioridade-das-personas). MQ01–MQ04 e MU01–MU08 se aplicam aos dois perfis, com resultados e cálculo das métricas separados por perfil. A compreensão de rótulos e mensagens deve ser verificada também com criadores amadores, conforme RC07. Se o recrutamento usar colegas como participantes proxy, registrar essa condição e limitar as conclusões à interação observada, sem usá-los como validação dos perfis finais.

Usar computador, os mesmos exemplos e uma versão identificada do protótipo. A visualização A é a entrada atual, conforme E06-D03, sem escolha definitiva entre A, B e C. As metas abaixo não exigem comparar as alternativas nem adotar uma nova direção visual.

Informar previamente apenas o contexto e os limites da demonstração, inclusive ausência de upload real e montagem. Registrar qualquer instrução de navegação, como as setas. Uma ação ensinada não conta como descoberta espontânea. Não revelar o caminho da tarefa nem explicar os metadados antes de registrar a resposta inicial.

O [guia usado na Entrega 6](../assets/06_prototipos/GUIA_simulacao.html) ensina navegação, significado dos tempos e caminhos de download. Ele não deve ser reutilizado integralmente antes das tarefas que verificam essas descobertas. Preparar uma versão de instruções sem essas respostas na Entrega 12. Ela mantém as informações necessárias ao consentimento e ao contexto da demonstração, separadas de qualquer explicação sobre navegação, significado dos tempos ou caminhos de download. O glossário do guia, que define "highlight ou lance", "corte", "tempo no arquivo" e "anotação", e a dica sobre os arquivos CSV e MP4 também são explicações prévias. Se a pessoa já tiver recebido tais explicações, registrar a exposição como ajuda prévia nas tentativas afetadas. Essas tentativas permanecem no denominador, mas não contam como sucesso independente.

Em MU01/MQ02, na versão 2 do protótipo, contam **Ver os 8 lances na base**, a seta para a direita e **Ir para o lance**, desde que usados após a conclusão natural da simulação. **Ver resultados prontos**, usado antes da conclusão, é registrado com o momento em que ocorreu. Na versão 1, usada em 22/10/2026, os caminhos eram a seta e **Ir para o lance**. A dica de setas exibida pela própria interface faz parte do artefato avaliado e não é ajuda externa. Instruções do facilitador ou do guia contam como ajuda prévia. Resultados de versões diferentes não se misturam.

### 3.1 Metas qualitativas

| ID | Meta e tarefa | Evidência desejada | Justificativa e origem |
|---|---|---|---|
| MQ01 | Conferir quais gravações entrarão no lote, A01, precondição de T03 | Identifica partida e tempo da partida, 1º ou 2º, retira a entrada indicada no cenário e explica que usou exemplos, sem afirmar que enviou um arquivo próprio | Evitar iniciar com entrada indevida ou confundir demonstração com upload; H08/H13/H24; PF01 da Entrega 6 |
| MQ02 | Compreender estado e continuidade, T03 → T01 | Distingue espera, andamento e conclusão e encontra o acesso à base sem orientação externa de caminho | E06-O01/D01. Na versão 2, falha de análise e recuperação localizada existem só como percurso encenado, sem meta própria nesta versão |
| MQ03 | Interpretar origem, tempo e contexto do candidato, T01 | Localiza partida e tempo da partida, 1º ou 2º, distingue relógio do jogo de posição no arquivo em um candidato do segundo tempo e explica se precisa rever o original antes de decidir | E06-O02/O06; T01. Discordância de pertinência não é erro. Os exemplos não validam suficiência de contexto para profissionais |
| MQ04 | Compreender seleção e saídas para continuidade externa, T01 → T02 | Retira um candidato sem interpretar a ação como exclusão da origem; diferencia CSV de MP4 e reconhece que montagem e chancela são externas | E06-O04/D05; R01/R03. Seleção não equivale a publicação |

Registrar a primeira explicação, a ação observada e eventuais dúvidas com referência ao item e à tela. Falas após ajuda devem ficar separadas. Não substituir evidência de compreensão pela preferência por uma visualização.

### 3.2 Metas quantitativas

**Os limites de MU01–MU06 foram confirmados por Pedro em 29/10/2026.** São critérios de aceitação definidos pela equipe, não resultados obtidos, sem derivação de U01 ou de exigência normativa. O limite de 100% expressa a ambição de que ninguém na pequena amostra fique bloqueado nessas tarefas delimitadas. Não estima uma taxa para toda a população. A calibração no piloto fica para a Entrega 12: verificar se o alvo de 100% e o tempo de 90 s distinguem dificuldades relevantes e registrar qualquer alteração antes da avaliação principal.

| ID | Dimensão e métrica | Público e tarefa delimitada | Limite confirmado | Como medir e verificar | Justificativa do limite |
|---|---|---|---|---|---|
| MU01 | Eficácia: proporção de conclusão independente | P01 e P03, separadamente; T03 → T01. Na tela de acompanhamento, após o fim natural da simulação, continuar até a base de resultados | 100% dos participantes avaliáveis de cada perfil, n/n | Sucesso ao abrir a base sem dica externa de caminho ou atalho antecipado. Registrar estado final, caminho usado e ajuda | O bloqueio apareceu em E06-O01. Continuar é precondição da revisão |
| MU02 | Compreensão: proporção de respostas inteiramente corretas | P01 e P03, separadamente; T01. Em um candidato do segundo tempo, identificar partida, tempo da partida, 1º ou 2º, e distinção entre relógio do jogo e posição no arquivo | 100% dos participantes avaliáveis de cada perfil, n/n | Fixar candidato e gabarito pelo manifesto antes da sessão, sem usar um exemplo previamente explicado à pessoa. Cada pessoa precisa acertar os três itens sem explicação prévia | E06-O06 registra perguntas e explicações, sem prova de compreensão independente. No segundo tempo, a diferença entre os relógios fica visível |
| MU03 | Eficácia: proporção de obtenção correta do CSV | P01 e P03, separadamente; T01/A04. Incluir dois candidatos indicados, retirar um terceiro previamente incluído e obter a relação final | 100% dos participantes avaliáveis de cada perfil, n/n | Abrir o CSV salvo. Deve conter exatamente os dois IDs previstos, sem o terceiro. Conferir origem e reconhecer que o arquivo contém metadados e links, sem vídeo incorporado | E06-O04/D05; verifica seleção, retirada e resultado efetivo, em vez de contar o clique em baixar |
| MU04 | Eficácia: proporção de obtenção correta do MP4 | P01 e P03, separadamente; T01/A04. Obter o vídeo de um candidato indicado, em condição inicial padronizada | 100% dos participantes avaliáveis de cada perfil, n/n | Conferir o arquivo salvo e reproduzi-lo, comparando o lance ao candidato solicitado. Um link ou CSV não satisfaz o critério | MP4 já existe no protótipo, mas sua obtenção não foi comprovada na sessão de U01 |
| MU05 | Eficiência: tempo mediano de localização e abertura | P01 e P03, separadamente; T01. Da base A com oito candidatos, sem filtro ou detalhe aberto, localizar um lance pela partida, tempo da partida, minuto do jogo e tipo e abrir seu detalhe | Mediana do tempo descontadas as esperas técnicas identificadas ≤ 90 s, entre conclusões independentes de cada perfil | Fixar um alvo único pelo manifesto. Iniciar após leitura e confirmação do cenário e com a base pronta. Encerrar ao abrir o candidato correto. Registrar todos os tempos, falhas e esperas técnicas e relatar o tempo total ao lado do ajustado | Orçamento inicial de exploração de um conjunto de oito itens. Não é benchmark profissional. O piloto deve verificar se 90 s permite diferenciar procura fluida de desorientação |
| MU06 | Satisfação: mediana da facilidade percebida por tarefa | P01 e P03, separadamente; após as tarefas de MU01, MU03 e MU04, separadamente | Mediana ≥ 4 em escala de 1 a 5 para cada tarefa e perfil | Perguntar: "Quão fácil ou difícil foi realizar esta tarefa?" Usar 1, muito difícil; 2, difícil; 3, nem fácil nem difícil; 4, fácil; 5, muito fácil. Registrar resposta e motivo antes da discussão. A pergunta e a escala ainda devem ser incorporadas ao protocolo da Entrega 12; não existem no I02 atual | Complementa a observação. Mede a facilidade percebida, que é só parte da satisfação. Escala local, sem equivalência a instrumento padronizado ou comprovação de sucesso |

#### Metas quantitativas propostas nesta revisão

[H] MU07 e MU08 dão medida própria à baixa taxa de erro e à memorização, conforme a seção 3.3. Seus limites foram propostos nesta revisão e ainda não foram confirmados pela equipe. Ficam sujeitos à mesma calibração no piloto da Entrega 12 e devem ser confirmados ou alterados antes da avaliação principal.

| ID | Meta de Nielsen e métrica | Público e tarefa delimitada | Limite proposto | Como medir e verificar | Justificativa do limite |
|---|---|---|---|---|---|
| MU07 | Baixa taxa de erro: erros de operação por tentativa | P01 e P03, separadamente; retirada da entrada indicada em MQ01, MU03 e MU04 | 100% das tentativas avaliáveis de cada perfil sem erro não corrigido no resultado e com no máximo um erro corrigido pela própria pessoa | Registrar cada erro de operação com tarefa, tela, ação, gravidade, se a pessoa percebeu e como recuperou. Um erro corrigido conta mesmo quando a tarefa termina com sucesso. Informar contagem de erros por tentativa ao lado de MU03 e MU04 | Separa conclusão final de execução sem erro. Erro não percebido leva material errado à edição externa, PN02. O limite de um erro corrigido admite exploração sem tratar qualquer desvio como bloqueio |
| MU08 | Facilidade de memorização: conclusão independente no retorno | P01 e P03, separadamente; mesmas pessoas da primeira sessão, após intervalo de pelo menos sete dias sem uso do protótipo. T03 → T01: continuar até a base, localizar um candidato equivalente ao de MU05 e obter o CSV com dois IDs indicados | 100% das tentativas avaliáveis de cada perfil, n/n | Iniciar em sessão nova, sem reler o guia nem receber lembrete de caminho. Aplicar os critérios de sucesso de MU01, MU03 e MU05 com alvos equivalentes, não idênticos. Registrar também o tempo de localização e compará-lo descritivamente ao da primeira sessão | O intervalo aproxima o retorno a uma nova rodada, H39. Repetir a tarefa logo em seguida mede outra situação. Verifica se a pessoa reencontra o caminho, não se o protótipo preserva estado após recarga, que não está implementado |

MU08 depende de recrutar as mesmas pessoas duas vezes. Se não houver retorno no prazo da disciplina, registrar MU08 como não avaliada, sem substituí-la por repetição imediata.

Os IDs MU identificam métricas, não tarefas novas. Usar como referência os critérios da Entrega 7: participantes com 18 anos ou mais e experiência em seleção ou recorte de lances de partidas encerradas nos últimos seis meses, distinguindo editores profissionais e criadores amadores. Confirmar na Entrega 12 a adequação desses critérios e o tamanho da amostra para a avaliação de usabilidade; as amostras de entrevista, questionário e brainstorming não determinam a amostra do teste. Não juntar P01, P03 e participantes proxy no cálculo das métricas. Se um perfil não estiver representado, registrar suas metas como não avaliadas para esse perfil. A aplicação dos mesmos limites aos dois perfis foi confirmada nesta versão e será revista no piloto, sem presumir familiaridade igual com edição.

#### Regras de registro e cálculo

- **Sucesso independente:** cumpre todo o critério sem dica externa sobre caminho, controle ou significado, inclusive instrução prévia no material entregue. Rótulos e dicas da própria interface fazem parte do artefato avaliado. Repetir literalmente o cenário não é ajuda. Explicar onde agir ou como interpretar é ajuda e deve ser transcrito ou descrito.
- **Conclusão com ajuda:** atinge o resultado depois de orientação. Relatar separadamente e não incluir no numerador de sucesso independente. Resultado incompleto é parcial; abandono ou término sem resultado é falha.
- **Erro de operação:** uma ação produz resultado contrário ao cenário, como retirar outro vídeo ou exportar seleção errada. Uma tentativa corrigida continua registrada como erro, mesmo com sucesso final. Dúvida é hesitação ou pergunta registrada; não presumir dúvida apenas pelo tempo decorrido.
- **Escolha editorial:** discordar da seleção automática ou considerar o contexto insuficiente não é erro. Os candidatos predefinidos das tarefas medem localização e operação, sem impor um julgamento editorial correto.
- **Taxas:** dividir sucessos independentes pelo total de tentativas avaliáveis de cada tarefa e perfil. Ajuda, falha e abandono permanecem no denominador. Registrar contagens absolutas e percentual. Com três tentativas avaliáveis de um mesmo perfil, o limite de 100% exige 3/3, sem generalização estatística.
- **Problema técnico:** se a mídia não carregar ou a sessão for interrompida por fator externo, marcar a tentativa como não avaliável, explicar a razão e informar quantas foram excluídas. Não esconder a ocorrência como sucesso ou falha da pessoa.
- **Tempo:** usar duração entre os eventos definidos em MU05, incluindo leitura da interface e exploração. Para cada tentativa, subtrair do tempo total a soma das esperas técnicas identificadas durante a sessão. Comparar a mediana desses tempos ajustados aos 90 s. Preservar também tempos totais e descontos por tentativa e relatar a mediana do tempo total ao lado da ajustada. Um tempo ajustado baixo não elimina o impacto da espera percebida pela pessoa; registrar comentários sobre a espera. Não estimar descontos depois da sessão. Em MU01, a espera do processamento não mede tempo de interação.
- **Mediana de tempo:** calcular apenas para conclusões independentes e informar quantos casos a compõem, ao lado das falhas e ajudas. Se ninguém concluir independentemente, não calcular mediana. Um tempo baixo entre poucos sucessos não compensa baixa eficácia.
- **Satisfação:** perguntar também após dificuldade ou falha, respeitando recusa. Informar respostas individuais, mediana e ausências por tarefa. Uma nota alta não transforma falha em sucesso. MU06 mede facilidade percebida por tarefa. Ao fim da sessão, perguntar também: "De modo geral, como foi sua experiência ao usar o protótipo?", em escala de 1, muito ruim, a 5, muito boa, com o motivo. Essa resposta complementa a interpretação da satisfação e não tem limite de aceitação nesta versão.
- **Respostas do I02:** não converter retrospectivamente G03, G07 ou outras respostas do formulário atual para a escala de MU06 ou para a pergunta geral. G03 registra realização declarada, não sucesso independente; G05 registra preferência, não compreensão dos metadados.

Antes da avaliação, definir os candidatos e gabaritos pelo manifesto, a versão e condição inicial de cada tarefa, o tratamento de repetições e um limite de interrupção. MU03 e MU04 devem ter preparação equivalente entre pessoas, sem ensinar o caminho de download durante a preparação. MU05 deve preceder tarefas que revelem a localização do mesmo candidato; se houver repetição, usar alvo equivalente e registrar aprendizagem.

Se MQ01 remover um tempo do lote, restaurar os quatro tempos e concluir a simulação antes das tarefas da base. Conferir os oito candidatos e os IDs previstos no gabarito antes de cada tarefa. Em MU03, preparar apenas o terceiro candidato como selecionado; em MU05, iniciar sem seleção, filtro ou detalhe aberto. A preparação deve ocorrer sem demonstrar à pessoa os caminhos que serão avaliados.

O limite confirmado de 90 s é um critério de desempenho, sem interrupção automática da tentativa. Se a pessoa ultrapassá-lo, o tempo continua registrado até conclusão, abandono ou limite de sessão previamente definido. Não há medições novas nesta entrega, e os aproximadamente 4min36s de áudio de U01 não são tempo de execução de nenhuma dessas tarefas.

### 3.3 Prioridades pelas metas de Nielsen

A priorização usa as cinco metas de usabilidade de Nielsen: facilidade de aprendizado, facilidade de memorização, eficiência, baixa taxa de erro e satisfação positiva do usuário. O material da disciplina apresenta esses fatores em [Qualidade de Uso](../slides_plinio/CC8122-Qualidade%20de%20Uso.pdf), slide 4, com base em Nielsen (1993), e nomeia a baixa taxa de erro como segurança no uso. A definição de memorização como restabelecimento da proficiência ao voltar após um período sem uso foi conferida na página [Usability 101 do Nielsen Norman Group](https://www.nngroup.com/articles/usability-101-introduction-to-usability/), consultada em 10/11/2026.

Continuidade, compreensão e obtenção efetiva continuam sendo preocupações do projeto. Elas não ocupam o lugar das metas: cada uma é relacionada abaixo à meta que serve. Eficácia e compreensão continuam como medidas operacionais, MU01–MU04 e MQ01–MQ04, usadas para verificar as metas. Concluir uma tarefa ao final não demonstra ter cometido poucos erros durante a execução; por isso a baixa taxa de erro tem medida própria.

[H] Os pesos abaixo representam a importância relativa das metas para o uso previsto, não desempenho atingido. Somam 100% e foram propostos nesta revisão a partir das evidências e hipóteses citadas, sem medição de severidade ou frequência no público. A equipe deve confirmá-los ou alterá-los antes do piloto da Entrega 12, registrando o motivo.

| Meta de Nielsen | Peso | Justificativa para o uso previsto | Preocupações do projeto relacionadas | Medidas que a verificam |
|---|---|---|---|---|
| Facilidade de aprendizado | 30% | [H] P03 usa o serviço de forma ocasional e P01 teria um primeiro contato sem treinamento. [F] O bloqueio de E06-O01 ocorreu no primeiro uso. As avaliações planejadas observam primeiro uso, sem guia que ensine o caminho | Continuidade, compreensão do lote, das referências temporais e das saídas | MU01–MU04 e MQ01–MQ04 na primeira sessão, sem ajuda prévia |
| Baixa taxa de erro | 25% | [H] Um erro de seleção ou de download leva material errado para a edição externa e pode só ser percebido depois, já fora do serviço, com retrabalho, H16. Retirar a entrada errada do lote invalida a análise daquela partida | Obtenção efetiva, retirada de candidatos e de entradas do lote | MU07 e registro de erros de operação em MQ01, MU03 e MU04 |
| Facilidade de memorização | 15% | [H] P01 trabalha por dia de rodada, H39, com intervalos entre rodadas, e é interrompido durante a revisão, H41. A seção 1 registra perda de seleção ao recarregar. A pessoa precisa reencontrar o caminho ao voltar, mesmo quando o protótipo não preserva o estado | Retomada, continuidade entre sessões, reconhecimento dos termos já vistos | MU08, em sessão de retorno após intervalo |
| Eficiência | 15% | [H] O volume de quatro a seis partidas por dia de rodada ainda é hipótese, H39, e o conjunto demonstrado tem oito candidatos. O tempo do detector pertence ao TCC. A eficiência importa depois que o uso é aprendido, mas não decide sozinha entre alternativas nesta iteração | Localização de candidatos, esforço após o processamento | MU05, com tempo total preservado |
| Satisfação positiva do usuário | 15% | [H] A adoção por editores e criadores depende de a experiência não ser frustrante, mas satisfação alta não compensa falha na tarefa | Confiança no material obtido, percepção da espera | MU06 e pergunta complementar sobre a experiência geral |

Em conflitos de design, a meta de maior peso orienta a decisão. Por exemplo, entre um atalho que acelera a navegação e um rótulo explícito do próximo passo, preservar o rótulo e manter o atalho como alternativa. Uma meta de peso menor continua com medida própria e não deixa de ser avaliada.

| Decisão | Critério adotado | Estado |
|---|---|---|
| Limites de eficácia e compreensão | MU01–MU04: 100% na amostra de cada perfil, com resultados por tarefa | Confirmado por Pedro em 29/10/2026; calibração na Entrega 12 |
| Limite de eficiência | MU05: mediana de até 90 s por perfil, descontadas as esperas técnicas identificadas, com os oito candidatos | Confirmado por Pedro em 29/10/2026; calibração na Entrega 12 |
| Limite de satisfação | MU06: mediana de pelo menos 4/5, por tarefa e perfil | Confirmado por Pedro em 29/10/2026; calibração na Entrega 12 |
| Pesos das metas de Nielsen | Aprendizado 30%, baixa taxa de erro 25%, memorização 15%, eficiência 15% e satisfação 15% | [H] Propostos nesta revisão; confirmação pela equipe pendente |

A confirmação dos critérios de MU01–MU06 é uma decisão da equipe, não resultado de avaliação. Os limites podem ser refinados com a coleta e o piloto da Entrega 12, registrando o motivo. A equipe deve fixar a versão dos critérios antes da avaliação principal. Uma alteração posterior não pode reclassificar silenciosamente os resultados já obtidos.

### 3.4 Cobertura das metas pelos instrumentos

[F] O I02 publicado no guia, versão `2026-10-21`, registra perfil de edição, G01, forma de realização, G02, realização declarada por tarefa, G03, momentos de dúvida, G04, preferência de visualização, G05, expectativa de download, G06, impressão geral em texto livre, G07, e nome opcional, G08. A fonte local, versão `2026-11-10`, retira G08 e revisa as alternativas de G01, G02, G03 e G05, conforme a [Entrega 7](07_coleta_dados.md); sua publicação está **PENDENTE**. Nenhuma das versões mede sozinha as metas desta entrega, embora possa trazer informações úteis. As verificações abaixo serão preparadas no protocolo da Entrega 12, sem execução nesta entrega.

| Meta de Nielsen | Medidas | Instrumento necessário | O que o I02 atual oferece | Lacuna a resolver na Entrega 12 |
|---|---|---|---|---|
| Facilidade de aprendizado | MU01–MU04, MQ01–MQ04 | Observação da primeira sessão com registro de ação, ajuda, estado final e arquivos salvos; gabaritos pelo manifesto | G03 e G04 como autorrelato; "Consegui" não substitui a conferência de conclusão sem ajuda | Folha de registro por tarefa, gabaritos e versão das instruções sem o caminho das tarefas |
| Baixa taxa de erro | MU07 | Observação com registro de cada erro, gravidade e recuperação; conferência do CSV e do MP4 salvos | Nenhuma medida de erro | Campo de erros na folha de registro e critérios de gravidade |
| Facilidade de memorização | MU08 | Segunda sessão após intervalo, com alvos equivalentes e mesmo registro da primeira | Nenhuma; o formulário é respondido uma vez | Agenda de retorno, alvos equivalentes e tratamento de quem não retornar |
| Eficiência | MU05 | Registro de tempo com eventos de início e fim, esperas técnicas e tempo total | Nenhuma medida de tempo | Forma de cronometragem e registro das esperas durante a sessão |
| Satisfação positiva do usuário | MU06 e pergunta geral | Perguntas após cada tarefa e ao fim da sessão, com escala de 1 a 5 e motivo | G07 em texto livre, sem escala, e G03 com outra escala | Incorporar MU06 e a pergunta geral ao protocolo, sem converter respostas antigas |

As respostas do I02 podem orientar o vocabulário, as dúvidas e a interpretação das metas. Não entram no numerador nem na mediana de nenhuma meta.

## 4. Como o ciclo será iterado

O projeto adota o Ciclo de Vida de Engenharia de Usabilidade de Mayhew, conforme [Processos de Projeto de IHC, Parte 1](../slides_plinio/CC8122-Processos-Parte1.pdf), slides 4 e 8, e [Parte 2](../slides_plinio/CC8122-Processos-Parte2.pdf), slides 2–25. O ciclo tem três fases: análise de requisitos; projeto, teste e desenvolvimento em três níveis; e instalação com feedback do usuário. Os três níveis são o projeto essencial, os padrões de telas e diálogos e o projeto detalhado. Eles se repetem, nessa ordem, para cada grupo de funcionalidades essenciais. Cada nível termina em testes que decidem o avanço ou o retorno.

Os números das entregas indicam a ordem de produção na disciplina. Eles não impedem retornos: um achado da Entrega 14 pode reabrir as Entregas 5, 8 ou 9.

### 4.1 Etapas do ciclo e trabalho do projeto

| Fase ou nível de Mayhew | Atividade do ciclo | Trabalho do projeto | Estado |
|---|---|---|---|
| Análise de requisitos | Perfil do usuário | Personas P01 e P03 como primárias e P02 como continuidade editorial externa, [Entrega 3](03_personas_contexto_jornada.md); hipóteses na [matriz](../RASTREABILIDADE.md) | [H] Proto-personas; coleta da [Entrega 7](07_coleta_dados.md) planejada, sem respostas analisadas |
| Análise de requisitos | Análise contextual das tarefas | Cenários de problema da [Entrega 4](04_cenarios_problema.md) e T01–T03 da [Entrega 5](05_analise_tarefas.md) | [H] Modelos do uso proposto, sem medição de desempenho humano |
| Análise de requisitos | Capacidades e restrições da plataforma | Seção 1 desta entrega | [F] Conferidas no código e no manifesto |
| Análise de requisitos | Princípios gerais de projeto | Seção 2, PN01–PN04 e PI01–PI06 | Definidos nesta entrega |
| Análise de requisitos | Metas de usabilidade | Seção 3: MQ01–MQ04, MU01–MU08 e prioridades da seção 3.3 | MU01–MU06 confirmadas por Pedro em 29/10/2026; MU07, MU08 e pesos propostos, a confirmar |
| Análise de requisitos | Guia de estilo | Registro das decisões de todas as fases. Começa com os princípios e as metas desta entrega | [?] Ainda não há documento próprio. As decisões ficam no histórico de cada entrega e na matriz até sua criação no Nível 2 |
| Nível 1, projeto essencial | Reengenharia do trabalho | Nova repartição da tarefa: o serviço sugere candidatos, a pessoa decide e continua fora do serviço, PN01 e PN02 | [H] Descrita nas Entregas 4 e 5 |
| Nível 1, projeto essencial | Modelo conceitual | Lote, análise, candidato, seleção e saídas, com navegação entre eles, [Entrega 9](09_modelo_conceitual.md) e Entrega 10, MoLIC | Entrega 9 em revisão; Entrega 10 não iniciada |
| Nível 1, projeto essencial | Maquete e testes de interface | Protótipo em papel e simulação dupla com U01, [Entrega 6](06_prototipacao_papel.md) | [F] Uma sessão formativa; decisões E06-D01 a D06. D01, D02 e D05 aplicadas na versão 2, sem verificação com participante |
| Nível 2, padrões de telas e diálogos | Padrões de telas e diálogos | Regras de controles, terminologia, cores e fontes derivadas de PI02–PI06, aplicadas na Entrega 11 | Não iniciado |
| Nível 2, padrões de telas e diálogos | Protótipo de baixa fidelidade | Protótipo HTML com exemplos anotados, que dialoga com a pessoa sem executar o detector, e protótipo no Figma, Entrega 11 | [F] HTML existente; Figma não iniciado |
| Nível 2, padrões de telas e diálogos | Testes | Planejamento, Entrega 12; inspeção, Entrega 13; observação com MU01–MU08, Entrega 14 | Não iniciados |
| Nível 3, projeto detalhado | Projeto detalhado e testes | Mensagens de falha, recuperação localizada, resultados parciais, histórico, retomada após recarga e volume maior que oito candidatos. Testes medem tempos contra os valores admissíveis | [F] Falha de um vídeo, recuperação localizada e resultados parciais encenados na versão 2, sem processamento real nem verificação com participante. [H] Histórico, retomada após recarga e volume maior estão fora do protótipo atual e dependem da continuidade do sistema no TCC |
| Instalação | Feedback do usuário | Feedback de quem já usa o sistema real, que pode originar nova versão ou novos requisitos | Fora do alcance da disciplina; sem sistema instalado |

### 4.2 Iteração planejada

| Etapa de Mayhew | Etapa ou evidência | Artefatos a revisitar | Critério para a revisão |
|---|---|---|---|
| Análise de requisitos | Coleta da Entrega 7 | Hipóteses em RASTREABILIDADE, personas, cenários e tarefas das Entregas 1 e 3–5; plataforma e metas desta entrega | Confirmar ou refinar perfil, vocabulário, condições de uso e necessidade das funções. Não presumir validação do contexto profissional por U01 |
| Nível 1, projeto essencial | Revisão do modelo conceitual | E06-D01, D02, D05 e D06; modelo conceitual e MoLIC das Entregas 9 e 10 | Revisar continuidade e significado de seleção, saídas e metadados no modelo. D01, D02 e D05 já têm telas na versão 2 da Entrega 6, ainda sem verificação; esta entrega não implementa mudanças de interface |
| Nível 2, padrões de telas e diálogos | Próxima iteração do protótipo, Entrega 11 | Padrões de telas e diálogos, guia de estilo, protótipo | Aplicar PI02–PI06 a rótulos, controles, contraste e terminologia, com a mesma nomenclatura nas visualizações e no CSV |
| Nível 2, testes | Piloto e planejamento da Entrega 12 | Instruções adaptadas do guia, gabaritos, condições iniciais, critérios de ajuda, registro de tempo, limites e instrumentos da seção 3.4 | Verificar aplicação dos critérios por outro avaliador e cobertura de P01/P03. Confirmar pesos, MU07 e MU08 e registrar a manutenção ou alteração dos limites antes do teste principal. Manter a investigação de maior volume, E06-D04, como questão futura; os oito candidatos não a resolvem |
| Nível 2, testes | Inspeção da Entrega 13 | Telas e estados pertinentes, operação por teclado, contraste e mensagens | Relacionar achados às metas afetadas. Inspeção pode revelar obstáculos, mas não comprova satisfação ou desempenho com usuários |
| Nível 2, testes | Observação da Entrega 14 | MU01–MU08, MQ01–MQ04, evidências e decisões de revisão | Confrontar arquivos, ações e respostas com os critérios fixados. Separar participantes finais de proxies e desempenho técnico de dificuldade de interação |
| Retorno ao nível indicado pelo achado | Nova versão após avaliação | Protótipo, tarefas afetadas, matriz, guia de estilo e histórico desta entrega | Ligar cada mudança ao achado e reaplicar a tarefa afetada. Mudança implementada só conta como melhoria verificada após nova evidência |

### 4.3 Avanço, retorno e registro das decisões

- **Avanço.** Um grupo de funcionalidades passa ao nível seguinte quando os testes do nível atual atingem as metas fixadas para ele, ou quando cada falha restante foi classificada e tem decisão registrada.
- **Retorno.** Cada problema volta ao nível em que se origina. Perfil, tarefa ou plataforma diferentes do previsto reabrem a análise de requisitos. Uma confusão sobre o que é lote, candidato, seleção ou saída, como em MQ04, reabre o Nível 1. Rótulo, controle, contraste ou terminologia reabrem o Nível 2. Mensagem ou caminho não essencial reabre o Nível 3.
- **Grupos de funcionalidades.** [H] O primeiro grupo é acompanhar a análise e continuar até a base, T03 → T01. O segundo é consultar, selecionar e obter, T01/A04. Falhas de análise e recuperação localizada têm estados encenados na versão 2, ainda sem meta própria. Histórico, A03, retomada após recarga e maior volume formam um grupo futuro, que só entra no ciclo quando houver estados para demonstrá-lo.
- **Guia de estilo.** Cada decisão de projeto fica registrada com o achado que a motivou. Até existir o guia de estilo, o registro fica no histórico da entrega afetada e na matriz de rastreabilidade.
- **Nova iteração.** Os resultados das Entregas 13 e 14 e o feedback do docente podem reabrir qualquer nível. O feedback de uso real, previsto por Mayhew após a instalação, depende do sistema do TCC e não é substituído pelas sessões da disciplina.

[F] Na versão 2 do protótipo, a falha de um vídeo, a recuperação localizada e o acesso a resultados parciais aparecem como estados encenados, sem processamento real e sem verificação com participante. Histórico, retomada após recarga e comportamento com mais de oito candidatos permanecem lacunas do protótipo. As metas atuais valem para o recorte demonstrado e não permitem concluir que esses cenários estão resolvidos. As metas dos estados encenados e das lacunas devem ser especificadas antes da avaliação correspondente. A ausência atual não justifica construir backend, aprovação editorial ou edição detalhada dentro da disciplina. P02 continua como continuidade editorial externa enquanto não houver evidência que justifique outra decisão de escopo.

## Checklist

- [x] Capacidades e restrições têm impacto de IHC explicitado.
- [x] Está claro o limite entre contribuição técnica do TCC e camada interativa da disciplina.
- [x] Dados e processamento simulados foram explicitados.
- [x] Metas de usabilidade avaliam a interação, sem substituir métricas técnicas do TCC.
- [x] Princípios estão organizados em grupos de negócio e de interface, contextualizados e com fontes identificadas.
- [x] Métricas têm tarefa, público e procedimento de verificação.
- [x] Prioridades usam as cinco metas de Nielsen, com pesos que somam 100% e relação com as medidas do projeto.
- [x] Baixa taxa de erro e memorização têm medida própria, MU07 e MU08.
- [x] Cada meta tem instrumento de verificação indicado, inclusive a escala de MU06 a incorporar na Entrega 12.
- [x] O ciclo de Mayhew organiza a iteração, com critérios de avanço, retorno e registro das decisões.
- [x] Limites de MU01–MU06 confirmados por Pedro em 29/10/2026; calibração prevista na Entrega 12.
- [ ] Pesos de prioridade e limites de MU07 e MU08 confirmados pela equipe.
- [x] Referência aos IDs MU/MQ na matriz central de rastreabilidade, como especificação, na [seção 3.2](../RASTREABILIDADE.md#32-metas-de-usabilidade-especificadas-na-entrega-8).

## Histórico

| Data | Alteração | Responsabilidade |
|---|---|---|
| 28/10/2026 | Preenchimento a partir das tarefas, código e evidências da Entrega 6. Inclusão de metas reproduzíveis, fontes oficiais e limites quantitativos propostos, sem aprovação ou avaliação empírica nova | Equipe 16, elaboração assistida a pedido de Pedro |
| 29/10/2026 | Revisão de coerência após auditoria das análises de Opus 5.5 medium e GPT 6.1 Sol high. Cobertura das duas personas primárias, distinção entre pausa e encerramento do player e esclarecimentos de instruções, alvos, condições iniciais e cálculo de tempo. Limites numéricos continuam propostos, sem nova avaliação empírica | Equipe 16, elaboração assistida a pedido de Pedro |
| 29/10/2026 | Pedro confirmou os limites de MU01–MU06. Entrega marcada como completa; calibração no piloto mantida na Entrega 12 e pesos condicionados à exigência do docente. Não foram declarados resultados de avaliação | Equipe 16, confirmação de Pedro |
| 30/10/2026 | Alinhamento com a Entrega 7: inclusão do planejamento na base de evidências, referência aos procedimentos éticos e critérios de participação já especificados e identificação do formulário do guia como I02. Metas quantitativas preservadas, sem nova evidência empírica | Equipe 16; revisão documental assistida pelo Codex a pedido da equipe |
| 10/11/2026 | Aplicação do parecer do professor: princípios em grupos de negócio e de interface, prioridades pelas cinco metas de Nielsen com pesos propostos, MU07 e MU08 propostas, cobertura das metas pelos instrumentos e ciclo de Mayhew na seção 4. Pesos e limites de MU07 e MU08 aguardam confirmação da equipe. Não foram declarados coleta, piloto ou resultados de avaliação | Equipe 16; revisão documental assistida a pedido de Pedro |
| 10/11/2026 | Consolidação com a versão 2 do protótipo da Entrega 6: plataforma, caminhos de MU01, I02 nas versões `2026-10-21` e `2026-11-10`, exposição ao glossário do guia e estados encenados de falha e resultados parciais. Histórico, recarga e maior volume continuam sem solução. Sem coleta, piloto ou resultado de avaliação | Equipe 16; revisão documental assistida a pedido de Pedro |
