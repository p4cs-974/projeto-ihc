# Feedback do Professor > Entrega 09 > Equipe 16

A equipe entregou três cenários de interação, cada um associado a um integrante e ao respectivo cenário de problema, três recortes de design centrado na comunicação, um mapa consolidado de objetivos e um esquema conceitual único de signos. A quantidade mínima foi atendida.

Os cenários apresentam boa continuidade com as entregas anteriores e distinguem cuidadosamente o uso proposto, a demonstração atual e as atividades que permanecem externas. O esquema de signos é o artefato mais maduro desta entrega. O principal problema conceitual está no mapa de objetivos: ele organiza atividades relevantes, mas não aplica a classificação ensinada de objetivos finais e objetivos instrumentais, diretos ou indiretos. O recorte de comunicação de CI02 também mistura conversa usuário–sistema com comunicação entre pessoas, exigindo uma separação mais rigorosa.

## Pontos positivos

- **Cenários de interação com origem e autoria identificadas.** CI01, CI02 e CI03 indicam C01, C02 e C03 como origem, preservam contexto, atores e objetivos e marcam em negrito as mudanças da solução proposta.
- **Evolução real dos cenários de problema.** CI01 substitui a procura manual integral pelo preparo, acompanhamento, revisão e obtenção de candidatos. CI03 transforma o problema de busca e limitação de equipamento em interação com análise, estados, falhas e obtenção, sem afirmar que o sistema reconhece automaticamente o atleta.
- **Justificativa adequada para o recorte de CI02.** A equipe explica que Arnaldo continua como persona atendida e destinatário externo, enquanto o editor utiliza a interface. Essa decisão preserva o escopo estabelecido e evita inventar um painel de aprovação.
- **Decisão humana preservada.** A classificação automática permanece como sugestão. Selecionar, baixar ou obter arquivos não significa aprovar publicação nem comprovar cobertura completa dos lances.
- **Conversas organizadas por tópicos e subtópicos.** CI01 e CI03 apresentam falas de U e D associadas a objetivos e signos, contemplando preparação, acompanhamento, revisão, seleção, obtenção e rupturas.
- **Esquema de signos amplo e contextualizado.** A tabela distingue conceitos do domínio e da aplicação, procedência dos valores, semântica, restrições, padrões, prevenção e recuperação. A separação entre relógio do jogo, posição no arquivo, duração, intervalo do corte, CSV e MP4 está bem realizada.
- **Rupturas comunicativas tratadas com cuidado.** A equipe define prevenção passiva, ativa e apoiada, recuperação apoiada e captura de erro, sem prometer recuperação interna quando a ação depende de ferramenta externa.
- **Rastreabilidade preservada.** Os objetivos e signos possuem identificadores reutilizáveis, e o documento registra hipóteses e limitações sem convertê-las em fatos comprovados.

## Correções prioritárias

### 1. Reconstruir o mapa segundo os tipos de objetivos da teoria

O mapa apresenta O00 como propósito global, três agrupamentos, O01–O07, O08 transversal e O09/O10 como continuidade externa. Essa organização ajuda a compreender o escopo, mas não classifica os objetivos como **finais**, **instrumentais**, **instrumentais diretos** ou **instrumentais indiretos**.

O material de aula define objetivo final como aquilo que leva o usuário a utilizar o sistema. Objetivos instrumentais facilitam esse resultado; os diretos atuam durante a interação, e os indiretos preparam algo para uso futuro. Essa classificação não aparece no diagrama nem no dicionário.

A equipe precisa revisar cada objetivo perguntando o que o usuário realmente deseja alcançar e o que funciona apenas como meio. “Obter material de melhores momentos para continuidade editorial externa” parece ocupar uma posição de finalidade, mas a classificação precisa ser assumida e justificada pela equipe. Preparar gravações, acompanhar análise, localizar candidatos e conferir seleção devem ser examinados quanto ao papel instrumental que desempenham.

Também revisem O09 e O10. Como parte dessas atividades ocorre fora da interface e envolve outro papel, o mapa deve deixar claro se representam objetivos finais de outra persona, objetivos externos relacionados ou simples continuidade do trabalho. A faixa tracejada atual sinaliza a fronteira, mas não resolve a classificação conceitual.

O mapa deve representar objetivos, não uma sequência de telas ou um roteiro operacional. A equipe já afirma essa intenção; agora precisa demonstrá-la com a notação e as categorias trabalhadas em aula.

### 2. Separar a conversa usuário–sistema da comunicação externa em CI02

O design centrado na comunicação trata a interação como uma conversa entre o usuário e o preposto do designer por meio da interface. Em CI02, as duas primeiras linhas seguem essa estrutura, com o editor como U e o sistema como D. As linhas seguintes criam uma categoria `E` para diálogos entre editor e Arnaldo por chat ou presencialmente.

Essas conversas externas são importantes para compreender a continuidade do trabalho, mas não constituem falas do usuário e do sistema na interface projetada. Mantê-las na mesma estrutura pode levar o MoLIC da próxima entrega a representar interações humanas externas como se fossem transições do sistema.

Preservem essas informações como contexto, fronteira ou condição de saída. No quadro de design centrado na comunicação, mantenham os tópicos, subtópicos e falas que realmente ocorrem entre U e D. Caso o recorte de Lucas tenha pouca conversa de interface porque P02 não opera o sistema, a equipe deve explicitar essa consequência e demonstrar qual conversa do editor com o sistema prepara adequadamente a passagem externa. A justificativa de escopo é válida; a notação precisa continuar rigorosa.

### 3. Distinguir melhor cenário de interação, especificação conceitual e hipótese técnica

Os cenários descrevem ações do usuário e respostas do sistema sem nomear botões ou widgets, o que está correto. Entretanto, alguns trechos acumulam condições técnicas detalhadas, como referência de tentativa, associação disponível, repetição orientada, estimativa de tamanho e preservação de resultados.

Essas informações podem fazer parte do modelo conceitual quando o usuário precisa compreendê-las. O cuidado necessário é não transformar capacidades ainda indefinidas do backend em comportamento já garantido. A redação utiliza expressões condicionais e reconhece várias limitações, mas a densidade dessas condições dificulta perceber a narrativa principal de uso.

Sugiro que vocês preservem no cenário apenas as respostas essenciais para o objetivo e para as rupturas. As condições técnicas detalhadas podem permanecer no esquema de signos e nas regras correspondentes. Isso tornará a evolução de C01–C03 mais clara e facilitará a passagem para o MoLIC.

### 4. Corrigir inconsistências entre signos e rastreabilidade

O esquema salta de S24 para S26. Isso não compromete o conteúdo, mas precisa ser explicado como identificador retirado ou reservado para evitar que o leitor procure S25.

Há uma inconsistência mais importante: `RASTREABILIDADE.md` referencia S34 e afirma que S33/S34 representam o tamanho individual e a soma dos vídeos. A tabela da Entrega 09 define apenas S33, referente ao tamanho individual do MP4. S34 não está definido. Corrijam a matriz ou incluam o signo correspondente, caso a soma seja realmente necessária e fundamentada.

Os intervalos compactos, como S16–S30, também podem esconder signos que não se aplicam a determinada relação. Prefiram referências precisas quando a decisão depende de poucos conceitos. A rastreabilidade deve ajudar a conferir o modelo, e não obrigar o leitor a adivinhar quais signos realmente sustentam cada relação.

### 5. Concluir a revisão individual e a consolidação declaradas como pendentes

O documento identifica Pedro, Lucas e Giovanni como autores de referência e fornece um cenário e um recorte de comunicação para cada um. Portanto, a quantidade formal foi atendida. Contudo, o próprio status e o checklist registram que a revisão individual, a apresentação dos recortes e a confirmação da consolidação ainda estão pendentes.

Antes de considerar a entrega encerrada, cada integrante precisa explicar seu cenário, as conversas, os objetivos e os signos associados. Em seguida, a equipe deve confirmar a nomenclatura consolidada e resolver as correções do mapa e de CI02. Esse fechamento é importante porque os mesmos nomes serão reutilizados no MoLIC; inconsistências propagadas agora aumentam o retrabalho na Entrega 10.


## Recomendações de melhoria

- Reduzam a quantidade de ressalvas repetidas dentro das falas. Limites importantes devem permanecer, mas a fala do preposto precisa ser compreensível para o usuário e não uma documentação interna completa.
- Mantenham uma legenda única para as siglas de prevenção e recuperação. O material apresenta nomenclaturas em português e abreviações de representação; registrem a correspondência para evitar divergência na Entrega 10.
- Confirmem se “candidato”, “lance”, “corte” e “seleção” são compreendidos pelo público. A distinção conceitual está boa, mas continua sendo hipótese até a avaliação.
- Atualizem a situação do questionário no documento, pois a página acessada já contém as revisões descritas, embora o texto ainda declare a publicação como pendente.
- Preservem a metamensagem da síntese: ela comunica adequadamente que o sistema apoia localização e obtenção, enquanto a pessoa mantém o julgamento editorial.

## Pontos que devem alimentar as próximas entregas

Na Entrega 10, utilizem somente objetivos e conversas já corrigidos. O MoLIC deve representar falas de U e D, processos, rupturas e encerramentos, sem transformar a conversa externa entre editor e supervisor em processamento do sistema.

A avaliação futura deverá investigar se os usuários distinguem relógio do jogo, posição no arquivo, candidato, corte, seleção, CSV e MP4. Também deverá verificar se estados, falhas e tentativas são compreendidos sem explicações do facilitador. Não considerem a completude do esquema de signos como prova de que o vocabulário funciona para os participantes.

O questionário publicado pode revelar dúvidas e preferências após o uso. Ele não substitui observação, conferência dos arquivos obtidos nem investigação das práticas profissionais. As entrevistas e o brainstorming continuam necessários para examinar o contexto do domínio e a passagem do material ao supervisor.

## Síntese das ações recomendadas

1. Classificar e reorganizar os objetivos como finais e instrumentais, diretos ou indiretos.
2. Retirar as conversas externas da estrutura de falas U–D de CI02, mantendo-as como fronteira do sistema.
3. Simplificar os cenários e concentrar detalhes técnicos no esquema de signos.
4. Corrigir S25/S34 e sincronizar o esquema com a rastreabilidade.
5. Realizar a revisão individual e confirmar a consolidação da equipe.


De forma geral, considero a Entrega 09 consistente com a trajetória do projeto e bastante cuidadosa na construção dos cenários e do esquema de signos. A equipe demonstra atenção ao vocabulário, às rupturas e aos limites do protótipo. O trabalho ainda precisa aplicar corretamente a teoria do mapa de objetivos, separar com rigor as conversas externas da interação usuário–sistema e concluir a revisão coletiva. Com essas correções, o modelo oferecerá uma base sólida e mais simples para a construção dos diagramas MoLIC.
