# Relatório do Backlog - Histórias de Usuário

Total de Histórias encontradas: **30**

Total de Story Points: **118**

---

### [SCRUM-45] HMS-US036: Registrar andamentos processuais do caso
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como advogado ou paralegal, quero visualizar os andamentos processuais derivados de outros fluxos na timeline do caso, para que o histórico seja completo sem dupla digitação.
  > 
  > *Rastreabilidade:* RF-023 (v1.2), RF-028.
  > *Telas Pencil:* Advogado - Caso Detalhe: Andamentos
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — Andamentos derivados (não manuais):* No MVP, andamentos são derivados de: baixa de prazo, protocolo (RF-022), comunicação relevante. Botão "Registrar andamento" removido da aba.
  > * [ ] *CA02 — Visibilidade dupla:* visivel_cliente (FALSE padrão) e visivel_terceiro (FALSE padrão). Ambos os badges sempre visíveis na timeline.
  > * [ ] *CA03 — Tipos fechados no MVP:* Audiência realizada, Publicação recebida, Notificação. Pendência: lista fechada ou configurável pelo admin?
  > * [ ] *CA04 — Timeline de eventos:* Seção "Andamentos" exibe timeline de eventos derivados em ordem cronológica inversa.
  > * [ ] *CA05 — Evolução pós-MVP:* Mecanismo de promoção (checkbox "promover a andamento?" ao dar baixa em prazo, registrar protocolo ou comunicação relevante). Eventos externos sem fluxo de origem ficam sem representação até evolução.

### [SCRUM-43] HMS-US034: Registrar ato de protocolo, distribuição ou entrega
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como advogado ou paralegal, quero registrar o ato de protocolo judicial, administrativo, distribuição ou entrega ao cliente, para que o caso avance para "Em execução/acompanhamento" com o ato devidamente documentado.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Campos obrigatórios: tipo de ato (Protocolo judicial · Protocolo administrativo · Distribuição · Entrega ao cliente), data/hora do ato (não pode ser futura), responsável e peça vinculada.
  > * CA02 - Número de protocolo é obrigatório quando tipo = protocolo judicial ou administrativo.
  > * CA03 - Ao salvar, o caso avança para "Protocolado/distribuído/entregue" e em seguida para "Em execução/acompanhamento".
  > * CA04 - Em caso de falha técnica no protocolo eletrônico, o usuário registra a contingência (protocolo manual realizado) com descrição e o sistema registra o evento.
  > * CA05 - Entrega parcial permite registro indicando quais entregáveis foram entregues; pendências para os restantes são mantidas.

### [SCRUM-44] HMS-US035: Gerenciar prazos e tarefas do caso em execução
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como advogado ou paralegal, quero criar, monitorar e concluir prazos, tarefas, audiências e publicações do caso, para que todos os compromissos sejam rastreados com alerta antecipado e sem perda de prazo.
  > 
  > *Rastreabilidade:* RF-023 (v1.2).
  > *Telas Pencil:* Advogado - Caso Detalhe: Prazos e Tarefas / Modal Nova Tarefa ou Prazo
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — Responsáveis unificados:* Campo único aceita 1..N responsáveis, sem distinção obrigatória advogado/paralegal na UI. Qualquer responsável recebe alertas. Sistema exibe aviso (não bloqueio) se prazo processual tiver apenas 1 responsável.
  > * [ ] *CA02 — 6 tipos fechados:* Prazo processual, Audiência, Publicação, Tarefa interna, Entrega, Outro. Tipo "Prazo processual" ativa automaticamente criticidade máxima (alerta antecipado, escalonamento, bloqueio de encerramento).
  > * [ ] *CA03 — Campos temporais condicionais:* Audiência = data + hora obrigatórias; Prazo processual = data obrigatória, hora opcional (default 23:59); Publicação = ambas opcionais; Tarefa/Entrega/Outro = data obrigatória, hora opcional.
  > * [ ] *CA04 — Status derivado (não escolhido):* Status = resultado de tipo + tempo + ação. Estados: Crítico, Vencida, Agendada, Aguardando, Em andamento, Concluída. Usuário não escolhe status no formulário.
  > * [ ] *CA05 — Prazos processuais diferenciados:* Alerta antecipado ao advogado e paralegal, escalonamento ao supervisor por proximidade sem baixa, bloqueio de encerramento do caso com itens críticos abertos.
  > * [ ] *CA06 — Auditoria:* Alterações em datas de prazos exigem motivo e são auditadas (data anterior, nova data, responsável).

### [SCRUM-46] HMS-US037: Registrar resultado do caso e iniciar rito de encerramento
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como advogado, quero registrar o resultado obtido e iniciar o rito de encerramento com 3 itens obrigatórios, para que o caso avance para "Resultado obtido / encerramento em andamento".
  > 
  > *Rastreabilidade:* RF-024 (v1.2), RF-051.
  > *Telas Pencil:* Advogado - Caso Detalhe: Encerramento
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — 3 marcos temporais distintos:* data_resultado, data_inicio_encerramento, data_conclusao_encerramento. Timeline horizontal materializa os 3 marcos na tela.
  > * [ ] *CA02 — Formulário de resultado:* Tipo de resultado (Decisão, Acordo, Entrega de Produto, etc.), descrição detalhada, data oficial do desfecho. Obrigatórios.
  > * [ ] *CA03 — Rito de encerramento com 3 itens:* (1) Comunicação final ao cliente; (2) Acerto e repasse ao cliente (alinhado com Bloco 2 do RF-051); (3) Documentos arquivados. Caso só avança para "Encerrado" após confirmação de todos.
  > * [ ] *CA04 — "Sem valores a repassar":* Quando não há valores a repassar (entrega jurídica, desfecho administrativo), Item 2 pode ser marcado como não aplicável. Pendência: regra automática pelo tipo ou manual?
  > * [ ] *CA05 — Contrato de honorários NÃO é do encerramento:* Definido na Formalização (RF-010). No encerramento, sistema apenas referencia honorários contratuais para cálculo do acerto.

### [SCRUM-47] HMS-US038: Concluir encerramento e preservar histórico do caso
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como advogado ou paralegal, quero concluir o rito de encerramento e fechar o caso, para que o caso fique disponível para consulta, nova demanda ou auditoria.
  > 
  > *Rastreabilidade:* RF-024 (v1.2), RF-049.
  > *Telas Pencil:* Advogado - Caso Detalhe: Encerramento Concluído
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — Validação do rito:* Encerramento definitivo (status 12 "Encerrado") exige validação humana de que os 3 itens do rito foram executados.
  > * [ ] *CA02 — 3 marcos gravados:* data_resultado, data_inicio_encerramento, data_conclusao_encerramento em campos distintos.
  > * [ ] *CA03 — Preservação do cadastro:* Conclusão não inativa/apaga cadastro da Pessoa; registro permanece ativo para futuros intakes.
  > * [ ] *CA04 — Histórico acessível:* Documentos, peças, logs, conversas do caso encerrado permanecem acessíveis para consulta interna.
  > * [ ] *CA05 — Reabertura restrita:* Exige perfil autorizado (Supervisor ou Administrador), motivo obrigatório (texto mínimo). Evento de reabertura auditado com: motivo, perfil, data/hora.
  > * [ ] *CA06 — Nova demanda pós-encerramento:* No estado "Encerrado", botão "Nova demanda deste cliente" vira ação principal. Cria novo intake vinculado à Pessoa existente sem duplicar cadastro (RF-049).

### [SCRUM-41] HMS-US032: Retornar peça para produção após ajustes solicitados
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como advogado (produtor), quero acessar a peça com ajustes solicitados, ver os comentários e resubmeter após correções, para que o ciclo produção → revisão → ajuste → revisão se repita até aprovação com histórico completo.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O advogado produtor acessa a peça em status "Ajustes solicitados" e visualiza os comentários do revisor destacados no painel lateral.
  > * CA02 - O editor é reativado para edição; o advogado realiza os ajustes e salva nova versão.
  > * CA03 - Ao resubmeter para revisão, o status da peça volta para "Em revisão" e o caso retorna ao status correspondente no Pipeline 2.
  > * CA04 - O histórico completo de versões, comentários de revisão e decisões é preservado de forma imutável e acessível a qualquer momento.
  > * CA05 - Não há limite de ciclos de revisão; o fluxo se repete quantas vezes necessário até aprovação final.

### [SCRUM-35] HMS-US026: Gerar pendência documental e mensagem assistida
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como sistema, quero gerar automaticamente pendência e mensagem assistida ao identificar documento faltante ou inadequado, para que o cliente seja comunicado rapidamente com texto validado pelo responsável antes do envio.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O sistema gera Pendencia automaticamente quando: documento é faltante, ilegível, incompleto, duplicado ou não corresponde ao item. Campos obrigatórios da pendência: tipo, motivo, responsável, documento relacionado e link ao checklist.
  > * CA02 - O sistema prepara MensagemAssistida com texto objetivo indicando o documento pendente e a ação necessária; a mensagem fica com status "Aguardando aprovação" antes do envio.
  > * CA03 - Mensagem de confirmação de recebimento pode ter envio automático condicionado à política da HMS; demais tipos de mensagem exigem aprovação humana antes do envio.
  > * CA04 - Comunicação de status jurídico e orientação têm envio automático bloqueado por padrão; exigem aprovação explícita do advogado responsável.
  > * CA05 - Se a pendência for gerada incorretamente por erro da IA, o paralegal cancela a pendência, registra o ErroIA com todos os campos obrigatórios e, se o cliente foi comunicado indevidamente, sinaliza necessidade de comunicação corretiva.
  > * CA06 - O checklist exibe contador de pendências ativas vinculadas a cada item.

### [SCRUM-17] HMS-US008: Visualizar intakes em Kanban do Pipeline 1
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como atendente ou supervisor, quero visualizar todos os intakes em Kanban com os 11 status do Pipeline 1, para que eu tenha visibilidade operacional do funil de relacionamento em tempo real.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O Kanban exibe exatamente 11 colunas correspondendo aos 11 status do Pipeline 1 com contador de intakes por coluna.
  > * CA02 - Cada card exibe: ID do intake, nome da pessoa, badge de origem, data de entrada, responsável (avatar) e prazo da próxima ação quando definido.
  > * CA03 - Intakes com prazo de próxima ação vencido exibem borda vermelha de alerta no card.
  > * CA04 - Toggle Kanban/Lista disponível; a Lista exibe: #, Nome, CPF, Origem, Status, Responsável, Data entrada, Próxima ação, Ações rápidas.
  > * CA05 - Filtros: status (multi-select), responsável, origem, canal e período de entrada.
  > * CA06 - Drag-and-drop de cards entre colunas é desabilitado; transições ocorrem apenas pelas ações no detalhe do intake.

### [SCRUM-18] HMS-US009: Controlar transições de status do Pipeline 1 com critérios de entrada
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como sistema, quero validar critérios de entrada antes de cada transição de status no Pipeline 1, para que intakes só avancem quando as condições operacionais estiverem satisfeitas.
  > 
  > *Rastreabilidade:* RF-005.
  > 
  > *Critérios de Aceitação:*
  > 
  > * *CA01:* A transição para o status "Consulta agendada" é bloqueada se data/hora, modalidade, canal ou advogado responsável não estiverem preenchidos no formulário.
  > * *CA02:* A progressão para "Contratado — abrir caso/serviço" é bloqueada se a formalização contratual não estiver marcada com o status concluído.
  > * *CA03:* O avanço para "Encerrado sem contratação" é bloqueado se o campo de motivo de encerramento estiver em branco.
  > * *CA04:* Cada transição realizada com sucesso gera um log de mudança de status registrando usuário, perfil, data/hora, entidade, status anterior e valor novo.
  > * *CA05:* Quando um critério de entrada falha, o sistema exibe um alerta descritivo inline explicando detalhadamente o item pendente.

### [SCRUM-38] HMS-US029: Iniciar elaboração de peça jurídica com ou sem apoio de IA
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como advogado, quero criar uma nova peça jurídica selecionando tipo e modelo base, com apoio opcional de IA, para que a produção seja iniciada com base no dossiê aprovado e o caso avance para "Em produção jurídica".
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O botão "Nova peça" só é habilitado quando o caso está em status "Pronto para produção jurídica" (checklist aprovado); em outros status é exibido desabilitado com tooltip explicando o bloqueio.
  > * CA02 - O formulário de criação exige: tipo de peça (Petição inicial · Recurso · Contrato · Requerimento · Minuta · Outro) e responsável. Modelo base e documentos de referência são opcionais.
  > * CA03 - Ao criar, o caso avança para "Em produção jurídica" e a peça recebe status "Em elaboração".
  > * CA04 - Quando IA disponível e validada por PoC, o sistema exibe sugestão de minuta no painel lateral com badge "Sugestão IA"; advogado pode aceitar como base, ajustar ou descartar.
  > * CA05 - Quando IA é utilizada na elaboração, o campo ia_utilizada = TRUE é registrado na Peca e o sistema registra SugestaoIA com todos os campos obrigatórios.
  > * CA06 - Quando IA indisponível, o editor abre em branco para elaboração manual sem mensagem de erro bloqueante.
  > * CA07 - A data_inicio_producao é registrada automaticamente ao criar a peça; campo alimenta o indicador MVP #10.

### [SCRUM-39] HMS-US030: Versionar peça jurídica com histórico imutável
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como advogado, quero salvar versões intermediárias da peça durante a elaboração com histórico preservado, para que todo o processo de elaboração seja rastreável e versões anteriores possam ser consultadas.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O editor exibe botão "Salvar versão" que cria registro imutável em VersaoPeca com: número de versão, conteúdo completo, hash SHA-256 do conteúdo, responsável e data/hora.
  > * CA02 - A aba "Versões" no painel lateral exibe todas as versões salvas com: número, data/hora, responsável e motivo quando informado.
  > * CA03 - Versões anteriores podem ser visualizadas mas não editadas; o usuário pode abrir qualquer versão em modo leitura.
  > * CA04 - Ao submeter para revisão, o sistema salva automaticamente a versão final antes da transição de status.
  > * CA05 - VersaoPeca é append-only; nenhuma operação UPDATE ou DELETE é permitida sobre registros de versão existentes.

### [SCRUM-40] HMS-US031: Revisar peça jurídica com alertas de IA e registrar decisão
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como advogado ou supervisor, quero revisar uma peça submetida, receber alertas de IA e registrar a decisão (aprovação, ajustes ou bloqueio), para que a peça só avance para protocolo/entrega após decisão humana documentada.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O editor de revisão exibe a peça em modo leitura com o painel de revisão em destaque mostrando os comentários do ciclo atual.
  > * CA02 - Quando IA disponível, o painel exibe alertas de revisão: inconsistências, lacunas, divergências entre fatos/documentos/peça e campos faltantes. Os alertas são sugestões, não decisões.
  > * CA03 - O revisor registra a decisão em um de três resultados:
  > * CA04 - Somente perfil Advogado ou Supervisor pode finalizar a revisão; para outros perfis os botões de decisão são ocultos.
  > * CA05 - Log de revisão gerado com: revisor, decisão, status anterior, novo status, comentário de revisão e data/hora.

### [SCRUM-42] HMS-US033: Aprovar versão final da peça para protocolo ou entrega
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como advogado, quero confirmar formalmente a aprovação da versão final da peça, para que a peça seja liberada para protocolo ou entrega com a responsabilidade técnica do advogado registrada.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Somente perfil Advogado pode aprovar a peça; tentativa por outro perfil é bloqueada com mensagem "Apenas advogados podem aprovar peças jurídicas".
  > * CA02 - O sistema exige confirmação explícita: checkbox "Confirmo que revisei e aprovo esta versão".
  > * CA03 - Aprovação registra: aprovador, versão final, data/hora e ressalva opcional do aprovador.
  > * CA04 - Ao aprovar, caso avança para "Aprovado para protocolo/entrega" e as opções de protocolo, distribuição ou entrega são habilitadas.
  > * CA05 - A IA não pode aprovar peça de forma autônoma; qualquer tentativa de aprovação automática sem ação humana é bloqueada tecnicamente e registrada em LogAuditoria.
  > * CA06 - A data_aprovacao é registrada automaticamente; campo alimenta o indicador MVP #10 (tempo médio de produção jurídica).

### [SCRUM-48] HMS-US039: Registrar comunicação na Central com visibilidade controlada
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como atendente, paralegal ou advogado, quero registrar qualquer interação na Central de Comunicação, para que a memória oficial esteja completa e a visibilidade seja controlada.
  > 
  > *Rastreabilidade:* RF-027 (v1.2), RF-028.
  > *Telas Pencil:* Advogado - Registrar Comunicação / Caso Detalhe: Comunicações
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — Campos obrigatórios:* Pessoa, tipo (ativa/passiva), canal, motivo, resumo descritivo.
  > * [ ] *CA02 — "Requer ação" com prazo:* Quando toggle "Requer ação" é ativado, campo "Prazo de ação" torna-se obrigatório (fundo dourado). Filtro dedicado "Requer ação · N" na timeline.
  > * [ ] *CA03 — Visibilidade padrão interno:* visivel_cliente = FALSE e visivel_terceiro = FALSE por padrão. Liberação externa é ato explícito do usuário autorizado.
  > * [ ] *CA04 — Validação antes de liberar externamente:* Sistema valida que texto não contém notas internas, estratégia, pareceres ou dados de terceiros. Liberação registra autorizador, data/hora, escopo.
  > * [ ] *CA05 — Assistente Virtual:* Comunicações do assistente virtual (RF-052) exibem badge "Auto" e atribuição a "Assistente virtual" ou responsável humano após transição.
  > * [ ] *CA06 — Distinção Comunicações vs Andamentos:* Comunicações = interações com pessoas (quem, quando, canal). Andamentos = eventos do caso. Registro manual mantido como essencial para comunicações.

### [SCRUM-55] HMS-US046: Cadastrar terceiro com tipo, natureza de vínculo e permissões explícitas
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como administrador ou supervisor, quero cadastrar um terceiro definindo tipo, natureza do vínculo e permissões específicas, para que o terceiro acesse apenas o que é vinculado ao seu escopo com permissões concedidas expressamente.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Campos obrigatórios: tipo (Sindicato · Associação · Empresa parceira · Parceiro institucional · Outro), nome, CNPJ, responsável interno e natureza do vínculo.
  > * CA02 - Natureza do vínculo é campo multi-select obrigatório: Origem da demanda · Pagador · Representante/parceiro · Apoiador documental · Contratante · Outro.
  > * CA03 - O padrão de acesso externo é negar; toda permissão deve ser concedida expressamente (ativa = FALSE por padrão em PermissaoTerceiro).
  > * CA04 - O sistema diferencia empresa como cliente PJ de empresa como terceiro/parceiro; o administrador define a categoria antes do cadastro.
  > * CA05 - Log de criação gerado com: usuário, data/hora, tipo de terceiro, natureza do vínculo e permissões concedidas.

### [SCRUM-56] HMS-US047: Acessar portal de terceiros com visão restrita e auditada
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como usuário de terceiro, quero acessar o portal com a visão dos casos vinculados ao meu terceiro, para que eu acompanhe os atendimentos dos associados/clientes vinculados sem ver dados internos da HMS.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O sistema autentica o usuário do terceiro individualmente (não apenas a organização); usuário inativo ou sem vínculo vigente tem acesso bloqueado imediatamente.
  > * CA02 - O portal exibe apenas clientes/casos vinculados ao terceiro específico; dados de clientes não vinculados são tecnicamente inacessíveis.
  > * CA03 - O conteúdo exibido não inclui: estratégia jurídica, notas internas, pareceres internos, comunicações internas ou documentos restritos.
  > * CA04 - Comunicação direta entre terceiro e cliente é bloqueada por padrão no portal; somente canal controlado e auditado via HMS está disponível quando a permissão estiver ativa.
  > * CA05 - Todo acesso é registrado em AcessoExterno com: usuário, terceiro, data/hora, caso acessado e permissão aplicada.
  > * CA06 - Tentativa de acesso a recurso não permitido é bloqueada e registrada em AcessoExterno com resultado = "negado".
  > * CA07 - Exportação de dados é bloqueada por padrão; somente relatório expressamente autorizado com log e escopo definido é permitido.

### [SCRUM-57] HMS-US048: Gerenciar permissões do terceiro com auditoria completa
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como administrador, quero conceder, alterar e revogar permissões do terceiro a qualquer momento com rastreabilidade completa, para que o acesso externo seja controlado com precisão e toda mudança seja auditada.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O administrador pode conceder, alterar ou revogar qualquer permissão da lista de 9 permissões externas disponíveis.
  > * CA02 - Permissão temporária exige: data de validade, aprovador e justificativa. O sistema revoga automaticamente ao atingir a validade.
  > * CA03 - Toda mudança de permissão gera log com: quem alterou, valor anterior, valor novo, justificativa, aprovador e data/hora.
  > * CA04 - Revogação: acesso do usuário do terceiro ao recurso revogado é bloqueado imediatamente sem necessidade de ação adicional.
  > * CA05 - O sistema disponibiliza lista de usuários externos ativos e permissões concedidas para revisão periódica pelo administrador.
  > * CA06 - Usuário do terceiro desligado ou inativo é bloqueado automaticamente quando o campo vinculo_vigente = FALSE.

### [SCRUM-58] HMS-US049: Registrar auditoria completa de toda ação relevante de IA
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como sistema, quero registrar automaticamente cada sugestão relevante de IA com todos os campos de rastreabilidade, para que toda atuação da IA seja auditável, validável e bloqueável por qualquer usuário autorizado.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Toda sugestão relevante de IA cria registro em SugestaoIA com os campos obrigatórios: tipo_acao, entidade_tipo, entidade_id, conteúdo sugerido quando necessário preservar, confiança quando disponível, status inicial "Sugerida", usuário solicitante e data/hora.
  > * CA02 - O usuário autorizado pode executar uma das quatro ações sobre qualquer sugestão: Aceitar · Ajustar · Rejeitar · Bloquear. O sistema não pode impedir o usuário de discordar da sugestão.
  > * CA03 - Rejeição exige motivo obrigatório (mín. 10 caracteres); motivo é salvo no campo observacao da SugestaoIA.
  > * CA04 - Decisão sobre a sugestão registra: status atualizado, usuário validador, data/hora e observação quando aplicável.
  > * CA05 - Sugestão com impacto jurídico, externo ou sensível tem efeito automático bloqueado independente do nível de confiança; exige validação humana explícita antes de produzir qualquer efeito.
  > * CA06 - Quando IA estiver indisponível, a plataforma continua operável por fluxo manual sem bloqueio de nenhum processo crítico.

### [SCRUM-60] HMS-US051: Registrar e tratar erros de IA com feedback estruturado
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como paralegal, advogado ou supervisor, quero registrar erros identificados nas sugestões da IA com todos os dados de correção, para que erros recorrentes alimentem indicadores de qualidade e a melhoria contínua do modelo.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Ao corrigir uma sugestão incorreta da IA, o sistema cria ErroIA com campos obrigatórios: tipo_erro, entidade afetada, resultado_ia (o que a IA errou), correcao_humana (o que foi corrigido), corrigido_por e data/hora.
  > * CA02 - Tipos de erro suportados: Classificação documental incorreta · Pendência documental indevida · Resumo de consulta incorreto · Minuta jurídica inadequada · Mensagem assistida inadequada · Alerta de gestão incorreto · Sugestão de triagem inadequada.
  > * CA03 - O campo requer_comunicacao_externa é marcado quando o erro gerou comunicação indevida ao cliente; o sistema sinaliza necessidade de comunicação corretiva.
  > * CA04 - O campo feedback_enviado é atualizado quando o erro é enviado para melhoria do modelo; este campo alimenta o indicador complementar de IA "Feedbacks enviados para melhoria".
  > * CA05 - O supervisor acessa relatório de erros de IA por tipo para calibrar parâmetros e revisar fornecedor ou configuração.

### [SCRUM-61] HMS-US052: Bloquear tecnicamente todos os usos proibidos de IA
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como sistema, quero impedir tecnicamente que a IA execute qualquer ação classificada como bloqueada no TO-BE, para que a responsabilidade jurídica e operacional permaneça sempre com o humano autorizado.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O sistema bloqueia decisão autônoma de viabilidade jurídica pela IA; a tela de avaliação de viabilidade não recebe sugestão de decisão, apenas organização de fatos e pendências.
  > * CA02 - O sistema bloqueia protocolo, envio ou entrega de peça sem aprovação humana registrada; qualquer tentativa de automação que contorne essa regra é registrada em LogAuditoria como "uso bloqueado de IA".
  > * CA03 - O sistema bloqueia envio automático livre de mensagem ao cliente com conteúdo de promessa de resultado ou orientação jurídica sem aprovação do advogado.
  > * CA04 - O sistema bloqueia liberação automática de dados a terceiros sem aprovação da HMS.
  > * CA05 - Análise de sentimento está bloqueada no MVP; qualquer chamada a essa função retorna erro controlado.
  > * CA06 - Todo bloqueio é registrado em LogAuditoria com: tipo de ação bloqueada, entidade, usuário que tentou e data/hora.

### [SCRUM-62] HMS-US053: Configurar parâmetros de confiança da IA por tipo documental
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como administrador, quero configurar limiares de confiança da IA por tipo documental e por tipo de ação, para que os parâmetros de automação sejam calibrados após PoC sem fixar valores na especificação.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - A tela de configuração exibe tabela com: tipo documental, limiar de automação (alta confiança) e limiar de revisão humana (baixa confiança) como campos editáveis por slider ou campo numérico.
  > * CA02 - Os limiares são parâmetros configuráveis, não constantes; o administrador pode ajustá-los após PoC sem alteração de código.
  > * CA03 - O sistema garante que: ações com impacto jurídico, externo ou sensível exigem validação humana independente do limiar configurado.
  > * CA04 - Toda alteração de parâmetro gera log com: quem alterou, tipo documental afetado, valor anterior, valor novo, justificativa e data/hora.
  > * CA05 - O administrador acessa relatório de erros e ajustes por tipo de IA para subsidiar a revisão periódica dos parâmetros.

### [SCRUM-63] HMS-US054: Calcular e exibir os 12 indicadores principais do MVP
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como supervisor ou administrador, quero visualizar os 12 indicadores principais do MVP calculados automaticamente a partir dos dados da plataforma, para que a gestão operacional seja baseada em dados estruturados sem entrada manual adicional.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O painel exibe os 12 indicadores: (1) Entradas por origem · (2) Conversão em contratação · (3) Consultas realizadas · (4) Tempo médio até contratação · (5) Encerrados sem contratação por motivo · (6) Tempo até checklist aprovado · (7) Pendências documentais por caso · (8) Docs recusados por motivo · (9) Casos prontos para produção · (10) Tempo médio de produção jurídica · (11) Casos por status de execução · (12) Ações de IA por status.
  > * CA02 - Cada indicador é calculado exclusivamente a partir dos dados estruturados já registrados na plataforma; nenhum dado de indicador é inserido manualmente.
  > * CA03 - Filtro obrigatório por período (data início — data fim); o painel recalcula ao aplicar.
  > * CA04 - Indicadores com campos mínimos obrigatórios faltantes em registros exibem alerta: "X registros com campos incompletos afetam este indicador. [Ver registros]".
  > * CA05 - Os indicadores de distribuição (por origem, por motivo, por status) são exibidos como gráfico de pizza ou barras usando as cores do HMS Design System (chart-1 a chart-5).
  > * CA06 - O supervisor pode fazer drill-down em cada indicador para ver os registros que compõem o número.
  > * CA07 - Indicadores complementares de IA e terceiros são exibidos em seção separada como indicadores opcionais.

### [SCRUM-64] HMS-US055: Exportar relatório de indicadores em CSV
- **Status**: `To Do` | **Story Points**: `2`
- **Descrição**:
  > Como supervisor ou administrador, quero exportar os indicadores calculados em CSV, para que os dados possam ser analisados em ferramentas externas ou compartilhados com a gestão.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Botão "Exportar CSV" está disponível no painel de indicadores e exporta os dados do período selecionado.
  > * CA02 - O CSV inclui: nome do indicador, período, valor calculado e breakdown quando aplicável (por origem, por motivo, por status).
  > * CA03 - A exportação gera log com: usuário que exportou, período, indicadores exportados e data/hora.
  > * CA04 - Apenas perfis Supervisor e Administrador têm acesso ao botão de exportação.

### [SCRUM-67] HMS-US058: Monitorar e reprocessar falhas de integração
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como administrador, quero visualizar eventos de integração com falhas e reprocessar manualmente quando necessário, para que nenhum documento ou comunicação seja perdido por falha técnica de integração.
  > 
  > *Critérios de Aceitação:*
  > 
  > * *CA01:* Quando uma integração (WhatsApp ou IA) for restabelecida após um período de inatividade, o sistema deve acionar um protocolo obrigatório de reconciliação de dados.  
  > * *CA02:* Documentos que foram classificados manualmente pela equipe durante a queda devem ser disponibilizados em lote para reprocessamento na IA/OCR para fins de validação cruzada.  
  > * *CA03:* Comunicações salvas manualmente no modo de contingência devem ser confrontadas e vinculadas aos eventos reais recebidos atrasados da API para higienizar a base e deletar duplicidades.  
  > * *CA04:* A tela administrativa lista todos os eventos de falha contendo: tipo de API, direção, contagem de tentativas automáticas, payload e mensagem de erro do servidor.  
  > * *CA05:* O sistema executa tentativas automáticas de reenvio para falhas transitórias e, esgotado o limite, altera o status para "Falha permanente" e notifica a TI.  
  > 
  > * *Rastreabilidade:* RF-044, RF-050. 

### [SCRUM-68] HMS-US059: Consultar log de auditoria imutável com filtros avançados
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como administrador ou supervisor, quero consultar o log de auditoria de todos os eventos críticos com filtros por entidade, usuário, ação e período, para que toda a rastreabilidade da plataforma esteja disponível para investigação, conformidade e auditoria.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O log exibe todos os eventos críticos com colunas: data/hora, usuário, perfil, entidade afetada, ação, origem (humano/sistema/ia/integração) e status do evento.
  > * CA02 - Filtros disponíveis: período, entidade (tipo), ação, usuário e origem da ação.
  > * CA03 - Ao clicar em um evento, o drawer de detalhe exibe: todos os campos mínimos do log, valor anterior e valor novo (quando aplicável) e motivo/justificativa.
  > * CA04 - O log é append-only; nenhum botão de edição, exclusão ou alteração está presente na interface; o sistema bloqueia tecnicamente qualquer operação UPDATE ou DELETE na tabela.
  > * CA05 - A exportação do log gera CSV com aviso: "Este log contém dados sensíveis. Respeite a política de retenção e confidencialidade da HMS."
  > * CA06 - Eventos de IA exibem badge "IA" e origem = "ia" para diferenciação visual.

### [SCRUM-69] HMS-US060: Garantir log de auditoria para todos os eventos críticos
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > Como sistema, quero gerar automaticamente log de auditoria para todos os eventos críticos da matriz definida no TO-BE, para que nenhum evento relevante passe sem rastreabilidade de usuário, ação, entidade e resultado.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O sistema gera log automático para os seguintes tipos de evento: criação, alteração, ativação e inativação de usuário/permissão; toda mudança de status nos Pipelines 1 e 2; toda aprovação de checklist, dossiê ou peça; toda ação de IA com decisão registrada; todo acesso externo (cliente/terceiro); toda liberação de documento ou comunicação ao externo; toda exceção (solicitada/aprovada/rejeitada/revogada); toda falha de integração; toda mudança de classificação documental.
  > * CA02 - Campos mínimos obrigatórios em todo log: usuário ou sistema responsável, perfil e função no momento da ação, escopo, data/hora, entidade afetada, ação realizada, valor anterior e valor novo quando aplicável, origem da ação e status do evento.
  > * CA03 - Falha no registro de log é tratada como evento crítico: a ação do usuário não é descartada, mas a falha é registrada no sistema de monitoramento e o administrador é notificado.
  > * CA04 - Logs de acesso externo são registrados em AcessoExterno (tabela separada) com os campos adicionais: permissão aplicada e resultado (permitido/negado).
  > * CA05 - Perfis e funções são copiados como snapshot no momento da ação; alterações posteriores no perfil do usuário não alteram logs históricos.

### [SCRUM-117] HMS-US085 - Configurar Fluxo de Atendimento Híbrido no WhatsApp
- **Status**: `To Do` | **Story Points**: `5`
- **Descrição**:
  > *Rastreabilidade:* {{RF-052}}, {{RF-029}}, {{RF-027}}
  > 
  > Como atendente/intake, quero que o assistente virtual trate mensagens padronizadas e passe o atendimento para o humano de forma transparente ao detectar desvios, para não perder o contexto da conversa e garantir a correta distribuição por unidade de origem.
  > 
  > *Telas: 40 a 41.*
  > 
  > * *Critérios de Aceitação:*
  > 
  > * *CA01:* Garantir que o assistente virtual responda autonomamente apenas as categorias parametrizadas e autorizadas (como confirmações de recebimento de mídias, status básico e faixas de horários pré-configuradas).
  > * *CA02:* Implementar transbordo transparente e sem perda de histórico da conversa para atendimento humano ao detectar ambiguidade, dúvida jurídica, insatisfação ou solicitação direta de atendente.
  > * *CA03:* Rotear automaticamente o atendimento humano para o responsável correto com base na linha oficial de origem do WhatsApp (ex: direcionar para a unidade regional de Indaiatuba se o contato veio daquele número).

### [SCRUM-119] HMS-US086 — Definir e Monitorar Política de SLA de Atendimento por Status
- **Status**: `To Do` | **Story Points**: `5`

### [SCRUM-120] HMS-US084 — Módulo Financeiro — Versão Incipiente do MVP
- **Status**: `To Do` | **Story Points**: `3`
- **Descrição**:
  > Como advogado ou financeiro, quero gerenciar os dois blocos financeiros do caso (contratação e acerto), para que honorários, recebíveis e repasses ao cliente sejam rastreáveis e calculados corretamente.
  > 
  > *Rastreabilidade:* RF-051 (v1.2), RF-010, RF-024.
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — Bloco 1 (Contratação):* Condições comerciais (7 modelos), contrato de honorários, parcelas, recebíveis. Executado na Formalização (RF-010) e geração de documentos (RF-056).
  > * [ ] *CA02 — Bloco 2 (Acerto e repasse):* Recebimento de crédito, cálculo do acerto, repasse com comprovante bancário, recibo/quitação. Executado no Encerramento (RF-024).
  > * [ ] *CA03 — Status do Acerto:* Em cálculo → Aguardando conferência → Aguardando aprovação → Aprovado para pagamento → Pago → Comprovante anexado → Recibo pendente → Recibo assinado → Concluído. Excepcionais: Divergente, Cancelado.
  > * [ ] *CA04 — Fórmula:* Valor líquido = bruto − honorários contratuais − sucumbenciais − despesas − custas − adiantamentos − outros descontos autorizados.
  > * [ ] *CA05 — Regras de bloqueio:* (1) Sem bruto/abatimentos/líquido calculado; (2) Divergência exige justificativa; (3) Repasse sem comprovante bancário; (4) Sem demonstrativo e recibo/quitação (salvo exceção).
  > * [ ] *CA06 — Distinção:* Comprovante bancário ≠ recibo. Comprovante = evidência de movimentação. Recibo = documento assinado pelo cliente. Ambos obrigatórios (salvo exceção).

### [SCRUM-129] HMS-US092: Controlar status do Pipeline 2 com 12 status formais
- **Status**: `To Do` | **Story Points**: `0`
- **Descrição**:
  > Como advogado ou paralegal, quero visualizar e controlar os 12 status formais do Pipeline 2, para que a progressão do caso seja rastreável com agrupamento visual no stepper.
  > 
  > *Rastreabilidade:* RF-048 (v1.2).
  > 
  > ----
  > 
  > *Critérios de Aceite:*
  > 
  > * [ ] *CA01 — 12 status formais:* (1) Caso aberto, (2) Documentação em formação, (3) Checklist pendente, (4) Pronto para produção, (5) Em produção jurídica, (6) Em revisão, (7) Ajustes solicitados, (8) Aprovado para protocolo/entrega, (9) Protocolado/distribuído/entregue, (10) Em execução/acompanhamento, (11) Resultado obtido / encerramento em andamento, (12) Encerrado.
  > * [ ] *CA02 — Agrupamento visual:* "Protocolo / Entrega" no stepper agrupa status 8 e 9. Dot ativo durante ambos. 12 status distintos no modelo de dados.
  > * [ ] *CA03 — Stepper na tela do caso:* Cada dot do stepper corresponde a um status. Status ativo em destaque, concluídos com check, futuros em outline.
  > * [ ] *CA04 — Transições controladas:* Critérios de entrada por status (checklist aprovado para produção, peça aprovada para protocolo, rito concluído para encerrado).
  > * [ ] *CA05 — Auditoria:* Toda transição gera log com: usuário, status anterior, novo status, data/hora.
