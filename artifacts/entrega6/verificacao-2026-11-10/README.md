# Verificação técnica da versão 2 do protótipo

Verificação de 10/11/2026 do [protótipo principal](../../../assets/06_prototipos/PROTOTIPO_fluxo_highlights.html), versão 2. Os scripts abrem o HTML local no Chromium, sem publicação, e percorrem as telas com cliques e teclas. Na tela 3 os cortes reais são reproduzidos em 2× até a revelação dos lances.

Esta é uma verificação do funcionamento das telas. Não é uma sessão com participante e não indica se as pessoas compreendem as telas revisadas. O roteiro dessa verificação está na [seção 5.3 da Entrega 6](../../../docs/06_prototipacao_papel.md).

## Como repetir

```sh
python3 -m http.server 8762 -d assets/06_prototipos      # protótipo v2
uv run --with playwright python artifacts/entrega6/verificacao-2026-11-10/percurso_principal.py
uv run --with playwright python artifacts/entrega6/verificacao-2026-11-10/conclusao_tela3.py
uv run --with playwright python artifacts/entrega6/verificacao-2026-11-10/percursos_encenados.py
python3 artifacts/entrega6/verificacao-2026-11-10/contraste_trilhas.py
```

Os scripts usam o Chromium em `/usr/bin/chromium`; ajuste `executable_path` se ele estiver em outro lugar. Passar uma pasta como argumento grava as capturas nela. `capturas_v1.py` espera a versão 1, `git show bce19c4:assets/06_prototipos/PROTOTIPO_fluxo_highlights.html`, servida na porta 8761 com a pasta `media` ao lado.

## Resultado em 10/11/2026

| Script | Percurso | Resultado |
|---|---|---|
| `percurso_principal.py` | Iniciar, abrir a base pelo botão com a análise em andamento, receber lances novos, terminar em segundo plano, selecionar dois lances, baixar a lista CSV e os dois MP4 | 14 de 14 verificações. CSV com cabeçalho e 2 linhas; `suarez.mp4` com 2.051.038 bytes e `bravo.mp4` com 2.128.284 bytes, iguais ao manifesto |
| `conclusao_tela3.py` | Voltar da base ao acompanhamento e esperar o fim da análise na tela 3 | 5 de 5. Ao fim, **✓ Análise concluída. 8 lances prontos para revisar** e **Ver os 8 lances na base →** |
| `percursos_encenados.py` | Falha em um vídeo, assistida na tela 3 até a falha, pendência e nova tentativa; vídeo sem lances e busca sem correspondência | 18 de 18. Só o 1º tempo de Bayern x Real Madrid falha, em 35:19; 7 lances ficam na base e a nova tentativa completa os 8 |
| `contraste_trilhas.py` | Contraste WCAG das etiquetas da alternativa B, v1 e v2, calculado das cores do CSS | Tabela reproduzida na seção 5.1 da Entrega 6 |

Nenhuma execução registrou erro de JavaScript na página. O download de vários MP4 de uma vez foi aceito pelo Chromium automatizado; em navegadores com bloqueio de downloads múltiplos, a lista do painel oferece os links individuais.
