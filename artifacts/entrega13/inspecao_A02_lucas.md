# Ficha individual de inspeção heurística — Avaliador A02

**Autor:** Lucas Roberto Boccia dos Santos — 22.123.012-1\
**Data da inspeção:** {{dd/mm/aaaa}}\
**Status:** ⬜ pendente\

## Dados da sessão

| Campo | Registro |
|---|---|
| URL avaliada | https://ihc-11.p4cs.com.br/ |
| Commit da versão publicada | `7405221` (arquivo-fonte de `7d52cdd`, publicado em 13/11/2026) |
| SHA-256 conferido do HTML | `aa6ec94773a783559e352f69ff5507bd3a8af9301c3830b832de879104b6f33c` |
| Navegador e versão | {{ex.: Chrome 131 / Firefox 133}} |
| Largura da janela (viewport) | {{ex.: 1440×900 px}} |
| Meios de interação usados | {{ex.: mouse e teclado (Tab, Enter, setas, Esc)}} |

> **Regra de independência:** conclua esta ficha antes de ler as fichas de A01 e A03 ou discutir achados com a equipe. Avalie apenas a interface do protótipo, não a acurácia do modelo de visão computacional do TCC.

## Procedimento rápido

1. Percorra o fluxo normal (`F01` até `F06`) uma vez para familiarização.
2. Inspecione sistematicamente todas as telas e estados da tabela abaixo aplicando **H1 a H10**.
3. Registre apenas violações observadas, sem forçar problemas onde não houver.
4. Salve uma captura anotada destacando a região de cada problema em `assets/13_heuristica/a02_v01.png`, `a02_v02.png` e assim por diante.
5. Atribua severidade de `0` a `4` depois de compreender o problema e justifique por **frequência**, **impacto** e **persistência**.

| Grau | Interpretação |
|---:|---|
| 0 | Não é considerado problema de usabilidade |
| 1 | Problema cosmético; corrigir se houver tempo |
| 2 | Problema menor; baixa prioridade |
| 3 | Problema maior; alta prioridade |
| 4 | Catástrofe de usabilidade; correção imperativa antes de disponibilizar |

## Cobertura de telas e estados

Marque cada grupo conforme concluir a verificação. Em `F04, falha`, verifique `QA10` (se a interface identifica o vídeo incompleto, distingue o material pronto do trecho afetado e preserva os demais resultados ao tentar novamente ou deixar pendente).

| Tela ou percurso | Estados a examinar | Verificado? | Observações rápidas |
|---|---|---:|---|
| F01, entrada | Carregamento dos exemplos e aviso de envio próprio indisponível. Falha de manifesto, se reproduzida em condição controlada. | [ ] | |
| F02, lote | Quatro tempos, remoção, lote vazio, reposição dos exemplos e escolha dos cenários normal, falha e vídeo sem lances. | [ ] | |
| F03, análise | Fila, processamento, resultados parciais, conclusão, falha encenada, vídeo concluído sem lances e transições para F04. | [ ] | |
| F04, destaques | Lista A, trilhas B, mosaico C, busca sem resultado e limpeza, filtros disponíveis, atualização parcial e preservação da seleção ao trocar de modo. | [ ] | |
| F04, falha (QA10) | Identificação do vídeo afetado, resultados preservados, confirmação e cancelamento de nova tentativa localizada e opção de deixar pendente. | [ ] | |
| F05, detalhe | Origem e tempos (relógio do jogo e posição no arquivo), reprodução, falha de mídia e nova tentativa (se reproduzida), inclusão/retirada e retorno à base. | [ ] | |
| F06, obtenção | Seleção vazia, abertura e fechamento do diálogo, distinção entre CSV e MP4, arquivos salvos e comportamento do navegador. | [ ] | |
| Navegação transversal | Etapa ativa na barra lateral, foco visível, navegação por teclado, retorno à tela anterior, preservação na sessão e efeito de recarga. | [ ] | |

## Matriz de cobertura das 10 heurísticas

| Heurística | Descrição | Telas e estados examinados | Houve violação? | IDs dos achados |
|---|---|---|---|---|
| H1 | Visibilidade do status do sistema | | sim / não | |
| H2 | Compatibilidade entre o sistema e o mundo real | | sim / não | |
| H3 | Controle e liberdade do usuário | | sim / não | |
| H4 | Consistência e padrões | | sim / não | |
| H5 | Prevenção de erros | | sim / não | |
| H6 | Reconhecimento em vez de memorização | | sim / não | |
| H7 | Flexibilidade e eficiência de uso | | sim / não | |
| H8 | Estética e design minimalista | | sim / não | |
| H9 | Ajudar usuários a reconhecer, diagnosticar e recuperar-se de erros | | sim / não | |
| H10 | Ajuda e documentação | | sim / não | |

## Declaração de violações (Modelo 02)

Siga o [Modelo 02 da disciplina](../../slides_plinio/Modelo%2002%20Avaliacao%20Heuristica.doc). Descreva o que ocorre, onde ocorre, em qual ação e qual consequência traz para P01 ou P03. Se faltar um elemento, marque na captura onde a ausência afeta a interação.

| ID | Heurística | Tela e estado | Problema observado (ação, local e consequência) | Evidência | Severidade | Justificativa (frequência, impacto e persistência) | Recomendação |
|---|---|---|---|---|---:|---|---|
| V01 | | | | `![A02 V01](../../assets/13_heuristica/a02_v01.png)` | | | |
