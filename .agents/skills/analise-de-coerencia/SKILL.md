---
name: analise-de-coerencia
description: Analisa a coerência documental do repositório e gera um relatório HTML com tickets numerados.
---

# Análise de coerência

Faça uma auditoria documental somente de leitura. Entregue o diagnóstico em HTML e preserve os arquivos analisados para uma etapa posterior de revisão.

## Escopo

- Trate os documentos indicados pelo usuário como foco principal. Quando nenhum documento for indicado, compare todos os documentos do repositório.
- Considere o repositório inteiro como contexto em toda execução. Inventarie todos os arquivos, leia todo texto produzido para o projeto e inspecione arquivos não textuais quando forem citados ou puderem mudar a conclusão. Registre no relatório qualquer categoria excluída e o motivo.
- Descubra a proposta do projeto e a autoridade relativa dos documentos a partir do próprio conteúdo. Use objetivos, decisões explícitas, datas, estados, referências e rastreabilidade. A ordem dos nomes dos arquivos não determina sozinha qual documento deve mudar.
- Use pesquisa na web quando ela ajudar a verificar uma afirmação, fonte ou prática externa. Cite cada fonte externa perto da conclusão que ela sustenta.
- Trabalhe sem entrevista inicial. Investigue o material disponível e avance. Quando a evidência não permitir uma conclusão segura, marque o ticket como `Precisa de revisão` e explique o que falta confirmar.

## Procedimento

1. **Cobrir o repositório.** Faça um inventário completo. Classifique arquivos como fonte textual, apoio, mídia, artefato gerado ou dependência. Leia cada fonte textual produzida para o projeto. A cobertura termina quando todo arquivo estiver lido, inspecionado ou incluído em uma categoria de exclusão justificada.

2. **Mapear o que cada documento afirma.** Extraia propósito, escopo, decisões, fatos, hipóteses, dúvidas, recomendações, público, terminologia e dependências. Anote a seção ou outra localização precisa de cada afirmação relevante. O mapa termina quando toda conclusão potencial pode ser rastreada a passagens concretas.

3. **Comparar.** Procure contradições, omissões, mudanças silenciosas de escopo, hipóteses tratadas como fatos, requisitos sem origem, recomendações sem apoio, terminologia incompatível e decisões que ignoram o contexto do projeto. Separe desalinhamento real de informação nova compatível e de diferença apenas editorial.

4. **Investigar incertezas.** Consulte referências internas e, quando trouxer ganho real, fontes externas. Evidência externa verifica fatos e práticas; decisões explícitas do projeto continuam sendo definidas pelo repositório. Se interpretações razoáveis ainda competirem, mantenha o achado e marque `Precisa de revisão`.

5. **Numerar os tickets.** Antes de criar tickets, procure em todos os relatórios existentes na pasta `análises de coerência` o maior identificador `AC-###`, inclusive identificadores preservados em comentários de tickets retirados. Comece no número seguinte. Se não houver identificador anterior, comece em `AC-001`. Cada desalinhamento recebe um identificador único, e a sequência continua entre relatórios.

6. **Escrever cada ticket.** Inclua gravidade, estado da conclusão, evidências localizáveis, efeito sobre a coerência e mudança sugerida no documento que fizer mais sentido para a proposta do projeto. Para cada recomendação analisada, verifique se é possível relacioná-la a alguma seção, atividade, hipótese ou decisão de um documento de base. Quando a relação não existir, apresente a recomendação como exploratória e sujeita a validação.

7. **Gerar o HTML.** Crie o relatório em `análises de coerência/DD-MM-YYYY-HH:MM.html`, usando a data, hora e fuso locais. Se o nome já existir, acrescente `-02`, `-03` e assim por diante, sem sobrescrever relatórios. Coloque no começo do documento a assinatura `modelo (nível de raciocínio) no harness`, com os dados reais da execução. Quando algum dado não estiver disponível, escreva `não informado` em seu lugar.

8. **Verificar.** Confirme que o HTML abre sem erro estrutural, funciona em telas pequenas, contém todos os tickets e não alterou nenhum arquivo analisado. Confira a continuidade e a unicidade dos IDs. A execução termina quando o relatório existe, todas as fontes do escopo foram contabilizadas e cada conclusão está sustentada ou marcada para revisão.

## Conteúdo do relatório

O HTML deve ser autocontido, sem scripts ou folhas de estilo externas. Use HTML semântico, CSS inline, tema claro e escuro conforme o sistema, contraste legível e tabelas responsivas.

Inclua no mínimo:

- assinatura do agente no início;
- data e escopo da análise;
- conclusão geral;
- cobertura do repositório e exclusões;
- pontos que já estão alinhados;
- tickets `AC-###`, organizados para leitura rápida;
- limitações da análise e fontes externas usadas.

Use nomes relativos ao repositório e seções para localizar evidências. Não exponha caminhos absolutos da máquina. Recomendações devem dizer qual documento mudaria e o que mudaria, sem editar o documento.

## Revisão de um relatório existente

Quando o usuário pedir ajustes no HTML, edite apenas o relatório indicado. Preserve os IDs dos tickets mantidos. Ao retirar um ticket, conserve seu identificador em um comentário HTML no formato `<!-- ticket-retirado: AC-### -->`; isso impede que o número seja reutilizado em relatórios futuros.
