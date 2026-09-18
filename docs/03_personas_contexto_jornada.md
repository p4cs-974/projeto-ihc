# Entrega 3 — Personas, mapa de empatia, contexto de uso e jornada

**Data:** 16/9/2026  
**Status:** 🟩 preenchida como proto-personas; validação com usuários pendente

**Responsabilidade:** 1 persona por integrante; 1 mapa de empatia, 1 contexto de uso consolidado e 1 jornada por equipe (salvo orientação diferente do docente).

## Objetivo da atividade

Representar grupos de usuários de forma útil para decisões de design. Persona não é personagem decorativo: suas características devem alterar requisitos, prioridades, linguagem, fluxos ou critérios de avaliação.

## Atenção a projetos técnicos

Em TCCs sem interface original, a persona pode representar um **profissional que se apropria da contribuição técnica**: DBA, analista, cientista de dados, administrador, pesquisador, técnico, operador, gestor ou especialista de domínio.

Não escolha um perfil apenas porque “parece combinar” com a tecnologia. Explique **qual objetivo esse perfil teria e qual parte da contribuição do TCC produziria valor para ele**. Se ainda for hipótese, mantenha como hipótese/proto-persona a validar.

Também considere papéis diferentes quando houver tarefas distintas, por exemplo:

- operador que executa análises;
- administrador que configura e gerencia permissões;
- especialista que interpreta resultados;
- gestor que consulta relatórios e decide;
- auditor que revisa histórico.

## Entradas da Entrega 1

Antes de criar personas, retome os tipos de usuários, características relevantes, objetivos e hipóteses registradas na Entrega 1. A persona **não deve transformar uma hipótese inicial em fato por meio de uma história fictícia**.

| Item da Entrega 1                                                                      | Status inicial | Evidência disponível agora                                                                        | Como será tratado nesta entrega                                          |
| -------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Editor de vídeo esportivo como usuário prioritário, H03, H21 e H27                     | H              | Entrega 1, seções 2.2 e 7.2; adequação do perfil ainda sem validação com usuários                 | Incorporar como base de proto-persona; manter como hipótese              |
| Obter cortes e metadados com menor esforço manual, H06 e H28                           | H              | Entrega 1, seções 3.1 e 7.3                                                                       | Incorporar como objetivo a validar                                       |
| Selecionar/exportar resultados e processar vídeos em lote, H07 e H08                   | H              | Atividades A01 a A04 da Entrega 1, seção 3.2; frequência e criticidade não confirmadas            | Incorporar atividades; investigar frequência e criticidade               |
| Esforço manual, omissões e retrabalho sob pressão de prazo, H01, H09, H10 e H11        | H              | Situação hipotética da Entrega 1, seção 4.5                                                       | Manter como dores hipotéticas, sem atribuir relatos a participantes      |
| Baixo conhecimento de computação e familiaridade com editores de vídeo, H05, H17 e H19 | H              | Entrega 2, seção 3, identifica padrões nas ferramentas, mas não comprova familiaridade do público | Manter como hipótese; investigar experiência e vocabulário               |
| Pós-produção, arquivos extensos e pressão de prazo, H12 e H13                          | H              | Entrega 1, seções 5.1 a 5.3                                                                       | Incorporar ao contexto provisório                                        |
| Entrega a responsáveis editoriais e decisões sobre resultados, H14, H22 e H23          | H              | Entrega 1, seções 5.4 e 7.1; divisão de responsabilidades não investigada                         | Manter como hipótese; não criar papéis adicionais sem tarefas distintas |
| Histórico e consequências de falhas, H15, H16 e H26                                    | H              | Entrega 1, seções 5.5, 5.6 e 7.1; recomendações RC03 e RC10 da Entrega 2                          | Investigar necessidade de histórico e formas de recuperação              |
| Equipamentos, local, acessibilidade, permissões e retenção                             | ?              | Lacunas registradas na Entrega 1, seções 2.4 e 5                                                  | Manter em aberto para coleta de dados                                    |

Fontes: [Entrega 1](01_conhecendo_o_problema.md), [Entrega 2](02_analise_concorrencia.md) e [registro de hipóteses](../RASTREABILIDADE.md). As referências às outras entregas recuperam o conhecimento da equipe; não constituem nova validação com usuários.

## 1. Personas

### Persona P01 — Rafael

**Autor(a):** Pedro Alexandre Custódio Silva — 22.123.049-3  
**Tipo:** primária  
**Base de evidências:** hipóteses da [entrega 1](01_conhecendo_o_problema.md), ainda não confirmadas com usuários, e análise de ferramentas da [entrega 2](02_analise_concorrencia.md) (decisões de interface).  
**Hipóteses da Entrega 1 relacionadas:** H01, H03, H05, H06, H09, H10, H11, H12, H13, H16, H17, H19, H21, H27 e H28

**Hipóteses novas da Entrega 3:** H30, H31 e H32, acompanhadas no [registro de hipóteses](../RASTREABILIDADE.md#21-hipóteses-acrescentadas-na-entrega-3).

![Avatar da persona Rafael](../assets/03_personas/rafael-avatar.png)

| Campo                             | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Faixa etária / contexto relevante | [?] Faixa etária não investigada. [H] Atuação na pós-produção de partidas encerradas, H12.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Ocupação/papel                    | [H] Editor de vídeo esportivo experiente em uma produtora de conteúdo esportivo, responsável por obter material de melhores momentos. Detalhamento de H03, H21 e H27 definido com o autor, ainda a validar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Conhecimento do domínio           | [H] Identifica lances como gols, defesas, finalizações perigosas e ocorrências disciplinares, conforme a situação de H11. A experiência em edição foi definida com o autor como característica hipotética do perfil; o conhecimento específico de futebol ainda precisa ser validado.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Experiência tecnológica           | [H] Experiente no uso de ferramentas de edição de vídeo, mas sem conhecimento de IA ou programação. Detalhamento de H05 e H17 definido com o autor, ainda a validar; a ferramenta utilizada não foi escolhida.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Objetivos                         | [H] Entregar no prazo uma seleção de lances relevantes, com contexto suficiente, gastando menos tempo procurando e recortando a gravação. Obter cortes e metadados para continuar a produção em ferramentas externas, H06 e H28. Critério de sucesso definido com o autor, ainda a validar com usuários.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Necessidades                      | [H] Reduzir o esforço de seleção e corte, preservar o contexto dos lances e poder conferir manualmente todos os cortes gerados antes de selecionar quais baixar, H01, H10, H11, H16 e H28. O próprio editor é responsável pela revisão, conforme definição do perfil com o autor. Quando uma partida falha, precisa entender o que aconteceu e como prosseguir, sem perder os resultados já concluídos das outras partidas, conforme definição com o autor e H16.                                                                                                                                                                                                                                                                                        |
| Dores/frustrações                 | [H] Prazo curto como pressão principal, acompanhado da preocupação de deixar passar lances importantes durante a seleção manual. Recortes sem contexto e retrabalho podem atrasar a entrega, H01, H09, H10 e H11. Prioridade definida com o autor, ainda a validar. Prefere revisar alguns cortes sem interesse a deixar um lance importante de fora, H30, conforme definição do perfil com o autor.                                                                                                                                                                                                                                                                                                                                                     |
| Motivadores                       | [H] Produzir melhores momentos com eficiência e consistência, H06. Outros motivadores ainda não foram investigados.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Restrições/acessibilidade         | [H] Arquivos extensos, tempo de processamento e pressão de prazo, H13. [?] Necessidades individuais de acessibilidade não investigadas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Ambiente típico de uso            | [H] Trabalho presencial na produtora, em sala de edição com pouca luz e computador com tela ampla, na pós-produção de partidas gravadas. Prefere o modo escuro para conforto no ambiente pouco iluminado, H31. Detalhamento de H12 e H13 definido com o autor, ainda a validar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Comportamentos relevantes         | [H] No processo atual imaginado, percorre a gravação, identifica lances e organiza os trechos, conforme H11. No uso proposto, envia várias partidas para a fila e continua outras edições enquanto aguarda o processamento. Precisa ser avisado quando os cortes estiverem prontos; então revisa uma partida por vez e seleciona o material para download. Ao perceber que falta um lance importante, consulta a gravação original e faz o corte no editor de vídeo que já utiliza. Se o processamento de uma partida falha, procura entender o motivo e a ação necessária para resolver o problema, enquanto continua com as demais. Fluxo definido com o autor, ainda a validar; a organização da espera e da revisão por partida é registrada em H32. |

**Decisões de design influenciadas por P01:**

- Facilitar a revisão e a exclusão de cortes da seleção para download. Conforme H30, Rafael aceita alguns resultados sem interesse para reduzir o risco de omitir lances importantes; essa preferência não garante que o modelo detecte todos os lances.

- Priorizar envio, acompanhamento, revisão e download, conforme RC01 da Entrega 2 e H28.
- Permitir enfileirar várias partidas, identificar o estado de cada uma e avisar quando seus cortes estiverem prontos, para que o editor continue outros trabalhos durante a espera. A organização do trabalho é hipótese H32; o meio de aviso ainda será definido.
- Explorar modo escuro com base na preferência hipotética H31 de P01, mantendo contraste, foco e controles legíveis.
- Permitir assistir a todos os cortes gerados e selecionar quais baixar, com contexto temporal para apoiar a revisão pelo próprio editor, conforme RC04 e RC05, H10, H11 e H16. Conferir os cortes gerados não permite garantir que nenhum lance foi omitido.
- Manter a recuperação de lances omitidos e a edição detalhada no editor externo já utilizado pelo profissional, conforme o fluxo definido com o autor e o recorte da Entrega 1.
- Manter parâmetros técnicos fora do fluxo principal e testar vocabulário do domínio com usuários, conforme RC06 e RC07, H05 e H19.
- Em caso de falha, identificar a partida afetada, explicar o motivo conhecido em linguagem compreensível para Rafael e indicar o próximo passo. Se a causa não for conhecida, informar isso sem inventar uma explicação. Preservar o acesso aos resultados já concluídos e permitir continuar com as outras partidas, conforme H16, H26 e o comportamento definido com o autor.
- Comunicar progresso e falhas em texto e permitir operação por teclado, conforme RC03 e RC11. A acessibilidade é uma recomendação de design da Entrega 2, não uma característica já observada de P01.
- Elemento visualmente semelhante a uma linha do tempo dos softwares de edição de vídeo, assim como um preview.

Essas decisões são iniciais e deverão ser revistas com a coleta de dados.

### Persona P02 — Arnaldo - Administrador/Editor-Chefe

**Autor(a):** Lucas Roberto Boccia dos Santos — 22.123.012-1
**Tipo:** Secundário

**Base de evidências:** proto-persona proposta pelo autor na PR #5, ainda sem validação com usuários.

**Base herdada:** H14, H22 e H23 admitem entrega a responsáveis editoriais e decisões posteriores sobre os resultados. A supervisão de P02 é uma derivação exploratória dessa base.

**Hipóteses novas da Entrega 3:** H33, relação com os resultados; H34, experiência tecnológica específica de P02; H35, possível necessidade de auditoria editorial. Acompanhamento no [registro de hipóteses](../RASTREABILIDADE.md#21-hipóteses-acrescentadas-na-entrega-3).

![Avatar ilustrativo da persona P02, administrador/editor-chefe](../assets/03_personas/p02-avatar.png)

O avatar foi gerado por IA e é apenas ilustrativo. Aparência e idade aparente não representam dados coletados.

| Campo | Descrição |
|---|---|
| Faixa etária / contexto relevante | [?] Faixa etária não investigada. [H] Atuação na administração do conteúdo como um todo. |
| Ocupação/papel | [H] Administrador do setor de mídias digitais, responsável pela supervisão da produção e gerenciamento de conteúdo digital. |
| Conhecimento do domínio | [H] Gerencia como o conteúdo trabalhado pelos editores deve ser tratado: fluxo de postagens em redes sociais, chancela de decisões editoriais. [?] Nível de experiência não investigado. |
| Experiência tecnológica | [H] Baixo conhecimento técnico de software e computação, com possível baixa familiaridade com editores de vídeo, H34, proposta original do autor para P02. H05 e H17 descrevem o perfil de edição e não comprovam essa combinação para a supervisão. |
| Objetivos | [H] Supervisionar a produção e chancelar decisões editoriais. No uso indireto proposto, decidir se os cortes recebidos podem seguir para montagem ou precisam de revisão pelo editor, H33. |
| Necessidades | [H] Receber cortes identificados por partida e metadados que permitam localizar e compreender os lances antes da decisão editorial, H33, derivada de H22/H23. Investigar quais informações do andamento o editor precisa comunicar para apoiar a supervisão. |
| Dores/frustrações | [H] Dificuldade de manter controle e supervisionar o processo atual, engessado. |
| Motivadores | [H] Maior produtividade do processo editorial e do fluxo de produção e gerenciamento de conteúdo. |
| Restrições/acessibilidade | [H] Conhecimento limitado sobre software e possível dificuldade de adaptação, H34. [?] Regras corporativas e necessidades individuais de acessibilidade não investigadas. |
| Ambiente típico de uso | [H] Supervisão editorial como derivação de H14/H22/H23, recebendo os resultados fora da interface, H33. [?] Local, equipamentos e necessidade de uma tela de acompanhamento não definidos. |
| Comportamentos relevantes | [H] Recebe do editor os cortes e metadados, consulta o material e devolve a decisão de seguir para montagem ou revisar a seleção, H33. Chancela editorial, gestão da produção e supervisão das postagens são atividades externas ao produto. |

**Tarefa proposta com os resultados do TCC, H33:**

| Etapa | Ação e informação |
|---|---|
| Início | Após a revisão e o download pelo editor, P02 recebe os cortes e metadados por um canal externo ainda a definir. |
| Consulta | Assiste aos cortes e consulta a partida de origem, os timecodes e a classificação dos lances nos metadados disponíveis, H25. |
| Decisão | Decide se a seleção atende à intenção editorial e pode seguir para montagem ou se o editor precisa revisá-la. |
| Resultado esperado | O editor recebe uma orientação vinculada aos cortes e à partida, para continuar a produção em ferramenta externa. |

O valor esperado da contribuição do TCC para P02 é receber trechos localizáveis e contextualizados para decidir sobre a seleção. O fluxo completo é hipotético. P02 não envia partidas nem aprova ou publica pela interface no recorte adotado.

**Decisões de design influenciadas por P02:**

- Manter identificáveis a partida de origem e os metadados dos cortes baixados pelo editor, para apoiar a consulta externa por P02, H33 e H25, RC05 e RC09.
- Apresentar ao editor estados e ocorrências compreensíveis de processamento, A02/H25/H26 e RC03. Investigar quais dessas informações P02 precisa receber para decidir sobre o andamento da produção; isso não define uma tela de supervisão.
- Manter parâmetros técnicos fora do fluxo principal, conforme a decisão da Entrega 1, seção 7.1, e RC06. Essa delimitação não depende de confirmar H34.
- Investigar a consulta de histórico de processamento pelo editor, A03/H15 e RC10, para localizar resultados e explicar falhas anteriores. Sua utilidade para a comunicação com P02 ainda está aberta.

**Proposta exploratória de auditoria editorial, H35:** o evento a investigar é uma decisão de aprovar uma seleção ou devolvê-la para revisão. Um possível registro identificaria a seleção, a decisão, seu responsável, o momento e o motivo, para esclarecer qual material foi chancelado e por que houve retrabalho. Pergunta de pesquisa: P02 precisa recuperar essas decisões para resolver divergências, e os registros externos já usados pela equipe atendem à necessidade? Não há evidência dessa necessidade nem decisão de incluir auditoria na interface. Logs técnicos continuam reservados ao suporte, conforme a Entrega 1, seção 8.

### Persona P03 — Jorginho Jr.

**Autor(a):** Giovanni Chahin Morassi — 22.123.025-3
**Tipo:** secundária

**Base de evidências:** hipóteses da [entrega 1](01_conhecendo_o_problema.md), ainda não confirmadas com usuários, e análise de ferramentas da [entrega 2](02_analise_concorrencia.md) (decisões de interface).

**Hipóteses da Entrega 1 relacionadas:** H05, H06, H08, H10, H11, H19, H24, H25 e H28.

**Hipóteses novas da Entrega 3:** H36, H37 e H38, acompanhadas no [registro de hipóteses](../RASTREABILIDADE.md#21-hipóteses-acrescentadas-na-entrega-3).

![Avatar ilustrativo da persona Jorginho Jr.](../assets/03_personas/jorginho-avatar.png)

*Avatar gerado por IA com gpt-image-2. Personagem fictício; aparência e idade aparente são ilustrativas e não representam dados de pesquisa.*

| Campo                             | Descrição                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Faixa etária / contexto relevante | [H] Jovem entre 12 e 24 anos, ainda sem renda própria e produzindo conteúdo esportivo de forma amadora. Faixa definida com o autor, ainda a validar.                                                                                                                                                                                                                                                          |
| Ocupação/papel                    | [H] Criador de conteúdo amador que busca se tornar youtuber ou influenciador digital de futebol; atualmente desempregado. Detalhamento definido com o autor, ainda a validar.                                                                                                                                                                                                                                  |
| Conhecimento do domínio           | [H] Assiste a muitos jogos, joga futebol casualmente com amigos e acompanha jogadores específicos. O reconhecimento de lances ainda é amador e precisa ser validado.                                                                                                                                                                                                                                            |
| Experiência tecnológica           | [H] Já usou editores de vídeo mobile e de computador, sem formação técnica em edição ou programação, H05 e H19. A familiaridade com NLEs profissionais (H17) não foi confirmada. Detalhamento definido com o autor, ainda a validar.                                                                                                                                                                            |
| Objetivos                         | [H] Produzir vídeos centrados em um jogador específico, capazes de divertir o público, e assim crescer como criador no meio digital. Obter cortes e metadados com menor esforço manual, H06 e H28. Objetivo definido com o autor, ainda a validar.                                                                                                                                                            |
| Necessidades                      | [H] Localizar rapidamente os momentos do jogador escolhido, reduzir o tempo de análise de partidas longas e reunir cortes de vários jogos em um compilado, H10, H11, H24, H25 e H36. Revisar e baixar os cortes para continuar a edição fora da interface, H28.                                                                                                                                                |
| Dores/frustrações                 | [H] O tempo elevado de análise por partida e a dificuldade de produzir um compilado de vários jogos tornam o trabalho frustrante; essa frustração afasta seu objetivo de manter edits e canais de esporte, H01 e H11. Prioridade definida com o autor, ainda a validar.                                                                                                                                       |
| Motivadores                       | [H] Alcançar reconhecimento no meio digital com seus vídeos, H06. Outros motivadores ainda não foram investigados.                                                                                                                                                                                                                                                                                             |
| Restrições/acessibilidade         | [H] Computador pouco potente e pouco espaço de armazenamento; tem boa conexão para enviar os vídeos e baixar os cortes, H37. [?] Necessidades individuais de acessibilidade não investigadas.                                                                                                                                                                                                                 |
| Ambiente típico de uso            | [H] Em casa, à mesa do computador, após um dia assistindo a jogos e resolvendo tarefas cotidianas. Detalhamento definido com o autor, ainda a validar.                                                                                                                                                                                                                                                        |
| Comportamentos relevantes         | [H] Reduz a velocidade de reprodução para localizar momentos interessantes e, em seguida, filtra os que pertencem ao jogador escolhido; reúne cortes de várias partidas em um mesmo compilado, H36. Por ter equipamento limitado, depende do processamento remoto para viabilizar o trabalho, H37. Fluxo definido com o autor, ainda a validar; o uso de editores mobile é registrado em H38. |

**Decisões de design influenciadas por P03:**

- Investigar a necessidade de identificar e filtrar lances por jogador para compilações centradas em um atleta, H36. A viabilidade técnica não está confirmada; o filtro não é uma capacidade assegurada do TCC nem um requisito fechado do protótipo.

- Manter o processamento no servidor e a troca por upload e download, para não exigir hardware potente nem armazenamento local do usuário, H37 e RC12.

- Preservar revisão, seleção e download dos cortes pelo próprio criador, com contexto temporal, conforme RC04, RC05, H10 e H25.

- Adotar vocabulário acessível a um editor amador, acostumado a editores mobile, evitando jargão técnico, RC07, H19 e H38.

- Representar o estado por partida e permitir reunir resultados de várias partidas no mesmo trabalho, H08 e H25.

- Manter a edição detalhada e a publicação fora da interface, prevendo a continuidade em ferramentas externas, inclusive mobile, conforme RC05 e o recorte da Entrega 1.

- É uma boa ideia ter um elemento visualmente semelhante às linhas do tempo dos softwares de edição de vídeo para capturar familiaridade dos usuários. talvez na tela de processamento?

Essas decisões são iniciais e deverão ser revistas com a coleta de dados.

### Síntese das personas

P01, Rafael, continua sendo a persona primária e representa o editor de vídeo esportivo priorizado em H27 e na [Entrega 1](01_conhecendo_o_problema.md). P02 representa a supervisão editorial que recebe os resultados fora da interface, H33. P03, Jorginho Jr., é uma persona secundária de criador amador.

| Aspecto | P01, Rafael | P02, Administrador/Editor-Chefe | P03, Jorginho Jr. |
|---|---|---|---|
| Participação | Envia partidas, acompanha o processamento, revisa e baixa resultados. | Recebe e consulta os cortes e metadados fora da interface. | Envia partidas, acompanha o processamento, revisa e baixa cortes para sua produção amadora. |
| Decisão | Escolhe quais cortes baixar para continuar a edição. | Chancela a seleção para montagem ou solicita revisão ao editor, H33. | Escolhe os cortes para compilações centradas em um jogador, H36; realiza a montagem em ferramenta externa. |
| Necessidade que afeta design | Reduzir esforço manual, evitar omissões e entender falhas, H28/H30/H32. | Receber material identificável e com contexto para a decisão editorial, H33. | Obter material de várias partidas com equipamento limitado, H36/H37. |
| Experiência tecnológica | Experiência com edição, sem conhecimento de IA/programação, H05/H17 refinadas para P01. | Possível baixa familiaridade com edição e computação, H34. | Experiência amadora com editores mobile e de computador; vocabulário a validar, H38. |

As três fichas são proto-personas sem validação empírica. O mapa de empatia e a jornada da equipe continuam centrados em P01. O uso direto da interface por P02 e a auditoria editorial permanecem em investigação, H33/H35.

## 2. Mapa de empatia — equipe

**Persona escolhida:** P01, Rafael  
**Idade:** [?] Não investigada.  
**Justificativa:** Rafael representa o editor de vídeo esportivo priorizado na Entrega 1, H27. Seu objetivo de obter cortes e metadados com menor esforço manual, H28, se relaciona diretamente à identificação automática de melhores momentos produzida pelo TCC.

![Mapa de empatia](../assets/03_personas/mapa_empatia.svg)

O mapa abaixo sintetiza as hipóteses de P01 e as escolhas feitas com o autor. Não contém falas coletadas nem observações de usuários. O arquivo visual acima apresenta a mesma síntese do quadro textual.

| Dimensão    | Registro                                                                                                                                                                                                   | Base                                         |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Vê          | [H] Gravações extensas e lances que precisa selecionar. No uso proposto, acompanha o estado das partidas e confere os cortes gerados.                                                                      | H11, H25 e H32; P01                          |
| Ouve        | [?] Não sabemos quais orientações, cobranças ou comentários recebe de colegas e responsáveis editoriais.                                                                                                   | Fluxo organizacional ainda a investigar, H14 |
| Fala e faz     | [H] Envia várias partidas, continua outras edições durante a espera, revisa uma partida por vez e escolhe os cortes para download. Recupera lances omitidos no editor externo. [?] Não há falas coletadas. | H32; comportamentos definidos para P01       |
| Pensa e sente | [H] Preocupa-se com o prazo e com a possibilidade de deixar passar um lance importante. Aceita revisar alguns cortes sem interesse para reduzir esse risco.                                                | H11 e H30; dores de P01                      |
| Dores       | [H] Seleção manual demorada, omissões, cortes sem contexto e retrabalho. Quando ocorre uma falha, precisa entender o motivo e como continuar.                                                              | H01, H10, H11, H16 e H26                     |
| Necessidades      | [H] Entregar no prazo lances relevantes e com contexto, gastando menos tempo procurando e recortando a gravação. Continuar outros trabalhos enquanto as partidas são processadas.                          | H06, H28 e H32; critério de sucesso de P01   |

Fontes: [Entrega 1](01_conhecendo_o_problema.md), perfil P01 desta entrega e [hipóteses H30 a H32](../RASTREABILIDADE.md#21-hipóteses-acrescentadas-na-entrega-3).

## 3. Contexto de uso — consolidação

| Dimensão                       | Descrição                                                                                                                                                                                                                       | Implicação de design                                                                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Usuários e stakeholders | [H] P01 é o editor de vídeo esportivo prioritário, H03, H21 e H27. P02 recebe os resultados fora da interface como responsável editorial, H33. P03 é um criador amador secundário, com experiência em editores mobile, H38. | Priorizar o fluxo de P01. Preservar identificação e contexto do material entregue a P02, RC05 e RC09. Testar vocabulário com os perfis, RC07. |
| Tarefas | [H] P01 e P03 compartilham envio de partidas, acompanhamento, revisão, seleção e download, A01, A02 e A04. A consulta de histórico, A03, permanece uma hipótese a validar. P03 reúne material de várias partidas para editar o compilado em ferramenta externa. | Organizar o fluxo de enviar, acompanhar, revisar e baixar, RC01. Manter a montagem externa e investigar a necessidade de histórico, RC10. |
| Equipamentos | [H] P01 usa computador com tela ampla. P03 usa computador pouco potente, com pouco armazenamento e boa conexão, H37; tem experiência com editores mobile, H38. [?] Escolha entre aplicação web e nativa ainda em aberto, Entrega 1, seção 5.2. | Projetar a revisão de vídeos em computador e considerar a limitação de equipamento de P03. Manter o processamento remoto proposto em sua ficha e testar a continuidade da edição em ferramentas externas, RC12. |
| Ambiente físico | [H] P01 trabalha presencialmente em sala de edição com pouca luz e pressão de prazo, H12/H13. P03 trabalha em casa, à mesa do computador, conforme sua ficha. [?] Ruído e compartilhamento não definidos. | Manter modo escuro e aviso de conclusão ligados às hipóteses H31/H32 de P01. Investigar as condições de uso doméstico de P03 sem atribuir a ele as preferências de P01. |
| Ambiente social/organizacional | [H] P01 pode entregar material a responsáveis editoriais, H14, H22 e H23. P02 recebe os cortes e metadados e devolve uma decisão sobre a seleção, H33. P03 produz conteúdo amador para seus canais e decide quais cortes usar, conforme Objetivos e Necessidades de sua ficha. | Permitir a P01 e P03 revisar e baixar os cortes para continuar a produção em ferramentas externas. P02 recebe o material e devolve sua decisão externamente. Publicação permanece fora do recorte, RC05 e RC09. |
| Papéis/permissões/governança | [H] P02 recebe material e devolve uma decisão editorial externamente, H33. [?] Regras detalhadas de aprovação, permissões e retenção não definidas. Parâmetros técnicos ficam com a equipe técnica, Entrega 1, seções 5.4 e 7.1. | Manter administração de usuários fora do escopo e parâmetros técnicos fora do fluxo principal, RC06. Acompanhamento direto por P02 permanece em investigação. |
| Volume de dados/histórico | [H] Vídeos extensos, H08/H13. P01 envia várias partidas e revisa uma por vez, H32. P03 reúne cortes de vários jogos para um compilado, conforme sua ficha. Utilidade de histórico a validar, H15. [?] Volume, formatos, limites e retenção não definidos. | Representar estado por vídeo e manter a origem dos cortes identificável ao selecionar resultados de várias partidas, RC02, RC03 e RC09. Investigar histórico para localizar resultados e evitar reprocessamento, RC10. |

Fontes: [Entrega 1](01_conhecendo_o_problema.md), seções 3, 5, 7 e 11, e [Entrega 2](02_analise_concorrencia.md), seção 5. As características específicas de P01 e P03 incorporam as escolhas de elaboração de suas fichas, ainda como hipóteses. A participação externa inicial de P02 foi delimitada com Pedro em H33 e é registrada em R03. As relações R04 e R05 da [matriz de rastreabilidade](../RASTREABILIDADE.md#3-rastreabilidade-entre-contribuição-técnica-necessidades-e-artefatos) ligam P03 às atividades compartilhadas. As implicações são recomendações iniciais de design.


## 4. Jornada do usuário — equipe

**Persona:** P01, Rafael  
**Objetivo da jornada:** [H] Obter cortes e metadados de uma partida gravada para continuar a produção em ferramentas externas, H28.  
**Início e fim da jornada:** [H] Começa com o recebimento da gravação integral após a partida, H11 e H12, e termina com a obtenção do material para continuar a edição em ferramenta externa, H28. Base: [Entrega 1](01_conhecendo_o_problema.md), seções 4.5 e 7.3.

| Etapa              | Situação/ação                                                                                                                           | Objetivo                                                  | Pensamento/emoção                                                        | Dor                                                                 | Oportunidade de design                                                                                         | Evidência                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 1                  | Recebe as gravações após as partidas e organiza o material para produzir os melhores momentos.                                          | Preparar o trabalho dentro do prazo.                      | [H] Preocupação com o prazo e com lances que podem passar despercebidos. | Gravações extensas exigem atenção e seleção manual.                 | Permitir identificar e conferir os vídeos antes de enviá-los.                                                  | H01, H11, H12 e H24; RC02                                        |
| 2                  | Envia várias partidas para processamento.                                                                                               | Obter cortes e metadados com menos esforço manual.        | [?] Reação específica ao envio não investigada.                          | Arquivo incompatível ou envio interrompido pode gerar retrabalho.   | Validar entradas e informar o estado de cada vídeo.                                                            | A01, H24, H26 e H32; RC02 e RC03                                 |
| 3                  | Continua outras edições enquanto as partidas são processadas e recebe aviso de conclusão.                                               | Aproveitar o tempo de espera e saber quando pode revisar. | [?] Sentimento durante a espera não investigado.                         | Processamento demorado e incerteza sobre seu estado.                | Mostrar estados reais por partida e avisar quando os resultados estiverem prontos. Meio de aviso a definir.    | A02, H13 e H32; RC03                                             |
| 4, se houver falha | Consulta o problema da partida afetada e a orientação para resolvê-lo; continua com as demais.                                          | Recuperar o trabalho sem perder resultados já concluídos. | [H] Preocupação com atraso e retrabalho.                                 | Falha sem explicação dificulta saber como prosseguir.               | Identificar a partida, explicar a causa conhecida e indicar o próximo passo; preservar os demais resultados.   | H16 e H26; necessidades e comportamentos de P01                  |
| 5                  | Revisa uma partida por vez, assiste aos cortes gerados e seleciona quais utilizar.                                                      | Obter uma seleção relevante e com contexto.               | [H] Prefere descartar cortes extras a perder um lance importante.        | Cortes sem contexto ou sem interesse aumentam o esforço de revisão. | Permitir prévia com contexto temporal e inclusão ou exclusão da seleção para download.                         | A04, H10, H16, H30 e H32; RC04 e RC05                            |
| 6                  | Baixa os cortes e metadados escolhidos.                                                                                                 | Levar o material revisado para a ferramenta de edição.    | [?] Reação específica ao download não investigada.                       | Download indisponível ou seleção incorreta atrasa a continuidade.   | Apresentar resumo da seleção e comunicar falhas na obtenção dos arquivos.                                      | A04, H25, H26 e H28; RC09                                        |
| 7                  | Continua a montagem no editor que já utiliza. Caso perceba uma omissão, procura o lance na gravação original e faz o corte manualmente. | Concluir o material no prazo com os lances relevantes.    | [H] Preocupação em não deixar um lance importante de fora.               | Uma omissão exige busca e corte adicionais.                         | Manter identificáveis a partida de origem e os tempos dos cortes para apoiar a continuidade fora da interface. | H10, H28 e H30; comportamentos de P01 e delimitação da Entrega 1 |

Esta é uma jornada proposta, baseada nas hipóteses da [Entrega 1](01_conhecendo_o_problema.md), nas recomendações RC da [Entrega 2](02_analise_concorrencia.md) e nas escolhas de P01. Não descreve um fluxo observado com usuários. A etapa de falha é condicional.

A jornada inclui a preparação anterior ao envio e a continuidade da edição após o download. A montagem e a eventual recuperação manual de lances acontecem fora da interface.

## Síntese

A partir da [Entrega 1](01_conhecendo_o_problema.md), os cenários e as tarefas seguintes devem contemplar:

- O esforço de localizar e recortar lances em gravações extensas e o risco de omissão ou perda de contexto (H01, H09, H10 e H11).
- A obtenção de cortes e metadados para continuar a produção em ferramentas externas (H06 e H28).
- O envio em lote e a compreensão de progresso, falhas e possibilidades de recuperação (A01 e A02, H08, H13 e H26).
- A revisão, seleção e download dos resultados (A04, H16 e H25) mantendo a decisão editorial com o usuário.
- A entrega externa de cortes e metadados a P02 para uma decisão sobre a seleção (H33); investigar H34/H35 antes de propor interações específicas para esse perfil.

Esses pontos mantêm o status de hipótese. P01, P02 e P03 estão elaboradas, o mapa textual e a jornada proposta tomam P01 como referência e precisam ser validados com usuários; P03 acrescenta a necessidade hipotética de filtrar lances por jogador (H36) cuja viabilidade técnica não está confirmada e não fazia parte do escopo original das capacidades do sistema proposto, e reforça a proposta de processamento remoto (H37). Edição detalhada, publicação e administração de usuários permanecem fora do escopo definido na Entrega 1.

## Checklist

- [x] O mapa de empatia visual está preenchido e corresponde ao quadro textual.
- [x] Existe pelo menos uma persona por integrante.
- [x] As personas diferem por tarefas, decisões, experiência e contexto de uso.
- [x] Está claro o que é dado real e o que é hipótese/proto-persona.
- [x] A persona não “validou por ficção” uma hipótese da Entrega 1; afirmações continuam marcadas como hipótese quando não há evidência.
- [x] Objetivos e dores de P01, P02 e P03 têm consequência para o design.
- [x] Contexto de uso está coerente com a Entrega 1.
- [x] Em TCC sem interface original, P01, P02 e P03 possuem relação explícita com a contribuição técnica.
- [x] P02 possui tarefa decisória distinta, fora da interface, em H33; não foi criado acesso administrativo.
- [x] Jornada possui etapas, dores e oportunidades e não é apenas wireflow.
- [x] IDs das personas elaboradas foram adicionados à rastreabilidade: P01, P02 e P03, nas relações R01 a R05.

## Lacunas para investigação
> Anotações do grupo pras próximas entregas

As lacunas abaixo não impedem a elaboração das personas, mas servem pra  orientar a coleta de dados da Entrega 7. As respostas da equipe detalham hipóteses; somente a pesquisa poderá fornecer evidências sobre os usuários. Em 16/09/2026, Pedro confirmou a manutenção da dimensão Ouve e das reações ao envio, à espera e ao download como não investigadas. Também definiu o filtro por jogador como necessidade a investigar, com viabilidade técnica não confirmada.

| Lacuna | Como investigar | Decisão afetada |
|---|---|---|
| Orientações e cobranças recebidas por Rafael, H14 | Perguntar a editores e responsáveis editoriais como combinam prazos e critérios de seleção. | Dimensão Ouve do mapa e comunicação entre P01 e P02. |
| Reações ao envio, à espera e ao download | Pedir ao editor que descreva essas etapas e observar dificuldades durante o uso do protótipo. | Feedback e apoio nas etapas 2, 3 e 6 da jornada. |
| Aviso de conclusão, H32 | Investigar como o editor alterna tarefas e quais avisos percebe sem interromper o trabalho. | Meio de aviso e retorno à revisão. |
| Histórico e recuperação, H15/H26 | Investigar situações de consulta a resultados anteriores e de falha no processamento. | Informações de histórico e ações de recuperação. |
| Condições de uso e acessibilidade | Levantar equipamentos, conexão, iluminação, ruído, compartilhamento e barreiras de interação. | Legibilidade, operação por teclado e continuidade do envio e download. |
| Volume, formatos e retenção | Levantar tamanho e quantidade de gravações com usuários e conferir limites com a equipe técnica. | Validação de entradas, armazenamento e disponibilidade dos resultados. |
| Supervisão e auditoria, H33/H35 | Investigar informações consultadas por P02 e como registra decisões fora do produto. | Necessidade de acompanhamento direto ou de registros adicionais. |
| Recorte por jogador, H36 | Investigar a seleção de lances por criadores e verificar se o backend pode identificar jogadores. | Viabilidade de filtro por jogador para P03. |


## Histórico de revisões
> NÃO É RELEVANTE PARA A ENTREGA.
> Anotações de trabalho do grupo.

- 09/09/2026 às 21:40: aplicação de AC-013 e AC-015. H30–H32 receberam IDs e acompanhamento; P01 foi ligada à contribuição técnica e às necessidades na matriz. Autoria completada com matrícula. Hipóteses permanecem abertas e a entrega continua em andamento.
- 10/09/2026: revisão de P03 (Jorginho Jr). Correções ortográficas e de estrutura; persona reposicionada no padrão de P01, tipificada como secundária, ligada a H05, H06, H08, H10, H11, H19, H24, H25 e H28; decisões de design preenchidas; avatar aplicado (`assets/03_personas/jorginho-avatar.jpg`, foto do Pexels, uso educativo). Registradas H33–H35 no [registro de hipóteses](../RASTREABILIDADE.md#21-hipóteses-acrescentadas-na-entrega-3). P02 ainda pendente.

- 16/09/2026 às 20:02: AC-024 aplicado. Foto atribuída ao Pexels substituída por avatar fictício gerado com gpt-image-2, via API no endpoint configurado no Codex. Imagem atual: `assets/03_personas/jorginho-avatar.png`. Legenda atualizada; prompt e registro de geração preservados na análise de coerência de 16/09/2026 às 19:49.

- 16/09/2026 às 20:04: AC-023 aplicado. P03 incorporada ao contexto consolidado, com diferenças de experiência, equipamento, ambiente e produção amadora. Relações R04/R05 registram suas atividades compartilhadas na matriz. P01 continua prioritária; mapa de empatia e jornada permanecem centrados em Rafael.

- 09/09/2026: aplicação de AC-016 a AC-019 da análise das 22:02. P02 recebeu tarefa externa hipotética, referências corrigidas, hipóteses H33 a H35 e relação R03. Síntese, contexto e pendências foram atualizados. Pedro definiu recebimento externo como participação inicial e acompanhamento direto como alternativa a investigar. Auditoria editorial permanece exploratória e não houve validação com usuários.

- 16/09/2026 às 20:07: AC-020 aplicado. Integrada a ficha de P02 da main ec04f95, com suas hipóteses H33/H34/H35 e relação R03 preservadas. As hipóteses de P03 foram renumeradas: H33 → H36, filtro por jogador; H34 → H37, equipamento/processamento remoto; H35 → H38, experiência tecnológica. Atualizadas as referências atuais, síntese, contexto e checklist. Registros anteriores conservam os IDs usados na época. P01 permanece prioritária e a entrega continua em andamento.

- 16/09/2026: substituído o placeholder do mapa de empatia por uma síntese visual de P01, com hipóteses e lacunas identificadas. Removidas instruções de preenchimento já atendidas e reunidas as perguntas para a coleta de dados. Incorporadas as respostas de Pedro: falas e reações não investigadas permanecem como lacunas; filtro por jogador condicionado à investigação e à viabilidade técnica. Preenchimento concluído, com validação empírica pendente.
