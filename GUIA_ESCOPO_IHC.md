# Guia para definir o escopo de IHC a partir do tema do TCC

## Por que a disciplina usa o tema do TCC?

A disciplina de Interação Humano-Computador (IHC) utiliza **preferencialmente o tema do TCC em andamento** como domínio para os exercícios semanais. A intenção é evitar um projeto artificial criado apenas para a disciplina e permitir que a equipe aplique métodos de IHC sobre um problema que já conhece e considera relevante.

Isso não significa que a disciplina altera automaticamente o escopo formal do TCC.

> **Regra central:** o tema do TCC é o ponto de partida da disciplina; o **escopo de IHC** é o recorte de interação usado para exercitar os métodos da disciplina. A interface projetada em IHC pode inspirar, complementar ou demonstrar o potencial do TCC, mas **não precisa se tornar uma obrigação de implementação ou um resultado formal do TCC**, salvo decisão da própria equipe em conjunto com o orientador.

## Três coisas que não devem ser confundidas

| Elemento | O que significa |
|---|---|
| **Tema do TCC** | problema, tecnologia, algoritmo, pesquisa, sistema ou domínio investigado no trabalho de conclusão |
| **Escopo formal do TCC** | aquilo que a equipe e o orientador realmente se comprometeram a pesquisar, implementar e avaliar no TCC |
| **Escopo de IHC da disciplina** | situação de uso e interface definidas para aplicar conceitos de usuários, tarefas, interação, prototipação e avaliação |

A equipe deve registrar essa distinção na Entrega 1.

---

## Dois caminhos possíveis

### Caminho A — o TCC já prevê uma interface

Quando o TCC já prevê aplicativo, sistema Web, desktop, interface móvel, painel, sistema interativo ou outro produto com interação humana, a equipe pode utilizar essa própria interface como objeto da disciplina.

A disciplina ajudará a investigar e amadurecer:

- quem realmente são os usuários;
- objetivos e necessidades;
- contexto de uso;
- tarefas;
- problemas e rupturas;
- modelo conceitual;
- fluxos de interação;
- protótipos;
- usabilidade e acessibilidade;
- avaliação por inspeção e com usuários.

Nesse caminho, o projeto de IHC pode contribuir diretamente para o TCC, embora as decisões sobre incorporação ao TCC continuem sendo da equipe e do orientador.

### Caminho B — o TCC não prevê uma interface

Alguns TCCs têm como resultado principal:

- algoritmo;
- biblioteca;
- API;
- técnica de otimização;
- modelo de aprendizado de máquina;
- LLM ou método associado;
- análise de datasets;
- benchmark;
- método de classificação;
- infraestrutura de software;
- protocolo;
- estudo experimental;
- arquitetura de backend;
- ferramenta de linha de comando;
- componente embarcado;
- processamento científico.

Nesses casos, **não é necessário mudar o escopo formal do TCC**. Para a disciplina, a equipe deverá imaginar um cenário plausível no qual a contribuição técnica possa ser usada por pessoas.

A pergunta deixa de ser:

> “O TCC possui uma interface?”

E passa a ser:

> **“Se o resultado deste TCC estivesse disponível para uso real, quem obteria valor dele, o que essa pessoa precisaria fazer e como poderia ocorrer essa interação?”**

---

## Raciocínio recomendado para TCCs sem interface prevista

Use esta sequência antes de pensar em telas:

**contribuição técnica → aplicação possível → usuário ou profissional interessado → objetivo humano → atividades → contexto → necessidades de interação → interface**

Evite a sequência inversa:

**“precisamos de telas” → login → dashboard → CRUD → tentar justificar depois**.

### Passo 1 — Qual capacidade o TCC produz?

Complete:

> “Nosso TCC produz, melhora, analisa ou permite `{{capacidade técnica}}`.”

Exemplos:

- otimizar consultas em banco de dados;
- classificar imagens;
- gerar ou resumir textos;
- detectar anomalias;
- comparar modelos;
- identificar padrões em dados;
- prever demanda;
- analisar desempenho;
- melhorar alocação de recursos;
- recomendar configurações;
- executar simulações.

### Passo 2 — Quem teria interesse nessa capacidade?

Pense além de “usuário final”. Perfis possíveis incluem:

- administradores de banco de dados (DBAs);
- analistas de dados;
- cientistas de dados;
- engenheiros de IA/ML;
- desenvolvedores;
- administradores de sistemas;
- profissionais de segurança;
- técnicos de manutenção;
- pesquisadores;
- gestores;
- operadores;
- auditores;
- especialistas do domínio;
- atendentes;
- professores;
- profissionais de saúde;
- clientes finais;
- responsáveis por configuração e governança.

### Passo 3 — O que essa pessoa precisa conseguir fazer?

Pergunte por **objetivos**, não por telas.

Exemplos:

- configurar parâmetros;
- fornecer ou selecionar dados de entrada;
- iniciar uma execução;
- acompanhar processamento;
- identificar falhas;
- comparar resultados;
- interpretar métricas;
- compreender uma recomendação;
- aceitar, rejeitar ou ajustar uma sugestão;
- localizar execuções anteriores;
- gerar um relatório;
- exportar evidências;
- compartilhar resultados;
- gerenciar permissões;
- consultar histórico;
- auditar alterações.

### Passo 4 — Em qual contexto isso acontece?

Investigue:

- local de uso;
- dispositivo;
- frequência;
- nível de experiência;
- pressão de tempo;
- privacidade;
- criticidade de erros;
- colaboração;
- necessidade de aprovação;
- volume de dados;
- disponibilidade de conexão;
- regras organizacionais;
- necessidade de rastreabilidade/auditoria.

### Passo 5 — Qual recorte é adequado para a disciplina?

Não é necessário criar “um sistema completo”. Escolha um conjunto coerente de objetivos que permita exercitar IHC ao longo do semestre.

Uma boa formulação é:

> **Para fins da disciplina de IHC, será projetada uma interface que permita a `{{perfil de usuário}}` utilizar `{{capacidade ou resultado do TCC}}` para `{{objetivo do usuário}}`, no contexto de `{{situação de uso}}`.**

Exemplo:

> Para fins da disciplina de IHC, será projetada uma interface que permita a DBAs analisar recomendações produzidas pelo algoritmo de otimização de consultas, comparar alternativas e acompanhar o histórico de execuções em um ambiente de administração de banco de dados.

---

## O “teste de comercialização” como exercício de reflexão

Quando a equipe disser que o trabalho “é somente código”, “é somente um modelo” ou “é apenas uma análise”, aplique este exercício mental:

> **Imagine que o TCC foi concluído com sucesso e uma empresa decidiu transformar a contribuição em um produto ou serviço. Quem pagaria, administraria, configuraria, operaria, interpretaria ou se beneficiaria desse resultado?**

Em seguida, pergunte:

1. quem é o cliente ou organização interessada?
2. quem é o usuário direto?
3. quem administra a solução?
4. quem interpreta os resultados?
5. quem toma decisões a partir deles?
6. quais dados entram?
7. quais resultados precisam ser entendidos?
8. que erros ou dúvidas podem ocorrer?
9. que histórico ou rastreabilidade pode ser necessário?
10. como uma pessoa saberia que a tecnologia gerou valor?

Esse exercício **não obriga o TCC a virar produto comercial**. Ele serve para revelar situações de uso plausíveis e o potencial de transferência da contribuição técnica.

---

# Catálogo de possibilidades de interface

As opções abaixo são **inspirações**, não uma lista obrigatória. Só inclua uma tela ou funcionalidade quando ela apoiar um objetivo real do usuário e puder ser justificada pelas entregas anteriores.

## 1. Dashboard / visão geral

Útil quando o usuário precisa acompanhar muitos resultados, estados ou indicadores.

Pode incluir:

- métricas principais;
- comparações;
- tendências;
- alertas;
- itens recentes;
- tarefas pendentes;
- saúde do sistema;
- indicadores de desempenho;
- atalhos para ações frequentes.

**Pergunta de IHC:** qual decisão o usuário consegue tomar a partir desse dashboard?

## 2. Tela de configuração ou parametrização

Útil quando a contribuição técnica depende de opções, limites, modelos, fontes de dados ou políticas.

Pode incluir:

- escolha de algoritmo/modelo;
- parâmetros avançados;
- limites e thresholds;
- configuração de fonte de dados;
- políticas de execução;
- agendamento;
- presets/perfis de configuração;
- validação antes da execução.

**Cuidado:** não exponha parâmetros técnicos desnecessários ao usuário. A interface deve traduzir complexidade quando possível.

## 3. Entrada, seleção ou preparação de dados

Possibilidades:

- upload de arquivo;
- escolha de dataset;
- seleção de tabelas/colunas;
- conexão com banco/API;
- pré-visualização;
- validação dos dados;
- correção de inconsistências;
- explicação de formato esperado.

## 4. Execução e acompanhamento de processamento

Útil para algoritmos demorados, pipelines, treinamento de modelos ou tarefas assíncronas.

Pode incluir:

- iniciar/cancelar execução;
- status;
- progresso;
- tempo estimado;
- fila;
- logs compreensíveis;
- aviso de falha;
- recuperação/reexecução.

## 5. Relatórios e resultados

Pode apresentar:

- resultado principal;
- indicadores;
- tabelas;
- gráficos;
- interpretação;
- evidências;
- limitações;
- recomendações;
- exportação PDF/CSV;
- compartilhamento.

**Pergunta de IHC:** o usuário consegue compreender o significado do resultado, ou apenas vê números produzidos pelo algoritmo?

## 6. Histórico com busca, filtros e ordenação

Muito útil para trabalhos em que diferentes execuções, experimentos, consultas ou análises precisam ser revisitados.

Pode incluir filtros por:

- data;
- usuário;
- dataset;
- status;
- modelo;
- versão;
- projeto;
- severidade;
- tipo de resultado;
- faixa de métricas.

Pode permitir:

- abrir detalhes;
- comparar execuções;
- repetir operação;
- exportar;
- arquivar;
- identificar quem realizou uma alteração.

## 7. Comparação de resultados

Especialmente apropriada para TCCs experimentais.

Exemplos:

- algoritmo A × algoritmo B;
- configuração anterior × nova;
- modelo 1 × modelo 2;
- antes × depois;
- execução atual × baseline;
- diferentes datasets.

A interface pode destacar **diferenças relevantes**, não apenas colocar duas tabelas lado a lado.

## 8. Detalhamento e explicabilidade

Para IA, recomendadores, classificadores e sistemas de decisão, pode ser importante mostrar:

- confiança;
- fatores considerados;
- evidências de suporte;
- limitações;
- motivo de uma recomendação;
- possibilidade de contestação/correção;
- origem dos dados;
- versão do modelo.

## 9. Telas administrativas

Podem fazer sentido quando existe operação institucional ou governança.

Exemplos:

- cadastro e edição de usuários;
- perfis de acesso;
- papéis e permissões;
- grupos/equipes;
- fontes de dados;
- parâmetros globais;
- integração com serviços;
- políticas de retenção;
- auditoria;
- gestão de filas/processos.

### CRUD de perfis de usuário

Um CRUD (`Create`, `Read`, `Update`, `Delete`) pode ser adequado quando há necessidade real de administrar pessoas, papéis ou entidades do domínio.

Exemplo de fluxo plausível:

> administrador localiza um usuário → consulta papel atual → altera permissão → sistema alerta impacto → administrador confirma → alteração fica registrada no histórico.

**Não use CRUD apenas para aumentar o número de telas.** O valor de IHC está na tarefa, nas decisões, no feedback, na prevenção de erros e na recuperação — não nos quatro verbos do CRUD.

## 10. Auditoria, logs e histórico de alterações

Pode ser importante para:

- segurança;
- administração;
- pesquisa reproduzível;
- sistemas críticos;
- rastreabilidade de modelos/dados;
- conformidade.

O desafio de IHC é transformar logs técnicos em informação útil para o perfil que precisa interpretá-los.

## 11. Alertas e central de ocorrências

Possibilidades:

- falha de processamento;
- degradação de desempenho;
- dado inconsistente;
- anomalia;
- risco detectado;
- tarefa aguardando aprovação.

A interface deve explicar **o que ocorreu, impacto e ação possível**.

## 12. Ajuda, documentação e onboarding

Pode ser relevante para ferramentas profissionais complexas:

- explicação contextual;
- exemplos;
- glossário;
- documentação de parâmetros;
- tutorial inicial;
- ajuda associada à tarefa.

---

# Exemplos de derivação do escopo de IHC

## Exemplo A — algoritmo de otimização de banco de dados

**TCC:** algoritmo que otimiza consultas considerando a estrutura de armazenamento.

**Interface prevista originalmente no TCC:** não.

**Possíveis usuários:** DBA, engenheiro de dados, administrador de infraestrutura.

**Objetivos possíveis:**

- identificar consultas de baixo desempenho;
- executar análise;
- compreender recomendação;
- comparar custo/desempenho;
- decidir se aplica uma estratégia;
- acompanhar histórico.

**Possíveis telas:**

- dashboard de desempenho;
- lista de consultas com filtros;
- detalhe de consulta;
- comparação “plano atual × recomendado”;
- configuração de análise;
- histórico de execuções;
- relatório exportável.

**Escopo de IHC possível:** interface de apoio ao DBA para analisar e interpretar recomendações de otimização.

## Exemplo B — desenvolvimento ou estudo de LLM

**TCC:** técnica de ajuste, avaliação ou uso de LLM.

**Possíveis usuários:** engenheiro de IA, pesquisador, administrador da solução, especialista do domínio.

**Possíveis objetivos:**

- selecionar versão/modelo;
- configurar experimento;
- escolher dataset;
- executar avaliação;
- comparar respostas/métricas;
- localizar execuções anteriores;
- aprovar uma versão.

**Possíveis telas:**

- configuração de experimento;
- painel de execuções;
- comparação de modelos;
- relatório de métricas;
- análise de casos de erro;
- histórico com filtros;
- administração de datasets/modelos.

## Exemplo C — análise de dataset

**TCC:** análise de evasão, mobilidade, saúde, mercado, educação ou outro domínio.

**Possíveis usuários:** analista, gestor, pesquisador, especialista de domínio.

**Objetivos:**

- explorar resultados;
- filtrar grupos;
- comparar períodos;
- localizar padrões;
- compreender fatores associados;
- gerar relatório para tomada de decisão.

**Possíveis telas:**

- dashboard;
- filtros;
- visualizações exploratórias;
- detalhamento;
- comparação;
- relatório e exportação;
- histórico de análises.

## Exemplo D — modelo de visão computacional

**Possíveis usuários:** operador, analista de qualidade, técnico, especialista.

**Possíveis interações:**

- enviar lote de imagens;
- acompanhar processamento;
- revisar classificações;
- verificar confiança;
- corrigir rótulo;
- encaminhar caso duvidoso;
- consultar histórico.

## Exemplo E — backend/API

**Possíveis usuários:** desenvolvedores clientes, administradores e equipes de operação.

**Possíveis telas:**

- portal de chaves/credenciais;
- documentação interativa;
- dashboard de consumo;
- limites/quota;
- saúde do serviço;
- logs de requisição;
- filtros por status/endpoint;
- gestão de usuários e permissões.

## Exemplo F — cibersegurança

**Possíveis usuários:** analista de SOC, administrador, auditor.

**Possíveis interações:**

- triagem de alertas;
- filtro por criticidade;
- visualização de evidências;
- classificação de ocorrência;
- atribuição a responsável;
- histórico e auditoria;
- configuração de limiares.

## Exemplo G — simulação científica

**Possíveis usuários:** pesquisador, engenheiro ou analista.

**Possíveis interações:**

- definir parâmetros;
- executar simulação;
- acompanhar fila;
- visualizar resultado;
- comparar cenários;
- reproduzir experimento;
- exportar dados.

---

# Como escolher entre várias possibilidades

Se a contribuição técnica permitir muitas interfaces, escolha o recorte usando estes critérios:

| Critério | Pergunta |
|---|---|
| Relevância humana | Existe um usuário plausível com um objetivo real? |
| Relação com o TCC | A interface utiliza de forma clara a capacidade central do tema? |
| Potencial de IHC | Há tarefas, decisões, erros, feedback e alternativas de interação interessantes? |
| Escopo | É possível prototipar e avaliar durante a disciplina? |
| Evidência | É possível encontrar usuários, especialistas ou fontes para investigar hipóteses? |
| Demonstração | O recorte ajuda a explicar o valor do projeto para pessoas externas? |

Prefira um **recorte pequeno e coerente** a um produto enorme e superficial.

---

# Relação com a INOVA e potencial extensionista

Pensar no usuário também melhora a capacidade de comunicar o projeto fora do contexto técnico.

Uma explicação exclusivamente tecnológica costuma seguir esta forma:

> “Implementamos a técnica X com o método Y e melhoramos a métrica Z.”

A reflexão de IHC permite acrescentar:

> “Este é o problema enfrentado por determinado público. Nossa contribuição técnica pode apoiar essa atividade. Este protótipo demonstra como uma pessoa poderia utilizar os resultados.”

A narrativa passa a conectar:

**problema humano → contribuição computacional → forma de uso → impacto potencial**.

Isso pode facilitar:

- apresentação na INOVA;
- comunicação com público não especializado;
- demonstração do potencial de mercado;
- identificação de clientes e stakeholders;
- discussão de impacto social/extensionista;
- reflexão sobre transferência de tecnologia.

A interface construída na disciplina pode funcionar como **protótipo demonstrativo do potencial de aplicação**, ainda que não seja implementada ou incorporada ao TCC.

---

# Erros de interpretação a evitar

## “Meu TCC não tem interface, então preciso inventar um aplicativo qualquer.”

Não. Primeiro derive usuário, objetivo e contexto a partir da contribuição técnica.

## “Todo projeto precisa ter login, dashboard e CRUD.”

Não. Esses são padrões possíveis. Só devem existir quando uma tarefa os justificar.

## “Se fizemos a interface na disciplina, teremos de implementá-la no TCC.”

Não necessariamente. O protótipo é uma entrega da disciplina. A incorporação ao TCC depende do escopo acordado com o orientador.

## “O usuário do algoritmo é o computador.”

Para IHC, procure as pessoas que configuram, operam, interpretam, supervisionam, decidem ou se beneficiam do sistema no contexto considerado.

## “Nosso usuário é qualquer pessoa.”

Esse nível de generalidade impede decisões de design. Identifique um perfil plausível e um contexto específico.

## “Vamos fazer uma tela para mostrar os números do algoritmo.”

Pergunte primeiro: **que decisão ou atividade esses números apoiam?** A visualização deve responder à tarefa do usuário.

---

# Modelo de declaração do escopo de IHC

Preencha ao final da Entrega 1:

**Tema do TCC:** {{...}}

**Escopo formal do TCC:** {{...}}

**O TCC já previa interface?** sim / não / parcialmente

**Capacidade/contribuição central do TCC:** {{...}}

**Usuário escolhido para o projeto de IHC:** {{...}}

**Objetivo principal desse usuário:** {{...}}

**Contexto de uso considerado:** {{...}}

**Interface que será explorada na disciplina:** {{...}}

**Relação entre a interface de IHC e o TCC:** {{parte já prevista / extensão conceitual / protótipo demonstrativo / outra}}

**Compromisso com o TCC:**

> A interface desenvolvida nesta disciplina é um artefato de aprendizagem de IHC baseado no tema do TCC. Sua inclusão ou implementação no TCC somente ocorrerá se isso for posteriormente decidido pela equipe e pelo orientador.

---

# Regra final

A equipe não deve tentar provar, na primeira semana, que a interface imaginada é a melhor solução. O objetivo é construir um **recorte plausível de interação** e registrar as hipóteses que precisarão ser investigadas durante o semestre.

O projeto de IHC deve evoluir por evidências:

**hipótese inicial → investigação → modelagem → prototipação → avaliação → revisão**.
