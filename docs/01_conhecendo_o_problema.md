# Entrega 1 — Conhecendo o projeto, o usuário e o problema

**Data:** 13/08/2026  
**Status:** `🟩 concluída`  
**Responsabilidade:** 1 solução consolidada por equipe

## Objetivo da atividade

Reinterpretar o tema do TCC sob a perspectiva de Interação Humano-Computador e construir um **entendimento comum entre os integrantes da equipe**.

A disciplina utiliza preferencialmente o tema do TCC para os exercícios de IHC. Isso vale tanto para TCCs que já preveem uma interface quanto para trabalhos cujo resultado principal é algoritmo, modelo, API, biblioteca, análise de dados, infraestrutura, estudo experimental ou outro artefato técnico.

> **Importante:** a interface projetada na disciplina é um artefato de aprendizagem de IHC. Ela **não se torna automaticamente uma obrigação do TCC**. Sua incorporação ao trabalho de conclusão depende de decisão da equipe e do orientador.

Antes de preencher, leia [`../GUIA_ESCOPO_IHC.md`](../GUIA_ESCOPO_IHC.md).

Nesta primeira semana a equipe **não deve começar desenhando telas**. Primeiro deverá compreender:

- o que o TCC realmente produz;
- quem poderia obter valor dessa contribuição;
- quais pessoas interagem, administram, configuram, interpretam ou são afetadas;
- o que essas pessoas precisam alcançar;
- como atividades relacionadas acontecem hoje;
- problemas, limitações e contexto;
- alternativas existentes;
- qual recorte de interação fará sentido para a disciplina.

Ao final desta entrega, a equipe deve diferenciar:

- **tema do TCC** × **escopo formal do TCC** × **escopo de IHC da disciplina**;
- **objetivo do projeto** × **objetivo do usuário**;
- **problema do usuário** × **solução tecnológica**;
- **fato conhecido** × **hipótese** × **lacuna de conhecimento**;
- **capacidade técnica** × **forma de uso dessa capacidade**;
- **funcionalidade** × **atividade/resultado que o usuário precisa alcançar**;
- **usuário direto** × **stakeholders**.

---

## Como classificar as respostas

Sempre que a resposta fizer uma afirmação sobre usuários, problemas, atividades, necessidades, contexto ou mercado, use:

- **[F] Fato conhecido** — existe evidência/fonte.
- **[H] Hipótese** — afirmação plausível que ainda precisa ser investigada.
- **[?] Não sabemos ainda** — lacuna relevante.

Quando usar `[F]`, informe a origem. Hipóteses prioritárias devem receber IDs (`H01`, `H02`...) e também ser registradas em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

> **Exemplo:** `[H] H01 — DBAs considerariam útil comparar automaticamente o plano atual de execução com uma recomendação produzida pelo algoritmo.`

Uma hipótese explicitada é melhor do que uma suposição escondida.

---

# 0. Identificação do TCC e da equipe

## 0.1 Membros

| Nome completo | Matrícula | GitHub | Responsabilidade Principal |
|---|---:|---|---|
| Pedro Alexandre Custodio Silva | 22.123.049-3 | [p4cs-974](https://github.com/p4cs-974) | Tela de Input |
| Lucas Roberto Boccia dos Santos | 22.123.012-1 | [uniflusantos](https://github.com/uniflusantos) | Tela de Output |
| Giovanni Chahin Morassi | 22.123.025-3 | [giovanni1351](https://github.com/giovanni1351) | Tela de Logs/Rastreabilidade |

## 0.2 Título atual do TCC

Identificação de Melhores Momentos em Partidas de Futebol Utilizando Sistemas Híbridos de Visão Computacional

## 0.3 Orientador(a)

Prof. Dr. Murillo Freitas Bouzon

## 0.4 Qual é o resultado principal atualmente previsto no TCC?

Marque e descreva:

- [ ] sistema/aplicação interativa;
- [x] algoritmo;
- [x] modelo de IA/ML/LLM;
- [ ] biblioteca/API/framework;
- [x] análise de dataset;
- [x] estudo/benchmark/avaliação experimental;
- [x] infraestrutura/backend;
- [ ] componente embarcado/IoT;
- [ ] outro: {{...}}.

**Descrição:** Sistema híbrido de visão computacional que recebe arquivos de vídeo de partidas de futebol e produz cortes de melhores momentos acompanhados de arquivos de metadados.

## 0.5 O TCC já previa desenvolvimento de interface com usuário?

- [ ] Sim, a interface já faz parte do TCC.
- [ ] Parcialmente; existe alguma interação, mas ainda não está bem definida.
- [x] Não. O TCC é predominantemente técnico e não previa interface.

**Explique o que está formalmente previsto no TCC:** Estava previsto apenas o desenvolvimento do sistema de backend. Com a orientação do professor, a equipe desenvolverá uma interface para a disciplina CC8122.

> Esta resposta serve para separar o compromisso do TCC do projeto da disciplina. Mesmo quando a opção for **não**, a equipe irá definir uma interface para exercitar IHC.

---

# 1. Entendendo a contribuição do projeto

## 1.1 Explique o TCC em uma frase, sem citar linguagem de programação, framework ou banco de dados.

Desenvolver um sistema híbrido de visão computacional capaz de automatizar o processo de corte de melhores momentos em partidas de futebol, reduzindo a necessidade de trabalho manual.

## 1.2 Qual situação, atividade ou problema do mundo real motivou o TCC?

[H] H01 — O corte e a geração de vídeos de melhores momentos são feitos manualmente, demandam tempo e estão sujeitos à interpretação humana, ao cansaço e a falhas.

## 1.3 Qual é a **capacidade/contribuição central** produzida pelo TCC?

Identificar automaticamente os melhores momentos de partidas de futebol e gerar os respectivos cortes de vídeo e metadados.

## 1.4 O que se espera que esteja diferente **para pessoas, organizações ou processos** se essa contribuição for bem-sucedida?

[H] H02 — Profissionais responsáveis pela geração de vídeos de melhores momentos gastarão menos tempo realizando cortes manualmente e terão resultados menos sujeitos a variações causadas por cansaço ou falha humana.

## 1.5 O que é mérito técnico/científico do TCC e o que seria uma possível aplicação prática?

| Mérito/contribuição técnica | Possível aplicação/valor em uso |
|---|---|
| Automação da identificação de melhores momentos com visão computacional | Redução do trabalho manual na produção dos cortes e geração de metadados para os resultados |
| Uso de LLMs multimodais na detecção e classificação dos highlights | Evidenciar a capacidade de generalização do conhecimento e aplicabilidade dos modelos de linguagem |

---

# 2. Entendendo as pessoas envolvidas

## 2.1 Quem interage diretamente com o produto, se já existe interface prevista?

NÃO SE APLICA AO ESCOPO ORIGINAL.

## 2.2 Quem poderia **usar, configurar, administrar, operar, interpretar ou tomar decisões** a partir da contribuição técnica?

Considere perfis profissionais e stakeholders, não apenas consumidores finais.

| Perfil | Relação com a contribuição | O que faria | Status/evidência |
|---|---|---|---|
| Profissional responsável pelo corte e geração de vídeos de melhores momentos | Usuário direto da aplicação potencial | Enviar vídeos para processamento, acompanhar o processo e acessar os cortes e metadados gerados | [H] H03 |

## 2.3 Existem pessoas afetadas que não usariam a interface diretamente?

| Stakeholder | Como é afetado | Usa interface? | Status/evidência |
|---|---|---|---|
| Empresas de mídia esportiva | menos custos devido à maior eficiência do processo | não | [H] H04 |

## 2.4 Que características desses perfis podem influenciar a interação?

- Baixo conhecimento técnico a respeito de software e computação no geral. [H] H05
- Uso de trackpads e mouses acima do teclado. [F]
- Costume com softwares tradicionais de edição/manipulação de vídeo. [F]
- Uso focado em desktop/web. [F]

---

# 3. Entendendo objetivos e atividades

## 3.1 O que o usuário está tentando conseguir no mundo real?

[H] H06 — Produzir vídeos de melhores momentos de partidas de futebol com eficiência e consistência, reduzindo o esforço de seleção e corte manual.

## 3.2 Quais são as atividades mais importantes?

| ID | Atividade/objetivo | Quem realiza | Frequência/criticidade inicial | Status/evidência |
|---|---|---|---|---|
| A01 | Processar vídeos em lote | Profissional responsável pela geração de vídeos de melhores momentos | Frequência e criticidade ainda desconhecidas | H |
| A02 | Acompanhar o processamento por meio de informações de observabilidade e logs | Profissional responsável pela geração de vídeos de melhores momentos | Frequência e criticidade ainda desconhecidas | H |
| A03 | Consultar o histórico de resultados processados | Profissional responsável pela geração de vídeos de melhores momentos | Frequência e criticidade ainda desconhecidas | H |

## 3.3 Qual atividade parece mais frequente? Por quê?

[H] H07 — Selecionar/exportar os resultados processados. Para gerar compilações, ou editar em softwares externos para publicar em outras mídias.

## 3.4 Qual parece mais crítica? Que consequência existe se for mal executada?

[H] H08 — Processar os vídeos em lote. Se for mal executada as consequências podem ser: necessidade de retrabalho, custo de processamento da inferência da LLM, perda de arquivos.

---

# 4. Entendendo o problema ou processo atual

## 4.1 Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina?

Pode existir software concorrente, linha de comando, planilha, notebook, script, painel técnico, processo manual, consulta a logs, análise visual, troca de mensagens, decisão por especialista etc.

[F] Editores humanos precisam segmentar e classificar os lances em tempo real durante as transmissões.

## 4.2 O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente?

[H] H09 — A análise depende da precisão e subjetividade do profissional, que pode estar sujeito a, por exemplo, se distrair e perdeu um highlight.

## 4.3 Que informações o profissional precisa interpretar para tomar decisão?

[F] Contexto da partida de futebol.

## 4.4 O que acontece quando a atividade falha ou quando o resultado é interpretado incorretamente?

[H] H10 — Um lance possivelmente interessante da partida pode não estar devidamente rotulado pelo profissional, consequentemente, esse lance pode acabar ficando de fora de um vídeo de highlights final.

## 4.5 Conte uma situação concreta.

Escreva uma pequena narrativa com pessoa, objetivo, atividade, contexto, dificuldade e consequência. **Não descreva ainda a futura solução.**

[H] H11 — Após o encerramento de uma partida, um editor de vídeo esportivo recebe a gravação integral e precisa preparar material de melhores momentos para publicação. Ele percorre o vídeo, identifica lances como gols, defesas, finalizações perigosas e ocorrências disciplinares, determina os limites dos trechos e os organiza para uso posterior. Sob pressão de prazo, assistir e selecionar manualmente conteúdo de uma partida extensa exige atenção contínua; um lance pode ser omitido ou recortado sem contexto, provocando retrabalho e atraso. A descrição deverá ser validada por entrevista ou observação de profissionais.

## 4.6 Que evidência existe hoje?

| Evidência/fonte | O que sustenta | Limitação |
|---|---|---|
| AKAN, Sara; VARLI, Songül. Use of deep learning in soccer videos analysis: survey: S. Akan, S. Varlı. Multimedia Systems, v. 29, n. 3, p. 897-915, 2023. | A produção ainda depende fortemente de edição manual; melhores momentos pós-jogo têm relevância e diferentes tempos de entrega; a detecção deve considerar eventos além de gols | Estudo acadêmico com 25 partidas e foco no desempenho técnico; não investiga diretamente o fluxo de trabalho ou a experiência de editores profissionais |
| YIN, Hongwei; SINNOTT, Richard O.; JAYAPUTERA, Glenn T. A survey of video-based human action recognition in team sports: H. Yin et al. Artificial intelligence review, v. 57, n. 11, p. 293, 2024. | Existem plataformas de mercado que analisam eventos, geram conteúdo e metadados e gerenciam ativos esportivos com IA | Fonte institucional e promocional; não oferece evidência independente de usabilidade ou adequação ao nosso público |
| SEWERYN, Karolina; WRÓBLEWSKA, Anna; ŁUKASIK, Szymon. Survey of action recognition, spotting, and spatio-temporal localization in soccer—Current trends and research perspectives. ACM Transactions on Intelligent Systems and Technology, v. 17, n. 2, p. 1-37, 2026. | Existem soluções que recebem vídeo gravado em MP4, geram clips/tags e permitem baixar resultados, além de fluxos mais amplos de edição e publicação | Fonte institucional e comercial; funcionalidades e resultados anunciados ainda precisam de análise independente na Entrega 2 |

---

# 5. Entendendo o contexto de uso

## 5.1 Onde e em quais situações a interação poderia ocorrer?

[H] H12 — O uso ocorrerá no fluxo de pós-produção, após a partida, quando o editor tiver acesso à gravação integral e precisar obter cortes para continuar o trabalho em ferramentas externas. O local exato — emissora, produtora, clube, trabalho remoto ou outro — ainda é [?] desconhecido.

## 5.2 Em quais dispositivos/equipamentos?

[?] O formato técnico da interface e os equipamentos prioritários ainda não foram definidos. Como o trabalho envolve vídeos longos, inspeção visual e download de arquivos, computadores com tela ampla são uma hipótese a validar; aplicação Web para desktop e aplicação desktop nativa permanecem alternativas.

## 5.3 Existem condições físicas relevantes?

Considere iluminação, ruído, mobilidade, conexão, privacidade, uso compartilhado, interrupções, pressão de tempo etc.

[H] H13 — Arquivos de vídeo extensos exigem armazenamento, largura de banda e tempo de processamento; a interface precisa deixar claros upload, fila, progresso, falha e conclusão. Também pode haver pressão para publicar logo após a partida e interrupções causadas por outras demandas de produção. Condições de iluminação, ruído, privacidade e compartilhamento de equipamento ainda são [?] desconhecidas.

## 5.4 Existem fatores sociais ou organizacionais?

Considere papéis, chefias, equipes, permissões, aprovação, responsabilidade profissional, auditoria, turnos e colaboração.

[H] H14 — O editor pode entregar os arquivos a produtores ou responsáveis editoriais que aprovam e publicam o conteúdo, mas esse fluxo e a separação entre editor e operador ainda precisam ser investigados. [?] Papéis, permissões, políticas de retenção, turnos e responsabilidade pela aprovação não estão definidos.

## 5.5 Existe necessidade de histórico, rastreabilidade ou auditoria?

[H] H15 — Um histórico com nome da partida, data, estado, arquivos de entrada, resultados e motivo de falha ajudaria a localizar downloads, evitar reprocessamentos e compreender o que ocorreu. A necessidade de auditoria formal ainda é [?] desconhecida.

## 5.6 Um erro pode produzir consequência relevante? Qual?

[H] H16 — Sim. Arquivo incompatível, envio interrompido, processamento com falha ou resultado incompleto podem causar atraso, retrabalho e custo adicional de inferência. Cortes incorretos podem omitir lances importantes; por isso o sistema não deve apresentar o resultado automático como editorialmente infalível.

---

# 6. Entendendo mercado e alternativas existentes

> Nesta entrega faça apenas um **levantamento inicial**. A análise aprofundada ocorre na Entrega 2.

## 6.1 Como pessoas resolvem problemas semelhantes hoje?

| Alternativa atual | Quem usa | Para quê | Status/evidência |
|---|---|---|---|
| Edição manual em software profissional, como Adobe Premiere Pro ou DaVinci Resolve | Editores de vídeo | Importar, assistir, marcar, recortar, organizar e exportar trechos | [F] A edição manual ainda é predominante em muitas ligas segundo [Shu e Yang (2024)](https://cs231n.stanford.edu/2024/papers/automatic-soccer-game-highlight-detection.pdf); [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/media) documenta importação, organização e metadados |
| WSC Sports | Organizações esportivas, ligas e emissoras | Analisar eventos, criar conteúdo, gerenciar ativos e distribuir resultados | [F] [Página oficial da plataforma](https://wsc-sports.com/platform/) |
| Magnifi | Produtores de vídeo, emissoras e organizações esportivas | Receber vídeo ao vivo ou gravado, gerar e etiquetar cortes e baixá-los ou distribuí-los | [F] [Página oficial do produto](https://www.magnifi.ai/product) e [FAQ](https://www.magnifi.ai/) |

## 6.2 Existem produtos que atuam na mesma área, mesmo sem serem equivalentes ao TCC?

[F] Sim. WSC Sports e Magnifi atuam com automação de conteúdo e melhores momentos esportivos. O DaVinci Resolve, Adobe Premiere Pro, CapCut, Final Cut Pro, e cap.so são alternativas indiretas para edição manual.

## 6.3 Quais interfaces profissionais esse público já conhece?

[H] H17 — Editores de vídeo esportivo provavelmente conhecem editores não lineares, como Adobe Premiere Pro e DaVinci Resolve, com player, biblioteca de mídia, marcadores, metadados, linha do tempo e exportação. Essa familiaridade precisa ser confirmada com o público-alvo.

## 6.4 O que essas soluções parecem fazer bem?

[F] As soluções automatizadas pesquisadas combinam análise, geração de cortes, metadados, organização e distribuição em escala. Magnifi declara suporte a vídeos gravados em MP4 e download dos resultados; WSC Sports declara análise contextual, criação automatizada e gestão de ativos. Fontes: páginas oficiais citadas na seção 6.1.

## 6.5 O que parecem fazer mal, dificultar ou não atender?

[?] Ainda não há evidência suficiente sobre problemas de usabilidade dessas plataformas. [H] H18 — Soluções amplas podem expor edição e distribuição além do necessário para o recorte simples de enviar, acompanhar, consultar e baixar. Preço, acesso, transparência do processamento e qualidade percebida deverão ser investigados na Entrega 2.

## 6.6 Que padrões de interface ou vocabulário parecem familiares a esse público?

[H] H19 — Player de vídeo, miniaturas, timecode, clipe, evento/lance, metadados, biblioteca de mídia, fila, progresso, status, histórico, filtros, download e exportação parecem adequados ao domínio. A terminologia deverá ser validada com editores para evitar expor termos técnicos como “inferência” ou “log” sem tradução.

---

# 7. Derivando o escopo de IHC da disciplina

## 7.1 Escolha o caminho do projeto

### Caminho A — TCC já possui interface

Explique qual parte da interface será usada como recorte da disciplina e por que esse fluxo é relevante.

Não se aplica: o escopo original do TCC não previa interface.

### Caminho B — TCC não possui interface prevista

Faça o exercício de transferência de uso:

> **Imagine que o TCC foi concluído com sucesso e uma empresa, laboratório ou organização quer transformar a contribuição em algo utilizável. Quem precisaria interagir com ela e para quê?**

Responda:

1. quem poderia contratar/adotar a solução? [H] H20 — Empresas de mídia esportiva, emissoras, produtoras, clubes, ligas e organizações que publiquem conteúdo de partidas.
2. quem seria o usuário direto? [H] H21 — Editor de vídeo esportivo responsável por obter material de melhores momentos.
3. quem administraria/configuraria? [?] A administração ainda não foi definida; no recorte inicial, parâmetros técnicos ficam sob responsabilidade da equipe técnica e não do editor.
4. quem interpretaria resultados? [H] H22 — O editor consultaria os cortes e metadados; produtores ou responsáveis editoriais poderiam utilizá-los posteriormente fora da interface.
5. quem tomaria decisões? [H] H23 — O editor decidiria quais arquivos baixar e como continuar o trabalho; a decisão de publicação poderia caber a um responsável editorial.
6. quais dados/entradas seriam necessários? [H] H24 — Um ou mais arquivos de vídeo de partidas encerradas e informações mínimas para identificá-los, como nome da partida e data. Formatos e limites ainda são [?] desconhecidos.
7. quais resultados deveriam ser compreendidos? [H] H25 — Estado do processamento, falhas e ações de recuperação, lista de lances, timecodes, classificação/metadados e arquivos disponíveis para download.
8. que erros/rupturas seriam possíveis? [H] H26 — Arquivo incompatível ou duplicado, interrupção de upload, processamento demorado, falha parcial ou total, resultado vazio, corte ou metadado incorreto e download indisponível.

## 7.2 Qual perfil será priorizado no projeto de IHC?

Editor de vídeo esportivo.

**Por que esse perfil foi escolhido?** [H] H27 — É o profissional cujo objetivo de produzir compilações se relaciona diretamente à capacidade do TCC de identificar e cortar lances. O recorte permite investigar entrada de arquivos, acompanhamento de processamento e compreensão dos resultados sem transformar a disciplina em um editor de vídeo completo. A adequação do perfil será validada nas Entregas 3 e 7.

## 7.3 Qual objetivo desse usuário será priorizado?

[H] H28 — Obter, com menor esforço manual, cortes e metadados de melhores momentos de partidas gravadas para continuar a edição ou publicação em ferramentas externas.

## 7.4 Que interface será explorada na disciplina?

Complete:

> **Para fins da disciplina de IHC, será projetada uma interface que permita a `editor de vídeo esportivo` utilizar `a identificação automática de melhores momentos e a geração de cortes e metadados` para `obter e baixar material que dará continuidade à produção de uma compilação`, no contexto de `pós-produção de uma ou mais partidas já encerradas`.**

O fluxo prioritário será: selecionar/enviar vídeos gravados → acompanhar o processamento → consultar os resultados → baixar cortes e metadados. A edição detalhada dos cortes e a publicação não serão realizadas nessa interface.

## 7.5 Qual é a relação dessa interface com o TCC?

- [ ] Já fazia parte do TCC.
- [ ] É um aprofundamento de algo parcialmente previsto.
- [ ] É uma extensão conceitual criada para a disciplina.
- [x] É um protótipo demonstrativo de aplicação potencial.
- [ ] Outra: {{...}}.

> **Declaração:** a interface desenvolvida nesta disciplina é um artefato de aprendizagem de IHC baseado no tema do TCC. Sua inclusão ou implementação no TCC somente ocorrerá se isso for posteriormente decidido pela equipe e pelo orientador.

---

# 8. Levantando possibilidades de interação — sem desenhar ainda

A equipe pode registrar possibilidades para investigação. **Não significa que todas serão implementadas.**

Marque apenas as que parecem plausíveis e explique o objetivo correspondente.

| Possibilidade | Pode fazer sentido? | Objetivo/tarefa que justificaria | Evidência atual |
|---|---|---|---|
| Dashboard/visão geral | sim | analisar o status/métricas do processamento dos vídeos atual/passados | [H] H29 |
| Configuração/parametrização | sim | identificar os vídeos enviados (nome da partida, data), escolher o modelo de IA e definir o material desejado antes do processamento | {{...}} |
| Entrada/upload/seleção de dados | sim | inputar o(s) vídeo(s) para processamento | {{...}} |
| Acompanhamento de processamento | sim | analisar as métricas/status para um vídeo específico em uma visão detalhada | {{...}} |
| Relatório/resultados | sim | analisar as saídas dos vídeos | {{...}} |
| Histórico com busca/filtros | sim | exportar os cortes do vídeo | {{...}} |
| Comparação de resultados | não | não há necessidade de comparar os resultados dos diferentes vídeos | {{...}} |
| Explicabilidade/detalhamento | sim | entender por que um trecho foi classificado como melhor momento, para decidir o que baixar e usar | {{...}} |
| Administração/configurações globais | sim | gerenciar armazenamento e retenção dos vídeos e resultados ao longo do tempo | {{...}} |
| Usuários/perfis/permissões | não | fora do recorte inicial: um único perfil (editor de vídeo esportivo); papéis e permissões ainda não definidos | {{...}} |
| CRUD de entidade do domínio | sim | gerenciar os registros das partidas enviadas (renomear, excluir, reprocessar) | {{...}} |
| Auditoria/logs | sim | investigar o motivo de falhas e o que foi produzido em cada processamento, sem depender da equipe técnica | {{...}} |
| Alertas/ocorrências | sim | ser avisado de conclusão ou falha do processamento sem precisar vigiar a tela | {{...}} |
| Ajuda/documentação | não | fora do recorte inicial: fluxo curto e linear (enviar → acompanhar → consultar → baixar) para um público familiarizado com ferramentas do domínio | {{...}} |

> **Atenção:** “login + dashboard + CRUD” não é uma solução universal. Cada padrão deve surgir de uma tarefa real.

---

# 9. Benefícios e ações iniciais

## 9.1 Qual benefício concreto o projeto de IHC pretende oferecer?

| Benefício esperado | Problema/necessidade | Usuário | Status/evidência |
|---|---|---|---|
| Economia de tempo | Necessidade de realizar manualmente cortes em vídeos brutos | Profissional responsável pela geração de vídeos de melhores momentos | H |
| Redução da subjetividade | A seleção manual pode variar devido à interpretação humana, ao cansaço ou a falhas | Profissional responsável pela geração de vídeos de melhores momentos | H |

## 9.2 Que ações o usuário deverá conseguir realizar?

| ID | O usuário precisa conseguir... | Para alcançar... | Prioridade inicial |
|---|---|---|---|
| F01 | Processar vídeos em lote | Analisar vídeos de maneira eficiente | média |
| F02 | Acompanhar o processamento por informações de observabilidade e logs | Acompanhar com precisão o processo | média |
| F03 | Visualizar o histórico de resultados | Acessar os resultados de todos os arquivos processados | média |

## 9.3 Tecnologias/restrições já definidas no TCC

A tecnologia aparece **agora**, depois do entendimento do uso.

| Tecnologia/restrição | Por que existe | Possível impacto na interação |
|---|---|---|
| Processamento de vídeo com visão computacional e LLMs multimodais | Núcleo do TCC: detecção e classificação dos melhores momentos | Tempo de processamento não trivial; a interface precisa comunicar fila, progresso e estimativas em vez de responder instantaneamente (H13) |
| Custo de inferência da LLM | Cada processamento tem custo computacional/financeiro | Reprocessar não é gratuito; a interface deve evitar envios duplicados e deixar claro quando o custo foi gerado (H08, H16) |
| Entrada em arquivo de vídeo (partidas gravadas, p. ex. MP4) | O escopo do TCC trabalha com partidas encerradas, não transmissão ao vivo | Upload de arquivos extensos; a interface precisa tratar upload lento/interrupto e formatos/limites ainda desconhecidos (H24, H26) |
| Backend sem interface prevista originalmente | O TCC previa apenas o sistema de backend | A interface da disciplina é um protótipo demonstrativo; opções como web desktop ou aplicação desktop nativa permanecem em aberto (5.2) |
| Saída em cortes de vídeo + arquivos de metadados | Formato de resultado definido pelo TCC | A interface precisa apresentar lances, timecodes e metadados de forma compreensível e permitir o download dos arquivos (H25) |

---

# 10. Hipóteses e dúvidas prioritárias

| ID | Hipótese/dúvida | Por que importa | Como poderá ser investigada |
|---|---|---|---|
| H01 | O corte e a geração de melhores momentos são feitos manualmente, demandam tempo e estão sujeitos a cansaço e falhas humanas | Motiva o problema central do TCC; se for falsa, a solução perde a justificativa | Entrega 4 (cenários) e 7 (coleta de dados) |
| H02 | Profissionais gastarão menos tempo e terão resultados menos sujeitos a variações | É o benefício esperado da solução; sustenta o valor percebido | Entrega 7 |
| H03 | O profissional responsável pelo corte é o usuário direto da aplicação | Define o usuário-alvo de todo o projeto de IHC | Entrega 3 (personas) e 7 |
| H05 | O perfil tem baixo conhecimento técnico de software e computação | Influi na simplicidade e na linguagem da interface | Entrega 3 e 7 |
| H07 | Selecionar/exportar os resultados é a atividade mais frequente | Prioriza o fluxo principal da interface | Entrega 5 (análise de tarefas) e 7 |
| H08 | Processar vídeos em lote é a atividade mais crítica | Prioriza tratamento de erro e confiabilidade | Entrega 5 e 7 |
| H12 | O uso ocorre na pós-produção, após a partida; local exato desconhecido | Define o contexto de uso e requisitos de ambiente | Entrega 3 e 7 |
| H13 | Arquivos extensos exigem armazenamento, banda e tempo; há pressão de prazo | Determina a necessidade de feedback de progresso e estados claros | Entrega 3 e 7 |
| H17 | Editores já conhecem NLEs (Premiere, Resolve), player, marcadores e timecode | Define padrões e vocabulário de interface reaproveitáveis | Entrega 2 (concorrência), 3 e 6 |
| H27 | O editor de vídeo esportivo é o perfil a priorizar | Foco do projeto de IHC; direciona personas e tarefas | Entrega 3 e 7 (validação) |
| H28 | Objetivo do usuário: obter cortes e metadados com menor esforço manual | É o objetivo que a interface deve servir | Entrega 3, 5 e 7 |

Registro completo das hipóteses H01–H29 em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

Registre em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

---

# 11. Síntese da equipe

| Pergunta | Síntese atual |
|---|---|
| Qual é a contribuição central do TCC? | Automatizar o processo de geração de cortes a partir da classificação de highlights em partidas de futebol |
| O TCC já previa interface? | não |
| Quem é o usuário prioritário de IHC? | editores de vídeo |
| O que ele precisa alcançar? | extração automática de cortes a partir de um vídeo de futebol |
| Qual problema/atividade será estudado? | classificação de highlights |
| Como isso acontece hoje? | manualmente, pessoas anotam o momento dos highlights |
| Qual é o contexto de uso? | pós produção de partidas de futebol |
| Que interface/recorte será explorado? | app de computador (desktop ou web) |
| Como a interface se relaciona ao TCC? | demosntração visual do processamento e resultados |
| Quais pontos ainda são hipóteses? | H01–H29, consolidadas na seção 10 e em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md); as prioritárias são H01, H02, H03, H05, H07, H08, H12, H13, H17, H27 e H28 |

### Delimitação

**Dentro do escopo de IHC:** transformar um vídeo íntegro de uma partida de futebol em cortes  
**Fora do escopo de IHC:** ciclo de vide completo de edição de video  
**Dentro do escopo formal do TCC:** detectar e classificar highlights em partidas de futebol  
**Interface da disciplina será implementada no TCC?** sim

---

# 12. Como esta entrega alimenta as próximas

- **Entrega 2:** verifica mercado, concorrentes e interfaces profissionais representativas.
- **Entrega 3:** detalha perfis e contexto.
- **Entrega 4:** aprofunda situações problemáticas.
- **Entrega 5:** modela tarefas centrais.
- **Entrega 6:** experimenta alternativas em baixa fidelidade.
- **Entrega 7:** investiga hipóteses com dados.
- **Entrega 8:** define restrições e metas de usabilidade.
- **Entregas 9–11:** transformam o recorte em modelo de interação e protótipo.
- **Entregas 12–14:** avaliam a interface construída na disciplina.

A Entrega 1 é uma **fotografia inicial do conhecimento**. Ela pode e deve ser revisada quando surgirem evidências.

---

# 13. Relação com INOVA e comunicação do projeto

Prepare uma explicação de até três frases:

1. **Problema/atividade humana:** classificação manual de highlights em partidas de futebol
2. **Contribuição técnica do TCC:** uso de LLMs multimodais para classificação
3. **Como uma pessoa poderia utilizar essa contribuição:** através do sistema contruído pelo projeto

Essa síntese ajuda a apresentar o projeto para público não especializado sem reduzir seu mérito técnico.

---

# Checklist de qualidade

- [x] Está clara a diferença entre tema do TCC, escopo formal do TCC e escopo de IHC.
- [x] A equipe declarou se o TCC já previa interface.
- [x] Se não previa, foi derivado um usuário plausível e um objetivo de uso.
- [x] A interface de IHC não foi apresentada como obrigação automática do TCC.
- [x] A contribuição do TCC foi descrita sem começar por tecnologias de implementação.
- [x] Usuários diretos e stakeholders foram diferenciados.
- [x] Foram considerados profissionais que configuram, administram, interpretam ou decidem, quando pertinente.
- [x] Objetivo do usuário não foi confundido com objetivo do projeto.
- [x] Processo/problema atual foi descrito antes da solução.
- [x] Existe situação concreta de uso/problema.
- [x] Contexto físico, social/organizacional, dispositivos e consequências de erro foram considerados.
- [x] Mercado/alternativas existentes foram levantados inicialmente.
- [x] Possibilidades como dashboard, relatório, histórico, filtros e CRUD foram tratadas como hipóteses de solução, não como requisitos automáticos.
- [x] Cada possibilidade de interface tem um objetivo/tarefa que poderia justificá-la.
- [x] Afirmações relevantes estão marcadas `[F]`, `[H]` ou `[?]`.
- [x] Hipóteses prioritárias receberam IDs e foram para a rastreabilidade.
- [x] O recorte de IHC é viável para modelar, prototipar e avaliar no semestre.
- [x] A equipe consegue explicar problema humano → contribuição computacional → forma de uso.
