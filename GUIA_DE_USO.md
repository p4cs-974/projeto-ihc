# Guia de uso, formatação e apresentação

Este guia existe para evitar que o repositório seja apenas um conjunto de respostas soltas. O GitHub deve funcionar como **documentação técnica e acadêmica navegável**, permitindo compreender o raciocínio de projeto e verificar as evidências.

## 0. Regra pedagógica: tema do TCC não é o mesmo que escopo de IHC

A disciplina usa o **tema do TCC** como domínio para os exercícios. Isso não significa que todo TCC deva ter uma interface como entrega formal.

Quando o TCC já possui interface prevista, a disciplina pode trabalhar diretamente sobre ela. Quando o TCC não possui interface prevista, a equipe deve construir um **recorte de interação plausível** para fins de aprendizagem. Esse recorte deve partir da contribuição técnica e de pessoas que poderiam configurá-la, operá-la, interpretar seus resultados, administrá-la ou se beneficiar dela.

A interface produzida na disciplina pode ser:

- parte já prevista no TCC;
- uma extensão conceitual;
- um protótipo demonstrativo;
- uma hipótese de produto futuro;
- uma forma de demonstrar aplicação e potencial de mercado/INOVA.

Ela **não precisa ser implementada no TCC**, salvo decisão posterior da equipe e do orientador.

Antes da Entrega 1, leia [GUIA_ESCOPO_IHC.md](GUIA_ESCOPO_IHC.md).

### 0.1 Como derivar uma interface sem inventar telas arbitrárias

Use a cadeia:

**contribuição do TCC → usuário plausível → objetivo → tarefa → contexto → necessidade de interação → interface**.

Exemplos de necessidades que podem emergir:

- acompanhar resultados em um **dashboard**;
- configurar parâmetros técnicos por uma **tela de administração/configuração**;
- consultar **relatórios** e exportar evidências;
- recuperar execuções em um **histórico com busca, ordenação e filtros**;
- comparar algoritmos, modelos, versões ou períodos;
- administrar **usuários, papéis e permissões**;
- realizar CRUD de entidades quando isso fizer parte de uma tarefa real do domínio;
- acompanhar processamento, filas, falhas e reexecuções;
- revisar resultados produzidos por IA e registrar correções;
- consultar logs/auditoria em linguagem adequada ao perfil.

Esses padrões são **possibilidades**, não requisitos. Não crie login, dashboard, CRUD ou filtros apenas para aumentar o número de telas. Cada elemento deve responder a uma necessidade rastreável.

## 1. Padrão de cada entrega

Cada arquivo em `docs/` segue, sempre que aplicável, esta estrutura:

1. **Identificação da entrega** — data, status, autores e escopo.
2. **Objetivo da atividade** — o que o método de IHC pretende descobrir/modelar/avaliar.
3. **Entradas** — quais entregas anteriores fundamentam esta etapa.
4. **Produção** — artefatos, tabelas, diagramas e análise.
5. **Síntese** — o que a equipe aprendeu e que decisão de design decorre da atividade.
6. **Rastreabilidade** — ligação explícita com artefatos anteriores e próximos.
7. **Checklist de qualidade** — revisão antes de concluir.
8. **Referências** — fontes acadêmicas e fontes externas efetivamente utilizadas.

## 2. Identificação de autoria

Entregas individuais devem conter a linha:

`**Autor(a):** Nome completo — matrícula`

Quando houver consolidação, não apague as contribuições individuais. Mostre **quem produziu cada artefato** e depois apresente a síntese da equipe.

## 3. Imagens, diagramas e prints

- Não use imagem minúscula ou ilegível.
- Coloque **legenda** e explique no texto por que a figura é relevante.
- Prefira arquivos locais do repositório a links temporários de anexos externos.
- Nomeie arquivos de forma estável: `hta_buscar_produto.png`, `molic_realizar_saque.png`, `heuristica_h3_tela_pagamento.png`.
- Para diagramas, mantenha **duas versões quando possível**:
  - versão renderizada (`.png` ou `.svg`) para leitura no GitHub;
  - fonte editável (`.drawio`, `.fig`, etc.) para manutenção.
- Em prints de concorrentes e protótipos, não recorte tanto a ponto de perder o contexto da tela.
- Não inclua dados pessoais reais sem necessidade e autorização.

Exemplo:

```md
![HTA — realizar transferência](assets/05_tarefas/hta_transferencia.svg)

*Figura 1 — HTA da tarefa “realizar transferência”. Fonte: elaboração da equipe.*
```

## 4. Tabelas

Use tabelas para **comparar** e **estruturar**, não para esconder textos muito longos. Quando uma célula virar um parágrafo extenso, considere criar subseções e deixar na tabela apenas a síntese.

Toda tabela comparativa deve ter critérios claros. Evite colunas vagas como “bom/ruim” sem justificativa.

## 5. Escrita acadêmica e objetividade

- Defina termos técnicos na primeira ocorrência.
- Distingua **dado**, **interpretação** e **decisão de projeto**.
- Não apresente suposições sobre usuários como fatos. Indique a origem: entrevista, questionário, literatura, análise de concorrência ou hipótese a validar.
- Evite frases genéricas (“a interface deve ser intuitiva”). Diga **para quem**, **em qual tarefa** e **como será verificado**.
- Use a terminologia do método corretamente. Ex.: MoLIC não é um fluxograma de telas; avaliação heurística não substitui teste com usuários.

### 5.1 Fato, hipótese e lacuna de conhecimento

Na primeira entrega, e sempre que ainda houver incerteza relevante, use a convenção:

- **[F] Fato conhecido:** há fonte ou evidência identificável.
- **[H] Hipótese:** afirmação plausível que ainda precisa ser investigada.
- **[?] Não sabemos:** lacuna importante para uma decisão posterior.

Não transforme uma hipótese em fato apenas porque ela parece intuitiva para a equipe. Hipóteses relevantes devem receber IDs (`H01`, `H02`...) e ser acompanhadas na [Matriz de rastreabilidade](RASTREABILIDADE.md). Quando uma entrega posterior produzir evidência, atualize o estado da hipótese como **sustentada, refutada ou refinada**, preservando o histórico.

> Exemplo: `[H] H01 — usuários preferem realizar a atividade pelo celular.` Isso só pode virar fato quando a equipe indicar uma evidência compatível com essa afirmação.

## 6. Referências

Ao usar uma fonte externa, informe pelo menos: autor/organização, título, ano (quando disponível), link e data de acesso quando pertinente. Referências acadêmicas centrais estão em [BIBLIOGRAFIA.md](BIBLIOGRAFIA.md).

Não confunda “fonte da imagem” com “referência conceitual”. Uma captura de um concorrente precisa indicar o produto e a data; uma definição de método deve ter referência bibliográfica.

## 7. Links externos

Links para Figma, Forms, vídeos e planilhas devem:

- estar com permissão de visualização adequada;
- ser testados em janela anônima antes da entrega;
- ter uma evidência local mínima no GitHub (print, tabela ou resumo), para que a correção não dependa exclusivamente do link externo.

## 8. Consistência entre entregas

Antes de concluir qualquer etapa, responda:

- As hipóteses e lacunas levantadas na Entrega 1 continuam abertas, foram sustentadas ou foram refutadas por alguma evidência?
- O **escopo de IHC** continua coerente com a contribuição do TCC e com o usuário escolhido, ou alguma evidência justificou sua revisão?
- O público desta entrega é o mesmo inicialmente levantado ou a mudança foi justificada por novas evidências?
- Os objetivos das personas aparecem nos cenários?
- As tarefas analisadas são relevantes para os cenários?
- O modelo conceitual utiliza os mesmos signos e objetivos?
- O MoLIC representa os mesmos objetivos e caminhos?
- O Figma implementa os fluxos do MoLIC?
- As avaliações cobrem justamente esses fluxos/telas?

Use [RASTREABILIDADE.md](RASTREABILIDADE.md) para registrar essas relações.

## 9. Erros frequentes que este template procura evitar

- confundir o escopo formal do TCC com o escopo pedagógico de IHC;
- concluir que “não há projeto de IHC” apenas porque o TCC não previa interface;
- inventar uma interface genérica (login + dashboard + CRUD) sem derivá-la de usuário, objetivo e contexto;
- iniciar o projeto descrevendo tecnologia antes de compreender usuário, objetivo, problema e contexto;
- tratar “não existe um aplicativo” como problema do usuário, sem descrever a dificuldade real que existe hoje;
- apresentar suposições sobre preferências, comportamentos ou dificuldades como fatos;
- confundir objetivo do projeto (“desenvolver um sistema”) com objetivo do usuário (“conseguir realizar X”);
- quantidade de artefatos menor que o número exigido de integrantes;
- ausência do nome do autor em entregas individuais;
- personas genéricas, estereotipadas ou sem relação com dados/evidências;
- cenários de problema que já descrevem a solução;
- HTA, GOMS e CTT usados como desenhos decorativos sem explicação;
- MoLIC reduzido a sequência de telas, sem conversação, alternativas e rupturas;
- Figma sem correspondência com os modelos anteriores;
- avaliação heurística que aplica apenas algumas heurísticas ou só às telas “principais”;
- problemas heurísticos sem print/localização, justificativa de severidade ou solução;
- teste com usuários sem perfil, consentimento, critérios de sucesso, tempos/erros ou evidência;
- conclusão que apenas diz “foi fácil”, sem consolidar achados e mudanças necessárias;
- dependência de links inacessíveis, sem conteúdo equivalente documentado no repositório.

## 10. Estado da entrega

Use um dos estados no topo do arquivo:

- `⬜ não iniciada`
- `🟨 em andamento`
- `🟩 concluída`
- `🟦 revisada após feedback`

Ao revisar após feedback, adicione uma seção **Histórico de revisões** indicando o que mudou.
