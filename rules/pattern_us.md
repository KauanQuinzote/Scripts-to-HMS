# 📜 Guia e Padrão de Estruturação de User Stories (US)

Este documento define o padrão oficial para elaboração, estruturação e reescrita de **Histórias de Usuário (US)** no projeto HMS, garantindo alinhamento rigoroso com os **Product Requirement Documents (PRDs)** disponíveis no repositório.

---

## 🎯 1. Estrutura Padrão da User Story

Toda User Story (US) deve seguir estritamente o modelo de seções abaixo:

```markdown
### Identificação
- **Código no Backlog:** [EX: SCRUM-27]
- **Código da US:** [EX: HMS-US018]
- **Título:** [Título claro e objetivo da funcionalidade]
- **Módulos PRD:** [Lista dos módulos do PRD impactados, ex: Módulo de Formalização, Módulo de Intake, Módulo de Produção Documental (Caso)]

---

### História de Usuário
- **Como** [Perfil/Ator/Papel do Usuário ou Sistema],
- **Quero** [Ação/Funcionalidade que se deseja realizar],
- **Para** [Benefício de negócio ou valor entregue].

---

### Contexto e Regras de Negócio
[Detalhamento técnico e de negócio estruturado em tópicos com títulos claros. Deve cobrir:]
- **Gatilhos de Entrada e Transições de Status:** O que dispara a ação e quais status mudam.
- **Atores, Perfis e Responsabilidades:** Quem executa, quem é responsável técnico e níveis de permissão.
- **Validações e Parâmetros:** Campos obrigatórios, travas de segurança e precondições.
- **Exceções e Cenários Alternativos:** Fluxos manuais ou contingências e justificativas necessárias.
- **Herdabilidade e Metadados:** Quais dados são propagados automaticamente de módulos anteriores.

---

### Critérios de Aceite (CA)
- **CA01 [Nome Curto do Gatilho/Funcionalidade]:** [Descrição objetiva, acionável e testável da regra].
- **CA02 [Nome Curto da Regra/Atribuição]:** [Descrição objetiva, acionável e testável da regra].
- **CA03 [Nome Curto da Interface/Permissão]:** [Descrição objetiva, acionável e testável da regra].
- **CA04 [Nome Curto de Trava/Exceção]:** [Descrição objetiva, acionável e testável da regra].
- **CA05 [Nome Curto de Propagação/Metadados]:** [Descrição objetiva, acionável e testável da regra].
```

---

## 🔍 2. Diretrizes para Análise e Reescrita baseadas nos PRDs

Ao criar ou reescrever uma US a partir dos PRDs disponíveis na pasta `prds/`, deve-se seguir o fluxo de trabalho abaixo:

### Passo 1: Localização dos PRDs Relevantes
1. Identifique no repositório os arquivos do módulo correspondente em `prds/*.txt` (ou `.pdf`). Exemplo:
   - `Módulo de Intake-200826-175721.txt`
   - `Módulo de Formalização-200826-175822.txt`
   - `Módulo de Produção Documental-200826-172839.txt`
   - `Módulo de Identidade-200826-172633.txt`
   - `Módulo de Catálogo Jurídico-200826-172804.txt`
   - `Módulo de Agendamento-200826-174249.txt`
   - `Módulo de Comunicação-200826-175750.txt`
   - `Módulo de Consulta-200826-183547.txt`
   - `Módulo de Motor Documental-200826-174827.txt`

### Passo 2: Extração de Regras e Validação de Requisitos
1. **Verificar Atores e Papéis:** Validar os nomes oficiais dos papéis (ex: *Advogado Principal*, *Paralegal*, *Estagiário*).
2. **Mapear Transições de Status:** Identificar os nomes exatos de status de origem e destino (ex: do status Intake *"Contratado — abrir caso/serviço"* para o status de Caso *"Caso/serviço aberto"*).
3. **Mapear Herdabilidade de Dados:** Confirmar quais campos devem ser copiados de uma entidade para outra (ex: Área do Direito, Tema, Qualificação).
4. **Identificar Trava de Exceção:** Garantir que fluxos manuais contenham os campos obrigatórios de justificativa ou aprovação exigidos no PRD.

### Passo 3: Formatatação e Redação dos Critérios de Aceite (CA)
- Cada CA deve possuir um prefixo identificador sequencial: `CA01`, `CA02`, `CA03`...
- Seguir a sintaxe `CAxx [Nome Curto em Colchetes]: Texto claro e testável`.
- Os CAs devem ser autossuficientes para permitir a criação de testes automatizados e validações no QA.

---

## 📌 3. Exemplo Prático de Aplicação

### Identificação
- **Código no Backlog:** SCRUM-27
- **Código da US:** HMS-US018
- **Título:** Abrir caso/serviço automaticamente após contratação
- **Módulos PRD:** Módulo de Formalização, Módulo de Intake e Módulo de Produção Documental (Caso)

### História de Usuário
- **Como** sistema e Advogado Principal,
- **Quero** que o caso/serviço seja instanciado automaticamente no Pipeline 2 imediatamente após a contratação,
- **Para** iniciar a gestão operacional do serviço jurídico com a equipe multidisciplinar e as permissões devidamente registradas.

### Contexto e Regras de Negócio
- **Instanciação Automática no Pipeline 2:** Assim que o Intake atinge o status *"Contratado — abrir caso/serviço"*, o sistema deve criar automaticamente um novo registro de Caso no Pipeline 2. O status inicial do Caso no Pipeline 2 é definido como *"Caso/serviço aberto"* (Status 1).
- **Definição da Equipe Multidisciplinar e Responsabilidade Formal:** O criador/advogado responsável vinculado à contratação é definido obrigatoriamente como *"Advogado Principal"* (Detentor da Responsabilidade Formal Técnica). O sistema deve permitir associar membros adicionais à equipe do caso, exigindo a seleção da função: *Paralegal designado*, *Advogado auxiliar/júnior* ou *Estagiário*. Para cada membro adicionado, o Advogado Principal deve definir o nível explícito de permissão: *Visualização*, *Edição* ou *Execução de tarefas*.
- **Validação de Parâmetros Iniciais do Serviço:** O Advogado Principal deve validar e confirmar a Área do Direito, o Tipo de Serviço Jurídico, a Prioridade Estrutural e o Responsável Técnico antes da primeira movimentação do Caso no Kanban/Pipeline.
- **Exceção para Criação Manual de Caso:** Em cenários excepcionais em que um Caso precisa ser criado manualmente (sem passar pelo fluxo de Intake/Formalização), o sistema exige o preenchimento obrigatório de um campo de texto contendo a justificativa da exceção.

### Critérios de Aceite (CA)
- **CA01 [Gatilho de Criação Automática]:** Ao receber o evento de contratação do Intake, o sistema deve criar a entidade Caso vinculada à Pessoa e ao Intake de origem, definindo o status inicial como *"Caso/serviço aberto"*.
- **CA02 [Advogado Principal Técnico]:** O usuário com perfil Advogado associado à contratação deve ser atribuído automaticamente como Advogado Principal do Caso. Esta atribuição não pode ficar vazia.
- **CA03 [Gestão da Equipe Multidisciplinar]:** A interface de detalhes do Caso deve disponibilizar a seção *"Equipe do Caso"*, permitindo adicionar usuários internos com a seleção obrigatória de função (*Paralegal*, *Advogado Auxiliar*, *Estagiário*) e escopo de permissão (*Visualização*, *Edição*, *Execução*).
- **CA04 [Trava de Abertura Manual]:** Ao tentar criar um Caso manualmente pela opção *"Novo Caso"*, o sistema deve exibir o campo obrigatório *"Justificativa de Exceção"*. Se o campo estiver em branco, o salvamento deve ser impedido.
- **CA05 [Herdabilidade de Metadados]:** O Caso criado deve herdar automaticamente a Área do Direito, o Tema e o histórico de qualificação definidos no Intake de origem.
