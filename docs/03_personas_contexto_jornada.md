# Entrega 3 — Personas, mapa de empatia, contexto de uso e jornada

**Data:** 9/9/2026  
**Status:** 🟨 em andamento  
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

| Item da Entrega 1 | Status inicial | Evidência disponível agora | Como será tratado nesta entrega |
|---|---|---|---|
| Editor de vídeo esportivo como usuário prioritário, H03, H21 e H27 | H | Entrega 1, seções 2.2 e 7.2; adequação do perfil ainda sem validação com usuários | Incorporar como base de proto-persona; manter como hipótese |
| Obter cortes e metadados com menor esforço manual, H06 e H28 | H | Entrega 1, seções 3.1 e 7.3 | Incorporar como objetivo a validar |
| Selecionar/exportar resultados e processar vídeos em lote, H07 e H08 | H | Atividades A01 a A04 da Entrega 1, seção 3.2; frequência e criticidade não confirmadas | Incorporar atividades; investigar frequência e criticidade |
| Esforço manual, omissões e retrabalho sob pressão de prazo, H01, H09, H10 e H11 | H | Situação hipotética da Entrega 1, seção 4.5 | Manter como dores hipotéticas, sem atribuir relatos a participantes |
| Baixo conhecimento de computação e familiaridade com editores de vídeo, H05, H17 e H19 | H | Entrega 2, seção 3, identifica padrões nas ferramentas, mas não comprova familiaridade do público | Manter como hipótese; investigar experiência e vocabulário |
| Pós-produção, arquivos extensos e pressão de prazo, H12 e H13 | H | Entrega 1, seções 5.1 a 5.3 | Incorporar ao contexto provisório |
| Entrega a responsáveis editoriais e decisões sobre resultados, H14, H22 e H23 | H | Entrega 1, seções 5.4 e 7.1; divisão de responsabilidades não investigada | Manter como hipótese; não criar papéis adicionais sem tarefas distintas |
| Histórico e consequências de falhas, H15, H16 e H26 | H | Entrega 1, seções 5.5, 5.6 e 7.1; recomendações RC03 e RC10 da Entrega 2 | Investigar necessidade de histórico e formas de recuperação |
| Equipamentos, local, acessibilidade, permissões e retenção | ? | Lacunas registradas na Entrega 1, seções 2.4 e 5 | Manter em aberto para coleta de dados |

Fontes: [Entrega 1](01_conhecendo_o_problema.md), [Entrega 2](02_analise_concorrencia.md) e [registro de hipóteses](../RASTREABILIDADE.md). As referências às outras entregas recuperam o conhecimento da equipe; não constituem nova validação com usuários.

## 1. Personas

### Persona P01 — Rafael

**Autor(a):** Pedro Alexandre Custódio Silva  
**Tipo:** primária  
**Base de evidências:** hipóteses da [entrega 1](01_conhecendo_o_problema.md), ainda não confirmadas com usuários, e análise de ferramentas da [entrega 2](02_analise_concorrencia.md) (decisões de interface).  
**Hipóteses da Entrega 1 relacionadas:** H01, H03, H05, H06, H09, H10, H11, H12, H13, H16, H17, H19, H21, H27 e H28

![Persona P01](../assets/03_personas/persona_p01.svg)

| Campo | Descrição |
|---|---|
| Faixa etária / contexto relevante | [?] Faixa etária não investigada. [H] Atuação na pós-produção de partidas encerradas, H12. |
| Ocupação/papel | [H] Editor de vídeo esportivo experiente em uma produtora de conteúdo esportivo, responsável por obter material de melhores momentos. Detalhamento de H03, H21 e H27 definido com o autor, ainda a validar. |
| Conhecimento do domínio | [H] Identifica lances como gols, defesas, finalizações perigosas e ocorrências disciplinares, conforme a situação de H11. A experiência em edição foi definida com o autor como característica hipotética do perfil; o conhecimento específico de futebol ainda precisa ser validado. |
| Experiência tecnológica | [H] Experiente no uso de ferramentas de edição de vídeo, mas sem conhecimento de IA ou programação. Detalhamento de H05 e H17 definido com o autor, ainda a validar; a ferramenta utilizada não foi escolhida. |
| Objetivos | [H] Entregar no prazo uma seleção de lances relevantes, com contexto suficiente, gastando menos tempo procurando e recortando a gravação. Obter cortes e metadados para continuar a produção em ferramentas externas, H06 e H28. Critério de sucesso definido com o autor, ainda a validar com usuários. |
| Necessidades | [H] Reduzir o esforço de seleção e corte, preservar o contexto dos lances e poder conferir manualmente todos os cortes gerados antes de selecionar quais baixar, H01, H10, H11, H16 e H28. O próprio editor é responsável pela revisão, conforme definição do perfil com o autor. Quando uma partida falha, precisa entender o que aconteceu e como prosseguir, sem perder os resultados já concluídos das outras partidas, conforme definição com o autor e H16. |
| Dores/frustrações | [H] Prazo curto como pressão principal, acompanhado da preocupação de deixar passar lances importantes durante a seleção manual. Recortes sem contexto e retrabalho podem atrasar a entrega, H01, H09, H10 e H11. Prioridade definida com o autor, ainda a validar. Prefere revisar alguns cortes sem interesse a deixar um lance importante de fora, conforme definição do perfil com o autor. |
| Motivadores | [H] Produzir melhores momentos com eficiência e consistência, H06. Outros motivadores ainda não foram investigados. |
| Restrições/acessibilidade | [H] Arquivos extensos, tempo de processamento e pressão de prazo, H13. [?] Necessidades individuais de acessibilidade não investigadas. |
| Ambiente típico de uso | [H] Trabalho presencial na produtora, em sala de edição com pouca luz e computador com tela ampla, na pós-produção de partidas gravadas. Prefere o modo escuro para conforto no ambiente pouco iluminado. Detalhamento de H12 e H13 definido com o autor, ainda a validar. |
| Comportamentos relevantes | [H] No processo atual imaginado, percorre a gravação, identifica lances e organiza os trechos, conforme H11. No uso proposto, envia várias partidas para a fila e continua outras edições enquanto aguarda o processamento. Precisa ser avisado quando os cortes estiverem prontos; então revisa uma partida por vez e seleciona o material para download. Ao perceber que falta um lance importante, consulta a gravação original e faz o corte no editor de vídeo que já utiliza. Se o processamento de uma partida falha, procura entender o motivo e a ação necessária para resolver o problema, enquanto continua com as demais. Fluxo definido com o autor, ainda a validar. |

**Decisões de design influenciadas por P01:**

- Facilitar a revisão e a exclusão de cortes da seleção para download. Rafael aceita alguns resultados sem interesse para reduzir o risco de omitir lances importantes; essa preferência não garante que o modelo detecte todos os lances.

- Priorizar envio, acompanhamento, revisão e download, conforme RC01 da Entrega 2 e H28.
- Permitir enfileirar várias partidas, identificar o estado de cada uma e avisar quando seus cortes estiverem prontos, para que o editor continue outros trabalhos durante a espera. O meio de aviso ainda será definido.
- Oferecer modo escuro para a preferência de P01 no ambiente pouco iluminado, mantendo contraste, foco e controles legíveis.
- Permitir assistir a todos os cortes gerados e selecionar quais baixar, com contexto temporal para apoiar a revisão pelo próprio editor, conforme RC04 e RC05, H10, H11 e H16. Conferir os cortes gerados não permite garantir que nenhum lance foi omitido.
- Manter a recuperação de lances omitidos e a edição detalhada no editor externo já utilizado pelo profissional, conforme o fluxo definido com o autor e o recorte da Entrega 1.
- Manter parâmetros técnicos fora do fluxo principal e testar vocabulário do domínio com usuários, conforme RC06 e RC07, H05 e H19.
- Em caso de falha, identificar a partida afetada, explicar o motivo conhecido em linguagem compreensível para Rafael e indicar o próximo passo. Se a causa não for conhecida, informar isso sem inventar uma explicação. Preservar o acesso aos resultados já concluídos e permitir continuar com as outras partidas, conforme H16, H26 e o comportamento definido com o autor.
- Comunicar progresso e falhas em texto e permitir operação por teclado, conforme RC03 e RC11. A acessibilidade é uma recomendação de design da Entrega 2, não uma característica já observada de P01.

Essas decisões são iniciais e deverão ser revistas com a coleta de dados. A elaboração e a diferenciação das demais personas continuam pendentes.

> Repita para P02, P03... Cada integrante deve produzir ao menos uma persona.

### Síntese das personas

O perfil prioritário é o editor de vídeo esportivo, conforme H27 e [entrega 1](01_conhecendo_o_problema.md). A síntese das diferenças entre personas depende da elaboração dos perfis individuais pelos integrantes.

## 2. Mapa de empatia — equipe

**Persona escolhida:** {{P01}}  
**Justificativa:** {{por que esse perfil é relevante}}

![Mapa de empatia](../assets/03_personas/mapa_empatia.svg)

Documente também em texto: o que vê; ouve; diz/faz; pensa/sente; dores; ganhos. Diferencie **evidência** de **hipótese**.

## 3. Contexto de uso — consolidação

| Dimensão | Descrição | Implicação de design |
|---|---|---|
| Usuários | [H] Editor de vídeo esportivo, H03, H21 e H27. | Priorizar obtenção e revisão de cortes e metadados; testar linguagem com o público, RC01 e RC07. |
| Tarefas | [H] Enviar vídeos em lote, acompanhar processamento, consultar histórico e revisar, selecionar e baixar resultados, A01 a A04. | Organizar o fluxo de enviar, acompanhar, revisar e baixar, RC01; validar a necessidade de histórico, RC10. |
| Equipamentos | [H] Computador com tela ampla, escolhido para P01. [?] Demais equipamentos e escolha entre aplicação web e nativa ainda em aberto, Entrega 1, seção 5.2. | Projetar para inspeção visual de vídeos em computador e considerar arquivos extensos na escolha da plataforma, RC12. |
| Ambiente físico | [H] Para P01, trabalho presencial em sala de edição da produtora, com pouca luz e pressão de prazo, como detalhamento de H12 e H13. [?] Ruído e compartilhamento não definidos. | Oferecer modo escuro com controles legíveis e estados claros de processamento; avisar sobre conclusão enquanto o editor realiza outros trabalhos, conforme o perfil definido e RC03. |
| Ambiente social/organizacional | [H] O editor pode entregar material a produtores ou responsáveis editoriais para aprovação e publicação, H14, H22 e H23. | Permitir revisar e baixar material para continuidade em ferramentas externas; publicação está fora do recorte, RC05 e RC09. |
| Papéis/permissões/governança | [?] Papéis, permissões, aprovação e retenção não definidos. Parâmetros técnicos ficam com a equipe técnica no recorte inicial, Entrega 1, seções 5.4 e 7.1. | Manter administração de usuários fora do escopo e parâmetros técnicos fora do fluxo principal, conforme delimitação da Entrega 1 e RC06. |
| Volume de dados/histórico | [H] Vídeos extensos, H08 e H13. Para P01, várias partidas na fila e revisão de uma por vez, conforme definição com o autor; utilidade de histórico a validar, H15. [?] Volume, formatos, limites e retenção não definidos. | Representar estado por vídeo, validar entradas e investigar histórico para localizar resultados e evitar reprocessamento, RC02, RC03 e RC10. |

Fontes: [Entrega 1](01_conhecendo_o_problema.md), seções 3, 5, 7 e 11, e [Entrega 2](02_analise_concorrencia.md), seção 5. As características específicas de P01 também incorporam as escolhas feitas com o autor nesta entrega, ainda como hipóteses. As implicações são recomendações iniciais de design.

## 4. Jornada do usuário — equipe

**Persona:** {{P01}}  
**Objetivo da jornada:** [H] Obter cortes e metadados de uma partida gravada para continuar a produção em ferramentas externas, H28.  
**Início e fim da jornada:** [H] Começa com o recebimento da gravação integral após a partida, H11 e H12, e termina com a obtenção do material para continuar a edição em ferramenta externa, H28. Base: [Entrega 1](01_conhecendo_o_problema.md), seções 4.5 e 7.3.

| Etapa | Situação/ação | Objetivo | Pensamento/emoção | Dor | Oportunidade de design | Evidência |
|---|---|---|---|---|---|---|
| 1 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

> A jornada pode incluir etapas **antes, durante e depois** do uso do produto. Não transforme a jornada em lista de telas.

## Síntese

A partir da [Entrega 1](01_conhecendo_o_problema.md), os cenários e as tarefas seguintes devem contemplar:

- O esforço de localizar e recortar lances em gravações extensas e o risco de omissão ou perda de contexto, H01, H09, H10 e H11.
- A obtenção de cortes e metadados para continuar a produção em ferramentas externas, H06 e H28.
- O envio em lote e a compreensão de progresso, falhas e possibilidades de recuperação, A01 e A02, H08, H13 e H26.
- A revisão, seleção e download dos resultados, A04, H16 e H25, mantendo a decisão editorial com o usuário.
- A investigação da necessidade de recuperar resultados anteriores, A03 e H15.

Esses pontos mantêm o status de hipótese. Ainda faltam os perfis individuais completos, o mapa de empatia e o detalhamento das etapas da jornada. Edição detalhada, publicação e administração de usuários permanecem fora do escopo definido na Entrega 1.

## Checklist

- [ ] Existe pelo menos uma persona por integrante.
- [ ] As personas não são apenas diferenças demográficas superficiais.
- [ ] Está claro o que é dado real e o que é hipótese/proto-persona.
- [ ] A persona não “validou por ficção” uma hipótese da Entrega 1; afirmações continuam marcadas como hipótese quando não há evidência.
- [ ] Objetivos e dores têm consequência para o design.
- [x] Contexto de uso está coerente com a Entrega 1.
- [ ] Em TCC sem interface original, a persona possui relação explícita com a contribuição técnica.
- [ ] Papéis administrativos, técnicos e decisórios só foram criados quando possuem objetivos/tarefas diferentes.
- [ ] Jornada possui etapas, dores e oportunidades e não é apenas wireflow.
- [ ] IDs das personas foram adicionados à rastreabilidade.
