# Feedback do Professor > Entrega 03 > Equipe 16

> **Status da aplicação (03/10/2026):** esta revisão cobre a persona de Pedro (P01, Rafael), o mapa de empatia e a jornada de P01 e as partes de grupo da entrega: composição das personas, contexto de uso, lacunas e matriz de rastreabilidade. As fichas de Lucas (P02, Arnaldo) e Giovanni (P03, Jorginho Jr.) ficam com seus autores, assim como os mapas e jornadas de P02 e P03, escritos por Lucas. Cada comentário abaixo traz uma anotação com o link para o commit correspondente, na branch `aplicar-feedback`. O texto original do professor foi preservado; as anotações aparecem em blocos de citação logo após cada item.
>
> | Item do parecer | Situação | Commit(s) |
> |---|---|---|
> | Correção 1: composição e prioridade das personas | aplicada | [`1dde02e`](https://github.com/p4cs-974/projeto-ihc/commit/1dde02e) |
> | Correção 2: personagens caracterizados | aplicada em Rafael; Arnaldo e Jorginho Jr. ficam com Lucas e Giovanni | [`84e1398`](https://github.com/p4cs-974/projeto-ihc/commit/84e1398) |
> | Correção 3: contexto físico e social | aplicada | [`623c187`](https://github.com/p4cs-974/projeto-ihc/commit/623c187) |
> | Correção 4: narrativa das jornadas | aplicada na jornada de Rafael; P02 e P03 ficam com Lucas | [`5b45239`](https://github.com/p4cs-974/projeto-ihc/commit/5b45239) |
> | Correção 5: necessidades, hipóteses e solução | aplicada no mapa e na jornada de Rafael; os quatro ajustes pontuais ficam com Lucas e Giovanni | [`2895911`](https://github.com/p4cs-974/projeto-ihc/commit/2895911) |
> | Recomendação: justificar a classificação em cada ficha | aplicada | [`1dde02e`](https://github.com/p4cs-974/projeto-ihc/commit/1dde02e) |
> | Recomendação: ligar dores e necessidades nos mapas | aplicada no mapa de Rafael | [`2895911`](https://github.com/p4cs-974/projeto-ihc/commit/2895911) |
> | Recomendação: jogador × melhores momentos gerais | aplicada nas lacunas | [`7bb45ad`](https://github.com/p4cs-974/projeto-ihc/commit/7bb45ad) |
> | Recomendação: contexto e rastreabilidade em sincronia com os cenários | aplicada | [`623c187`](https://github.com/p4cs-974/projeto-ihc/commit/623c187), [`1f73b32`](https://github.com/p4cs-974/projeto-ihc/commit/1f73b32) |
> | Pontos para as próximas entregas | registrados nas lacunas | [`7bb45ad`](https://github.com/p4cs-974/projeto-ihc/commit/7bb45ad) |
> | Pendência da Entrega 1: redação de H05 na tabela de entradas | aplicada | [`9ed8554`](https://github.com/p4cs-974/projeto-ihc/commit/9ed8554) |
>
> \- Pedro

## Avaliação geral

A equipe apresenta três personas, três mapas de empatia e três jornadas, articulados com o problema de selecionar e revisar lances esportivos. O trabalho já diferencia a edição profissional, a supervisão editorial e a produção amadora, e registra suas principais suposições como hipóteses. Essa base é útil, mas ainda precisa de revisão antes de orientar as decisões de interface.

A quantidade de fichas atende à exigência de uma persona por integrante: Pedro responde por P01, Rafael; Lucas por P02, Arnaldo; e Giovanni por P03, Jorginho Jr. Entretanto, a composição de **uma persona primária e duas secundárias não atende à predominância de personas primárias solicitada**. Além disso, a participação exclusivamente externa de Arnaldo exige uma justificativa mais cuidadosa de sua classificação. As biografias, o contexto físico e social e a apresentação narrativa das jornadas também precisam avançar.

## Pontos positivos

- As três personas estão identificadas e possuem imagens em `assets/03_personas/`. As fichas apresentam objetivos, dificuldades, experiência e implicações para o projeto; portanto, há material efetivo para análise, e não apenas títulos preenchidos.
- Rafael tem características relevantes para a interação: experiência com edição, pressão de prazo, revisão dos cortes e preocupação com omissões. A preferência hipotética por conferir candidatos adicionais, em vez de perder lances relevantes, ajuda a discutir o esforço de revisão.
- Jorginho Jr. introduz diferenças pertinentes de equipamento, experiência e finalidade de uso. Produzir uma compilação sobre um atleta exige critérios de seleção que não podem ser presumidos iguais aos de um resumo geral da partida.
- Os mapas visuais `mapa_empatia_p01.svg`, `mapa_empatia_p02.svg` e `mapa_empatia_p03.svg` apresentam a persona central e os seis campos: pensa e sente, ouve, vê, fala e faz, dores e necessidades. **O formalismo básico do método está presente**, com correspondência entre os mapas e os textos.
- As jornadas contemplam preparação, atividades relacionadas ao serviço e continuidade externa. A montagem e a publicação posteriores ao download aparecem como parte do objetivo dos usuários.
- As hipóteses H30 a H38 e as relações R01 a R05 em `RASTREABILIDADE.md` ajudam a acompanhar a origem das características e decisões. É positivo declarar que as proto-personas ainda não representam resultados de pesquisa com usuários.

## Correções prioritárias

### 1. Rever a composição e justificar a prioridade das personas

Na seção de personas, Rafael é primário; Arnaldo e Jorginho Jr. são secundários. Para o conjunto atual de três fichas, a predominância solicitada exige pelo menos duas primárias. Contudo, a revisão não pode consistir apenas em trocar a classificação de uma ficha.

A equipe precisa demonstrar quais objetivos e necessidades de interação justificam priorizar cada perfil. Ser persona primária significa orientar decisões essenciais do projeto; ser secundária exige explicar como suas necessidades adicionais serão atendidas sem comprometer as prioritárias. A importância profissional do personagem, por si só, não resolve essa classificação.

Arnaldo merece atenção especial: sua participação foi delimitada como recebimento de arquivos e decisão editorial **fora da interface proposta**. Ele é relevante para compreender o processo, mas a ficha ainda não demonstra uma interação com o produto que sustente sua apresentação como persona secundária de uso. Esclareçam esse papel e revejam a seleção dos perfis necessários para cumprir a atividade. Não criem uma área administrativa apenas para fazer a classificação caber. A solução deve preservar o recorte do projeto e partir das atividades que efetivamente serão apoiadas.

> **✅ Como foi tratado** ([`1dde02e`](https://github.com/p4cs-974/projeto-ihc/commit/1dde02e)): a seção de personas abre com a subseção **Composição e prioridade das personas**. Para cada perfil, ela registra as atividades realizadas na interface, a justificativa da prioridade e a consequência prática no projeto. P01 e P03 são primárias porque as duas usam a interface do envio ao download. As restrições de equipamento e vocabulário de P03 mudam o próprio fluxo principal, por isso P03 não cabe como secundária. Arnaldo não usa a interface no recorte e passou a **persona atendida**, categoria de Cooper para quem não opera o produto, mas depende do que ele produz. As necessidades dele recaem sobre o que Rafael baixa, sem área administrativa nem tela de supervisão. Fichas, síntese, contexto, checklist e a linha R03 da matriz acompanham a mudança. Se Lucas preferir substituir Arnaldo por outro perfil que use a interface, a decisão fica com ele.
>
> \- Pedro

### 2. Transformar os perfis em personagens suficientemente caracterizados

As fichas são estruturadas, mas a caracterização ainda se concentra na ocupação e na relação com o projeto. Rafael e Arnaldo têm a idade não investigada, enquanto Jorginho Jr. reúne a faixa de 12 a 24 anos. Essa faixa cobre momentos de vida bastante diferentes e dificulta imaginar autonomia, rotina, disponibilidade e relação com os equipamentos.

Sugiro que vocês construam uma identidade fictícia mais definida para cada personagem, com nome identificável, idade ou recorte de vida coerente e uma breve biografia que conecte trajetória, rotina, experiência, responsabilidades e motivações. Isso não significa inventar resultados de entrevistas: características escolhidas para compor a proto-persona devem continuar explicitamente hipotéticas.

Em Rafael, expliquem como sua experiência e sua rotina se relacionam com a revisão de várias partidas. Em Arnaldo, deem consistência à trajetória e à responsabilidade editorial, além da expressão genérica de supervisão “engessada”. Em Jorginho Jr., delimitem o momento de vida e a relação entre produção de conteúdo, tempo disponível e recursos. Incluam somente detalhes que ajudem a compreender comportamentos e decisões de interação; uma biografia extensa, sem consequência para o projeto, também não resolve o problema.

> **🟨 Tratado em parte** ([`84e1398`](https://github.com/p4cs-974/projeto-ihc/commit/84e1398)): Rafael ganhou nome completo, Rafael Moura, idade, 31 anos, e uma biografia curta. Ela cobre a trajetória, a rotina em dia de rodada, de quatro a seis partidas, a responsabilidade pela seleção e a motivação ligada a uma omissão já cobrada por um clube. A biografia explica por que a experiência não reduz o esforço: o gargalo é o volume de partidas e a atenção que cai ao longo do dia, não a habilidade com a ferramenta. Todos os traços estão marcados como escolhas da proto-persona; o volume de partidas virou H39. A idade também entrou no mapa de empatia. As biografias de Arnaldo e de Jorginho Jr., incluindo a faixa de 12 a 24 anos, ficam com Lucas e Giovanni.
>
> \- Pedro

### 3. Detalhar o contexto físico e social de uso

A seção de contexto já distingue a sala de edição pouco iluminada de Rafael e o ambiente doméstico de Jorginho Jr. Entretanto, ainda há lacunas sobre as condições concretas em que as atividades acontecem. No caso de Arnaldo, a própria Entrega 04 já descreve circulação entre ilhas de edição, interrupções e decisões sob pressão, enquanto o contexto consolidado da Entrega 03 permanece menos definido.

A equipe precisa conectar ambiente e comportamento: quem está presente, como surgem interrupções, como os envolvidos se comunicam, quais recursos compartilham e de que forma a pressão social interfere na atenção e na decisão. Para o contexto doméstico, especifiquem as condições relevantes do local e a relação com outras atividades da rotina. Para o contexto profissional, explicitem a coordenação entre editor e supervisor e a passagem do material entre eles.

Essas condições podem permanecer como hipóteses nesta etapa. O necessário é que sejam descritas de maneira suficiente para orientar o projeto, sem substituir contexto de uso por uma lista de características do computador ou do servidor.

> **✅ Como foi tratado** ([`623c187`](https://github.com/p4cs-974/projeto-ihc/commit/623c187)): o contexto de uso ganhou a subseção **Condições físicas e sociais de uso**. Na produtora, ela descreve quem divide a sala com Rafael, como surgem as interrupções, os recursos compartilhados, a passagem dos cortes para Arnaldo por pasta no servidor e aviso pelo chat, e a cobrança diante dos colegas. A circulação de Arnaldo entre as ilhas vem do cenário C02. Na casa de Jorginho Jr., descreve o local, o momento, as outras atividades no mesmo computador e as relações sociais do canal, em sincronia com o cenário C03. Cada bloco termina com as consequências para o projeto. A passagem editor-supervisor virou H40 e a retomada após interrupção virou H41. Quem divide a casa com Jorginho Jr. ficou como lacuna, porque depende do momento de vida que Giovanni vai definir. O cenário C02 chama o local de trabalho de "emissora", e a ficha de Rafael fala em "produtora"; o alinhamento desse termo fica com Lucas.
>
> \- Pedro

### 4. Completar o caráter narrativo das jornadas

As três jornadas apresentam sete etapas e **já incluem o antes, o durante e o depois**. O problema não é ausência dessas fases: a descrição está concentrada em tabelas, com introduções e sínteses, mas ainda falta uma narrativa encadeada que permita acompanhar a experiência de cada personagem.

Acrescentem um relato que conecte a motivação inicial, a preparação, a sequência de atividades, as decisões diante de dificuldades e o benefício obtido após o uso. As tabelas podem permanecer como apoio. Não basta converter cada linha em uma frase isolada; expliquem por que uma etapa leva à seguinte.

Em Rafael, alinhem o encerramento declarado da jornada com a etapa de edição externa que o próprio documento inclui. Em Arnaldo, deixem explícito que a experiência descrita acompanha o processo editorial e o recebimento externo dos resultados, sem atribuir a ele um uso direto que não foi definido. Em Jorginho Jr., mantenham a distinção entre selecionar manualmente os cortes disponíveis e depender de uma identificação automática por atleta ainda não confirmada.

> **🟨 Tratado em parte** ([`5b45239`](https://github.com/p4cs-974/projeto-ihc/commit/5b45239)): a jornada de Rafael ganhou um relato encadeado. Ele parte do prazo e do receio de repetir uma omissão, passa pela conferência das gravações, pelo envio de todas as partidas para liberar o dia e pelas decisões diante de uma falha ou interrupção, e termina no benefício esperado. As tabelas continuam como apoio. O início e o fim declarados agora incluem a montagem no editor externo, que já era a etapa 7. As jornadas de Arnaldo e Jorginho Jr. foram escritas por Lucas e ficam com ele.
>
> \- Pedro

### 5. Separar necessidades, hipóteses de experiência e decisões de solução

Nos mapas de empatia, alguns campos de comportamento já descrevem a solução pretendida, como enviar partidas e aguardar o processamento remoto. Isso pode representar uma experiência futura proposta, mas não deve parecer evidência de comportamento atual. Identifiquem essa diferença para evitar que a solução imaginada seja usada como justificativa de si mesma.

Também há afirmações que precisam ser ajustadas:

- Na ficha de P03, processamento remoto é associado a não exigir armazenamento local. O próprio fluxo inclui obtenção de gravações e download de cortes. Reformulem o benefício esperado em termos de redução de esforço ou de necessidade de recursos, sem prometer ausência de armazenamento.
- O mapa e a jornada de P03 especificam uso pela web e navegador. Se essa plataforma ainda não foi consolidada nas decisões do projeto, registrem a escolha e sua justificativa ou mantenham a descrição sem esse compromisso.
- A oportunidade final da jornada de P02 afirma que o processo “reduz expressivamente falhas editoriais”. Essa redução é um benefício esperado a investigar, não um resultado demonstrado.
- Na etapa de download de P03, a reação é declarada não investigada e, em seguida, aparece satisfação com o pacote. Separem a lacuna de conhecimento da emoção hipotética adotada na narrativa.

Esses ajustes preservam o que vocês já fizeram bem ao distinguir hipóteses e evidências, tornando essa distinção consistente ao longo de toda a entrega.

> **🟨 Tratado em parte** ([`2895911`](https://github.com/p4cs-974/projeto-ihc/commit/2895911)): no mapa de Rafael, os campos Vê, Fala e faz e Necessidades separam **Hoje**, o comportamento atual hipotético baseado no cenário C01, de **Uso proposto**, a experiência imaginada com a interface. A separação vale na tabela e no SVG, onde o uso proposto aparece em azul. A jornada de Rafael declara que as etapas 2 a 6 descrevem o uso proposto e não servem de evidência a favor dele.
>
> **⏭️ Fora desta revisão:** os quatro ajustes pontuais estão em artefatos de Lucas e Giovanni. O armazenamento local é da ficha de P03, de Giovanni. A plataforma web, a frase "reduz expressivamente falhas editoriais" e a emoção no download de P03 estão nos mapas e jornadas de P02 e P03, escritos por Lucas.
>
> \- Pedro

## Recomendações de melhoria

- Justifiquem a classificação primária ou secundária junto de cada ficha, indicando a consequência prática dessa prioridade.

  > **✅ Como foi tratado** ([`1dde02e`](https://github.com/p4cs-974/projeto-ihc/commit/1dde02e)): a ficha de Rafael ganhou a linha **Por que primária**, e as fichas de Arnaldo e Jorginho Jr. apontam para a tabela de composição, que traz a consequência prática de cada classificação.
  >
  > \- Pedro

- Mantenham nos mapas a ligação entre dores e necessidades específicas. A estrutura visual está adequada; o próximo ganho está na precisão do conteúdo.

  > **✅ Como foi tratado** ([`2895911`](https://github.com/p4cs-974/projeto-ihc/commit/2895911)): o mapa de Rafael ganhou uma tabela que liga cada dor à necessidade correspondente e às hipóteses de origem. Os mapas de P02 e P03 ficam com Lucas.
  >
  > \- Pedro

- Diferenciem a necessidade de obter lances de um jogador da capacidade de detectar melhores momentos em geral. Um conjunto de destaques pode deixar de fora ações relevantes para a compilação desejada por P03.

  > **✅ Como foi tratado** ([`7bb45ad`](https://github.com/p4cs-974/projeto-ihc/commit/7bb45ad)): a lacuna do recorte por jogador agora pede para comparar os lances que P03 quer no compilado com os melhores momentos gerais, porque movimentações sem bola e passes de um atleta podem ficar fora de um conjunto de destaques.
  >
  > \- Pedro

- Atualizem o contexto e a rastreabilidade quando os cenários acrescentarem características úteis às personas. Novos detalhes hipotéticos são aceitáveis, mas precisam permanecer coerentes entre os documentos.

  > **✅ Como foi tratado** ([`623c187`](https://github.com/p4cs-974/projeto-ihc/commit/623c187), [`1f73b32`](https://github.com/p4cs-974/projeto-ihc/commit/1f73b32)): as condições físicas e sociais de uso incorporam detalhes dos cenários C01, C02 e C03. As características novas foram registradas como H39 a H41, e a matriz ganhou a entrada no registro de mudanças e no histórico.
  >
  > \- Pedro

## Pontos que devem alimentar as próximas entregas

A investigação posterior deverá verificar a tolerância a omissões e candidatos excedentes de Rafael, as informações realmente necessárias à decisão editorial de Arnaldo e a adequação dos resultados ao objetivo de Jorginho Jr. Também será importante investigar interrupções, condições de revisão, vocabulário compreendido e dificuldades de transferência do material para ferramentas externas.

Não é necessário antecipar agora resultados dessa investigação. Registrem o que ainda precisa ser conhecido e como cada dúvida interfere nas tarefas e na interação. H35, sobre auditoria editorial, e H36, sobre o recorte por jogador, merecem atenção para que possibilidades exploratórias não se tornem funcionalidades presumidas.

> **✅ Como foi tratado** ([`7bb45ad`](https://github.com/p4cs-974/projeto-ihc/commit/7bb45ad)): a tabela de lacunas ganhou tolerância de Rafael a omissões e a candidatos a mais, interrupções e retomada da revisão, vocabulário compreendido pelas duas personas primárias e transferência para ferramentas externas. A linha de supervisão passou a perguntar quais informações Arnaldo consulta para decidir. Uma nota abaixo da tabela mantém H35 e H36 fora do protótipo até haver evidência e, no caso de H36, confirmação técnica.
>
> \- Pedro

## Síntese das ações recomendadas

1. Rever a seleção e a classificação das personas, garantindo predominância de primárias com justificativas consistentes.
2. Completar a identidade e a biografia dos três personagens e esclarecer a participação de Arnaldo.
3. Detalhar o contexto físico e social e sincronizá-lo com os cenários.
4. Complementar as jornadas com narrativas encadeadas, preservando o antes, o durante e o depois já identificados.
5. Revisar as promessas de benefício e as decisões de solução, mantendo hipóteses e lacunas claramente diferenciadas.

> **Situação:** os itens 1 e 3 estão aplicados. Nos itens 2, 4 e 5, a parte de Rafael está aplicada; a parte de Arnaldo e Jorginho Jr. fica com Lucas e Giovanni (ver tabela no início).
>
> \- Pedro

De modo geral, considero que a entrega apresenta uma base organizada e pertinente ao projeto, especialmente nos mapas de empatia e na identificação das atividades que continuam após o uso. Ainda não a considero plenamente atendida, porque a composição das personas contraria a predominância solicitada e a caracterização dos personagens e de seus contextos precisa sustentar melhor as decisões futuras. A revisão deve aprofundar quem são essas pessoas e como vivem a atividade, aproveitando os artefatos existentes para produzir um entendimento mais concreto da experiência de uso.
