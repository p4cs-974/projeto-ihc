# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** {{dd/mm/aaaa}}  
**Status:** ⬜ não iniciada  
**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Planejar a avaliação antes de executá-la, ligando perguntas de avaliação a métodos, participantes, tarefas, métricas, aspectos práticos, ética e forma de análise.

## O que está sendo avaliado

Em projetos cuja interface foi criada ou ampliada para a disciplina, o plano deve declarar explicitamente que a avaliação investiga **a qualidade da interação/protótipo**, não a validade científica ou o desempenho técnico do algoritmo/modelo do TCC.

Exemplos de perguntas:

- o DBA consegue localizar e comparar duas execuções?
- o analista entende o significado de um indicador?
- o administrador consegue alterar uma permissão sem risco de erro não percebido?
- o usuário compreende que o processamento está em andamento e consegue recuperar-se de uma falha?
- os filtros ajudam a localizar o histórico relevante?
- um relatório permite identificar a informação necessária para a decisão?

Se o protótipo utiliza dados ou resultados simulados, documente isso no plano.

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | Quais objetivos da avaliação? Relacione às metas de usabilidade da Entrega 8. |
| **E — Explore the questions** | Quais perguntas específicas a avaliação deve responder? |
| **C — Choose the evaluation paradigm and techniques** | Quais métodos serão usados e por quê? Ex.: inspeção heurística + observação de usuários. |
| **I — Identify the practical issues** | Participantes, recrutamento, ambiente, equipamentos, piloto, cronograma, responsáveis, riscos técnicos. |
| **D — Decide how to deal with ethical issues** | Consentimento, privacidade, gravação, anonimização, interrupção, dados sensíveis. |
| **E — Evaluate, interpret and present the data** | Como dados quantitativos/qualitativos serão consolidados, comparados às metas e apresentados. |

## B. Perguntas de avaliação

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | {{usuários completam T01 sem ajuda?}} | observação | sucesso, ajuda, erro | {{MU01}} |
| QA02 | {{há problemas de feedback?}} | heurística | violações H1 | {{...}} |

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | {{...}} |
| Critérios de inclusão/exclusão | {{...}} |
| Nº de participantes | {{...}} |
| Ambiente | presencial/remoto/campo/laboratório |
| Dispositivo | {{...}} |
| Protótipo/versão | {{...}} |
| Teste piloto | {{quem, quando, o que validar}} |

## D. Lista de tarefas de avaliação

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 | {{...}} | {{T01/O01}} | {{...}} | {{...}} |

> Uma boa instrução descreve o objetivo do participante sem dizer **onde clicar** ou usar o rótulo exato do controle que está sendo testado.

## E. Instrumentos

- [Modelo de termo de consentimento](../instrumentos/termo_consentimento_modelo.md)
- [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md)
- [Planilha de observação](../instrumentos/planilha_observacao_modelo.md)
- [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md)
- {{questionário pré/pós-teste}}

## F. Plano de análise

Defina antes dos testes:

- sucesso total / parcial / falha;
- o que conta como erro, dúvida, ajuda e abandono;
- como tempo será medido;
- escala de satisfação pós-tarefa;
- como observações/falas serão codificadas;
- como problemas serão priorizados;
- como comparar resultados às metas de usabilidade.

## Checklist

- [ ] As seis etapas DECIDE foram contextualizadas, não apenas expandidas por sigla.
- [ ] Perguntas de avaliação têm método e evidência correspondentes.
- [ ] O plano distingue avaliação de IHC de avaliação técnica/científica do TCC.
- [ ] Dados ou processamentos simulados no protótipo estão declarados.
- [ ] Tarefas vêm de objetivos/cenários relevantes.
- [ ] Critérios de sucesso foram definidos antes da coleta.
- [ ] Questões práticas e éticas estão resolvidas.
- [ ] Instrumentos estão prontos antes da Entrega 13/14.
- [ ] Plano diz como dados serão analisados e apresentados.
