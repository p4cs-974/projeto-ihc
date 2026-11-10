# Feedback do Professor > Entrega 08 > Equipe 16

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

### 2. Refazer a priorização com as cinco metas de Nielsen

A seção 3.3 prioriza continuidade, compreensão e obtenção efetiva e depois confirma limites de eficácia, eficiência e satisfação. Essa organização é útil para discutir tarefas, mas não atende à estrutura de priorização solicitada na disciplina.

A priorização deve utilizar as cinco metas de Nielsen: **facilidade de aprendizado, facilidade de memorização, eficiência, baixa taxa de erro e satisfação positiva do usuário**. Continuidade, compreensão e obtenção são preocupações do projeto que precisam ser relacionadas a essas metas, em vez de ocuparem seu lugar.

Isso não significa descartar MU01–MU06. Eficácia e compreensão continuam sendo medidas úteis e compatíveis com o material de engenharia de usabilidade; o ajuste necessário é distinguir medidas operacionais da organização das prioridades. Por exemplo, concluir uma tarefa ao final não significa necessariamente ter cometido poucos erros durante sua execução.

Definam a importância relativa das cinco metas para o uso previsto e justifiquem as escolhas. A memorização merece discussão, especialmente diante das interrupções e da retomada mencionadas no projeto; ela não pode desaparecer apenas porque o protótipo ainda não preserva todos os estados. Se forem usados percentuais, eles devem somar 100% e representar prioridade, não desempenho atingido.

Retomem a videoaula sobre essas metas antes da revisão. Deixar de assistir às videoaulas não é uma prática recomendada: o preenchimento do modelo precisa incorporar também os critérios apresentados nas aulas. O documento atual demonstra a divergência conceitual, mas não permite concluir quais materiais cada integrante consultou.

### 3. Explicar a iteração a partir de um modelo de ciclo de vida

A seção 4 apresenta um plano útil de revisão das entregas, com retorno às hipóteses, protótipos e avaliações. Entretanto, não identifica nem descreve um dos modelos de processo trabalhados no material de aula. Relacionar as próximas entregas não basta para explicar o modelo que organiza essas atividades.

Recomendo adotar explicitamente o **Ciclo de Vida de Engenharia de Usabilidade de Mayhew**, conforme estudado. Relacionem o trabalho existente à análise de requisitos — perfil do usuário, tarefas, plataforma, princípios e metas — e expliquem a passagem pelo projeto essencial/modelo conceitual, pelos padrões de telas e diálogos e pelo projeto detalhado. Mostrem como a avaliação determina avanço ou retorno, como as decisões alimentam o guia de estilo e como o feedback posterior pode originar uma nova iteração.

Não é necessário implementar agora todas essas etapas. É necessário explicar como elas orientarão o projeto. A tabela atual pode ser aproveitada, desde que fique claro a qual etapa cada atividade pertence e o que levará a equipe a revisar um nível anterior. Também evitem tratar os números das entregas como uma sequência que impede retornos.

### 4. Tornar explícita a cobertura das prioridades pelos instrumentos de avaliação

O questionário I02 publicado no guia registra dificuldade, realização declarada das tarefas, preferência de visualização e expectativa de download. Ele pode trazer informações úteis, mas não mede sozinho as metas desta entrega. A resposta “Consegui” não substitui a conferência de conclusão sem ajuda, e a preferência por uma visualização não demonstra compreensão dos metadados.

MU06 prevê uma escala de 1 a 5 sobre facilidade percebida, que não corresponde às alternativas de G03 nem à pergunta geral G07 do formulário atual. O documento já prevê preparação de instrumentos na Entrega 12; explicitem, portanto, que essa escala ainda deverá ser incorporada ao protocolo correspondente. Não convertam retrospectivamente as respostas atuais para essa escala.

A facilidade percebida é um indicador pertinente, mas representa apenas parte da experiência de satisfação. Esclareçam esse alcance e considerem uma pergunta complementar sobre a experiência geral, caso ela seja necessária à decisão de design.

Ao reorganizar as prioridades de Nielsen, indiquem também como verificar aprendizado, erros e memorização. O documento define o que é erro de operação, mas ainda não estabelece uma meta própria de baixa taxa de erro. A memorização exigirá uma condição de retorno após algum intervalo; repetir imediatamente uma tarefa mede outra situação. Planejem essas verificações de modo proporcional ao projeto, sem antecipar sua execução nesta entrega.

## Recomendações de melhoria

- **Preservar o caráter provisório dos limites.** O alvo de 100% em uma pequena amostra e o tempo de 90 segundos são critérios definidos pela equipe, não resultados obtidos. A justificativa inicial está explícita; no piloto, verifiquem se esses valores distinguem dificuldades relevantes e registrem qualquer alteração antes da avaliação principal.
- **Interpretar o tempo com o contexto.** É útil separar espera técnica de esforço de interação, mas mantenham também o tempo total da experiência. Um resultado rápido após descontos não elimina o impacto da espera percebida pelo usuário.
- **Evitar ensinar aquilo que será avaliado.** A orientação de adaptar o guia está correta. Conservem a separação entre informações necessárias para consentimento e contexto e explicações que revelam navegação, significado dos tempos ou caminhos de download.
- **Consolidar as referências de rastreabilidade.** A Entrega 08 relaciona várias metas a tarefas e hipóteses, mas a matriz central ainda não explicita os IDs MU/MQ. Acrescentem uma referência à especificação dessas metas, sem registrá-las como resultados alcançados.
- **Atualizar status e checklist após as correções.** A confirmação interna dos números encerra uma decisão da equipe, mas não resolve a organização dos princípios, das prioridades e do ciclo. O status “completa” deve acompanhar a revisão desses pontos.

## Pontos que devem alimentar as próximas entregas

Na Entrega 12, detalhem amostra, gabaritos, condições de aplicação, tempo máximo de sessão e instrumentos de registro. Na inspeção e nos testes posteriores, mantenham separados os achados sobre acessibilidade, compreensão, desempenho e satisfação. Um tipo de evidência não substitui automaticamente os demais.

Preservem como questões futuras o comportamento com mais de oito candidatos, a recuperação de falhas, a retomada após recarga e a necessidade de histórico. As metas atuais são válidas para o recorte demonstrado, mas não permitem concluir que esses outros cenários estão resolvidos. Também mantenham P02 como continuidade editorial externa enquanto não houver evidência que justifique outra decisão de escopo.

## Síntese das ações recomendadas

1. Organizar os princípios nos grupos de negócio e interface.
2. Priorizar pelas cinco metas de Nielsen e relacioná-las às medidas do projeto.
3. Explicar o ciclo adotado, suas etapas, critérios de retorno e registro das decisões.
4. Identificar os instrumentos necessários para verificar cada meta, incluindo a escala de MU06.
5. Atualizar a rastreabilidade, o checklist e o status da entrega.

De forma geral, considero que vocês avançaram bastante na especificação de metas verificáveis e no cuidado com a interpretação dos resultados. A entrega apresenta uma boa base para avaliar a interface sem confundir simulação com desempenho real do sistema. Para concluí-la adequadamente, é preciso ligar essa qualidade operacional à estrutura conceitual da disciplina: princípios organizados, prioridades de Nielsen justificadas e ciclo de engenharia de usabilidade explicitamente aplicado ao projeto.
