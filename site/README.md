# Publicação em ihc.p4cs.com.br

Worker `ihc-prototipo` com arquivos estáticos e um banco D1 para os feedbacks do guia da simulação.

| Caminho | Origem |
|---|---|
| `/` | [`PROTOTIPO_fluxo_highlights.html`](../assets/06_prototipos/PROTOTIPO_fluxo_highlights.html) |
| `/guia` | [`GUIA_simulacao.html`](../assets/06_prototipos/GUIA_simulacao.html) |
| `POST /api/feedback` | [`src/worker.js`](src/worker.js), grava na tabela `feedback` do D1 `ihc-feedback` |

`build.sh` copia os HTML para `public/` antes de cada `dev` e `deploy`. Edite os arquivos em `assets/06_prototipos`, não em `public/`.

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
