# Melhores Momentos — Projeto de IHC da Equipe 16

**Entrega final documental: 25/11/2026.** O repositório reúne a definição do problema, os modelos de interação, o protótipo e as avaliações de uma interface para preparar material de melhores momentos de partidas de futebol. A observação de uso foi encerrada com **uma sessão exploratória e um único vídeo**. As limitações e os requisitos não atendidos estão registrados na [Entrega 14](docs/14_observacao_usuario.md) e no [checklist final](CHECKLIST_FINAL.md).

## Identificação

**Projeto/TCC de origem:** Identificação de melhores momentos em partidas de futebol utilizando sistemas híbridos de visão computacional\
**Orientador:** Murillo Freitas Bouzon\
**Disciplina:** Interação Humano-Computador · Centro Universitário FEI · 2026 / 8º semestre

| Integrante | Matrícula | GitHub | Recorte de referência |
|---|---|---|---|
| Pedro Alexandre Custodio Silva | 22.123.049-3 | [p4cs-974](https://github.com/p4cs-974) | Envio e revisão de material; P01/T01 |
| Lucas Roberto Boccia dos Santos | 22.123.012-1 | [uniflusantos](https://github.com/uniflusantos) | Supervisão editorial externa; P02/T02 |
| Giovanni Chahin Morassi | 22.123.025-3 | [giovanni1351](https://github.com/giovanni1351) | Acompanhamento e tratamento de falhas; P03/T03 |

## Problema, público e escopo

O projeto parte da hipótese de que editores esportivos gastam esforço ao assistir a gravações, localizar lances e organizar cortes para edição. O público de referência inclui o editor profissional (P01) e o criador amador (P03); o supervisor editorial (P02) recebe e aprova material por canais externos. Essas caracterizações são modelos de projeto, sem validação empírica suficiente para generalizar rotinas ou ganhos de produtividade. A [Entrega 1](docs/01_conhecendo_o_problema.md) distingue fatos, hipóteses e lacunas.

O TCC investiga um sistema híbrido de visão computacional que recebe partidas e produz cortes e metadados. O TCC previa backend; a interface foi derivada para a disciplina de IHC como **protótipo demonstrativo de aplicação potencial**, sem se tornar obrigação formal do TCC.

O objetivo de interação é preparar o lote, acompanhar o processamento, revisar candidatos e obter vídeos MP4 e referências CSV para continuar o trabalho em ferramentas externas. Montagem, chancela e publicação permanecem fora da interface.

## Acesso ao protótipo e às evidências

- [Protótipo publicado e avaliado](https://ihc-11.p4cs.com.br/) — commit `7405221`, referência comum das Entregas 13 e 14.
- [Documentação do protótipo, telas e limites](docs/11_figma.md) — distingue a versão publicada da revisão local posterior.
- [Vídeo da única sessão exploratória EXP01](https://youtu.be/AxZfRabCQ-E) — 24/11/2026, duração 06:44; [relatório, achados e limites de uso](docs/14_observacao_usuario.md#vídeo-ilustrativo-do-teste-e-dos-resultados).
- [Transcrição higienizada](assets/14_testes/transcript.md) e [39 quadros da interface](assets/14_testes/frames_video/) — evidências locais da observação, sem o arquivo audiovisual bruto.
- [Inspeções individuais e consolidação heurística](docs/13_avaliacao_heuristica.md) — três avaliadores, dez heurísticas e 33 achados consolidados.

O protótipo usa quatro tempos de duas partidas do SoccerNet-v2 e oito cortes reais em 224p. Upload próprio está indisponível; fila, progresso, falha e ausência de lances são simulados. A demonstração não comprova precisão ou desempenho do detector. As avaliações dizem respeito à interação com essa versão.

## Entregas e situação no fechamento

“Documentada” indica que o artefato está apresentado; não equivale a validação empírica ou aprovação do docente. Atividades não realizadas são limitações desta entrega, sem previsão de novas gravações ou coleta neste fechamento.

| # | Entrega | Situação final documentada |
|---:|---|---|
| 1 | [Conhecendo o projeto, o usuário e o problema](docs/01_conhecendo_o_problema.md) | Preenchida; hipóteses e lacunas identificadas. |
| 2 | [Público-alvo e análise de concorrência](docs/02_analise_concorrencia.md) | Preenchida; pendências de C06/C07 dispensadas pelo professor em sala, conforme registro anterior. |
| 3 | [Personas, empatia, contexto e jornada](docs/03_personas_contexto_jornada.md) | Revisão documental concluída; proto-personas sem validação empírica suficiente. |
| 4 | [Cenários de análise/problema](docs/04_cenarios_problema.md) | Revisão documental concluída; cenários hipotéticos. |
| 5 | [Análise de tarefas: HTA, GOMS e CTT](docs/05_analise_tarefas.md) | Três tarefas documentadas e coerência revisada; modelos hipotéticos. |
| 6 | [Prototipação em papel](docs/06_prototipacao_papel.md) | Walkthrough da v1 registrado; v2 revisada, sem verificação específica com participante. |
| 7 | [Coleta de dados e aspectos éticos](docs/07_coleta_dados.md) | Instrumentos e protocolo documentados; pilotos e pesquisa I01–I03 não executados. |
| 8 | [Ciclo de vida e engenharia de usabilidade](docs/08_engenharia_usabilidade.md) | Metas especificadas; sem resultados quantitativos. Pesos e MU07/MU08 permanecem propostas. |
| 9 | [Modelo conceitual e design centrado na comunicação](docs/09_modelo_conceitual.md) | Documentação consolidada; aceite individual dos autores não registrado. |
| 10 | [MoLIC](docs/10_molic.md) | Três modelos documentados; aceite individual não registrado. |
| 11 | [Protótipo navegável integrado](docs/11_figma.md) | Publicado e documentado; cobertura parcial e limites explícitos. |
| 12 | [Planejamento da avaliação — DECIDE](docs/12_planejamento_avaliacao.md) | Plano e cinco instrumentos documentados; execução reduzida registrada como desvio. |
| 13 | [Avaliação heurística](docs/13_avaliacao_heuristica.md) | Três inspeções, H1–H10, 33 achados e consolidação concluídos. |
| 14 | [Avaliação por observação de usuários](docs/14_observacao_usuario.md) | Relatório encerrado com uma exploração guiada (EXP01), nove achados e comparação com a inspeção; amostra mínima e métricas estruturadas não atendidas. |

## Conclusões do projeto

A disciplina permitiu transformar uma contribuição técnica do TCC em um percurso de interação rastreável: preparar gravações, acompanhar a análise, revisar os candidatos e obter material para edição externa. Personas, cenários, tarefas, objetivos, signos e MoLIC fundamentaram as telas, com os vínculos preservados na [matriz de rastreabilidade](RASTREABILIDADE.md).

A inspeção de três avaliadores consolidou **33 problemas (HC01–HC33)**, dos quais quatro receberam severidade 3: falha na entrada dos exemplos, reinício com seleção de execução anterior, navegação incompleta no mosaico e perda de seleção ao recarregar. A única observação exploratória gerou **nove achados (AU01–AU09)**, incluindo a expectativa espontânea de cancelar uma análise e dificuldades para descobrir detalhes, modos de visualização e novos lances disponíveis. Esses métodos trouxeram evidências complementares sobre a interface; a sessão guiada não mede recorrência entre usuários nem sucesso independente.

O participante elogiou o fluxo, a estética e as visualizações em linha do tempo e mosaico, especialmente após sua apresentação pelo moderador. Esses sinais de valor percebido orientam a evolução do protótipo, mas não comprovam eficácia, produtividade ou satisfação por escala. **MU01–MU08 não foram avaliadas quantitativamente.** Não houve a pesquisa de necessidades I01–I03, as três sessões estruturadas previstas, o piloto formal ou o retorno de memorização; o perfil profissional do participante não foi verificado. A quantidade mínima de observação não foi atendida e não há dispensa docente registrada.

As recomendações prioritárias são tornar as ações mais visíveis, melhorar a recuperação de erros e a continuidade dos resultados, esclarecer as saídas CSV/MP4 e reconsiderar cancelamento e persistência de seleção. **São propostas para uma próxima iteração**, com necessidade de revisar modelos e reavaliar as mudanças. Não foram implementadas nem validadas como parte deste fechamento. O resultado entregue é um protótipo acadêmico acompanhado de modelos, evidências e limites explícitos, sem afirmação de validação do produto ou do detector do TCC.

## Documentos de apoio

- [Checklist final e requisitos não atendidos](CHECKLIST_FINAL.md)
- [Matriz de rastreabilidade](RASTREABILIDADE.md)
- [Guia de uso e apresentação](GUIA_DE_USO.md)
- [Guia para definir o escopo de IHC a partir do TCC](GUIA_ESCOPO_IHC.md)
- [Bibliografia de IHC](BIBLIOGRAFIA.md)
- [Orientações de contribuição](CONTRIBUTING.md)
- [Instrumentos reutilizáveis](instrumentos/README.md)
- [Evidências e organização dos assets](assets/README.md)
