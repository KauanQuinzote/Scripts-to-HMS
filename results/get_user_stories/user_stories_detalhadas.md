# Especificacao Detalhada de Historias de Usuario (US) - HMS

Documento elaborado pela Gestao de Produtos (Senior Product Owner) para detalhamento tecnico das Historias de Usuario (US) do ecossistema HMS. O objetivo deste documento e eliminar ambiguidades, estabelecer criterios de aceite (CA) testaveis e garantir o alinhamento com os Documentos de Requisitos de Produto (PRDs).

---

## US01 - HMS-US003: Editar dados cadastrais de pessoa com auditoria

### Identificacao
- Codigo no Backlog: SCRUM-12
- Codigo da US: HMS-US003
- Titulo: Editar dados cadastrais de pessoa com auditoria
- Modulo PRD: Modulo de Identidade (PRD - Modulo de Identidade)

### Historia de Usuario
Como atendente, supervisor ou administrador autorizado,
Quero editar os dados cadastrais de uma pessoa (cliente ou colaborador) ja registrada no sistema,
Para manter as informacoes atualizadas e garantir a rastreabilidade completa de todas as alteracoes via logs de auditoria imutaveis.

### Contexto e Regras de Negocio
1. Escopo de Permissao por Perfil:
   - Perfil Atendimento / Intake: Pode editar apenas campos de contato e endereco, especificamente: telefone principal, telefone secundario, e-mail, logradouro, numero, complemento, bairro, cidade, UF, CEP e observacoes cadastrais.
   - Perfil Supervisor ou Administrador: Obrigatorio para alteracao de campos criticos: CPF/CNPJ, Nome Completo / Razao Social e registros de Consentimento LGPD.
2. Controle de Duplicidade (CPF/CNPJ):
   - Ao alterar o CPF/CNPJ de uma pessoa, o sistema deve executar a verificacao de duplicidade na base de dados (normalizando caracteres nao numericos).
   - Se o documento informado ja pertencer a outra pessoa cadastrada, o sistema deve exibir um aviso de duplicidade em tela.
   - A confirmacao de salvamento com documento duplicado exige a intervencao explicita de um perfil Supervisor ou Administrador, registrando a justificativa da operacao.
3. Rastreabilidade e Auditoria Imutavel:
   - Toda alteracao salva deve gerar compulsoriamente um registro na entidade LogAuditoria.
   - O registro de auditoria deve armazenar: id_usuario, perfil_usuario, timestamp (com fuso horario TIMESTAMPTZ), entidade ("Pessoa"), id_entidade, campo_alterado, valor_anterior e valor_novo.
4. Interface de Confirmacao:
   - Antes de efetivar a gravacao dos dados, a interface deve exibir um modal de confirmacao contendo a mensagem: "Confirmar alteracoes? As mudancas serao registradas em auditoria."

### Criterios de Aceite (CA)
- CA01 [Matriz de Permissoes]: Se o usuario logado possuir o perfil "Atendimento/Intake" e tentar alterar os campos CPF, CNPJ ou Nome Completo, a interface deve manter esses campos bloqueados para edicao e o backend deve rejeitar a requisicao com codigo HTTP 403 (Forbidden).
- CA02 [Normalizacao e Busca de Duplicidade]: Ao alterar CPF ou CNPJ, o sistema deve remover pontuacoes e mascaras antes de consultar a base. Caso exista duplicidade, a interface deve exibir o alerta "Documento ja cadastrado para outra pessoa" e solicitar confirmacao de perfil autorizado.
- CA03 [Log de Auditoria Detalhado]: Para cada campo modificado no formulario, o sistema deve inserir uma linha correspondente no LogAuditoria registrando a diferenca exata entre o valor anterior e o novo valor.
- CA04 [Modal de Confirmacao]: O botao "Salvar Alteracoes" deve disparar a abertura do modal de confirmacao de auditoria. Caso o usuario cancele no modal, nenhuma alteracao deve ser persistida e o formulario deve manter os dados digitados.
- CA05 [Edicao de Endereco e Contato]: Alteracoes em telefone, e-mail e endereco realizadas por perfil autorizado devem ser salvas com sucesso e refletidas imediatamente na ficha da pessoa.

---

## US02 - HMS-US017: Controlar formalizacao e registrar data de contratacao

### Identificacao
- Codigo no Backlog: SCRUM-26
- Codigo da US: HMS-US017
- Titulo: Controlar formalizacao e registrar data de contratacao
- Modulos PRD: Modulo de Formalizacao e Modulo de Intake

### Historia de Usuario
Como paralegal ou atendente,
Quero registrar o andamento da formalizacao contratual e concluir o rito de contratacao,
Para avançar o intake para o status "Contratado" e registrar a data oficial de contratacao para alimentacao dos indicadores de desempenho.

### Contexto e Regras de Negocio
1. Painel de Acompanhamento da Formalizacao:
   - A tela de formalizacao deve listar todos os documentos contratuais associados ao intake (ex: Contrato de Honorarios, Procuracao, Declaracao de Hipossuficiencia).
   - Cada documento possui um status individual obrigatorio: Pendente, Recebido ou Assinado.
2. Registro do Tipo de Assinatura:
   - O sistema deve permitir registrar o tipo de assinatura utilizado para cada documento: Fisica (documento impresso e assinado manualmente), Digital (certificado digital ICP-Brasil) ou Eletronica (plataforma de assinatura via token/link).
3. Regra de Elegibilidade para Conclusao:
   - A conclusao da formalizacao exige obrigatoriamente que pelo menos um documento contratual principal esteja com o status "Recebido" ou "Assinado".
   - Se todos os documentos estiverem com status "Pendente", o botao de conclusao deve permanecer desabilitado.
4. Data de Contratacao e Indicadores:
   - Ao concluir a formalizacao com sucesso, a data_contratacao deve ser gravada automaticamente pelo servidor com a data/hora atual (TIMESTAMPTZ).
   - Esse campo e o gatilho oficial para o calculo do Indicador MVP numero 4 (Tempo medio de qualificacao e contratacao).
5. Transicao de Status e Gatilho para o Caso:
   - Na conclusao bem-sucedida, o Intake avança automaticamente para o status "Contratado — abrir caso/servico" e envia a notificacao de evento para instanciacao do Caso no Pipeline 2.
6. Encerramento por Insucesso:
   - Se a formalizacao for interrompida ou recusada pelo cliente, o usuario deve acionar a acao de encerramento do intake, sendo obrigatorio selecionar um motivo valido do catalogo regulamentar.

### Criterios de Aceite (CA)
- CA01 [Lista de Documentos Contratuais]: A interface de formalizacao deve exibir a tabela de documentos exigidos mostrando o nome do arquivo, status individual (Pendente, Recebido, Assinado) e o tipo de assinatura selecionado.
- CA02 [Validaçao para Conclusao]: O sistema deve bloquear a tentativa de conclusao da formalizacao caso nenhum documento esteja marcado como "Recebido" ou "Assinado", exibindo a mensagem "E necessario ter ao menos um documento recebido ou assinado para concluir a contratacao".
- CA03 [Gravacao Automatica da Data]: Ao clicar em "Concluir Contratacao", o backend deve definir data_contratacao = CURRENT_TIMESTAMP e atualizar o status do Intake para "Contratado — abrir caso/servico".
- CA04 [Integracao com Pipeline 2]: A alteracao de status do Intake para "Contratado" deve emitir um evento interno síncrono/assíncrono solicitando a abertura do Caso correspondente no Pipeline 2.
- CA05 [Encerramento sem Contratacao]: Caso o usuario selecione "Encerrar Formalizacao", o sistema deve exigir a escolha do motivo (ex: Desistência do Cliente, Inviabilidade Financeira) antes de alterar o status para "Encerrado sem contratacao".

---

## US03 - HMS-US018: Abrir caso/servico automaticamente apos contratacao

### Identificacao
- Codigo no Backlog: SCRUM-27
- Codigo da US: HMS-US018
- Titulo: Abrir caso/servico automaticamente apos contratacao
- Modulos PRD: Modulo de Formalizacao, Modulo de Intake e Modulo de Producao Documental (Caso)

### Historia de Usuario
Como sistema e Advogado Principal,
Quero que o caso/servico seja instanciado automaticamente no Pipeline 2 imediatamente apos a contratacao,
Para iniciar a gestao operacional do serviço juridico com a equipe multidisciplinar e as permissoes devidamente registradas.

### Contexto e Regras de Negocio
1. Instanciacao Automatica no Pipeline 2:
   - Assim que o Intake atinge o status "Contratado — abrir caso/servico", o sistema deve criar automaticamente um novo registro de Caso no Pipeline 2.
   - O status inicial do Caso no Pipeline 2 e definido como "Caso/servico aberto" (Status 1).
2. Definicao da Equipe Multidisciplinar e Responsabilidade Formal:
   - O criador/advogado responsavel vinculado a contratacao e definido obrigatoriamente como "Advogado Principal" (Detentor da Responsabilidade Formal Tecnica).
   - O sistema deve permitir associar membros adicionais a equipe do caso, exigindo a selecao da funcao: Paralegal designado, Advogado auxiliar/junior ou Estagiario.
   - Para cada membro adicionado, o Advogado Principal deve definir o nivel explicito de permissao: Visualizacao, Edicao ou Execucao de tarefas.
3. Validacao de Parametros Iniciais do Servico:
   - O Advogado Principal deve validar e confirmar a Area do Direito, o Tipo de Servico Juridico, a Prioridade Estrutural e o Responsavel Tecnico antes da primeira movimentacao do Caso no Kanban/Pipeline.
4. Excecao para Criacao Manual de Caso:
   - Em cenarios excepcionais em que um Caso precisa ser criado manualmente (sem passar pelo fluxo de Intake/Formalizacao), o sistema exige o preenchimento obrigatorio de um campo de texto contendo a justificativa da excecao.

### Criterios de Aceite (CA)
- CA01 [Gatilho de Criacao Automatica]: Ao receber o evento de contratacao do Intake, o sistema deve criar a entidade Caso vinculada a Pessoa e ao Intake de origem, definindo o status inicial como "Caso/servico aberto".
- CA02 [Advogado Principal Tecnico]: O usuario com perfil Advogado associado a contratacao deve ser atribuido automaticamente como Advogado Principal do Caso. Esta atribuicao nao pode ficar vazia.
- CA03 [Gestao da Equipe Multidisciplinar]: A interface de detalhes do Caso deve disponibilizar a secao "Equipe do Caso", permitindo adicionar usuarios internos com a selecao obrigatoria de funcao (Paralegal, Advogado Auxiliar, Estagiario) e escopo de permissao (Visualizacao, Edicao, Execucao).
- CA04 [Trava de Abertura Manual]: Ao tentar criar um Caso manualmente pela opcao "Novo Caso", o sistema deve exibir o campo obrigatorio "Justificativa de Excecao". Se o campo estiver em branco, o salvamento deve ser impedido.
- CA05 [Herdabilidade de Metadados]: O Caso criado deve herdar automaticamente a Area do Direito, o Tema e o historico de qualificacao definidos no Intake de origem.

---

## US04 - HMS-US021: Processar documento com IA/OCR e controlar status individual

### Identificacao
- Codigo no Backlog: SCRUM-30
- Codigo da US: HMS-US021
- Titulo: Processar documento com IA/OCR e controlar status individual
- Modulo PRD: Modulo de Motor Documental (PRD - Modulo de Motor Documental)

### Historia de Usuario
Como sistema e Paralegal,
Quero processar cada arquivo recebido em um lote via OCR e IA para identificar tipo, qualidade, duplicidade e vinculo ao checklist,
Para automatizar a classificacao documental e direcionar para revisao humana apenas os itens que exigirem validacao.

### Contexto e Regras de Negocio
1. Etapas do Processamento Automatizado:
   - Para cada arquivo contido em um lote documental recebido, o sistema executa: 1) Leitura OCR e extracao de texto; 2) Sugestao de tipo documental; 3) Avaliacao de qualidade/legibilidade; 4) Calculo de Hash SHA-256 e checagem de duplicidade; 5) Sugestao de vinculo a um item do checklist documental do caso.
2. Regras de Transicao baseadas em Confianca da IA:
   - Alta Confianca (>= Limiar de Alta Confianca) + Ato Operacional Reversivel: O sistema aplica a classificacao automaticamente e atualiza o status do documento para "Classificado pela IA", registrando o log com origem="ia".
   - Confianca Media/Baixa (< Limiar de Alta Confianca) OU Tipo Documental Sensivel OU Divergência Detectada: O status do documento avanca para "Revisao humana pendente" e o arquivo entra na fila de validacao do Paralegal.
3. Tratamento de Documento Ilegivel:
   - Se a avaliacao de qualidade identificar arquivo corrompido, desfocado ou sem condicoes de leitura: O status do documento avanca para "Ilegivel" e o sistema gera automaticamente um registro de Pendencia com tipo="ilegivel".
4. Tratamento de Documento Duplicado:
   - O sistema compara o Hash SHA-256 do arquivo com os hashes ja armazenados no sistema. Se for detectada duplicidade, o sistema sugere o vinculo ao documento original existente. O Paralegal devera confirmar se a duplicidade afeta a conformidade do checklist.
5. Contingência por Indisponibilidade do Servico de IA/OCR:
   - Caso a API de OCR ou o modelo de IA esteja indisponivel ou retorne erro de timeout: O sistema define o status do documento como "Triagem automatica pendente" e envia o arquivo para a fila de validacao manual do Paralegal, sem interromper ou bloquear os demais fluxos da plataforma.
6. Registro na Tabela SugestaoIA:
   - Cada processamento de arquivo deve persistir um registro em SugestaoIA contendo: tipo_acao="classificacao_documental", conteudo_sugerido (JSON com tipo, qualidade e item de checklist), nivel_confianca (float de 0 a 1), status e timestamp.

### Criterios de Aceite (CA)
- CA01 [Execucao do Pipeline de OCR/IA]: Todo arquivo inserido em um lote deve passar pela esteira de extracao de texto OCR, geracao de hash SHA-256 e classificacao preditiva de IA.
- CA02 [Classificacao Automatica por Alta Confianca]: Documentos que atingirem a pontuacao de confianca configurada para alta confianca devem ser marcados como "Classificado pela IA" e ter seus metadados preenchidos sem necessidade de clique do operador.
- CA03 [Fila de Validacao para Baixa Confianca]: Documentos com pontuacao abaixo do limiar ou com divergência de dados devem receber o status "Revisao humana pendente" e aparecer na mesa de validacao split-screen do Paralegal.
- CA04 [Geracao de Pendencia para Ilegiveis]: Ao identificar um documento ilegivel, o sistema deve definir o status como "Ilegivel" e criar uma Pendencia associada com a mensagem "Documento ilegivel identificado pelo sistema".
- CA05 [Detecçao de Duplicidade por SHA-256]: Arquivos com Hash SHA-256 identico a um arquivo ja existente na base devem ser sinalizados com a tag "Duplicado" e ter a sugestao de vinculo apresentada ao validador humano.
- CA06 [Modo Contingência Off-line]: Na falha da conexao com a IA, o sistema nao deve travar a aplicacao; deve definir o status do arquivo como "Triagem automatica pendente" e liberar a edicao 100% manual.

---

## US05 - HMS-US028: Formar e aprovar dossie como base para producao juridica

### Identificacao
- Codigo no Backlog: SCRUM-37
- Codigo da US: HMS-US028
- Titulo: Formar e aprovar dossie como base para producao juridica
- Modulos PRD: Modulo de Producao Documental e Modulo de Motor Documental

### Historia de Usuario
Como paralegal ou advogado,
Quero revisar, organizar e homologar o Dossiê Documental do caso,
Para garantir que a produçao de pecas juridicas so seja liberada sobre uma base documental solida, validada e aprovada por um responsavel humano.

### Contexto e Regras de Negocio
1. Gate de Liberaçao Sequencial para Produçao:
   - O Dossiê Documental atua como o segundo gate sequencial e impeditivo do fluxo de trabalho. A liberação do inicio da elaboracao de pecas juridicas depende estritamente da aprovacao humana explicita deste dossie.
2. Evolucao de Status do Dossiê:
   - Em formação: Status inicial enquanto o checklist documental esta sendo preenchido e validado.
   - Completo preliminar: Transicao automatica disparada pelo sistema no momento em que todos os documentos obrigatorios do checklist do caso forem validados com sucesso.
3. Decisao Humana de Homologacao:
   - O Paralegal ou Advogado analisa o conjunto de arquivos reunidos no Dossiê e registra uma das tres decisoes possiveis: Aprovado, Aprovado com exceçao ou Bloqueado.
4. Trtatamento de Inconsistencias e Rejeicao:
   - Se um documento essencial for rejeitado ou apresentar divergência durante a homologacao: O sistema retorna o Dossiê para o estagio de documentacao, bloqueia a liberação para producao e gera uma tarefa corretiva na fila do Paralegal.
5. Impacto de Alteracao Documental Pós-Aprovacao:
   - Se qualquer arquivo integrante do Dossiê for modificado, substituido ou excluido apos o inicio da producao juridica: O Dossiê altera automaticamente seu status para "Atualizado/substituido" e envia uma notificacao ativa para o Advogado autor da peca em elaboracao para avaliacao de impacto na tese.

### Criterios de Aceite (CA)
- CA01 [Bloqueio do Início de Peça]: O botao "Nova Peça Juridica" ou "Iniciar Elaboracao" deve permanecer desabilitado enquanto o Dossiê Documental do Caso nao estiver nos status "Aprovado" ou "Aprovado com excecao".
- CA02 [Transicao Automatica para Completo Preliminar]: Quando o ultimo item do checklist documental obrigatorio for validado, o status do Dossiê deve mudar de "Em formacao" para "Completo preliminar".
- CA03 [Decisao de Aprovacao Humana]: A interface do Dossiê deve disponibilizar os botoes de decisao "Aprovar Dossiê", "Aprovar com Excecao" e "Bloquear Dossiê". A escolha deve gravar o autor, a decisao e a data/hora no historico.
- CA04 [Retorno por Documento Incorreto]: Ao selecionar "Bloquear Dossiê", o sistema deve exigir o motivo da rejeicao, alterar o status do Dossiê para "Em formacao" e gerar uma tarefa pendente para o Paralegal ajustar os arquivos.
- CA05 [Alerta de Substituicao de Arquivo]: Caso um documento do Dossiê Aprovado seja substituido enquanto houver peca em rascunho/revisao, o Dossiê deve passar para "Atualizado/substituido" e um alerta de notificacao deve ser exibido no painel do Advogado produtor.

---

## US06 - HMS-US056: Configurar tipos de demanda e checklists por tipo de servico

### Identificacao
- Codigo no Backlog: SCRUM-65
- Codigo da US: HMS-US056
- Titulo: Configurar tipos de demanda e checklists por tipo de servico
- Modulos PRD: Modulo de Catalogo Juridico e Modulo de Producao Documental

### Historia de Usuario
Como administrador do sistema,
Quero configurar os tipos de demanda disponiveis e definir os modelos de checklist (ChecklistTemplate) por tipo de servico juridico,
Para que cada novo caso aberto receba automaticamente a esteira correta de documentos obrigatorios e opcionais.

### Contexto e Regras de Negocio
1. Gestao de Tipos de Demanda:
   - O Administrador pode criar, editar e desativar tipos de demanda juridica (ex: Acao Trabalhista Rito Ordinario, Concessao de Aposentadoria por Idade).
   - Tipos de demanda marcados como "Desativados" deixam de ser exibidos imediatamente nos seletores de criacao de Intake e Caso.
2. Parametrizacao do ChecklistTemplate:
   - Para cada tipo de servico juridico, o Administrador configura a estrutura de ChecklistTemplate definindo: Nome do documento exigido, indicao de Obrigatoriedade (Obrigatorio de Merito ou Opcional) e a Ordem de exibicao no checklist.
3. Vinculacao Automatica na Abertura do Caso:
   - No momento em que um novo Caso e criado para determinado tipo de servico, o sistema busca o ChecklistTemplate ativo correspondente e instancia a entidade ChecklistCaso com todos os itens configurados.
4. Trtatamento para Ausência de Template:
   - Se nao houver um ChecklistTemplate cadastrado ou ativo para o tipo de servico selecionado, o sistema deve exibir um aviso informativo ao usuario ("Nenhum template de checklist configurado para este tipo de servico"), sem bloquear a abertura do Caso (permitindo a insercao manual de itens ad-hoc).
5. Principio da Nao-Retroatividade:
   - Alteracoes efetuadas em um ChecklistTemplate aplicam-se exclusivamente aos novos Casos criados apos a data da alteracao. Casos ja abertos preservam inalterada a estrutura de checklist que foi instanciada originalmente.

### Criterios de Aceite (CA)
- CA01 [Cadastro de Tipos de Demanda]: O Administrador deve conseguir cadastrar novos tipos de demanda associados a uma Area do Direito. O sistema deve impedir nomes duplicados dentro da mesma area.
- CA02 [Configuracao de itens do ChecklistTemplate]: Na tela de configuracao do template, o Administrador pode adicionar itens, definir a flag "Obrigatorio" (Sim/Nao) e reordenar a sequencia dos documentos.
- CA03 [Instanciacao Automatica no Caso]: Ao criar um Caso de determinado tipo de servico, o sistema deve copiar os itens do ChecklistTemplate ativo para a tabela ChecklistCaso do novo registro.
- CA04 [Aviso de Ausência de Template]: Se um Caso for criado com um tipo de servico sem template cadastrado, a tela do Caso deve apresentar o aviso "Sem template padrao. Adicione os itens manualmente" e permitir a abertura normal.
- CA05 [Preservacao de Casos Existentes]: Editar ou remover um item de um ChecklistTemplate nao pode alterar, excluir ou renomear os itens de checklists de casos criados anteriormente.

---

## US07 - HMS-US090: Congelar versao final para envio de assinatura ou protocolo

### Identificacao
- Codigo no Backlog: SCRUM-130
- Codigo da US: HMS-US090
- Titulo: Congelar versao final para envio de assinatura ou protocolo
- Modulos PRD: Modulo de Producao Documental (PRD - Modulo de Producao Documental)

### Historia de Usuario
Como advogado responsavel pela peca,
Quero congelar a versao aprovada de um documento juridico gerando um PDF estatico e imutavel com metadados de integridade,
Para garantir que o artefato enviado para assinatura eletronica ou protocolo judicial seja exatamente o texto homologado, impedindo alteracoes indevidas.

### Contexto e Regras de Negocio
1. Geracao do Snapshot PDF Imutavel:
   - Ao confirmar formalmente a aprovacao final de um documento ou peca juridica, o sistema deve compilar o texto aprovado e gerar um arquivo PDF estatico (Snapshot).
2. Metadados de Integridade e Rastreabilidade:
   - O sistema deve calcular o Hash SHA-256 do arquivo PDF gerado e gravar no banco de dados os seguintes metadados obrigatorios: hash_sha256, timestamp_congelamento (TIMESTAMPTZ), id_advogado_aprovador, id_template_modelo e numero_versao_congelada.
3. Unico Artefato para Integracoes Externas:
   - O PDF congelado passa a ser o unico e exclusivo artefato valido a ser transmitido para integracoes externas de assinatura eletronica (ex: Clicksign/DocuSign) ou sistemas de protocolo judicial (ex: PJe/e-SAJ). Nao e permitido enviar arquivos em formato editavel (DOCX, HTML ou RTF).
4. Garantia de Imutabilidade e Fluxo de Correcao:
   - Apos o congelamento, o texto do documento torna-se estritamente imutavel. Qualquer necessidade de alteracao ou correcao textual exige a execucao de um novo ciclo: reabrir edicao, gerar nova versao intermediaria, submeter a nova revisao e gerar um novo snapshot PDF congelado com seu proprio Hash SHA-256 independente.

### Criterios de Aceite (CA)
- CA01 [Geracao do PDF Snapshot]: Ao aprovar a versao final da peca, o sistema deve compilar o documento e salvar o arquivo PDF imutavel no repositório de documentos do caso.
- CA02 [Registro de SHA-256 e Metadados]: O sistema deve calcular a assinatura SHA-256 do arquivo PDF gerado e gravar o registro contendo hash_sha256, data/hora exata, ID do advogado aprovador e versao da peca.
- CA03 [Bloqueio de Edicao Pos-Congelamento]: A interface do editor de texto deve ser bloqueada para edicao apos o congelamento, exibindo o status "Documento Congelado para Envio/Protocolo".
- CA04 [Restricao de Envio Externo]: As rotinas de envio para assinatura eletronica ou protocolo devem aceitar unicamente a URL/Stream do arquivo PDF congelado validado pelo Hash SHA-256.
- CA05 [Ciclo de Nova Versao por Correcao]: Caso o advogado solicite alteracao em documento ja congelado, o sistema deve exigir o registro do motivo e criar uma nova versao da peca (ex: v2.0), mantendo a v1.0 congelada e preservada no historico.

