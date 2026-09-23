# Entrega 4 — Cenários de análise/problema

**Data:** 17/09/2026
**Status:** 🟨 em andamento; C01 desenvolvido como hipótese, demais cenários pendentes
**Responsabilidade:** 1 análise de cenário por integrante

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

| Elemento | Questão que a premissa deixa em aberto | Resposta adotada para a narrativa e origem | O que investigar com usuários |
|---|---|---|---|
| Ambiente/contexto | Em que condições Rafael faz a seleção? | Um dia de trabalho com várias gravações de partidas encerradas, na sala de edição pouco iluminada da produtora, com computador e tela ampla. Contexto de P01, H12/H13, e recorte diário confirmado pelo autor. O prazo é uma pressão de fundo, sem horário exato. | Quantidade e duração das gravações, tempo disponível e condições reais de trabalho. |
| Ator | A dificuldade decorre de pouca experiência com edição? | Rafael é experiente em edição. A dificuldade aqui é sustentar a atenção e repetir julgamentos ao longo da gravação. P01 e H01/H09/H17. | Experiência, ferramentas usadas e estratégias pessoais para localizar lances. |
| Objetivo | O que precisa estar pronto ao final desta atividade? | Seleções de trechos relevantes das partidas recebidas, com contexto suficiente para seguir à montagem. P01, H06/H11/H28 e desfecho confirmado pelo autor. | Critérios editoriais, quantidade esperada de cortes e como se determina que a seleção está pronta. |
| Planejamento | Como pretende percorrer o material e tratar dúvidas? | Trabalha uma partida por vez e revisa seus cortes antes de começar a próxima. Avança nos períodos que considera pouco promissores e retorna ao perceber uma possível jogada relevante. Mantém candidatos duvidosos para reavaliar, conforme H30. Estratégia confirmada pelo autor, detalhando H11. | Ordem efetiva, uso de anotações e tratamento de trechos duvidosos. |
| Ações | O que faz ao encontrar um lance? | Reproduz, avança, pausa, retorna ao início da jogada, delimita o trecho e o separa para revisão. Com o cansaço, delimita os cortes com menos cuidado e precisa rever decisões. Detalhamento de H01/H09/H11 confirmado pelo autor. | Como registra os trechos, define seus limites e evita refazer trabalho. |
| Eventos | Que ocorrência torna o problema visível? | Na revisão de uma das últimas partidas do dia, a reprodução de um corte começa com a finalização e deixa de fora a construção da jogada. Episódio de H11 escolhido com o autor para tornar visível a queda de qualidade. | Ocorrência e frequência de cortes inadequados e como são percebidos. |
| Avaliação | Como Rafael interpreta o corte e decide o próximo passo? | Julga que falta contexto, volta ao original e amplia o trecho. Ao final, distingue a qualidade dos cortes revisados da dúvida sobre lances que podem ter passado despercebidos. Construção hipotética apoiada em H09/H10/H11. | Como confere a cobertura da partida e equilibra revisão, cansaço e prazo. |

### 3. Cenário refinado

Os parágrafos identificados com **[NOVO]** desenvolvem a premissa inicial. Os detalhes são uma construção narrativa baseada nas hipóteses acima, sem atribuição de falas ou observações a participantes reais.

**[NOVO]** Em um dia de trabalho na produtora de conteúdo esportivo, Rafael recebe as gravações integrais de várias partidas já encerradas e precisa selecionar seus melhores momentos. Trabalha numa sala de edição com pouca luz, diante de um computador com tela ampla. As seleções precisam ficar prontas a tempo de continuar a montagem dos vídeos. Rafael conhece as ferramentas de edição, mas localizar os lances dentro de gravações extensas ocupa horas do seu dia.

**[NOVO]** Rafael decide trabalhar uma partida por vez e revisar os cortes selecionados antes de começar a seguinte. Abre a primeira gravação no editor que já utiliza e procura gols, defesas, finalizações perigosas e ocorrências disciplinares relevantes para contar o que aconteceu no jogo. Quando tem dúvida sobre um candidato, prefere separá-lo provisoriamente e decidir durante a revisão.

**[NOVO]** Ao percorrer o vídeo, avança nos períodos que considera pouco promissores. Quando percebe uma possível jogada relevante, retorna a um ponto anterior e assiste à sequência. Pausa, decide onde o corte deve começar para preservar o contexto e até onde precisa ir para mostrar o desfecho. Separa o trecho e retoma a procura. Antes de abrir a próxima partida, reproduz os cortes escolhidos, reavalia os candidatos duvidosos e ajusta os limites que considera inadequados.

**[NOVO]** Nas gravações seguintes, Rafael repete esse processo. Com o acúmulo de horas, a busca se torna mentalmente exaustiva e a qualidade do trabalho começa a cair. Ele delimita os trechos com menos cuidado e passa a duvidar de decisões que antes tomava com segurança. Retorna a passagens já examinadas para conferir se as avaliou bem. Avançar pelo vídeo ajuda a percorrer o material, mas também deixa a dúvida de ter pulado algum lance relevante. As conferências e correções consomem parte do tempo disponível para a montagem.

**[NOVO]** Na revisão de uma das últimas partidas do dia, Rafael reproduz uma finalização perigosa e percebe que o corte começa quando o jogador já está chutando. Falta a sequência anterior que explica como a oportunidade surgiu. Considera o trecho insuficiente, localiza novamente a jogada na gravação original e amplia seu início. Depois, assiste ao corte corrigido para conferir se a jogada ficou compreensível. O cuidado insuficiente na seleção exigiu uma nova busca e mais uma revisão.

**[NOVO]** Rafael termina as seleções das partidas recebidas e segue para a montagem exausto, com menos tempo disponível para concluir os vídeos. Conseguiu revisar os trechos escolhidos, mas essa conferência não elimina sua dúvida sobre possíveis lances ignorados durante os avanços. Rever integralmente as gravações exigiria mais tempo e atenção. Ao encerrar a seleção, leva consigo essa incerteza, além do desgaste acumulado e do tempo gasto refazendo cortes.

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
**Persona relacionada:** [P02, Administrador/Editor-Chefe](03_personas_contexto_jornada.md#persona-p02--administradoreditor-chefe)  
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
=======
### Referência conceitual

Material de aula, *Cenários de análise/problema*, arquivo disponível em `.ref/`. As páginas 3 e 4 definem a narrativa e seus elementos; as páginas 5 e 6 exemplificam ações, dificuldades e consequências; a página 7 orienta a elaboração da atividade. O PDF atribui o conteúdo a Barbosa e Silva, 2010. A estrutura de cenário inicial, questões e refinamento vem do roteiro deste repositório.

Os demais integrantes devem acrescentar seus cenários com autoria própria. C01 não substitui as análises dos outros membros do grupo.


## Checklist

Checklist da equipe. Os itens permanecem abertos até a incorporação e revisão dos cenários dos demais integrantes. C01 já contém narrativa refinada, os sete elementos do PDF e vínculo com R01.

- [ ] Há um cenário completo por integrante.
- [x] Cada cenário tem título, ator, objetivo, contexto e problema.
- [x] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [x] O texto descreve a situação atual, sem antecipar a solução.
- [x] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”.
- [x] Questões de refinamento acrescentam informação nova.
- [x] O refinamento mostra claramente o que foi adicionado/alterado.
- [x] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [x] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.
