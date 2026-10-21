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

Os vídeos são reais e a análise é simulada. O manifesto descreve os dois tempos de Real Madrid 0 x 4 Barcelona (LaLiga, 21/11/2015) do SoccerNet-v2, em 224p (398×224, 25 fps), e quatro cortes de 27 a 28 s tirados deles: gols de Suárez, Neymar e Iniesta e uma defesa do Barcelona. A Tela 3 do protótipo só revela, em ritmo simulado, essas anotações que já existem no SoccerNet. Nenhum modelo roda no site.

Os tempos completos ficam fora do site e o protótipo nunca os pede. Cada corte tem cerca de 2 MB e só é baixado quando a pessoa clica em reproduzir. O protótipo busca o MP4 inteiro com `fetch` e toca a partir de um blob, porque o `wrangler dev` local responde MP4 sem `Content-Length` e o Chrome deixa de permitir avançar ou voltar no vídeo.

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
