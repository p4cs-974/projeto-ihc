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

O PDF de referência apresenta sete elementos de cenário, mas não define uma taxonomia de perguntas. As questões abaixo estão organizadas por esses elementos. As respostas adotadas vêm da ficha de P01 e das decisões narrativas discutidas e confirmadas com Pedro durante o refinamento de C01. Essa confirmação estabelece o cenário pretendido pelo autor; não constitui validação com usuários.

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

### Referência conceitual

Material de aula, *Cenários de análise/problema*, arquivo disponível em `.ref/`. As páginas 3 e 4 definem a narrativa e seus elementos; as páginas 5 e 6 exemplificam ações, dificuldades e consequências; a página 7 orienta a elaboração da atividade. O PDF atribui o conteúdo a Barbosa e Silva, 2010. A estrutura de cenário inicial, questões e refinamento vem do roteiro deste repositório.

Os demais integrantes devem acrescentar seus cenários com autoria própria. C01 não substitui as análises dos outros membros do grupo.

## Checklist

Checklist da equipe. Os itens permanecem abertos até a incorporação e revisão dos cenários dos demais integrantes. C01 já contém narrativa refinada, os sete elementos do PDF e vínculo com R01.

- [ ] Há um cenário completo por integrante.
- [ ] Cada cenário tem título, ator, objetivo, contexto e problema.
- [ ] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [ ] O texto descreve a situação atual, sem antecipar a solução.
- [ ] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”.
- [ ] Questões de refinamento acrescentam informação nova.
- [ ] O refinamento mostra claramente o que foi adicionado/alterado.
- [ ] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [ ] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.
