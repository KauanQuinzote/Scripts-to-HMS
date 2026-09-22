# 📋 Jira Stories Extractor & Backlog Reporter

Conjunto de scripts em Python para integração com a API Agil/REST do Jira, permitindo extrair e gerar relatórios em Markdown das Histórias de Usuário (US) de Sprints e do Backlog com filtros totalmente customizáveis.

---

## 🚀 Requisitos e Configuração

### 1. Pré-requisitos
- Python 3.8 ou superior
- Dependências instaladas (`requests`, `python-dotenv`)

```bash
# Caso precise instalar as dependências no ambiente python local/venv:
pip install requests python-dotenv
```

### 2. Configuração do `.env`
Crie ou edite o arquivo `.env` na raiz do diretório com as seguintes variáveis de acesso ao Jira:

```env
JIRA_BASE_URL=https://seu-dominio.atlassian.net
JIRA_EMAIL=seu-email@dominio.com
JIRA_API_TOKEN=seu_api_token_jira
JIRA_PROJECT_KEY=CHAVE_DO_PROJETO
JIRA_BOARD_ID=1
```

> **Dica**: O Token de API pode ser gerado no Jira em: **Account Settings > Security > Create and manage API tokens**.

## 📁 Organização dos Arquivos de Saída (`results/`)

Todos os scripts salvam automaticamente seus relatórios e arquivos de saída dentro do diretório `results/(nome_do_script)/`:

- **`get_backlog_stories.py`** $\rightarrow$ Salva relatórios em `results/get_backlog_stories/` (ex: `results/get_backlog_stories/backlog_stories_report.md`).
- **`get_jira_stories.py`** $\rightarrow$ Salva extrações em `results/get_jira_stories/` (`results/get_jira_stories/jira_stories.json` e `results/get_jira_stories/jira_stories_report.md`).
- **`update_jira_stories.py`** $\rightarrow$ Salva relatórios de execução em `results/update_jira_stories/` (`results/update_jira_stories/update_report.json`).

---

## 📌 Script: `get_backlog_stories.py`

Este script é focado em buscar edições do **Backlog** do Jira e exportar relatórios customizados em **Markdown**.

### 🛠️ Parâmetros Disponíveis (`--help`)

| Parâmetro | Tipo | Descrição |
| :--- | :--- | :--- |
| `--titles-only` | Flag | Exporta apenas a Chave e o Título das US (sem descrição ou detalhes). |
| `--no-description` | Flag | Oculta o bloco de descrição, mantendo os detalhes/campos selecionados. |
| `--fields` | Lista | Define campos adicionais a exibir. Opções: `status`, `points`, `assignee`, `priority`, `parent`, `labels`, `components`, `all`. (Padrão: `status points`). |
| `--status` | Texto | Filtra por status específicos separados por vírgula (ex: `"To Do,Refinement"`). |
| `--priority` | Texto | Filtra por prioridade (ex: `"High,Medium"`). |
| `--component` | Texto | Filtra por componente do Jira. |
| `--label` | Texto | Filtra por label. |
| `--epic` | Texto | Filtra por chave do Epic ou Parent. |
| `--jql` | Texto | Permite adicionar uma condição JQL customizada. |
| `--issue-type` | Texto | Tipo de edição Jira a buscar (Padrão: `"Story"`). |
| `-o`, `--output` | Caminho | Nome/Caminho do arquivo Markdown de saída (Padrão em `results/get_backlog_stories/`). |

---

## 💡 Principais Comandos e Exemplos

### 1. Puxar apenas os Títulos do Backlog (Resumido)
Ideal para ter uma visualização rápida e limpa de todas as histórias pendentes no backlog:
```bash
python3 get_backlog_stories.py --titles-only -o titulos_backlog.md
```
*(Salvo em `results/get_backlog_stories/titulos_backlog.md`)*

### 2. Puxar Títulos e Detalhes principais (sem Descrição)
```bash
python3 get_backlog_stories.py --no-description --fields status points assignee priority -o backlog_resumido.md
```

### 3. Puxar Histórias Completas com Descrição e Todos os Campos
```bash
python3 get_backlog_stories.py --fields all -o backlog_completo.md
```

### 4. Filtrar por Status Específico
```bash
python3 get_backlog_stories.py --status "To Do,Refinement" --fields status points -o backlog_todo.md
```

### 5. Filtrar por Epic / Parent
```bash
python3 get_backlog_stories.py --epic "PROJ-123" -o backlog_epic_123.md
```

### 6. Filtrar por Consulta JQL Customizada
```bash
python3 get_backlog_stories.py --jql "updated >= -7d" -o historias_atualizadas_recentemente.md
```

---

## 📦 Script Adicional: `get_jira_stories.py`

Script complementar que extrai histórias organizadas por **Sprints** (Ativas, Futuras e Concluídas) e pelo **Backlog**, exportando na pasta `results/get_jira_stories/` os arquivos `jira_stories.json` e `jira_stories_report.md`.

```bash
python3 get_jira_stories.py
```

---

## ✏️ Script de Atualização: `update_jira_stories.py`

Script em Python para atualizar Histórias de Usuário (US) existentes no Jira via REST API v3. Permite atualizar títulos, descrições (com suporte a Markdown $\rightarrow$ ADF nativo), story points, status (transições), responsáveis, prioridades, labels e componentes. Salva o relatório de execução em `results/update_jira_stories/update_report.json`.

### 🛠️ Parâmetros Disponíveis (`--help`)

| Parâmetro | Tipo | Descrição |
| :--- | :--- | :--- |
| `--key` | Texto | Chave da US a ser atualizada (ex: `SCRUM-27`). |
| `--summary`, `--title` | Texto | Novo título / resumo da US. |
| `--description` | Texto | Nova descrição da US (convertida para ADF do Jira). |
| `--points`, `--story-points` | Número | Novo valor de Story Points. |
| `--status` | Texto | Novo status (ex: `"In Progress"`, `"Done"`, `"To Do"`). |
| `--assignee` | Texto | E-mail ou ID do novo responsável (ou `"none"` para desatribuir). |
| `--priority` | Texto | Nova prioridade (ex: `"High"`, `"Medium"`). |
| `--labels` | Texto | Novas labels separadas por vírgula. |
| `--components` | Texto | Novos componentes separados por vírgula. |
| `--file`, `-f` | Caminho | Caminho para arquivo JSON contendo lote de atualizações. |
| `--dry-run` | Flag | Simula as alterações sem enviá-las ao Jira. |
| `-y`, `--yes` | Flag | Confirma execução sem solicitar confirmação manual. |

### 💡 Exemplos de Uso

#### 1. Simular alteração individual (Dry-Run)
```bash
python3 update_jira_stories.py --key SCRUM-27 --points 5 --status "In Progress" --dry-run
```

#### 2. Atualizar título, story points e status de uma US
```bash
python3 update_jira_stories.py --key SCRUM-27 --points 8 --status "In Progress" -y
```

#### 3. Atualizar responsável e prioridade
```bash
python3 update_jira_stories.py --key SCRUM-45 --assignee "dev@empresa.com" --priority "High" -y
```

#### 4. Atualizações em lote (Batch via JSON)
Crie um arquivo `updates.json`:
```json
[
  {
    "key": "SCRUM-27",
    "story_points": 5,
    "status": "In Progress"
  },
  {
    "key": "SCRUM-45",
    "story_points": 3,
    "priority": "High"
  }
]
```

E execute:
```bash
python3 update_jira_stories.py --file updates.json --dry-run
python3 update_jira_stories.py --file updates.json -y
```

