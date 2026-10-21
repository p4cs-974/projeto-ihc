# Clipes SoccerNet da demonstração

O manifesto liga cada corte à partida, ao tempo, ao arquivo local e à anotação original do SoccerNet-v2. O T3 localizou o projeto `tcc`, registrado em `/home/pedro/tcc`. Os arquivos existentes ficam em `benchmark/downloads`. Nenhuma partida foi baixada ou copiada para este repositório.

Os cortes vêm de duas partidas: Real Madrid 0 x 4 Barcelona (LaLiga, 21/11/2015) e Bayern de Munique 1 x 2 Real Madrid (quartas de final da Liga dos Campeões, 12/04/2017). Os candidatos foram encontrados em `Labels-v2.json` de cada partida e conferidos no T3, em quadros da construção, da finalização e do desfecho e na reprodução do corte publicado. A defesa do Barcelona corresponde à anotação `Shots on target`; o rótulo de defesa vem da conferência visual do goleiro espalmando a bola. No pênalti de Vidal, a anotação `Penalty` cai no chute, em 45:53 do primeiro tempo, conferido em quadros a cada 0,5 s: Navas cai e a bola passa por cima do gol.

| Corte | Tempo | Relógio do jogo na anotação | Corte na fonte, segundos | Evento dentro do corte | Duração | MP4, bytes |
|---|---|---|---|---|---|---|
| Suárez | 1 | 10:04 | 590 a 618 | 14,240 s | 28 s | 2.051.038 |
| Neymar | 1 | 38:35 | 2302 a 2330 | 13,370 s | 28 s | 2.118.067 |
| Defesa do Barcelona | 2 | 47:55 | 163 a 190 | 12,605 s | 27 s | 2.128.284 |
| Iniesta | 2 | 52:17 | 423 a 451 | 14,840 s | 28 s | 1.885.059 |
| Vidal (Bayern) | 1 | 24:43 | 1470 a 1498 | 13,960 s | 28 s | 2.386.647 |
| Pênalti perdido por Vidal | 1 | 45:53 | 2739 a 2767 | 14,000 s | 28 s | 1.722.172 |
| Cristiano Ronaldo | 2 | 46:35 | 81 a 109 | 14,440 s | 28 s | 1.832.449 |
| Cristiano Ronaldo, segundo gol | 2 | 76:03 | 1849 a 1877 | 14,440 s | 28 s | 2.109.983 |

## Tempos e origem

`annotation.position` mede milissegundos no vídeo do respectivo tempo. `annotationToVideoOffsetSeconds` é zero nas quatro fontes, confirmado pela ação visível nos candidatos. Não se concatena o segundo tempo ao arquivo do primeiro. O relógio da transmissão fica aproximadamente um segundo atrás do instante anotado.

`gameTime` também é relativo ao tempo. Por exemplo, `2 - 07:17` aparece como `52:17` no relógio total da partida. O arquivo do segundo tempo continua usando 437,840 segundos. O corte de Iniesta começa em 423 segundos, portanto o evento está em 14,840 segundos no player. O marcador representa um instante anotado, sem inventar uma duração para o evento.

Cada miniatura é um quadro do MP4 publicado, 1,5 segundo antes do evento anotado. Os hashes das anotações e dos clipes estão no manifesto. Os arquivos completos de origem têm 190.470.781 e 204.988.194 bytes (Real Madrid x Barcelona) e 187.736.200 e 174.269.113 bytes (Bayern x Real Madrid), 757.464.288 bytes no total. Seus caminhos são registros de proveniência, sem URL de download no produto.

## Gerar os mesmos cortes

São necessários Python, FFmpeg e FFprobe. Execute na raiz do repositório, apontando para uma cópia local já existente do dataset.

```sh
python scripts/extract-highlights.py /home/pedro/tcc/benchmark/downloads --compare
sh site/build.sh
```

O script verifica o hash de `Labels-v2.json`, a presença da anotação, o formato da fonte e os limites dos cortes. Depois extrai os MP4 e as miniaturas e atualiza tamanhos e hashes. `--compare` também gera a amostra CRF 26 em `artifacts/media-review`, fora dos arquivos publicados pelo site.

As fontes já são H.264, 398 × 224, 25 fps, com áudio Vorbis estéreo. A extração preserva a resolução e a frequência. Usa H.264 CRF 23, preset `slow`, `yuv420p`, keyframes a cada dois segundos, áudio AAC a 64 kbit/s e `faststart`. A recodificação permite cortes exatos e converte o áudio para reprodução em navegadores. Um remux sem recodificação exigiria acomodar os keyframes espaçados da fonte.

O corte de Suárez tem 2.051.038 bytes em CRF 23 e 1.510.134 bytes em CRF 26. A segunda opção economiza 26,4% nesse mesmo intervalo. A comparação visual no T3 mostrou a jogada compreensível nas duas versões. CRF 23 foi escolhido para conservar mais detalhe na fonte de baixa resolução. Essa escolha não cria detalhe de alta definição.

Os oito MP4 totalizam 16.233.699 bytes, 223 segundos. As oito miniaturas somam 161.863 bytes. O build publica apenas os oito MP4, as oito miniaturas e o manifesto. Reextrair tudo com o script reproduz byte a byte os quatro cortes do clássico. A comparação CRF 26 permanece fora do site.
