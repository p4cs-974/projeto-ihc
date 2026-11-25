# Checklist final do projeto

**Revisão de fechamento: 25/11/2026.** Este checklist registra o estado da entrega com a única sessão exploratória disponível (`EXP01`). `[x]` indica atendimento documental verificado ou condição explicitamente não aplicável; `[ ]` indica requisito não atendido ou não comprovado, com a razão registrada. Os itens abertos não constituem promessa de coleta ou gravação adicional. Não se presume aprovação docente para a redução da amostra.

Foram conferidos os caminhos e as âncoras dos links locais do README, desta lista, da rastreabilidade e das 14 entregas. Os cálculos da Entrega 13 foram reproduzidos a partir das fichas e da consolidação. A inspeção visual completa de todos os diagramas antigos e a conferência online de permissões externas não foram repetidas nesta revisão. As evidências e limitações detalhadas estão na [Entrega 14](docs/14_observacao_usuario.md).

## Relação entre TCC e escopo de IHC

- [x] Está claro qual é o **tema/contribuição do TCC** e qual é o **escopo de IHC da disciplina**.
- [x] A equipe registrou se o TCC já previa interface, previa parcialmente ou não previa.
- [x] Se o TCC não previa interface, a equipe explicou como derivou o recorte de IHC a partir da contribuição técnica.
- [x] O usuário escolhido para IHC é plausível e possui relação clara com o valor produzido pelo tema do TCC.
- [x] O objetivo do usuário é descrito como resultado no mundo real, e não como “usar o sistema”.
- [x] A interface da disciplina não é apresentada como obrigação formal do TCC, salvo se isso tiver sido acordado com o orientador.
- [x] O recorte de IHC é pequeno o suficiente para ser modelado, prototipado e avaliado durante a disciplina. Escopo delimitado e modelado; avaliação por observação encerrada com limitações de cobertura.
- [x] O projeto consegue explicar a cadeia **problema humano → contribuição computacional → forma de uso → impacto potencial**.

## Estrutura e apresentação

- [x] O README explica problema, público, contexto, contribuição do TCC e recorte de IHC.
- [x] Todos os 14 arquivos de entrega estão linkados e abrem corretamente.
- [x] Não existem links locais quebrados.
- [ ] Imagens e diagramas são legíveis no GitHub. **Não atendido/sem comprovação:** A legibilidade de todos os artefatos antigos no GitHub não foi revalidada neste fechamento; o fluxograma final foi renderizado e inspecionado localmente.
- [x] Arquivos editáveis dos principais diagramas foram preservados quando possível. Fontes SVG/HTML e demais fontes disponíveis estão versionadas.
- [x] Entregas individuais identificam o autor.
- [ ] As quantidades mínimas por integrante foram atendidas. **Não atendido/sem comprovação:** Não atendido na observação: uma pessoa em exploração guiada, ante três sessões estruturadas previstas.
- [ ] Links externos (Figma, Forms, vídeos) foram testados sem autenticação privilegiada. **Sem comprovação completa:** O protótipo usa HTML em vez de Figma; seu acesso foi documentado na Entrega 11. As ferramentas não carregaram o protótipo e o vídeo na tentativa deste fechamento. O link do vídeo foi fornecido pela equipe e está no README e na Entrega 14, sem confirmação independente de reprodução ou permissões.

## Coerência de IHC

- [ ] Público-alvo, personas e participantes de pesquisa/teste são coerentes com o escopo de IHC. **Não atendido/sem comprovação:** O escopo dos modelos é coerente; o perfil de EXP01 não foi verificado e a pesquisa I01–I03 não foi executada.
- [x] Cenários de problema descrevem o problema/atividade sem antecipar a solução.
- [x] Tarefas analisadas correspondem a objetivos importantes das personas.
- [x] Modelo conceitual, signos e MoLIC usam terminologia consistente.
- [x] MoLIC contém caminhos principais, alternativas e rupturas relevantes.
- [ ] O Figma cobre os fluxos modelados e não cria funcionalidades críticas sem rastreabilidade. **Não atendido/sem comprovação:** O artefato adotado é HTML navegável; a cobertura dos modelos é parcial e está discriminada na Entrega 11.
- [x] Metas de usabilidade são verificáveis.
- [x] Em projetos técnicos, resultados do algoritmo/modelo foram traduzidos para linguagem e decisões compreensíveis ao perfil de usuário escolhido.

## Justificativa das telas e padrões

- [x] Cada tela importante possui relação com uma tarefa/objetivo rastreável.
- [x] Dashboard, se existente, apoia uma decisão ou necessidade de acompanhamento concreta. O acompanhamento de processamento tem vínculo com T03; não foi introduzido dashboard administrativo genérico.
- [x] Relatórios apresentam informação necessária para uma tarefa, e não apenas “números porque existem”.
- [x] Histórico, busca, ordenação e filtros possuem volume/uso que justifique sua existência. Filtros limitados à demonstração; histórico permanente e escala profissional não são declarados validados.
- [x] Telas administrativas existem porque há atividades reais de configuração, governança ou operação. Não aplicável: telas administrativas não foram adotadas no recorte.
- [x] CRUDs representam entidades e tarefas relevantes; não foram criados apenas para aumentar o número de telas. Não aplicável: CRUD administrativo não foi adotado.
- [x] Gestão de usuários/perfis/permissões, se existente, considera papéis, prevenção de erros e consequências de alterações. Não aplicável: autenticação e gestão de contas não integram o protótipo.
- [x] Telas de configuração não expõem complexidade técnica desnecessária sem justificativa. Não há configuração técnica de detector exposta; as limitações da demonstração estão descritas.
- [x] Estados de carregamento, processamento, vazio, erro, sucesso e recuperação foram considerados quando pertinentes.
- [x] Comparações e visualizações ajudam o usuário a interpretar diferenças e tomar decisões.

## Avaliação

- [x] Cada avaliador heurístico percorreu todas as telas/estados relevantes. Cobertura declarada nas três fichas; o pedido nativo de múltiplos downloads não apareceu na configuração usada.
- [x] As 10 heurísticas foram explicitamente verificadas por cada avaliador.
- [x] Violações têm evidência, localização, severidade justificada e recomendação.
- [x] Problemas duplicados entre avaliadores foram consolidados sem apagar a autoria da descoberta.
- [ ] O número final de usuários observados atende ao exigido pela disciplina. **Não atendido/sem comprovação:** Não atendido: uma pessoa observada em EXP01, sem as três sessões estruturadas previstas. Não há dispensa docente registrada.
- [ ] Participantes finais representam o público-alvo e não são membros da equipe. **Não atendido/sem comprovação:** EXP01 é externo à equipe, mas idade e experiência do perfil-alvo não foram verificadas pelo pré-teste.
- [x] Se o perfil profissional é difícil de recrutar, qualquer uso de participante aproximado/proxy foi justificado e registrado como limitação. EXP01 é apresentado como perfil não verificado, sem ser promovido a editor profissional ou participante representativo.
- [x] Tarefas de teste possuem cenário, instrução neutra e critério de sucesso. Definidos na Entrega 12; não aplicados no formato estruturado em EXP01.
- [ ] Tempos, erros, ajudas, sucesso e satisfação foram registrados por usuário/tarefa. **Não atendido/sem comprovação:** Há observações e intervenções qualitativas, sem cronometragem padronizada, notas 1–5 ou classificação válida de sucesso independente.
- [x] A avaliação mede a **interação com o protótipo**, e não tenta substituir a avaliação técnica/científica do algoritmo ou modelo do TCC.
- [x] A conclusão identifica padrões, problemas prioritários e mudanças concretas. Padrões internos da única sessão e recomendações fundamentadas; sem inferir recorrência populacional ou implementação.

## Ética e privacidade

- [ ] Há consentimento compatível com a atividade realizada. **Não atendido/sem comprovação:** Há aceite verbal para voz/opinião; as autorizações separadas e o alcance de compartilhamento audiovisual não foram comprovados integralmente.
- [ ] O participante sabe que pode interromper a participação. **Não atendido/sem comprovação:** A informação não foi registrada no áudio de EXP01; constava no protocolo original.
- [x] Dados pessoais desnecessários não foram coletados/publicados. As evidências locais foram higienizadas: nomes substituídos e quadro com notificação removido. O bruto fica fora do Git.
- [ ] Vídeos/áudios/imagens de participantes só são compartilhados com autorização. **Sem comprovação completa:** O Git contém transcrição e quadros higienizados. O endereço do vídeo externo foi fornecido pela equipe para a entrega; o registro disponível contém aceite verbal para voz/opinião, sem comprovação separada do alcance da autorização audiovisual.
- [x] Resultados públicos usam IDs anônimos (`U01`, `U02`...). EXP01 identifica a sessão de observação; U01 da Entrega 6 pertence a outro registro.

## Comunicação e INOVA

- [x] A equipe consegue explicar o projeto sem depender apenas de jargão técnico. README apresenta a explicação; desempenho em apresentação oral não foi avaliado.
- [x] O protótipo demonstra como uma pessoa poderia usar ou se beneficiar da contribuição técnica.
- [x] A apresentação deixa claro o que é resultado real do TCC e o que é hipótese/protótipo da disciplina.
- [x] O potencial de aplicação, mercado ou extensão é apresentado sem afirmar validações que ainda não ocorreram.
