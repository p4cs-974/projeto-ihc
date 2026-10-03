# Entrega 4 — Cenários de análise/problema

**Data:** 17/09/2026
**Status:** 🟩 concluído; C01, C02 e C03 desenvolvidos como hipótese
**Responsabilidade:** 1 análise de cenário por integrante

**OBS: O Histórico de commits recentes pode parecer um pouco "bagunçado", foi analisado 1 cenário por integrante conforme as personas desenvolvidas na entrega 03**

## Objetivo da atividade

Descrever situações atuais em que o usuário tenta alcançar um objetivo e encontra dificuldades. O cenário de análise/problema deve tornar visível **o contexto, os atores, as ações e as rupturas**, sem antecipar a interface que será projetada.

> **Regra central:** cenário de problema é a “história do problema”. Se o texto já diz “o sistema mostra”, “o aplicativo resolve” ou descreve botões/telas futuras, provavelmente está misturando problema com solução.

Sempre que possível, o cenário deve aprofundar uma **situação concreta já registrada na Entrega 1**.

### Quando o TCC não possuía interface

O cenário continua sendo uma história de **problema/atividade humana**, não uma história do futuro sistema. Descreva como o profissional realiza hoje uma atividade semelhante ou como lida atualmente com dados, resultados, configurações, logs, decisões e limitações que o tema do TCC pretende apoiar.

Exemplo: em vez de “o DBA abre o novo dashboard e executa o algoritmo”, descreva “o DBA precisa investigar uma consulta lenta, reúne informações em ferramentas distintas, compara planos manualmente e tem dificuldade para estimar o impacto de uma mudança”.

A interface da disciplina aparecerá somente depois, nos cenários de interação.

Se o integrante escolher um novo problema/situação, explique por que ele passou a ser relevante e indique a evidência que motivou sua inclusão.

## Cenário C01 — Seleção manual de melhores momentos sob pressão de prazo

**Autor:** Pedro Alexandre Custódio Silva, 22.123.049-3  
**Persona relacionada:** [P01, Rafael](03_personas_contexto_jornada.md#persona-p01--rafael)  
**Necessidade relacionada:** R01, reduzir o esforço manual e revisar a seleção com contexto  
**Situação de origem:** [Entrega 1, seção 4.5](01_conhecendo_o_problema.md#45-conte-uma-situação-concreta), H11  
**Hipóteses relacionadas:** H01, H06, H09, H10, H11, H12, H13, H17, H28 e H30

### 1. Cenário inicial

Rafael é um editor de vídeo esportivo que precisa preparar os melhores momentos de partidas gravadas. Hoje, passa horas do seu dia em ferramentas de edição, procurando e selecionando manualmente os lances relevantes. O trabalho exige atenção contínua e é mentalmente exaustivo. Sob pressão de prazo, precisa concluir a seleção sem deixar de fora lances importantes.

Essa é a premissa definida pelo autor para C01. A duração expressa como "horas" é qualitativa, não uma medição. O cenário e seus desdobramentos são hipotéticos e ainda precisam de validação com profissionais.

### 2. Questões de refinamento

Cada questão parte de uma lacuna da versão inicial. A coluna "Já informado na versão inicial" registra o que a premissa apresenta, para que a resposta acrescente apenas o que ainda não constava. Os números das questões são usados entre colchetes na narrativa refinada.

| Nº | Elemento | Já informado na versão inicial | Questão de refinamento | Resposta adotada para a narrativa e origem | O que investigar com usuários |
|---|---|---|---|---|---|
| 1 | Ambiente/contexto | Partidas gravadas, horas do dia em ferramentas de edição e pressão de prazo. | Onde e com que equipamento Rafael trabalha, quantas gravações recebe nesse dia e o que depende do término da seleção? | Várias partidas encerradas recebidas no mesmo dia, sala de edição pouco iluminada da produtora e computador com tela ampla. A montagem dos vídeos depende das seleções e precisa começar no mesmo dia. Contexto de P01, H12/H13, e recorte diário confirmado pelo autor. O prazo não tem horário exato. | Quantidade e duração das gravações, tempo disponível e condições reais de trabalho. |
| 2 | Ator | Editor de vídeo esportivo que passa horas em ferramentas de edição. | Qual é a experiência de Rafael com edição e com futebol, e ela explica a demora da seleção? | É experiente em edição e reconhece os tipos de lance que importam. A demora não vem de operar a ferramenta, e sim de sustentar a atenção e repetir julgamentos ao longo de gravações extensas. P01 e H01/H09/H17. | Experiência, ferramentas usadas e estratégias pessoais para localizar lances. |
| 3 | Objetivo | Selecionar os lances relevantes para preparar os melhores momentos, sem deixar de fora os importantes. | Que critério define um lance relevante, um corte aceitável e uma seleção de partida pronta? | Relevantes são gols, defesas, finalizações perigosas e ocorrências disciplinares que ajudam a contar o jogo. Um corte é aceitável quando mostra como a jogada surgiu e como terminou. A seleção de uma partida está pronta quando todos os cortes foram revistos. P01, H06/H11/H28 e critério definido com o autor. | Critérios editoriais, quantidade esperada de cortes e como se determina que a seleção está pronta. |
| 4 | Planejamento | Nada sobre como organiza o percurso das gravações nem o tratamento de dúvidas. | Como pretende percorrer o material e tratar dúvidas? | Trabalha uma partida por vez e revisa seus cortes antes de começar a próxima. Avança nos períodos que considera pouco promissores e retorna ao perceber uma possível jogada relevante. Mantém candidatos duvidosos para reavaliar, conforme H30. Estratégia confirmada pelo autor, detalhando H11. | Ordem efetiva, uso de anotações e tratamento de trechos duvidosos. |
| 5 | Ações | "Procura e seleciona manualmente", sem descrever os comportamentos. | O que faz ao encontrar um lance? | Reproduz, avança, pausa, retorna ao início da jogada, delimita o trecho e o separa para revisão. Com o cansaço, delimita os cortes com menos cuidado e precisa rever decisões. Detalhamento de H01/H09/H11 confirmado pelo autor. | Como registra os trechos, define seus limites e evita refazer trabalho. |
| 6 | Eventos | Nenhuma ocorrência específica; exaustão e prazo aparecem como condições. | Que ocorrência torna o problema visível? | Na revisão de uma das últimas partidas do dia, a reprodução de um corte começa com a finalização e deixa de fora a construção da jogada. Episódio de H11 escolhido com o autor para tornar visível a queda de qualidade. | Ocorrência e frequência de cortes inadequados e como são percebidos. |
| 7 | Avaliação | Preocupação geral em não deixar lances importantes de fora. | Como Rafael interpreta o corte e decide o próximo passo? | Julga que falta contexto, volta ao original e amplia o trecho. Ao final, distingue a qualidade dos cortes revisados da dúvida sobre lances que podem ter passado despercebidos. Construção hipotética apoiada em H09/H10/H11. | Como confere a cobertura da partida e equilibra revisão, cansaço e prazo. |

### 3. Cenário refinado

Os números entre colchetes indicam a questão da seção 2 respondida naquele trecho. Trechos sem número retomam a versão inicial. Os detalhes são uma construção narrativa baseada nas hipóteses acima, sem atribuição de falas ou observações a participantes reais.

Em um dia de trabalho na produtora de conteúdo esportivo, Rafael recebe as gravações integrais de várias partidas já encerradas **[1]** e precisa selecionar seus melhores momentos. Trabalha numa sala de edição com pouca luz, diante de um computador com tela ampla **[1]**. As seleções precisam ficar prontas a tempo de começar a montagem dos vídeos no mesmo dia **[1]**. Rafael domina a ferramenta de edição e reconhece os lances que importam numa partida **[2]**, mas localizar os lances dentro de gravações extensas ocupa horas do seu dia.

Em cada partida, procura gols, defesas, finalizações perigosas e ocorrências disciplinares que ajudem a contar o que aconteceu no jogo **[3]**. Para ele, um corte serve quando mostra como a jogada surgiu e como terminou, e a seleção de uma partida só está pronta depois que todos os cortes foram revistos **[3]**.

Rafael decide trabalhar uma partida por vez e revisar os cortes selecionados antes de começar a seguinte **[4]**. Abre a primeira gravação no editor que já utiliza **[5]**. Quando tem dúvida sobre um candidato, prefere separá-lo provisoriamente e decidir durante a revisão **[4]**.

Ao percorrer o vídeo, avança nos períodos que considera pouco promissores **[4, 5]**. Quando percebe uma possível jogada relevante, retorna a um ponto anterior e assiste à sequência. Pausa, decide onde o corte deve começar para preservar o contexto e até onde precisa ir para mostrar o desfecho. Separa o trecho e retoma a procura **[5]**. Antes de abrir a próxima partida, reproduz os cortes escolhidos, reavalia os candidatos duvidosos e ajusta os limites que considera inadequados **[5]**.

Nas gravações seguintes, Rafael repete esse processo. Com o acúmulo de horas, a busca se torna mentalmente exaustiva e a qualidade do trabalho começa a cair. Ele delimita os trechos com menos cuidado e passa a duvidar de decisões que antes tomava com segurança **[5, 7]**. Retorna a passagens já examinadas para conferir se as avaliou bem **[5]**. Avançar pelo vídeo ajuda a percorrer o material, mas também deixa a dúvida de ter pulado algum lance relevante **[7]**. As conferências e correções consomem parte do tempo disponível para a montagem.

Na revisão de uma das últimas partidas do dia, Rafael reproduz uma finalização perigosa e percebe que o corte começa quando o jogador já está chutando **[6]**. Falta a sequência anterior que explica como a oportunidade surgiu. Considera o trecho insuficiente, localiza novamente a jogada na gravação original e amplia seu início **[7]**. Depois, assiste ao corte corrigido para conferir se a jogada ficou compreensível **[7]**. O cuidado insuficiente na seleção exigiu uma nova busca e mais uma revisão.

Rafael termina as seleções das partidas recebidas e segue para a montagem exausto, com menos tempo disponível para concluir os vídeos. Conseguiu revisar os trechos escolhidos, mas essa conferência não elimina sua dúvida sobre possíveis lances ignorados durante os avanços **[7]**. Rever integralmente as gravações exigiria mais tempo e atenção. Ao encerrar a seleção, leva consigo essa incerteza, além do desgaste acumulado e do tempo gasto refazendo cortes.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ambiente ou contexto | Um dia de pós-produção com várias gravações de partidas encerradas, sala de edição da produtora, pouca luz, computador com tela ampla e prazo como pressão de fundo. |
| Ator | Rafael, P01, editor experiente que realiza a busca, a seleção e a revisão. |
| Objetivo | Obter seleções de lances relevantes e compreensíveis das partidas recebidas, a tempo de continuar a montagem. |
| Planejamento | Trabalhar uma partida por vez; percorrer a gravação com avanços e retornos, separar candidatos e revisar os cortes antes da próxima partida. |
| Ações | Abrir a gravação, reproduzir, avançar, pausar, retornar, delimitar e separar trechos; localizar a jogada original e corrigir um corte. |
| Eventos | Recebimento das gravações e reprodução, pelo programa de edição, de um trecho que começa diretamente na finalização durante a revisão de uma das últimas partidas. |
| Avaliação | Julgar a relevância dos candidatos, perceber a falta de contexto, avaliar o corte corrigido e ponderar o custo de rever integralmente as gravações. |
| Recursos e informações | Gravações integrais, ferramenta de edição, trechos separados por partida, conhecimento do jogo e prazo de entrega. |
| Problemas e rupturas | Desgaste acumulado entre partidas, cortes delimitados com menos cuidado, decisões reavaliadas e descoberta de um corte sem contexto durante a revisão. |
| Consequências | Busca repetida, correção de cortes, cansaço mental, menos tempo para montagem e incerteza sobre possíveis omissões. |

Planejamento e avaliação descrevem atividades mentais; ações descrevem comportamentos observáveis. No episódio do corte, a reprodução é o evento, a percepção de contexto insuficiente é a avaliação e o retorno à gravação é a ação decorrente.

### 5. Implicações para as próximas entregas

Para a [Entrega 5](05_analise_tarefas.md), C01 oferece como tarefa de origem **selecionar lances relevantes de uma partida gravada para continuar a montagem**. A análise deve explicitar a procura, os critérios de seleção, a delimitação dos trechos, a revisão e os retornos motivados por dúvida ou contexto insuficiente. Essas atividades incluem decisões humanas que precisam aparecer na modelagem. A tarefa se repete para cada partida, com revisão antes de iniciar a seguinte; o cenário permite analisar também o desgaste acumulado ao longo do dia.

Ao modelar o uso proposto, a relação R01 liga esse problema à atividade A04, revisar, selecionar e baixar cortes e metadados. É necessário declarar se cada modelo representa o trabalho atual ou o uso proposto. A montagem e os ajustes detalhados permanecem no editor externo, conforme o escopo existente. Os modelos HTA, GOMS e CTT ainda serão elaborados na Entrega 5.

A coleta de dados deverá investigar quanto tempo se gasta procurando, recortando e revisando; como se escolhem os lances; que contexto cada corte precisa preservar; e como o editor identifica omissões. Também deve examinar se os avanços, as dúvidas e os retornos descritos aqui ocorrem na prática, se há queda de qualidade com o desgaste acumulado entre partidas e como o prazo interfere nessas decisões.

O valor a investigar para o projeto é reduzir o esforço de busca e preparação dos trechos, preservando a possibilidade de o editor julgar sua relevância e contexto. C01 não demonstra que uma seleção automática seria completa nem que eliminaria a revisão humana.

## Cenário C02 — Controle do Processo Editorial Engessado

**Autor:** Lucas Roberto Boccia dos Santos, 22.123.012-1  
**Persona relacionada:** [P02, Arnaldo](03_personas_contexto_jornada.md#persona-p02--arnaldo)  
**Necessidade relacionada:** R03, receber material identificável e contextualizado para decidir sobre a seleção e supervisão editorial  
**Situação de origem:** [Entrega 1, seção 5.4](01_conhecendo_o_problema.md#54-existem-fatores-sociais-ou-organizacionais), H14  
**Hipóteses relacionadas:** H04, H10, H14, H16, H20, H22, H23, H33, H34 e H35

### 1. Cenário inicial

Arnaldo é editor-chefe de uma emissora esportiva e tem como dever supervisionar o trabalho dos editores e garantir a fluidez do processo editorial. Hoje, passa horas por dia andando pelas salas de edição, conversando com editores e tentando manter controle sobre o trabalho manual que todos estão desenvolvendo, tendo que chancelar decisões editoriais em meio a prazos e expectativas de entrega, sendo o responsável maior pelo conteúdo final publicado.

Essa é a premissa definida pelo autor para C02. O relato descreve as dificuldades da supervisão presencial e da aprovação sob demanda. O cenário e seus desdobramentos são hipotéticos e ainda precisam de validação com profissionais.

### 2. Questões de refinamento

| Elemento | Questão que a premissa deixa em aberto | Resposta adotada para a narrativa e origem | Contexto | O que investigar com usuários |
|---|---|---|---|---|
| Ambiente/contexto | Em que condições Arnaldo precisa controlar o processo atual? | Um dia de trabalho com diversos editores trabalhando na edição de múltiplas partidas diferentes, muitas vezes não relacionadas entre si, percorrendo a sala de edição e olhando as diferentes telas para monitorar o que está sendo feito. | Contexto de P02. | Quantidade média de atividades acompanhadas simultaneamente, tipo de decisões a chancelar, condições reais de trabalho |
| Ator | A dificuldade decorre de falta de entendimento do processo? | Arnaldo é um editor-chefe experiente, que já atua na função há anos. A dificuldade é manter a atenção e coerência enquanto avalia diversos processos simultaneamente, com pouco tempo para chancelar decisões editoriais. | P02 | Experiência, como esse processo já evoluiu com o tempo e como a demanda cada vez maior tem o transformado |
| Objetivo | O que precisa estar pronto ao final desta atividade? | O conteúdo editado deve ter sido publicado na internet de acordo com as normas e preferências da emissora, processo chancelado pelo editor-chefe | P02 | Critérios editoriais, processo de publicação. |
| Planejamento | Como pretende monitorar e auditorar o processo? | Acompanha o trabalho de vários editores ao mesmo tempo, está em contato constante com os mesmos e procura manter anotações das questões que considera de maior relevância, garantindo que o processo siga conforme o esperado e desejado pela emissora. | P02 | Ordem efetiva, uso de anotações e tratamento de trechos duvidosos. |
| Ações | Como aprova e chancela (ou não) decisões? | Possui conhecimento pleno das normas, exigências e necessidades da emissora. Baseia suas decisões nestas e na sua experiência no ofício. Tem a palavra final sobre o trabalho produzido pelos editores. | P02 | Quais fatores e situações costumam gerar a necessidade de intervenção por parte do editor-chefe. |
| Eventos | Que ocorrência torna o problema visível? | Mídias sendo postadas nas redes sociais de forma inconsistente ou com falhas no conteúdo. Aprovar decisões "às cegas", baseado puramente na experiência profissional, pois não tem tempo ou condições de fazer a revisão completa e adequada. | P02 | Qual a frequência desse tipo de ocorrência. Como isso tem escalado com o aumento constante da demanda por esse tipo de conteúdo. |
| Avaliação | Como toma uma decisão editorial em um momento de pressão? | Necessita chancelar uma decisão definitiva em meio à indecisão dos editores, muitas vezes em pouco tempo. Utiliza sua experiência e aprendizados de casos anteriores para tomar a decisão que julga ser a mais cabível ou segura para a situação. | P02 | Quais os principais fatores levados em consideração na tomada dessas decisões. Quais os principais aprendizados das ocorrências anteriores. |

### 3. Cenário refinado

Os parágrafos identificados com **[NOVO]** desenvolvem a premissa inicial. Os detalhes são uma construção narrativa baseada nas hipóteses acima, sem atribuição de falas ou observações a participantes reais.

**[NOVO]** Em um dia movimentado de rodada de futebol na emissora esportiva, Arnaldo atua como editor-chefe responsável por supervisionar a produção de conteúdo digital e chancelar a publicação dos melhores momentos. Na área de pós-produção, vários editores trabalham simultaneamente em ilhas de edição, cada um encarregado de uma partida diferente. O ritmo é acelerado e há forte expectativa da direção e da audiência para que os vídeos e recortes sejam publicados nas redes sociais logo após o término dos jogos. Arnaldo conhece a fundo a linha editorial e as exigências da emissora, mas o acompanhamento presencial e descentralizado de múltiplas partidas consome horas do seu turno.

**[NOVO]** Para tentar manter o controle, Arnaldo adota a estratégia de circular continuamente pelas ilhas de edição, observando o que está sendo montado diretamente nas telas de cada computador. Ele conversa brevemente com os editores para acompanhar o andamento dos cortes e mantém um bloco de notas manual com anotações pontuais sobre o status de cada partida, os lances pendentes e os alertas prioritários. O objetivo é assegurar que todas as seleções atendam aos padrões de qualidade da emissora antes de serem liberadas para postagem externa.

**[NOVO]** Ao longo da jornada, Arnaldo é constantemente interrompido por editores que solicitam sua presença física para resolver dúvidas e validar escolhas difíceis. Diante da indecisão de um editor sobre a pertinência de um cartão polêmico ou a delimitação de uma finalização perigosa, Arnaldo debruça-se sobre a estação de trabalho, assiste ao trecho isolado na linha do tempo e precisa chancelar uma decisão definitiva em poucos minutos. Como não acompanhou os 90 minutos daquela partida, recorre exclusivamente à sua memória de casos anteriores e à sua intuição profissional para definir se o corte deve ser mantido ou descartado.

**[NOVO]** Conforme várias partidas se encerram quase ao mesmo tempo, a demanda atinge o ápice e o processo se torna caótico e engessado. Os editores acumulam vídeos prontos para revisão simultaneamente, gerando uma fila de espera pela chancela do editor-chefe. Sem tempo hábil para assistir a todos os trechos e com os prazos de publicação estourando, Arnaldo é forçado a aprovar lotes de cortes "às cegas", confiando apenas nas anotações de sua prancheta e no relato verbal rápido dos profissionais, sem condições de verificar se os recortes mantiveram o contexto do lance ou se omissões ocorreram.

**[NOVO]** A fragilidade desse modelo torna-se visível quando um clipe de melhores momentos é publicado nas redes sociais da emissora com grave falha de contexto: a jogada que culminou no gol da vitória foi cortada sem mostrar o lance de falta anterior que gerou intensa reclamação do time adversário. Em poucos minutos, a postagem acumula críticas de torcedores nos comentários questionando a imparcialidade do canal, e a direção da emissora contata Arnaldo cobrando explicações imediatas sobre a aprovação daquele conteúdo incompleto.

**[NOVO]** Arnaldo precisa interromper o acompanhamento dos outros editores para intervir na crise: ordena a retirada imediata do vídeo do ar, senta-se com o editor responsável para refazer o corte recuperando a jogada original e chancela a republicação do material corrigido. O episódio consome um tempo precioso e atrasa as postagens das demais partidas do dia. Ao término do expediente, Arnaldo conclui seu trabalho desgastado e frustrado, percebendo que a supervisão puramente presencial, informal e desprovida de registros contextualizados sobre os cortes não apenas sobrecarrega sua rotina, mas deixa o processo editorial exposto a falhas graves.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ambiente ou contexto | Dia de rodada esportiva na emissora, área de pós-produção com múltiplas ilhas de edição operando simultaneamente em partidas distintas, sob forte pressão de prazo para publicação em redes sociais. |
| Ator | Arnaldo, P02, editor-chefe experiente encarregado da supervisão editorial e da chancela final das publicações. |
| Objetivo | Garantir que o conteúdo publicado nas redes sociais e plataformas digitais cumpra as normas da emissora e mantenha alto padrão editorial, chancelado a tempo. |
| Planejamento | Circular continuamente pelas ilhas de edição, monitorar as telas dos editores, manter anotações manuais sobre o andamento e atender pontualmente às dúvidas editoriais. |
| Ações | Percorrer as salas de edição, inspecionar telas, dialogar com editores, anotar pendências, assistir a cortes pontuais nas ilhas de edição, chancelar aprovações sob pressão e ordenar a remoção/correção de vídeo com falha. |
| Eventos | Acúmulo de partidas encerradas simultaneamente, solicitação de aprovação de múltiplos lotes em curto intervalo e publicação nas redes sociais de um corte com contexto incompleto (falta anterior ao gol suprimida). |
| Avaliação | Julgar a pertinência editorial de lances com base na experiência acumulada, avaliar o risco de aprovar cortes "às cegas" para não atrasar a publicação e reconhecer o impacto negativo do vídeo incompleto publicado. |
| Recursos e informações | Normas e diretrizes da emissora, estações/telas de edição dos editores, bloco de anotações manual, lances montados nas linhas do tempo e reações imediatas da audiência nas redes sociais. |
| Problemas e rupturas | Supervisão manual e engessada, interrupções frequentes, sobrecarga cognitiva diante de múltiplos jogos simultâneos, aprovação "às cegas" por falta de tempo e publicação de conteúdo inconsistente. |
| Consequências | Postagem com falha editorial, exposição negativa da emissora, cobrança da direção, retrabalho emergencial (remover, regravar e republicar) e exaustão com sensação de perda de controle do processo. |

Planejamento e avaliação descrevem atividades mentais; ações descrevem comportamentos observáveis. No episódio da postagem incorreta, a publicação do corte truncado e as críticas da audiência configuram os eventos, o julgamento de que o material é inaceitável e expõe a emissora representa a avaliação, e a ordem de remoção e refação do corte constituem as ações decorrentes.

### 5. Implicações para as próximas entregas

Para a [Entrega 5](05_analise_tarefas.md), C02 oferece como tarefa de origem **supervisionar a seleção editorial e chancelar cortes para publicação**. A análise deve detalhar a rotina de monitoramento das ilhas de edição, o atendimento a dúvidas dos editores, a verificação da cobertura e do contexto dos lances sob pressão de tempo, os momentos de decisão/chancela e o fluxo de contingência diante de falhas de publicação. Essas atividades evidenciam como o julgamento profissional e os critérios de qualidade da emissora se manifestam no trabalho cotidiano e onde o processo manual se torna um gargalo.

Ao modelar o uso proposto, a relação R03 liga essa necessidade ao consumo qualificado dos resultados. Conforme delimitado no projeto, P02 atua inicialmente como stakeholder indireto que recebe cortes identificados por partida e acompanhados de metadados estruturados (timecode, tipo de lance, descrição) fora da interface, após a atividade A04 realizada pelo editor. Isso permite a P02 avaliar e chancelar as seleções antes da montagem final ou solicitar revisões pontuais sem precisar inspecionar vídeos inteiros ou aprovar "às cegas". A eventual existência de uma visualização direta para supervisão ou histórico de auditoria editorial (H35) permanece como proposta exploratória a ser validada, sem previsão de telas de publicação direta ou CMS no escopo de IHC. Os modelos HTA, GOMS e CTT para essas atividades serão desenvolvidos na Entrega 5.

A coleta de dados (para a [Entrega 7](07_coleta_dados.md)) deverá investigar a quantidade média de editores e partidas supervisionadas ao mesmo tempo; quais critérios e diretrizes orientam a decisão de chancelar ou vetar um lance; que tipo de informação mínima o editor-chefe precisa consultar para aprovar um corte com segurança; com que frequência ocorrem aprovações sob pressão ou erros perceptíveis pelo público; e como são tratadas as divergências e retrabalhos na equipe.

O valor a investigar para o projeto é conferir rastreabilidade, identificação e contexto aos lances gerados, facilitando a supervisão e reduzindo o risco de decisões arbitrárias ou desinformadas. C02 evidencia que a tecnologia do TCC deve apoiar o fluxo de revisão humana com metadados claros, e não automatizar a política editorial nem substituir o papel do editor-chefe na emissora.

## Cenário C03 — Decupagem manual de lances por jogador sob restrições de hardware

**Autor:** Giovanni Chahin Morassi, 22.123.025-3  
**Persona relacionada:** [P03, Jorginho Jr.](03_personas_contexto_jornada.md#persona-p03--jorginho-jr)  
**Necessidade relacionada:** R04, reduzir a busca manual e obter cortes de várias partidas para produção amadora; e R05, viabilizar o preparo de materiais com equipamento limitado  
**Situação de origem:** [Entrega 1, seção 3.3 e seção 5.3](01_conhecendo_o_problema.md#33-qual-atividade-parece-mais-frequente-por-quê), H07 e H13  
**Hipóteses relacionadas:** H01, H06, H08, H10, H11, H13, H19, H24, H25, H28, H36, H37 e H38

### 1. Cenário inicial

Jorginho Jr. é um criador de conteúdo amador que produz compilações e vídeos de melhores momentos focados em jogadores específicos para publicar em seu canal. Hoje, passa dias inteiros baixando gravações completas de múltiplas partidas e percorrendo-as manualmente em seu computador modesto para tentar identificar e recortar as jogadas em que o atleta de interesse participa. Com capacidade de processamento fraca e pouco espaço de armazenamento livre, seu computador frequentemente engasga ou trava ao manipular vídeos longos em alta resolução, e o esforço de decupagem manual repetitiva em vários jogos de 90 minutos é exaustivo e sujeito a omissões e perda de arquivos.

Essa é a premissa definida pelo autor para C03. O relato reflete a realidade de produção independente sem infraestrutura profissional de hardware ou licenças de softwares avançados. O cenário e seus desdobramentos são hipotéticos e ainda precisam de validação empírica com criadores amadores.

### 2. Questões de refinamento

| Elemento | Questão que a premissa deixa em aberto | Resposta adotada para a narrativa e origem | O que investigar com usuários |
|---|---|---|---|
| Ambiente/contexto | Em que condições e com quais equipamentos Jorginho realiza a decupagem das partidas? | Em seu quarto residencial, à mesa do computador doméstico, utilizando um PC com configurações modestas de processador/memória e armazenamento quase no limite, com boa conexão de internet. Contexto de P03, H13, H37 e recorte amador confirmado pelo autor. A busca abrange várias partidas completas de um atleta para montar um compilado temático. | Configurações reais de hardware dos criadores amadores, espaço médio disponível em disco, formato e tamanho dos arquivos baixados e tempo despendido por vídeo. |
| Ator | A dificuldade decorre de pouca familiaridade com edição de vídeo? | Jorginho tem prática intuitiva com editores simples e mobile (como CapCut), sem formação técnica em edição audiovisual ou programação. A dificuldade é sustentar a atenção visual procurando um único atleta entre 22 jogadores em vídeos longos e lidar com a lentidão e engasgos de uma máquina fraca. P03, H05, H19, H37 e H38. | Editores e aplicativos habitualmente utilizados (mobile/desktop), termos familiares, conhecimento prático de edição e como organizam os arquivos de projeto. |
| Objetivo | O que precisa estar pronto ao final desta etapa de decupagem? | Um conjunto selecionado de cortes curtos contendo as melhores jogadas (dribles, finalizações, assistências e desarmes) do atleta-alvo extraídas de três jogos distintos, com contexto temporal suficiente para seguir para a montagem e pós-produção externa no canal. P03, H06, H28 e H36. | Quantidade média de clipes necessária para um compilado típico, critérios para julgar o lance como aproveitável para a audiência e formato final esperado de vídeo. |
| Planejamento | Como pretende garimpar os lances do jogador nas partidas e lidar com o espaço em disco? | Baixa uma partida por vez devido ao armazenamento limitado em disco. Abre a gravação no editor local, acelera a reprodução e tenta rastrear o número da camisa do atleta. Planeja recortar os lances do jogador, exportar os clipes pequenos e apagar o arquivo bruto de 90 minutos para liberar espaço antes de baixar o jogo seguinte. Estratégia de contorno baseada em P03, H11, H36 e H37. | Fluxo real de gerenciamento de arquivos em disco, estratégias de busca visual (avançar em 2x, pular minutos, consultar cronogramas) e como evitam perdas. |
| Ações | O que faz ao localizar visualmente o atleta participando de uma jogada? | Reduz a velocidade para 1x, retrocede alguns segundos na linha do tempo para capturar a origem da jogada, define os marcadores de início e fim, fatia o clipe e o salva na pasta do projeto. Quando a linha do tempo engasga por sobrecarga, aguarda ou força o encerramento de outros programas. P03, H01, H11, H36 e H37. | Como definem a margem de tempo de cada corte, nomenclatura e organização de pastas locais, e métodos de recuperação ao sofrer travamentos. |
| Eventos | Que ocorrência torna o problema e as limitações de recursos visíveis? | Durante a decupagem da segunda partida, ao tentar aplicar um corte e pré-visualizar uma sequência de drible do atleta, o editor congela por consumo excessivo de memória RAM e esgotamento do disco de cache temporário. O programa encerra repentinamente, corrompe o arquivo do projeto e faz Jorginho perder mais de uma hora de marcações não salvas. P03, H13, H16 e H37. | Frequência de falhas técnicas locais (travamentos, falta de espaço em disco, perda de projetos) e impacto disso na motivação e continuidade do canal. |
| Avaliação | Como Jorginho reage à perda de tempo e avalia o resultado do material obtido? | Constata que perdeu horas de esforço não salvo, reavalia se vale a pena conferir a partida inteira de novo ou fatiar de forma apressada, e percebe que cortes rápidos deixaram de fora lances decisivos. Reconhece que o hardware modesto torna insustentável manter a frequência do canal com o fluxo manual atual. P03, H01, H10, H11, H36 e H37. | Como equilibram o cansaço mental da busca manual, a tolerância a falhas do equipamento e a qualidade/frequência dos vídeos publicados. |

### 3. Cenário refinado

Os parágrafos identificados com **[NOVO]** desenvolvem a premissa inicial. Os detalhes são uma construção narrativa baseada nas hipóteses acima, sem atribuição de falas ou observações a participantes reais.

**[NOVO]** Em uma tarde de sábado, em sua casa, Jorginho Jr. prepara o próximo vídeo para seu canal esportivo no YouTube. Ele pretende produzir um compilado temático de melhores momentos destacando a atuação de uma jovem promessa do futebol em seus três últimos jogos. Sentado à mesa do quarto, utiliza um computador de mesa modesto, equipado com processador antigo, memória RAM limitada e um disco rígido quase cheio, embora conte com uma conexão de internet de boa velocidade. Jorginho tem familiaridade intuitiva com editores de vídeo simples e aplicativos mobile, mas não domina softwares profissionais de pós-produção nem técnicas avançadas de gerenciamento de mídias pesadas.

**[NOVO]** Devido ao pouco espaço disponível no disco rígido, Jorginho não consegue baixar as três gravações completas de uma só vez, já que cada partida em alta definição ocupa dezenas de gigabytes. Ele adota como estratégia trabalhar uma partida por vez: baixa o primeiro jogo da internet, importa o arquivo bruto para o editor de vídeo que costuma utilizar e planeja garimpar manualmente cada lance em que seu jogador favorito toca na bola. Seu plano é fatiar os trechos do atleta, salvar esses pequenos cortes em uma pasta de favoritos e em seguida apagar o vídeo de 90 minutos do computador para liberar espaço e poder baixar a partida seguinte.

**[NOVO]** Para encontrar as jogadas sem precisar assistir aos 90 minutos em tempo real, Jorginho acelera a reprodução e tenta acompanhar visualmente o atleta em meio aos 22 jogadores na tela. Quando identifica a camisa do jogador recebendo a bola, desacelera o vídeo, volta alguns segundos na linha do tempo para capturar a construção do lance, define os limites do corte e separa o trecho. O processo exige concentração contínua e gera incerteza: ao avançar a gravação de forma acelerada para economizar tempo, teme ter pulado uma movimentação importante sem a bola ou um passe decisivo. Ainda assim, conclui a primeira partida, exporta os clipes obtidos e apaga a gravação original para liberar o disco.

**[NOVO]** Ao baixar e abrir a segunda gravação, o acúmulo de horas de trabalho e as limitações de hardware começam a cobrar seu preço. O computador esquenta, a memória RAM chega ao limite com o acúmulo de arquivos temporários de cache e o sistema operacional emite alertas intermitentes de armazenamento insuficiente. A reprodução na linha do tempo fica engasgada, com quedas constantes de quadros que dificultam enxergar o número da camisa do atleta. Visualmente exausto após horas diante do monitor, Jorginho passa a acelerar ainda mais os trechos, delimitando os cortes de forma apressada e seca, suprimindo o início das jogadas para tentar terminar logo a tarefa.

**[NOVO]** A fragilidade desse fluxo manual em equipamento limitado atinge o ponto crítico durante a decupagem de um contra-ataque decisivo da segunda partida. Enquanto tenta retroceder a agulha de reprodução para capturar o drible que originou o lance, a interface do editor trava por completo. O cursor do mouse vira um círculo giratório de carregamento, o sistema operacional para de responder e, após alguns segundos de congelamento, o programa fecha inesperadamente devido ao estouro de memória e à falta de espaço no disco de cache. Ao reabrir o software, Jorginho descobre que o arquivo de projeto foi corrompido e que mais de uma hora de marcações e cortes realizados naquela partida foram perdidos.

**[NOVO]** Diante do prejuízo, Jorginho precisa gastar quase uma hora apagando arquivos pessoais e limpando caches do sistema para conseguir reabrir o editor com estabilidade mínima, precisando recomeçar o garimpo da segunda partida do zero. O desgaste acumulado atrasa todo o cronograma de publicação do canal no fim de semana, deixando a terceira partida pendente por falta de tempo e esgotamento mental. Ao revisar os poucos cortes que conseguiu salvar, percebe que muitos ficaram curtos demais e sem contexto. Ele encerra a noite desanimado, questionando se conseguirá manter o sonho de crescer como criador de conteúdo digital sem uma forma eficiente de receber os lances do jogador já recortados e sem sobrecarregar sua máquina.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ambiente ou contexto | Quarto residencial, mesa do computador doméstico, PC com configurações modestas de processamento e pouco armazenamento livre, boa conexão de internet e objetivo de produzir conteúdo amador no fim de semana. |
| Ator | Jorginho Jr., P03, criador de conteúdo esportivo amador, sem formação técnica em computação ou edição profissional. |
| Objetivo | Isolar e extrair lances de um jogador específico a partir de várias partidas gravadas, gerando cortes curtos e contextuais para montar compilações em ferramentas externas e publicar em seu canal. |
| Planejamento | Baixar e decupar uma partida por vez para contornar o limite de armazenamento; acelerar a reprodução para rastrear o atleta; fatiar e salvar clipes individuais e apagar os arquivos brutos pesados antes da próxima partida. |
| Ações | Baixar gravação, importar no editor local, acelerar reprodução, rastrear visualmente a camisa do atleta, desacelerar, retroceder na linha do tempo, marcar início e fim de cortes, excluir arquivos pesados para liberar espaço e reiniciar o sistema após crash. |
| Eventos | Emissão de alertas de disco cheio pelo sistema operacional, engasgos severos na reprodução da linha do tempo e congelamento do software de edição com encerramento forçado e perda do projeto da segunda partida. |
| Avaliação | Julgar se uma movimentação do atleta é relevante, notar cortes secos sem contexto feitos por pressa, constatar a perda de horas de trabalho após o crash e avaliar a inviabilidade de sustentar a frequência do canal com o fluxo manual em máquina limitada. |
| Recursos e informações | Gravações completas de futebol em alta definição, computador modesto com CPU/RAM limitadas e pouco espaço livre em disco, editor de vídeo amador, conexão de internet e conhecimento visual do estilo de jogo do atleta. |
| Problemas e rupturas | Hardware sobrecarregado por arquivos pesados, esgotamento de memória e disco de cache, fadiga visual ao rastrear um atleta entre 22 jogadores, cortes sem contexto por pressa e travamento catastrófico com perda de dados. |
| Consequências | Horas de esforço perdidas, necessidade de retrabalho integral da segunda partida, cancelamento do planejamento da terceira partida, atraso no cronograma de publicação e frustração com o risco de desistência do canal. |

Planejamento e avaliação descrevem atividades mentais; ações descrevem comportamentos observáveis. No episódio do travamento, o congelamento da interface e o fechamento abrupto do software configuram os eventos, a percepção do tempo perdido e o sentimento de desânimo com a limitação da máquina constituem a avaliação, e a exclusão de arquivos para liberar espaço e o reinício da decupagem formam as ações decorrentes.

### 5. Implicações para as próximas entregas

Para a [Entrega 5](05_analise_tarefas.md), C03 oferece como tarefa de origem **garimpar e decupar lances de um jogador específico em partidas gravadas para compilação em ferramenta externa**. A análise deve detalhar o recebimento e armazenamento provisório dos arquivos brutos, a busca visual do atleta na linha do tempo, a delimitação temporal dos trechos, a gestão de arquivos em disco limitado e os fluxos de recuperação diante de travamentos e perda de trabalho. Essas atividades evidenciam como a ausência de automação e as restrições de infraestrutura criam gargalos severos para o criador de conteúdo amador.

Ao modelar o uso proposto, as relações R04 e R05 ligam esse problema às capacidades centrais do TCC. A relação R05 contempla o envio de gravações e o acompanhamento remoto (atividades A01 e A02), transferindo o processamento pesado de visão computacional para o servidor remoto e contornando as restrições locais de CPU e armazenamento de P03 (H37 e RC12). A relação R04 abrange a revisão, seleção e download de cortes leves e metadados estruturados (atividade A04), permitindo ao criador baixar apenas os trechos que realmente importam, identificados por partida e com timecodes legíveis (RC05 e RC09), para então realizar a edição estética e musical em editores amadores de desktop ou mobile (H38 e RC05). A possibilidade de filtrar diretamente os lances pelo atleta de interesse (H36) permanece como necessidade a investigar com a equipe técnica quanto à viabilidade no backend, preservando a autonomia do criador na seleção final dos trechos. Os modelos HTA, GOMS e CTT para essas tarefas serão estruturados na Entrega 5.

A coleta de dados (para a [Entrega 7](07_coleta_dados.md)) deverá investigar a configuração típica de hardware e armazenamento de criadores amadores; quanto tempo despendem decupando jogos versus montando o vídeo final; quais termos e convenções visuais utilizam em editores acessíveis; a frequência de travamentos e perdas de arquivos locais; e como definem e recortam jogadas de atletas específicos para seus canais.

O valor a investigar para o projeto é democratizar o acesso à análise e corte de partidas, permitindo que criadores independentes com equipamentos modestos possam produzir vídeos com agilidade e consistência, delegando o processamento computacionalmente intensivo para a nuvem. C03 evidencia que o fornecimento de cortes leves e contextualizados viabiliza a rotina de produção de P03 sem descaracterizar a natureza humana e criativa da edição audiovisual.

### Referência conceitual

Material de aula, *Cenários de análise/problema*, referenciado a partir de Barbosa e Silva (2010), catalogado em [BIBLIOGRAFIA.md](../BIBLIOGRAFIA.md). As seções teóricas definem a narrativa e seus elementos (ambiente/contexto, atores, objetivos, planejamento, ações, eventos e avaliação), exemplificam ações, dificuldades e consequências, e orientam a elaboração da atividade. A estrutura de cenário inicial, questões e refinamento vem do roteiro deste repositório.

Com a incorporação de C01 (Pedro Custódio), C02 (Lucas Roberto) e C03 (Giovanni Chahin), a entrega contempla a totalidade dos integrantes da equipe, cobrindo os diferentes perfis (editor profissional, supervisor editorial e criador amador) e suas respectivas necessidades na matriz de rastreabilidade.


## Checklist

Checklist da equipe. Os três cenários (C01, C02 e C03) contêm narrativa refinada, os elementos da taxonomia e vínculos na matriz de rastreabilidade (R01, R03, R04 e R05).

- [x] Há um cenário completo por integrante.
- [x] Cada cenário tem título, ator, objetivo, contexto e problema.
- [x] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [x] O texto descreve a situação atual, sem antecipar a solução.
- [x] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”.
- [x] Questões de refinamento acrescentam informação nova.
- [x] O refinamento mostra claramente o que foi adicionado/alterado.
- [x] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [x] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.
