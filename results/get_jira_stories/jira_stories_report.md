# Relatório de Histórias de Usuário (Jira Board)

## Resumo por Sprint
- **Sprint 2 (CLOSED)**: 22 histórias, 87 Story Points
- **Sprint 3 - Cliente e Atendimen (CLOSED)**: 9 histórias, 36 Story Points
- **Sprint 4 - Adv. Paralegal e WP (CLOSED)**: 11 histórias, 53 Story Points
- **Sprint 5 - Formalização (ACTIVE)**: 5 histórias, 16 Story Points
- **Sprint 6 (ACTIVE)**: 8 histórias, 40 Story Points
- **Backlog**: 30 histórias, 118 Story Points

---

## Sprint: Sprint 2 (CLOSED)

### [SCRUM-92] HMS-US070 – Painel de Monitoramento Crítico de Prazos Processuais (SLA)
- **Status**: `Done`
- **Story Points**: 8
- **Descrição**:
  > Como um Advogado, eu quero que o sistema diferencie visualmente os prazos processuais das tarefas operacionais cotidianas através de políticas estritas de SLA, para que os prazos fatais jurídicos recebam prioridade e tratamento de escalonamento imediato.
  > 
  > [Rastreabilidade: RF-023, RF-026, RF-053 | Entidades: TarefaPrazo, SLA_Policy]
  > 
  > *Critérios de Aceitação:*
  > 
  > * O painel Kanban/Lista de prazos do caso deve categorizar os itens obrigatoriamente sob dois tipos visuais distintos: 'Prazo Processual' (Criticidade Máxima) ou 'Tarefa Operacional'.
  > * Os itens com o tipo 'Prazo Processual' devem receber uma estilização em alta visibilidade (borda ou fundo vermelho suave) e exibir o indicador de contagem regressiva de tempo baseado no SLA de permanência configurado pelo administrador.
  > * Para cada registro, a interface deve exibir de forma explícita a divisão de responsabilidades: o Advogado Principal listado como responsável técnico e o Paralegal designado listado para execução e monitoramento.
  > * Caso o tempo de permanência de um 'Prazo Processual' atinja a margem de aproximação do limite do SLA sem que a baixa tenha sido dada, o sistema deve disparar alertas visuais na barra superior do Advogado Principal. Caso estoure o limite, o item deve ser marcado como gargalo operacional e escalonado ao Supervisor.
  > * O sistema deve bloquear o encerramento do caso se houver qualquer item de tipo 'Prazo Processual' em aberto, emitindo um aviso impeditivo na tela de encerramento.
  > * Qualquer alteração de data limite ou responsável por um prazo ativa o rito de exceção, exigindo justificativa obrigatória enviada para homologação do Supervisor.

### [SCRUM-91] HMS-US069 – Revisão Técnica e Aprovação de Peça (Etapa Unificada)
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como um Advogado Revisor ou Supervisor, eu quero analisar uma peça submetida em uma interface unificada com alertas analíticos de IA, para aprovar o documento para protocolo ou devolvê-lo para ajustes em um único ato técnico.
  > 
  > [Rastreabilidade: RF-020, RF-047 | Entidades: Peca, Caso, LogAuditoria]
  > 
  > *Critérios de Aceitação:*
  > 
  > * A interface de revisão deve carregar a peça em modo de leitura comparativa, exibindo o histórico de versões e uma aba lateral de Alertas de IA apontando ativamente contradições, lacunas de mérito e campos de dados pessoais faltantes.
  > * O painel de ações de revisão deve expor três decisões excludentes: Botão 'Aprovar Peça' (move a peça para 'Aprovada' e exige marcação de checkbox termo-ético: 'Confirmo minha responsabilidade técnica...'); Botão 'Solicitar Ajustes' (exige campo de texto para comentários e retorna a peça); Botão 'Bloquear por Falta Documental' (peça vira 'Bloqueada por dossiê incompleto' e caso retrocede para a fase de checklist).
  > * Regra de Bloqueio Hard: O sistema deve impedir por completo que a IA realize o rito de aprovação ou mude o status da peça de forma automatizada sem a interação humana de clique gravada.

### [SCRUM-90] HMS-US068 – Início de Elaboração de Peça com Assistência Lateral de IA
- **Status**: `Done`
- **Story Points**: 8
- **Descrição**:
  > Como um Advogado, eu quero iniciar a redação de um entregável jurídico utilizando modelos internos e suporte lateral de IA, para acelerar a produção intelectual garantindo o controle total sobre as versões intermediárias.
  > 
  > [Rastreabilidade: RF-016, RF-018, RF-019 | Entidades: Peca, VersaoPeca, SugestaoIA]
  > 
  > *Critérios de Aceitação:*
  > 
  > * [ ] O sistema só deve liberar o botão 'Iniciar Produção de Peça' se o caso estiver no status 'Pronto para produção jurídica', o que exige o Checklist Final Aprovado (ou com exceção) e o Dossiê Documental nos status 'Aprovado' ou 'Aprovado com exceção'. Caso contrário, a ação é bloqueada com mensagem de erro em tela.
  > * [ ] Ao iniciar, a interface do editor deve abrir em tela dividida (split-screen): no lado esquerdo, a árvore de arquivos do Dossiê Documental Validado; no centro, o editor de texto rico; no lado direito, o painel assistivo de IA.
  > * [ ] O painel de IA (condicionado à PoC) deve apresentar sugestões de minutas ou blocos textuais específicos com base nos documentos do Dossiê. O sistema deve exibir uma tag visual nítida 'Gerada com apoio de IA' no status da peça se o advogado aceitar o bloco de texto.
  > * [ ] O editor deve autosalvar o rascunho atual com debounce durante a edição, preservando recuperação operacional sem gerar uma nova versão formal a cada tecla. A tabela {{VersaoPeca}} deve registrar versões imutáveis apenas em marcos juridicamente relevantes, como criação da peça, aplicação de modelo, aceite de bloco de IA, conclusão da elaboração, solicitação de ajustes, reenvio para revisão, aprovação ou bloqueio por falta documental. Cada versão deve identificar número da versão, data/hora (TIMESTAMPTZ), ID do usuário, tipo do marco e conteúdo da peça naquele momento.
  > * [ ] Ao clicar em 'Concluir Elaboração', a peça deve mudar para o status 'Em revisão' e o caso deve avançar no Pipeline 2 para o status 6.

### [SCRUM-107] HMS-US082 – Design do Frame: Dashboard Operacional, SLAs e Gargalos (Pipeline 2)
- **Status**: `Done`
- **Story Points**: 8
- **Descrição**:
  > Como Designer de UI, quero projetar a interface do Dashboard Operacional do Pipeline 2 com foco em volumetria e monitoramento de riscos, para que a gestão identifique gargalos na produção jurídica e prazos (SLAs) prestes a estourar.
  > 
  > [Contexto: Entidade Indicador / Caso / TarefaPrazo | Rastreabilidade: RF-053]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Desenhar a seção central contendo os 4 indicadores operacionais do MVP (KPI Cards): Tempo de Formação de Dossiê, Tempo de Elaboração de Peças, Índice de Refugo Técnico e Volumetria de Casos Ativos por Área.-
  > * -Criar um gráfico de barras combinadas ou mapa de calor (Heatmap) que aponte visualmente o volume de tarefas e prazos que estão na margem crítica de estourar o SLA de permanência.-
  > * -Incluir uma listagem compacta com os 'Top 5 Casos Mais Retidos', ordenados decrescentemente pelo tempo de inatividade no Pipeline 2.-

### [SCRUM-101] HMS-US076 – Design do Frame: Painel de Monitoramento de Assinaturas e Gatilho do Caso
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como Designer de UI, quero projetar o Painel de Acompanhamento de Assinaturas Contratuais, evidenciando as interações com o cliente e a automação de destravamento das credenciais do Portal do Cliente após a formalização do vínculo.
  > 
  > [Contexto: Entidades Contratacao e Caso | Rastreabilidade: RF-010, RF-011, RF-033]
  > 
  > *Critérios de Aceitação:*
  > 
  > * Criar um componente de listagem cronológica (Timeline) indicando o status em tempo real de cada documento enviado para as APIs externas de assinatura eletrônica, utilizando badges coloridos: Aguardando Assinatura (Amarelo), Assinado (Verde) ou Recusado (Vermelho).
  > * Desenhar uma seção de notificações e histórico contendo o registro do link seguro enviado para o WhatsApp do cliente.
  > * Projetar o estado visual do sistema no momento em que a última assinatura é computada: a interface deve renderizar um modal ou banner de sucesso indicando 'Marco de Contratação Atingido! Criando Caso Jurídico...'.
  > * Incluir no layout de sucesso a indicação visual de que as credenciais de acesso completo ao Portal do Cliente foram geradas e enviadas ao WhatsApp do destinatário, liberando-o da antessala de leads.

### [SCRUM-100] HMS-US075 – Design do Frame: Mesa de Formalização e Geração de Minutas
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como Designer de UI, quero projetar a interface da Mesa de Formalização de Contratos utilizando componentes do Design System, para que a equipe de atendimento ou o paralegal consiga emitir minutas, revisar dados de cobrança e disparar os documentos para assinatura eletrônica de forma ergonômica e centralizada.
  > 
  > [Contexto: Entidade Contratacao / Intake | Rastreabilidade: RF-010]
  > 
  > *Critérios de Aceitação:*
  > 
  > * Desenhar a tela principal exibindo o status atual do relacionamento do cliente como 'Formalização em andamento'.
  > * Criar uma seção de formulário contendo os inputs estruturados para a geração dos documentos essenciais do MVP (Contrato de Honorários e Procuração), trazendo os dados da pessoa previamente preenchidos.
  > * Projetar uma área de pré-visualização da minuta de texto rica em formato de folha de papel (padrão A4 vertical dentro de um container centralizado).
  > * Desenhar a barra de ações inferior com os botões: 'Girar Nova Minuta via IA' (Secundário), 'Editar Texto Manualmente' (Link) e o botão de destaque de conversão 'Disparar para Assinatura Eletrônica' (Ação Primária).

### [SCRUM-111] Design do Frame: Tela de Detalhes de Consulta
- **Status**: `Done`
- **Story Points**: 0
- **Descrição**:
  > Como Designer de UI, quero projetar a tela de detalhes da consulta jurídica utilizando os componentes do Design System HMS, para que o advogado visualize os dados do intake, registre a consulta realizada, documente pendências e avance para avaliação de viabilidade com clareza e rastreabilidade.
  > 
  > [Contexto: Entidades Consulta, Intake, Pessoa, SugestaoIA | Rastreabilidade: RF-007, RF-008, RF-009, RF-032]
  > 
  > *Critérios de Aceitação:*
  > 
  > * Desenhar o cabeçalho da página com título “Detalhes da Consulta”, status da consulta e metadados do intake/pessoa vinculada.
  > * Criar área de resumo do agendamento contendo data/hora, modalidade, canal, advogado responsável, local/link quando aplicável e histórico de remarcações/ausência.
  > * Projetar formulário estruturado para registro da consulta com campos obrigatórios: data/hora realizada, modalidade, canal, resumo, pendências, documentos solicitados, avaliação e próximos passos.
  > * Prever estado de consulta virtual por WhatsApp vídeo, deixando claro que recebe os mesmos campos obrigatórios da consulta presencial.
  > * Incluir componente para sugestão de resumo por IA quando disponível, com badge “Sugestão IA” e ações “Aceitar”, “Ajustar” e “Rejeitar”.
  > * Projetar área de documentos solicitados com input por tags, permitindo múltiplos itens e visualização clara das pendências geradas.
  > * Incluir seção de avaliação de viabilidade com opções “Viável”, “Inviável” e “Pendente”, mantendo decisão humana explícita do advogado.
  > * Desenhar ações finais com hierarquia correta: “Salvar registro da consulta”, “Registrar avaliação de viabilidade” e ação secundária de voltar/cancelar.
  > * Garantir que perfis não autorizados visualizem o formulário em modo leitura com aviso “Aguardando validação do advogado”.

### [SCRUM-94] HMS-US072 – Design do Frame: Caixa de Triagem de Lotes Órfãos
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como Designer de UI, quero projetar a tela de Caixa de Triagem de Lotes Órfãos utilizando Plus Jakarta Sans e a paleta PADRÃO, para que o Paralegal identifique rapidamente arquivos sem associação no sistema.
  > 
  > [Contexto: Entidade LoteDocumental | Rastreabilidade: RF-045]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Desenhar a Sidebar específica do Paralegal contendo os 4 itens de navegação definidos na arquitetura, marcando 'Caixa de Triagem' como estado ativo.-
  > * -Criar a tabela/grid principal listando os lotes não identificados contendo: ID do Lote (Monospace), Canal de Origem (ex: WhatsApp, Web), Data/Hora (TIMESTAMPTZ) e quantidade de arquivos.-
  > * Desenhar o componente de busca inline e o botão de ação rápida 'Vincular a Pessoa/Intake' em cada linha da tabela.
  > * -Incluir uma gaveta lateral modal (Drawer) que se abre ao clicar no lote para listar a miniatura básica dos arquivos contidos nele antes da associação.-

### [SCRUM-112] Design do Frame: Tela de Agenda do Advogado
- **Status**: `Done`
- **Story Points**: 0
- **Descrição**:
  > Como Designer de UI, quero projetar a tela de agenda do advogado utilizando os componentes do Design System HMS, para que o advogado visualize consultas, disponibilidade semanal, bloqueios de horário e eventos vinculados aos seus intakes de forma organizada.
  > 
  > [Contexto: Entidades Consulta, Intake, Usuario/Advogado, Disponibilidade | Rastreabilidade: RF-007, RF-023, RF-044]
  > 
  > *Critérios de Aceitação:*
  > 
  > * Desenhar o cabeçalho da página com o título “Agenda do Advogado”, identificação do advogado e seletor de período/visualização.
  > * Criar visualização principal em calendário semanal/mensal e alternativa em lista cronológica de consultas/eventos.
  > * Exibir cards de consulta com horário, nome da pessoa/intake, modalidade, canal, status da consulta e origem da entrada.
  > * Projetar estados visuais para consulta agendada, realizada, ausente, remarcada e cancelada, usando badges e cores do Design System.
  > * Incluir painel de configuração de disponibilidade semanal, duração padrão de consulta e bloqueios de datas/horários.
  > * Criar fluxo visual para bloquear horário/data, exigindo motivo obrigatório e exibindo o bloqueio no calendário.
  > * Projetar ação rápida para abrir os detalhes da consulta/intake a partir do evento no calendário.
  > * Prever mensagens de vazio, conflito de agenda e indisponibilidade de integração/contingência manual.
  > * Respeitar a separação entre agenda do advogado e agenda administrativa, evitando exposição de dados fora do escopo do usuário.

### [SCRUM-110] Design do Frame: Tela de Pessoas
- **Status**: `Done`
- **Story Points**: 0
- **Descrição**:
  > Como Designer de UI, quero projetar a tela de Pessoas utilizando os componentes do Design System HMS, para que a equipe consiga consultar, cadastrar, editar e identificar pessoas sem duplicidade, com visão clara do status relacional e do histórico associado.
  > 
  > [Contexto: Entidade Pessoa | Rastreabilidade: RF-001, RF-002, RF-041]
  > 
  > *Critérios de Aceitação:*
  > 
  > * Desenhar o cabeçalho da página com o título “Pessoas” usando Fraunces e ações principais alinhadas à direita.
  > * Criar uma listagem/tabela de pessoas com colunas mínimas: nome, CPF/CNPJ, telefone principal, e-mail, status relacional, responsável HMS e último registro/atualização.
  > * Incluir busca por nome, CPF/CNPJ e telefone, com campo de busca em destaque e filtros por status relacional, responsável e tipo de pessoa.
  > * Projetar o empty state para ausência de resultados, com ação “Criar nova pessoa”.
  > * Projetar o estado de alerta de possível duplicidade ao tentar criar pessoa com CPF/CNPJ ou telefone já existente.
  > * Criar drawer/modal de cadastro e edição com campos principais da Pessoa e área de consentimentos LGPD/WhatsApp/e-mail.
  > * Prever visualização de histórico resumido de intakes anteriores vinculados à pessoa, sem expor dados jurídicos sensíveis fora do escopo do perfil.
  > * Usar badges e estados visuais de acordo com o Design System, preservando cores oficiais, espaçamentos e componentes de tabela/lista.

### [SCRUM-109] Design do Frame: Tela de Novo Intake
- **Status**: `Done`
- **Story Points**: 0
- **Descrição**:
  > Como Designer de UI, quero projetar a tela de criação de novo intake utilizando os componentes do Design System HMS, para que o atendimento consiga registrar uma nova entrada com origem, canal, pessoa vinculada e responsável HMS de forma clara, rastreável e sem duplicidade.
  > 
  > [Contexto: Entidades Pessoa, Intake | Rastreabilidade: RF-001, RF-003, RF-004]
  > 
  > *Critérios de Aceitação:*
  > 
  > * Desenhar o cabeçalho da página com o título “Novo Intake” usando Fraunces e metadados/contexto em Plus Jakarta Sans.
  > * Criar seção inicial de busca/seleção de Pessoa, permitindo buscar por nome, CPF/CNPJ ou telefone antes de criar novo intake.
  > * Projetar o estado de pessoa encontrada, com card resumido contendo nome, CPF/CNPJ, telefone principal, status relacional e botão “Criar intake vinculado”.
  > * Projetar o estado de pessoa não encontrada, com ação para iniciar cadastro mínimo de pessoa antes da abertura do intake.
  > * Criar formulário de intake com campos obrigatórios: origem da entrada, canal de contato, terceiro vinculado quando origem = via terceiro, responsável HMS, área do direito, tipo de problema relatado e grau de urgência.
  > * Projetar mensagens inline de validação para campos obrigatórios ausentes, preservando o padrão visual do Design System.
  > * Incluir ação primária “Salvar Intake” e ação secundária/outline “Cancelar”, respeitando hierarquia visual, espaçamento e cores oficiais.
  > * Prever estado de sucesso indicando criação do intake com status “Novo registro” ou “Aguardando informações”, conforme os dados preenchidos.

### [SCRUM-89] HMS-US067 – Configuração da Equipe Multidisciplinar do Caso
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como o Advogado Principal (responsável formal), eu quero associar perfis auxiliares à equipe do caso e definir seus níveis de permissão na abertura do serviço, para delegar tarefas operacionais sem perder o controle técnico.
  > 
  > [Rastreabilidade: RF-011, RF-015 | Entidades: Caso, Permissoes, ChecklistCaso]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Logo após a detecção do status 'Contratado — abrir caso/serviço', o sistema deve instanciar o caso no Pipeline 2 com o status inicial 'Caso/serviço aberto'.-
  > * -A interface deve exibir um componente de listagem de equipe ('Equipe do Caso'), definindo compulsoriamente o criador/advogado sênior logado como o Advogado Principal (Detentor da Responsabilidade Formal).-
  > * -O sistema deve disponibilizar um botão 'Adicionar Membro' que permita associar múltiplos usuários internos, exigindo a seleção do seu Cargo/Função (Paralegal designado, Advogado auxiliar/júnior, Estagiário).-
  > * -Para cada membro adicionado, o Advogado Principal deve selecionar o escopo de permissão em um menu suspenso: Visualização, Edição ou Execução de tarefas.-
  > * -O checklist documental do caso deve ser instanciado automaticamente nesta tela a partir de um template padrão baseado na Área do Direito selecionada.-
  > * -A interface deve permitir que o Advogado Principal adicione itens complementares ao checklist específicos para o caso concreto, salvando uma justificativa em texto sem alterar o template original da área.-

### [SCRUM-105] HMS-US080 – Design do Frame: Painel de Monitoramento de Estouro de SLA
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como Designer de UI, quero projetar la tela de monitoramento de estouro de SLA para uso da supervisão, evidenciando os gargalos operacionais e os prazos processuais críticos que exigem intervenção imediata da liderança.
  > 
  > [Contexto: Entidade TarefaPrazo / SLA_Policy | Rastreabilidade: RF-023, RF-053]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Desenhar um painel de triagem focado em 'Casos com SLA Estourado', aplicando uma listagem com ordenação decrescente pelo tempo de atraso (aging por status).-
  > * -Criar cartões de listagem que diferenciem com clareza visual absoluta os itens de tipo 'Prazo Processual Crítico' (com bordas de alerta reforçadas e ícone de urgência) das 'Tarefas Operacionais' comuns.-
  > * -Exibir de forma nítida em cada card o nome do Advogado Principal (responsável técnico) e do Paralegal designado para o acompanhamento do caso.-
  > * -Desenhar um botão de ação rápida 'Notificar Responsáveis' ou 'Escalonar Caso', que abre uma gaveta lateral para disparar alertas internos diretos na interface dos colaboradores associados.-

### [SCRUM-103] HMS-US078 – Design do Frame: Fila de Homologação de Exceções Operacionais
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como Designer de UI, quero projetar la interface da Fila de Homologação de Exceções, utilizando os componentes do Design System, para que o Supervisor analise, aprove ou rejeite desvios operacionais solicitados pela equipe jurídica de forma centralizada e com rastreabilidade completa.
  > 
  > [Contexto: Entidade Excecao / LogAuditoria | Rastreabilidade: RF-025, RF-026, RF-042]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Desenhar o painel em formato de lista/grid contendo as solicitações de exceção pendentes, exibindo as colunas: ID da Exceção (Monospace), Tipo de Exceção (ex: Dispensa documental, Exceção de prazo), Solicitante, Caso Vinculado e Impacto Estimado.-
  > * -Projetar a visualização detalhada da solicitação (via modal ou painel de expansão), destacando obrigatoriamente a Justificativa Objetiva preenchida pelo solicitante.-
  > * -Desenhar os componentes de decisão para o Supervisor: Botão 'Homologar Exceção' (Sucesso/Verde) e Botão 'Rejeitar Exceção' (Alerta/Vermelho).-
  > * -Implementar uma trava visual de interface (Segregação de Funções): Se o usuário logado for o mesmo que solicitou a exceção, os botões de ação devem aparecer desabilitados (disabled), exibindo a mensagem: 'Aprovação bloqueada: O solicitante não pode aprovar a própria exceção'.-

### [SCRUM-88] HMS-US066 – Avaliação de Viabilidade Jurídica da Demanda
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como um Advogado, eu quero registrar formalmente a análise técnica de viabilidade de um intake após a realização de uma consulta, para determinar se a demanda está apta a seguir para a fase de contratação ou se deve ser arquivada.
  > 
  > [Rastreabilidade: RF-008, RF-009 | Entidades: Consulta, Intake]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -O sistema deve exibir em tela o resumo estruturado da consulta (seja presencial ou virtual por WhatsApp Vídeo). Se gerado por IA (PoC), deve permitir edição humana integral.-
  > * -A interface deve fornecer um componente de seleção (Radio Button ou Dropdown) contendo três opções exclusivas de decisão: 'Viável', 'Inviável' ou 'Pendente'.-
  > * -Se o advogado selecionar 'Viável', o sistema deve avançar o status do intake para 'Viável — aguardando formalização'.-
  > * -Se o advogado selecionar 'Inviável', o sistema deve tornar o campo 'Justificativa de Inviabilidade' obrigatório. O salvamento sem o preenchimento deste campo deve ser bloqueado, e o avanço deve encaminhar o registro ao status 'Encerrado sem contratação'.-
  > * -Se o advogado selecionar 'Pendente', a interface deve exigir o registro das ações e documentos necessários para retomar a análise, mantendo o intake em 'Em avaliação de viabilidade'.-
  > * -Trava de Segurança: É proibida qualquer automação que emita ou salve a decisão de viabilidade de forma autônoma por IA (Uso não permitido).-

### [SCRUM-102] HMS-US077 – Design do Frame: Parametrizador de Checklists e Templates por Área
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como Designer de UI, quero projetar a tela de gerenciamento e parametrização de templates de checklist por área do direito, para que a equipe técnica ou supervisão defina a esteira padrão de documentos obrigatórios que o sistema instanciará na abertura de novos casos.
  > 
  > [Contexto: Entidade ChecklistTemplate | Rastreabilidade: RF-015]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Desenhar o cabeçalho utilizando a fonte serifada Fraunces para o título 'Modelos de Checklist por Área do Direito'.-
  > * -Criar uma interface estruturada em duas colunas: a coluna esquerda exibe um seletor das áreas do direito (Trabalhista, Previdenciário, Cível, etc.) e a coluna direita carrega a lista expansível de arquivos obrigatórios exigidos para aquela respectiva área.-
  > * -Desenhar os componentes de interação dentro da lista: botões de arrastar para reordenar (Drag and Drop), caixas de seleção (checkboxes) indicando se o documento é opcional ou obrigatório de mérito, e campo de texto para apelidar o documento.-
  > * -Incluir o botão primário 'Salvar Template de Checklist' no canto superior direito do grid, mantendo o padrão visual e alinhamento do projeto.-

### [SCRUM-95] HMS-US073 – Design do Frame: Mesa de Validação Documental Split-Screen
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como Designer de UI, quero projetar a interface Split-Screen de Validação Documental, para garantir ergonomia visual ao Paralegal no ato de conferência de dados de IA versus documento real, e projetar a listagem da Fila de Revisão como ponto de acesso a esta interface.  [Contexto: Entidades Documento, Pendencia | Rastreabilidade: RF-012, RF-013, RF-14, RF-046]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Estruturar a tela em um layout dividido (50% canvas esquerdo para o visualizador de PDF/Imagem com controles de zoom, 50% coluna direita para o formulário de metadados).-
  > * -Desenhar os inputs de metadados preenchidos por IA (Tipo Documental, Nome do Titular, Data de Emissão) com uma tag sutil indicando extração automatizada.-
  > * -Criar os três botões principais de ação com hierarquia clara do Design System: 'Validar' (Sucesso/Verde), 'Rejeitar' (Alerta/Vermelho) e 'Avançar com Exceção' (Link Secundário).-
  > * -Desenhar o componente de banner de Alerta Crítico para Casos de Duplicidade de Hash SHA-256, bloqueando os botões normais e exibindo a opção 'Descartar Arquivo Duplicado'.-
  > * -Projetar a tela modal que se abre ao clicar em 'Rejeitar', contendo o seletor com os motivos regulamentares (Ilegível, Incompleto, Divergente) e a pré-visualização da mensagem assistida que será enviada ao cliente.-
  > * -Desenhar a interface de listagem “Fila de validação”, atuando como gatilho e rota de acesso principal à tela Split-Screen.-

### [SCRUM-96] HMS-US074 – Design do Frame: Monitor de Checklists e Liberação de Dossiê
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como Designer de UI, quero projetar o painel de Monitor de Checklists de Casos ativos, evidenciando o progresso percentual e o gatilho de liberação de Dossiê para a advocacia.
  > 
  > [Contexto: Entidades ChecklistCaso, Dossie | Rastreabilidade: RF-014, RF-015, RF-048]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Desenhar o cabeçalho da página utilizando a fonte Fraunces para o título 'Acompanhamento de Checklists' e Plus Jakarta Sans para metadados do caso e da Área do Direito.-
  > * -Criar o componente de Barra de Progresso Visual Horizontal (ProgressBar) que calcula dinamicamente o preenchimento dos itens documentais obrigatórios.-
  > * -Desenhar a listagem de itens do checklist divididos entre as categorias 'Obrigatórios' e 'Opcionais', exibindo os badges de status para cada arquivo: Validado (Verde), Pendente (Amarelo) ou Rejeitado (Vermelho).-
  > * -Projetar os dois estados do botão mestre 'Fechar Dossiê e Liberar para Produção': 1) Desabilitado (Disabled Gray) quando o progresso for menor que 100% e não houver exceção; 2) Habilitado (Primary Accent Color) quando o checklist estiver em total conformidade.-

### [SCRUM-93] HMS-US071 – Registro de Encerramento e Controle de Acesso Documental (Gate de Saída)
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como um Advogado, eu quero registrar o resultado final do processo jurídico e executar as travas de classificação de acesso aos documentos, para concluir o serviço mantendo a segurança da informação para futuras demandas do mesmo cliente.
  > 
  > [Rastreabilidade: RF-024, RF-043, RF-051 | Entidades: Caso, Documento, Pessoa]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Na fase de encerramento, o Advogado deve preencher um formulário estruturado contendo: Tipo de Resultado (Acordo, Decisão Judicial Procedente/Improcedente, Entrega de Produto), Descrição Detalhada e Data do Resultado. O preenchimento move o caso para 'Resultado obtido / encerramento em andamento' (Status 11).-
  > * -A tela deve exibir uma subseção para o Módulo Financeiro Incipiente do MVP, permitindo que o advogado consulte dados básicos de honorários e emita ou anexe um recibo simples (Contendo: valor, data, descrição e responsável pela emissão), sem travar o andamento por conciliações complexas.-
  > * -Painel de Governança de Acesso: A interface deve carregar a listagem de todos os documentos anexados ao caso e exibir a classificação de acesso atual (Cliente, Interno, Restrito, Confidencial, Parceiro liberado).-
  > * -O sistema deve escolher a classificação padrão de segurança como 'Interno' para todos os arquivos. A alteração para a categoria 'Cliente' ou 'Parceiro liberado' exige uma ação de clique e liberação manual do advogado, registrando a auditoria imediata.-
  > * -Após a conclusão das checagens e do arquivamento dos arquivos, o botão 'Concluir Rito de Encerramento' altera o status para 'Encerrado' (Status 12) e preserva o cadastro da Pessoa intacto para abertura de futuros intakes.-

### [SCRUM-106] HMS-US081 – Design do Frame: Dashboard de Conversão e Eficiência de Funil (Pipeline 1)
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como Designer de UI, quero projetar a interface do Dashboard de Conversão do Pipeline 1 utilizando gráficos e componentes de cartões dinâmicos, para que a diretoria consiga monitorar a saúde comercial, o volume de entrada de leads e o tempo médio de triagem de novas demandas.
  > 
  > [Contexto: Entidade Indicador / Intake | Rastreabilidade: RF-053]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Desenhar o cabeçalho principal da página com o título utilizando a fonte serifada Fraunces e um seletor global de período de tempo dinâmico (ex: 'Últimos 30 dias', 'Este Trimestre').-
  > * -Projetar a renderização visual dos 4 primeiros indicadores do MVP em formato de cartões de resumo rápido (KPI Cards): Taxa de Conversão, Volume de novos Intakes por canal, Tempo Médio de Qualificação e Índice de Perda de Oportunidades.-
  > * -Desenhar um gráfico de funil vertical de alta legibilidade que mostre a quebra de volume de leads passando pelos status de triagem e avaliação até o gate de contratação.-

### [SCRUM-108] HMS-US083 – Design do Frame: Dashboard de Performance de IA e Governança
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como Designer de UI, quero projetar a tela de Indicadores de Eficiência de IA e Exceções, evidenciando o nível de automação atingido pelo ecossistema e o volume de desvios operacionais homologados.
  > 
  > [Contexto: Entidade Indicador / SugestaoIA / Excecao | Rastreabilidade: RF-053, RF-037]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Projetar os 4 últimos indicadores analíticos do MVP organizados em cartões de destaque no topo da tela: Taxa de Automação do Checklist, Índice de Acurácia do OCR/IA, Volumetria de Exceções Aprovadas e Tempo Médio de Resposta do Cliente.-
  > * -Adicionar um componente visual de selo ou badge indicando o nível geral de conformidade com a LGPD e políticas de segurança configuradas na plataforma.-

### [SCRUM-104] HMS-US079 – Design do Frame: Central de Governança e Calibragem de IA
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como Designer de UI, quero projetar la interface do Painel de Governança de IA, para que a gestão consiga monitorar métricas de assertividade dos modelos e calibrar os limiares de confiança para automações em uma tela altamente legível.
  > 
  > [Contexto: Entidade SugestaoIA / ErroIA / SLA_Policy | Rastreabilidade: RF-037, RF-038, RF-039]
  > 
  > *Critérios de Aceitação:*
  > 
  > * -Estruturar o cabeçalho utilizando a fonte serifada Fraunces para o título 'Governança e Calibragem de IA'.-
  > * -Desenhar um painel analítico com cartões de desempenho exibindo o volume total de sugestões da IA divididas por status de feedback humano: Aceitas (Verde), Ajustadas (Amarelo) e Rejeitadas (Vermelho).-
  > * -Projetar a tabela de parametrização de limiares por Tipo Documental, contendo componentes de controle deslizante (Sliders) ou inputs numéricos para ajustar as faixas de 'Alta Confiança' (Automação Direta) e 'Baixa Confiança' (Revisão Humana Obrigatória).-
  > * -Incluir uma seção de logs estáticos contendo o registro visual de tentativas de uso bloqueado de IA (ex: tentativa de protocolo automático sem aprovação humana), sinalizadas com ícones de escudo de segurança.-

---

## Sprint: Sprint 3 - Cliente e Atendimen (CLOSED)

### [SCRUM-19] HMS-US010: Realizar triagem inicial com decisão registrada
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como atendente/intake, quero registrar a decisão de triagem e avançar o intake para o próximo estágio correto, para que a jornada do cliente progrida com a decisão documentada e rastreável.
  > 
  > *Telas:* 23 a 27
  > 
  > *Rastreabilidade:* RF-004.
  > 
  > *Critérios de Aceitação:*
  > 
  > * *CA01:* Para permitir a conclusão da triagem ou qualquer decisão, o intake deve capturar obrigatoriamente a tríade de dados da demanda: área do direito envolvida (via lista), tipo de problema jurídico (relato estruturado ou texto livre) e grau de urgência.
  > * *CA02:* A triagem deve resultar em uma das cinco decisões obrigatórias: Consulta necessária, Consulta desnecessária, Informações pendentes, Remarcação ou Encerramento.
  > * *CA03:* A decisão "Informações pendentes" move o status para "Aguardando informações" e exige o registro em campo de texto dos dados faltantes.
  > * *CA04:* A decisão "Encerramento" exige a seleção de um motivo obrigatório antes de avançar o status para "Encerrado sem contratação".
  > * *CA05:* Havendo dúvida jurídica na triagem, o atendente aciona a opção "Acionar advogado"; o sistema congela o intake em triagem aguardando a orientação do profissional antes de permitir a conclusão.

### [SCRUM-21] HMS-US012: Encerrar Intake sem contratação com motivo obrigatório
- **Status**: `Done`
- **Story Points**: 2
- **Descrição**:
  > Como atendente ou supervisor autorizado, quero encerrar um Intake sem contratação registrando o motivo, para preservar o histórico da demanda e medir corretamente os desfechos sem contratação.
  > 
  > *Escopo:* encerramento terminal do módulo de Intake.
  > 
  > *Tela Pencil:* ação de encerramento e modal de confirmação (B7EP5E).
  > 
  > ----
  > 
  > *Critérios de Aceite*
  > 
  > * [ ] *CA01 — Estados elegíveis:* *Encerrar sem contratação* fica disponível em *Consulta agendada*, *Consulta realizada*, *Viabilidade registrada* e *Em Formalização*.
  > * [ ] *CA02 — Estados terminais:* A ação não fica disponível em *Contratado* nem em *Encerrado sem contratação*. Estados terminais não podem ser reabertos no MVP.
  > * [ ] *CA03 — Confirmação:* O primeiro clique sempre abre modal padronizado; o encerramento não ocorre imediatamente.
  > * [ ] *CA04 — Motivo obrigatório:* O modal exige motivo antes de habilitar a confirmação. O campo aceita o catálogo vigente: Inviável juridicamente, Cliente desistiu, Sem contato, Fora do escopo, Encaminhado e Outro, com observação complementar quando aplicável.
  > * [ ] *CA05 — Ação destrutiva:* O rótulo é sempre *Encerrar sem contratação* e a confirmação usa variante destrutiva. Erros mantêm o modal aberto e preservam os dados preenchidos.
  > * [ ] *CA06 — Registro completo:* A transição registra status anterior, novo status, motivo, observação, autor e data/hora na linha do tempo imutável do Intake.
  > * [ ] *CA07 — Cliente preservado:* Encerrar o Intake não inativa, exclui ou altera o Cliente. O Intake encerrado permanece na listagem e no histórico do Cliente.
  > * [ ] *CA08 — Pendências relacionadas:* Agendamentos, formalizações e outras pendências relacionadas recebem os comandos de encerramento aplicáveis, sem apagar seus históricos e sem alterar dados internos de outro módulo diretamente.
  > * [ ] *CA09 — Indicadores:* O desfecho e o motivo são publicados em evento oficial para atualizar indicadores de encerramentos sem contratação, sem depender de inferência da interface.
  > * [ ] *CA10 — Permissão e servidor:* O servidor valida estado, permissão e versão atual do Intake. Ocultar o botão não é controle suficiente.
  > * [ ] *CA11 — Idempotência e concorrência:* Retentativas não criam duas transições. Se encerramento e contratação forem solicitados simultaneamente, somente a primeira transição válida é confirmada; a outra falha com o estado atual explícito.
  > * [ ] *CA12 — Privacidade:* Eventos e auditoria carregam apenas identificadores e referências mínimas, evitando texto integral da demanda e dados pessoais sem necessidade.

### [SCRUM-13] HMS-US004: Registrar e consultar consentimentos do cliente
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como colaborador autorizado, quero registrar e consultar os consentimentos de um Cliente, para que cada autorização seja explícita, rastreável e respeitada pelas atividades dependentes.
  > 
  > *Escopo:* consentimentos mantidos pela Identidade e aplicados pelos módulos que realizam atividades dependentes de autorização.
  > 
  > *Tela Pencil:* etapa Privacidade/LGPD (CmxME).
  > 
  > ----
  > 
  > *Critérios de Aceite*
  > 
  > * [ ] *CA01 — Cliente existente:* O consentimento só pode ser registrado para um Cliente já cadastrado. Cadastrar o Cliente não significa consentir.
  > * [ ] *CA02 — Tipos do MVP:* O sistema trata separadamente: tratamento de dados, comunicação por WhatsApp, comunicação por e-mail e compartilhamento com terceiros.
  > * [ ] *CA03 — Manifestação explícita:* Cada tipo exige ação explícita. Informar telefone não concede WhatsApp; informar e-mail não concede comunicação por e-mail.
  > * [ ] *CA04 — Estado inicial:* As opções não vêm marcadas previamente. A ausência de registro é exibida como *Não registrado*, não como *Revogado*.
  > * [ ] *CA05 — Concessão imutável:* Cada concessão registra tipo, autoria e data/hora. O registro é preservado e não pode ser apagado por uma ação comum.
  > * [ ] *CA06 — Revogação:* Somente um consentimento vigente pode ser revogado. A revogação cria um novo registro com status *Revogado* e data/hora; o registro anterior permanece imutável.
  > * [ ] *CA07 — Nova concessão:* Depois de revogado, o Cliente pode conceder novamente o mesmo tipo. Não pode existir mais de um consentimento vigente do mesmo tipo para o mesmo Cliente.
  > * [ ] *CA08 — Aplicação:* WhatsApp, e-mail e compartilhamento com terceiros só podem ser executados quando houver consentimento vigente do tipo correspondente. A falta ou revogação deve informar o motivo do bloqueio.
  > * [ ] *CA09 — LGPD e cadastro:* A ausência de consentimento não cria autorização implícita e não deve apagar o cadastro. O cadastro pode prosseguir, mas atividades dependentes permanecem bloqueadas sem consentimento vigente.
  > * [ ] *CA10 — Consulta:* A ficha do Cliente exibe o estado atual de cada tipo — *Vigente*, *Revogado* ou *Não registrado* — e permite consultar o histórico em ordem cronológica.
  > * [ ] *CA11 — Permissão e privacidade:* O servidor valida que o colaborador está autenticado e autorizado; a tela e os logs exibem somente os dados necessários.
  > * [ ] *CA12 — Idempotência:* Repetir uma concessão vigente, uma revogação já realizada ou uma tentativa concorrente não pode criar registros duplicados nem alterar silenciosamente o histórico.

### [SCRUM-11] HMS-US002: Localizar cliente antes de criar Intake
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como atendente autorizado, quero localizar um Cliente existente antes de concluir um Intake, para vincular a demanda ao cadastro correto e preservar seu histórico.
  > 
  > *Escopo:* etapa *Cliente* do fluxo de Intake. O Cliente pertence à Identidade; o Intake mantém apenas a referência.
  > 
  > *Telas:* etapa Cliente do Intake (zcbcc) e modal de cadastro de Cliente.
  > 
  > ----
  > 
  > *Critérios de Aceite*
  > 
  > * [ ] *CA01 — Busca autorizada:* A busca permite localizar Cliente por nome, CPF, CNPJ ou telefone, respeitando as permissões sobre dados pessoais.
  > * [ ] *CA02 — Normalização:* CPF/CNPJ podem ser informados com ou sem máscara; pontuação, espaços e formatação não alteram a identificação.
  > * [ ] *CA03 — Resultados mínimos:* Cada resultado exibe somente os dados necessários para reconhecimento: nome ou razão social, documento parcialmente protegido, contato principal, estado cadastral e quantidade ou histórico resumido de Intakes.
  > * [ ] *CA04 — Homônimos:* Resultados encontrados por nome devem permitir distinguir Clientes com nomes iguais sem expor dados desnecessários.
  > * [ ] *CA05 — Cliente encontrado:* Ao selecionar um resultado, a etapa Cliente fica vinculada ao cadastro existente e o usuário segue para a etapa Decisão. A ação principal é *Abrir cliente* quando for necessário consultar o cadastro.
  > * [ ] *CA06 — Cliente não encontrado:* O estado vazio oferece *Cadastrar cliente* e abre o fluxo de Identidade. Depois da criação, o novo Cliente retorna ao estado temporário do Intake.
  > * [ ] *CA07 — Sem duplicação de Intake:* Selecionar ou criar um Cliente não cria o Intake, não reserva ID e não aparece na listagem nem no histórico até a confirmação da terceira etapa.
  > * [ ] *CA08 — Vários Intakes:* Um Cliente pode possuir vários Intakes, inclusive simultâneos. Vincular uma nova demanda não sobrescreve vínculos ou históricos anteriores.
  > * [ ] *CA09 — Duplicidade bloqueada:* Se a Identidade bloquear a criação por documento já existente ou possível duplicidade, o usuário deve resolver o conflito antes de avançar. Não há união automática de cadastros.
  > * [ ] *CA10 — Falha e concorrência:* Falhas de busca preservam a demanda temporária; duas ações concorrentes não podem produzir dois Clientes ou dois vínculos para a mesma operação.
  > * [ ] *CA11 — Privacidade:* O servidor valida autorização em todas as operações e limita resultados, dados completos e histórico ao escopo permitido.

### [SCRUM-118] HMS-087: Aplicar Política de Segurança de Autenticação, Sessão e Bloqueio
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > *Rastreabilidade:* {{RF-054}}, {{RF-033}}, {{RF-035}}
  > 
  > 
  > 
  > *Descrição:* Como sistema de segurança, quero forçar diretrizes de controle de sessões e autenticação forte em todas as interfaces internas e portais de acesso externos, para mitigar riscos de vazamento de dados de clientes ou acessos simultâneos indevidos.
  > 
  > * *Critérios de Aceitação:*
  > 
  > * -*CA01:* Forçar o encerramento automático da sessão por inatividade técnica e aplicar política de bloqueio temporário de conta após o estouro do limite configurável de tentativas incorretas de login consecutivas.-
  > * -*CA02:* Implementar módulo de controle de sessões simultâneas que invalide e derrube a conexão mais antiga de forma automática se o mesmo usuário autenticar em um segundo terminal.-
  > * -*CA03:* Estruturar fluxo seguro de redefinição de senhas por meio de link ou token descartável enviado exclusivamente aos canais validados de e-mail ou telefone celular cadastrados.-

### [SCRUM-22] HMS-US013: Agendar consulta jurídica virtual ou presencial
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como atendente/intake, quero agendar consulta na Etapa 3 do wizard de novo intake, selecionando modalidade, canal, advogado e horário disponível, para que o intake avance para "Consulta agendada" com todos os dados registrados.
  > 
  > *Rastreabilidade:* RF-007 (v1.2), RF-003.
  > *Telas Pencil:* Atendente - Novo Intake: Agendar Consulta RF-003, RF-007
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — Modalidade:* Toggle visual entre "Virtual" (fundo teal, borda 2px) e "Presencial" (fundo branco, borda cinza).
  > * [ ] *CA02 — Canal (condicional a Virtual):* 4 opções visuais — WhatsApp, Meet, Teams, Outro. Cada opção é card selecionável com ícone e label.
  > * [ ] *CA03 — Local:* Campo desabilitado quando modalidade = Virtual (opacidade reduzida). Obrigatório quando Presencial.
  > * [ ] *CA04 — Advogado:* Select com nome e especialidade. Ao selecionar, sistema exibe card contextual com avatar, especialidade e badge informativo ("12 horários nos próximos 7 dias").
  > * [ ] *CA05 — Calendário:* Seção split — calendário de semanas à esquerda (navegação mensal) e grade de horários à direita para o dia selecionado. Slots derivados da agenda pré-configurada do advogado. Hint de duração abaixo da grade.
  > * [ ] *CA06 — Remarcação:* Exige motivo obrigatório, preservando histórico imutável das agendas passadas.
  > * [ ] *CA07 — Configurara Agenda:* Criação de tela “Configurar Agenda” com “Duração Padrão de Consulta”, “Disponibilidade Semanal” , “Bloqueios de Agenda” e seus respectivos modais.

### [SCRUM-16] HMS-US007: Registrar nova entrada com origem obrigatória via wizard de 3 etapas
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como atendente/intake, quero registrar uma nova entrada na plataforma usando um wizard guiado de 3 etapas, para que toda entrada tenha rastreabilidade de origem, pessoa vinculada e decisão inicial.
  > 
  > *Rastreabilidade:* RF-003 (v1.2), RF-001, RF-006, RF-007.
  > *Telas Pencil:* Atendente - Novo Intake: Demanda / Vincular Pessoa / Agendar Consulta / Encerrar Atendimento
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — Wizard de 3 etapas:* Tela full-page com stepper numerado (1 Demanda → 2 Cliente → 3 Decisão). Stepper exibe progresso visual: etapa ativa (brand escuro), concluída (verde + check), futura (outline cinza).
  > * [ ] *CA02 — Etapa 1 Demanda:* Card com 3 blocos: (1) Origem + Canal (2 selects); (2) Área do Direito + Tipo de Demanda + Urgência (3 selects); (3) Observações (textarea opcional). Footer: "Próximo".
  > * [ ] *CA03 — Etapa 2 Cliente:* Card "Vincular pessoa ao intake" com busca por telefone ou nome, exibição de pessoa encontrada com avatar, dados resumidos e badge "Vinculado". Botão "Cadastrar nova pessoa" abre dialog modal de cadastro (RF-001). Footer: "Anterior" + "Próximo".
  > * [ ] *CA04 — Etapa 3 Decisão:* Decision grid com 2 cards lado a lado: "Agendar consulta" (ícone calendar-check, fundo teal) e "Encerrar atendimento" (ícone door-open). Seleção determina formulário exibido abaixo. Header ganha "Cancelar" + "Salvar intake".
  > * [ ] *CA05 — Campos obrigatórios:* Origem e Canal são obrigatórios na Etapa 1. Pessoa vinculada é obrigatória na Etapa 2. Decisão é obrigatória na Etapa 3.
  > * [ ] *CA06 — Auditoria:* Intake criado com status "Novo registro" e log com: usuário, data/hora, pessoa, origem, canal e terceiro (se aplicável).

### [SCRUM-10] HMS-US001: Cadastrar cliente com prevenção de duplicidade
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como atendente autorizado, quero cadastrar um Cliente pessoa física ou jurídica após verificar seus identificadores, para manter um cadastro único na Identidade e evitar duplicidades.
  > 
  > *Escopo:* cadastro de Cliente mantido pelo módulo de Identidade, quando iniciado a partir do fluxo de Intake.
  > 
  > *Telas Pencil:* Cadastro de cliente — Identificação, Duplicidade Encontrada, Não Encontrada, Dados Cadastrais, Privacidade LGPD e Revisão.
  > 
  > ----
  > 
  > *Critérios de Aceite*
  > 
  > * [ ] *CA01 — Modal em cinco etapas:* O cadastro ocorre em modal com stepper: Identificação → Busca/Deduplicação → Dados cadastrais → Privacidade/LGPD → Revisão.
  > * [ ] *CA02 — Identificação:* O usuário informa CPF para Cliente pessoa física ou CNPJ para Cliente pessoa jurídica; o documento deve ser validado antes da conclusão. A busca também pode usar telefone ou nome conforme a permissão.
  > * [ ] *CA03 — Normalização:* Máscara, pontuação, espaços e diferenças de formatação não podem permitir dois cadastros para o mesmo CPF ou CNPJ.
  > * [ ] *CA04 — Duplicidade:* Se o documento já existir, o sistema exibe dados mínimos para reconhecimento, bloqueia a criação de outro Cliente e oferece *Abrir cliente* ou buscar outro documento. Cadastros não são mesclados automaticamente.
  > * [ ] *CA05 — Cadastro pessoa física:* Nome completo e CPF são obrigatórios. E-mail, telefone e endereço podem ser informados; quando preenchido, o endereço deve conter logradouro, número, bairro, cidade, estado e CEP, com complemento opcional.
  > * [ ] *CA06 — Cadastro pessoa jurídica:* Razão social e CNPJ são obrigatórios. Nome fantasia, e-mail, telefone e endereço são opcionais conforme as regras do cadastro. Representantes e sócios não fazem parte desta US.
  > * [ ] *CA07 — Dados completos:* O cadastro deve ser concluído por inteiro ou não ser criado. Erros de validação preservam os dados já informados.
  > * [ ] *CA08 — Tipo imutável:* Pessoa física não pode ser convertida em pessoa jurídica, nem o inverso, pela edição cadastral comum.
  > * [ ] *CA09 — Sem conta de acesso:* Criar um Cliente não cria uma conta para acesso à plataforma.
  > * [ ] *CA10 — Consentimento separado:* Criar o Cliente não concede consentimentos automaticamente. Consentimentos dependem de manifestação explícita e registro próprio.
  > * [ ] *CA11 — Integração com Intake:* Quando o cadastro for iniciado durante um Intake, o Cliente pode ser selecionado no estado temporário do fluxo. A criação do Cliente, sozinha, não cria nem publica um Intake.
  > * [ ] *CA12 — Autorização e auditoria:* O servidor valida permissão, registra autoria e data das alterações e impede repetição acidental ou concorrente que resulte em duplicidade.

### [SCRUM-49] HMS-US040: Visualizar histórico de comunicações por pessoa, intake ou caso
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como atendente, paralegal ou advogado, quero visualizar o histórico completo de comunicações vinculadas a uma pessoa, intake ou caso, para que o contexto de relacionamento esteja sempre disponível sem consultar múltiplos sistemas.
  > 
  > *Critérios de Aceitação:*
  > 
  > * -*CA01:* A listagem exibe as interações em ordem cronológica inversa (mais recentes primeiro), destacando o canal, responsável técnico e o badge visual de visibilidade.  -
  > * -*CA02:* Mensagens capturadas automaticamente por integrações de APIs (WhatsApp) recebem obrigatoriamente a tag visual "Auto" para diferenciação das notas manuais.  -
  > * *CA03:* O usuário pode aplicar filtros rápidos diretamente na timeline para isolar comunicações urgentes com status de "requer ação" pendente.  
  > * *CA04:* Registros que foram compartilhados externamente com portais exibem marcadores coloridos diferenciados para alertar a equipe sobre a exposição pública do dado.  
  > 
  > *Rastreabilidade:* RF-027.

---

## Sprint: Sprint 4 - Adv. Paralegal e WP (CLOSED)

### [SCRUM-59] HMS-US050: Aceitar, ajustar ou rejeitar sugestão de IA com rastreabilidade
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como paralegal ou advogado  quero visualizar sugestões da IA no contexto da tarefa e decidir sobre elas com feedback registrado, para que a IA acelere meu trabalho sem nunca substituir minha decisão.
  > 
  > *Telas: 40 a 41. Talvez seja necessária a inclusão de mais telas.*
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - A interface exibe a sugestão com: badge "Sugestão IA", tipo de ação, conteúdo sugerido, nível de confiança (quando disponível) e três botões: Aceitar · Ajustar · Rejeitar.
  > * CA02 - Alta confiança: botão Aceitar em destaque. Baixa confiança: badge amarelo "Revisão recomendada", botão Ajustar em destaque.
  > * CA03 - Ao ajustar: o conteúdo sugerido é pré-preenchido em campo editável; o usuário edita e confirma; o status final é "Ajustada" com conteúdo final salvo.
  > * CA04 - Ao rejeitar: campo de motivo obrigatório aparece; após preenchimento e confirmação, status = "Rejeitada" e ErroIA é criado com todos os campos obrigatórios.
  > * CA05 - Ao bloquear: status = "Bloqueada"; o sistema não gera novas sugestões do mesmo tipo para a mesma entidade até revisão do administrador.
  > * CA06 - O fluxo de trabalho nunca é bloqueado pela sugestão de IA; o usuário pode prosseguir manualmente independente da sugestão apresentada.

### [SCRUM-31] HMS-US022: Validar, ajustar ou rejeitar documento individualmente
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como paralegal, quero revisar a classificação sugerida pela IA para cada documento e registrar minha decisão, para que o status de cada documento reflita a decisão humana com auditoria completa.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - A fila de revisão exibe para cada documento: preview, tipo sugerido pela IA, nível de confiança disponível, qualidade indicada e vínculo ao checklist sugerido.
  > * CA02 - Ao validar: paralegal confirma ou ajusta tipo documental e vínculo ao checklist; status avança para "Validado".
  > * CA03 - Ao rejeitar por ilegibilidade: status avança para "Ilegível"; sistema gera Pendencia e prepara MensagemAssistida de reenvio.
  > * CA04 - Ao rejeitar por incompletude: status avança para "Incompleto"; campo de motivo ("faltando página/verso") é obrigatório.
  > * CA05 - Ao confirmar duplicidade: paralegal vincula ao documento original; status avança para "Duplicado"; documento não conta duas vezes no checklist.
  > * CA06 - Ao rejeitar por não correspondência: paralegal registra que o documento não corresponde ao item exigido; status avança para "Não corresponde".
  > * CA07 - Toda correção humana de classificação incorreta da IA gera registro em ErroIA com: tipo de erro, resultado sugerido, correção humana, usuário que corrigiu e data/hora.
  > * CA08 - Divergência com impacto jurídico: paralegal aciona advogado antes de finalizar; documento permanece em revisão até orientação recebida.

### [SCRUM-127] HMS-US089: Gerar documento com apoio de IA a partir de template
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como advogado, quero gerar documentos (contratos, procurações, termos, peças) a partir de templates parametrizáveis com IA, para que a redação seja acelerada mantendo revisão humana obrigatória.
  > 
  > *Rastreabilidade:* RF-056 (v1.2 — Novo). Substitui RF-019.
  > 
  > ----
  > 
  > *Critérios de Aceite:*
  > 
  > * [ ] *CA01 — Arquitetura AI-at-runtime:* Sistema envia à IA: template com tokens {{variavel}} + dados disponíveis (ficha, consulta, condições comerciais, cliente, escritório). IA redige texto adaptado ao contexto.
  > * [ ] *CA02 — Revisão humana obrigatória:* Texto gerado é rascunho até aprovação. Bloqueio de envio/assinatura/protocolo se não aprovado.
  > * [ ] *CA03 — Dados insuficientes:* Sistema identifica variáveis obrigatórias sem dados e exibe status "Falta info" com indicação do que falta. Documento gerado parcialmente com lacunas marcadas.
  > * [ ] *CA04 — Geração em lote:* Via Pacote da Consulta (HMS-US088), gera todos os documentos marcados em uma ação. Status individual por documento.
  > * [ ] *CA05 — Unificação:* Este mecanismo é único para contratos, procurações, termos e peças jurídicas. Os 7 modelos de honorários não são templates separados; são estados do formulário de Condições Comerciais.
  > * [ ] *CA06 — Auditoria:* Toda geração registrada em SugestaoIA (RF-037) e LogAuditoria (RF-042).

### [SCRUM-23] HMS-US014: Registrar consulta realizada com Ficha de Atendimento estruturada
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como advogado, quero registrar a consulta realizada usando uma Ficha de Atendimento estruturada em 11 seções com apoio de IA, para que o registro seja completo, padronizado e rastreável.
  > 
  > *Rastreabilidade:* RF-008 (v1.2), RF-009, RF-037, RF-038.
  > *Telas Pencil:* Advogado - Consulta: Detalhes / Ficha de Atendimento
  > 
  > ----
  > 
  > *Critérios de Aceite (v1.2):*
  > 
  > * [ ] *CA01 — 3 abas:* Tela com abas Detalhes (resumo), Ficha de Atendimento (formulário) e Pacote de Consulta (documentos — ver HMS-US088).
  > * [ ] *CA02 — Aba Detalhes:* Card Cliente & Origem (split horizontal), card Contexto (fundo teal), card Agendamento, CTA para iniciar Ficha.
  > * [ ] *CA03 — Ficha de Atendimento (11 seções):* (1) Qualificação, (2) Área e Tema, (3) Dados Trabalhistas (condicional), (4) Perguntas Direcionadas (borda teal, chips), (5) Fatos e Linha do Tempo (lista ordenável + "Extrair com IA"), (6) Pretensão e Pedidos (lista + IA + descartados), (7) Relato e Histórico (textareas + "Gerar com IA"), (8) Documentos e Pendências, (9) Diagnóstico Jurídico, (10) Viabilidade e Decisão, (11) Condições Comerciais Preliminares.
  > * [ ] *CA04 — Autosave:* Indicador visual de salvamento automático no footer. Botão "Finalizar" em cor primária.
  > * [ ] *CA05 — IA assistiva:* Botões "Extrair com IA" e "Gerar com IA" em seções específicas. Toda sugestão é revisável/editável antes de ser aceita (RF-037/038).
  > * [ ] *CA06 — Aba Pacote bloqueada:* Aba Pacote de Consulta exibida com opacity 0.5 e badge lock até Ficha estar completa.

### [SCRUM-51] HMS-US042: Receber documentos via WhatsApp e criar lote documental
- **Status**: `Done`
- **Story Points**: 8
- **Descrição**:
  > Como sistema, quero ao receber documentos pelo WhatsApp, criar lote documental com auditoria completa e verificar permissão de terceiros, para que documentos recebidos pelo canal principal sejam integrados ao motor documental sem intervenção manual.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Ao receber arquivo (documento, imagem ou PDF) pelo WhatsApp oficial, o sistema cria LoteDocumental preservando: nome do arquivo, tipo MIME, tamanho, hash SHA-256, canal (WhatsApp), remetente e data/hora.
  > * CA02 - Remetente identificado como terceiro: o sistema verifica se o terceiro tem permissão de apoiador documental para o cliente ou caso vinculado. Sem permissão, bloqueia o vínculo, registra a tentativa em log e notifica o atendimento.
  > * CA03 - Lote identificado segue para classificação documental (IA/OCR ou manual).
  > * CA04 - Lote não identificado vai para caixa de triagem.
  > * CA05 - Arquivo com formato não suportado é rejeitado; sistema prepara mensagem assistida ao remetente indicando formatos aceitos.
  > * CA06 - Auditoria do arquivo recebido registra obrigatoriamente: nome, tipo, tamanho, hash/identificador, lote, remetente e status inicial.

### [SCRUM-126] HMS-US088: Gerar Pacote de Documentos da Consulta
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como advogado, quero gerar os documentos obrigatórios e condicionais da consulta em lote com apoio de IA, para que o pacote esteja pronto para a formalização sem retrabalho manual.
  > 
  > *Rastreabilidade:* RF-008 (v1.2), RF-056.
  > *Telas Pencil:* Advogado - Pacote de Consulta: Configuração / Documentos Gerados
  > 
  > ----
  > 
  > *Critérios de Aceite:*
  > 
  > * [ ] *CA01 — Aba Pacote de Consulta:* Aba dedicada na tela de Consulta, bloqueada (opacity 0.5 + lock) até Ficha estar completa.
  > * [ ] *CA02 — Estado 1 Configuração:* Card com seção "Sempre Gerados" (docs obrigatórios com badge "Obrigatório" + lock — ex.: Procuração, Termo LGPD) e "Documentos Condicionais" (checkbox para marcar aplicabilidade — ex.: Declaração Hipossuficiência, Minuta Petição Inicial).
  > * [ ] *CA03 — Geração com IA:* Botão "Gerar documentos" com ícone sparkles aciona geração em lote usando AI-at-runtime (RF-056): template + dados da consulta como contexto.
  > * [ ] *CA04 — Estado 2 Documentos Gerados:* Painel com lista de documentos. Cada linha: ícone, nome, descrição, coluna status (108px: dot + texto) e coluna ação (140px: botão contextual).
  > * [ ] *CA05 — Status por documento:* "Pronto" (dot verde, botão "Revisar" teal) ou "Falta info" (dot amarelo, botão "Completar" dourado com indicação do que falta — ex.: "Faltam RG e endereço completo").
  > * [ ] *CA06 — Governança IA:* Toda geração auditada (RF-037/042). Documentos são rascunho até aprovação humana.

### [SCRUM-50] HMS-US041: Receber mensagem de texto via WhatsApp oficial e registrar na Central
- **Status**: `Done`
- **Story Points**: 8
- **Descrição**:
  > Como sistema, quero receber mensagens de texto pelo WhatsApp oficial, vinculá-las à entidade correta e registrar na Central de Comunicação, para que toda comunicação recebida pelo WhatsApp seja rastreável sem ação manual da equipe.
  > 
  > *Critérios de Aceitação:*
  > 
  > * *CA01:* A plataforma deve suportar múltiplos números oficiais de WhatsApp Business API de forma simultânea, permitindo linhas dedicadas para advogados ou unidades regionais (ex.: filial de Indaiatuba).
  > * *CA02:* O sistema deve ser parametrizado para identificar a linha oficial de origem de cada mensagem e organizar os fluxos de atendimento direcionando-os ao responsável vinculado àquela linha específica.
  > * *CA03:* Mensagens recebidas de números de telefone com correspondência na base são automaticamente anexadas à linha do tempo da Central de Comunicação do cliente.
  > * *CA04:* Mensagens de remetentes não identificados são desviadas para a Caixa de Triagem com o status "Sem vínculo identificado".
  > * *CA05:* O sistema bloqueia a integração de números ou contas de WhatsApp pessoais de colaboradores no MVP.
  > * *CA06:* Cada evento capturado gera um registro de log contendo: canal, remetente, data/hora, número de origem e entidade vinculada.
  > 
  > *Rastreabilidade:* RF-029.

### [SCRUM-25] HMS-US016: Registrar avaliação de viabilidade jurídica
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como advogado, quero registrar formalmente a avaliação de viabilidade (Viável / Inviável / Pendente) com justificativa, para que o intake avance corretamente com a responsabilidade técnica do advogado documentada.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Somente perfil Advogado acessa e salva a avaliação de viabilidade; outros perfis veem campo readonly com mensagem "Aguardando avaliação do advogado".
  > * CA02 - Seleção entre Viável · Inviável · Pendente é obrigatória; justificativa é obrigatória (mín. 20 caracteres) para qualquer opção.
  > * CA03 - Viável → intake avança para "Viável — aguardando formalização".
  > * CA04 - Inviável → sistema exige motivo de inviabilidade e avança para "Encerrado sem contratação".
  > * CA05 - Pendente → intake permanece em "Em avaliação de viabilidade"; advogado registra o que está pendente e a ação necessária para retomar.
  > * CA06 - A IA não exibe sugestão de decisão de viabilidade; pode apenas exibir fatos e pendências organizados como apoio à decisão do advogado.

### [SCRUM-29] HMS-US020: Gerenciar caixa de triagem de lotes não identificados
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > Como paralegal ou atendente, quero acessar a caixa de triagem, avaliar lotes não identificados e vinculá-los manualmente, para que nenhum arquivo recebido fique sem processamento por falta de identificação automática.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - A caixa de triagem exibe lotes e mensagens com status "Identificação pendente" com: canal, remetente, tipo, data/hora e preview do conteúdo.
  > * CA02 - O usuário pode vincular um lote a uma Pessoa, Intake, Caso ou Terceiro via busca; após vínculo, o lote segue para classificação documental.
  > * CA03 - O usuário pode rejeitar um item com motivo obrigatório; o item é arquivado com o log de rejeição preservado.
  > * CA04 - Se o remetente não estiver cadastrado e o conteúdo justificar, o atendente pode iniciar cadastro de Pessoa diretamente da caixa de triagem e depois vincular o lote.
  > * CA05 - A caixa de triagem exibe badge de contagem no menu de navegação quando houver itens pendentes.
  > * CA06 - Toda ação na caixa de triagem (vínculo ou rejeição) gera log com: usuário, decisão, entidade vinculada e data/hora.

### [SCRUM-28] HMS-US019: Criar lote documental automaticamente ao receber arquivos
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como sistema, quero criar automaticamente um lote documental ao receber qualquer arquivo por qualquer canal, para que todo recebimento documental seja rastreável com origem, remetente e data/hora preservados.
  > 
  > *Critérios de Aceitação:*
  > 
  > * -CA01 - Todo recebimento de arquivo (WhatsApp, portal do cliente, portal de terceiros ou upload interno) cria automaticamente um LoteDocumental com: canal_origem, remetente, data/hora e lista de arquivos.-
  > * -CA02 - O lote é criado com status "Recebido"; se o sistema identificar com confiança suficiente a entidade vinculada (pessoa/intake/caso), avança para "Identificado".-
  > * CA03 - Se não identificar a entidade vinculada com confiança suficiente, o lote vai para a caixa de triagem com status "Identificação pendente" e na_caixa_triagem = TRUE.
  > * CA04 - O sistema gera número legível único no formato LOTE-YYYYMMDD-NNNN e registra evento na Central de Comunicação.
  > * CA05 - Em caso de falha de recebimento, o sistema registra o IntegracaoEvento com: origem, destino, erro, tentativas e status; executa reprocessamento automático para falhas transitórias.
  > * -CA06 - Upload direto pela equipe HMS cria lote vinculado automaticamente à entidade em contexto (caso ou intake aberto) com o usuário como remetente.-

### [SCRUM-54] HMS-US045: Acessar portal do cliente com visão simplificada do caso
- **Status**: `Done`
- **Story Points**: 5
- **Descrição**:
  > Como cliente, quero acessar um portal com o status simplificado do meu caso, documentos pendentes e mensagens liberadas, para que eu acompanhe minha jornada sem depender de contato manual com o escritório.
  > 
  > Lembre-se de garantir que o banco de dados já possua a lógica básica de {{status_relacional}} e tabelas de relacionamento, pois o portal exige a assinatura de contrato (marco de contratação) ou um intake ativo para liberar o acesso.
  > 
  > *Telas: 01 a 06*
  > 
  > *Critérios de Aceitação:*
  > 
  > * *CA01:* O gatilho técnico para habilitar o acesso e gerar as credenciais do cliente para o portal é a assinatura do contrato (marco de contratação com caso ativo no sistema).
  > * *CA02:* Interessados, leads ou clientes potenciais sem contrato assinado são permanentemente bloqueados de acessar o portal completo, sendo retidos em uma "antessala" com dados institucionais gerais.
  > * *CA03:* A tela exibe unicamente informações simplificadas autorizadas pela equipe interna: status do caso, lista de documentos pendentes solicitados e mensagens explicitamente liberadas.
  > * *CA04:* O número do processo judicial ou andamentos processuais externos só aparecem na tela do cliente se marcados como "liberados" na área interna da HMS.
  > * *CA05:* O sistema bloqueia por padrão a exibição de notas de estratégia jurídica, pareceres, comunicações internas ou dados financeiros restritos.
  > * *CA06:* Cada tentativa de login, logout ou carregamento de página gera logs de auditoria detalhados no painel administrativo.
  > 
  > *Rastreabilidade:* RF-033, RF-010.

---

## Sprint: Sprint 5 - Formalização (ACTIVE)

### [SCRUM-33] HMS-US024: Atualizar checklist automaticamente com documento validado
- **Status**: `In Progress`
- **Story Points**: 5
- **Descrição**:
  > Como sistema, quero atualizar automaticamente o item correspondente do checklist ao validar um documento, para que a completude do checklist reflita o estado real da documentação sem entrada manual.
  > 
  > *Rastreabilidade:* RF-015.
  > 
  > *Critérios de Aceitação:*
  > 
  > *CA01:* O Checklist Documental de cada caso é instanciado automaticamente no momento da abertura a partir de um template padrão associado à Área do Direito e tipo de serviço selecionado.
  > 
  > * *CA02:* O Advogado Principal do caso possui alçada para incluir itens complementares/avulsos específicos para o caso concreto, sem que isso modifique o template padrão de origem.
  > * *CA03:* Quando um documento é marcado como "Validado" pelo paralegal ou classificado com alta confiança pela IA, o sistema vincula o arquivo ao item correspondente do checklist.
  > * *CA04:* A cada documento vinculado, a plataforma recalcula a barra de progresso de completude do checklist.
  > * *CA05:* Atendidos todos os documentos obrigatórios da matriz, o status do checklist avança automaticamente para "Completo para validação", notificando os responsáveis.

### [SCRUM-128] HMS-US091: Rastrear ciclo de vida de assinatura eletrônica
- **Status**: `In Progress`
- **Story Points**: 0
- **Descrição**:
  > Como paralegal, quero rastrear o status de assinatura de cada documento enviado, para que eu saiba quais documentos foram assinados e quais estão pendentes.
  > 
  > *Rastreabilidade:* RF-058 (v1.2 — Novo).
  > *Telas Pencil:* Advogado - Formalização: Pós-envio
  > 
  > ----
  > 
  > *Critérios de Aceite:*
  > 
  > * [ ] *CA01 — Estados binários no MVP:* Assinado (dot teal, badge verde, ação "Ver assinado") e Não assinado (dot cinza, badge muted). Estados intermediários fora do MVP.
  > * [ ] *CA02 — Progress bar:* "2 de 4 documentos assinados · 50%" com barra visual.
  > * [ ] *CA03 — Footer contextual:* "Aguardando 2 assinaturas · 3 dias desde o envio · expira em 12 dias".
  > * [ ] *CA04 — Integração D4Sign:* Webhook para atualização automática. API pull como contingência (RF-050).
  > * [ ] *CA05 — Reenvio:* Ação "Reenviar link para cliente" disponível enquanto houver docs não assinados. Auditado.
  > * [ ] *CA06 — Cancelamento:* Ação destrutiva "Cancelar pacote" com motivo obrigatório.
  > * [ ] *CA07 — Arquitetura agnóstica:* Projetada para ser independente de provedor.

### [SCRUM-32] HMS-US023: Controlar classificação de acesso de cada documento
- **Status**: `Done`
- **Story Points**: 3
- **Descrição**:
  > 🎯 Descrição da História
  > _Como_ Paralegal ou Advogado,
  > _Quero_ definir e gerenciar a classificação de acesso diretamente na _instância do documento gerado/armazenado_ ({{Documento}}),
  > _Para que_ arquivos reais com dados de clientes nunca sejam expostos externamente sem liberação expressa e rastreável.
  > 
  > ----
  > 
  > DIRETRIZ ARQUITETURAL OBRIGATÓRIA (LEIA ANTES DE IMPLEMENTAR)
  > 
  > ----
  > 
  > Taxonomia de Acesso no Documento Gerado
  > 
  > * {{INTERNO}} *(Default):*
  > ** _Acesso Interno:_ Advogados e Paralegais alocados ao caso
  > ** _Acesso Externo:_ ❌ Ninguém
  > ** _Finalidade:_ Minutas de trabalho, arquivos em elaboração e notas internas.
  > * {{CLIENTE}}*:*
  > ** _Acesso Interno:_ Advogados e Paralegais alocados ao caso
  > ** _Acesso Externo:_ ✅ Cliente titular
  > ** _Finalidade:_ Contrato assinado, procuração, relatórios e peças protocoladas.
  > * {{RESTRITO}}*:*
  > ** _Acesso Interno:_ Advogados e Paralegais responsáveis
  > ** _Acesso Externo:_ ❌ Ninguém
  > ** _Finalidade:_ Dados financeiros e certidões com dados de terceiros.
  > * {{CONFIDENCIAL}}*:*
  > ** _Acesso Interno:_ Apenas Advogado Responsável e Admin
  > ** _Acesso Externo:_ ❌ Ninguém
  > ** _Finalidade:_ Segredo de justiça, extratos fiscais/bancários e relatórios de risco.
  > * {{PARCEIRO_LIBERADO}}*:*
  > ** _Acesso Interno:_ Advogados, Paralegais + Parceiro homologado indicado
  > ** _Acesso Externo:_ ✅ Parceiro específico
  > ** _Finalidade:_ Laudos periciais e guias de custas para correspondentes.
  > 
  > _\{color:#de350b}Regra de Atendente:_\{color} Atendentes _NÃO possuem permissão de visualização para nenhum documento_, independentemente do nível de classificação.
  > 
  > ----
  > 
  >  Critérios de Aceitação
  > 
  > * _CA01 — Privacy by Default na Geração:_
  > ** No momento em que um documento é gerado a partir de um template pelo sistema, o registro correspondente na tabela {{documentos}} deve ser persistido com {{classificacao_acesso = 'INTERNO'}} por padrão.
  > ** A tela/formulário de templates de documentos não deve conter nenhum campo ou configuração sobre classificação de acesso.
  > * _CA02 — Alteração da Classificação na Ação do Documento:_
  > ** O controle de alteração do nível de acesso deve ficar no menu de contexto/ações do próprio documento (dentro de "Documentos do Caso", "Dossiê" ou "Arquivos do Intake").
  > ** Alterar para {{CLIENTE}} ou {{PARCEIRO_LIBERADO}} exige ação explícita e confirmação em modal.
  > ** Para {{PARCEIRO_LIBERADO}}, o sistema deve exigir a seleção obrigatória do parceiro homologado destinatário.
  > ** O sistema deve registrar: {{usuario_id}}, {{data_hora}}, {{classificacao_nova}} e {{destinatario_identificador}}.
  > * _CA03 — Bloqueio de Acesso Externo & Log de Violação:_
  > ** Qualquer tentativa de acesso externo via link/token a documentos com status {{INTERNO}}, {{RESTRITO}} ou {{CONFIDENCIAL}} deve retornar erro {{HTTP 403 Forbidden}}.
  > ** Toda recusa deve gerar log na tabela {{logs_acesso_externo}} com: {{documento_id}}, {{ip_origem}}, {{token_utilizado}}, {{data_hora}} e {{motivo_negativa}}.
  > * _CA04 — Exibição Visual (Badges) na Listagem de Arquivos:_
  > ** Em todas as listagens de arquivos gerados (Dossiê, Arquivos do Intake, Documentos do Cliente), exibir badge com as cores padronizadas:
  > *** {{INTERNO}}: Cinza
  > *** {{CLIENTE}}: Azul
  > *** {{RESTRITO}}: Laranja / Âmbar
  > *** {{CONFIDENCIAL}}: Vermelho
  > *** {{PARCEIRO_LIBERADO}}: Roxo
  > * _CA05 — Trilha de Auditoria Imutável (Audit Trail):_
  > ** Toda alteração no campo {{classificacao_acesso}} da tabela {{documentos}} deve inserir um registro imutável em {{auditoria_documentos}} contendo:
  > *** {{documento_id}}
  > *** {{usuario_responsavel_id}}
  > *** {{valor_anterior}}
  > *** {{valor_novo}}
  > *** {{created_at}}
  > * _CA06 — Restrição por Perfil (RBAC):_
  > ** Somente _Advogados_, _Paralegais_ e _Administradores_ podem visualizar e gerenciar a classificação dos documentos.
  > ** Perfis com role _Atendente_ possuem bloqueio total de visualização, download ou listagem para _qualquer documento_.

### [SCRUM-34] HMS-US025: Aprovar checklist como gate obrigatório para produção jurídica
- **Status**: `In Review`
- **Story Points**: 5
- **Descrição**:
  > Como paralegal ou advogado, quero aprovar o checklist final como gate de avanço para produção jurídica, para que nenhum caso entre em produção sem documentação validada e aprovada por perfil autorizado.
  > 
  > *Rastreabilidade:* RF-016.
  > 
  > *Critérios de Aceitação:*
  > 
  > * *CA01:* O sistema trata o Checklist e o Dossiê Documental como dois gates sequenciais, distintos e obrigatórios.
  > * *CA02:* A aprovação humana do checklist final avança o status do caso para "Pronto para produção jurídica" no Pipeline 2, mas não libera a escrita até que o Dossiê seja homologado na sequência.
  > * *CA03:* Havendo pendências cobertas por uma exceção previamente autorizada, o usuário pode realizar a aprovação com o status "Aprovado com exceção", exibindo as ressalvas na tela.
  > * *CA04:* O sistema bloqueia de forma estrita o avanço para a fase de produção caso o checklist esteja marcado como "Bloqueado/insuficiente".
  > * *CA05:* O advogado pode reprovar e bloquear o avanço mesmo que o checklist esteja formalmente completo se identificar insuficiência jurídica de mérito na análise das peças.

### [SCRUM-52] HMS-US043: Registrar áudio e chamada de voz recebidos via WhatsApp
- **Status**: `In Review`
- **Story Points**: 3
- **Descrição**:
  > Como atendente ou paralegal, quero registrar áudios e chamadas de voz recebidos pelo WhatsApp como comunicações na Central, para que o histórico de interações seja completo mesmo para modalidades sem transcrição automática.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - Ao detectar áudio ou chamada de voz pelo WhatsApp oficial, o sistema cria registro na Central com: tipo (áudio ou chamada de voz), canal (WhatsApp), remetente e data/hora.
  > * CA02 - O sistema tenta vincular o evento à entidade correspondente pelo número do remetente.
  > * CA03 - O responsável complementa o registro com resumo manual do conteúdo após o atendimento.
  > * CA04 - Transcrição automática de áudio não está disponível no MVP; a tela exibe nota: "Resumo manual necessário. Transcrição automática disponível em versão futura."
  > * CA05 - Evento sem vínculo identificado vai para caixa de triagem com tipo identificado.

---

## Sprint: Sprint 6 (ACTIVE)

### [SCRUM-26] HMS-US017: Controlar formalização e registrar data de contratação
- **Status**: `To Do`
- **Story Points**: 5
- **Descrição**:
  > h2. US02 - HMS-US017: Controlar formalizacao e registrar data de contratacao
  > 
  > h3. Identificacao
  > 
  > * Codigo no Backlog: SCRUM-26
  > * Codigo da US: HMS-US017
  > * Titulo: Controlar formalizacao e registrar data de contratacao
  > * Modulos PRD: Modulo de Formalizacao e Modulo de Intake
  > 
  > h3. Historia de Usuario
  > 
  > Como paralegal ou atendente,
  > 
  > Quero registrar o andamento da formalizacao contratual e concluir o rito de contratacao,
  > 
  > Para avançar o intake para o status "Contratado" e registrar a data oficial de contratacao para alimentacao dos indicadores de desempenho.
  > 
  > h3. Contexto e Regras de Negocio
  > 
  > # Painel de Acompanhamento da Formalizacao:
  > 
  > * A tela de formalizacao deve listar todos os documentos contratuais associados ao intake (ex: Contrato de Honorarios, Procuracao, Declaracao de Hipossuficiencia).
  > * Cada documento possui um status individual obrigatorio: Pendente, Recebido ou Assinado.
  > 
  > # Registro do Tipo de Assinatura:
  > 
  > * O sistema deve permitir registrar o tipo de assinatura utilizado para cada documento: Fisica (documento impresso e assinado manualmente), Digital (certificado digital ICP-Brasil) ou Eletronica (plataforma de assinatura via token/link).
  > 
  > # Regra de Elegibilidade para Conclusao:
  > 
  > * A conclusao da formalizacao exige obrigatoriamente que pelo menos um documento contratual principal esteja com o status "Recebido" ou "Assinado".
  > * Se todos os documentos estiverem com status "Pendente", o botao de conclusao deve permanecer desabilitado.
  > 
  > # Data de Contratacao e Indicadores:
  > 
  > * Ao concluir a formalizacao com sucesso, a data_contratacao deve ser gravada automaticamente pelo servidor com a data/hora atual (TIMESTAMPTZ).
  > * Esse campo e o gatilho oficial para o calculo do Indicador MVP numero 4 (Tempo medio de qualificacao e contratacao).
  > 
  > # Transicao de Status e Gatilho para o Caso:
  > 
  > * Na conclusao bem-sucedida, o Intake avança automaticamente para o status "Contratado — abrir caso/servico" e envia a notificacao de evento para instanciacao do Caso no Pipeline 2.
  > 
  > # Encerramento por Insucesso:
  > 
  > * Se a formalizacao for interrompida ou recusada pelo cliente, o usuario deve acionar a acao de encerramento do intake, sendo obrigatorio selecionar um motivo valido do catalogo regulamentar.
  > 
  > h3. Criterios de Aceite (CA)
  > 
  > * CA01 [Lista de Documentos Contratuais]: A interface de formalizacao deve exibir a tabela de documentos exigidos mostrando o nome do arquivo, status individual (Pendente, Recebido, Assinado) e o tipo de assinatura selecionado.
  > * CA02 [Validaçao para Conclusao]: O sistema deve bloquear a tentativa de conclusao da formalizacao caso nenhum documento esteja marcado como "Recebido" ou "Assinado", exibindo a mensagem "E necessario ter ao menos um documento recebido ou assinado para concluir a contratacao".
  > * CA03 [Gravacao Automatica da Data]: Ao clicar em "Concluir Contratacao", o backend deve definir data_contratacao = CURRENT_TIMESTAMP e atualizar o status do Intake para "Contratado — abrir caso/servico".
  > * CA04 [Integracao com Pipeline 2]: A alteracao de status do Intake para "Contratado" deve emitir um evento interno síncrono/assíncrono solicitando a abertura do Caso correspondente no Pipeline 2.
  > * CA05 [Encerramento sem Contratacao]: Caso o usuario selecione "Encerrar Formalizacao", o sistema deve exigir a escolha do motivo (ex: Desistência do Cliente, Inviabilidade Financeira) antes de alterar o status para "Encerrado sem contratacao".
  > 
  > ----

### [SCRUM-30] HMS-US021: Processar documento com IA/OCR e controlar status individual
- **Status**: `To Do`
- **Story Points**: 8
- **Descrição**:
  > h2. US04 - HMS-US021: Processar documento com IA/OCR e controlar status individual
  > 
  > h3. Identificacao
  > 
  > * Codigo no Backlog: SCRUM-30
  > * Codigo da US: HMS-US021
  > * Titulo: Processar documento com IA/OCR e controlar status individual
  > * Modulo PRD: Modulo de Motor Documental (PRD - Modulo de Motor Documental)
  > 
  > h3. Historia de Usuario
  > 
  > Como sistema e Paralegal,
  > 
  > Quero processar cada arquivo recebido em um lote via OCR e IA para identificar tipo, qualidade, duplicidade e vinculo ao checklist,
  > 
  > Para automatizar a classificacao documental e direcionar para revisao humana apenas os itens que exigirem validacao.
  > 
  > h3. Contexto e Regras de Negocio
  > 
  > # Etapas do Processamento Automatizado:
  > 
  > * Para cada arquivo contido em um lote documental recebido, o sistema executa: 1) Leitura OCR e extracao de texto; 2) Sugestao de tipo documental; 3) Avaliacao de qualidade/legibilidade; 4) Calculo de Hash SHA-256 e checagem de duplicidade; 5) Sugestao de vinculo a um item do checklist documental do caso.
  > 
  > # Regras de Transicao baseadas em Confianca da IA:
  > 
  > * Alta Confianca (>= Limiar de Alta Confianca) + Ato Operacional Reversivel: O sistema aplica a classificacao automaticamente e atualiza o status do documento para "Classificado pela IA", registrando o log com origem="ia".
  > * Confianca Media/Baixa (< Limiar de Alta Confianca) OU Tipo Documental Sensivel OU Divergência Detectada: O status do documento avanca para "Revisao humana pendente" e o arquivo entra na fila de validacao do Paralegal.
  > 
  > # Tratamento de Documento Ilegivel:
  > 
  > * Se a avaliacao de qualidade identificar arquivo corrompido, desfocado ou sem condicoes de leitura: O status do documento avanca para "Ilegivel" e o sistema gera automaticamente um registro de Pendencia com tipo="ilegivel".
  > 
  > # Tratamento de Documento Duplicado:
  > 
  > * O sistema compara o Hash SHA-256 do arquivo com os hashes ja armazenados no sistema. Se for detectada duplicidade, o sistema sugere o vinculo ao documento original existente. O Paralegal devera confirmar se a duplicidade afeta a conformidade do checklist.
  > 
  > # Contingência por Indisponibilidade do Servico de IA/OCR:
  > 
  > * Caso a API de OCR ou o modelo de IA esteja indisponivel ou retorne erro de timeout: O sistema define o status do documento como "Triagem automatica pendente" e envia o arquivo para a fila de validacao manual do Paralegal, sem interromper ou bloquear os demais fluxos da plataforma.
  > 
  > # Registro na Tabela SugestaoIA:
  > 
  > * Cada processamento de arquivo deve persistir um registro em SugestaoIA contendo: tipo_acao="classificacao_documental", conteudo_sugerido (JSON com tipo, qualidade e item de checklist), nivel_confianca (float de 0 a 1), status e timestamp.
  > 
  > h3. Criterios de Aceite (CA)
  > 
  > * CA01 [Execucao do Pipeline de OCR/IA]: Todo arquivo inserido em um lote deve passar pela esteira de extracao de texto OCR, geracao de hash SHA-256 e classificacao preditiva de IA.
  > * CA02 [Classificacao Automatica por Alta Confianca]: Documentos que atingirem a pontuacao de confianca configurada para alta confianca devem ser marcados como "Classificado pela IA" e ter seus metadados preenchidos sem necessidade de clique do operador.
  > * CA03 [Fila de Validacao para Baixa Confianca]: Documentos com pontuacao abaixo do limiar ou com divergência de dados devem receber o status "Revisao humana pendente" e aparecer na mesa de validacao split-screen do Paralegal.
  > * CA04 [Geracao de Pendencia para Ilegiveis]: Ao identificar um documento ilegivel, o sistema deve definir o status como "Ilegivel" e criar uma Pendencia associada com a mensagem "Documento ilegivel identificado pelo sistema".
  > * CA05 [Detecçao de Duplicidade por SHA-256]: Arquivos com Hash SHA-256 identico a um arquivo ja existente na base devem ser sinalizados com a tag "Duplicado" e ter a sugestao de vinculo apresentada ao validador humano.
  > * CA06 [Modo Contingência Off-line]: Na falha da conexao com a IA, o sistema nao deve travar a aplicacao; deve definir o status do arquivo como "Triagem automatica pendente" e liberar a edicao 100% manual.
  > 
  > ----

### [SCRUM-37] HMS-US028: Formar e aprovar dossiê como base para produção jurídica
- **Status**: `To Do`
- **Story Points**: 5
- **Descrição**:
  > h2. US05 - HMS-US028: Formar e aprovar dossie como base para producao juridica
  > 
  > h3. Identificacao
  > 
  > * Codigo no Backlog: SCRUM-37
  > * Codigo da US: HMS-US028
  > * Titulo: Formar e aprovar dossie como base para producao juridica
  > * Modulos PRD: Modulo de Producao Documental e Modulo de Motor Documental
  > 
  > h3. Historia de Usuario
  > 
  > Como paralegal ou advogado,
  > 
  > Quero revisar, organizar e homologar o Dossiê Documental do caso,
  > 
  > Para garantir que a produçao de pecas juridicas so seja liberada sobre uma base documental solida, validada e aprovada por um responsavel humano.
  > 
  > h3. Contexto e Regras de Negocio
  > 
  > # Gate de Liberaçao Sequencial para Produçao:
  > 
  > * O Dossiê Documental atua como o segundo gate sequencial e impeditivo do fluxo de trabalho. A liberação do inicio da elaboracao de pecas juridicas depende estritamente da aprovacao humana explicita deste dossie.
  > 
  > # Evolucao de Status do Dossiê:
  > 
  > * Em formação: Status inicial enquanto o checklist documental esta sendo preenchido e validado.
  > * Completo preliminar: Transicao automatica disparada pelo sistema no momento em que todos os documentos obrigatorios do checklist do caso forem validados com sucesso.
  > 
  > # Decisao Humana de Homologacao:
  > 
  > * O Paralegal ou Advogado analisa o conjunto de arquivos reunidos no Dossiê e registra uma das tres decisoes possiveis: Aprovado, Aprovado com exceçao ou Bloqueado.
  > 
  > # Trtatamento de Inconsistencias e Rejeicao:
  > 
  > * Se um documento essencial for rejeitado ou apresentar divergência durante a homologacao: O sistema retorna o Dossiê para o estagio de documentacao, bloqueia a liberação para producao e gera uma tarefa corretiva na fila do Paralegal.
  > 
  > # Impacto de Alteracao Documental Pós-Aprovacao:
  > 
  > * Se qualquer arquivo integrante do Dossiê for modificado, substituido ou excluido apos o inicio da producao juridica: O Dossiê altera automaticamente seu status para "Atualizado/substituido" e envia uma notificacao ativa para o Advogado autor da peca em elaboracao para avaliacao de impacto na tese.
  > 
  > h3. Criterios de Aceite (CA)
  > 
  > * CA01 [Bloqueio do Início de Peça]: O botao "Nova Peça Juridica" ou "Iniciar Elaboracao" deve permanecer desabilitado enquanto o Dossiê Documental do Caso nao estiver nos status "Aprovado" ou "Aprovado com excecao".
  > * CA02 [Transicao Automatica para Completo Preliminar]: Quando o ultimo item do checklist documental obrigatorio for validado, o status do Dossiê deve mudar de "Em formacao" para "Completo preliminar".
  > * CA03 [Decisao de Aprovacao Humana]: A interface do Dossiê deve disponibilizar os botoes de decisao "Aprovar Dossiê", "Aprovar com Excecao" e "Bloquear Dossiê". A escolha deve gravar o autor, a decisao e a data/hora no historico.
  > * CA04 [Retorno por Documento Incorreto]: Ao selecionar "Bloquear Dossiê", o sistema deve exigir o motivo da rejeicao, alterar o status do Dossiê para "Em formacao" e gerar uma tarefa pendente para o Paralegal ajustar os arquivos.
  > * CA05 [Alerta de Substituicao de Arquivo]: Caso um documento do Dossiê Aprovado seja substituido enquanto houver peca em rascunho/revisao, o Dossiê deve passar para "Atualizado/substituido" e um alerta de notificacao deve ser exibido no painel do Advogado produtor.
  > 
  > ----

### [SCRUM-65] HMS-US056: Configurar tipos de demanda e checklists por tipo de serviço
- **Status**: `To Do`
- **Story Points**: 3
- **Descrição**:
  > h2. US06 - HMS-US056: Configurar tipos de demanda e checklists por tipo de servico
  > 
  > h3. Identificacao
  > 
  > * Codigo no Backlog: SCRUM-65
  > * Codigo da US: HMS-US056
  > * Titulo: Configurar tipos de demanda e checklists por tipo de servico
  > * Modulos PRD: Modulo de Catalogo Juridico e Modulo de Producao Documental
  > 
  > h3. Historia de Usuario
  > 
  > Como administrador do sistema,
  > 
  > Quero configurar os tipos de demanda disponiveis e definir os modelos de checklist (ChecklistTemplate) por tipo de servico juridico,
  > 
  > Para que cada novo caso aberto receba automaticamente a esteira correta de documentos obrigatorios e opcionais.
  > 
  > h3. Contexto e Regras de Negocio
  > 
  > # Gestao de Tipos de Demanda:
  > 
  > * O Administrador pode criar, editar e desativar tipos de demanda juridica (ex: Acao Trabalhista Rito Ordinario, Concessao de Aposentadoria por Idade).
  > * Tipos de demanda marcados como "Desativados" deixam de ser exibidos imediatamente nos seletores de criacao de Intake e Caso.
  > 
  > # Parametrizacao do ChecklistTemplate:
  > 
  > * Para cada tipo de servico juridico, o Administrador configura a estrutura de ChecklistTemplate definindo: Nome do documento exigido, indicao de Obrigatoriedade (Obrigatorio de Merito ou Opcional) e a Ordem de exibicao no checklist.
  > 
  > # Vinculacao Automatica na Abertura do Caso:
  > 
  > * No momento em que um novo Caso e criado para determinado tipo de servico, o sistema busca o ChecklistTemplate ativo correspondente e instancia a entidade ChecklistCaso com todos os itens configurados.
  > 
  > # Trtatamento para Ausência de Template:
  > 
  > * Se nao houver um ChecklistTemplate cadastrado ou ativo para o tipo de servico selecionado, o sistema deve exibir um aviso informativo ao usuario ("Nenhum template de checklist configurado para este tipo de servico"), sem bloquear a abertura do Caso (permitindo a insercao manual de itens ad-hoc).
  > 
  > # Principio da Nao-Retroatividade:
  > 
  > * Alteracoes efetuadas em um ChecklistTemplate aplicam-se exclusivamente aos novos Casos criados apos a data da alteracao. Casos ja abertos preservam inalterada a estrutura de checklist que foi instanciada originalmente.
  > 
  > h3. Criterios de Aceite (CA)
  > 
  > * CA01 [Cadastro de Tipos de Demanda]: O Administrador deve conseguir cadastrar novos tipos de demanda associados a uma Area do Direito. O sistema deve impedir nomes duplicados dentro da mesma area.
  > * CA02 [Configuracao de itens do ChecklistTemplate]: Na tela de configuracao do template, o Administrador pode adicionar itens, definir a flag "Obrigatorio" (Sim/Nao) e reordenar a sequencia dos documentos.
  > * CA03 [Instanciacao Automatica no Caso]: Ao criar um Caso de determinado tipo de servico, o sistema deve copiar os itens do ChecklistTemplate ativo para a tabela ChecklistCaso do novo registro.
  > * CA04 [Aviso de Ausência de Template]: Se um Caso for criado com um tipo de servico sem template cadastrado, a tela do Caso deve apresentar o aviso "Sem template padrao. Adicione os itens manualmente" e permitir a abertura normal.
  > * CA05 [Preservacao de Casos Existentes]: Editar ou remover um item de um ChecklistTemplate nao pode alterar, excluir ou renomear os itens de checklists de casos criados anteriormente.
  > 
  > ----

### [SCRUM-27] HMS-US018: Abrir caso/serviço automaticamente após contratação
- **Status**: `To Do`
- **Story Points**: 3
- **Descrição**:
  > h2. US03 - HMS-US018: Abrir caso/servico automaticamente apos contratacao
  > 
  > h3. Identificacao
  > 
  > * Codigo no Backlog: SCRUM-27
  > * Codigo da US: HMS-US018
  > * Titulo: Abrir caso/servico automaticamente apos contratacao
  > * Modulos PRD: Modulo de Formalizacao, Modulo de Intake e Modulo de Producao Documental (Caso)
  > 
  > h3. Historia de Usuario
  > 
  > Como sistema e Advogado Principal,
  > 
  > Quero que o caso/servico seja instanciado automaticamente no Pipeline 2 imediatamente apos a contratacao,
  > 
  > Para iniciar a gestao operacional do serviço juridico com a equipe multidisciplinar e as permissoes devidamente registradas.
  > 
  > h3. Contexto e Regras de Negocio
  > 
  > # Instanciacao Automatica no Pipeline 2:
  > 
  > * Assim que o Intake atinge o status "Contratado — abrir caso/servico", o sistema deve criar automaticamente um novo registro de Caso no Pipeline 2.
  > * O status inicial do Caso no Pipeline 2 e definido como "Caso/servico aberto" (Status 1).
  > 
  > # Definicao da Equipe Multidisciplinar e Responsabilidade Formal:
  > 
  > * O criador/advogado responsavel vinculado a contratacao e definido obrigatoriamente como "Advogado Principal" (Detentor da Responsabilidade Formal Tecnica).
  > * O sistema deve permitir associar membros adicionais a equipe do caso, exigindo a selecao da funcao: Paralegal designado, Advogado auxiliar/junior ou Estagiario.
  > * Para cada membro adicionado, o Advogado Principal deve definir o nivel explicito de permissao: Visualizacao, Edicao ou Execucao de tarefas.
  > 
  > # Validacao de Parametros Iniciais do Servico:
  > 
  > * O Advogado Principal deve validar e confirmar a Area do Direito, o Tipo de Servico Juridico, a Prioridade Estrutural e o Responsavel Tecnico antes da primeira movimentacao do Caso no Kanban/Pipeline.
  > 
  > # Excecao para Criacao Manual de Caso:
  > 
  > * Em cenarios excepcionais em que um Caso precisa ser criado manualmente (sem passar pelo fluxo de Intake/Formalizacao), o sistema exige o preenchimento obrigatorio de um campo de texto contendo a justificativa da excecao.
  > 
  > h3. Criterios de Aceite (CA)
  > 
  > * CA01 [Gatilho de Criacao Automatica]: Ao receber o evento de contratacao do Intake, o sistema deve criar a entidade Caso vinculada a Pessoa e ao Intake de origem, definindo o status inicial como "Caso/servico aberto".
  > * CA02 [Advogado Principal Tecnico]: O usuario com perfil Advogado associado a contratacao deve ser atribuido automaticamente como Advogado Principal do Caso. Esta atribuicao nao pode ficar vazia.
  > * CA03 [Gestao da Equipe Multidisciplinar]: A interface de detalhes do Caso deve disponibilizar a secao "Equipe do Caso", permitindo adicionar usuarios internos com a selecao obrigatoria de funcao (Paralegal, Advogado Auxiliar, Estagiario) e escopo de permissao (Visualizacao, Edicao, Execucao).
  > * CA04 [Trava de Abertura Manual]: Ao tentar criar um Caso manualmente pela opcao "Novo Caso", o sistema deve exibir o campo obrigatorio "Justificativa de Excecao". Se o campo estiver em branco, o salvamento deve ser impedido.
  > * CA05 [Herdabilidade de Metadados]: O Caso criado deve herdar automaticamente a Area do Direito, o Tema e o historico de qualificacao definidos no Intake de origem.
  > 
  > ----

### [SCRUM-12] HMS-US003: Editar dados cadastrais de pessoa com auditoria
- **Status**: `To Do`
- **Story Points**: 3
- **Descrição**:
  > h2. US01 - HMS-US003: Editar dados cadastrais de pessoa com auditoria
  > 
  > h3. Identificacao
  > 
  > * Codigo no Backlog: SCRUM-12
  > * Codigo da US: HMS-US003
  > * Titulo: Editar dados cadastrais de pessoa com auditoria
  > * Modulo PRD: Modulo de Identidade (PRD - Modulo de Identidade)
  > 
  > h3. Historia de Usuario
  > 
  > Como atendente, supervisor ou administrador autorizado,
  > 
  > Quero editar os dados cadastrais de uma pessoa (cliente ou colaborador) ja registrada no sistema,
  > 
  > Para manter as informacoes atualizadas e garantir a rastreabilidade completa de todas as alteracoes via logs de auditoria imutaveis.
  > 
  > h3. Contexto e Regras de Negocio
  > 
  > # Escopo de Permissao por Perfil:
  > 
  > * Perfil Atendimento / Intake: Pode editar apenas campos de contato e endereco, especificamente: telefone principal, telefone secundario, e-mail, logradouro, numero, complemento, bairro, cidade, UF, CEP e observacoes cadastrais.
  > * Perfil Supervisor ou Administrador: Obrigatorio para alteracao de campos criticos: CPF/CNPJ, Nome Completo / Razao Social e registros de Consentimento LGPD.
  > 
  > # Controle de Duplicidade (CPF/CNPJ):
  > 
  > * Ao alterar o CPF/CNPJ de uma pessoa, o sistema deve executar a verificacao de duplicidade na base de dados (normalizando caracteres nao numericos).
  > * Se o documento informado ja pertencer a outra pessoa cadastrada, o sistema deve exibir um aviso de duplicidade em tela.
  > * A confirmacao de salvamento com documento duplicado exige a intervencao explicita de um perfil Supervisor ou Administrador, registrando a justificativa da operacao.
  > 
  > # Rastreabilidade e Auditoria Imutavel:
  > 
  > * Toda alteracao salva deve gerar compulsoriamente um registro na entidade LogAuditoria.
  > * O registro de auditoria deve armazenar: id_usuario, perfil_usuario, timestamp (com fuso horario TIMESTAMPTZ), entidade ("Pessoa"), id_entidade, campo_alterado, valor_anterior e valor_novo.
  > 
  > # Interface de Confirmacao:
  > 
  > * Antes de efetivar a gravacao dos dados, a interface deve exibir um modal de confirmacao contendo a mensagem: "Confirmar alteracoes? As mudancas serao registradas em auditoria."
  > 
  > h3. Criterios de Aceite (CA)
  > 
  > * CA01 [Matriz de Permissoes]: Se o usuario logado possuir o perfil "Atendimento/Intake" e tentar alterar os campos CPF, CNPJ ou Nome Completo, a interface deve manter esses campos bloqueados para edicao e o backend deve rejeitar a requisicao com codigo HTTP 403 (Forbidden).
  > * CA02 [Normalizacao e Busca de Duplicidade]: Ao alterar CPF ou CNPJ, o sistema deve remover pontuacoes e mascaras antes de consultar a base. Caso exista duplicidade, a interface deve exibir o alerta "Documento ja cadastrado para outra pessoa" e solicitar confirmacao de perfil autorizado.
  > * CA03 [Log de Auditoria Detalhado]: Para cada campo modificado no formulario, o sistema deve inserir uma linha correspondente no LogAuditoria registrando a diferenca exata entre o valor anterior e o novo valor.
  > * CA04 [Modal de Confirmacao]: O botao "Salvar Alteracoes" deve disparar a abertura do modal de confirmacao de auditoria. Caso o usuario cancele no modal, nenhuma alteracao deve ser persistida e o formulario deve manter os dados digitados.
  > * CA05 [Edicao de Endereco e Contato]: Alteracoes em telefone, e-mail e endereco realizadas por perfil autorizado devem ser salvas com sucesso e refletidas imediatamente na ficha da pessoa.
  > 
  > ----

### [SCRUM-130] HMS-US090: Congelar versão final para envio de assinatura ou protocolo
- **Status**: `To Do`
- **Story Points**: 8
- **Descrição**:
  > h2. US07 - HMS-US090: Congelar versao final para envio de assinatura ou protocolo
  > 
  > h3. Identificacao
  > 
  > * Codigo no Backlog: SCRUM-130
  > * Codigo da US: HMS-US090
  > * Titulo: Congelar versao final para envio de assinatura ou protocolo
  > * Modulos PRD: Modulo de Producao Documental (PRD - Modulo de Producao Documental)
  > 
  > h3. Historia de Usuario
  > 
  > Como advogado responsavel pela peca,
  > 
  > Quero congelar a versao aprovada de um documento juridico gerando um PDF estatico e imutavel com metadados de integridade,
  > 
  > Para garantir que o artefato enviado para assinatura eletronica ou protocolo judicial seja exatamente o texto homologado, impedindo alteracoes indevidas.
  > 
  > h3. Contexto e Regras de Negocio
  > 
  > # Geracao do Snapshot PDF Imutavel:
  > 
  > * Ao confirmar formalmente a aprovacao final de um documento ou peca juridica, o sistema deve compilar o texto aprovado e gerar um arquivo PDF estatico (Snapshot).
  > 
  > # Metadados de Integridade e Rastreabilidade:
  > 
  > * O sistema deve calcular o Hash SHA-256 do arquivo PDF gerado e gravar no banco de dados os seguintes metadados obrigatorios: hash_sha256, timestamp_congelamento (TIMESTAMPTZ), id_advogado_aprovador, id_template_modelo e numero_versao_congelada.
  > 
  > # Unico Artefato para Integracoes Externas:
  > 
  > * O PDF congelado passa a ser o unico e exclusivo artefato valido a ser transmitido para integracoes externas de assinatura eletronica (ex: Clicksign/DocuSign) ou sistemas de protocolo judicial (ex: PJe/e-SAJ). Nao e permitido enviar arquivos em formato editavel (DOCX, HTML ou RTF).
  > 
  > # Garantia de Imutabilidade e Fluxo de Correcao:
  > 
  > * Apos o congelamento, o texto do documento torna-se estritamente imutavel. Qualquer necessidade de alteracao ou correcao textual exige a execucao de um novo ciclo: reabrir edicao, gerar nova versao intermediaria, submeter a nova revisao e gerar um novo snapshot PDF congelado com seu proprio Hash SHA-256 independente.
  > 
  > h3. Criterios de Aceite (CA)
  > 
  > * CA01 [Geracao do PDF Snapshot]: Ao aprovar a versao final da peca, o sistema deve compilar o documento e salvar o arquivo PDF imutavel no repositório de documentos do caso.
  > * CA02 [Registro de SHA-256 e Metadados]: O sistema deve calcular a assinatura SHA-256 do arquivo PDF gerado e gravar o registro contendo hash_sha256, data/hora exata, ID do advogado aprovador e versao da peca.
  > * CA03 [Bloqueio de Edicao Pos-Congelamento]: A interface do editor de texto deve ser bloqueada para edicao apos o congelamento, exibindo o status "Documento Congelado para Envio/Protocolo".
  > * CA04 [Restricao de Envio Externo]: As rotinas de envio para assinatura eletronica ou protocolo devem aceitar unicamente a URL/Stream do arquivo PDF congelado validado pelo Hash SHA-256.
  > * CA05 [Ciclo de Nova Versao por Correcao]: Caso o advogado solicite alteracao em documento ja congelado, o sistema deve exigir o registro do motivo e criar uma nova versao da peca (ex: v2.0), mantendo a v1.0 congelada e preservada no historico.

### [SCRUM-36] HMS-US027: Solicitar e aprovar exceção documental
- **Status**: `To Do`
- **Story Points**: 5
- **Descrição**:
  > Como paralegal ou advogado, quero solicitar exceção documental quando não for possível resolver uma pendência e for necessário avançar o caso, para que o avanço seja rastreável com justificativa, impacto, solicitante e aprovador distintos.
  > 
  > *Critérios de Aceitação:*
  > 
  > * CA01 - O formulário de exceção exige: tipo (Dispensa · Aceite provisório · Substituição · Juntada posterior · Equivalência documental · Outro), justificativa (mín. 30 caracteres), impacto e entidade vinculada.
  > * CA02 - O sistema encaminha a exceção para aprovação por perfil autorizado diferente do solicitante; a tentativa de auto-aprovação é bloqueada com mensagem "Você não pode aprovar a própria exceção".
  > * CA03 - Exceção aprovada: checklist avança para "Aprovado com exceção"; a ressalva é visível e vinculada ao checklist, dossiê e caso.
  > * CA04 - Exceção rejeitada: checklist permanece bloqueado; usuário deve resolver a pendência normalmente ou solicitar nova exceção.
  > * CA05 - Exceção temporária exige data de validade; o sistema revoga automaticamente ao atingir a data e bloqueia o avanço dependente.
  > * CA06 - Log completo gerado com: solicitante, aprovador, tipo, justificativa, impacto, status e data/hora.

---

## Backlog

### [SCRUM-45] HMS-US036: Registrar andamentos processuais do caso
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 2
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 5
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
- **Status**: `To Do`
- **Story Points**: 5
- **Descrição**:
  > Sem descrição

### [SCRUM-120] HMS-US084 — Módulo Financeiro — Versão Incipiente do MVP
- **Status**: `To Do`
- **Story Points**: 3
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
- **Status**: `To Do`
- **Story Points**: 0
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

