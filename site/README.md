# Publicação em ihc.p4cs.com.br

Worker `ihc-prototipo` com arquivos estáticos e um banco D1 para os feedbacks do guia da simulação.

| Caminho | Origem |
|---|---|
| `/` | [`PROTOTIPO_fluxo_highlights.html`](../assets/06_prototipos/PROTOTIPO_fluxo_highlights.html) |
| `/guia` | [`GUIA_simulacao.html`](../assets/06_prototipos/GUIA_simulacao.html) |
| `/media/*` | [`media/manifest.json`](../assets/06_prototipos/media/manifest.json) e os MP4/JPG que ele referencia |
| `POST /api/feedback` | [`src/worker.js`](src/worker.js), grava na tabela `feedback` do D1 `ihc-feedback` |

`build.sh` copia os HTML para `public/` antes de cada `dev` e `deploy`, junto com `media/manifest.json` e só os MP4 e JPG listados nele (`src` e `poster` de cada corte). Edite os arquivos em `assets/06_prototipos`, não em `public/`.

## Mídia

Os vídeos são reais e a análise é simulada. O manifesto descreve os quatro tempos de duas partidas do SoccerNet-v2, em 224p (398×224, 25 fps): Real Madrid 0 x 4 Barcelona (LaLiga, 21/11/2015) e Bayern de Munique 1 x 2 Real Madrid (Liga dos Campeões, 12/04/2017). Dele saem oito cortes de 27 a 28 s, dois por tempo. Nenhum modelo roda no site.

A Tela 3 toca, em 2× e sem som, os cortes de cada tempo na ordem do arquivo, dois tempos por vez, um em cada prévia. O lance aparece quando o vídeo passa pelo instante anotado no SoccerNet. A trilha de progresso por vídeo enche conforme o vídeo toca e passa pela posição de cada anotação no instante em que o lance é revelado; o marcador chega à trilha logo depois, ao fim da animação. Com os cortes em cache, a análise leva cerca de um minuto. Sair da Tela 3 ou esconder a aba pausa os vídeos; reiniciar descarta os vídeos e lances anteriores.

Os tempos completos ficam fora do site e o protótipo nunca os pede. Os cortes, cerca de 2 MB cada e 16,2 MB no total, começam a baixar quando a pessoa clica em usar os exemplos, na ordem em que a Tela 3 vai precisar deles. Se um corte não chegou, a prévia mostra o quadro dele e espera, sem avançar o progresso. Cada corte é buscado inteiro com `fetch` e tocado a partir de um blob, porque o `wrangler dev` local responde MP4 sem `Content-Length` e o Chrome deixa de permitir avançar ou voltar no vídeo.

Em contexto seguro (HTTPS ou `localhost`), os blobs ficam na Cache API do navegador (`ihc-cortes`), com o sha256 do manifesto na chave; fora dele, ficam só na memória da aba. Numa nova visita a Tela 3 e o player da Tela 4 leem dali, sem nenhuma requisição de MP4. Um corte reextraído muda de chave, e as entradas que o manifesto não cita mais são apagadas ao carregar a página. O cache HTTP sozinho não bastaria: os assets do Worker saem com `Cache-Control: public, max-age=0, must-revalidate`, então cada visita revalidaria cada corte. Nada de vídeo vai para `localStorage`.

O HTML lê `media/manifest.json` por caminho relativo, então funciona servido de `assets/06_prototipos/` (por exemplo `python3 -m http.server` nessa pasta) e do site publicado. Aberto direto do disco (`file://`), o navegador bloqueia o `fetch` e a primeira tela mostra o erro.

O download da Tela 4 é um CSV com, para cada corte escolhido, partida, tempo, anotação, instante no arquivo, início e fim do corte no arquivo, instante do lance dentro do corte, duração e URL do MP4. Cada lance também tem um link para baixar o próprio MP4.

```sh
cd site
npx wrangler d1 migrations apply ihc-feedback --remote   # só quando houver migração nova
npx wrangler deploy
```

Ler os feedbacks:

```sh
npx wrangler d1 execute ihc-feedback --remote --json \
  --command "SELECT id, criado_em, respostas FROM feedback ORDER BY id"
```

Para testar localmente, rode `npx wrangler d1 migrations apply ihc-feedback --local` e depois `npx wrangler dev`.

## Preview de uma branch

O bloco `previews` usa o D1 `ihc-feedback-preview`, separado do banco de produção. Os previews compartilham esse banco de teste. Os assets vêm do build da branch, sem publicar no domínio de produção.

Com Wrangler 4.135.0 ou mais recente, execute em `site/`:

```sh
npx wrangler d1 migrations apply ihc-feedback --remote --preview
npx wrangler preview --name real-soccernet-clips
```

O comando de preview executa `build.sh` e retorna as URLs da branch e da implantação. Use um nome diferente para outra branch. A publicação de preview é manual; não há workflow de GitHub Actions neste repositório.
