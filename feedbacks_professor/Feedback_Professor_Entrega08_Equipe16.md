# Feedback do Professor > Entrega 08 > Equipe 16

> **Status da aplicação (10/11/2026):** [F] revisão documental de `docs/08_engenharia_usabilidade.md`, entrega de grupo, aplicada com assistência de automação a pedido de Pedro, na branch `docs/apply-e08-feedback`. As anotações registram o que mudou no documento; não confirmam fatos novos. Não houve coleta, piloto nem avaliação com usuários nesta revisão. Pesos de prioridade e limites de MU07 e MU08 ficam como proposta a confirmar pela equipe. O texto original do professor foi preservado; as anotações aparecem em blocos de citação logo após cada item.
>
> | Item do parecer | Situação | Commit(s) |
> |---|---|---|
> | Registro do parecer | incluído sem alteração | [`31219bb`](https://github.com/p4cs-974/projeto-ihc/commit/31219bb) |
> | Correção 1: princípios de negócio e de interface | aplicada | [`d23f330`](https://github.com/p4cs-974/projeto-ihc/commit/d23f330) |
> | Correção 2: priorização pelas cinco metas de Nielsen | aplicada; pesos propostos aguardam confirmação da equipe | [`01811bf`](https://github.com/p4cs-974/projeto-ihc/commit/01811bf) |
> | Correção 3: ciclo de Mayhew | aplicada | [`f693bf0`](https://github.com/p4cs-974/projeto-ihc/commit/f693bf0) |
> | Correção 4: cobertura das metas pelos instrumentos | aplicada como plano; protocolo e instrumentos ficam para a Entrega 12; limites de MU07 e MU08 a confirmar | [`0743b4d`](https://github.com/p4cs-974/projeto-ihc/commit/0743b4d) |
> | Recomendações de melhoria | aplicadas em parte; referência MU/MQ na matriz central fica para a consolidação | [`534ceaa`](https://github.com/p4cs-974/projeto-ihc/commit/534ceaa) |
> | Pontos para as próximas entregas | encaminhados | [`f693bf0`](https://github.com/p4cs-974/projeto-ihc/commit/f693bf0), [`534ceaa`](https://github.com/p4cs-974/projeto-ihc/commit/534ceaa) |
> | Cabeçalho e histórico | registrados | [`e10a8f8`](https://github.com/p4cs-974/projeto-ihc/commit/e10a8f8) |
>
> \- Pedro

Vocês construíram uma entrega detalhada, com boa separação entre a contribuição técnica do TCC e aquilo que pode ser avaliado na interação. A descrição da plataforma apresenta capacidades e restrições concretas, e as metas estão relacionadas às tarefas e aos dois perfis de usuários primários. O cuidado para distinguir ajuda, sucesso independente e limitações da simulação é um ponto forte.

As seções do modelo foram preenchidas, mas três aspectos centrais ainda precisam de revisão: a organização dos princípios em dois grupos, a priorização pelas cinco metas de Nielsen e a explicação do ciclo adotado com base em um dos modelos estudados. O documento está avançado na definição de medidas, mas ainda não pode ser considerado completamente alinhado à atividade.

## Pontos positivos

- **Capacidades e restrições bem caracterizadas.** A seção 1 explica seleção de exemplos, acompanhamento, visualizações, CSV e MP4, além de ausência de upload real, execução do detector, montagem e histórico persistente. Também relaciona rede, dispositivos e interrupções às consequências para o usuário. A indicação de HTML, CSS e JavaScript é válida como característica da plataforma e está acompanhada de implicações de interação.
- **Limites do protótipo apresentados com clareza.** A equipe não trata resultados previamente anotados como detecção real nem usa o tempo da simulação como comprovação de produtividade. A separação evita atribuir ao usuário uma dificuldade causada por uma funcionalidade que não existe na demonstração.
- **Metas qualitativas específicas.** MQ01–MQ04 abordam entendimento do lote, continuidade, referências temporais e significado das saídas. São questões que podem orientar mudanças concretas de rótulos, mensagens e organização das telas.
- **Metas quantitativas ligadas a tarefas e públicos.** MU01–MU06 apresentam limites, procedimentos e justificativas. Conferir o conteúdo do CSV e reproduzir o MP4 salvo é mais informativo do que considerar apenas o clique no botão de download.
- **Tratamento cuidadoso das evidências.** Os resultados de P01 e P03 serão separados; participantes proxy não serão usados como validação dos perfis profissionais. A equipe reconhece que a sessão de U01 não fornece uma linha de base de desempenho.
- **Preparação para avaliações reproduzíveis.** As regras sobre ajuda, denominadores, esperas técnicas, condições iniciais e exposição prévia ao guia reduzem ambiguidades. Também é correto fixar os critérios antes do teste principal e registrar alterações posteriores.

## Correções prioritárias

### 1. Separar os princípios de negócio dos princípios de interface

Na seção 2, vocês reúnem normas, cuidados éticos, julgamento editorial e orientações de interface em uma única lista. Os conteúdos são pertinentes, mas a atividade pede dois grupos explícitos: **princípios direcionados ao negócio** e **princípios direcionados à interface**.

No primeiro grupo, explicitem as regras e restrições do domínio que governam o serviço, como a responsabilidade pela decisão editorial e os limites entre seleção, montagem e publicação. No segundo, organizem as orientações de interação, como visibilidade de estado, clareza das saídas, acessibilidade e consistência. Classifiquem as referências normativas pela finalidade que cumprem; a simples presença de uma ISO não transforma automaticamente um princípio de usabilidade em regra de negócio.

Preservem a ligação já existente entre princípio, contexto e decisão decorrente. A revisão deve mostrar o que orienta o funcionamento do serviço e o que orienta sua apresentação e operação pelo usuário, sem acrescentar normas apenas para preencher espaço.

> **✅ Como foi tratado** ([`d23f330`](https://github.com/p4cs-974/projeto-ihc/commit/d23f330)): a seção 2 tem agora a subseção 2.1, princípios direcionados ao negócio, PN01 a PN04: decisão editorial humana, limites entre seleção, montagem e publicação, origem rastreável dos candidatos e privacidade na coleta acadêmica, com a LGPD. A subseção 2.2, princípios direcionados à interface, reúne PI01 a PI06: usabilidade no contexto de uso, com a ISO 9241-11 classificada pela finalidade de orientar a avaliação, visibilidade de estado, clareza das saídas, consistência de termos e as duas linhas de WCAG. Cada linha mantém aplicabilidade, decisão decorrente e fonte. A única referência acrescentada é o material de aula de princípios e diretrizes, que fundamenta PI02 e PI04.
>
> \- Pedro

### 2. Refazer a priorização com as cinco metas de Nielsen

A seção 3.3 prioriza continuidade, compreensão e obtenção efetiva e depois confirma limites de eficácia, eficiência e satisfação. Essa organização é útil para discutir tarefas, mas não atende à estrutura de priorização solicitada na disciplina.

A priorização deve utilizar as cinco metas de Nielsen: **facilidade de aprendizado, facilidade de memorização, eficiência, baixa taxa de erro e satisfação positiva do usuário**. Continuidade, compreensão e obtenção são preocupações do projeto que precisam ser relacionadas a essas metas, em vez de ocuparem seu lugar.

Isso não significa descartar MU01–MU06. Eficácia e compreensão continuam sendo medidas úteis e compatíveis com o material de engenharia de usabilidade; o ajuste necessário é distinguir medidas operacionais da organização das prioridades. Por exemplo, concluir uma tarefa ao final não significa necessariamente ter cometido poucos erros durante sua execução.

Definam a importância relativa das cinco metas para o uso previsto e justifiquem as escolhas. A memorização merece discussão, especialmente diante das interrupções e da retomada mencionadas no projeto; ela não pode desaparecer apenas porque o protótipo ainda não preserva todos os estados. Se forem usados percentuais, eles devem somar 100% e representar prioridade, não desempenho atingido.

Retomem a videoaula sobre essas metas antes da revisão. Deixar de assistir às videoaulas não é uma prática recomendada: o preenchimento do modelo precisa incorporar também os critérios apresentados nas aulas. O documento atual demonstra a divergência conceitual, mas não permite concluir quais materiais cada integrante consultou.

> **✅ Como foi tratado** ([`01811bf`](https://github.com/p4cs-974/projeto-ihc/commit/01811bf)): a seção 3.3 prioriza pelas cinco metas de Nielsen, com pesos que somam 100%: aprendizado 30%, baixa taxa de erro 25%, memorização 15%, eficiência 15% e satisfação 15%. Cada meta tem justificativa, as preocupações do projeto relacionadas, como continuidade, compreensão e obtenção, e as medidas que a verificam. A memorização é ligada a H39 e H41. A seção explica que eficácia e compreensão são medidas operacionais e que concluir uma tarefa não demonstra poucos erros. Os pesos estão marcados `[H]` como proposta desta revisão e aguardam confirmação da equipe. Os conceitos foram conferidos no slide 4 de Qualidade de Uso e na página Usability 101 do Nielsen Norman Group. Esta anotação não afirma quais videoaulas ou leituras cada integrante consultou; isso fica para cada integrante declarar.
>
> \- Pedro

### 3. Explicar a iteração a partir de um modelo de ciclo de vida

A seção 4 apresenta um plano útil de revisão das entregas, com retorno às hipóteses, protótipos e avaliações. Entretanto, não identifica nem descreve um dos modelos de processo trabalhados no material de aula. Relacionar as próximas entregas não basta para explicar o modelo que organiza essas atividades.

Recomendo adotar explicitamente o **Ciclo de Vida de Engenharia de Usabilidade de Mayhew**, conforme estudado. Relacionem o trabalho existente à análise de requisitos — perfil do usuário, tarefas, plataforma, princípios e metas — e expliquem a passagem pelo projeto essencial/modelo conceitual, pelos padrões de telas e diálogos e pelo projeto detalhado. Mostrem como a avaliação determina avanço ou retorno, como as decisões alimentam o guia de estilo e como o feedback posterior pode originar uma nova iteração.

Não é necessário implementar agora todas essas etapas. É necessário explicar como elas orientarão o projeto. A tabela atual pode ser aproveitada, desde que fique claro a qual etapa cada atividade pertence e o que levará a equipe a revisar um nível anterior. Também evitem tratar os números das entregas como uma sequência que impede retornos.

> **✅ Como foi tratado** ([`f693bf0`](https://github.com/p4cs-974/projeto-ihc/commit/f693bf0)): a seção 4 adota o Ciclo de Vida de Engenharia de Usabilidade de Mayhew, com base nos slides de Processos, Partes 1 e 2. A seção 4.1 relaciona perfil, tarefas, plataforma, princípios, metas e guia de estilo à análise de requisitos e situa o trabalho nos níveis de projeto essencial, padrões de telas e diálogos, projeto detalhado e instalação. A seção 4.2 aproveita a tabela anterior com a etapa de cada atividade. A seção 4.3 define critérios de avanço e de retorno ao nível de origem do problema, grupos de funcionalidades e registro das decisões. O texto declara que os números das entregas não impedem retornos e que ainda não há documento próprio de guia de estilo, marcado `[?]`.
>
> \- Pedro

### 4. Tornar explícita a cobertura das prioridades pelos instrumentos de avaliação

O questionário I02 publicado no guia registra dificuldade, realização declarada das tarefas, preferência de visualização e expectativa de download. Ele pode trazer informações úteis, mas não mede sozinho as metas desta entrega. A resposta “Consegui” não substitui a conferência de conclusão sem ajuda, e a preferência por uma visualização não demonstra compreensão dos metadados.

MU06 prevê uma escala de 1 a 5 sobre facilidade percebida, que não corresponde às alternativas de G03 nem à pergunta geral G07 do formulário atual. O documento já prevê preparação de instrumentos na Entrega 12; explicitem, portanto, que essa escala ainda deverá ser incorporada ao protocolo correspondente. Não convertam retrospectivamente as respostas atuais para essa escala.

A facilidade percebida é um indicador pertinente, mas representa apenas parte da experiência de satisfação. Esclareçam esse alcance e considerem uma pergunta complementar sobre a experiência geral, caso ela seja necessária à decisão de design.

Ao reorganizar as prioridades de Nielsen, indiquem também como verificar aprendizado, erros e memorização. O documento define o que é erro de operação, mas ainda não estabelece uma meta própria de baixa taxa de erro. A memorização exigirá uma condição de retorno após algum intervalo; repetir imediatamente uma tarefa mede outra situação. Planejem essas verificações de modo proporcional ao projeto, sem antecipar sua execução nesta entrega.

> **✅ Como foi tratado** ([`0743b4d`](https://github.com/p4cs-974/projeto-ihc/commit/0743b4d)): a seção 3.4 indica, para cada meta de Nielsen, as medidas, o instrumento necessário, o que o I02 atual oferece e a lacuna a resolver na Entrega 12. O texto declara que G03 não substitui a conferência de sucesso independente e que G05 não demonstra compreensão. MU06 registra que a escala ainda deve ser incorporada ao protocolo da Entrega 12, e as regras proíbem converter G03, G07 ou outras respostas atuais. A facilidade percebida fica delimitada como parte da satisfação, com uma pergunta geral complementar sem limite de aceitação. MU07 dá meta própria à baixa taxa de erro. MU08 verifica memorização em sessão de retorno após pelo menos sete dias, com a regra de registrar como não avaliada se não houver retorno. Os limites de MU07 e MU08 são proposta `[H]` a confirmar pela equipe. Nenhuma verificação foi executada.
>
> \- Pedro

## Recomendações de melhoria

- **Preservar o caráter provisório dos limites.** O alvo de 100% em uma pequena amostra e o tempo de 90 segundos são critérios definidos pela equipe, não resultados obtidos. A justificativa inicial está explícita; no piloto, verifiquem se esses valores distinguem dificuldades relevantes e registrem qualquer alteração antes da avaliação principal.

  > **✅ Como foi tratado** ([`534ceaa`](https://github.com/p4cs-974/projeto-ihc/commit/534ceaa)): a seção 3.2 diz que os limites são critérios definidos pela equipe, não resultados obtidos, e que o piloto da Entrega 12 deve verificar se 100% e 90 s distinguem dificuldades relevantes, registrando alterações antes da avaliação principal. MU07 e MU08 seguem a mesma regra.
  >
  > \- Pedro
- **Interpretar o tempo com o contexto.** É útil separar espera técnica de esforço de interação, mas mantenham também o tempo total da experiência. Um resultado rápido após descontos não elimina o impacto da espera percebida pelo usuário.

  > **✅ Como foi tratado** ([`534ceaa`](https://github.com/p4cs-974/projeto-ihc/commit/534ceaa)): MU05 e a regra de tempo exigem relatar a mediana do tempo total ao lado da ajustada e registrar comentários sobre a espera. O texto diz que um tempo ajustado baixo não elimina o impacto da espera percebida.
  >
  > \- Pedro
- **Evitar ensinar aquilo que será avaliado.** A orientação de adaptar o guia está correta. Conservem a separação entre informações necessárias para consentimento e contexto e explicações que revelam navegação, significado dos tempos ou caminhos de download.

  > **✅ Como foi tratado** ([`534ceaa`](https://github.com/p4cs-974/projeto-ihc/commit/534ceaa)): a orientação sobre o guia adaptado da Entrega 12 separa as informações de consentimento e contexto das explicações sobre navegação, significado dos tempos e caminhos de download.
  >
  > \- Pedro
- **Consolidar as referências de rastreabilidade.** A Entrega 08 relaciona várias metas a tarefas e hipóteses, mas a matriz central ainda não explicita os IDs MU/MQ. Acrescentem uma referência à especificação dessas metas, sem registrá-las como resultados alcançados.

  > **🟨 Tratado em parte**: esta revisão não alterou `RASTREABILIDADE.md`. A inclusão da referência a MQ01–MQ04 e MU01–MU08 na matriz central, como especificação e não como resultado, fica para a consolidação da equipe e está como item aberto no checklist da Entrega 8.
  >
  > \- Pedro
- **Atualizar status e checklist após as correções.** A confirmação interna dos números encerra uma decisão da equipe, mas não resolve a organização dos princípios, das prioridades e do ciclo. O status “completa” deve acompanhar a revisão desses pontos.

  > **✅ Como foi tratado** ([`534ceaa`](https://github.com/p4cs-974/projeto-ihc/commit/534ceaa), [`e10a8f8`](https://github.com/p4cs-974/projeto-ihc/commit/e10a8f8)): o status passou a 🟨 revisada após o parecer, com pesos, MU07 e MU08 a confirmar. O checklist inclui os novos itens e deixa abertos a confirmação desses valores e a referência na matriz. O cabeçalho e o histórico registram a revisão de 10/11/2026.
  >
  > \- Pedro

## Pontos que devem alimentar as próximas entregas

Na Entrega 12, detalhem amostra, gabaritos, condições de aplicação, tempo máximo de sessão e instrumentos de registro. Na inspeção e nos testes posteriores, mantenham separados os achados sobre acessibilidade, compreensão, desempenho e satisfação. Um tipo de evidência não substitui automaticamente os demais.

Preservem como questões futuras o comportamento com mais de oito candidatos, a recuperação de falhas, a retomada após recarga e a necessidade de histórico. As metas atuais são válidas para o recorte demonstrado, mas não permitem concluir que esses outros cenários estão resolvidos. Também mantenham P02 como continuidade editorial externa enquanto não houver evidência que justifique outra decisão de escopo.

> **ℹ️ Encaminhamento** ([`f693bf0`](https://github.com/p4cs-974/projeto-ihc/commit/f693bf0), [`534ceaa`](https://github.com/p4cs-974/projeto-ihc/commit/534ceaa)): a seção 3.4 lista o que a Entrega 12 precisa preparar, como folha de registro, gabaritos, cronometragem, agenda de retorno e perguntas de satisfação; amostra e tempo máximo de sessão continuam com a Entrega 12. A seção 4 mantém separados achados de inspeção e de observação, conserva como questões futuras mais de oito candidatos, recuperação de falhas, retomada após recarga e histórico, e mantém P02 como continuidade editorial externa.
>
> \- Pedro

## Síntese das ações recomendadas

1. Organizar os princípios nos grupos de negócio e interface.
2. Priorizar pelas cinco metas de Nielsen e relacioná-las às medidas do projeto.
3. Explicar o ciclo adotado, suas etapas, critérios de retorno e registro das decisões.
4. Identificar os instrumentos necessários para verificar cada meta, incluindo a escala de MU06.
5. Atualizar a rastreabilidade, o checklist e o status da entrega.

> **Situação:** as ações 1 a 4 foram aplicadas em `docs/08_engenharia_usabilidade.md`, com pesos e limites de MU07 e MU08 como proposta a confirmar pela equipe. Na ação 5, checklist e status foram atualizados; a referência MU/MQ em `RASTREABILIDADE.md` fica para a consolidação. Nenhuma coleta, piloto ou revalidação ocorreu nesta revisão.
>
> \- Pedro

De forma geral, considero que vocês avançaram bastante na especificação de metas verificáveis e no cuidado com a interpretação dos resultados. A entrega apresenta uma boa base para avaliar a interface sem confundir simulação com desempenho real do sistema. Para concluí-la adequadamente, é preciso ligar essa qualidade operacional à estrutura conceitual da disciplina: princípios organizados, prioridades de Nielsen justificadas e ciclo de engenharia de usabilidade explicitamente aplicado ao projeto.
