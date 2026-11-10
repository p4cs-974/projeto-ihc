# Aplicação dos pareceres das Entregas 6, 7 e 8

**Data:** 10/11/2026
**Branch:** `feedback/entregas-06-07-08`, a partir de `bce19c4`
**Aplicação:** automação a pedido de Pedro. Os commits e as anotações registram o que mudou nos arquivos. Não confirmam fatos novos, consentimentos nem contribuições de Lucas e Giovanni.
**Revisão independente:** feita sobre `bb5415f` por GPT-6.1 Sol, esforço high (Codex), e Opus 5.5, esforço medium (Claude Agent). Os dois concluíram ISSUES sem defeito funcional. Os reparos estão na seção 8.

Este relatório reúne, item por item, o que cada parecer pediu, onde foi tratado, a evidência no repositório e o que depende de alguém da equipe. Os pareceres anotados são a fonte de cada decisão:

- [Parecer da Entrega 6](../../feedbacks_professor/Feedback_Professor_Entrega06_Equipe16.md)
- [Parecer da Entrega 7](../../feedbacks_professor/Feedback_Professor_Entrega07_Equipe16.md)
- [Parecer da Entrega 8](../../feedbacks_professor/Feedback_Professor_Entrega08_Equipe16.md)

Situações usadas: **aplicada**, **em parte** (uma parte ficou com alguém ou depende de ação externa), **encaminhada** (não pede mudança agora) e **pendente**.

## 1. Entrega 6, prototipação

| Item do parecer | Situação | Commits | Evidência | Pendência humana |
|---|---|---|---|---|
| Registro do parecer | aplicada | `3ff5030` | `feedbacks_professor/Feedback_Professor_Entrega06_Equipe16.md` | Nenhuma |
| Correção 1: revisão concreta das telas e status | aplicada; verificação com participante pendente | `b087c06`, `9c67289` | `docs/06_prototipacao_papel.md`, seções 5.1 e 5.2; `assets/06_prototipos/capturas/` | Revalidar as telas da versão 2 com o roteiro da seção 5.3 |
| Correção 2: continuidade e obtenção | aplicada | `9c67289` | `assets/06_prototipos/PROTOTIPO_fluxo_highlights.html`, telas 3 e 4 e painel **Obter seleção**; `artifacts/entrega6/verificacao-2026-11-10/percurso_principal.py` | Nenhuma no protótipo; a verificação com pessoa fica na Correção 4 |
| Correção 3: exceções | aplicada como percurso encenado | `9ed3753` | E06-P03F, E06-P04F e E06-P04Z na seção 3.1; `artifacts/entrega6/verificacao-2026-11-10/percursos_encenados.py` | Nenhuma; nenhum processamento real falha |
| Correção 4: condução do walkthrough | em parte | `d09b9c3` | Seções 4.3 e 5.3 | Nova verificação com participante não realizada |
| Correção 5: evidências e acessos | em parte | `d5d9f71`, `fb259aa`, `0dff068` | `artifacts/entrega6/sessao-2026-10-22/README.md`, com o SHA-256 do áudio; link interno no guia e no `README.md` | Áudio não publicado: falta autorização registrada de U01 ou versão com vozes alteradas, decisão de Pedro |
| Correção 6: participação dos integrantes | em parte | `0d0ac88` | Seção 6 | Contribuições reais de Lucas e Giovanni: PENDENTE, cada um registra a própria |
| Recomendação: capturas por versão | aplicada | `576d03b` | `assets/06_prototipos/capturas/README.md`; nota em `artifacts/media-review/README.md` | Nenhuma |
| Recomendação: termos highlight, corte, seleção e CSV | aplicada | `9c67289`, `d09b9c3`, `dfbe0f5`, `14f6c1d` | Rótulos **Selecionar** e **Obter seleção**; seção 4.1 registra a exposição ao glossário; roteiro 5.3 separa interface de instrução | Nenhuma; o glossário do guia foi mantido de propósito |
| Recomendação: ordem e objetivos equivalentes nas alternativas | aplicada; volume maior pendente | `d09b9c3`, `b087c06` | Roteiro 5.3; E06-D04 na seção 5.2 | Explorar C com mais de oito candidatos exige cortes novos |
| Recomendação: não investir em acabamento visual | encaminhada | nenhum | Revisão limitada às observações | Nenhuma |
| Cabeçalho e histórico | aplicada | `b7cfe44` | Cabeçalho e histórico do documento | Nenhuma |
| Anotação do parecer | aplicada | `f28c6b1`, `e0221a3` | Parecer anotado | Nenhuma |
| Integração da revisão | aplicada | `451e3e4` | Merge da branch da Entrega 6 | Nenhuma |

## 2. Entrega 7, coleta de dados

| Item do parecer | Situação | Commits | Evidência | Pendência humana |
|---|---|---|---|---|
| Registro do parecer | aplicada | `241b13d` | `feedbacks_professor/Feedback_Professor_Entrega07_Equipe16.md` | Nenhuma |
| Pontos positivos preservados | aplicada | `930f673` | I01, I03, protocolo comum e limites mantidos em `docs/07_coleta_dados.md` | Nenhuma |
| Correção 1: papel de I02 | aplicada | `dc58d6e`, `e84eb25` | "Papel no conjunto" de I02 e matriz de análise; seção 3.2 de `RASTREABILIDADE.md` | Nenhuma |
| Correção 2: elegibilidade | aplicada na fonte local | `3c49540` | G01 e confirmação de maioridade em `assets/06_prototipos/GUIA_simulacao.html` | Publicar a versão `2026-11-10`; a página on-line segue na `2026-10-21` |
| Correção 3: protocolo ético no formulário | em parte; aplicada na fonte local | `8767d6c`, `7110617`, `fbc6452`, `db94a63` | Seção "Sua participação" do guia; "Prefiro não responder"; "Apagar rascunho"; código de resposta | Canal fixo de contato para quem recebeu o link repassado; publicação |
| Correção 4: reprodutibilidade de I02 | aplicada; piloto pendente | `110cf22` | Procedimento em nove passos de I02 | Confirmar Lucas na exportação e outro integrante na conferência; verificar acesso ao D1; piloto |
| Correção 5: Parte A individual, cabeçalho e checklist | em parte | `748ad81` | A01–A03 e cabeçalho do documento | A01–A03 são planejamento proposto; cada integrante revisa e assume a sua |
| Recomendação: sondagem condicional de E07 | aplicada | `930f673` | Roteiro de I01 | Nenhuma |
| Recomendação: revisão manual como contexto | aplicada | `930f673` | Cartão de abertura do guia | Nenhuma |
| Recomendação: nome em G08 | aplicada | `930f673` | G08 retirado da fonte local | Retirar o campo `nome` dos registros `2026-10-21` na exportação |
| Recomendação: relator e recursos do brainstorming | em parte | `930f673` | I03 com recursos e Pedro como relator proposto | Confirmar relator e ferramenta de quadro |
| Pontos para as próximas entregas | encaminhados | `dc58d6e`, `e84eb25` | Matriz de análise de I02; seção 3.2 da matriz | Revisar P01/P02/P03 e tarefas só depois da coleta |
| Síntese, item 5: pilotos | pendente | nenhum | Checklist da Entrega 7 | Realizar pilotos de I01, I02 e I03 |
| Cabeçalho e histórico | aplicada | `d3dddd2` | Cabeçalho e histórico do documento | Nenhuma |
| Anotação do parecer | aplicada | `b3215d4`, `e0221a3` | Parecer anotado | Nenhuma |
| Integração da revisão | aplicada | `56a53fe` | Merge da branch da Entrega 7 | Nenhuma |

## 3. Entrega 8, engenharia de usabilidade

| Item do parecer | Situação | Commits | Evidência | Pendência humana |
|---|---|---|---|---|
| Registro do parecer | aplicada | `31219bb` | `feedbacks_professor/Feedback_Professor_Entrega08_Equipe16.md` | Nenhuma |
| Correção 1: princípios de negócio e de interface | aplicada | `d23f330` | Seções 2.1 e 2.2 de `docs/08_engenharia_usabilidade.md` | Nenhuma |
| Correção 2: cinco metas de Nielsen | aplicada; pesos propostos | `01811bf` | Seção 3.3 | Confirmar os pesos; cada integrante declara as videoaulas que consultou |
| Correção 3: ciclo de Mayhew | aplicada | `f693bf0`, `050a480` | Seção 4 | Nenhuma; guia de estilo próprio continua `[?]` |
| Correção 4: cobertura pelos instrumentos | aplicada como plano | `0743b4d`, `050a480` | Seção 3.4; MU07 e MU08 | Confirmar os limites de MU07 e MU08; preparar os instrumentos na Entrega 12 |
| Recomendação: limites provisórios | aplicada | `534ceaa` | Seção 3.2 | Calibrar no piloto da Entrega 12 |
| Recomendação: tempo com contexto | aplicada | `534ceaa` | MU05 e regra de tempo | Nenhuma |
| Recomendação: não ensinar o que será avaliado | aplicada | `534ceaa`, `050a480`, `14f6c1d` | Seção 3; o glossário do guia conta como explicação prévia; dica das setas corrigida sem novo caminho | Preparar as instruções adaptadas na Entrega 12 |
| Recomendação: MU/MQ na matriz central | aplicada | `e84eb25`, `90ab599` | Seção 3.2 de `RASTREABILIDADE.md`, como especificação e não como resultado | Nenhuma |
| Recomendação: status e checklist | aplicada | `534ceaa`, `e10a8f8`, `0dff068` | Status 🟨 no documento e no `README.md` | Nenhuma |
| Pontos para as próximas entregas | encaminhados | `f693bf0`, `534ceaa`, `050a480` | Seções 3.4 e 4 | Mais de oito candidatos, histórico e retomada após recarga continuam sem solução |
| Cabeçalho e histórico | aplicada | `e10a8f8`, `050a480` | Cabeçalho e histórico do documento | Nenhuma |
| Anotação do parecer | aplicada | `d99bc75`, `e0221a3` | Parecer anotado | Nenhuma |

## 4. Consolidação entre as entregas

| Mudança | Commit | Arquivos |
|---|---|---|
| Espaço sobrando no fim da linha 25 do script de verificação | `da5ebf5` | `artifacts/entrega6/verificacao-2026-11-10/percurso_principal.py` |
| Dica das setas: a seta não termina mais a análise na versão 2; a frase errada saiu sem nova instrução de caminho. Comentário do protótipo sem "Baixar CSV" | `14f6c1d` | `assets/06_prototipos/GUIA_simulacao.html`, `assets/06_prototipos/PROTOTIPO_fluxo_highlights.html` |
| Entrega 6 descrevia só o formulário `2026-10-21` e chamava a seleção de inclusão no CSV; exposição ao glossário registrada | `dfbe0f5` | `docs/06_prototipacao_papel.md` |
| Entrega 8 dizia que entrar na base concluía a análise e que falhas e resultados parciais não existiam; agora são estados encenados e não verificados | `050a480` | `docs/08_engenharia_usabilidade.md` |
| Status das Entregas 6 a 8 com pendências e links aos pareceres | `0dff068` | `README.md` |
| Seção 3.1 na versão 2, nova seção 3.2 com MQ/MU, seção 4, três linhas da seção 5 e histórico | `e84eb25` | `RASTREABILIDADE.md` |
| Checklist da Entrega 8 com a referência MU/MQ feita | `90ab599` | `docs/08_engenharia_usabilidade.md` |
| Anotações da consolidação nos três pareceres | `e0221a3` | `feedbacks_professor/` |

## 5. Decisões registradas

- **I02 fica restrito à experiência de uso do protótipo.** A alternativa do parecer, acrescentar perguntas sobre a prática atual, foi descartada na revisão da Entrega 7. A matriz central e o `README.md` seguem essa decisão.
- **D01, D02 e D05 contam como implementadas, não como validadas.** Nenhum documento afirma que as telas da versão 2 resolveram as dificuldades de U01.
- **MQ01–MQ04 e MU01–MU08 entram na matriz como especificação.** Nenhuma meta foi medida.
- **O guia mantém o glossário e não ganhou instrução de caminho.** A frase errada sobre as setas saiu sem substituição. A exposição aos termos fica registrada como instrução recebida, para não ser lida como descoberta espontânea.
- **Maior volume, histórico e retomada após recarga continuam sem solução.** Nenhuma mudança desta rodada os representa.
- **Pesos de prioridade, MU07 e MU08 seguem como proposta.** Só os limites de MU01–MU06 têm confirmação registrada, de Pedro em 29/10/2026.
- **O link da Entrega 6 no `README.md` aponta para o protótipo do repositório.** A versão on-line não recebeu a versão 2 nem o formulário `2026-11-10`, porque esta rodada não fez deploy.

## 6. Pendências humanas

| Pendência | Quem decide ou executa |
|---|---|
| Publicar o áudio da sessão de 22/10/2026 ou manter só a transcrição. Exige autorização registrada de U01 ou versão com vozes alteradas | Pedro |
| Registrar as contribuições reais de Lucas e Giovanni na Entrega 6 | Lucas e Giovanni: PENDENTE |
| Revisar e assumir A01–A03 da Parte A da Entrega 7 | Cada integrante |
| Confirmar os pesos de prioridade e os limites de MU07 e MU08 | Equipe |
| Revalidar as telas da versão 2 com uma ou duas pessoas de fora do desenho | Equipe |
| Publicar a versão `2026-11-10` do guia e do formulário | Equipe |
| Pilotos de I01, I02 e I03; coleta | Equipe |
| Confirmar responsáveis pela exportação e conferência de I02, o canal fixo de contato, o acesso ao D1 restrito aos três integrantes, o relator e a ferramenta de quadro de I03 | Equipe |
| Explorar C com mais de oito candidatos | Equipe |

## 7. Verificação feita nesta rodada

- `git diff --check bce19c4..HEAD` sem ocorrências.
- Links relativos e âncoras de `README.md`, `RASTREABILIDADE.md`, `docs/06`, `docs/07`, `docs/08`, dos três pareceres e dos READMEs de capturas e verificação conferidos por script, sem falhas.
- Cada tabela alterada tem o mesmo número de colunas em todas as linhas.
- O texto do professor nos três pareceres é igual ao do commit que o registrou; só as citações anotadas mudaram.
- O HTML de diffs foi gerado fora do repositório, com `.agents/skills/aplicar-feedback-professor/scripts/gerar_diffs.py`, um por parecer e um agregado.

## 8. Revisão independente de `bb5415f`

Dois revisores de famílias diferentes revisaram a branch no commit `bb5415f`:

| Revisor | Modelo e esforço | Veredito | O que executou |
|---|---|---|---|
| Codex | GPT-6.1 Sol, high | ISSUES, sem defeito funcional | Chromium no percurso principal (14 de 14), percursos encenados (18 de 18), conclusão natural (5 de 5); formulário com falha, recusa e rascunho; exportação pela CLI e hashes das mídias |
| Claude Agent | Opus 5.5, medium | ISSUES, sem defeito funcional | Os mesmos scripts Chromium e o formulário; hash e metadados do áudio local; preservação do texto do professor |

Achados e reparos:

| Achado | Reparo | Commit |
|---|---|---|
| A tabela de I02 não listava "Prefiro não responder" em G01, ao contrário do formulário | Alternativa acrescentada na tabela | `fbc6452` |
| O comando de exportação do passo 8 de I02 não rodava: o Wrangler exige `--command` ou `--file` | Comando completo, executado em `site/`, com `SELECT id, criado_em, versao, respostas FROM feedback ORDER BY id`, `--remote --json` e destino `<pasta-privada>`. Sintaxe conferida no `--help` do Wrangler 4.159.0 e consulta conferida contra a migração em SQLite local. Nada foi executado contra produção | `97d9782` |
| O roteiro 5.3 da Entrega 6 supunha que o formulário grava com o protótipo servido por `python3 -m http.server`, que responde 501 ao envio | Autorrelato na ficha de observação; `npx wrangler dev` com D1 local só para testes; formulário `2026-11-10` para participação remota só após publicação; versões `2026-10-21` e `2026-11-10` separadas. O 501 foi conferido com `curl` | `9c1eadb` |
| A anotação da Correção 3 da Entrega 7 dizia ✅ com o canal fixo de contato pendente | Anotação passou a 🟨 Tratado em parte | `fe83f19` |
| A anotação de status da Entrega 8 listava como aberta a referência na matriz, já feita em `90ab599` | Anotação corrigida | `fe83f19` |
| A seção 6 da Entrega 6 atribuía a Pedro todos os commits dos arquivos da entrega | Exceção para `f47f4b5` e `1a52696`, do modelo da disciplina, de Plinio Thomaz Aquino Junior, conferida com `git log` | `b47af95` |
| A Entrega 8 dizia que todos os limites da seção 3.2 estavam confirmados | Só MU01–MU06; MU07, MU08 e os pesos seguem como proposta | `97f3f07` |
| `site/README.md` descrevia um download único de CSV | Painel **Obter seleção**, CSV sem vídeo, um MP4 por lance e links individuais | `eb0c7a7` |
| I02 espera cerca de três minutos e a revalidação da Entrega 6 espera 30 segundos, sem explicação | Os dois documentos justificam pela modalidade. O roteiro 5.3 usa 30 segundos; I02 usa três minutos. Nenhum resultado foi criado | `a6d24e0` |
| O checklist da Entrega 7 não trazia canal fixo, acesso ao D1, relator e ferramenta de I03 | Quatro itens abertos acrescentados | `db94a63` |
| I02 não dizia qual percurso do protótipo usar, e o README das capturas não ligava dois arquivos aos IDs do inventário | I02 usa o **Percurso normal**, e os percursos encenados ficam na revalidação; capturas ligadas a E06-P04L e E06-P04Z | `e103763`, `ebd0a61` |
| Comentários novos narravam a versão ou a etapa no protótipo, no guia e nos scripts | Comentários retirados; nomes ambíguos renomeados (ver decisão abaixo) | `607fc76` |
| Anotações dos reparos nos pareceres | Uma linha na tabela de situação de cada parecer e uma nota por item tocado | `fe83f19` |

**Decisão de escopo sobre comentários.** Os revisores divergiram sobre quanto mexer no código para tirar os comentários. A rodada retirou só os comentários novos de narração e renomeou os nomes que dependiam deles: `base` para `displayedHighlights`, `SCEN` para `STAGED_PATHS`, `failPos` para `stagedFailureSecond`, `bgSync`, `BG_MS`, `bgStep` e `bgT` para `syncBackgroundAnalysis`, `BACKGROUND_VIDEO_MS`, `finishNextBackgroundVideo` e `backgroundTimer`, e `spread` para `nudgeOverlappingMarks`. O estado `S.base` manteve o nome, porque deixou de colidir com a função. O comentário de `contraste_trilhas.py` ficou, porque explica a interpolação do `color-mix` que o script reproduz fora do navegador. O `sed` de `site/build.sh` ficou, porque adapta o link entre os dois layouts e já foi verificado. A decisão não pediu arquiteto nem painel extra.

**Verificação dos reparos.**

- Os três scripts Chromium, em cópia temporária apontada para um servidor próprio na porta 18762, passaram depois dos renomes: `percurso_principal.py` 14 de 14, `conclusao_tela3.py` 5 de 5, `percursos_encenados.py` 18 de 18, sem erro de JavaScript na página. O servidor foi encerrado ao fim.
- `git diff --check bb5415f..HEAD` sem ocorrências.
- Links relativos, âncoras e número de colunas das tabelas conferidos por script nos arquivos alterados.
- O texto do professor nos três pareceres continua igual ao dos commits que o registraram.

**Pendências humanas preservadas.** As da seção 6 continuam abertas: áudio, contribuições de Lucas e Giovanni (PENDENTE), A01–A03, pesos e limites de MU07 e MU08, revalidação com participante, publicação da versão `2026-11-10`, pilotos e coleta, responsáveis por I02, canal fixo de contato, acesso ao D1, relator e ferramenta de I03 e volume maior em C.
