# Formulário de inspeção heurística de Melhores Momentos

Faça uma cópia por integrante para a [Entrega 13](../docs/13_avaliacao_heuristica.md). Preencha avaliador, data, URL, commit, navegador, largura da janela e meios de interação usados.

## Inspecione o protótipo

1. Percorra o fluxo normal para se familiarizar. Depois aplique as dez heurísticas a todas as telas e estados da tabela.
2. Registre o contexto, a ação, o efeito e a evidência de cada problema. Atribua severidade de 0 a 4 e justifique pela frequência esperada, pelo impacto e pela persistência.
3. Conclua a inspeção antes de discutir os achados com os demais. Na consolidação, reúna ocorrências equivalentes e preserve os IDs de origem.
4. Depois da inspeção, reúna com a equipe dez exemplos didáticos, um por heurística. A mesma heurística pode ter uma violação em um estado e um bom exemplo em outro. Use a seção [Uso das heurísticas](../docs/13_avaliacao_heuristica.md#8-uso-das-heurísticas) da Entrega 13.

| Tela ou percurso | Estados a examinar | Cobertura e evidências |
|---|---|---|
| F01, entrada | Carregamento dos exemplos, envio próprio indisponível. Indisponibilidade de manifesto se reproduzida em condição controlada. | |
| F02, lote | Quatro tempos, remoção, lote vazio, reposição dos exemplos, escolha de cenário normal, falha e vídeo sem lances. | |
| F03, análise | Fila, processamento, resultados parciais, conclusão, falha encenada e vídeo concluído sem lances. Transições para F04. | |
| F04, destaques | Lista A, trilhas B, mosaico C, buscas sem resultado e limpeza, filtros disponíveis, atualização parcial e preservação da seleção ao trocar de modo. | |
| F04, falha | Identificação do vídeo, resultados preservados, confirmação e cancelamento de nova tentativa localizada, opção de deixar pendente. | |
| F05, detalhe | Origem e tempos, reprodução, falha de mídia se reproduzida, nova tentativa do player, inclusão e retirada, retorno à base. | |
| F06, obtenção | Seleção vazia, abertura e fechamento do diálogo, diferenças entre CSV e MP4, arquivos salvos e comportamento do navegador. | |
| Navegação transversal | Página ativa, foco, teclado, retorno à tela anterior, contexto durante a sessão e efeito da recarga. | |

Em QA10, confira se a falha identifica o vídeo, distingue o material pronto do trecho incompleto e mantém as demais entradas ao tentar novamente ou deixar pendente. A versão de referência e a relação com as tarefas constam no [plano DECIDE](../docs/12_planejamento_avaliacao.md).

## Cobertura H1 a H10

| ID | Heurística | Telas e estados verificados | Violação e IDs |
|---|---|---|---|
| H1 | Visibilidade do status do sistema | | |
| H2 | Compatibilidade entre o sistema e o mundo real | | |
| H3 | Controle e liberdade do usuário | | |
| H4 | Consistência e padrões | | |
| H5 | Prevenção de erros | | |
| H6 | Reconhecimento em vez de memorização | | |
| H7 | Flexibilidade e eficiência de uso | | |
| H8 | Estética e design minimalista | | |
| H9 | Reconhecer, diagnosticar e recuperar-se de erros | | |
| H10 | Ajuda e documentação | | |

## Violações observadas

Siga o [Modelo 02 da disciplina](../slides_plinio/Modelo%2002%20Avaliacao%20Heuristica.doc). Inclua uma captura da tela com a região do problema destacada e descreva a violação. Se faltar um elemento, marque onde a ausência afeta a interação.

| ID | Heurística | Tela e estado | Ação e problema observado | Consequência | Evidência | Severidade 0–4 e justificativa | Recomendação |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
