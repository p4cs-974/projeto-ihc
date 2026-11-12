# Capturas do protótipo principal

Capturas a 1280 × 800 no Chromium local, com os oito cortes de duas partidas descritos em [`media/manifest.json`](../media/manifest.json). A pasta indica a versão e a data. Os scripts estão em [`artifacts/entrega6/verificacao-2026-11-10`](../../../artifacts/entrega6/verificacao-2026-11-10/).

## Versão 1, usada na sessão de 22/10/2026

Pasta [`v1_2026-10-22_antes`](v1_2026-10-22_antes/). Arquivo de `bce19c4`, capturado em 10/11/2026. O estado concluído da tela 3 foi obtido chamando a função `finishAll` da própria página, sem esperar a reprodução; por isso as prévias mostram os primeiros vídeos.

| Arquivo | Tela |
|---|---|
| `E06-P03_analise_concluida_v1.png` | Fim da análise, sem ação para continuar |
| `E06-P04A_busca_v1.png` | Alternativa A, busca primeiro |
| `E06-P04B_trilhas_v1.png` | Alternativa B, trilhas por partida, com um lance incluído |
| `E06-P04C_mosaico_v1.png` | Alternativa C, mosaico por tipo |

## Versão 2, revisada em 10/11/2026

Pasta [`v2_2026-11-10`](v2_2026-11-10/). As telas revisadas respondem a E06-O01, O02, O04 e O06 e aos percursos de exceção. Não foram usadas por participantes. O nome de cada arquivo começa pelo ID da tela no inventário da [seção 3.1 da Entrega 6](../../../docs/06_prototipacao_papel.md#31-inventário-e-navegação); quando o nome não traz o ID do estado, a coluna da direita o indica.

| Arquivo | Tela ou estado |
|---|---|
| `E06-P02_percurso_encenado_v2.png` | Vídeos selecionados com o percurso **Falha em um vídeo** escolhido |
| `E06-P03_em_andamento_v2.png` | Análise com o primeiro lance pronto e **Ver resultados prontos (1) →** |
| `E06-P03_analise_concluida_v2.png` | Fim da análise, com **Ver os 8 lances na base →** |
| `E06-P03F_falha_localizada_v2.png` | Falha encenada de um vídeo enquanto os outros continuam |
| `E06-P04_resultados_parciais_v2.png` | E06-P04L. Base aberta com a análise em andamento e o estado de cada vídeo |
| `E06-P04A_busca_v2.png` | Alternativa A com o lote concluído |
| `E06-P04B_trilhas_v2.png` | Alternativa B com filtros claros, legenda e etiquetas com relógio do jogo |
| `E06-P04C_mosaico_v2.png` | Alternativa C |
| `E06-P04F_falha_na_base_v2.png` | Falha na base, com lance preservado, nova tentativa e pendência |
| `E06-P04V_busca_sem_correspondencia_v2.png` | Busca sem correspondência, com o 2º tempo de Bayern sem lances listado à parte |
| `E06-P04B_video_sem_lances_v2.png` | E06-P04Z na alternativa B. Faixa de B para um tempo analisado sem lances |
| `E06-P04S_obter_selecao_v2.png` | Painel **Obter seleção**, com lista CSV e vídeos MP4 separados |

O [esboço original](../esboco_original.png) registra uma fase anterior, com a organização da base ainda em aberto. As capturas de [`artifacts/media-review`](../../../artifacts/media-review/README.md) são de 21/10/2026 e registram uma etapa intermediária da troca para clipes reais, com quatro cortes de uma partida. O commit integrado naquele dia, `74041d3`, já tem os oito cortes de duas partidas.
