# Entrega 4 — Cenários de análise/problema

**Data:** {{dd/mm/aaaa}}  
**Status:** ⬜ não iniciada  
**Responsabilidade:** 1 solução completa por integrante

## Objetivo da atividade

Descrever situações atuais em que o usuário tenta alcançar um objetivo e encontra dificuldades. O cenário de análise/problema deve tornar visível **o contexto, os atores, as ações e as rupturas**, sem antecipar a interface que será projetada.

> **Regra central:** cenário de problema é a “história do problema”. Se o texto já diz “o sistema mostra”, “o aplicativo resolve” ou descreve botões/telas futuras, provavelmente está misturando problema com solução.

Sempre que possível, o cenário deve aprofundar uma **situação concreta já registrada na Entrega 1**.

### Quando o TCC não possuía interface

O cenário continua sendo uma história de **problema/atividade humana**, não uma história do futuro sistema. Descreva como o profissional realiza hoje uma atividade semelhante ou como lida atualmente com dados, resultados, configurações, logs, decisões e limitações que o tema do TCC pretende apoiar.

Exemplo: em vez de “o DBA abre o novo dashboard e executa o algoritmo”, descreva “o DBA precisa investigar uma consulta lenta, reúne informações em ferramentas distintas, compara planos manualmente e tem dificuldade para estimar o impacto de uma mudança”.

A interface da disciplina aparecerá somente depois, nos cenários de interação.

Se o integrante escolher um novo problema/situação, explique por que ele passou a ser relevante e indique a evidência que motivou sua inclusão.

## Cenário C02 — Controle do Processo Editorial Engessado

**Autor(a):** Lucas Roberto Boccia dos Santos, 22.123.012-1
**Persona(s) relacionada(s):** PO2
**Necessidade relacionada:** R02 - Manter o controle e supervisão sobre todo o processo editorial e trabalho dos editores  
**Situação concreta da Entrega 1 relacionada:** {{seção 4.4 / H01 / outra ou “nova situação justificada”}}  
**Hipóteses ainda presentes:** {{H01, H02 ou —}}

### 1. Cenário inicial

Arnaldo é editor-chefe de uma emissora esportiva e tem como dever supervisionar o trabalho dos editores e garantir a fluidez do processo editorial. Hoje, passa horas por dia andando pelas salas de edição, conversando com editores e tentando manter controle sobre o trabalho manual que todos estão desenvolvendo, tendo que chancelar decisões editoriais em meio a prazos e epxectativas de entrega, sendo o responsável maior pelo conteúdo final publicado.

### 2. Questões de refinamento

Use os tipos de questões/taxonomia definidos na aula. As perguntas devem revelar informações **ainda ausentes** do cenário, não repetir o que já foi respondido.

| Elemento | Questão que a premissa deixa em aberto | Resposta adotada para a narrativa e origem | Contexto | O que investigar com usuários |
|---|---|---|---|---|
| Ambiente/contexto | Em que condições Arnaldo precisa controlar o processo atual? | Um dia de trabalho com diversos editores trabalhando na edição de múltiplas partidas diferentes, muitas vezes não relacionadas entre si, percorrendo a sala de edição e olhando as diferentes telas para monitorar o que está sendo feito. | Contexto de P02. | Quantidade média de atividades acompanhadas simultaneamente, tipo de decisões a chancelar, condições reais de trabalho |
| Ator | A dificuldade decorre de falta de entendimento do processo? | Arnaldo é um editor-chefe experiente, que já atua na função há anos. A dificuldade é manter a atenção e coerência enquanto avalia diversos processos simultaneamente, com pouco tempo para chancelar decisões editoriais. | P02 | Experiência, como esse processo já evoluiu com o tempo e como a demanda cada vez maior tem o transformado |
| Objetivo | O que precisa estar pronto ao final desta atividade? | O conteúdo editado deve ter sido publicado na internet de acordo com as normas e preferências da emissora, processo chancelado pelo editor-chefe | PO2 | Critérios editoriais, processo de publicação. |
| Planejamento | Como pretende monitorar e auditorar o processo? | Acompanha o trabalho de vários editores ao mesmo tempo, está em contato constante com os mesmos e procura manter anotações das questões que considera de maior relevância, garantindo que o processo siga conforme o esperado e desejado pela emissora. | PO2 | Ordem efetiva, uso de anotações e tratamento de trechos duvidosos. |
| Ações | Como aprova e chancela (ou não) decisões? | Possui conhecimento pleno das normas, exigências e necessidades da emissora. Baseia suas decisões nestas e na sua experiência no ofício. Tem a palavra final sobre o trabalho produzido pelos editores. | PO2 | Quais fatores e situações costumam gerar a necessidade de intervenção por parte do editor-chefe. |
| Eventos | Que ocorrência torna o problema visível? | Na revisão de uma das últimas partidas do dia, a reprodução de um corte começa com a finalização e deixa de fora a construção da jogada. Episódio de H11 escolhido com o autor para tornar visível a queda de qualidade. | Ocorrência e frequência de cortes inadequados e como são percebidos. |
| Avaliação | Como Rafael interpreta o corte e decide o próximo passo? | Julga que falta contexto, volta ao original e amplia o trecho. Ao final, distingue a qualidade dos cortes revisados da dúvida sobre lances que podem ter passado despercebidos. Construção hipotética apoiada em H09/H10/H11. | Como confere a cobertura da partida e equilibra revisão, cansaço e prazo. |

### 3. Cenário refinado

Reescreva o cenário incorporando as respostas. Marque o conteúdo novo de forma consistente (por exemplo, `**[NOVO: ...]**`).

{{narrativa refinada}}

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | {{...}} |
| Objetivo(s) | {{...}} |
| Contexto | {{...}} |
| Recursos/informações | {{...}} |
| Ações | {{...}} |
| Problemas/rupturas | {{...}} |
| Consequências | {{...}} |

### 5. Implicações para as próximas entregas

Quais tarefas merecem análise? Quais informações precisam ser coletadas? **Não desenhe a solução ainda.**

> Repita para C02, C03... com autoria individual.

## Checklist

- [ ] Há um cenário completo por integrante.
- [ ] Cada cenário tem título, ator, objetivo, contexto e problema.
- [ ] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [ ] O texto descreve a situação atual, sem antecipar a solução.
- [ ] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”.
- [ ] Questões de refinamento acrescentam informação nova.
- [ ] O refinamento mostra claramente o que foi adicionado/alterado.
- [ ] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [ ] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.
