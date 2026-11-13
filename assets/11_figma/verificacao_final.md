# Registro da conferência final da Entrega 11

**Data da execução:** 13/11/2026.\
**Artefato:** [preview público](https://ihc-11.p4cs.com.br/) e [fonte editável](../06_prototipos/PROTOTIPO_fluxo_highlights.html).\
**Execução:** GPT-6.1 Terra, raciocínio high e serviço priority, com complemento de GPT-6.1 Sol, pelo harness Codex no T3 Code.

Este registro consolida as observações da conferência final descrita na [Entrega 11](../../docs/11_figma.md). Os números abaixo são daquela execução, não de uma nova rodada de testes.

## Percursos e resultados observados

| Conferência | Resultado |
|---|---|
| Entrada → exemplos → lote → análise | Quatro vídeos carregados. O complemento acompanhou a conclusão natural, sem atalho: quatro prontos e oito lances disponíveis. O botão final abriu a base com os oito itens |
| A/B/C, busca e seleção | Seleção de Suárez e Defesa do Barcelona mantida ao trocar visualização. Busca sem correspondência em A apresentou mensagem e limpeza dos critérios. Obter seleção desativado com seleção vazia |
| Detalhe e obtenção | Player do detalhe avançou. Diálogo apresentou CSV e MP4 separados. O navegador registrou os três downloads concluídos |
| CSV salvo | Exatamente duas linhas de dados, IDs suarez e bravo. Seleção, URLs e tempos conferidos contra o manifesto |
| MP4 salvos | Hashes iguais aos arquivos de origem e ao manifesto. Decodificação integral com ffmpeg sem erro |
| Reprodução dos arquivos salvos | Arquivos abertos por seletor local em página temporária de teste, como URLs blob, sem buscar de novo os vídeos do site. Ambos chegaram a ended=true, com error=null. Quadros dos arquivos e captura do player inspecionados |

## Amostra do CSV salvo

O CSV usa ponto e vírgula, UTF-8 com BOM e 16 colunas. A tabela apresenta as referências temporais e os links das duas linhas, sem substituir o arquivo exportado.

| ID | Partida | Tempo | Relógio do jogo | Evento no arquivo | Início do corte | Fim do corte | URL do MP4 |
|---|---|---|---|---|---|---|---|
| suarez | Real Madrid 0 x 4 Barcelona | 1 | 10:04 | 604.24 s | 590 s | 618 s | [suarez.mp4](https://ihc-11.p4cs.com.br/media/suarez.mp4) |
| bravo | Real Madrid 0 x 4 Barcelona | 2 | 47:55 | 175.605 s | 163 s | 190 s | [bravo.mp4](https://ihc-11.p4cs.com.br/media/bravo.mp4) |

## Integridade e reprodução dos MP4

Os dois vídeos têm resolução de 398 × 224. Quadros apresentados e descartados foram lidos com getVideoPlaybackQuality() após o término da reprodução no navegador.

| Arquivo | Bytes | Duração | Quadros apresentados | Quadros descartados | SHA-256 |
|---|---|---|---|---|---|
| suarez | 2051038 | 28 s | 700 | 0 | `619ec7fa533a5b96ad9d83dba6c6e72ccab0f4d317e857626a35554c0df73f26` |
| bravo | 2128284 | 27 s | 675 | 0 | `db04a5a7f84e764d7289acb427fe83f2a6d2c37670f71efb4ba83e2bdfdbe791` |

Os valores de referência também podem ser consultados no [manifesto versionado](../06_prototipos/media/manifest.json). Para conferir um arquivo baixado, compare seu SHA-256 com a tabela e execute a decodificação completa, substituindo o nome pelo caminho do arquivo salvo:

```sh
sha256sum suarez.mp4
ffmpeg -v error -xerror -i suarez.mp4 -f null -
```

Esses comandos verificam bytes e decodificação. A reprodução no navegador foi uma verificação separada, descrita acima.

## Limites

A rodada cobriu uma seleção de dois dos oito cortes. O acesso aos resultados pelo atalho também foi usado nos testes de A/B/C; o complemento verificou separadamente a conclusão natural. A primeira reprodução técnica com dispositivos dummy não contou como inspeção visual; ela foi complementada pela reprodução dos arquivos salvos no navegador e inspeção dos quadros.

Não houve avaliação auditiva da qualidade do áudio, sessão com participantes, leitor de tela, avaliação mobile ou repetição de todos os ramos de falha e recuperação. Os resultados não demonstram conformidade global de acessibilidade nem cumprimento de metas de usabilidade. Não houve defeito reproduzido na amostra verificada.
