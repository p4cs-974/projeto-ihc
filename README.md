# Entregas do projeto

01 - 🟩 Conhecendo o projeto, o usuário e o problema — concluído

02 - 🟩 Público-alvo e análise de concorrência — concluído

03 - 🟩 Personas, empatia, contexto e jornada — concluído

04 - 🟩 Cenários de análise/problema — concluído

05 - 🟩 Análise de tarefas: HTA, GOMS e CTT — concluído

06 - 🟩 Prototipação e walkthrough — concluído

07 - 🟩 Instrumentos de coleta e aspectos éticos — concluído

08 - 🟩 Ciclo de vida e engenharia de usabilidade — concluído

09 - 🟩 Modelo conceitual e design centrado na comunicação — concluído

10 - 🟩 MoLIC — concluído

11 - 🟩 Protótipo navegável integrado — concluído

12 - 🟩 Planejamento da avaliação — DECIDE — concluído

13 - 🟩 Avaliação heurística — concluído

14 - 🟩 Relatório de observação de usuário — concluído com amostra reduzida

> **Legenda:** 🟩 indica o artefato do laboratório concluído para entrega. A execução da pesquisa, as validações e as limitações estão descritas na tabela e nos respectivos relatórios.

# Projeto de Interação Humano-Computador (IHC)  - Equipe 16

> **Documentação acadêmica do projeto de IHC da Equipe 16.**
> Entrega final em 25/11/2026, com modelos, protótipo, avaliações e evidências organizados neste repositório.

## Princípio do projeto da disciplina

A disciplina utiliza **preferencialmente o tema do TCC em andamento** como domínio para exercitar os métodos de Interação Humano-Computador.

Isso vale também quando o TCC é predominantemente técnico e **não previa o desenvolvimento de uma interface**.

- Se o TCC **já prevê interface**, ela pode ser o objeto principal das atividades de IHC.
- Se o TCC **não prevê interface**, a equipe deverá derivar um **escopo de IHC** a partir da contribuição técnica: quem poderia utilizar ou se beneficiar do resultado, o que essa pessoa precisaria fazer, em qual contexto e que interação seria necessária.
- A interface criada na disciplina **não se torna automaticamente uma obrigação do TCC**. Ela pode ser um protótipo de aprendizagem, uma extensão conceitual ou uma demonstração de aplicação potencial. Sua incorporação ao TCC depende de decisão da equipe e do orientador.

Leia obrigatoriamente o [Guia para definir o escopo de IHC a partir do tema do TCC](GUIA_ESCOPO_IHC.md).

## Identificação

**Título do projeto de IHC:** Identificação de melhores momentos em partidas de futebol utilizando sistemas híbridos de visão computacional

**TCC/projeto de origem:** Identificação de melhores momentos em partidas de futebol utilizando sistemas híbridos de visão computacional
**Orientador(a):** Murillo Freitas Bouzon\
**Disciplina:** Interação Humano-Computador\
**Instituição:** Centro Universitário FEI\
**Semestre:** 2026 / 8o semestre

### Equipe

| Nome completo | Matrícula | GitHub | Responsabilidade principal |
|---|---:|---|---|
| Pedro Alexandre Custodio Silva | 22.123.049-3 | [p4cs-974](https://github.com/p4cs-974) | Envio de partidas para processamento (A01) |
| Lucas Roberto Boccia dos Santos | 22.123.012-1 | [uniflusantos](https://github.com/uniflusantos) | Revisão, seleção e download de resultados (A04) |
| Giovanni Chahin Morassi | 22.123.025-3 | [giovanni1351](https://github.com/giovanni1351) | Acompanhamento e histórico de processamento (A02/A03) e manutenção da matriz de rastreabilidade |

## Relação entre TCC e projeto de IHC

| Item | Descrição |
|---|---|
| Tema central do TCC | Identificação de melhores momentos em partidas de futebol utilizando sistemas híbridos de visão computacional |
| Resultado técnico esperado do TCC | Sistema híbrido de visão computacional (algoritmo, modelo de IA/LLM, análise de dataset, benchmark e backend) que recebe vídeos de partidas e produz cortes de melhores momentos com metadados |
| O TCC já previa interface? | não — previa apenas o sistema de backend; a interface surgiu para a disciplina de IHC |
| Capacidade técnica que pode gerar valor para pessoas | Identificação automática de melhores momentos e geração dos respectivos cortes de vídeo e metadados, reduzindo o trabalho manual de edição |
| Usuário principal adotado em IHC | Editor de vídeo esportivo, responsável por obter material de melhores momentos (H27) |
| Objetivo principal desse usuário | Obter, com menor esforço manual, cortes e metadados de melhores momentos de partidas gravadas para continuar a edição ou publicação em ferramentas externas (H28) |
| Interface/recorte explorado na disciplina | Interface para enviar vídeos gravados, acompanhar o processamento, consultar os resultados e baixar cortes e metadados — sem edição detalhada nem publicação |
| Relação com o escopo formal do TCC | protótipo demonstrativo de aplicação potencial |

> **Importante:** a tabela acima explica a relação entre os dois trabalhos. Ela não altera o compromisso formal do TCC.

## Resumo do projeto pela perspectiva do usuário

O projeto parte da hipótese de que um editor de vídeo esportivo precisa produzir compilações de melhores momentos após o encerramento das partidas e dedica esforço a assistir à gravação, localizar lances, definir cortes e organizar o material. O TCC investiga um sistema híbrido de visão computacional para apoiar a identificação desses momentos. Para a disciplina de IHC, a equipe desenvolveu uma interface demonstrativa para preparar gravações, acompanhar a análise, revisar os candidatos e obter cortes e metadados para continuar a edição em ferramentas externas. As hipóteses sobre práticas profissionais e ganhos de produtividade estão identificadas na [Entrega 1](docs/01_conhecendo_o_problema.md).

## Por que pensar em interface mesmo em TCCs técnicos?

Algoritmos, modelos, APIs, análises de datasets e componentes de infraestrutura podem não exigir interface como resultado acadêmico do TCC. Porém, quando essas contribuições são transferidas para uma situação real, normalmente existem pessoas que:

- configuram parâmetros;
- fornecem ou selecionam dados;
- iniciam ou acompanham processamento;
- interpretam resultados;
- comparam alternativas;
- tomam decisões;
- administram usuários e permissões;
- consultam histórico;
- geram relatórios;
- investigam erros;
- auditam mudanças.

Essas atividades fornecem um campo legítimo para exercitar IHC.

Possibilidades de interface incluem **dashboards, telas administrativas, configuração, relatórios, histórico com filtros, comparação de resultados, visualização de dados, acompanhamento de processamento, gestão de perfis e permissões, CRUDs justificados pelo domínio, alertas, auditoria e ajuda contextual**. Nenhuma dessas telas é obrigatória por si só: deve existir uma tarefa e um objetivo de usuário que a justifique.

## Relação com apresentação e potencial de aplicação

A reflexão sobre usuários ajuda a equipe a explicar o projeto para públicos externos, inclusive em eventos como a **INOVA**. Em vez de comunicar apenas a técnica implementada, a equipe pode apresentar:

**problema humano → contribuição computacional → forma de uso → impacto potencial**.

O protótipo de IHC pode, portanto, funcionar como uma demonstração do potencial de mercado, transferência tecnológica ou impacto extensionista do tema do TCC, sem necessariamente integrar a implementação final do trabalho de conclusão.

## Como usar este repositório

1. Leia o [Guia de uso e apresentação](GUIA_DE_USO.md).
2. Leia o [Guia de definição de escopo de IHC](GUIA_ESCOPO_IHC.md), especialmente se o TCC não previa interface.
3. Preencha as entregas na ordem em que forem trabalhadas na disciplina.
4. Em toda entrega individual, **identifique o autor**.
5. Salve imagens, diagramas e evidências em [`assets/`](assets/README.md).
6. Mantenha a [Matriz de rastreabilidade](RASTREABILIDADE.md) atualizada.
7. Na Entrega 1, diferencie **[F] fatos**, **[H] hipóteses** e **[?] lacunas de conhecimento**.
8. Antes de cada entrega, revise o checklist do arquivo e o [Checklist final](CHECKLIST_FINAL.md).
9. Sempre que uma evidência posterior contrariar uma hipótese inicial, **revise o projeto**. IHC é um processo iterativo.

## Entregas

| # | Entrega | Quantidade mínima / responsabilidade | Status |
|---:|---|---|---|
| 1 | [Conhecendo o projeto, o usuário e o problema](docs/01_conhecendo_o_problema.md) | 1 solução consolidada por equipe | 🟩 concluída |
| 2 | [Público-alvo e análise de concorrência](docs/02_analise_concorrencia.md) | no mínimo 1 concorrente/interface representativa por integrante + síntese | 🟩 concluída; C06/C07 dispensadas pelo professor em sala |
| 3 | [Personas, empatia, contexto e jornada](docs/03_personas_contexto_jornada.md) | 1 persona por integrante; demais artefatos consolidados | 🟩 personas, empatia, contexto e jornadas concluídos |
| 4 | [Cenários de análise/problema](docs/04_cenarios_problema.md) | 1 solução completa por integrante | 🟩 cenários concluídos e revisados |
| 5 | [Análise de tarefas: HTA, GOMS e CTT](docs/05_analise_tarefas.md) | cada integrante: pelo menos 1 HTA + 1 GOMS + 1 CTT | 🟩 HTA, GOMS e CTT dos três integrantes concluídos |
| 6 | [Prototipação em papel](docs/06_prototipacao_papel.md) · [protótipo](assets/06_prototipos/PROTOTIPO_fluxo_highlights.html) · [parecer](feedbacks_professor/Feedback_Professor_Entrega06_Equipe16.md) | 1 protótipo integrado por equipe | 🟩 protótipo, walkthrough e revisão documentados |
| 7 | [Coleta de dados e aspectos éticos](docs/07_coleta_dados.md) · [parecer](feedbacks_professor/Feedback_Professor_Entrega07_Equipe16.md) | soluções individuais + técnicas distintas; questionário entre as técnicas | 🟩 instrumentos e aspectos éticos documentados; coleta I01–I03 não executada |
| 8 | [Ciclo de vida e engenharia de usabilidade](docs/08_engenharia_usabilidade.md) · [parecer](feedbacks_professor/Feedback_Professor_Entrega08_Equipe16.md) | 1 solução consolidada por equipe | 🟩 ciclo de vida, princípios e metas especificados |
| 9 | [Modelo conceitual e design centrado na comunicação](docs/09_modelo_conceitual.md) · [parecer](feedbacks_professor/Feedback_Professor_Entrega09_Equipe16.md) | soluções individuais + consolidação de objetivos/signos | 🟩 modelo conceitual, objetivos e signos documentados |
| 10 | [MoLIC](docs/10_molic.md) · [parecer](feedbacks_professor/Feedback_Professor_Entrega10_Equipe16.md) | 1 diagrama completo por integrante | 🟩 três diagramas MoLIC documentados |
| 11 | [Protótipo navegável integrado](docs/11_figma.md) | 1 protótipo integrado por equipe, cobrindo fluxos modelados | 🟩 [protótipo publicado](https://ihc-11.p4cs.com.br/) e documentação concluída |
| 12 | [Planejamento da avaliação — DECIDE](docs/12_planejamento_avaliacao.md) | 1 plano consolidado por equipe | 🟩 plano DECIDE e cinco instrumentos concluídos |
| 13 | [Avaliação heurística](docs/13_avaliacao_heuristica.md) | 1 avaliação completa por integrante, todas as telas/estados e 10 heurísticas | 🟩 três inspeções, 33 achados consolidados e exemplos concluídos |
| 14 | [Avaliação por observação de usuários](docs/14_observacao_usuario.md) | avaliação consolidada; nº de participantes finais = nº de integrantes | 🟩 relatório concluído com uma sessão exploratória e [vídeo](https://youtu.be/AxZfRabCQ-E); amostra reduzida e limitações registradas |

> Se o docente definir quantidade diferente para a turma/semestre, a orientação da disciplina prevalece.

## Visão de continuidade

O projeto deve formar uma cadeia de evidências:

**tema/contribuição do TCC → possível aplicação → usuários/stakeholders → objetivos → problema/contexto → alternativas → necessidades → personas → cenários → tarefas → modelo conceitual → MoLIC → protótipo → planejamento → inspeção → teste com usuários → melhorias**.

Uma entrega não deve “reiniciar” o projeto. Se o escopo de IHC foi criado para um DBA, por exemplo, as personas, tarefas, MoLIC, protótipo e avaliação devem permanecer coerentes com esse perfil, salvo quando novas evidências justificarem a revisão.

## Conclusões do projeto

O trabalho conectou o problema e os perfis de referência às personas, cenários, tarefas, modelo conceitual, MoLIC e protótipo navegável. A interface demonstra como preparar um lote, acompanhar a análise, revisar lances e obter arquivos MP4 e referências CSV para edição externa. O [protótipo publicado](https://ihc-11.p4cs.com.br/) utiliza exemplos do SoccerNet e processamento simulado, conforme os limites registrados na [Entrega 11](docs/11_figma.md).

A [avaliação heurística](docs/13_avaliacao_heuristica.md) reuniu três inspeções e 33 achados consolidados. A [observação exploratória](docs/14_observacao_usuario.md), registrada no [único vídeo da entrega](https://youtu.be/AxZfRabCQ-E), acrescentou nove achados sobre descoberta de controles, continuidade dos resultados e expectativa de cancelamento. Esses resultados orientam melhorias para uma próxima iteração. A amostra reduzida e a ausência de medições quantitativas estão explicitadas no relatório; as recomendações não representam alterações já implementadas ou validadas.

## Documentos de apoio

- [Guia de uso e apresentação](GUIA_DE_USO.md)
- [Guia para definir o escopo de IHC a partir do TCC](GUIA_ESCOPO_IHC.md)
- [Matriz de rastreabilidade](RASTREABILIDADE.md)
- [Checklist final](CHECKLIST_FINAL.md)
- [Bibliografia de IHC](BIBLIOGRAFIA.md)
- [Orientações de contribuição no GitHub](CONTRIBUTING.md)
- [Instrumentos reutilizáveis](instrumentos/README.md)
