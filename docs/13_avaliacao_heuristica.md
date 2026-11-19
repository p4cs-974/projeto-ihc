# Entrega 13 — Avaliação de IHC por inspeção heurística

**Data:** {{dd/mm/aaaa}}  
**Status:** ⬜ não iniciada  
**Responsabilidade:** 1 avaliação completa por integrante, sobre todas as telas/estados relevantes do projeto.

## Objetivo da atividade

Encontrar problemas de usabilidade por inspeção sistemática da interface com as **10 heurísticas de Nielsen**. Cada avaliador trabalha individualmente primeiro; depois a equipe consolida problemas duplicados e prioridades.

Use a matriz de cobertura para registrar a inspeção das dez heurísticas. Registre as violações observadas e reúna um exemplo positivo por heurística na atividade didática ao final.

## 1. Heurísticas adotadas

1. Visibilidade do status do sistema
2. Compatibilidade entre o sistema e o mundo real
3. Controle e liberdade do usuário
4. Consistência e padrões
5. Prevenção de erros
6. Reconhecimento em vez de memorização
7. Flexibilidade e eficiência de uso
8. Estética e design minimalista
9. Ajudar usuários a reconhecer, diagnosticar e recuperar-se de erros
10. Ajuda e documentação

## Cobertura especial para interfaces administrativas e analíticas

Quando existirem, não limite a avaliação às “telas principais”. Inspecione também:

- dashboard em estados normal, vazio e erro;
- filtros sem resultado e filtros combinados;
- relatórios e exportação;
- histórico/listas longas;
- formulários CRUD (criação, edição, exclusão, validação);
- alteração de perfil/permissão;
- confirmações de ações destrutivas;
- processamento/loading/progresso;
- falha e recuperação;
- comparação de resultados;
- mensagens de termos técnicos, métricas e recomendações;
- ajuda/documentação contextual.

Em TCCs técnicos, observe especialmente se a interface comunica o estado do processamento e traduz informações técnicas para o vocabulário do usuário escolhido.

## 2. Escopo da inspeção

| Item | Definição |
|---|---|
| Versão avaliada | {{link/commit/data}} |
| Telas/estados | {{lista completa}} |
| Fluxos | {{M01/M02...}} |
| Dispositivo/viewport | {{...}} |
| Avaliadores | {{nomes}} |

## Processo e fluxograma da avaliação heurística

O relatório da equipe inclui o fluxograma da inspeção. Represente a preparação, a inspeção individual de cada tela e estado com H1–H10, o registro e a interpretação das violações, a reunião de consolidação e o relato final. Mostre no fluxo a repetição das verificações e quando os avaliadores se reúnem.

## 3. Procedimento individual

Cada avaliador deve:

1. percorrer os fluxos/telas ao menos uma vez para familiarização;
2. inspecionar novamente aplicando sistematicamente H1–H10;
3. registrar cada problema com evidência e contexto;
4. atribuir severidade **depois de compreender bem o problema**, justificando a decisão;
5. não discutir achados com os demais antes de terminar a inspeção individual, quando o objetivo for preservar independência.

### Escala de severidade (0–4)

| Grau | Interpretação |
|---:|---|
| 0 | não é considerado problema de usabilidade |
| 1 | problema cosmético; corrigir se houver tempo |
| 2 | problema menor; baixa prioridade |
| 3 | problema maior; alta prioridade |
| 4 | catástrofe de usabilidade; correção imperativa antes de disponibilizar |

Ao justificar, considere **frequência, impacto e persistência** do problema no contexto real de uso.

---

## Avaliador A01 — {{nome}}

### 4. Matriz de cobertura das 10 heurísticas

| Heurística | Telas/fluxos examinados | Houve violação? | IDs dos achados |
|---|---|---|---|
| H1 | {{...}} | sim/não | {{V01...}} |
| H2 | {{...}} | sim/não | |
| H3 | {{...}} | sim/não | |
| H4 | {{...}} | sim/não | |
| H5 | {{...}} | sim/não | |
| H6 | {{...}} | sim/não | |
| H7 | {{...}} | sim/não | |
| H8 | {{...}} | sim/não | |
| H9 | {{...}} | sim/não | |
| H10 | {{...}} | sim/não | |

### 5. Declaração de violações

Use o [Modelo 02 da disciplina](../slides_plinio/Modelo%2002%20Avaliacao%20Heuristica.doc) para relatar as violações. Destaque na captura de tela a região onde ocorre o problema e descreva a ação, o efeito e a correção sugerida.

| ID | Heurística | Tela/estado | Problema observado | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---:|---|---|
| V01 | H1 | {{F02}} | {{o que ocorre, em que ação e qual consequência}} | ![print](../assets/13_heuristica/v01.svg) | 3 | {{frequência/impacto/persistência}} | {{correção específica}} |

**Qualidade do relato:** o problema deve ser observável e localizado. Evite “interface confusa” sem dizer **o que**, **onde**, **quando** e **para quem**.

> Repita a seção para A02, A03... um avaliador por integrante.

## 6. Consolidação da equipe

Problemas iguais ou muito semelhantes encontrados por avaliadores diferentes devem ser consolidados, preservando quem os encontrou.

| ID consolidado | Achados individuais | Heurística | Problema | Severidade final | Prioridade | Responsável pela correção |
|---|---|---|---|---:|---|---|
| HC01 | V01(A01), V04(A02) | H1 | {{...}} | {{...}} | alta | {{...}} |

## 7. Síntese e plano de melhoria

- Quantidade de problemas por heurística e severidade.
- Problemas críticos/graves que bloqueiam teste ou release.
- Padrões recorrentes entre telas.
- Correções que serão feitas antes/para a avaliação com usuários.

## 8. Uso das heurísticas

Reúna dez exemplos didáticos no protótipo, um por heurística. Uma heurística com violação em uma tela também pode ser ilustrada com um caso que a atende em outra tela ou estado.

| Heurística | Tela e estado | Exemplo no protótipo | Evidência | Por que atende |
|---|---|---|---|---|
| H1 | | | | |
| H2 | | | | |
| H3 | | | | |
| H4 | | | | |
| H5 | | | | |
| H6 | | | | |
| H7 | | | | |
| H8 | | | | |
| H9 | | | | |
| H10 | | | | |

## Checklist

- [ ] O fluxograma mostra a inspeção individual, a repetição das verificações e a consolidação da equipe.
- [ ] Cada integrante fez uma inspeção completa e identificada.
- [ ] Todas as telas/estados relevantes foram examinados.
- [ ] Estados administrativos, filtros, relatórios, históricos, processamento e erros foram incluídos quando existentes.
- [ ] A inspeção avaliou a interface/protótipo, não o mérito técnico do algoritmo/modelo.
- [ ] H1–H10 aparecem na matriz de cobertura de cada avaliador.
- [ ] Parte de violações contém apenas violações, sem “forçar” exemplos.
- [ ] Todo problema tem print/localização e contexto.
- [ ] Severidade possui justificativa, não apenas número.
- [ ] Recomendação resolve a causa ou reduz o impacto.
- [ ] Achados duplicados foram consolidados ao final.
- [ ] A seção Uso das heurísticas apresenta dez exemplos positivos com evidência, um por heurística.
