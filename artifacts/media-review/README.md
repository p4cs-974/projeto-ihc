# Conferência da mídia real

A seleção e os tempos estão no [manifesto](../../assets/06_prototipos/media/manifest.json). O procedimento está no [guia de extração](../../assets/06_prototipos/media/README.md).

## Amostras da mesma jogada

- [CRF 23 escolhido, 2.051.038 bytes](../../assets/06_prototipos/media/suarez.mp4).
- [CRF 26, 1.510.134 bytes](suarez-crf26.mp4).

As duas amostras têm os mesmos 28 segundos, 398 × 224 pixels, 25 fps e áudio AAC a 64 kbit/s. A comparação usa o mesmo arquivo de origem e os mesmos limites, sem reduzir a resolução. CRF 26 economiza 540.904 bytes. Escolhi CRF 23 para conservar mais detalhe na bola e nos jogadores. A diferença observada é pequena; a resolução disponível é o principal limite de qualidade.

O player busca o MP4 curto inteiro após um clique. Assim, o primeiro quadro espera o download de aproximadamente 2 MB, e interromper cedo não reduz esse primeiro download. O benefício é seeking completo e previsível no navegador do T3, inclusive quando o servidor local não informa `Content-Length`. Apenas o corte ativo ocupa um objeto de mídia. Trocar de corte cancela a requisição pendente e libera o objeto anterior.

## Verificação no navegador do T3

Os [resultados brutos](browser-measurements.json) registram Navigation Timing e Resource Timing do navegador, usando o build servido por `wrangler dev`, sem publicação. Na rodada final, os assets da origem `127.0.0.1:8768` ainda não estavam no cache. Fontes externas já estavam em cache ou não apareceram em Resource Timing. Portanto os totais iniciais abaixo são os bytes observados, um limite inferior do tráfego completo; não incluem todo o custo de fontes, TCP ou TLS. `transferSize` inclui a estimativa de cabeçalhos do navegador, e `encodedBodySize` mede o corpo comprimido.

| Ação | Bytes observados transferidos | MP4 solicitado |
|---|---:|---|
| Abrir tela inicial | 18.830 | Nenhum |
| Abrir exemplos e chegar à lista, acumulado | 94.043 | Nenhum |
| Reproduzir Suárez | 2.051.338 | Apenas `suarez.mp4` |
| Reproduzir Neymar | 2.118.367 | Apenas `neymar.mp4` |
| Reproduzir a defesa | 2.128.584 | Apenas `bravo.mp4` |
| Reproduzir Iniesta | 1.885.359 | Apenas `iniesta.mp4` |

A primeira medição da lista em `localhost` observou 95.092 bytes, incluindo 1.071 bytes do CSS de fontes. A diferença para a rodada final vem do cache externo e de ajustes pequenos no HTML. Nenhuma medição inicial pediu MP4 ou partida completa. Os valores de reprodução vêm da rodada anterior em `localhost`, com os mesmos MP4 e hashes. A tabela reúne essas duas rodadas, sem tratar o resultado como uma única sessão fria.

As quatro jogadas foram conferidas visualmente, com construção e desfecho: [Suárez](suarez.png), [Neymar](neymar.png), [defesa](bravo.png) e [Iniesta](iniesta.png). Os players chegaram ao fim sem erro e permitiram buscar dentro do corte; os intervalos buscáveis cobriram os 27 ou 28 segundos completos. O campo `fullPlayback` dos resultados brutos registra `ended: true` e o tempo final dos quatro players, em uma rodada adicional a 4×. A [tela de análise](analysis.png) usa quadros reais e revela anotações existentes. O [detalhe final](detail-final.png) mantém as proporções das imagens e separa os três referenciais de tempo.

A revisão independente de Claude Opus 5.5 não encontrou defeitos de código. Apontou duas lacunas na evidência, corrigidas com os registros `fullPlayback` e a nova captura do detalhe, agora com a linha do tempo visível.

Com um vídeo em reprodução, trocar variante, trocar tela ou filtrar o evento removeu sua fonte e deixou o vídeo anterior pausado. Um fetch artificialmente pendente confirmou o cancelamento ao trocar de detalhe. O T3 não alterou `document.hidden` ao trocar abas pela ferramenta, então o tratamento de aba oculta foi verificado injetando esse estado e disparando `visibilitychange`; não foi uma troca de aba nativa. O [CSV baixado pela interface](cortes_selecionados.csv) contém quatro linhas com os valores do manifesto. A gravação da sessão permanece no caminho de evidência registrado no JSON, fora do build e do Git.

## Cloudflare

Consulta em 21 de outubro de 2026. `site/wrangler.jsonc` configura o Worker `ihc-prototipo`, domínio `ihc.p4cs.com.br`, Static Assets em `site/public` e D1 `ihc-feedback` para o formulário. Não há R2, Stream ou backend de detecção configurado. `wrangler deployments list` confirmou a versão publicada `bfa18dd8-c68a-4812-8a7f-055787ac2cf2`, criada em 16 de outubro. Esta alteração foi validada localmente, sem publicar uma versão nova.

O build inclui somente 8.263.209 bytes de mídia e manifesto, cerca de 8,26 MB decimais. Os quatro MP4 representam 8.182.448 bytes, cerca de 7,80 MiB. A amostra CRF 26 e este relatório não entram no build. O maior arquivo tem 2.128.284 bytes, abaixo do limite de 25 MiB por Static Asset.

Segundo os [preços de Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/), requisições desses assets são gratuitas e ilimitadas e seu armazenamento não tem custo adicional. Na configuração atual, arquivos encontrados são servidos antes do Worker; não há `run_worker_first`. Vídeos não consultam D1. A estimativa incremental de servir estes clipes é US$ 0 por mês sob essa tabela.

A assinatura e o consumo agregado da conta não foram consultados. Esta estimativa não afirma o total da fatura. Se for necessário contratar Workers Paid, sua assinatura começa em US$ 5 por mês, compartilhada com o restante da conta. O formulário continua sujeito aos limites do Worker e do D1. Veja os [preços de Workers](https://developers.cloudflare.com/workers/platform/pricing/) e os [limites de Static Assets](https://developers.cloudflare.com/workers/platform/limits/). A estimativa se refere ao produto Workers Static Assets, sem presumir que um plano genérico de CDN oferece hospedagem irrestrita de vídeo.

Hipóteses de tráfego, sem descontar cache do navegador e sem downloads adicionais:

| Visitas mensais | Cortes por visita | Downloads de MP4 | Corpos de MP4 transferidos |
|---|---|---|---|
| 1.000 | 2, em média uniforme entre os quatro | 2.000 | 4,09 GB |
| 1.000 | Os quatro | 4.000 | 8,18 GB |
| 10.000 | Os quatro | 40.000 | 81,82 GB |

Esses valores somam o conteúdo dos MP4. HTML, manifesto, miniaturas, fontes e cabeçalhos ficam fora da projeção acima. Reproduções do corte já carregado podem usar o objeto em memória; revisitas e trocas podem aproveitar o cache HTTP. Consumo e cobranças de outros projetos da conta ficam fora da estimativa.
