# Resumo da branch `lab-5-pedro`: Entrega 5 (Análise de tarefas)

**Última atualização:** 09/10/2026  
**Base:** `main` (após o merge da PR #13)  
**Documento principal:** [docs/05_analise_tarefas.md](docs/05_analise_tarefas.md)

Este arquivo registra o que foi feito nesta branch até agora, para orientar a revisão. Não substitui o histórico de revisões da Entrega 5 nem o da matriz de rastreabilidade.

## Situação das tarefas

| Tarefa | Autor | Situação |
|---|---|---|
| T01: Obter, revisar e selecionar lances de melhores momentos (P01, C01) | Pedro Alexandre Custódio Silva — 22.123.049-3 | HTA, GOMS e CTT concluídos; aguarda revisão |
| T02: Supervisionar processo editorial e chancelar cortes esportivos (P02, C02) | Lucas Roberto Boccia dos Santos — 22.123.012-1 | HTA, GOMS e CTT concluídos |
| T03 (P03, C03) | Giovanni Chahin Morassi — 22.123.025-3 | Pendente; nome da tarefa em branco na tabela de seleção |

## Commits da branch

| Commit | Autor | O que fez |
|---|---|---|
| `ebe92b5` | Lucas | Início do lab 05: T02 completa (HTA, GOMS e CTT), tabela de seleção das tarefas, diagramas `hta_t02.svg` e `ctt_t02.svg`, R03 atualizada e relatório de coerência de 07/10/2026 |
| `fdc3650` | Lucas | Deixou em branco a descrição da T03 na tabela de seleção |
| `db5c852` | Pedro | T01 a partir do C01: HTA do trabalho atual, GOMS com o método atual (M1) e o proposto (M2), CTT do uso proposto (A04), síntese, checklist e R01. Corrigiu a matrícula de Pedro na tabela |
| `7cc44df` | Pedro | T01 renomeada e ampliada para incluir o envio das partidas e o acompanhamento do processamento (A01 e A02), com o caminho de falha. CTT dividida em duas figuras. R02 passa a apontar para T01 |
| `755a89c` | Pedro | T01 alinhada aos slides da disciplina (CC8122, HTA e GOMS/CTT): notação dos planos, uso de `METHOD`, estimativa GOMS-KLM e tipos de tarefa da CTT |

## T01 em detalhe

**O que cada modelo representa.** O C01 pede que cada modelo declare se descreve o trabalho atual ou o uso proposto:

- **HTA:** trabalho atual narrado em C01, sem a interface. Objetivos 1 a 5: organizar o dia, localizar e separar candidatos, revisar os cortes, entregar a seleção e atender a pergunta da supervisão e retomar. Os planos usam a notação dos slides (`>` sequencial, `/` seleção); repetição e interrupção estão descritas em texto. Diagrama: `assets/05_tarefas/hta_t01.svg`.
- **GOMS:** compara os dois. GOAL 3 tem os métodos M1 (percorrer a gravação no editor) e M2 (revisar os cortes gerados). As metas de enviar as partidas, acompanhar o processamento e tratar falhas só existem no uso proposto. `METHOD` só aparece onde há alternativas, cada uma com sua regra de seleção (SR1 a SR4). Inclui uma comparação qualitativa entre M1 e M2 e uma estimativa GOMS-KLM do tratamento de um candidato: de 3,7 s a 5,0 s em M2, contra 10,8 s em M1, sem contar o tempo de reprodução. O ganho esperado de M2 está na busca, que o KLM não modela.
- **CTT:** uso proposto (A01, A02 e A04), em duas figuras. A Figura 2a (`ctt_t01.svg`) mostra o envio, o processamento em concorrência com o tratamento de cada partida e o caminho de falha (reenviar ou selecionar manualmente). A Figura 2b (`ctt_t01_revisao.svg`) mostra a revisão de uma partida concluída: prévia com margem, manter ou excluir, suspensão e retomada pela pergunta da supervisão, conferência de cobertura, download e entrega. As tarefas realizadas fora do sistema (chat, pasta do servidor, editor externo) são tarefas do usuário, conforme a definição dos slides.

**Principais implicações registradas na síntese** (todas são hipóteses a validar, não requisitos confirmados):

1. A contribuição do TCC troca a busca na gravação pela revisão de cortes, mas não elimina o julgamento editorial de Rafael.
2. A margem antes e depois do lance é condição para revisar o corte. Isso vale também para Arnaldo em T02.
3. A omissão muda de lugar: sai dos trechos avançados e passa para os lances que o modelo não detecta. A conferência de cobertura não tem apoio do sistema em nenhum modelo; fica como questão para a Entrega 7.
4. A revisão precisa ser retomada no ponto em que parou depois de uma interrupção (H41).
5. Obter os lances passa a depender do processamento: validar arquivos, mostrar o estado por partida, avisar a conclusão e explicar falhas sem bloquear as outras partidas (H16, H26, H32).
6. Tarefas candidatas para o teste: enviar as partidas e lidar com a falha de uma; revisar uma partida com um corte sem construção e uma interrupção no meio.

## Outros arquivos alterados

- **[RASTREABILIDADE.md](RASTREABILIDADE.md):** R01 e R02 apontam para T01; R03 aponta para T02. O cenário de problema de R02 continua PENDENTE, porque C01 não narra o envio. O histórico registra cada etapa.
- **Tabela de seleção e síntese da Entrega 5:** a síntese foi dividida por tarefa (T01 e T02), com uma seção de pontos comuns. O checklist mantém desmarcado "cada integrante produziu HTA, GOMS e CTT" enquanto a T03 estiver pendente.
- **Figuras:** as figuras de T02 foram renumeradas para 3 e 4, porque as de T01 vêm antes no documento.

## Pendências

- **T03:** modelagem de Giovanni, incluindo o nome da tarefa na tabela de seleção.
- **T02 em relação aos slides (Lucas):** a T02 tem divergências que foram corrigidas na T01 e não foram alteradas aqui:
  - tarefas realizadas fora do sistema estão classificadas como interativas;
  - aparece "habilitação" em vez de "ativação";
  - a tabela de operadores CTT usa `|||` sem escape dentro da tabela Markdown, o que pode quebrar as colunas no GitHub.
- **Decisões abertas na T01:**
  - onde fica a nota de ajuste do M-CORR-2;
  - se o tratamento de arquivo recusado na validação deve aparecer na CTT (hoje está só no GOMS).
- **Análise de coerência:** não foi gerado relatório de coerência para as mudanças de Pedro.
