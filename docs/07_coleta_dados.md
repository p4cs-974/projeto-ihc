# Entrega 7 — Coleta de dados, necessidades e aspectos éticos

**Data:** 25/10/2026\
**Status:** planejamento e instrumentos textuais preenchidos; configuração em ferramentas on-line, piloto e coleta pendentes\
**Responsabilidade:** mapeamento geral da Equipe 16 e instrumentos individuais

| Integrante | Matrícula | Técnica elaborada |
|---|---|---|
| Pedro Alexandre Custódio Silva | 22.123.049-3 | I01 — Entrevista semiestruturada |
| Lucas Roberto Boccia dos Santos | 22.123.012-1 | I02 — Questionário |
| Giovanni Chahin Morassi | 22.123.025-3 | I03 — Brainstorming de necessidades e desejos dos usuários |

## Objetivo da atividade

Planejar a investigação de como editores esportivos e criadores amadores selecionam lances de partidas encerradas, quais dificuldades encontram e quais informações precisam para continuar a edição em ferramentas externas. Investigar também como responsáveis editoriais recebem e avaliam esse material. A coleta deverá verificar a plausibilidade do recorte de IHC derivado do TCC, em vez de assumir que enviar, acompanhar, consultar e baixar já são práticas ou necessidades comprovadas.

A contribuição técnica prevista é identificar melhores momentos e produzir cortes com metadados. O recorte de IHC permanece uma aplicação potencial: preparar gravações, acompanhar o processamento, revisar candidatos e obter arquivos para continuidade externa. Edição detalhada, montagem, publicação e chancela editorial continuam fora da interface. Reconhecimento automático de jogadores não é capacidade assegurada do TCC.

**Natureza deste documento:** todos os tamanhos de amostra, durações e procedimentos abaixo são propostas de aplicação. Não há respostas de participantes, entrevistas realizadas ou ideias de brainstorming coletadas nesta entrega. A sessão de U01 em 22/10/2026 pertence à Entrega 6 e não valida o contexto de trabalho de editores.

## Fundamentação e contexto recuperado

| Fonte | Orientação utilizada nesta entrega |
|---|---|
| [CC8122 — Identificação de Necessidades — A](../slides_plinio/CC8122-Identificacao%20Necessidades-A.pdf), slides 2–7 | Investigar cinco dimensões: o próprio usuário, relação com tecnologia, conhecimento do domínio, conhecimento das tarefas e motivações/valores. O mapeamento geral da Parte A explicita essas dimensões para orientar os três instrumentos. |
| Mesmo material, slides 8–13 | Incluir usuários e stakeholders; identificar quem usa, quem é afetado, quem decide objetivos/funcionalidades e quem define os processos; tratar autonomia, benefícios, riscos, justiça, consentimento e privacidade. |
| [CC8122 — Identificação de Necessidades — B](../slides_plinio/CC8122-Identificacao%20Necessidades-B.pdf), slides 3–9 | Entrevista para profundidade, com entrevistador preparado; questionário para respostas comparáveis, combinando perguntas fechadas e abertas, sem ambiguidades ou indução. |
| Mesmo material, slide 12 | Brainstorming com 8 a 12 usuários, moderador, geração individual seguida de coletiva e ausência de censura durante a geração. O foco é levantar necessidades e desejos. |
| Mesmo material, slides 20–21 | Escolher método e amostra conforme o objetivo e fornecer protocolo reproduzível. Entrevista e questionário devem utilizar ferramenta on-line; a cópia textual e as configurações estão abaixo, mas a criação dos formulários ainda está pendente. |
| [Entrega 1](01_conhecendo_o_problema.md) e [rastreabilidade](../RASTREABILIDADE.md) | Hipóteses H01–H29, refinamentos H30–H42 e lacunas sobre público, atividades, acessibilidade e contexto; nenhuma será convertida em fato pelo planejamento. |
| [Entrega 2](02_analise_concorrencia.md) | Padrões e recomendações RC01–RC12 são referências para investigação; existência de um recurso em concorrente não comprova necessidade ou compreensão pelo nosso público. |
| [Entrega 3](03_personas_contexto_jornada.md) e [Entrega 4](04_cenarios_problema.md) | P01/Rafael e P03/Jorginho Jr. são proto-personas primárias; P02/Arnaldo é persona atendida por resultados recebidos externamente. C01–C03 descrevem problemas hipotéticos. Não recrutar pessoas para que reproduzam essas biografias. |
| [Entrega 5](05_analise_tarefas.md) | T01: localizar, selecionar e revisar; T02: supervisão editorial externa; T03: acompanhar processamento e tratar falhas. A01 é a entrada de envio; A03/histórico ainda depende de investigação e modelagem própria. |
| [Entrega 6](06_prototipacao_papel.md), seções 4–5 | U01, sem experiência em edição, precisou de orientação e declarou dúvidas sobre conclusão, rótulos, tempos e obtenção de arquivos. Esses pontos motivam perguntas de compreensão, sem estabelecer preferência profissional por uma visualização. |

## Hipóteses e lacunas prioritárias herdadas do projeto

A evidência atual é documental, salvo o walkthrough limitado de U01. Os agrupamentos preservam os IDs originais; não representam novas hipóteses nem resultados de coleta.

| IDs | Hipótese/lacuna | Evidência atual | Decisão que depende da resposta | Prioridade |
|---|---|---|---|---|
| H01, H09, H10, H11 | Seleção manual extensa, omissões involuntárias e retrabalho sob prazo | Processo e cenários hipotéticos, sem relatos do público | Qual problema apoiar e em que etapa; distinguir descarte editorial de omissão | Alta |
| H03, H06, H12, H21, H27, H28 | Editor esportivo como usuário e obtenção de cortes para pós-produção como objetivo | Recorte escolhido pela equipe | Manter ou refinar público, contexto e finalidade da interface | Alta |
| H02 | Automação reduziria tempo, esforço e retrabalho | Benefício esperado, sem medição comparativa | Definir benefício a avaliar posteriormente; esta coleta não demonstra ganho real | Alta |
| H05, H17, H19, H34, H38 | Familiaridade com edição, programação, IA e vocabulário varia entre perfis | Padrões observados em ferramentas; características de personas não validadas | Linguagem, ajuda e abstração de parâmetros técnicos | Alta |
| H07, H08, H24, H39 | Frequência da revisão, criticidade do envio, entradas e volume de partidas | Quantidades narrativas e prioridades provisórias | Lote, validação das entradas e ordem de prioridades | Alta |
| H13, H16, H25, H26, H32, H41 | Espera, falhas, interrupções e retomada afetam o trabalho | Hipóteses; U01 teve dúvida ao concluir a análise simulada | Informações de estado, recuperação localizada, conclusão e continuidade | Alta |
| H14, H22, H23, H33, H40 | Editor entrega material a um responsável que decide externamente | Fluxo organizacional hipotético | Identificação de arquivos e passagem de material; investigar papéis sem criar área administrativa | Alta |
| H30 | Revisar candidatos extras pode ser preferível a omitir lances relevantes | Preferência atribuída à proto-persona P01 | Esforço de conferência e comunicação dos limites da detecção | Alta |
| H36, H37 | Compilados por atleta e equipamento/armazenamento limitados podem restringir P03 | Hipóteses; identificação automática de atleta não confirmada | Adequação dos melhores momentos gerais e viabilidade do fluxo local/remoto | Alta |
| H15, H29 | Histórico e visão geral ajudariam a consultar resultados e andamento | Propostas sem tarefa atual comprovada; base do protótipo é do lote atual | Se precisam existir e quais decisões/informações justificariam cada recurso | Média |
| H31, H42 e lacuna de acessibilidade | Iluminação, rotina, equipamentos compartilhados e barreiras de interação | Características fictícias; necessidades de acessibilidade desconhecidas | Legibilidade, operação por teclado e continuidade entre sessões | Média |
| H04, H18, H20, H35 | Adoção, barreiras de acesso e eventual recuperação de decisões editoriais | Materiais de concorrência e hipóteses organizacionais | Investigar quem escolhe ferramentas e se registros externos bastam; sem fechar mercado ou auditoria | Média |

## Parte A — Necessidades e requisitos de IHC

O mapeamento geral orienta os três instrumentos da Parte B: I01 — entrevista semiestruturada, I02 — questionário e I03 — brainstorming. A entrevista aprofunda experiências e decisões, o questionário permite comparar práticas na amostra e o brainstorming amplia necessidades e desejos. As cinco dimensões abaixo constituem uma base comum, explorada conforme a finalidade de cada técnica.

### Que dados coletar?

| Dimensão dos slides A | Dados/informações | Hipóteses/lacunas relacionadas | Por que são necessários | Decisões de design que podem afetar |
|---|---|---|---|---|
| O próprio usuário | Papel na produção, atuação profissional/amadora, experiência, formas de aprender, vocabulário e ajustes de leitura ou operação informados voluntariamente | H03, H19, H21, H27, H42; acessibilidade | Distinguir quem executa, recebe e decide, caracterizando os perfis pela atividade real | Rótulos, instruções, ajuda, navegação e acessibilidade |
| Relação com tecnologia | Ferramentas, dispositivos, obtenção e armazenamento de gravações, conexão, ambiente de trabalho e familiaridade com automação, programação e IA | H05, H13, H17, H24, H31, H37, H38 | Verificar condições de uso e restrições, sem presumir infraestrutura ou conhecimento técnico | Preparação e transferência de arquivos, validações, apresentação e abstração de parâmetros |
| Conhecimento do domínio | Finalidades da seleção, critérios de relevância, contexto anterior/posterior e diferenças entre melhores momentos gerais e compilados por atleta | H10, H11, H25, H28, H30, H36 | Compreender o julgamento editorial e a adequação dos resultados às finalidades reais | Prévia, contexto, identificação dos trechos e comunicação dos limites da seleção |
| Conhecimento das tarefas | Fluxo atual, volume e prazos, seleção e conferência, esperas, erros e consequências, interrupções, retomada, consulta a trabalhos anteriores e entrega de arquivos | H01, H07, H08, H09, H14, H15, H16, H23, H24, H25, H26, H29, H32, H39, H40, H41 | Identificar necessidades ligadas a situações concretas, distinguindo frequência, gravidade e ausência de dificuldade | Refinar T01/T02/T03, estados, recuperação e continuidade externa; justificar ou dispensar histórico e visão geral |
| Motivações e valores | Critérios de sucesso, satisfação, autonomia, confiança em sugestões, limites de revisão, benefícios esperados, disposição para aprender e fatores de adoção, escolha e pagamento de ferramentas | H02, H06, H18, H20, H28, H30, H31 | Distinguir desejos e expectativas de necessidades vinculadas ao trabalho, sem presumir ganho de produtividade | Priorização, controle editorial, ajuda inicial e comunicação das limitações |

### De quem coletar?

O critério comum é ter 18 anos ou mais e experiência na atividade indicada nos últimos seis meses. As proto-personas orientam a diversidade de perfis, sem exigir suas biografias, idades fictícias ou equipamentos específicos.

| Perfil/stakeholder | Experiência necessária | Relação com o projeto e participação |
|---|---|---|
| Editor profissional de futebol | Ter selecionado ou recortado lances de partidas encerradas, com fluxo manual ou automatizado | Usuário potencial associado a P01; participa de I01, I02 e I03 |
| Criador amador de futebol | Ter preparado seleções de lances, inclusive com ferramentas simples/mobile, produção própria ou remuneração ocasional | Usuário potencial associado a P03; participa de I01, I02 e I03 |
| Supervisor, produtor ou editor-chefe | Ter recebido e avaliado seleções de lances | Stakeholder associado a P02, com decisão externa à interface; participa de I01. Quem apenas supervisiona ou assiste a futebol não integra o público de I02/I03 |

**Quem usa?** Editores e criadores são usuários potenciais, a confirmar pela investigação. 
**Quem é afetado?** Responsáveis editoriais, organizações, destinatários dos cortes e pessoas identificáveis nas gravações, sem necessidade de coletar seus nomes ou imagens.
**Quem decide objetivos e funcionalidades?** Investigar quem determina a finalidade editorial e autoriza ou escolhe ferramentas; a equipe traduz os achados em decisões de projeto e verifica a viabilidade técnica após a coleta. **Quem definiu os processos?** Identificar se o fluxo foi estabelecido pelo próprio editor, pela supervisão ou pela organização, preservando diferenças entre contextos.

### Aspectos éticos e gestão dos dados

Os cuidados comuns estão definidos no protocolo abaixo. Na entrevista, solicitar relatos sem identificar terceiros ou expor materiais confidenciais, em conversa individual sem superior acompanhando. No questionário, não solicitar identificadores pessoais nem exigir login ou coleta automática de e-mail; desidentificar textos livres antes da divulgação. No brainstorming, combinar confidencialidade, evitar relações de chefia direta e permitir que a pessoa não fale, vote ou justifique sua experiência; a geração de ideias não terá críticas nem julgamentos de competência ou viabilidade. Não é possível garantir o sigilo pelos demais participantes.

#### Protocolo comum aos três instrumentos

Os princípios de autonomia, não maleficência, beneficência e justiça apresentados nos slides A são traduzidos nas medidas abaixo. Trata-se de planejamento acadêmico; não se afirma que houve consentimento, aprovação institucional ou coleta. Antes da aplicação, os responsáveis deverão conferir com o docente as exigências institucionais e ajustar o [modelo de consentimento](../instrumentos/termo_consentimento_modelo.md) ao protocolo.

| Aspecto | Medida prevista neste projeto |
|---|---|
| Voluntariedade e autonomia | Convite sem obrigação acadêmica ou profissional, com possibilidade de pular perguntas, fazer pausa ou desistir sem justificativa. Não recrutar subordinados por ordem de gestores. Restringir este planejamento a adultos. |
| Benefícios e ônus | Benefício esperado indireto: compreender melhor a seleção de lances. Não prometer aumento de produtividade, precisão do modelo ou benefício individual. Informar a duração e combinar horário que não prejudique a produção. |
| Riscos e minimização | Possível constrangimento ao relatar erro, cobrança ou dificuldade; não avaliar desempenho individual. Não coletar salário, diagnósticos, credenciais, material sigiloso nem dados de jogadores. Perguntar sobre ajustes de interação, sem exigir condição médica. |
| Consentimento | Apresentar objetivo, procedimento, registros, acesso, divulgação e descarte antes do aceite. I01/I03 usam registro separado com código do participante, data e aceite; I02 usa aceite inicial. Sem aceite, não coletar respostas de pesquisa. |
| Gravação | Somente I01 admite áudio opcional, mediante autorização específica. Não gravar vídeo/tela. I02 não grava; I03 usa cartões/notas. Recusa de áudio em I01 não impede a participação. |
| Privacidade | Códigos ENT-01… para entrevista e BRA-01… para brainstorming; QUE-01… atribuídos na exportação do questionário. Contatos de agendamento e registros de consentimento ficam separados das respostas. Notas com códigos ainda podem permitir associação e serão tratadas como confidenciais. |
| Divulgação | Publicar apenas síntese, contagens e trechos desidentificados. Remover nomes e combinações que revelem empregador/canal ou episódio reconhecível; agregar ou suprimir grupos muito pequenos. Não subir áudio, consentimentos, contatos ou respostas brutas ao Git público. |
| Armazenamento e acesso | Pasta privada da equipe em conta institucional, acesso nominal somente aos três integrantes. Desativar link público dos formulários de registro/quadro e do painel de respostas. Compartilhar com o docente preferencialmente a síntese desidentificada. |
| Retenção e descarte | Apagar áudio após conferir a transcrição, em até 30 dias da sessão. Apagar contatos após encerrar o agendamento/retornos. Excluir respostas brutas, cartões, transcrições e consentimentos até 90 dias após o encerramento da disciplina, incluindo cópias locais e lixeira sob controle da equipe. Conservar no repositório somente sínteses desidentificadas. |
| Retirada após participar | Em I01/I03, informar o código privadamente para solicitar retirada ao responsável que enviou o convite, até a consolidação da síntese, prevista em até 30 dias da sessão. Após agregação, pode não ser possível separar uma contribuição. Em I02, sem identificador de vínculo, pode não ser possível localizar uma resposta já enviada; informar isso antes do aceite. |
| Justiça e acessibilidade | Oferecer material legível, tempo de pausa e possibilidade de ditar respostas/cartões a um facilitador, registrando a adaptação. Identificar barreiras de acesso ao método; não excluir uma pessoa por pouca habilidade com ferramentas digitais. |

#### Texto comum de apresentação e consentimento

> Somos a Equipe 16 da disciplina de Interação Humano-Computador da FEI. Estamos estudando como pessoas selecionam lances de partidas de futebol encerradas e preparam esse material para edição ou avaliação posterior. Queremos compreender o processo; sua habilidade profissional não está sendo avaliada. A participação é voluntária, você pode deixar perguntas sem resposta ou parar a qualquer momento, sem prejuízo. Não informe nomes de clientes/colegas, credenciais ou conteúdo confidencial. Somente os três integrantes terão acesso aos registros brutos; a divulgação acadêmica usará dados agrupados ou trechos sem identificação. Os registros serão descartados até 90 dias após o encerramento da disciplina. Você pode pedir esclarecimentos ao integrante responsável pelo convite. Não há benefício individual garantido.

O responsável acrescentará antes do aceite a descrição específica:

- **I01:** conversa individual de cerca de 40–50 minutos, registrada por notas; áudio somente se autorizado separadamente, apagado em até 30 dias. Será enviado um código para solicitar retirada antes da consolidação da síntese, em até 30 dias da sessão.
- **I02:** formulário direto, sem nome ou e-mail solicitado. Você pode sair antes de enviar; sem identificador de vínculo, talvez não seja possível localizar e retirar sua resposta depois do envio. A plataforma pode manter registros técnicos próprios, que a equipe não publicará nem usará para identificar você.
- **I03:** encontro de aproximadamente 75 minutos com 8 a 12 pessoas, com cartões/notas e sem gravação. Pediremos a todos que preservem o sigilo, mas não podemos garantir confidencialidade por parte dos demais. Você receberá um código para solicitar retirada antes da consolidação da síntese; ideias já combinadas no grupo podem não ser separáveis.

## Parte B — Ferramentas de coleta

Cada integrante elaborou uma técnica distinta. A entrevista aprofunda práticas e decisões, o questionário descreve diferenças na amostra e o brainstorming amplia o conjunto de necessidades e desejos. Não se usarão números de ideias como medida de prevalência nem preferências declaradas como prova de desempenho.

### Instrumento I01 — Entrevista semiestruturada

**Autor:** Pedro Alexandre Custódio Silva — 22.123.049-3\
**Objetivo:** reconstruir episódios de produção e entender critérios de seleção, esforço, falhas, contexto e transferência de material antes de discutir a aplicação potencial.\
**Público/amostra pretendida:** oito adultos por conveniência com variação de experiência: quatro editores profissionais, dois criadores amadores e dois responsáveis editoriais. Meta exploratória, sem representatividade estatística ou alegação prévia de saturação.\
**Duração:** 40–50 minutos por entrevista.\
**Modalidade e ferramenta planejadas:** encontro individual presencial ou por chamada on-line; roteiro e formulário de registro no Google Forms ou ferramenta institucional equivalente. O formulário de notas será preenchido pelo entrevistador e terá acesso restrito. A entrevista permanece uma conversa, não um questionário autoadministrado.\
**Situação da ferramenta:** formulário ainda não criado; este documento contém o roteiro integral e a especificação de registro.

#### Procedimento padronizado de aplicação

1. **Preparar e recrutar:** confirmar maioridade e atuação nos últimos seis meses sem pedir prova documental; agendar por canal separado das respostas. Não exigir vínculo com empresa específica. Ler o protocolo e ensaiar com um colega da equipe para evitar indução; o ensaio não contará como entrevista do público.
2. **Fazer um piloto:** aplicar a uma pessoa elegível, conferir compreensão, sequência e duração e registrar ajustes de versão. Se o instrumento mudar de forma relevante, não juntar o piloto à análise principal sem explicitar a diferença.
3. **Apresentar e obter consentimento, 5 min:** ler o texto comum e a descrição I01; registrar código, aceite e decisão sobre áudio em arquivo separado. Não iniciar registro de áudio antes da autorização. Confirmar local reservado e possibilidade de pausa.
4. **Investigar a prática atual, 25–30 min:** seguir E01–E09. Perguntar primeiro de forma aberta; usar sondagens somente após a resposta, sem presumir dificuldades ou exemplos das personas. Anotar respostas e perguntas puladas. Para supervisores, usar a adaptação indicada no roteiro.
5. **Explorar a aplicação potencial, 8–10 min:** apresentar somente a descrição neutra antes de E10–E12. Não demonstrar telas nem antecipar nomes de funcionalidades. Registrar separadamente relato de experiência, opinião e expectativa hipotética.
6. **Encerrar, 3–5 min:** perguntar E13, resumir o entendimento e permitir correção. Relembrar código, contato para retirada e prazos de descarte. Agradecer sem prometer implantação das sugestões.
7. **Tratar os registros:** desidentificar notas e transcrição, conferir fidelidade ao áudio quando autorizado e armazenar em pasta privada. Publicar apenas síntese; registrar data, versão, perfil, duração real, desvios e ajuda oferecida.

#### Roteiro integral

As perguntas principais são obrigatórias no roteiro, mas a pessoa pode não responder. As sondagens são apoios opcionais; não ler uma lista de exemplos como se todos precisassem ocorrer. Ao ouvir uma generalização, pedir um caso recente: “Pode contar como foi da última vez?”. Não corrigir o vocabulário durante o relato.

| ID | Pergunta principal | Sondagens neutras e adaptações | Relação com o projeto |
|---|---|---|---|
| E01 | Qual é sua participação na preparação de vídeos de futebol e há quanto tempo faz esse trabalho? | O que faz pessoalmente e o que cabe a outras pessoas? Como aprendeu? Profissional, amador ou supervisão? | Público; H03/H21/H27/H38/H42 |
| E02 | Conte como foi o último trabalho com lances de uma partida encerrada, do recebimento do material até a entrega. | O que precisava entregar, para quem e com qual prazo? Quantas partidas havia? Para supervisores: do recebimento da seleção até a decisão e devolutiva. | Processo atual; H01/H11/H12/H14/H28/H39 |
| E03 | Que ferramentas e equipamentos utilizou em cada etapa? | Como obteve a gravação? Veio inteira ou por tempos/arquivos? Onde guardou entradas e saídas? Houve alguma limitação? Que contato tem com automação, programação ou IA? | Tecnologia; H05/H13/H17/H24/H37/H38 |
| E04 | Como decidiu quais lances eram relevantes e onde cada trecho começava e terminava? | A finalidade mudou essa decisão? Que informações consultou? Houve seleção por atleta? O que precisou ver antes/depois? Para supervisores: o que fez aceitar ou devolver o trecho? | Julgamento editorial; H10/H11/H25/H28/H36 |
| E05 | O que foi simples e o que exigiu mais esforço nesse trabalho? | Em que etapa, com que frequência e por quê? Como conferiu se faltava algo? Se não houve problema, o que ajudou? | Problema; H01/H07/H09/H10/H39 |
| E06 | Houve algum erro ou interrupção? Como percebeu e o que fez depois? | O que precisou refazer? Qual foi a consequência? Já ocorreu algo mais grave em outra ocasião? Distinguir falha técnica, omissão involuntária e descarte deliberado. | Criticidade/retomada; H08/H16/H26/H41 |
| E07 | Como o material passou entre você e as outras pessoas envolvidas? | Quem definiu o processo e a finalidade? Como se reconhece a partida, o corte e a versão? Como voltam pedidos de ajuste? Se trabalha sozinho, como organiza essa passagem para o editor seguinte? | Supervisão externa; H14/H22/H23/H33/H34/H40 |
| E08 | Em que situações precisa voltar a um trabalho anterior ou conferir algo que ainda está em andamento? | Qual informação procura, que decisão toma e como resolve hoje? O que faz durante esperas? Quando e como precisa saber que pode continuar? Se nunca precisou, registrar. Para supervisores: precisa recuperar decisões antigas? | Histórico/espera, sem sugerir tela; H15/H29/H32/H35 |
| E09 | Como são o ambiente e as condições em que realiza esse trabalho? | Iluminação, interrupções, equipamento compartilhado e preferências de aprendizagem. Há algum ajuste de leitura, som ou operação que facilitaria sua participação ou trabalho, sem precisar explicar motivo médico? | Contexto/acessibilidade; H12/H13/H31/H37/H41/H42 |

**Descrição neutra para a segunda parte:** “O projeto investiga um sistema que recebe gravações de partidas encerradas e sugere cortes de possíveis melhores momentos acompanhados de informações sobre os trechos. A pessoa precisa conferir a seleção; sugestões podem estar incorretas ou incompletas. A edição detalhada e a publicação continuam em ferramentas externas. A identificação automática de jogadores não está assegurada.”

| ID | Pergunta principal | Sondagens neutras e adaptações | Relação com o projeto |
|---|---|---|---|
| E10 | Em que parte do trabalho que descreveu isso teria utilidade, se tivesse? Em que parte não ajudaria? | O que precisaria receber e conferir? O que ainda faria manualmente? O resultado serviria para a finalidade de sua última seleção? Para supervisores: o que precisaria receber do editor? | Plausibilidade/benefício esperado; H02/H06/H18/H25/H28/H33/H36 |
| E11 | Se uma seleção sugerida trouxesse lances sem interesse ou deixasse de fora lances importantes, como decidiria o que fazer? | O que muda sob prazo? O que torna a conferência inviável? Se quiser comparar, apresentar verbalmente dois casos sem números: candidatos extras e candidatos faltando. Alternar a ordem entre entrevistas. | Limites de revisão; H10/H16/H30 |
| E12 | O que pesaria na decisão de experimentar ou não esse apoio? | Quem escolhe/autoriza ferramentas? Quem arca com custos? Há restrições ao envio de gravações? Quanto treinamento aceitaria? Que palavras usaria para um trecho, seu momento e o arquivo recebido? | Adoção, privacidade e linguagem; H04/H05/H18/H19/H20/H24/H38 |
| E13 | O que não perguntamos e seria importante para entender seu trabalho? Nosso resumo descreve corretamente o que você quis dizer? | Permitir correção e registrar divergências; não pedir que confirme a solução da equipe. | Lacunas e conferência do entendimento |

#### Formulário de registro e análise

O formulário on-line de notas terá campos para código, data, versão, papel, modalidade, duração, E01–E13, sondagens usadas, desvios e observações do entrevistador. Consentimento e contato ficarão fora desse formulário. Cada anotação distinguirá **relato de episódio**, **expectativa sobre a proposta**, **fala literal conferida** e **interpretação da equipe**. Não preencher uma fala literal com uma paráfrase.

Pedro organizará trechos por temas: prática atual, relevância/contexto, volume/prazo, tecnologia, espera, falhas, transferência, linguagem, acessibilidade e adoção, admitindo temas novos. Outro integrante revisará a codificação e os casos que contradizem as hipóteses; registrarão divergências e sua resolução. Comparar P01/P03 e o recebimento externo por P02, preservando diferenças em vez de construir uma rotina média fictícia.

Cada conclusão deverá citar código e pergunta de origem e indicar se veio de episódio ou expectativa. Por exemplo de **regra de decisão**, e não resultado: se os relatos indicarem necessidade de reconhecer o material fora do produto, refinar identificação dos arquivos e RC09; se não houver tarefa de consulta anterior, H15 não estará sustentada pela amostra. Relatos sobre tempo não comprovam H02 como ganho efetivo: isso exige avaliação comparativa posterior com tarefas equivalentes.

### Instrumento I02 — Questionário

**Autor:** Lucas Roberto Boccia dos Santos — 22.123.012-1\
**Objetivo:** caracterizar práticas, condições, dificuldades e expectativas de editores profissionais e criadores amadores, comparando os perfis sem generalizar a amostra para todo o mercado.\
**Público/amostra pretendida:** pelo menos 20 respostas elegíveis, buscando cerca de dez profissionais e dez criadores amadores. Recrutamento por conveniência em contatos e comunidades de edição/futebol; a divisão é meta de diversidade, não cota representativa. Se não for alcançada, apresentar a quantidade real e o desequilíbrio.\
**Duração estimada:** 15–20 minutos, a conferir no piloto.\
**Ferramenta planejada:** Google Forms ou equivalente institucional, com navegação por seções e ramificação.\
**Situação da ferramenta:** formulário ainda não criado; o texto integral, os tipos de campo e as regras de navegação estão abaixo.

Link do questionário para preenchimento abaixo, inserido dentro do nosso guia de utilização do protótipo. O questionário está na parte inferior da página:

https://ihc.p4cs.com.br/guia/

### Instrumento I03 — Brainstorming de necessidades e desejos dos usuários

**Autor:** Giovanni Chahin Morassi — 22.123.025-3\
**Objetivo:** explorar livremente necessidades, informações e resultados desejados ao selecionar lances e dar continuidade ao trabalho, incluindo aspectos não previstos pelas hipóteses da equipe.\
**Público/amostra pretendida:** uma sessão com 8 a 12 usuários adultos, buscando equilíbrio entre editores profissionais e criadores amadores, sem relação de chefia direta entre participantes. Exigir experiência na atividade nos últimos seis meses; não exigir correspondência às biografias de P01/P03.\
**Duração:** aproximadamente 75 minutos.\
**Papéis:** Giovanni como moderador; outro integrante como relator, sem produzir ideias em nome dos usuários.\
**Modalidade/material:** presencial com cartões e painel, ou remota com quadro digital privado e chamada sem gravação; oferecer ditado de cartões quando necessário.\
**Situação:** protocolo e materiais textuais preparados; sessão não realizada.

#### Procedimento padronizado de aplicação

1. **Preparar:** recrutar usuários pelos critérios acima, verificar ausência de chefia direta e perguntar necessidades de participação sem solicitar diagnósticos. Preparar cartões vazios, códigos BRA-01…, relógio e ficha de registro. Não expor o protótipo, personas, hipóteses ou exemplos de funcionalidades. Treinar moderador e relator com ensaio interno que não contará como dado de usuários.
2. **Confirmar viabilidade da sessão:** planejar para 8 a 12 usuários, conforme os slides. Se comparecerem menos de oito, tentar reagendar; se a aplicação reduzida for a única opção, discutir a adaptação com o docente e registrar tamanho real, justificativa e limitação. Não completar a amostra com integrantes da equipe ou pessoas sem experiência como se fossem usuários.
3. **Acolher e obter consentimento, 10 min:** ler apresentação e descrição I03, registrar aceite individual separadamente e combinar confidencialidade. Explicar que não haverá gravação e que ninguém precisa falar sobre si ou nomear organização. Informar como sair ou pedir retirada de um cartão.
4. **Apresentar tema e regras, 5 min:** ler o enunciado neutro e as regras abaixo. Permitir esclarecimentos sobre a atividade, sem ensinar uma solução. Identificar somente o papel geral de cada participante.
5. **Gerar individualmente, 12 min:** cada pessoa anota necessidades/desejos em cartões, uma ideia por cartão, sem consultar os demais. Não impor quantidade mínima nem exigir que use as perguntas de apoio. Relator pode transcrever ditado literalmente e conferir com a pessoa.
6. **Gerar coletivamente, 23 min:** convidar cada pessoa a compartilhar uma ideia por rodada, podendo passar a vez. Abrir espaço para acrescentar, combinar e ampliar ideias. Adiar críticas, avaliação de custos e discussão de viabilidade. Registrar novas ideias e relações, preservando o cartão original.
7. **Esclarecer e agrupar, 15 min:** anunciar o fim da geração. Pedir explicações breves sem exigir defesa da ideia; agrupar por afinidade com rótulos sugeridos pelo grupo e permitir que um cartão permaneça isolado ou pertença a mais de um tema. Não apagar duplicatas ou divergências.
8. **Sinalizar relevância, 7 min:** cada participante pode indicar até três necessidades que mais afetam seu próprio trabalho, sem obrigação de usar todas as indicações. Perguntar que situação dá sentido à escolha. Essa etapa ocorre após a geração e não elimina ideias pouco votadas, especialmente barreiras de acessibilidade ou necessidades de um perfil minoritário.
9. **Encerrar e conferir, 3 min:** ler a síntese dos temas, perguntar se algo foi distorcido ou ficou ausente e relembrar retirada, contato e descarte. Não prometer funcionalidades. Agradecer e restringir o acesso ao quadro após a sessão.
10. **Tratar os registros:** o relator e Giovanni revisam cartões e notas, removem identificadores e separam ideias individuais, acréscimos coletivos e interpretação posterior. Guardar os originais em pasta privada e preparar uma síntese desidentificada para o repositório.

#### Enunciado integral de abertura

> Queremos levantar necessidades e desejos de quem prepara seleções de lances de partidas de futebol já encerradas. Pense no que precisa alcançar, compreender ou preservar ao receber as gravações, escolher trechos e continuar o trabalho ou entregar material a outra pessoa. Não há resposta certa. Pode trazer algo que funciona bem, algo que gostaria de melhorar ou uma necessidade que ainda não sabe como atender. Não precisa propor uma tela, aplicativo ou tecnologia. Primeiro cada pessoa escreverá suas ideias; depois ampliaremos o conjunto em grupo. Durante a geração não discutiremos se uma ideia é viável, cara, boa ou ruim.

#### Regras a manter visíveis

- Registrar uma ideia por cartão e usar palavras próprias; desenhos ou ditado também são aceitos.
- Buscar variedade e acolher ideias incomuns, sem censurar a si ou aos demais.
- Ouvir sem julgar; não corrigir a experiência de outra pessoa nem avaliar sua habilidade.
- Acrescentar ideias a partir das demais sem apagar diferenças de objetivo ou contexto.
- Falar uma pessoa por vez, com convite a quem ainda não participou e liberdade de passar a vez.
- Evitar nomes, dados de clientes e conteúdo protegido ou confidencial.
- Deixar custos, viabilidade e escolha de soluções para análise posterior da equipe.

#### Perguntas de apoio do moderador

Usar somente se o grupo precisar de estímulo, depois de dar tempo para ideias espontâneas. Não transformar a lista em rodada obrigatória de respostas. Registrar quais estímulos foram usados.

| ID | Estímulo aberto | Necessidade a explorar |
|---|---|---|
| B01 | O que você precisa saber ou ter disponível antes de começar uma seleção? | Entradas e condições de trabalho; H13/H24/H37 |
| B02 | O que torna um trecho útil para o tipo de material que você prepara? O que varia entre finalidades? | Relevância e contexto; H10/H11/H28/H36 |
| B03 | O que ajudaria a continuar o trabalho quando precisa esperar ou se afastar dele? | Espera, interrupções e retomada; H13/H32/H41 |
| B04 | Quando algo não sai como esperado, o que precisa compreender ou preservar para prosseguir? | Falhas e recuperação; H08/H16/H26 |
| B05 | O que precisa acompanhar os trechos quando você os abre em outra ferramenta ou entrega a alguém? | Continuidade externa; H22/H23/H25/H33/H40 |
| B06 | Quando precisa voltar a algo que já fez, que dúvida está tentando resolver? E quando isso não é necessário? | Necessidade de recuperação, sem pressupor histórico; H15/H29 |
| B07 | O que faria esse trabalho valer a pena, ficar mais compreensível ou exigir menos esforço para você? | Motivações, valores e aprendizagem; H02/H06/H18/H28/H38 |
| B08 | Que condições do seu ambiente ou dos seus recursos ainda não apareceram nesta conversa? | Barreiras e necessidades não previstas; H31/H37/H42 e acessibilidade |

**Intervenções padronizadas:** diante de crítica durante a geração, dizer “Vamos registrar a ideia e deixar a avaliação para depois”; diante de domínio da conversa, “Vamos abrir espaço para quem ainda não falou; você pode passar a vez”; diante de uma solução pronta, perguntar “Que necessidade essa ideia atende, e em que situação?”, preservando também a formulação original. Se surgir desejo de reconhecimento de jogador, registrá-lo sem confirmar capacidade técnica. Se surgir montagem/publicação, registrar a necessidade e marcar a relação com o escopo somente na análise posterior.

#### Ficha de cartão e de sessão

Cada cartão terá: **ID da ideia** (BN-001…), **código do participante**, **origem** (individual ou acréscimo coletivo), **texto original**, **situação/finalidade explicada**, **relações com outros cartões**, **tema após agrupamento** e **indicações de relevância**. IDs de ideias BN-… serão distintos dos IDs de estímulos B01–B08 e dos códigos de participantes. Não exigir que todos os campos sejam preenchidos durante a geração; o relator poderá completar contexto na fase de esclarecimento sem inventar informação.

A ficha da sessão registrará data, versão, modalidade, moderador/relator, quantidade e composição real do grupo, duração de cada etapa, adaptações de acessibilidade, estímulos usados, desvios, divergências e observações sobre participação. A ficha de consentimento ficará separada. Não inserir nomes em capturas do quadro; uma imagem do painel só será divulgada depois de desidentificada.

#### Como os dados serão analisados

Giovanni e o relator organizarão os temas preservando texto original e contexto, diferenciando **episódio/prática relatada**, **necessidade expressa**, **desejo** e **solução sugerida**. Uma ideia livre não comprova um comportamento; perguntar por um episódio ajuda a investigar sua relação com a prática, sem impor essa exigência durante a geração.

Para cada tema, registrar a necessidade, os perfis/contextos em que apareceu, divergências, ligação com hipóteses, informação ainda ausente e possível impacto no design. Quantidade de cartões e indicações de relevância servem para organizar a discussão, não para estimar prevalência. Ideias produzidas coletivamente não equivalem a várias confirmações independentes. Considerar possível influência de participantes mais experientes e do próprio moderador.

Necessidades relacionadas a busca por atleta, auditoria, histórico ou painel geral serão investigadas pela situação e decisão que apoiam; não serão convertidas automaticamente em funcionalidades. Verificar viabilidade com a equipe técnica depois da sessão. Preservar também ideias fora do recorte como achados a discutir, sem ampliar silenciosamente o compromisso do TCC ou da disciplina.

## Integração, decisões e rastreabilidade após a coleta

### Amostra, sequência e limites

A sequência planejada é pilotar os instrumentos, realizar entrevistas iniciais, aplicar o questionário e conduzir o brainstorming. Os instrumentos estão especificados nesta versão; alterações motivadas pelos pilotos ou por entrevistas deverão gerar nova versão documentada. Os três integrantes poderão apoiar a aplicação uns dos outros mantendo o protocolo e a autoria de elaboração indicada.

As metas de oito entrevistas, vinte respostas e um grupo de 8 a 12 usuários são propostas viáveis para investigação acadêmica exploratória, sem garantia de acesso ou saturação. Não somar participantes de técnicas diferentes como pessoas únicas se houver sobreposição. Não usar idade, rotina ou volume fictícios das personas como critérios de recrutamento.

Se o acesso a profissionais for insuficiente, registrar tentativas, canais, datas e perfis efetivamente alcançados e discutir com o docente uma adaptação metodológica. Especialistas próximos, literatura e participantes proxy deverão ser identificados como tais. O colega U01 da Entrega 6 não será reapresentado como editor ou evidência sobre produtividade profissional. Uma amostra só de colegas sem prática não permite concluir que o usuário e o contexto adotados foram validados.

Este conjunto coleta principalmente autorrelatos, opiniões e necessidades expressas. Não mede diretamente desempenho, frequência por observação, acessibilidade efetiva, qualidade da detecção ou compatibilidade de importação de arquivos. A conferência prática desses aspectos requer atividades posteriores com usuários e material autorizado, articuladas às Entregas 8 e 12–14.

### Síntese esperada e critérios de atualização das hipóteses

| Hipóteses | Evidência a procurar nos instrumentos | Critério para sustentar, refutar ou refinar | Artefato/decisão a revisar |
|---|---|---|---|
| H01/H09/H10/H11 | E02/E04–E06; Q08/Q09/Q16/Q17; B02/B04 | Episódios de esforço e omissão podem sustentar o problema no contexto relatado; processos já resolvidos ou outras dores podem refinar ou contrariar sua centralidade. Descarte editorial não será contado como erro. | Problema da Entrega 1 e C01/C03 |
| H03/H06/H12/H21/H27/H28 | E01/E02/E10; Q02/Q03/Q07/Q21; B01/B02/B05 | Atividade e objetivo reais compatíveis sustentam o recorte apenas nos perfis/contextos alcançados. Se os resultados gerais não servirem à finalidade ou a atividade não existir, refinar público/objetivo. | P01/P03, contexto e escopo de IHC |
| H02 | E05/E10/E12; Q23–Q26; B07 | Registrar benefício desejado e condições para avaliá-lo; manter o ganho efetivo em aberto até comparação com tarefas equivalentes. Intenção de uso não confirma redução de tempo. | Critérios de avaliação nas Entregas 8 e 12–14 |
| H05/H17/H19/H34/H38 | E01/E03/E07/E12; Q10/Q11/Q27; B05/B07 | Comparar ferramentas, termos espontâneos e formas de aprendizagem; diferenças entre perfis refinam a linguagem. Não inferir compreensão só porque o termo existe em concorrente. | RC06/RC07, ajuda e representação dos resultados externos |
| H07/H08/H24/H39 | E02/E03/E05/E06; Q05/Q06/Q09/Q15–Q17; B01/B04 | Frequência de repetição e consequência de falhas podem mudar prioridades; volume real pode contrariar quatro a seis partidas/dia. Investigar entradas por partida, tempo ou outro arquivo. | A01, RC02 e prioridades de T01/T03 |
| H13/H16/H25/H26/H32/H41 | E03/E06/E08/E09; Q13/Q16–Q21; B03/B04 | Episódios de espera, retomada e falha refinam estados e informações; ausência de necessidade de aviso ou retomada evita pressupor o recurso. Capacidade técnica de recuperar continua verificação separada. | RC03/RC05, T03 e continuidade para T01 |
| H14/H22/H23/H33/H40 | E02/E07/E08/E10 com editor e supervisor; Q21/Q22; B05 | Descrever quem recebe, decide e devolve, por qual canal. Divergências entre relatos refinam a passagem; uso direto de P02 exige tarefa fundamentada antes de rever o recorte. | T02 externo, identificação dos arquivos e RC09 |
| H30 | E04/E11; Q25; B02/B07 | Registrar em que finalidades/prazos candidatos extras ou omissões são toleráveis; respostas condicionais refinam a hipótese, sem afirmar cobertura completa. | Revisão de T01 e comunicação de limites |
| H36/H37 | E03/E04/E10; Q07/Q08/Q12/Q13/Q26; B01/B02/B08 | Separar demanda por atleta da capacidade de atendê-la. Identificar espaço para originais, cortes e edição externa; processamento remoto não comprova economia de disco. | Adequação de P03 e viabilidade a discutir com a equipe técnica |
| H15/H29/H35 | E08, inclusive supervisores; Q19; B06 | Sustentar somente quando houver situação e decisão que exijam recuperação/visão geral; registros externos suficientes ou ausência de tarefa podem refinar/refutar a necessidade. Histórico técnico e auditoria editorial são distintos. | A03 a modelar se justificada; H35 continua exploratória |
| H31/H42 e acessibilidade | E01/E09; Q04/Q12–Q14/Q18; B08 | Refinar condições de uso pela rotina real e barreiras relatadas, sem buscar confirmar 19 anos ou modo escuro por princípio. Preferência não substitui avaliação de legibilidade. | Contexto, apresentação e avaliação futura de acessibilidade |
| H04/H18/H20 | E07/E10/E12, inclusive supervisores; Q22/Q26; B07 | Esclarecer papéis de adoção, restrições e benefícios esperados; não declarar redução de custos, comprador confirmado ou mercado validado com essa amostra. | Stakeholders e limites de adoção da Entrega 1 |

Após a coleta, construir uma tabela de achados com os campos **ID do achado**, **fonte/código e item do instrumento**, **contexto/perfil**, **relato ou expectativa**, **evidências convergentes/contrárias**, **limitação**, **hipótese afetada**, **estado proposto** e **decisão de design**. Não preencher agora achados hipotéticos como resultados.

Na consolidação, considerar **sustentada no contexto investigado** quando houver evidência pertinente à afirmação e limites explícitos; **refutada nesse contexto** quando evidências pertinentes a contrariarem; **refinada** quando a afirmação precisar de condições, perfis ou termos mais precisos; e **aberta** quando a evidência for insuficiente ou contraditória sem resolução. Para afirmações de desempenho, opiniões não bastam. Não usar maioria simples de técnicas ou contagem de ideias como regra automática de validação.

Preservar o histórico em [RASTREABILIDADE.md](../RASTREABILIDADE.md), acrescentando data, origem e consequência somente depois de analisar os dados. Atualizar personas, cenários, tarefas e recomendações quando uma conclusão justificar mudança; registrar pendências técnicas separadamente. O planejamento desta entrega não altera o estado empírico atual das hipóteses.

## Síntese

A entrevista de Pedro busca a profundidade necessária para reconstruir o trabalho e as decisões editoriais. O questionário de Lucas descreve a variedade de práticas e restrições na amostra. O brainstorming de Giovanni amplia necessidades e desejos sem começar pelo desenho das telas. O conjunto prioriza verificar quem realiza a atividade, o que considera um resultado útil, que dificuldades enfrenta e como os arquivos precisam continuar o fluxo externo.

Os instrumentos deverão reduzir as lacunas que sustentam o recorte de envio, acompanhamento, revisão e obtenção, permitindo confirmar sua plausibilidade em contextos delimitados ou revisá-lo. O roteiro de análise acima explicita quais hipóteses poderão ser sustentadas, refutadas ou refinadas. Ganho efetivo de produtividade, qualidade da detecção, identificação de jogadores e capacidade técnica de recuperação permanecem dependentes de outras evidências.

## Checklist

- [x] Hipóteses/lacunas prioritárias da Entrega 1 e refinamentos posteriores foram revisitados.
- [x] A coleta planejada investiga a plausibilidade do usuário, tarefa e contexto derivados do TCC técnico.
- [x] Perguntas não pressupõem dashboard, histórico, filtros, relatórios ou auditoria como necessários.
- [x] Cada dimensão de dados responde a uma dúvida concreta e indica uma decisão possível.
- [x] Parte A reúne o mapeamento geral das cinco dimensões dos slides e dos perfis/stakeholders para os três instrumentos.
- [x] Aspectos éticos são contextualizados, com consentimento, gravação opcional, acesso e descarte.
- [x] Há uma técnica completa por integrante, com nome e matrícula, e técnicas distintas.
- [x] Questionário está incluído entre as técnicas.
- [x] Cada instrumento possui objetivo, público, amostra pretendida, procedimento e conteúdo integral.
- [x] Questionário informa alternativas, tipos de campo, obrigatoriedade e lógica de triagem.
- [x] Brainstorming prevê 8 a 12 usuários, geração individual seguida de coletiva e ausência de censura na geração.
- [x] Perguntas evitam indução, admitem ausência de necessidade e coletam apenas dados pertinentes.
- [x] Está definido como analisar, triangular e usar os dados no design, preservando limitações.

## Histórico de revisões

| Data | Descrição | Responsabilidade |
|---|---|---|
| 25/10/2026 | Preenchimento das soluções individuais, protocolo ético, entrevista de Pedro, questionário de Lucas, brainstorming de Giovanni e plano de análise, com base nos slides A/B e nas Entregas 1–6. Instrumentos não aplicados; ferramentas on-line e pilotos pendentes. | Autoria por integrante indicada nas partes A/B; elaboração documental assistida pelo Codex a pedido da equipe |
| 29/10/2026 | Consolidação de A01, A02 e A03 em um mapeamento geral na Parte A, com dados, públicos e cuidados éticos comuns aos três instrumentos. | Equipe 16; revisão documental assistida pelo Codex a pedido da equipe |
| 30/10/2026 | Revisão de coerência com a Entrega 8. Especificação textual de I02 com Q00–Q27, triagem, consentimento, aplicação e análise, tornando explícitas as perguntas citadas na matriz. Formulário do guia identificado como feedback da Entrega 6, distinto de I02. Configuração on-line, piloto e coleta continuam pendentes. | Equipe 16; autoria de I02 mantida conforme identificação do instrumento, com revisão documental assistida pelo Codex a pedido da equipe |
