# Clipes SoccerNet da demonstração

O manifesto liga cada corte à partida, ao tempo, ao arquivo local e à anotação original do SoccerNet-v2. O T3 localizou o projeto `tcc`, registrado em `/home/pedro/tcc`. Os arquivos existentes ficam em `benchmark/downloads`. Nenhuma partida foi baixada ou copiada para este repositório.

Todos os cortes vêm de Real Madrid 0 x 4 Barcelona, em 21 de novembro de 2015. Os candidatos foram encontrados em `Labels-v2.json` e conferidos no navegador T3, com reprodução e quadros da construção, da finalização e do desfecho. A defesa corresponde à anotação `Shots on target`; o rótulo de defesa vem da conferência visual do goleiro espalmando a bola.

| Corte | Tempo | Relógio do jogo na anotação | Corte na fonte, segundos | Evento dentro do corte | Duração | MP4, bytes |
|---|---|---|---|---|---|---|
| Suárez | 1 | 10:04 | 590 a 618 | 14,240 s | 28 s | 2.051.038 |
| Neymar | 1 | 38:35 | 2302 a 2330 | 13,370 s | 28 s | 2.118.067 |
| Defesa do Barcelona | 2 | 47:55 | 163 a 190 | 12,605 s | 27 s | 2.128.284 |
| Iniesta | 2 | 52:17 | 423 a 451 | 14,840 s | 28 s | 1.885.059 |

## Tempos e origem

`annotation.position` mede milissegundos no vídeo do respectivo tempo. `annotationToVideoOffsetSeconds` é zero nestas duas fontes, confirmado pela ação visível nos candidatos. Não se concatena o segundo tempo ao arquivo do primeiro. O relógio da transmissão fica aproximadamente um segundo atrás do instante anotado.

`gameTime` também é relativo ao tempo. Por exemplo, `2 - 07:17` aparece como `52:17` no relógio total da partida. O arquivo do segundo tempo continua usando 437,840 segundos. O corte de Iniesta começa em 423 segundos, portanto o evento está em 14,840 segundos no player. O marcador representa um instante anotado, sem inventar uma duração para o evento.

Cada miniatura é um quadro do MP4 publicado, 1,5 segundo antes do evento anotado. Os hashes das anotações e dos clipes estão no manifesto. Os arquivos completos de origem têm 190.470.781 e 204.988.194 bytes. Seus caminhos são registros de proveniência, sem URL de download no produto.

## Gerar os mesmos cortes

São necessários Python, FFmpeg e FFprobe. Execute na raiz do repositório, apontando para uma cópia local já existente do dataset.

```sh
python scripts/extract-highlights.py /home/pedro/tcc/benchmark/downloads --compare
sh site/build.sh
```

O script verifica o hash de `Labels-v2.json`, a presença da anotação, o formato da fonte e os limites dos cortes. Depois extrai os MP4 e as miniaturas e atualiza tamanhos e hashes. `--compare` também gera a amostra CRF 26 em `artifacts/media-review`, fora dos arquivos publicados pelo site.

As fontes já são H.264, 398 × 224, 25 fps, com áudio Vorbis estéreo. A extração preserva a resolução e a frequência. Usa H.264 CRF 23, preset `slow`, `yuv420p`, keyframes a cada dois segundos, áudio AAC a 64 kbit/s e `faststart`. A recodificação permite cortes exatos e converte o áudio para reprodução em navegadores. Um remux sem recodificação exigiria acomodar os keyframes espaçados da fonte.

O corte de Suárez tem 2.051.038 bytes em CRF 23 e 1.510.134 bytes em CRF 26. A segunda opção economiza 26,4% nesse mesmo intervalo. A comparação visual no T3 mostrou a jogada compreensível nas duas versões. CRF 23 foi escolhido para conservar mais detalhe na fonte de baixa resolução. Essa escolha não cria detalhe de alta definição.

Os quatro MP4 totalizam 8.182.448 bytes, 111 segundos. As quatro miniaturas somam 74.013 bytes. O build publica apenas os quatro MP4, as quatro miniaturas e o manifesto. A comparação CRF 26 permanece fora do site.
