# Entrega 13: avaliação de IHC por inspeção heurística

**Data:** 19/11/2026 (estrutura, escopo, fluxograma e fichas individuais preparados; inspeções em andamento)\
**Status:** 🟨 em andamento (escopo congelado, fluxograma criado e fichas individuais abertas; inspeções A01–A03, consolidação e exemplos da seção 8 pendentes)\
**Responsabilidade:** 1 avaliação completa e independente por integrante da Equipe 16 (Pedro Alexandre Custodio Silva, Lucas Roberto Boccia dos Santos e Giovanni Chahin Morassi), seguida de consolidação coletiva.

## Objetivo da atividade

Encontrar problemas de usabilidade no protótipo **Melhores Momentos** por inspeção sistemática com as **10 heurísticas de Nielsen**. Cada avaliador percorre todas as telas e estados individualmente antes de qualquer discussão; depois a equipe consolida violações equivalentes, define severidades finais e prioriza correções antes da observação com usuários ([Entrega 14](14_observacao_usuario.md)).

A inspeção avalia exclusivamente a interface e o diálogo do protótipo. A precisão da detecção de lances, a cobertura dos eventos e o desempenho do modelo híbrido pertencem à avaliação técnica do TCC ([Entrega 12](12_planejamento_avaliacao.md#o-que-está-sendo-avaliado)).

## 1. Heurísticas adotadas

1. **H1:** Visibilidade do status do sistema
2. **H2:** Compatibilidade entre o sistema e o mundo real
3. **H3:** Controle e liberdade do usuário
4. **H4:** Consistência e padrões
5. **H5:** Prevenção de erros
6. **H6:** Reconhecimento em vez de memorização
7. **H7:** Flexibilidade e eficiência de uso
8. **H8:** Estética e design minimalista
9. **H9:** Ajudar usuários a reconhecer, diagnosticar e recuperar-se de erros
10. **H10:** Ajuda e documentação

### Cobertura de estados no escopo de Melhores Momentos

A inspeção não se limita ao fluxo feliz. A tabela abaixo separa os estados críticos que existem no protótipo daqueles que estão fora do recorte definido na [Entrega 1](01_conhecendo_o_problema.md) e na [Entrega 11](11_figma.md).

| Categoria | Situação no protótipo | Onde inspecionar |
|---|---|---|
| Processamento, fila e progresso | Aplicável (simulado com mídia real em 2×) | F02 e F03 (fila, andamento, resultados parciais, conclusão e reinício) |
| Filtros, busca sem resultado e modos alternativos | Aplicável | F04 A (busca textual, filtros por tipo/vídeo e limpeza de consulta vazia), F04 B (trilhas) e F04 C (mosaico) |
| Exportação e obtenção de saídas | Aplicável | F05 (download individual de MP4) e F06 (seleção vazia, separação CSV × MP4, tamanhos e aviso do navegador) |
| Falha, recuperação e confirmação de ação | Aplicável (cobre `QA10`) | F01 (indisponibilidade de manifesto, se simulada), F02 (lote vazio), F03/F04 (falha encenada, confirmação/cancelamento de nova tentativa localizada e opção de deixar pendente), F05 (falha e nova tentativa do player) |
| Tradução de termos técnicos e metadados | Aplicável | F02, F04, F05 e F06 (partida, tempo, relógio do jogo, posição no arquivo, duração, tamanho e distinção entre relação CSV e arquivos MP4) |
| Navegação transversal, foco e teclado | Aplicável | Barra lateral (`aria-current`), contorno de foco, atalhos de teclado (`Tab`, `Enter`, `Esc`, setas, `/`), preservação na sessão e efeito da recarga |
| Dashboard administrativo, CRUD de permissões, histórico persistente e comparação de modelos do TCC | Fora do escopo de IHC | Não existem no protótipo ([Entrega 11](11_figma.md#cobertura-molic-e-limites) e [Entrega 12](12_planejamento_avaliacao.md#o-que-está-sendo-avaliado)) |

## 2. Escopo da inspeção

| Item | Definição |
|---|---|
| Versão avaliada | Preview público em [ihc-11.p4cs.com.br](https://ihc-11.p4cs.com.br/), correspondente ao commit `7405221` (arquivo-fonte de `7d52cdd`, publicado em 13/11/2026). SHA-256 do HTML verificado em 19/11/2026: `aa6ec94773a783559e352f69ff5507bd3a8af9301c3830b832de879104b6f33c`. O commit local `62bbbed` (18/11/2026) não foi publicado nesse link e fica fora desta rodada. |
| Telas e estados | **F01** (entrada: carregamento de exemplos, envio próprio indisponível e erro de manifesto quando reproduzido); **F02** (lote: 4 tempos, remoção, lote vazio, reposição e seleção dos cenários normal, falha e vídeo sem lances); **F03** (análise: fila, progresso, resultados parciais, conclusão, falha encenada, vídeo sem lances e transições para F04); **F04** (destaques: lista A com busca/filtros/vazio, trilhas B, mosaico C, preservação de seleção e faixa de falha com confirmação/cancelamento de nova tentativa e opção de deixar pendente); **F05** (detalhe: origem, relógio do jogo, posição no arquivo, player, erro de mídia quando reproduzido, seleção e retorno); **F06** (obtenção: seleção vazia, diálogo, distinção CSV × MP4 e downloads); **Navegação transversal** (barra lateral, foco, teclado, contexto na sessão e recarga). |
| Fluxos e perguntas | Modelos `M01`, `M02` e `M03` ([Entrega 10](10_molic.md)), tarefas `T01`, continuidade de `T02` e `T03` ([Entrega 5](05_analise_tarefas.md)) e pergunta `QA10` ([Entrega 12](12_planejamento_avaliacao.md#b-perguntas-de-avaliação)). |
| Dispositivo e viewport | Computador desktop. Cada avaliador registra navegador, versão, largura da janela e meios de interação na própria seção. |
| Avaliadores | **A01:** Pedro Alexandre Custodio Silva (`22.123.049-3`); **A02:** Lucas Roberto Boccia dos Santos (`22.123.012-1`); **A03:** Giovanni Chahin Morassi (`22.123.025-3`). |

## Processo e fluxograma da avaliação heurística

O fluxo abaixo segue as cinco fases descritas por Barbosa e Silva (2010) e pelos materiais da disciplina: preparação em equipe, coleta de dados individual, interpretação individual, consolidação em reunião e relato dos resultados.

![Fluxograma do processo da avaliação heurística](../assets/13_heuristica/fluxograma_heuristica.svg)

*Figura 1. Fluxograma do processo de avaliação heurística da Equipe 16, destacando a separação para inspeção independente, os dois laços iterativos (verificação individual por tela/estado/heurística e reconferência durante a consolidação) e o ponto em que os três avaliadores se reúnem. Fonte: elaboração da equipe com base em Barbosa e Silva (2010) e [Avaliação de Usabilidade por Inspeções](../slides_plinio/Avaliacao%20Usabilidade%20Inspecoes.pdf) (slides 8, 15 e 16).*

As etapas ocorrem nesta ordem:

1. **Preparação (equipe reunida):** alinhar perfis (`P01` e `P03`), fluxos (`M01`–`M03`) e heurísticas (`H1`–`H10`), congelar a versão publicada (`ihc-11.p4cs.com.br`, commit `7405221`) e abrir uma ficha individual por integrante.
2. **Coleta de dados e interpretação (individual e independente):** cada avaliador percorre o fluxo normal uma vez para familiarização e depois entra no laço iterativo de inspeção. Para cada tela, estado e heurística, verifica se há violação, registra evidência com captura destacada, classifica severidade (`0`–`4`) com justificativa de frequência, impacto e persistência e propõe correção. O ciclo repete até fechar a matriz `H1`–`H10` sem discussão prévia entre integrantes.
3. **Consolidação dos resultados (reunião da equipe):** somente após `A01`, `A02` e `A03` concluírem suas fichas, os três se reúnem para agrupar violações equivalentes (`HC01...`) preservando a autoria original e calibrar severidade final, prioridade e responsável. Quando surge divergência sobre o comportamento de um estado, a equipe reinspeciona o protótipo em um segundo laço curto antes de fechar a classificação.
4. **Relato dos resultados e continuidade (equipe):** produzir a síntese por heurística e severidade, definir quais correções entram antes da [Entrega 14](14_observacao_usuario.md) e reunir os dez exemplos didáticos positivos na seção [Uso das heurísticas](#8-uso-das-heurísticas). Se o protótipo for alterado, a equipe registra o novo commit antes do piloto da Entrega 14.

## 3. Procedimento individual

Cada integrante preenche primeiro sua ficha independente, baseada em [entrega12_formulario_heuristica.md](../instrumentos/entrega12_formulario_heuristica.md), para evitar influência mútua e conflitos de edição:

- **A01 (Pedro):** [artifacts/entrega13/inspecao_A01_pedro.md](../artifacts/entrega13/inspecao_A01_pedro.md)
- **A02 (Lucas):** [artifacts/entrega13/inspecao_A02_lucas.md](../artifacts/entrega13/inspecao_A02_lucas.md)
- **A03 (Giovanni):** [artifacts/entrega13/inspecao_A03_giovanni.md](../artifacts/entrega13/inspecao_A03_giovanni.md)

Regras de execução individual:

1. Percorra os fluxos e telas ao menos uma vez para familiarização.
2. Inspecione novamente aplicando `H1`–`H10` a todas as telas e estados definidos no escopo.
3. Registre cada problema com ação, local, consequência e captura anotada destacando a região afetada em `assets/13_heuristica/` (`a01_v01.png`, `a02_v01.png`, `a03_v01.png`).
4. Atribua severidade somente depois de compreender o problema, justificando por **frequência**, **impacto** e **persistência**.
5. Não leia as fichas dos colegas nem discuta achados antes de encerrar a sua matriz de cobertura.

### Escala de severidade (0–4)

| Grau | Interpretação |
|---:|---|
| 0 | Não é considerado problema de usabilidade |
| 1 | Problema cosmético; corrigir se houver tempo |
| 2 | Problema menor; baixa prioridade |
| 3 | Problema maior; alta prioridade |
| 4 | Catástrofe de usabilidade; correção imperativa antes de disponibilizar |

---

## Avaliador A01: Pedro Alexandre Custodio Silva

**Autor:** Pedro Alexandre Custodio Silva — 22.123.049-3\
**Ficha de trabalho:** [inspecao_A01_pedro.md](../artifacts/entrega13/inspecao_A01_pedro.md)\
**Sessão:** data pendente · navegador pendente · viewport pendente · meios de interação pendentes\

### 4.1 Matriz de cobertura das 10 heurísticas (A01)

| Heurística | Telas e estados examinados | Houve violação? | IDs dos achados |
|---|---|---|---|
| H1 | *Pendente* | *Pendente* | |
| H2 | *Pendente* | *Pendente* | |
| H3 | *Pendente* | *Pendente* | |
| H4 | *Pendente* | *Pendente* | |
| H5 | *Pendente* | *Pendente* | |
| H6 | *Pendente* | *Pendente* | |
| H7 | *Pendente* | *Pendente* | |
| H8 | *Pendente* | *Pendente* | |
| H9 | *Pendente* | *Pendente* | |
| H10 | *Pendente* | *Pendente* | |

### 5.1 Declaração de violações (A01)

Seguir o [Modelo 02 da disciplina](../slides_plinio/Modelo%2002%20Avaliacao%20Heuristica.doc). Registrar apenas violações reais observadas, com captura destacando a região do problema, ação, efeito, severidade justificada e recomendação.

| ID | Heurística | Tela e estado | Problema observado | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---:|---|---|
| *Pendente* | | | *A preencher após inspeção individual de A01* | | | | |

---

## Avaliador A02: Lucas Roberto Boccia dos Santos

**Autor:** Lucas Roberto Boccia dos Santos — 22.123.012-1\
**Ficha de trabalho:** [inspecao_A02_lucas.md](../artifacts/entrega13/inspecao_A02_lucas.md)\
**Sessão:** data pendente · navegador pendente · viewport pendente · meios de interação pendentes\

### 4.2 Matriz de cobertura das 10 heurísticas (A02)

| Heurística | Telas e estados examinados | Houve violação? | IDs dos achados |
|---|---|---|---|
| H1 | *Pendente* | *Pendente* | |
| H2 | *Pendente* | *Pendente* | |
| H3 | *Pendente* | *Pendente* | |
| H4 | *Pendente* | *Pendente* | |
| H5 | *Pendente* | *Pendente* | |
| H6 | *Pendente* | *Pendente* | |
| H7 | *Pendente* | *Pendente* | |
| H8 | *Pendente* | *Pendente* | |
| H9 | *Pendente* | *Pendente* | |
| H10 | *Pendente* | *Pendente* | |

### 5.2 Declaração de violações (A02)

Seguir o [Modelo 02 da disciplina](../slides_plinio/Modelo%2002%20Avaliacao%20Heuristica.doc). Registrar apenas violações reais observadas, com captura destacando a região do problema, ação, efeito, severidade justificada e recomendação.

| ID | Heurística | Tela e estado | Problema observado | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---:|---|---|
| *Pendente* | | | *A preencher após inspeção individual de A02* | | | | |

---

## Avaliador A03: Giovanni Chahin Morassi

**Autor:** Giovanni Chahin Morassi — 22.123.025-3\
**Ficha de trabalho:** [inspecao_A03_giovanni.md](../artifacts/entrega13/inspecao_A03_giovanni.md)\
**Sessão:** data pendente · navegador pendente · viewport pendente · meios de interação pendentes\

### 4.3 Matriz de cobertura das 10 heurísticas (A03)

| Heurística | Telas e estados examinados | Houve violação? | IDs dos achados |
|---|---|---|---|
| H1 | *Pendente* | *Pendente* | |
| H2 | *Pendente* | *Pendente* | |
| H3 | *Pendente* | *Pendente* | |
| H4 | *Pendente* | *Pendente* | |
| H5 | *Pendente* | *Pendente* | |
| H6 | *Pendente* | *Pendente* | |
| H7 | *Pendente* | *Pendente* | |
| H8 | *Pendente* | *Pendente* | |
| H9 | *Pendente* | *Pendente* | |
| H10 | *Pendente* | *Pendente* | |

### 5.3 Declaração de violações (A03)

Seguir o [Modelo 02 da disciplina](../slides_plinio/Modelo%2002%20Avaliacao%20Heuristica.doc). Registrar apenas violações reais observadas, com captura destacando a região do problema, ação, efeito, severidade justificada e recomendação.

| ID | Heurística | Tela e estado | Problema observado | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---:|---|---|
| *Pendente* | | | *A preencher após inspeção individual de A03* | | | | |

---

## 6. Consolidação da equipe

*Pendente: preencher na reunião após a conclusão das inspeções individuais de A01, A02 e A03.*

Problemas iguais ou equivalentes encontrados por mais de um avaliador devem ser consolidados em um único ID (`HC01...`), preservando quem encontrou cada ocorrência (por exemplo, `V01(A01), V04(A02)`).

| ID consolidado | Achados individuais | Heurística | Tela e estado | Problema consolidado | Severidade final | Prioridade | Responsável pela correção |
|---|---|---|---|---|---:|---|---|
| *Pendente* | | | | *A preencher após consolidação coletiva* | | | |

## 7. Síntese e plano de melhoria

*Pendente: preencher após a consolidação da seção 6.*

### Distribuição consolidada por heurística e severidade

| Heurística | Sev. 0 | Sev. 1 | Sev. 2 | Sev. 3 | Sev. 4 | Total |
|---|---:|---:|---:|---:|---:|---:|
| H1 | 0 | 0 | 0 | 0 | 0 | 0 |
| H2 | 0 | 0 | 0 | 0 | 0 | 0 |
| H3 | 0 | 0 | 0 | 0 | 0 | 0 |
| H4 | 0 | 0 | 0 | 0 | 0 | 0 |
| H5 | 0 | 0 | 0 | 0 | 0 | 0 |
| H6 | 0 | 0 | 0 | 0 | 0 | 0 |
| H7 | 0 | 0 | 0 | 0 | 0 | 0 |
| H8 | 0 | 0 | 0 | 0 | 0 | 0 |
| H9 | 0 | 0 | 0 | 0 | 0 | 0 |
| H10 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **0** | **0** | **0** | **0** | **0** | **0** |

### Achados prioritários e encaminhamento para a Entrega 14

- **Problemas críticos ou graves (severidades 3 e 4):** *a consolidar após A01–A03.*
- **Padrões recorrentes entre telas:** *a consolidar após A01–A03.*
- **Decisão de versão para a Entrega 14:** *definir quais correções entram antes do piloto da Entrega 14; se o protótipo for atualizado, registrar o novo commit e a nova publicação conforme o [plano DECIDE](12_planejamento_avaliacao.md#c-escopo-e-participantes).*

## 8. Uso das heurísticas

*Pendente: preencher com a equipe após a conclusão das inspeções individuais para não influenciar a busca por violações.*

Reúna dez exemplos didáticos positivos no protótipo, um por heurística, com captura de tela salva em `assets/13_heuristica/` (`uso_h01.png` a `uso_h10.png`). Uma heurística com violação em um estado pode ser ilustrada por um caso que a atende em outro estado.

| Heurística | Tela e estado | Exemplo no protótipo | Evidência | Por que atende |
|---|---|---|---|---|
| H1 | | | | |
| H2 | | | | |
| H3 | | | | |
| H4 | | | | |
| H5 | | | | |
| H6 | | | | |
| H7 | | | | |
| H8 | | | | |
| H9 | | | | |
| H10 | | | | |

## Checklist

- [x] O fluxograma mostra a inspeção individual, a repetição das verificações e a consolidação da equipe.
- [ ] Cada integrante fez uma inspeção completa e identificada.
- [ ] Todas as telas/estados relevantes foram examinados.
- [ ] Estados administrativos, filtros, relatórios, históricos, processamento e erros foram incluídos quando existentes.
- [ ] A inspeção avaliou a interface/protótipo, não o mérito técnico do algoritmo/modelo.
- [ ] H1–H10 aparecem na matriz de cobertura de cada avaliador.
- [ ] Parte de violações contém apenas violações, sem “forçar” exemplos.
- [ ] Todo problema tem print/localização e contexto.
- [ ] Severidade possui justificativa, não apenas número.
- [ ] Recomendação resolve a causa ou reduz o impacto.
- [ ] Achados duplicados foram consolidados ao final.
- [ ] A seção Uso das heurísticas apresenta dez exemplos positivos com evidência, um por heurística.

## Referências

- BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador*. Rio de Janeiro: Elsevier, 2010. (Referenciada em [BIBLIOGRAFIA.md](../BIBLIOGRAFIA.md).)
- NIELSEN, Jakob. *10 Usability Heuristics for User Interface Design*. Nielsen Norman Group, 1994 (atualizado em 2024).
- Slides da disciplina: [Avaliação de Usabilidade por Inspeções](../slides_plinio/Avaliacao%20Usabilidade%20Inspecoes.pdf) (slides 8–16) e [Modelo 02 Avaliacao Heuristica.doc](../slides_plinio/Modelo%2002%20Avaliacao%20Heuristica.doc).
- Artefatos do projeto: [Entrega 11 — protótipo navegável](11_figma.md), [Entrega 12 — plano DECIDE](12_planejamento_avaliacao.md) e [formulário de inspeção heurística](../instrumentos/entrega12_formulario_heuristica.md).
