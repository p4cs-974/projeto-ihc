# Feedback do Professor > Entrega 09 > Equipe 16

> **Status da aplicação (18/11/2026).** A revisão cobre os recortes individuais e a consolidação da equipe. [?] As apresentações, a confirmação de cada autor e a validação com usuários seguem pendentes.
>
> | Item do parecer | Situação | Commit |
> |---|---|---|
> | Correção 1 · Classificação dos objetivos | Aplicada | [`aa1dd5a`](https://github.com/p4cs-974/projeto-ihc/commit/aa1dd5a505ad98e4807d6d3349d2de60eb2b2a4f) |
> | Correção 2 · Conversa da interface em CI02 | Aplicada | [`1d9068c`](https://github.com/p4cs-974/projeto-ihc/commit/1d9068c7c1f47ed04bed79332e039c26de99b51e) |
> | Correção 3 · Narrativas e condições técnicas | Aplicada | [`5222fdd`](https://github.com/p4cs-974/projeto-ihc/commit/5222fdd262892fa9895c70df1407ac6b79ae6ee9) |
> | Correção 4 · Signos na matriz | Aplicada | [`85a6b55`](https://github.com/p4cs-974/projeto-ihc/commit/85a6b5535eec8bcc51f1e5caee05650e47915ed3) |
> | Correção 5 · Revisão dos autores e consolidação | Parcial | [`347184c`](https://github.com/p4cs-974/projeto-ihc/commit/347184c1c1a7e360093cede29d46345ef1d2f827) |
> | Recomendação 1 · Falas mais curtas | Aplicada | [`ff68acc`](https://github.com/p4cs-974/projeto-ihc/commit/ff68acc2db92d6375e9fbac430d1c5b129d1146b) |
> | Recomendação 2 · Legenda única | Aplicada | [`1b91d96`](https://github.com/p4cs-974/projeto-ihc/commit/1b91d966214abad7b47a3cebe58fa994a9f288de) |
> | Recomendação 3 · Compreensão dos termos | Encaminhada | [`7fea226`](https://github.com/p4cs-974/projeto-ihc/commit/7fea226990cbe73377864d837ad469704e2bafcc) |
> | Recomendação 4 · Publicação do questionário | Aplicada | [`a2c35b1`](https://github.com/p4cs-974/projeto-ihc/commit/a2c35b1fee5cb5d190a35a761959a109c483233e) |
> | Recomendação 5 · Metamensagem | Preservada | — |
> | Próximas entregas 1 · Base para o MoLIC | Aplicada | [`7b65ffa`](https://github.com/p4cs-974/projeto-ihc/commit/7b65ffa829169099711f174ac9f5dd91b9ba09ba) |
> | Próximas entregas 2 · Avaliação de estados e arquivos | Encaminhada | [`c7e93a6`](https://github.com/p4cs-974/projeto-ihc/commit/c7e93a6cd45b3f834fb1e871fe406f5723095e78) |
> | Próximas entregas 3 · Alcance dos instrumentos | Aplicada | [`5747e01`](https://github.com/p4cs-974/projeto-ihc/commit/5747e0177765247e70302891dc7d99f2393525b1) |
>
> \- Pedro

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

> **✅ Como foi tratado** ([`aa1dd5a`](https://github.com/p4cs-974/projeto-ihc/commit/aa1dd5a505ad98e4807d6d3349d2de60eb2b2a4f)). [F] O mapa e o dicionário classificam O00 como finalidade de P01 e P03, O01 como instrumental indireto e O02 a O08 como instrumentais diretos. O09 é a finalidade externa de P02. O10 é continuidade de edição.
>
> \- Pedro

### 2. Separar a conversa usuário–sistema da comunicação externa em CI02

O design centrado na comunicação trata a interação como uma conversa entre o usuário e o preposto do designer por meio da interface. Em CI02, as duas primeiras linhas seguem essa estrutura, com o editor como U e o sistema como D. As linhas seguintes criam uma categoria `E` para diálogos entre editor e Arnaldo por chat ou presencialmente.

Essas conversas externas são importantes para compreender a continuidade do trabalho, mas não constituem falas do usuário e do sistema na interface projetada. Mantê-las na mesma estrutura pode levar o MoLIC da próxima entrega a representar interações humanas externas como se fossem transições do sistema.

Preservem essas informações como contexto, fronteira ou condição de saída. No quadro de design centrado na comunicação, mantenham os tópicos, subtópicos e falas que realmente ocorrem entre U e D. Caso o recorte de Lucas tenha pouca conversa de interface porque P02 não opera o sistema, a equipe deve explicitar essa consequência e demonstrar qual conversa do editor com o sistema prepara adequadamente a passagem externa. A justificativa de escopo é válida; a notação precisa continuar rigorosa.

> **✅ Como foi tratado** ([`1d9068c`](https://github.com/p4cs-974/projeto-ihc/commit/1d9068c7c1f47ed04bed79332e039c26de99b51e)). [F] O quadro contém a conversa U–D do editor. A avaliação, os pedidos de ajuste e a decisão de Arnaldo estão na condição de saída para T02.
>
> \- Pedro

### 3. Distinguir melhor cenário de interação, especificação conceitual e hipótese técnica

Os cenários descrevem ações do usuário e respostas do sistema sem nomear botões ou widgets, o que está correto. Entretanto, alguns trechos acumulam condições técnicas detalhadas, como referência de tentativa, associação disponível, repetição orientada, estimativa de tamanho e preservação de resultados.

Essas informações podem fazer parte do modelo conceitual quando o usuário precisa compreendê-las. O cuidado necessário é não transformar capacidades ainda indefinidas do backend em comportamento já garantido. A redação utiliza expressões condicionais e reconhece várias limitações, mas a densidade dessas condições dificulta perceber a narrativa principal de uso.

Sugiro que vocês preservem no cenário apenas as respostas essenciais para o objetivo e para as rupturas. As condições técnicas detalhadas podem permanecer no esquema de signos e nas regras correspondentes. Isso tornará a evolução de C01–C03 mais clara e facilitará a passagem para o MoLIC.

> **✅ Como foi tratado** ([`5222fdd`](https://github.com/p4cs-974/projeto-ihc/commit/5222fdd262892fa9895c70df1407ac6b79ae6ee9)). [F] CI01, CI02 e CI03 concentram-se em ações, respostas e rupturas. O esquema de signos reúne condições para tentativa, aceitação, preservação de resultados e retomada.
>
> \- Pedro

> **Após revisão independente** ([`ca3f4f6`](https://github.com/p4cs-974/projeto-ihc/commit/ca3f4f62e97d3409db9e1e531c55afd599007702)). [F] A descrição da demonstração indica que há falha e nova tentativa localizada encenadas. [?] A recuperação no serviço real permanece em aberto.
>
> \- Pedro

### 4. Corrigir inconsistências entre signos e rastreabilidade

O esquema salta de S24 para S26. Isso não compromete o conteúdo, mas precisa ser explicado como identificador retirado ou reservado para evitar que o leitor procure S25.

Há uma inconsistência mais importante: `RASTREABILIDADE.md` referencia S34 e afirma que S33/S34 representam o tamanho individual e a soma dos vídeos. A tabela da Entrega 09 define apenas S33, referente ao tamanho individual do MP4. S34 não está definido. Corrijam a matriz ou incluam o signo correspondente, caso a soma seja realmente necessária e fundamentada.

Os intervalos compactos, como S16–S30, também podem esconder signos que não se aplicam a determinada relação. Prefiram referências precisas quando a decisão depende de poucos conceitos. A rastreabilidade deve ajudar a conferir o modelo, e não obrigar o leitor a adivinhar quais signos realmente sustentam cada relação.

> **✅ Como foi tratado** ([`85a6b55`](https://github.com/p4cs-974/projeto-ihc/commit/85a6b5535eec8bcc51f1e5caee05650e47915ed3)). [F] S25 está reservado. A matriz aponta para S33, tamanho individual do MP4, e usa referências pertinentes a R01–R05.
>
> \- Pedro

> **Após revisão independente** ([`7b92f56`](https://github.com/p4cs-974/projeto-ihc/commit/7b92f561137bd1278234b0d9cda341a12d064f4c)). [F] R03 inclui a duração S21 de M02. R02 e R05 incluem S29 e a retomada O08.
>
> \- Pedro

### 5. Concluir a revisão individual e a consolidação declaradas como pendentes

O documento identifica Pedro, Lucas e Giovanni como autores de referência e fornece um cenário e um recorte de comunicação para cada um. Portanto, a quantidade formal foi atendida. Contudo, o próprio status e o checklist registram que a revisão individual, a apresentação dos recortes e a confirmação da consolidação ainda estão pendentes.

Antes de considerar a entrega encerrada, cada integrante precisa explicar seu cenário, as conversas, os objetivos e os signos associados. Em seguida, a equipe deve confirmar a nomenclatura consolidada e resolver as correções do mapa e de CI02. Esse fechamento é importante porque os mesmos nomes serão reutilizados no MoLIC; inconsistências propagadas agora aumentam o retrabalho na Entrega 10.

> **🟨 Tratado em parte** ([`347184c`](https://github.com/p4cs-974/projeto-ihc/commit/347184c1c1a7e360093cede29d46345ef1d2f827)). [F] O checklist atribui a apresentação e a revisão de CI01 a Pedro, CI02 a Lucas e CI03 a Giovanni. [?] A equipe ainda precisa apresentar os recortes e confirmar a nomenclatura e a fronteira de CI02.
>
> \- Pedro


## Recomendações de melhoria

- Reduzam a quantidade de ressalvas repetidas dentro das falas. Limites importantes devem permanecer, mas a fala do preposto precisa ser compreensível para o usuário e não uma documentação interna completa.

  > **✅ Como foi tratado** ([`ff68acc`](https://github.com/p4cs-974/projeto-ihc/commit/ff68acc2db92d6375e9fbac430d1c5b129d1146b)). [F] As falas comunicam a informação de que a pessoa precisa para decidir. As condições detalhadas constam no esquema de signos.
  >
  > \- Pedro
- Mantenham uma legenda única para as siglas de prevenção e recuperação. O material apresenta nomenclaturas em português e abreviações de representação; registrem a correspondência para evitar divergência na Entrega 10.

  > **✅ Como foi tratado** ([`1b91d96`](https://github.com/p4cs-974/projeto-ihc/commit/1b91d966214abad7b47a3cebe58fa994a9f288de)). [F] A tabela de convenções registra PP, PA, AL, RA e CE como referência para os MoLIC.
  >
  > \- Pedro

  > **Após revisão independente** ([`6a1bd3d`](https://github.com/p4cs-974/projeto-ihc/commit/6a1bd3d9c0616312af3c11afc5daabaf3f49e94b)). [F] A tabela indica a correspondência de AL com `[SP]` e de RA com `[SR]` no exemplo da Parte B.
  >
  > \- Pedro

- Confirmem se “candidato”, “lance”, “corte” e “seleção” são compreendidos pelo público. A distinção conceitual está boa, mas continua sendo hipótese até a avaliação.

  > **ℹ️ Encaminhamento** ([`7fea226`](https://github.com/p4cs-974/projeto-ihc/commit/7fea226990cbe73377864d837ad469704e2bafcc)). [F] A avaliação prevê pedir que a pessoa explique lance, candidato, corte e seleção durante a revisão. [?] A compreensão pelo público permanece em aberto.
  >
  > \- Pedro
- Atualizem a situação do questionário no documento, pois a página acessada já contém as revisões descritas, embora o texto ainda declare a publicação como pendente.

  > **✅ Como foi tratado** ([`a2c35b1`](https://github.com/p4cs-974/projeto-ihc/commit/a2c35b1fee5cb5d190a35a761959a109c483233e)). [F] A Entrega 7 e o README registram a versão pública 2026-11-10, conferida no guia. Pilotos e coleta seguem pendentes.
  >
  > \- Pedro
- Preservem a metamensagem da síntese: ela comunica adequadamente que o sistema apoia localização e obtenção, enquanto a pessoa mantém o julgamento editorial.

  > **ℹ️ Preservado**. [F] A síntese mantém o sistema como apoio à localização e à obtenção. A pessoa decide o que é pertinente e como continuar o trabalho editorial.
  >
  > \- Pedro

## Pontos que devem alimentar as próximas entregas

Na Entrega 10, utilizem somente objetivos e conversas já corrigidos. O MoLIC deve representar falas de U e D, processos, rupturas e encerramentos, sem transformar a conversa externa entre editor e supervisor em processamento do sistema.

> **✅ Como foi tratado** ([`7b65ffa`](https://github.com/p4cs-974/projeto-ihc/commit/7b65ffa829169099711f174ac9f5dd91b9ba09ba)). [F] A tabela de cobertura vincula os recortes à Entrega 10 e define a supervisão em CI02 como condição de saída.
>
> \- Pedro

A avaliação futura deverá investigar se os usuários distinguem relógio do jogo, posição no arquivo, candidato, corte, seleção, CSV e MP4. Também deverá verificar se estados, falhas e tentativas são compreendidos sem explicações do facilitador. Não considerem a completude do esquema de signos como prova de que o vocabulário funciona para os participantes.

> **ℹ️ Encaminhamento** ([`c7e93a6`](https://github.com/p4cs-974/projeto-ihc/commit/c7e93a6cd45b3f834fb1e871fe406f5723095e78)). [F] As questões de avaliação indicam o que observar sem ajuda do facilitador e pedem abrir o CSV e reproduzir o MP4 salvos.
>
> \- Pedro

O questionário publicado pode revelar dúvidas e preferências após o uso. Ele não substitui observação, conferência dos arquivos obtidos nem investigação das práticas profissionais. As entrevistas e o brainstorming continuam necessários para examinar o contexto do domínio e a passagem do material ao supervisor.

> **✅ Como foi tratado** ([`5747e01`](https://github.com/p4cs-974/projeto-ihc/commit/5747e0177765247e70302891dc7d99f2393525b1)). [F] A Entrega 9 registra quais evidências dependem de observação, conferência de arquivos, relatos após o uso e investigação das práticas editoriais.
>
> \- Pedro

## Síntese das ações recomendadas

1. Classificar e reorganizar os objetivos como finais e instrumentais, diretos ou indiretos.
2. Retirar as conversas externas da estrutura de falas U–D de CI02, mantendo-as como fronteira do sistema.
3. Simplificar os cenários e concentrar detalhes técnicos no esquema de signos.
4. Corrigir S25/S34 e sincronizar o esquema com a rastreabilidade.
5. Realizar a revisão individual e confirmar a consolidação da equipe.

> **Situação.** [F] As mudanças documentais estão registradas acima. [?] Faltam as apresentações e a confirmação de Pedro, Lucas e Giovanni.
>
> \- Pedro


De forma geral, considero a Entrega 09 consistente com a trajetória do projeto e bastante cuidadosa na construção dos cenários e do esquema de signos. A equipe demonstra atenção ao vocabulário, às rupturas e aos limites do protótipo. O trabalho ainda precisa aplicar corretamente a teoria do mapa de objetivos, separar com rigor as conversas externas da interação usuário–sistema e concluir a revisão coletiva. Com essas correções, o modelo oferecerá uma base sólida e mais simples para a construção dos diagramas MoLIC.
