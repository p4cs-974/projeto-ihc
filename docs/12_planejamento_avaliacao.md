# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 18/11/2026\
**Status:** 🟨 plano e instrumentos preparados. Piloto pendente.\
**Responsabilidade:** 1 solução por equipe. Equipe 16, Pedro Alexandre Custódio Silva, Lucas Roberto Boccia dos Santos e Giovanni Chahin Morassi.

## Objetivo da atividade

Planejar a avaliação antes de executá-la, ligando perguntas de avaliação a métodos, participantes, tarefas, métricas, aspectos práticos, ética e forma de análise.

## O que está sendo avaliado

Avaliar como editores esportivos e criadores amadores usam o protótipo **Melhores Momentos** para preparar um lote, acompanhar a análise, revisar lances e obter material para edição. A precisão do detector, a cobertura dos lances e o desempenho do modelo pertencem à avaliação técnica do TCC. O tempo da análise encenada é uma condição do teste de interação.

A revisão publicada em 13/11/2026 usa quatro tempos de duas partidas do SoccerNet-v2 e oito cortes reais, com resultados derivados das anotações do conjunto. Fila, progresso, conclusão, falha, nova tentativa e cenário sem lances são encenados. A demonstração utiliza arquivos de exemplo. Montagem, chancela e publicação acontecem em ferramentas externas. [Protótipo avaliado](https://ihc-11.p4cs.com.br/) · [Entrega 11](11_figma.md) · [Manifesto dos exemplos](../assets/06_prototipos/media/manifest.json).

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | Verificar se P01 e P03 conferem o lote, reconhecem o fim da análise, localizam e interpretam um lance e obtêm a seleção correta para editar. Medir independência, tempo de localização e facilidade percebida conforme MQ01–MQ04 e MU01–MU06. Registrar erros e planejar o retorno para MU07 e MU08, propostas da Entrega 8. |
| **E — Explore the questions** | Usar QA01–QA10 abaixo. As perguntas distinguem comportamentos observáveis, compreensão das saídas e problemas que os avaliadores podem encontrar na interface. |
| **C — Choose the evaluation paradigm and techniques** | Fazer inspeção heurística na Entrega 13. Cada integrante percorre F01–F06 e os estados do formulário, aplicando H1–H10 individualmente antes de consolidar. Na Entrega 14, observar tarefas com participantes de P01 e P03. A inspeção localiza problemas de interface e a observação mostra onde surgem dificuldades e quais estratégias as pessoas usam. Comparar os achados pela causa e pelo estado da interface. |
| **I — Identify the practical issues** | Recrutar três adultos externos à equipe. Usar computador em sessão remota moderada, com a mesma versão, dados e estado inicial por tarefa. Fazer um piloto e revisar as instruções, os gabaritos, os limites de interrupção e o registro antes da coleta. |
| **D — Decide how to deal with ethical issues** | Obter aceite antes da coleta e registrar observações por código. Pedir autorizações específicas para gravar a aba do protótipo e para usar trechos no vídeo ilustrativo da Entrega 14. Restringir o acesso aos registros, explicar a retirada e permitir que a pessoa pule perguntas, pause ou encerre. |
| **E — Evaluate, interpret and present the data** | Consolidar por participante, tarefa e perfil. Conferir os arquivos salvos e as respostas contra o gabarito, comparar os indicadores às metas e reunir problemas da inspeção e da observação em uma lista priorizada. |

[Planejamento da Avaliação de IHC, slides 25–27 e 37–38](../slides_plinio/Planejamento%20Avaliacao%20IHC.pdf) · [Avaliação de Usabilidade por Inspeções, slides 16–17](../slides_plinio/Avaliacao%20Usabilidade%20Inspecoes.pdf) · [Teste de Usabilidade por Observação, slides 6–7 e 15–16](../slides_plinio/Teste%20Usabilidade%20Observacao%20Usuario.pdf) · [Palestra de Felipe Melo sobre testes remotos](https://www.youtube.com/watch?v=zjKaHb6erzQ) · [Metas e critérios da Entrega 8](08_engenharia_usabilidade.md#3-metas-de-usabilidade).

## B. Perguntas de avaliação

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | A pessoa confere quais gravações entraram no lote e retira a entrada pedida? | Observação, UT01 | Partidas e tempos identificados na interface e lista resultante. Registrar à parte a confirmação de que os vídeos são de exemplo, informação dada no consentimento. | Conferência independente de MQ01. Identificar as duas partidas e seus quatro tempos e retirar apenas o tempo indicado. |
| QA02 | A pessoa entende o estado da análise e chega à base depois de concluída? | Observação, UT02 | Estados exibidos e interpretados, momento e caminho do primeiro acesso à base, ajuda | MQ02. Distinguir espera, andamento e conclusão. MU01. Todos os participantes avaliáveis de cada perfil acessam a base pela primeira vez de forma independente, após a conclusão natural. |
| QA03 | Com oito candidatos, a pessoa localiza e abre o lance indicado? | Observação, UT03 | Detalhe aberto, tempo total, esperas técnicas e tempo ajustado | MU05. Mediana ajustada de até 90 s nas conclusões independentes de cada perfil. |
| QA04 | A pessoa distingue origem, tempo da partida e referências de tempo em um corte do segundo tempo? | Observação, UT04 | Resposta inicial sobre partida, tempo e diferença entre relógio do jogo e posição no arquivo, além do julgamento sobre contexto | MQ03 e MU02. Todos os participantes avaliáveis de cada perfil acertam os três itens sem explicação prévia. Registrar se a pessoa precisaria do original e por quê. |
| QA05 | A pessoa corrige a seleção e obtém a relação solicitada para edição? | Observação, UT05 | Seleção antes e depois, linhas do CSV salvo e explicação sobre retirada, conteúdo e uso das saídas | MQ04 e MU03. Todos os participantes avaliáveis de cada perfil obtêm exatamente os dois IDs previstos com as origens corretas e entendem que o CSV contém referências e links. |
| QA06 | A pessoa obtém o vídeo correto e entende onde continuar o trabalho? | Observação, UT06 | Arquivo salvo, reprodução do lance e explicação inicial sobre a continuidade | MU04. Todos os participantes avaliáveis de cada perfil obtêm o MP4 correto sem orientação. Conferir a reprodução do arquivo salvo. Para MQ04, verificar separadamente se a pessoa distingue o vídeo da relação de referências e entende onde ocorre a montagem e a aprovação. |
| QA07 | Quão fáceis a pessoa considera a continuidade da análise e a obtenção dos dois tipos de saída? | Pós-tarefa, UT02, UT05 e UT06 | Nota de 1 a 5 e motivo, inclusive após dificuldade ou falha | MU06. Mediana de pelo menos 4 por tarefa e perfil. |
| QA08 | Que erros ocorrem ao retirar uma entrada, mudar a seleção ou obter um arquivo? | Observação, UT01, UT05 e UT06 | Ação, gravidade, percepção, correção e efeito no resultado | MU07, proposta. Em cada perfil, todas as tentativas avaliáveis terminam sem erro não corrigido e com no máximo um erro corrigido pela própria pessoa. |
| QA09 | Depois de pelo menos sete dias, a mesma pessoa reencontra a base, localiza outro lance equivalente e obtém novo CSV? | Observação de retorno, UT08 | Conclusão independente nas três partes, tempo de localização e conferência do CSV | MU08, proposta. Todas as tentativas avaliáveis de retorno de cada perfil cumprem as três partes. |
| QA10 | O estado de falha explica o que ficou incompleto e permite continuar com os resultados disponíveis? | Inspeção, F03/F04, H1, H3, H5 e H9. Observação, UT07 | Evidência da mensagem, alcance da recuperação, interpretação, ação e estado final | Identificar o vídeo incompleto e o efeito nos demais. Continuar a revisão com a pendência ou solicitar nova tentativa apenas do vídeo afetado. Esta pergunta tem análise qualitativa. |

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | Editores profissionais de vídeo esportivo (P01) e criadores amadores (P03). A supervisão editorial (P02) recebe o material externamente. O teste cobre o preparo das saídas para esse repasse. |
| Critérios de inclusão/exclusão | Ter pelo menos 18 anos e ter selecionado ou recortado lances de partidas encerradas nos últimos seis meses. Para P01, a atividade integra o trabalho profissional. Para P03, é produção própria ou amadora, inclusive com remuneração ocasional. Excluir integrantes da Equipe 16 e pessoas cuja experiência seja apenas assistir ou supervisionar. |
| Nº de participantes | Três sessões principais individuais, uma por integrante, conforme o [modelo da Entrega 14](14_observacao_usuario.md). Recrutar dois participantes P01 e um P03. A amostra é exploratória. O plano de execução do Moodle cita 5 a 10 como faixa usual. |
| Ambiente | Sessão remota individual em sala virtual institucional. Enviar instruções técnicas antes da sessão e preparar a sala com 15 min de antecedência. Validar no piloto o controle remoto do navegador e o efeito sobre o tempo. Reservar 45 min para a primeira sessão e 25 min para o retorno. |
| Dispositivo | Computador de teste da equipe com navegador capaz de reproduzir MP4, mouse ou teclado, internet e pasta temporária para downloads. A pessoa controla o navegador durante as tarefas. O moderador verifica os arquivos locais conforme o roteiro. |
| Protótipo/versão | Usar a [publicação da Entrega 11](https://ihc-11.p4cs.com.br/) e a [fonte da revisão](../assets/06_prototipos/PROTOTIPO_fluxo_highlights.html), registradas no commit `7405221`. Registrar URL, data e commit efetivos em cada sessão. Se a inspeção motivar uma correção antes da observação, registrar o que mudou, repetir o piloto afetado e fixar a nova versão. Consolidar cada versão separadamente. |
| Teste piloto | Após consolidar a inspeção e antes da primeira sessão oficial, Pedro modera, Lucas anota e Giovanni executa o roteiro em um computador separado. Validar instruções sem atalhos, estados iniciais, duração, captura de tela autorizada, sala alternativa, cronômetro, gabaritos, downloads, recuperação e aplicação das categorias de sucesso por dois integrantes. Use o código PIL01. O piloto fica fora da amostra. |
| Recrutamento | Convidar por contatos e comunidades de edição e futebol. Confirmar idade, atividade recente, perfil e disponibilidade para a sessão inicial e o retorno. Registrar exposição prévia ao guia ou ao protótipo. |
| Contingência | Se faltar um dos perfis, priorizar outra pessoa elegível do outro perfil. Se for necessário recorrer a um proxy, usar adulto externo com experiência recente em seleção ou edição de vídeo em domínio próximo. Registrar a lacuna e o motivo antes da sessão. Reportar os proxies à parte. Marcar metas sem tentativas avaliáveis de um perfil como não avaliadas. |
| Divisão proposta | Pedro modera U01 (P01), Lucas modera U02 (P01) e Giovanni modera U03 (P03). Lucas anota U01, Giovanni anota U02 e Pedro anota U03. A mesma dupla acompanha o retorno. Os códigos e a distribuição são reservas de agenda. |
| Riscos técnicos | Verificar manifesto, mídia, rede, permissões de download e espaço livre antes da sessão. Para MU01, manter a aba da análise visível até o fim natural. Se a sala falhar, usar a sala alternativa ou o canal de contato combinado. Se a interação continuar instável, reagendar a sessão remota. Se for preciso recorrer ao presencial, registrar a modalidade. Quando uma falha externa impedir uma tentativa, registrar a causa e seguir a regra de tentativa não avaliável. |

### Sequência de trabalho

| Marco | Responsável | Entrega do marco |
|---|---|---|
| Antes da inspeção | Os três integrantes | Fixar a versão, abrir uma cópia do formulário por avaliador e combinar a cobertura de telas e estados. Iniciar o recrutamento para os dois perfis. |
| Entrega 13 | Os três integrantes | Preparar o fluxograma da inspeção, fazer inspeções individuais, consolidar achados e registrar a versão a observar após eventuais correções. |
| Antes da primeira sessão | Pedro, Lucas e Giovanni no piloto | Preparar o fluxograma de observação e simular toda a sessão, incluindo a contingência remota. Registrar a data, problemas e ajustes no roteiro. Alinhar com o docente o vídeo ilustrativo e o formato alternativo caso ninguém autorize o uso de trechos. Confirmar com a equipe as propostas MU07, MU08 e pesos da Entrega 8. Se houver calibração de critério ou tempo, registrar a mudança antes da coleta. |
| Entrega 14, sessão inicial | Duplas de moderação e registro | Obter aceite e executar UT01–UT07. Reservar o retorno com quem puder participar. |
| Entrega 14, retorno | Mesmas duplas | Aplicar UT08 às mesmas pessoas, após pelo menos sete dias sem usar o protótipo. Confirmar o intervalo no começo da sessão. Se o calendário, a ausência ou o uso no intervalo impedir o retorno válido, registrar a causa e a cobertura de MU08. |
| Após as sessões | Equipe | Conferir as fichas, sintetizar evidências e publicar os achados desidentificados, os limites da amostra e as decisões sobre o protótipo. Preparar o vídeo ilustrativo e incluir o link de acesso restrito no relatório da Entrega 14. |

## D. Lista de tarefas de avaliação

Leia apenas a coluna **Cenário neutro entregue ao usuário**. Os objetivos e critérios ficam com a equipe. Os cenários vêm de C01 e C03, com continuidade editorial de C02. [Cenários de problema](04_cenarios_problema.md) · [Tarefas T01–T03](05_analise_tarefas.md) · [Modelos de interação M01–M03](10_molic.md).

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 | "Você vai preparar um resumo de duas partidas. Confira quais partidas e tempos estão disponíveis e deixe de fora o segundo tempo de Bayern de Munique contra Real Madrid. Mostre onde conferiu o que ficou no lote e avise antes de iniciar a análise." | A01, O01, M03, F01–F02. Conferir o lote, MQ01 e MU07. | Identifica as duas partidas e seus quatro tempos na interface. Ao final, deixa três vídeos no lote com apenas a entrada pedida removida. Registrar o reconhecimento da origem dos vídeos à parte, como confirmação de contexto. | 3 min |
| UT02 | "Agora você recebeu o lote completo. Coloque os vídeos para análise. Enquanto acompanha, diga quais estão esperando, quais estão em andamento e quando terminaram. Quando tudo estiver pronto, abra o material disponível para revisão." | T03 → T01, O02/O04, M03, F02–F04. Verificar MQ02, MU01 e MU06. | Abre a base de oito candidatos pela primeira vez após a conclusão natural. Se houver acesso antecipado, o critério de MU01 fica por cumprir mesmo que a pessoa retorne e abra a base novamente. Registrar a compreensão dos estados separadamente para MQ02. | 6 min |
| UT03 | "Encontre e abra o gol que ocorreu por volta de 52 minutos de jogo, no segundo tempo de Real Madrid contra Barcelona." | T01, O04, M01, F04–F05. Medir localização, MU05. | Abre o detalhe de `iniesta`, 52:17. | 4 min |
| UT04 | "Uma colega precisa localizar na gravação o lance aberto. Diga de qual partida e tempo ele veio. Explique o que os tempos mostrados dizem sobre o jogo e sobre onde achar o trecho no arquivo. Você precisaria rever a gravação antes de usar o lance? Por quê?" | T01, O05, M01, F05. Verificar MQ03 e MU02. | Identifica Real Madrid contra Barcelona, segundo tempo, e explica a diferença entre 47:55 no jogo e o intervalo 2:43 a 3:10 no arquivo desse tempo. Justifica se o corte basta para decidir. | 3 min |
| UT05 | "A relação para a edição já tem o gol de Neymar. A pauta mudou. Deixe na relação somente o gol de Suárez e o gol de Vidal. Salve no computador a relação final que você enviaria à produção, com as referências para localizar os trechos. Explique o que o arquivo contém e o que aconteceu com o corte de Neymar." | T01/A04 → T02, O06/O07, M01/M02, F04–F06. Verificar MQ04, MU03, MU06 e MU07. | Retira `neymar`, inclui `suarez` e `vidal` e salva um CSV que contém exatamente esses dois IDs com a origem correta. Reconhece que a retirada afeta só a seleção e que o CSV tem referências e links. | 5 min |
| UT06 | "Seu resumo vai incluir o gol de Cristiano Ronaldo aos 76 minutos de jogo, no segundo tempo de Bayern de Munique contra Real Madrid. Salve o vídeo desse lance e abra o arquivo no computador." | T01/A04 → T02, O07, M01/M02, F05–F06. Verificar MQ04, MU04, MU06 e MU07. | Salva `ronaldo-2.mp4` e confirma sua reprodução local. Para MQ04, registrar separadamente se a pessoa distingue o vídeo da relação de referências e explica onde continuaria a montagem e a aprovação. | 4 min |
| UT07 | "Parte do lote já está disponível, mas uma gravação ficou incompleta. Descubra qual foi e o que isso significa para os demais vídeos. Decida como prosseguir com a revisão sem recomeçar o lote inteiro." | T03, O03, M03, F03/F04. Observar interpretação e reação à falha encenada. | Identifica o primeiro tempo de Bayern de Munique contra Real Madrid como incompleto, reconhece os outros resultados disponíveis e deixa a gravação pendente ou inicia nova tentativa só dela. | 5 min |
| UT08 | "Você voltou para preparar o material de outra rodada. Primeiro, coloque o lote completo para análise e, depois de concluído, abra o material para revisão. Em seguida, encontre e abra o gol de Cristiano Ronaldo por volta de 46 minutos de jogo, no segundo tempo de Bayern de Munique contra Real Madrid. Por fim, na relação que já contém o pênalti perdido de Vidal, deixe somente a defesa do Barcelona e o gol de Iniesta. Salve a relação final de referências e explique o que ficou no arquivo." | Retorno a T03 → T01, O02/O04/O06/O07, M03/M01, F02–F06. Verificar MU08. | Cumpre as três partes de forma independente. Abre a base pela primeira vez após a conclusão natural, conforme UT02. Localiza `ronaldo-1` e salva CSV com `bravo` e `iniesta`, sem `vidal-penalti`, com origens corretas e compreensão do conteúdo. Ler uma parte por vez com os estados iniciais previstos. | 6 min, 4 min e 5 min, respectivamente |

> Uma boa instrução descreve o objetivo do participante sem dizer **onde clicar** ou usar o rótulo exato do controle que está sendo testado.

## E. Instrumentos

- [Consentimento para a observação](../instrumentos/entrega12_consentimento.md)
- [Roteiro do moderador, estados iniciais e gabaritos](../instrumentos/entrega12_roteiro_observacao.md)
- [Ficha privada de observação](../instrumentos/entrega12_ficha_observacao.md)
- [Formulário de inspeção heurística da Entrega 13](../instrumentos/entrega12_formulario_heuristica.md)
- [Perguntas de perfil, pós-tarefa e pós-teste](../instrumentos/entrega12_questionarios.md)

O moderador envia o consentimento antes das tarefas. O participante pode pular perguntas ou desistir. Pedir autorização específica para gravar apenas a aba do protótipo, sem câmera, áudio ou tela inteira, para conferir as notas. Se a pessoa recusar ou o recurso de captura não permitir esse recorte, registrar por escrito.

O vídeo ilustrativo da Entrega 14 apresentará o procedimento, os resultados desidentificados e as melhorias propostas. Usar somente trechos desidentificados da aba com autorização adicional para esse fim. O link no relatório dará acesso à equipe e ao docente da disciplina. Antes da coleta, confirmar com o docente se uma demonstração reencenada pela equipe, com resultados desidentificados das sessões, atende à atividade quando não houver trechos autorizados. Identificar a reencenação no vídeo.

A ficha usa U01–U03. Contatos de agendamento e aceites ficam em pasta institucional privada, separados das notas e gravações, com acesso nominal aos três integrantes. Evitar nomes de pessoas, empresas, canais, credenciais e gravações particulares. A pessoa pode solicitar a retirada dos seus registros pelo canal do convite com seu código, até 30 dias após sua última sessão, antes da consolidação pública. Descartar gravações brutas após conferir as notas e selecionar eventuais trechos autorizados, em até 30 dias da sessão. Descartar contatos após os retornos e demais registros privados, incluindo o vídeo ilustrativo e suas cópias sob controle da equipe, em até 90 dias após o fim da disciplina. Publicar sínteses desidentificadas. Suprimir cruzamentos e trechos que permitam identificar alguém em um grupo pequeno. [Protocolo ético da Entrega 7](07_coleta_dados.md#aspectos-éticos-e-gestão-dos-dados).

## F. Plano de análise

- **Sucesso total, parcial e falha.** Classificar o resultado de cada tentativa.
  - **Total independente.** Cumpre todos os critérios antes do limite, sem instrução externa sobre caminho, controle ou significado. Rótulos e dicas da interface contam como parte do protótipo. Quando a equipe abre o arquivo local que a pessoa baixou e indicou sem orientação, a abertura é uma conferência e preserva a classificação independente.
  - **Total com ajuda.** Cumpre todos os critérios após dica dada durante a tarefa ou já recebida no guia ou em sessão anterior. Conta como conclusão com ajuda. Repetir literalmente a instrução ou relembrar o objetivo da avaliação não conta como ajuda.
  - **Parcial.** Atinge parte do resultado ao atingir o limite ou encerrar. Exemplo em UT05: salva uma relação com apenas um dos dois lances. Registrar os critérios cumpridos.
  - **Falha.** Termina sem resultado utilizável, entrega apenas resultado incompatível ou abandona voluntariamente. Registrar abandono e motivo informado, inclusive se houve progresso.
  - **Não avaliável.** Um fator externo impede julgar a interação, como queda da sala virtual ou falha comprovada da rede. Registrar o motivo e o que ocorreu antes da interrupção. Dificuldade produzida pelo próprio protótipo permanece como evidência de usabilidade.
- **Erros, dúvidas, ajudas e abandono.** Registrar as ocorrências durante a tarefa.
  - **Erro.** Ação com efeito contrário ao cenário, como retirar outro vídeo ou baixar o arquivo errado. Registrar também as autocorreções, percepção e efeito final. Exploração sem efeito contrário e decisão editorial justificada são observações de outra natureza.
  - **Dúvida.** Hesitação com comportamento observável, pergunta ou comentário sobre o que a pessoa entendeu. Registrar ação e contexto. O tempo em silêncio, isoladamente, não é evidência de dúvida.
  - **Ajuda.** Contar cada intervenção que revela um caminho ou significado e anotar o texto ou seu teor. Registrar separadamente pedidos, intervenções e exposição prévia ao guia.
  - **Abandono.** Registrar o momento, o resultado parcial e o motivo, se a pessoa quiser informá-lo. Classificar a tentativa abandonada como falha.
- **Tempo.** Iniciar após leitura e confirmação do cenário, com a condição inicial pronta. Encerrar ao concluir o objetivo observável, desistir ou chegar ao limite. Em UT03 e na busca de UT08, concluir ao abrir o detalhe correto. Registrar início e fim de esperas técnicas no momento em que ocorrerem e subtrair essas esperas do tempo total. Comparar com 90 s a mediana ajustada das conclusões independentes de UT03, por perfil. Exibir também a mediana bruta, a quantidade de tempos, as ajudas e as falhas. Os 90 s são a meta, e a interrupção de UT03 ocorre aos 4 min. A espera na simulação de UT02 entra como contexto da interação.
- **Satisfação pós-tarefa.** Após UT02, UT05 e UT06, perguntar a facilidade em escala de 1 a 5 a todos que tentaram a tarefa, inclusive quem teve dificuldade. Registrar a nota, o motivo e as recusas. Comparar a mediana de cada tarefa e perfil com 4. Usar a nota geral do pós-teste como contexto. Respostas do questionário I02 da Entrega 7 têm outra finalidade e ficam fora desses cálculos.
- **Codificação de observações e falas.** Codificar ações e falas por tela, tarefa e tema, como estado da análise, tempo e origem, seleção, saída ou recuperação. Distinguir ação observada, citação e interpretação do avaliador. Preservar ocorrências que discordem do padrão. Para MQ01–MQ04, apresentar por perfil quais critérios foram demonstrados e a evidência que sustenta cada conclusão.
- **Prioridade dos problemas.** Na inspeção, justificar severidade de 0 a 4 por frequência esperada, impacto e persistência. Na observação, registrar recorrência, consequência e possibilidade de recuperação. Cruzar os achados por problema e tela, preservando os IDs e a versão de origem. Priorizar bloqueios, resultado incorreto sem aviso e problemas recorrentes que gerem retrabalho. Associar cada correção ao artefato e à tarefa correspondente na [rastreabilidade](../RASTREABILIDADE.md).
- **Comparação com as metas e apresentação.** Consolidar as evidências das duas avaliações.
  - **Eficácia e compreensão.** Por tarefa e perfil, dividir o número de sucessos independentes pelo total de tentativas avaliáveis. Incluir como avaliáveis as conclusões com ajuda, os parciais, as falhas e os abandonos da tarefa. Mostrar numerador, denominador e percentual. Quando uma tarefa tiver critérios de duas metas, aplicar cada critério separadamente. Por exemplo, a interpretação dos estados em MQ02 e a chegada à base em MU01 têm registros próprios.
  - **Erros e retorno.** Para MU07, calcular quantas tentativas por tarefa e perfil terminam sem erro não corrigido e com até um erro autocorrigido. Para MU08, comparar a primeira sessão e o retorno por pessoa com os três critérios de UT08 e descrever os tempos de localização com os alvos equivalentes. Informar quantas pessoas retornaram no intervalo válido. Se ninguém de um perfil retornar em condição válida, registrar MU08 como não avaliada para o perfil.
  - **Relatórios.** Na Entrega 13, apresentar o fluxograma da inspeção, as matrizes H1–H10 individuais, as violações com evidência, a consolidação e os dez exemplos didáticos, um por heurística. Na Entrega 14, apresentar o fluxograma de observação, os resultados por participante e tarefa, o quadro de metas por perfil, a comparação com a inspeção e as recomendações priorizadas. Registrar as recomendações de Felipe Melo adotadas e incluir o link restrito do vídeo ilustrativo do teste e dos resultados. Os três participantes formam uma amostra exploratória. No perfil P03, a tentativa única planejada fornece uma observação por tarefa e, quando houver tempo ou nota, a mediana corresponde a esse valor. Identificar esse caso ao apresentar os resultados. Informar os efeitos da simulação, da amostra por conveniência, de eventuais proxies e do conjunto de oito cortes.

## Checklist

- [x] As seis etapas DECIDE foram contextualizadas, não apenas expandidas por sigla.
- [x] Perguntas de avaliação têm método e evidência correspondentes.
- [x] O plano distingue avaliação de IHC de avaliação técnica/científica do TCC.
- [x] Dados ou processamentos simulados no protótipo estão declarados.
- [x] Tarefas vêm de objetivos/cenários relevantes.
- [x] Critérios de sucesso foram definidos antes da coleta.
- [ ] Questões práticas e éticas estão resolvidas.
- [ ] Instrumentos estão prontos antes da Entrega 13/14.
- [x] Plano diz como dados serão analisados e apresentados.

A equipe preparou os cinco instrumentos. Para concluir as duas verificações pendentes, é preciso confirmar agenda, participantes e configuração de gravação, alinhar o vídeo e a alternativa de reencenação com o docente e validar o roteiro e a contingência remota no piloto. A confirmação de MU07, MU08 e dos pesos também está pendente.
