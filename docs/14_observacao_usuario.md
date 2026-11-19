# Entrega 14 — Avaliação de usabilidade por observação de usuários

**Data:** {{dd/mm/aaaa}}  
**Status:** ⬜ não iniciada  
**Responsabilidade:** solução consolidada por equipe. O número de participantes finais observados deve ser igual ao número de integrantes, conforme o modelo da disciplina; recomenda-se que cada integrante seja responsável por conduzir/analisar ao menos um participante.

## Objetivo da atividade

Observar usuários representativos realizando tarefas reais ou realisticamente simuladas para identificar problemas de eficácia, eficiência, compreensão e satisfação que não podem ser inferidos apenas por inspeção.

> **Participantes finais não devem ser membros da equipe.** Um integrante pode participar do teste piloto apenas para validar roteiro/equipamentos, sem contar na amostra final.

### Quando o usuário é um perfil profissional especializado

Em TCCs técnicos, o público pode ser DBA, analista, pesquisador, administrador, técnico ou outro especialista. Priorize participantes que possuam relação real com as tarefas. Se não for possível recrutar o perfil ideal, qualquer participante aproximado/proxy deve ser **justificado previamente e tratado como limitação**; não apresente o resultado como equivalente ao de especialistas reais.

O teste avalia a **interação com o protótipo**. Não é necessário que o participante valide o desempenho científico do algoritmo. Resultados simulados podem ser usados quando declarados e coerentes com a tarefa.

Tarefas podem envolver, por exemplo, interpretar um dashboard, configurar uma análise, encontrar uma execução no histórico usando filtros, comparar resultados, gerar relatório, revisar alerta ou administrar permissões.

## A. Fluxograma do processo — equipe

[Arquivo reservado para o fluxograma](../assets/14_testes/fluxograma_avaliacao.svg).

Represente o planejamento, a preparação técnica, o piloto e seus ajustes, o recrutamento, o consentimento, a sessão remota com observação e pós-teste, a interpretação, a consolidação e o relato dos resultados. Mostre como a equipe trata falhas de conexão e sessões reagendadas.

## B. Procedimento de preparação e execução — equipe

### Passo 1 — Objetivos e versão avaliada

**Versão/commit/Figma:** {{...}}  
**Metas de usabilidade relacionadas:** {{MU01...}}

### Passo 2 — Participantes

| ID | Perfil | Critérios que justificam participação | Integrante responsável |
|---|---|---|---|
| U01 | {{sem nome real}} | {{...}} | {{...}} |

### Passo 3 — Consentimento e privacidade

- [Termo de consentimento](../instrumentos/entrega12_consentimento.md) e registro privado do aceite.
- Registre se a pessoa autorizou a gravação da aba para conferência das notas e se também autorizou o uso de trechos desidentificados no vídeo ilustrativo.
- Forma de anonimização: IDs `U01`, `U02`...
- Local e período de armazenamento: {{...}}

### Passo 4 — Teste piloto

**Data:** {{...}}  
**O que foi validado:** roteiro, duração, entendimento das instruções, protótipo, gravação.  
**Mudanças após piloto:** {{...}}

### Passo 5 — Tarefas

| ID | Cenário/instrução apresentada | Critério de sucesso | Métricas | Ligação com modelo |
|---|---|---|---|---|
| UT01 | {{“Você precisa...” sem dizer o controle}} | {{resultado observável}} | sucesso, tempo, erros e ajudas | {{T01/M01/F01}} |

### Passo 6 — Protocolo do moderador

1. Receber participante e explicar que **o produto está sendo avaliado, não a pessoa**.
2. Obter consentimento.
3. Aplicar perfil pré-teste mínimo necessário.
4. Ler instruções padronizadas.
5. Observar sem ensinar o caminho; registrar pedidos de ajuda separadamente.
6. Se usar *think aloud*, explicar e aplicar de forma consistente.
7. Após UT02, UT05 e UT06, aplicar a pergunta de facilidade percebida de 1 a 5 e registrar o motivo, inclusive após falha ou conclusão com ajuda. Usar essas três tarefas no cálculo de MU06. [Questionário pós-tarefa](../instrumentos/entrega12_questionarios.md#pós-tarefa).
8. Fazer pós-teste/entrevista breve.
9. Encerrar e explicar uso dos dados.

### Recomendações de Felipe Melo adotadas

Registre quais recomendações foram aplicadas e como funcionaram nas sessões. O [roteiro de observação](../instrumentos/entrega12_roteiro_observacao.md#preparar-a-sessão) prevê instruções prévias, teste do ambiente com 15 minutos de antecedência, sala alternativa e canal de contato para retomar ou reagendar.

## C. Resultados — por participante

### U01 — {{perfil resumido}}

| Tarefa | Grau de sucesso | Erros | Tipos de erro/dificuldade | Ajudas | Tempo | Satisfação | Evidência/observação |
|---|---|---:|---|---:|---|---|---|
| UT01 | total/parcial/falha | {{n}} | {{...}} | {{n}} | {{mm:ss}} | não se aplica | {{fala/comportamento}} |

**Registro da sessão:** {{anotações ou gravação interna autorizada}}\
**Resposta pós-teste:** {{...}}

> Repita para U02, U03...

## D. Consolidação por tarefa e perfil

Use uma linha por tarefa e perfil. Em `n/N`, informe o número de sucessos independentes sobre o total de tentativas avaliáveis. Apresente os registros de participantes proxy à parte.

| Tarefa | Perfil | Sucesso independente (n/N e %) | Tempo típico | Erros recorrentes | Satisfação | Meta atendida? | Problemas prioritários |
|---|---|---:|---|---|---|---|---|
| UT01 | {{P01 ou P03}} | {{n/N e %}} | {{...}} | {{...}} | não se aplica | {{sim, não ou não avaliada}} | {{...}} |

## E. Achados e recomendações

| ID | Achado | Evidência (quant. + qual.) | Impacto | Recomendação | Artefatos a revisar |
|---|---|---|---|---|---|
| AU01 | {{...}} | {{n/N falharam, com fala ou ação desidentificada}} | {{...}} | {{...}} | {{MoLIC/Figma/signos...}} |

### Vídeo ilustrativo do teste e dos resultados

Inclua o link do vídeo no relatório com acesso restrito à equipe e ao docente. Mostre como o teste foi conduzido e apresente resultados desidentificados e melhorias propostas. Use trechos da aba com autorização específica e mantenha as gravações brutas no armazenamento privado da equipe. Quando não houver trechos autorizados, use a demonstração reencenada se o docente aprovar esse formato e identifique-a no vídeo.

**Link do vídeo ilustrativo:** {{link restrito}}

## F. Comparação com a avaliação heurística

| Problema | Detectado na heurística? | Detectado por usuários? | O que aprendemos |
|---|---|---|---|
| {{...}} | sim/não | sim/não | {{...}} |

## G. Conclusão

A conclusão deve responder:

1. Quais metas de usabilidade foram atingidas?
2. Quais problemas foram recorrentes e com quais perfis/tarefas?
3. O que surpreendeu a equipe?
4. Quais mudanças são prioritárias?
5. Que limitações do teste impedem generalizações amplas?

## Checklist

- [ ] Número de participantes finais atende ao enunciado.
- [ ] Participantes são representativos do público e não são membros da equipe.
- [ ] Se foram usados participantes proxy, a justificativa e a limitação estão explícitas.
- [ ] O teste avalia a interação; não confunde usabilidade do protótipo com desempenho técnico do TCC.
- [ ] Tarefas administrativas/analíticas usadas no teste são rastreáveis a objetivos e cenários.
- [ ] Há consentimento e anonimização.
- [ ] Foi realizado teste piloto.
- [ ] O fluxograma representa o piloto, a observação, a análise e o relato.
- [ ] O relatório registra as recomendações de teste remoto que foram adotadas.
- [ ] Tarefas têm critérios de sucesso definidos antes do teste.
- [ ] Moderadores não ensinaram o caminho durante a tarefa.
- [ ] Resultados estão separados por usuário e por tarefa.
- [ ] Foram registrados sucesso, erros, ajudas, tempo e satisfação quando aplicáveis.
- [ ] Conclusão combina evidência quantitativa e qualitativa.
- [ ] Achados geram recomendações e atualização da rastreabilidade.
- [ ] O vídeo ilustrativo tem link de acesso restrito no relatório. Os trechos de sessões incluídos têm autorização específica.
