# Matriz de rastreabilidade de IHC

A matriz deve ser atualizada ao longo do semestre. Ela ajuda a demonstrar que a interface não surgiu arbitrariamente e registra **como o conhecimento da equipe evoluiu**.

Para projetos cujo TCC não previa interface, esta matriz é especialmente importante: deve ficar visível a passagem da **contribuição técnica do TCC** para um **cenário de uso plausível**, e desse cenário para as decisões de interação.

## 1. Derivação do escopo de IHC a partir do TCC

| Elemento | Registro da equipe | Evidência/justificativa | Estado |
|---|---|---|---|
| Tema do TCC | Identificação de Melhores Momentos em Partidas de Futebol Utilizando Sistemas Híbridos de Visão Computacional | [`docs/01`](docs/01_conhecendo_o_problema.md) seção 0.2 | definido |
| Resultado técnico esperado | Sistema híbrido de visão computacional que recebe vídeos de partidas e produz cortes e metadados de melhores momentos (algoritmo, modelo de IA/LLM, análise de dataset, benchmark e backend) | [`docs/01`](docs/01_conhecendo_o_problema.md) seção 0.4 | definido |
| O TCC previa interface? | não — o TCC previa apenas o backend | [`docs/01`](docs/01_conhecendo_o_problema.md) seção 0.5 | definido |
| Capacidade/contribuição central | Identificação automática de melhores momentos e geração de cortes + metadados | [`docs/01`](docs/01_conhecendo_o_problema.md) seção 1.3 | definido |
| Possíveis beneficiários/stakeholders | Profissional responsável pelo corte (usuário direto) e empresas de mídia esportiva (stakeholder indireto) | [`docs/01`](docs/01_conhecendo_o_problema.md) seções 2.2–2.3; hipóteses H03 e H04 | H |
| Usuário escolhido para IHC | Editor de vídeo esportivo responsável por obter material de melhores momentos | [`docs/01`](docs/01_conhecendo_o_problema.md) seção 7.2; hipótese H27 | H |
| Objetivo principal do usuário | Obter, com menor esforço manual, cortes e metadados de melhores momentos de partidas gravadas | [`docs/01`](docs/01_conhecendo_o_problema.md) seção 7.3; hipótese H28 | H |
| Contexto de uso adotado | Pós-produção de partidas já encerradas, em computador com tela ampla; fluxo enviar → acompanhar → consultar → baixar | [`docs/01`](docs/01_conhecendo_o_problema.md) seções 5.1–5.2 e 7.4; hipóteses H12 e H13 | H |
| Interface/recorte de IHC | Interface para enviar vídeos gravados, acompanhar o processamento, consultar e baixar cortes e metadados (sem edição detalhada nem publicação) | [`docs/01`](docs/01_conhecendo_o_problema.md) seção 7.4; deriva das linhas acima | proposta |
| Relação com o TCC | protótipo demonstrativo de aplicação potencial (artefato de aprendizagem de IHC, não obrigação do TCC) | [`docs/01`](docs/01_conhecendo_o_problema.md) seção 7.5 | definido |

> Se o escopo de IHC mudar ao longo do semestre, preserve a decisão anterior no histórico e registre **qual evidência motivou a mudança**.

## 2. Registro de hipóteses e lacunas da Entrega 1

Use esta tabela para itens importantes marcados como `[H]` ou `[?]`. Preserve o histórico: não apague uma hipótese refutada.

| ID | Afirmação / dúvida inicial | Tipo | Por que importa | Como/onde investigar | Evidência obtida | Estado atual | Impacto no projeto |
|---|---|---|---|---|---|---|---|
| H01 | O corte e a geração de melhores momentos são feitos manualmente, demandam tempo e estão sujeitos a cansaço e falhas humanas | H | Motiva o problema central do TCC | Entrega 4 (cenários) e 7 (coleta de dados) | PENDENTE | aberta | Problema central a resolver |
| H02 | Profissionais gastarão menos tempo e terão resultados menos sujeitos a variações por cansaço ou falha | H | Benefício esperado da solução | Entrega 7 | PENDENTE | aberta | Justifica o valor da solução |
| H03 | O profissional responsável pelo corte de melhores momentos é o usuário direto da aplicação | H | Define o usuário-alvo do IHC | Entrega 3 (personas) e 7 | PENDENTE | aberta | Define persona e recorte |
| H04 | Empresas de mídia esportiva são stakeholders afetadas (menos custos por maior eficiência) | H | Mapeia stakeholders e adoção | Entrega 2 (concorrência) e 7 | PENDENTE | aberta | Mercado e adoção |
| H05 | O perfil tem baixo conhecimento técnico de software e computação | H | Influi na simplicidade da interface | Entrega 3 e 7 | PENDENTE | aberta | Curva de aprendizado e linguagem |
| H06 | O usuário quer produzir vídeos de melhores momentos com eficiência e consistência, reduzindo o esforço manual | H | Objetivo do usuário no mundo real | Entrega 3, 5 e 7 | PENDENTE | aberta | Objetivo central do projeto |
| H07 | Selecionar/exportar os resultados processados é a atividade mais frequente | H | Prioriza tarefas e fluxos da interface | Entrega 5 e 7 | PENDENTE | aberta | Fluxo principal da interface |
| H08 | Processar vídeos em lote é a atividade mais crítica (retrabalho, custo de inferência, perda de arquivos) | H | Prioriza tarefas e tratamento de erro | Entrega 5 e 7 | PENDENTE | aberta | Confiabilidade do fluxo |
| H09 | A análise depende da precisão e subjetividade do profissional (distração pode fazer perder lances) | H | Dor central do processo atual | Entrega 4 e 7 | PENDENTE | aberta | Problema que a solução ataca |
| H10 | Lances interessantes podem ficar fora dos highlights finais por rotulação inadequada | H | Consequência de falha no processo atual | Entrega 4 e 7 | PENDENTE | aberta | Qualidade percebida do resultado |
| H11 | Cenário: editor recebe a gravação integral e prepara melhores momentos sob pressão de prazo, com risco de omitir/recortar sem contexto | H | Situação concreta de uso/problema | Validar por entrevista/observação nas Entregas 4 e 7 | PENDENTE | aberta | Base do cenário de problema (Entrega 4) |
| H12 | Uso no fluxo de pós-produção, após a partida; local exato (emissora, produtora, clube, remoto) desconhecido | H | Contexto de uso | Entrega 3 e 7 | PENDENTE | aberta | Contexto e requisitos de ambiente |
| H13 | Arquivos extensos exigem armazenamento, banda e tempo; a interface deve deixar claros upload, fila, progresso, falha e conclusão; há pressão de prazo e interrupções | H | Condições físicas do uso | Entrega 3 e 7 | PENDENTE | aberta | Feedback de progresso e estados |
| H14 | O editor entrega arquivos a produtores/responsáveis editoriais que aprovam e publicam; papéis, permissões e políticas ainda indefinidos | H | Fatores organizacionais e papéis | Entrega 3 e 7 | PENDENTE | aberta | Permissões e fluxo de aprovação |
| H15 | Um histórico com nome, data, estado, entradas, resultados e motivo de falha ajudaria; necessidade de auditoria formal desconhecida | H | Funcionalidades de histórico/rastreabilidade | Entrega 5, 7 e 8 | PENDENTE | aberta | Tela de histórico/estado |
| H16 | Erros (arquivo incompatível, upload interrompido, falha, resultado incompleto) causam atraso, retrabalho e custo; não apresentar o resultado como infalível | H | Tratamento de erro e confiabilidade | Entrega 8 e 12–14 | PENDENTE | aberta | Mensagens de erro e recuperação |
| H17 | Editores conhecem NLEs (Premiere, Resolve) com player, biblioteca de mídia, marcadores, metadados, linha do tempo e exportação | H | Vocabulário e padrões familiares | Entrega 2, 3 e 6 | PENDENTE | aberta | Padrões de interface reaproveitáveis |
| H18 | Soluções amplas podem expor edição/distribuição além do necessário; preço, acesso, transparência e qualidade percebida a investigar | H | Define o recorte da interface | Entrega 2 e 7 | PENDENTE | aberta | Escopo do protótipo |
| H19 | Vocabulário familiar: player, miniaturas, timecode, clipe, evento/lance, metadados, fila, progresso, status, histórico, filtros, download e exportação | H | Terminologia da interface | Entrega 2, 3 e 6 | PENDENTE | aberta | Linguagem da interface |
| H20 | Quem contrataria/adotaria a solução: empresas de mídia esportiva, emissoras, produtoras, clubes, ligas e organizações | H | Adoção da solução | Entrega 2 e 7 | PENDENTE | aberta | Mercado-alvo |
| H21 | Usuário direto: editor de vídeo esportivo responsável por obter material de melhores momentos | H | Perfil priorizado | Entrega 3 e 7 | PENDENTE | aberta | Persona principal |
| H22 | O editor consulta cortes e metadados; produtores ou responsáveis editoriais podem usá-los fora da interface | H | Quem interpreta os resultados | Entrega 3 e 7 | PENDENTE | aberta | Escopo de consumo dos resultados |
| H23 | O editor decide quais arquivos baixar e como continuar o trabalho; a publicação pode caber a um responsável editorial | H | Decisões e responsabilidades | Entrega 3 e 7 | PENDENTE | aberta | Limites da interface |
| H24 | Entradas: arquivos de vídeo de partidas encerradas + nome e data; formatos e limites desconhecidos | H | Requisitos de entrada | Entrega 5, 7 e 8 | PENDENTE | aberta | Upload e validação |
| H25 | Resultados a compreender: estado do processamento, falhas e recuperação, lances, timecodes, metadados e downloads | H | Requisitos de saída | Entrega 5 e 7 | PENDENTE | aberta | Tela de resultados/download |
| H26 | Erros possíveis: arquivo incompatível/duplicado, upload interrompido, processamento demorado, falha, resultado vazio, corte/metadado incorreto, download indisponível | H | Tratamento de erro | Entrega 5, 8 e 12–14 | PENDENTE | aberta | Estados de erro da interface |
| H27 | Perfil escolhido: editor de vídeo esportivo; o recorte permite investigar entrada, acompanhamento e resultados sem virar editor completo | H | Foco do projeto de IHC | Entrega 3 e 7 (validação) | PENDENTE | aberta | Persona e escopo do projeto |
| H28 | Objetivo priorizado: obter, com menor esforço manual, cortes e metadados de melhores momentos para continuar a edição/publicação | H | Objetivo de usuário central | Entrega 3, 5 e 7 | PENDENTE | aberta | Objetivo da interface |
| H29 | Uma visão geral (dashboard) com status/métricas do processamento dos vídeos atuais e passados seria útil | H | Justifica o padrão de interface “dashboard” | Entrega 5 (tarefas) e 7 | PENDENTE | aberta | Tela de dashboard/visão geral |

## 3. Rastreabilidade entre contribuição técnica, necessidades e artefatos

| ID | Capacidade do TCC utilizada | Necessidade/problema | Persona | Cenário problema | Objetivo/tarefa | HTA/GOMS/CTT | Cenário de interação / signos | MoLIC | Tela(s) Figma | Heurística / problema | Tarefa no teste | Decisão/melhoria |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | {{ex.: recomendação de otimização}} | {{...}} | {{P01}} | {{C01}} | {{T01}} | {{links}} | {{...}} | {{M01}} | {{F01...}} | {{V01 ou —}} | {{UT01}} | {{...}} |
| R02 |  |  |  |  |  |  |  |  |  |  |  |  |

## 4. Rastreabilidade de padrões de interface

Use esta tabela quando o projeto incorporar padrões como dashboard, relatório, histórico, filtros ou administração. O objetivo é **justificar o padrão**, não apenas listar telas.

| ID da tela/fluxo | Padrão de interface | Objetivo/tarefa que justifica | Informação/ação principal | Evidência de necessidade | Artefatos relacionados |
|---|---|---|---|---|---|
| F01 | dashboard | {{T01}} | {{...}} | {{H01/evidência...}} | {{C01/M01}} |
| F02 | histórico com filtros | {{T02}} | {{...}} | {{...}} | {{...}} |
| F03 | administração/CRUD | {{T03}} | {{...}} | {{...}} | {{...}} |

## 5. Registro de mudanças de escopo

| Data | O que mudou | Evidência/feedback que motivou | Artefatos afetados | Responsável |
|---|---|---|---|---|
| {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

## Como usar

- Use identificadores estáveis (`H01`, `P01`, `C01`, `T01`, `M01`, `F01`, `UT01`).
- Quando uma necessidade/problema tiver origem em hipótese da Entrega 1, cite o ID correspondente.
- Em TCC sem interface original, pelo menos uma linha deve mostrar claramente **como uma capacidade técnica chega até uma tarefa de usuário e uma tela/fluxo**.
- Uma linha pode se desdobrar quando um objetivo possui múltiplos caminhos.
- Não force relação inexistente: se algo ainda não foi modelado, marque `PENDENTE`.
- Ao remover uma funcionalidade, registre a decisão em vez de apagar silenciosamente o histórico.
- Dashboard, CRUD, filtros e relatórios só devem aparecer quando houver objetivo/tarefa que os justifique.
