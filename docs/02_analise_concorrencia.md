# Entrega 2 — Público-alvo e análise de concorrência

**Data:** 19/08/2026  
**Status:** `🟨 em andamento`
**Responsabilidade mínima:** cada integrante analisa pelo menos 1 concorrente/interface representativa; a equipe produz síntese comparativa.

## Objetivo da atividade

Compreender soluções do mesmo domínio **e também interfaces familiares ao público-alvo**. O objetivo não é copiar telas, mas identificar convenções, padrões, affordances percebidas, problemas recorrentes, expectativas e oportunidades de design.

> **Concorrente não precisa ser idêntico ao produto.** Pode atuar na mesma área, resolver objetivo semelhante ou disputar a mesma necessidade. Quando não houver concorrente direto, use produtos análogos e softwares que o público já utiliza.

### Para TCCs que não previam interface

Não procure apenas um “concorrente do algoritmo”. Investigue **interfaces profissionais que materializam atividades semelhantes** às que o usuário escolhido precisaria realizar.

Exemplos:

- TCC de banco de dados → consoles de administração, ferramentas para DBA, monitoramento e análise de consultas;
- TCC de LLM/ML → painéis de experimentos, gestão de modelos/datasets, comparação de métricas, revisão de resultados;
- TCC de análise de dados → dashboards, ferramentas de BI, filtros, relatórios e exploração;
- TCC de infraestrutura/API → portais administrativos, observabilidade, logs, gestão de credenciais e uso;
- TCC de cibersegurança → consoles de alertas, triagem, histórico e auditoria.

A pergunta é: **“que convenções esse perfil já conhece para executar tarefas equivalentes?”**

## Entrada obrigatória da Entrega 1

> softwares pra olhar: capcut, davinci resolve, premiere pro, fina cut pro, cap.so, sony vegas

Retome o mapa inicial de alternativas e produtos citado na Entrega 1. Aqui a equipe deixa de trabalhar apenas com impressão inicial e passa a **investigar sistematicamente** cada solução.

| Item citado na Entrega 1 | Tipo                 | Por que foi citado                                                         | Status inicial                                                          | Decisão nesta entrega |
| ------------------------ | -------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------- |
| Adobe Premiere Pro       | ferramenta cotidiana | Editar manualmente vídeos de melhores momentos                             | [F] Citado na Entrega 1 como editor profissional conhecido pelo público | analisar              |
| DaVinci Resolve          | ferramenta cotidiana | Importar, assistir, marcar, recortar, organizar e exportar trechos         | [F] Alternativa de edição manual documentada na Entrega 1               | analisar              |
| CapCut                   | ferramenta cotidiana | Editar manualmente vídeos                                                  | [F] Citado na Entrega 1 como alternativa indireta para edição manual    | analisar              |
| Final Cut Pro            | ferramenta cotidiana | Editar manualmente vídeos                                                  | [F] Citado na Entrega 1 como alternativa indireta para edição manual    | analisar              |
| cap.so                   | ferramenta cotidiana | Editar manualmente vídeos                                                  | [F] Citado na Entrega 1 como alternativa indireta para edição manual    | analisar              |
| WSC Sports               | concorrente direto   | Analisar eventos, criar conteúdo, gerenciar ativos e distribuir resultados | [F] Página oficial da plataforma citada na Entrega 1                    | analisar              |
| Magnifi                  | concorrente direto   | Gerar, etiquetar, baixar e distribuir cortes de vídeos esportivos          | [F] Página oficial do produto e FAQ citados na Entrega 1                | analisar              |

Se uma hipótese da Entrega 1 for confirmada ou refutada durante esta análise, atualize `H01`, `H02`... em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

## 1. Público-alvo desta análise

O público-alvo principal é formado por profissionais responsáveis pelo corte e pela produção de vídeos de melhores momentos de partidas de futebol, como editores de vídeo esportivo. Na pós-produção, eles precisam processar gravações, acompanhar os resultados e acessar os cortes e metadados gerados. Empresas de mídia esportiva, ligas, emissoras, produtoras e clubes são stakeholders desse processo. Conforme a Entrega 1, esse público utiliza principalmente computadores e pode estar familiarizado com softwares de edição de vídeo, o que orienta a análise das interfaces selecionadas.

## 2. Concorrentes diretos/indiretos

### Análise C01 — Adobe Premiere Pro

**Autor(a):** Giovanni Chahin Morassi — 22.123.025-3  
**Tipo:** concorrente indireto / ferramenta cotidiana  
**Link oficial:** {{URL}}  
**Data de acesso:** {{dd/mm/aaaa}}

#### Contexto e proposta

Analisar como o Adobe Premiere Pro apoia a edição manual de vídeos de melhores momentos, incluindo importação, marcação, organização, recorte e exportação.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print                              | Observação de IHC |
| -------------- | ---------------- | -------------------------------------------- | ----------------- |
| Abrir video        | O usuario pode abrir uma pasta do computador, selecionar os arquivos e importar para o projeto, o software entende isso e consegue utilizar para visualização do conteudo           | `../assets/02_concorrencia/premiere-pro/...` | {{...}}           |
| Adicionar na timeline      | pela interface do sistema é possivel o usuario arrastar os videos importados para a area da timeline          | `../assets/02_concorrencia/premiere-pro/...` | {{...}}           |
| cortar um clipe        | a timeline possui um cursor, no qual pode navegar por toda duração do video, ao colocar o cursor em determinado momento existe um botão com o icone de tesoura, é possivel clickar, e ao clickar os clips onde estão por baixo do cursor serão divididos em 2          | `../assets/02_concorrencia/premiere-pro/...` | {{...}}           |
| adicionar musica ao video        | a timeline é dividida em visual e audio, é possivel da mesma forma que adicionar um video ao projeto é possivel adicionar uma musica, e da mesma foram que ao adicionar o video na timeline é possivel adicionar a musica, porem no setor da timeline da musica          | `../assets/02_concorrencia/premiere-pro/...` | {{...}}           |

#### Experiência do usuário e opiniões

{{...}}

#### Padrões e tendências percebidos

{{...}}

#### Pontos positivos, limitações e lições

| Ponto   | Evidência | Implicação para nosso projeto |
| ------- | --------- | ----------------------------- |
| {{...}} | {{...}}   | {{...}}                       |

### Análise C02 — DaVinci Resolve

**Autor(a):** Giovanni Chahin Morassi — 22.123.025-3  
**Tipo:** concorrente indireto / ferramenta cotidiana  
**Link oficial:** [Página oficial](https://www.blackmagicdesign.com/products/davinciresolve/media)  
**Data de acesso:** {{dd/mm/aaaa}}

#### Contexto e proposta

Analisar como o DaVinci Resolve apoia a importação, organização, marcação, edição e exportação de vídeos.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print                                 | Observação de IHC |
| -------------- | ---------------- | ----------------------------------------------- | ----------------- |
| {{...}}        | {{...}}          | `../assets/02_concorrencia/davinci-resolve/...` | {{...}}           |

#### Experiência do usuário e opiniões

{{...}}

#### Padrões e tendências percebidos

{{...}}

#### Pontos positivos, limitações e lições

| Ponto   | Evidência | Implicação para nosso projeto |
| ------- | --------- | ----------------------------- |
| {{...}} | {{...}}   | {{...}}                       |

### Análise C03 — CapCut

**Autor(a):** Pedro Alexandre Custodio Silva — 22.123.049-3  
**Tipo:** concorrente indireto / ferramenta cotidiana  
**Link oficial:** {{URL}}  
**Data de acesso:** {{dd/mm/aaaa}}

#### Contexto e proposta

Analisar como o CapCut apoia a edição manual de vídeos.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print                        | Observação de IHC |
| -------------- | ---------------- | -------------------------------------- | ----------------- |
| {{...}}        | {{...}}          | `../assets/02_concorrencia/capcut/...` | {{...}}           |

#### Experiência do usuário e opiniões

{{...}}

#### Padrões e tendências percebidos

{{...}}

#### Pontos positivos, limitações e lições

| Ponto   | Evidência | Implicação para nosso projeto |
| ------- | --------- | ----------------------------- |
| {{...}} | {{...}}   | {{...}}                       |

### Análise C04 — Final Cut Pro

**Autor(a):** Pedro Alexandre Custodio Silva — 22.123.049-3  
**Tipo:** concorrente indireto / ferramenta cotidiana  
**Link oficial:** {{URL}}  
**Data de acesso:** {{dd/mm/aaaa}}

#### Contexto e proposta

Analisar como o Final Cut Pro apoia a edição manual de vídeos.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print                               | Observação de IHC |
| -------------- | ---------------- | --------------------------------------------- | ----------------- |
| {{...}}        | {{...}}          | `../assets/02_concorrencia/final-cut-pro/...` | {{...}}           |

#### Experiência do usuário e opiniões

{{...}}

#### Padrões e tendências percebidos

{{...}}

#### Pontos positivos, limitações e lições

| Ponto   | Evidência | Implicação para nosso projeto |
| ------- | --------- | ----------------------------- |
| {{...}} | {{...}}   | {{...}}                       |

### Análise C05 — cap.so

**Autor(a):** Pedro Alexandre Custodio Silva — 22.123.049-3  
**Tipo:** concorrente indireto / ferramenta cotidiana  
**Link oficial:** {{URL}}  
**Data de acesso:** {{dd/mm/aaaa}}

#### Contexto e proposta

Analisar como o cap.so apoia a edição manual de vídeos.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print                        | Observação de IHC |
| -------------- | ---------------- | -------------------------------------- | ----------------- |
| {{...}}        | {{...}}          | `../assets/02_concorrencia/cap-so/...` | {{...}}           |

#### Experiência do usuário e opiniões

{{...}}

#### Padrões e tendências percebidos

{{...}}

#### Pontos positivos, limitações e lições

| Ponto   | Evidência | Implicação para nosso projeto |
| ------- | --------- | ----------------------------- |
| {{...}} | {{...}}   | {{...}}                       |

### Análise C06 — WSC Sports

**Autor(a):** Lucas Roberto Boccia dos Santos — 22.123.012-1  
**Tipo:** concorrente direto  
**Link oficial:** [Página da plataforma](https://wsc-sports.com/platform/)  
**Data de acesso:** {{dd/mm/aaaa}}

#### Contexto e proposta

A WSC Sports provê uma plataforma com algorítmos especializados de IA para analisar, classificar, avaliar, criar e gerenciar conteúdo de eventos de esporte. O principal objetivo do serviço é acelerar e aprimorar o fluxo de produção e personalização do conteúdo.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print                            | Observação de IHC |
| -------------- | ---------------- | ------------------------------------------ | ----------------- |
| Identificar e classificar objetos em vídeos      | O usuário seleciona um vídeo e um algorítmo de visão computacional realiza a identificação e classificação dos objetos na tela | ![Detecção de Objetos](../assets/02_concorrencia/wsc-sports/wsc-objects.jpeg) | O site não nos dá uma preview do processo para realizar essa análise, mas a interface que mostra os objetos na tela destaca e classifica os objetos na tela de forma muito sólida, com bounding boxes e tags contrastantes e fáceis de serem lidas e um índice de objetos identificados        |
| Criação de vídeos automática | O usuário seleciona um conjunto de cenas, clica em "Criar Video" e o sistema cria um ou mais vídeos personalizados com o conjunto de cenas | [Criar Vídeos](projeto-ihc/assets/02_concorrencia/wsc-sports/wsc-create.jpeg) | A preview de interface que o site nos fornece é bem direta ao ponto, o usuário seleciona o conjunto de cenas e clica em um botão "Create Video", e os vídeos são gerados na tela para ele |
| Estúdio de edição de vídeos | O usuário possui, dentro da plataforma, um serviço completo de edição de vídeos, com opções para gerenciar vídeo, aúdio, legendas, gráficos, tudo com preview em tempo real e uma opção de publicação automática | [Estúdio de Edição](projeto-ihc/assets/02_concorrencia/wsc-sports/wsc-studio.jpeg) | A preview simplificada da interface no site representa uma UI clássica de programas famosos de edição, com uma tela de preview, e os atributos (áudio, vídeo, legendas, gráficos) na parte inferior em um sistema de barras |
| Pesquisa por Conteúdo Existente | O usuário dispõe da funcionalidade de gerenciar o contéudo já gravado na plataforma, podendo pesquisar por mídias específicas, seja por nome, seja por classificação | [Gerenciamento de Vídeos](projeto-ihc/assets/02_concorrencia/wsc-sports/wsc-manage.jpeg) |  A preview do sistema de pesquisa mostra uma interface de busca organizada e direta ao ponto, sem muitos elementos na tela além do essencial |
| Monitoramento de Performance dos Vídeos | O usuário consegue visualizar a "performance" do vídeo nas mídias sociais, podendo acessar dados como número de visualizações, número de compartilhamentos, número de vezes que o app foi instalado e até a renda estimada | [Monitoramento](projeto-ihc/assets/02_concorrencia/wsc-sports/wsc-engage.jpeg) | Os indicadores de performance são diretos e fáceis de entender, o sistema indica ao usuário as informações de forma bem clara e explícita, acompanhado de uma preview do vídeo |

#### Experiência do usuário e opiniões

Os relatos foram traduzidos da página oficial de clientes da WSC Sports

"A confiabilidade da plataforma da WSC Sports é algo que nunca nos deixou na mão. É algo em que pudemos confiar desde que começamos a usá-la em 2015." - Brandon Jirousek, VP Digital, Cleveland Cavaliers.

"A WSC Sports nos permite investir de verdade na personalização e na localização do nosso conteúdo, o que é fundamental para ampliar o nível de personalização que oferecemos aos nossos torcedores." - Chris Foster, VP Digital Business Development - NHL.

"Em colaboração com a WCS Sports, poderemos oferecer aos nossos torcedores conteúdos cada vez mais envolventes e inovadores, assim como oferecer aos 20 clubes da Lega Serie A um produto de ponta para ampliar suas ofertas nas redes sociais" - Lorenzo Dallari, Editorial & Social Director - Lega Serie A.

"Nossa parceria com a WSC nos permite liderar a criação e a entrega de conteúdo altamente relevante e personalizado — aquele que é mais importante para o nosso público — em tempo real." - Olek Lowenstein, President of Global Sports - TelevisaUnivision.

"A ATP Media busca constantemente formas de aumentar o engajamento e oferecer um atendimento excepcional aos nossos fãs. Por meio da parceria com a WSC Sports, podemos levar momentos ainda mais emocionantes dos nossos torneios a milhões de fãs de tênis em todo o mundo, com rapidez e em grande escala." - Stuart Watts, COO - ATP Media.

"Nós sabemos o que os fãs querem. Em parceria com a WSC Sports, conseguimos maximizar o impacto dos nossos direitos e transformar a nossa forma de entrega nesse segmento; estamos alcançando mais fãs ao criar clipes e melhores momentos empolgantes, adaptados aos locais e plataformas de onde eles consomem o conteúdo." - Sarah Beattie, Chief of Marketing Officer - Six Nations Rugby.

#### Padrões e tendências percebidos

Com base nas previews que temos acesso no site da WSC_Sports, a plataforma utiliza um padrão de interface que mistura elementos comuns de interfaces web com o visual clássico de outros softwares populares de edição de vídeo. Os mecanismos de busca e gerenciamento de conteúdo usam um layout com elementos visuais semelhantes aos de muitos webapps, com botões responsivos, animações, emojis e navegação rápida. O layout do estúdio de edição, por sua vez, segue o padrão de fundo escuro, cores contrastantes e divisão de elementos de edição (como áudio, vídeo, legendas e gráficos) por meio de um sistema de barras.

#### Pontos positivos, limitações e lições

| Ponto   | Evidência | Implicação para nosso projeto |
| ------- | --------- | ----------------------------- |
| Ponto positivo: Interfaces modernas e que seguem o padrão dos outros softwares observados | Prints da pasta assets e os pontos discutidos anteriormente. Essas informações estão disponíveis no site da WSC Sports   | Valida o tipo de interface comum entre os softwares da área, nos dando uma ideia do que a indústria usa e de qual é o padrão que estão mais acostumados, fatores que devemos levar em consideração no desenvolvimento da nossa interface |
| Ponto positivo: Plataforma completa que condensa diversos tipos de serviços diferentes e úteis da área (automação de cortes, edição de vídeo, detecção de objetos, análise de performance...) | Tabela de funcionalidades acima e relatos dos clientes. Informações estão disponíveis no site da WSC Sports | Nos dá uma ideia de que tipo de software já existe e é adotado e validado pela indústria hoje, nos permitindo ter uma visão melhor de quais elementos adotar para a nossa interface e de onde a contribuição científica da nossa pesquisa se posiciona na área |
| Limitação: Pouco acesso a informações técnicas mais aprofundadas e à interface completa do produto | A WSC Sports divulga informações técnicas e imagens da plataforma de forma muito limitada no seu website e nas suas mídias sociais | Por não termos acesso à interface completa da plataforma, nem a detalhes técnicos mais aprofundados sobre o seu funcionamento, a plataforma da WSC Sports serve como um exemplo muito mais limitado do que outros softwares tradicionais do meio, em que o acesso e conhecimento sobre a operação e a interface são muito mais difundidos e facilmente accessíveis |

### Análise C07 — Magnifi

**Autor(a):** Lucas Roberto Boccia dos Santos — 22.123.012-1  
**Tipo:** concorrente direto  
**Link oficial:** [Página do produto](https://www.magnifi.ai/product)  
**Data de acesso:** {{dd/mm/aaaa}}

#### Contexto e proposta

Analisar como a Magnifi recebe vídeos, gera e etiqueta cortes esportivos e permite baixar ou distribuir os resultados.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print                         | Observação de IHC |
| -------------- | ---------------- | --------------------------------------- | ----------------- |
| {{...}}        | {{...}}          | `../assets/02_concorrencia/magnifi/...` | {{...}}           |

#### Experiência do usuário e opiniões

{{avaliações, relatos, estudos ou teste próprio com fonte identificável}}

#### Padrões e tendências percebidos

{{...}}

#### Pontos positivos, limitações e lições

| Ponto   | Evidência | Implicação para nosso projeto |
| ------- | --------- | ----------------------------- |
| {{...}} | {{...}}   | {{...}}                       |

> Preencha cada análise com evidências próprias, fontes identificáveis e prints legíveis antes de transformar os templates em conclusões.

## 3. Softwares que o público-alvo usa no cotidiano

Analise interfaces que moldam a expectativa do público, mesmo que não sejam concorrentes.

| Software           | Por que o público usa                           | Padrões relevantes                                                   | Prints   | O que aprender                                                                |
| ------------------ | ----------------------------------------------- | -------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------- |
| Adobe Premiere Pro | Importar, organizar, recortar e exportar vídeos | Player, biblioteca de mídia, marcadores, linha do tempo e exportação | Pendente | Empregar termos e controles familiares aos editores de vídeo                  |
| DaVinci Resolve    | Organizar, editar e exportar vídeos             | Player, biblioteca de mídia, metadados, linha do tempo e exportação  | Pendente | Apresentar arquivos e resultados de forma visual e organizada                 |
| CapCut             | Realizar edições e exportações de vídeo         | Player, miniaturas, linha do tempo e exportação                      | Pendente | Manter as tarefas principais acessíveis e reduzir a complexidade da interface |
| Final Cut Pro      | Organizar, editar e exportar vídeos             | Player, biblioteca de mídia, marcadores, linha do tempo e exportação | Pendente | Facilitar a localização, seleção e manipulação de trechos                     |
| cap.so             | Editar e apresentar vídeos                      | Player, pré-visualização e exportação                                | Pendente | Oferecer pré-visualização clara antes de baixar ou exportar resultados        |

> A familiaridade do público com esses softwares e padrões ainda deve ser validada, conforme a hipótese H17 da Entrega 1.

## 3.1 Padrões de interface relevantes ao escopo de IHC

Registre somente padrões encontrados nas soluções analisadas e que possam ter relação com objetivos reais da equipe.

| Padrão observado         | Produto(s) | Para qual tarefa serve | Vantagem percebida | Risco/limitação | Aplicável ao nosso escopo? |
| ------------------------ | ---------- | ---------------------- | ------------------ | --------------- | -------------------------- |
| dashboard                | {{...}}    | {{...}}                | {{...}}            | {{...}}         | sim/não/talvez             |
| relatório                | {{...}}    | {{...}}                | {{...}}            | {{...}}         | {{...}}                    |
| histórico + filtros      | {{...}}    | {{...}}                | {{...}}            | {{...}}         | {{...}}                    |
| administração/CRUD       | {{...}}    | {{...}}                | {{...}}            | {{...}}         | {{...}}                    |
| comparação de resultados | {{...}}    | {{...}}                | {{...}}            | {{...}}         | {{...}}                    |

> O objetivo não é concluir “todo concorrente tem dashboard, então teremos um”. O padrão só será adotado se apoiar uma tarefa rastreável.

## 4. Síntese comparativa da equipe

| Critério                      | C01 | C02 | C03 | Oportunidade para o projeto |
| ----------------------------- | --- | --- | --- | --------------------------- |
| Navegação                     |     |     |     |                             |
| Feedback/estado               |     |     |     |                             |
| Prevenção/recuperação de erro |     |     |     |                             |
| Terminologia                  |     |     |     |                             |
| Acessibilidade                |     |     |     |                             |
| Eficiência                    |     |     |     |                             |

## 5. Recomendações derivadas

Liste recomendações com origem explícita.

- **RC01:** {{recomendação}} — derivada de {{C01/C02/evidência}}.
- **RC02:** {{...}}

## Referências

{{fontes dos produtos, avaliações e literatura}}

## Checklist

- [ ] O mapa inicial de alternativas da Entrega 1 foi revisitado e aprofundado.
- [ ] Hipóteses relevantes sobre mercado/padrões foram atualizadas na rastreabilidade quando surgiram evidências.
- [ ] Há pelo menos uma análise completa por integrante.
- [ ] Cada análise contém prints legíveis da interface.
- [ ] Prints mostram telas/estados relevantes, não apenas logos/homepage.
- [ ] Foram analisados concorrentes e/ou interfaces representativas ao público.
- [ ] Em TCC sem interface original, foram investigadas ferramentas profissionais análogas às atividades do usuário escolhido.
- [ ] Padrões como dashboard, relatório, filtros e CRUD foram analisados como soluções para tarefas, não como requisitos automáticos.
- [ ] Opiniões de UX têm fonte.
- [ ] A síntese compara critérios comuns e produz recomendações.
- [ ] Não há “copiar porque o concorrente faz”; há justificativa de adequação ao público/contexto.
