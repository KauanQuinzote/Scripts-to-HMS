# 📋 Histórias de Usuário (US) Reescritas no Padrão HMS

Documento compilado com a reescrita das Histórias de Usuário de acordo com as regras estabelecidas no arquivo [rules/pattern_us.md](file:///home/kauan/Documentos/HMS/script-python/rules/pattern_us.md) e fundamentadas nos Product Requirement Documents (PRDs) do projeto HMS.

---

## 1. HMS-US017: Controlar formalização e registrar data de contratação

### Identificação
- **Código no Backlog:** SCRUM-26
- **Código da US:** HMS-US017
- **Título:** Controlar formalização e registrar data de contratação
- **Módulos PRD:** Módulo de Formalização e Módulo de Intake

---

### História de Usuário
- **Como** paralegal ou atendente,
- **Quero** registrar o andamento da formalização contratual e concluir o rito de contratação,
- **Para** avançar o intake para o status "Contratado — abrir caso/serviço" e registrar a data oficial de contratação para alimentação dos indicadores de desempenho.

---

### Contexto e Regras de Negócio
- **Painel de Acompanhamento da Formalização:** A tela de formalização deve listar todos os documentos contratuais associados ao intake (ex: Contrato de Honorários, Procuração, Declaração de Hipossuficiência). Cada documento possui um status individual obrigatório: Pendente, Recebido ou Assinado.
- **Registro do Tipo de Assinatura:** O sistema deve permitir registrar o tipo de assinatura utilizado para cada documento: Física (impressa e assinada manualmente), Digital (certificado digital ICP-Brasil) ou Eletrônica (plataforma de assinatura via token/link).
- **Regra de Elegibilidade para Conclusão:** A conclusão da formalização exige obrigatoriamente que pelo menos um documento contratual principal esteja com o status "Recebido" ou "Assinado". Se todos os documentos estiverem com status "Pendente", o botão de conclusão deve permanecer desabilitado.
- **Data de Contratação e Indicadores:** Ao concluir a formalização com sucesso, a `data_contratacao` deve ser gravada automaticamente pelo servidor com a data/hora atual (TIMESTAMPTZ). Esse campo é o gatilho oficial para o cálculo do Indicador MVP #4 (Tempo médio de qualificação e contratação).
- **Transição de Status e Gatilho para o Caso:** Na conclusão bem-sucedida, o Intake avança automaticamente para o status "Contratado — abrir caso/serviço" e envia a notificação de evento para instanciação do Caso no Pipeline 2.
- **Encerramento por Insucesso:** Se a formalização for interrompida ou recusada pelo cliente, o usuário deve acionar a ação de encerramento do intake, sendo obrigatório selecionar um motivo válido do catálogo regulamentar.

---

### Critérios de Aceite (CA)
- **CA01 [Lista de Documentos Contratuais]:** A interface de formalização deve exibir a tabela de documentos exigidos mostrando o nome do arquivo, status individual (Pendente, Recebido, Assinado) e o tipo de assinatura selecionado.
- **CA02 [Validação para Conclusão]:** O sistema deve bloquear a tentativa de conclusão da formalização caso nenhum documento esteja marcado como "Recebido" ou "Assinado", exibindo a mensagem "É necessário ter ao menos um documento recebido ou assinado para concluir a contratação".
- **CA03 [Gravação Automática da Data]:** Ao clicar em "Concluir Contratação", o backend deve definir `data_contratacao = CURRENT_TIMESTAMP` e atualizar o status do Intake para "Contratado — abrir caso/serviço".
- **CA04 [Integração com Pipeline 2]:** A alteração de status do Intake para "Contratado — abrir caso/serviço" deve emitir um evento interno solicitando a abertura do Caso correspondente no Pipeline 2.
- **CA05 [Encerramento sem Contratação]:** Caso o usuário selecione "Encerrar Formalização", o sistema deve exigir a escolha do motivo antes de alterar o status para "Encerrado sem contratação".

---

## 2. HMS-US026: Gerar pendências documentais e acionar mensageria assistida

### Identificação
- **Código no Backlog:** SCRUM-35
- **Código da US:** HMS-US026
- **Título:** Gerar pendências documentais e acionar mensageria assistida
- **Módulos PRD:** Módulo de Motor Documental, Módulo de Comunicação e Módulo de Formalização

---

### História de Usuário
- **Como** sistema e paralegal,
- **Quero** gerar automaticamente pendências documentais e elaborar rascunhos de mensagens assistidas padronizadas,
- **Para** que o cliente seja notificado com agilidade sobre documentos faltantes ou inadequados com validação humana prévia ao envio.

---

### Contexto e Regras de Negócio
- **Geração de Pendências por Inadequação:** O sistema gera uma entidade `Pendencia` automaticamente quando um documento é identificado como faltante, ilegível, incompleto, duplicado ou não correspondente ao item do checklist. Os campos obrigatórios incluem tipo, motivo, responsável, documento relacionado e vínculo ao `ChecklistCaso`.
- **Elaboração de Mensagem Assistida:** O sistema prepara uma `MensagemAssistida` contendo texto objetivo especificando os documentos pendentes e as instruções de envio. A mensagem assume inicialmente o status "Aguardando aprovação".
- **Trava de Segurança e Aprovação Humana:** Comunicações de status jurídico, solicitações formais e orientações possuem envio automático bloqueado por padrão; exigem validação explícita do advogado ou paralegal responsável antes de serem disparadas ao cliente.
- **Contador de Pendências no Checklist:** A interface do checklist do caso deve apresentar um contador visual com o total de pendências ativas associadas a cada item documental.
- **Tratamento de Erros da IA:** Se a pendência for gerada indevidamente por falha na classificação da IA, o paralegal deve cancelar a pendência, registrando uma entrada na tabela `ErroIA` com justificativa e acionando comunicação corretiva caso o cliente já tenha sido notificado.

---

### Critérios de Aceite (CA)
- **CA01 [Geração Automática de Pendência]:** Ao identificar um documento faltante, ilegível ou inadequado, o sistema deve registrar a entidade `Pendencia` vinculada ao item do checklist correspondente.
- **CA02 [Rascunho de Mensagem Assistida]:** O sistema deve compor automaticamente a `MensagemAssistida` associada à pendência com o status "Aguardando aprovação".
- **CA03 [Trava de Envio sem Validação]:** O envio de mensagens de pendência ao cliente deve permanecer bloqueado até que o operador humano revise e autorize o disparo.
- **CA04 [Contador de Pendências no Checklist]:** O checklist do caso deve exibir a contagem de pendências ativas vinculadas a cada documento exigido.
- **CA05 [Cancelamento de Pendência por Erro de IA]:** Ao cancelar uma pendência incorreta gerada por IA, o sistema deve exigir o registro em `ErroIA` e sinalizar a necessidade de mensagem corretiva ao cliente se aplicável.

---

## 3. HMS-US027: Solicitar e aprovar exceção documental (dispensa e aceite provisório)

### Identificação
- **Código no Backlog:** SCRUM-36
- **Código da US:** HMS-US027
- **Título:** Solicitar e aprovar exceção documental (dispensa e aceite provisório)
- **Módulos PRD:** Módulo de Motor Documental, Módulo de Formalização e Módulo de Produção Documental

---

### História de Usuário
- **Como** paralegal ou advogado,
- **Quero** solicitar e homologar exceções documentais (dispensa definitiva ou aceite provisório com prazo determinado),
- **Para** viabilizar o avanço operacional do caso sem comprometer as regras de governança e a gestão de riscos jurídicos.

---

### Contexto e Regras de Negócio
- **Modalidades de Exceção Documental:**
  1. *Dispensa Definitiva:* Isenta compulsoriamente a apresentação de um documento não essencial.
  2. *Aceite Provisório:* Autoriza a progressão temporária do fluxo mediante a definição obrigatória de uma data limite para o envio do documento definitivo.
- **Alçada de Decisão e Governança:** A solicitação é iniciada pelo Paralegal e depende da aprovação formal de um usuário com perfil *Advogado Principal* ou *Supervisor*.
- **Rastreabilidade e Log Imutável:** A solicitação exige justificativa de negócio detalhada. Toda aprovação ou rejeição persiste um registro em `ExcecaoDocumental` e gera log no `LogAuditoria`.
- **Monitoramento e Expiração de Aceite Provisório:** Se o prazo do aceite provisório expirar sem a entrega do documento validado, o status da exceção muda para "Expirado", gerando um alerta crítico no painel do Advogado Principal e bloqueando o gate de aprovação final da peça jurídica.

---

### Critérios de Aceite (CA)
- **CA01 [Solicitação de Exceção Documental]:** A interface deve disponibilizar o formulário de exceção exigindo a escolha da modalidade (Dispensa ou Aceite Provisório) e a justificativa técnica.
- **CA02 [Obrigatoriedade de Prazo para Aceite Provisório]:** Quando a modalidade selecionada for "Aceite Provisório", o sistema deve exigir o preenchimento da data limite para saneamento da pendência.
- **CA03 [Controle de Alçada por Perfil]:** Apenas usuários autenticados com o perfil Advogado Principal ou Supervisor possuem acesso aos botões de aprovação e rejeição de exceções.
- **CA04 [Registro de Auditoria de Exceção]:** Toda decisão referente a uma exceção deve gravar os metadados (autor, decisão, justificativa e timestamp) em `ExcecaoDocumental` e `LogAuditoria`.
- **CA05 [Trava por Expiração de Aceite Provisório]:** Aceites provisórios vencidos devem mudar o status para "Expirado", notificar o responsável e bloquear a aprovação final de peças do caso.

---

## 4. HMS-US039: Registrar comunicação na Central com visibilidade controlada

### Identificação
- **Código no Backlog:** SCRUM-48
- **Código da US:** HMS-US039
- **Título:** Registrar comunicação na Central com visibilidade controlada
- **Módulos PRD:** Módulo de Comunicação e Módulo de Identidade

---

### História de Usuário
- **Como** atendente, paralegal ou advogado,
- **Quero** registrar interações de comunicação na Central controlando a visibilidade de cada registro,
- **Para** manter a memória operacional do atendimento preservando informações internas e segredos estratégicos do escritório.

---

### Contexto e Regras de Negócio
- **Campos Mínimos da Comunicação:** O formulário de registro exige a seleção da Pessoa, Direção (Ativa ou Passiva), Canal (WhatsApp, Telefone, E-mail, Presencial), Motivo e Resumo descritivo.
- **Controle de Ação Requerida e Prazos:** Ao marcar o toggle "Requer ação", o campo "Prazo de ação" torna-se obrigatório (exibido com fundo destacado em dourado) e a comunicação passa a ser listada no filtro dedicado "Requer ação · N".
- **Política Restritiva de Visibilidade (Default Interno):** As flags `visivel_cliente` e `visivel_terceiro` são marcadas por padrão como `FALSE`.
- **Liberação para Acesso Externo:** Tornar a comunicação visível para o cliente ou terceiro exige um comando explícito de um usuário autorizado, que deve confirmar que o texto não contém pareceres internos, notas de estratégia ou dados sigilosos de terceiros.
- **Identificação de Atendimentos Automatizados:** Comunicações provenientes do assistente virtual (WhatsApp) recebem o badge "Auto" e registram a identificação do agente automatizado ou do atendente responsável pelo transbordo.

---

### Critérios de Aceite (CA)
- **CA01 [Formulário de Registro de Comunicação]:** O formulário deve validar o preenchimento obrigatório dos campos Pessoa, Direção, Canal, Motivo e Resumo antes de salvar a comunicação.
- **CA02 [Obrigatoriedade de Prazo para Ação Requerida]:** Ao ativar o toggle "Requer ação", a interface deve exigir o preenchimento do campo "Prazo de ação".
- **CA03 [Visibilidade Interna por Padrão]:** Todo registro de comunicação deve ser gravado com `visivel_cliente = FALSE` e `visivel_terceiro = FALSE` como estado inicial padrão.
- **CA04 [Validação para Liberação Externa]:** A liberação de visibilidade externa exige confirmação explícita no modal e grava no log o responsável, a data/hora e o escopo concedido.
- **CA05 [Tag Visual para Assistente Virtual]:** Interações registradas automaticamente pelo assistente virtual devem ser apresentadas na timeline com a tag visual "Auto".

---

## 5. HMS-US028: Seleção de teses do catálogo e inicialização da minuta da peça jurídica

### Identificação
- **Código no Backlog:** SCRUM-37
- **Código da US:** HMS-US028
- **Título:** Seleção de teses do catálogo e inicialização da minuta da peça jurídica
- **Módulos PRD:** Módulo de Catálogo Jurídico e Módulo de Produção Documental

---

### História de Usuário
- **Como** advogado responsável pela peça jurídica,
- **Quero** selecionar teses jurídicas cadastradas no Catálogo e inicializar a minuta estruturada,
- **Para** acelerar a redação documental garantindo o alinhamento com os padrões técnicos e teses pré-aprovadas pelo escritório.

---

### Contexto e Regras de Negócio
- **Gate de Liberação por Dossiê Homologado:** A ação de criar uma nova peça jurídica permanece estritamente desabilitada até que o Dossiê Documental do Caso atinja os status "Aprovado" ou "Aprovado com exceção".
- **Pesquisa e Filtro de Teses:** O editor disponibiliza busca no Catálogo Jurídico com filtros por Área do Direito, Tema e palavras-chave.
- **Importação de Blocos Fundamentados:** A seleção de uma tese insere no editor a estrutura completa contendo a tese jurídica, fundamentação legal, precedentes/jurisprudência e os pedidos associados.
- **Suporte Automatizado de IA na Minuta:** O advogado pode solicitar a compilação inicial da minuta por IA, que unifica os dados da Ficha de Atendimento e as teses selecionadas em um rascunho inicial.
- **Registro do Início da Produção:** A geração da minuta salva `data_inicio_producao = CURRENT_TIMESTAMP` (que alimenta o Indicador MVP #10) e atualiza o status do Caso para "Em produção jurídica".

---

### Critérios de Aceite (CA)
- **CA01 [Gate do Dossiê Documental]:** O botão de criação de minuta jurídica deve permanecer desabilitado enquanto o Dossiê Documental do Caso não estiver nos status "Aprovado" ou "Aprovado com exceção".
- **CA02 [Buscador do Catálogo Jurídico]:** A interface deve permitir pesquisar teses ativas no Catálogo Jurídico e selecionar múltiplas teses para compor a peça.
- **CA03 [Inserção Automática de Fundamentação]:** A seleção de uma tese deve importar automaticamente os blocos de fundamentação legal e pedidos no corpo do editor de texto.
- **CA04 [Transição para Em Produção Jurídica]:** Ao salvar o rascunho inicial da peça, o sistema deve criar a entidade `Peca` com status "Em elaboração" e alterar o status do Caso para "Em produção jurídica".
- **CA05 [Gravação da Data de Início de Produção]:** O backend deve registrar a `data_inicio_producao` no momento da criação da minuta para alimentação do cálculo de SLA de produção.

---

## 6. HMS-US029: Edição, versionamento e revisão assistida por IA da peça processual

### Identificação
- **Código no Backlog:** SCRUM-38
- **Código da US:** HMS-US029
- **Título:** Edição, versionamento e revisão assistida por IA da peça processual
- **Módulos PRD:** Módulo de Produção Documental e Módulo de Motor Documental

---

### História de Usuário
- **Como** advogado ou supervisor,
- **Quero** editar a peça processual, registrar versões imutáveis e realizar a revisão assistida por alertas de IA,
- **Para** assegurar a excelência técnica da minuta, preservar o histórico completo de alterações e fundamentar a decisão final de aprovação.

---

### Contexto e Regras de Negócio
- **Editor com Versionamento Imutável:** Durante a redação, o sistema permite acionar a gravação de versão, inserindo um registro na tabela `VersaoPeca` contendo número da versão, conteúdo integral, identificação do autor, timestamp e Hash SHA-256.
- **Imutabilidade da Tabela de Versões:** A tabela `VersaoPeca` é imutável (`append-only`). O sistema bloqueia tecnicamente qualquer instrução de alteração (`UPDATE`) ou deleção (`DELETE`) de versões salvas.
- **Painel de Alertas e Revisão por IA:** O editor de revisão analisa o texto em relação ao Dossiê do Caso e apresenta em um painel lateral alertas sobre potenciais omissões, incoerências fáticas, ausência de documentos citados ou contradições jurídicas.
- **Decisão Humana de Revisão:** O revisor registra o parecer em uma de três alternativas: *Aprovar*, *Solicitar Ajustes* (retornando o documento ao produtor) ou *Bloquear*. A opção "Solicitar Ajustes" habilita novamente o editor para o advogado autor.
- **Auditoria de Decisões sobre IA:** As sugestões de IA aceitas ou rejeitadas pelo revisor são gravadas na tabela `SugestaoIA` para auditoria e calibragem contínua dos modelos.

---

### Critérios de Aceite (CA)
- **CA01 [Geração de Snapshot de Versão com SHA-256]:** Cada acionamento de "Salvar Versão" deve registrar uma linha em `VersaoPeca` contendo o texto completo e a assinatura Hash SHA-256.
- **CA02 [Imutabilidade do Histórico de Versões]:** O sistema deve rejeitar qualquer tentativa de modificação ou exclusão de versões gravadas anteriormente no histórico.
- **CA03 [Exibição de Alertas de IA na Revisão]:** A tela de revisão deve apresentar o painel lateral com os alertas identificados pela IA sem alterar o texto de forma automática.
- **CA04 [Fluxo de Retorno para Ajustes]:** Ao selecionar a decisão "Solicitar Ajustes", o sistema deve alterar o status da peça para "Ajustes solicitados", salvar os comentários do revisor e liberar o editor para o produtor.
- **CA05 [Registro em SugestãoIA]:** A validação humana sobre os apontamentos da IA deve persistir o status e as justificativas na entidade `SugestaoIA`.

---

## 7. HMS-US048: Portal do Cliente: upload seguro de documentos e saneamento de pendências

### Identificação
- **Código no Backlog:** SCRUM-57
- **Código da US:** HMS-US048
- **Título:** Portal do Cliente: upload seguro de documentos e saneamento de pendências
- **Módulos PRD:** Módulo de Comunicação, Módulo de Identidade e Módulo de Motor Documental

---

### História de Usuário
- **Como** cliente final,
- **Quero** acessar o Portal do Cliente para realizar o upload seguro dos documentos solicitados e acompanhar a resolução de pendências,
- **Para** sanar as pendências do meu atendimento com comodidade, segurança e sem necessidade de deslocamento ao escritório.

---

### Contexto e Regras de Negócio
- **Acesso Autenticado e Visão Simplificada:** O cliente acessa o portal mediante autenticação segura (token OTP por WhatsApp/SMS). A interface apresenta apenas os dados de acompanhamento simplificado e as pendências documentais ativas direcionadas a ele.
- **Listagem de Pendências Documentais:** Exibe claramente quais documentos estão pendentes, o motivo da solicitação e as instruções simples para envio.
- **Upload Seguro e Validação de Formatos:** Permite o envio de arquivos de imagem (PNG, JPG, JPEG) e PDF. O sistema valida extensão e tamanho máximo permitido no frontend e backend antes da recepção, aplicando criptografia no envio e no armazenamento.
- **Processamento Automático e Mudança de Status:** Ao concluir o upload de um arquivo referente a uma pendência, o status da pendência altera para "Em análise" e o documento é enviado para a fila de leitura e triagem por OCR/IA.
- **Confirmação e Protocolo:** O cliente recebe uma confirmação imediata em tela com número de protocolo do envio e uma notificação de recibo via WhatsApp.

---

### Critérios de Aceite (CA)
- **CA01 [Autenticação OTP e Visão Restrita]:** O portal deve autenticar o cliente via OTP e limitar a visualização estritamente às suas próprias pendências documentais e status simplificado.
- **CA02 [Validação de Upload de Arquivos]:** O upload deve aceitar exclusivamente formatos de imagem e PDF dentro do limite de tamanho configurado, exibindo alerta descritivo caso o arquivo seja inválido.
- **CA03 [Vínculo à Pendência e Status Em Análise]:** O envio do documento deve associar o arquivo à `Pendencia` correspondente e atualizar o status da pendência para "Em análise".
- **CA04 [Encaminhamento para Fila de OCR/IA]:** Todo arquivo recebido via Portal do Cliente deve ser automaticamente inserido no lote documental para triagem por OCR/IA e notificação da equipe interna.
- **CA05 [Emissão de Protocolo de Recebimento]:** Após a conclusão do upload, o portal deve exibir a tela de confirmação contendo o código de protocolo e a data/hora do envio.
