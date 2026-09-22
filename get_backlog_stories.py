#!/usr/bin/env python3
import os
import sys
import json
import base64
import argparse
import requests
from dotenv import load_dotenv

# Try loading env from multiple locations
possible_env_paths = [
    os.path.join(os.getcwd(), '.env'),
    os.path.join(os.getcwd(), '.venv', '.env'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '.venv', '.env')
]

env_loaded = False
for path in possible_env_paths:
    if os.path.exists(path):
        load_dotenv(path)
        env_loaded = True
        break

# Retrieve environment variables
JIRA_BASE_URL = (os.getenv("JIRA_BASE_URL") or os.getenv("JIRA_URL", "")).strip().rstrip('/')
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "").strip()
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "").strip()
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "").strip()
JIRA_BOARD_ID = os.getenv("JIRA_BOARD_ID", "").strip()

def setup_session():
    if not JIRA_BASE_URL or not JIRA_EMAIL or not JIRA_API_TOKEN:
        print("Erro: JIRA_BASE_URL, JIRA_EMAIL e JIRA_API_TOKEN devem ser configurados no arquivo .env ou variáveis de ambiente.")
        sys.exit(1)
    
    session = requests.Session()
    auth_str = f"{JIRA_EMAIL}:{JIRA_API_TOKEN}"
    b64_auth = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
    session.headers.update({
        "Authorization": f"Basic {b64_auth}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    })
    return session

def get_request(session, url, params=None):
    """Helper para realizar requisições HTTP com tratamento de erro."""
    response = session.get(url, params=params)
    if response.status_code != 200:
        print(f"Erro ao requisitar {url}: {response.status_code} - {response.text}")
        response.raise_for_status()
    return response.json()

def adf_to_text(adf):
    """Converte recursivamente Atlassian Document Format (ADF) para texto plano."""
    if not adf:
        return ""
    if isinstance(adf, str):
        return adf
    text_parts = []
    if isinstance(adf, dict):
        if adf.get("type") == "text":
            return adf.get("text", "")
        node_type = adf.get("type")
        if node_type in ["paragraph", "heading", "listItem"]:
            text_parts.append("\n")
        
        for key, val in adf.items():
            if key != "type":
                text_parts.append(adf_to_text(val))
    elif isinstance(adf, list):
        for item in adf:
            text_parts.append(adf_to_text(item))
    return "".join(text_parts).strip()

def find_story_points_field(session):
    """Descobre dynamicamente a chave do campo Story Points."""
    try:
        fields = get_request(session, f"{JIRA_BASE_URL}/rest/api/3/field")
        for field in fields:
            name = field.get("name", "").lower()
            if "story point" in name or "story_point" in name:
                return field.get("id")
    except Exception:
        pass
    return "customfield_10016"

def find_board_id(session, project_key):
    """Encontra o primeiro board associado ao project_key."""
    try:
        boards_data = get_request(session, f"{JIRA_BASE_URL}/rest/agile/1.0/board", params={"projectKeyOrId": project_key})
        values = boards_data.get("values", [])
        if values:
            return values[0].get("id")
    except Exception as e:
        print(f"Erro ao procurar board: {e}")
    return None

def build_jql(args):
    """Constrói a query JQL com base nas flags de filtro."""
    jql_clauses = []

    # Tipo de edição (ex: Story)
    issue_type = args.issue_type or os.getenv("JIRA_ISSUE_TYPES", "Story")
    types_list = [f"'{t.strip()}'" for t in issue_type.split(",")]
    jql_clauses.append(f"issuetype in ({','.join(types_list)})")

    # Status
    if args.status:
        statuses = [f"'{s.strip()}'" for s in args.status.split(",")]
        jql_clauses.append(f"status in ({','.join(statuses)})")

    # Prioridade
    if args.priority:
        priorities = [f"'{p.strip()}'" for p in args.priority.split(",")]
        jql_clauses.append(f"priority in ({','.join(priorities)})")

    # Componente
    if args.component:
        components = [f"'{c.strip()}'" for c in args.component.split(",")]
        jql_clauses.append(f"component in ({','.join(components)})")

    # Labels
    if args.label:
        labels = [f"'{l.strip()}'" for l in args.label.split(",")]
        jql_clauses.append(f"labels in ({','.join(labels)})")

    # Epic
    if args.epic:
        jql_clauses.append(f'("Epic Link" = "{args.epic}" OR parent = "{args.epic}")')

    # JQL customizada adicional
    if args.jql:
        jql_clauses.append(f"({args.jql})")

    return " AND ".join(jql_clauses)

def fetch_backlog_issues(session, board_id, jql, story_points_field):
    """Busca todas as edições do backlog respeitando a JQL e paginação."""
    issues = []
    start_at = 0
    max_results = 50
    fields_to_request = [
        "summary", "description", story_points_field, "status",
        "priority", "assignee", "labels", "components", "parent", "epic"
    ]
    
    while True:
        url = f"{JIRA_BASE_URL}/rest/agile/1.0/board/{board_id}/backlog"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "jql": jql,
            "fields": ",".join(fields_to_request)
        }
        data = get_request(session, url, params=params)
        values = data.get("issues", [])
        issues.extend(values)
        if start_at + len(values) >= data.get("total", 0) or len(values) < max_results:
            break
        start_at += len(values)
    return issues

def parse_issue(issue, story_points_field):
    """Extrai informações relevantes de um issue do Jira."""
    fields = issue.get("fields", {})
    description = fields.get("description")
    desc_text = adf_to_text(description) if description else "Sem descrição"
    
    story_points = fields.get(story_points_field)
    try:
        story_points = float(story_points) if story_points is not None else 0.0
        if story_points.is_integer():
            story_points = int(story_points)
    except (ValueError, TypeError):
        story_points = 0

    assignee = fields.get("assignee")
    assignee_name = assignee.get("displayName", "Não atribuído") if assignee else "Não atribuído"

    priority = fields.get("priority")
    priority_name = priority.get("name", "N/A") if priority else "N/A"

    labels = fields.get("labels", [])
    components = [c.get("name") for c in fields.get("components", []) if isinstance(c, dict)]

    parent = fields.get("parent")
    parent_key = parent.get("key") if parent else None

    return {
        "key": issue.get("key"),
        "title": fields.get("summary", ""),
        "description": desc_text,
        "story_points": story_points,
        "status": fields.get("status", {}).get("name", "N/A"),
        "assignee": assignee_name,
        "priority": priority_name,
        "labels": labels,
        "components": components,
        "parent": parent_key
    }

def generate_markdown(issues, args):
    """Gera a string contendo o relatório formatado em Markdown."""
    lines = []
    lines.append("# Relatório do Backlog - Histórias de Usuário\n")
    lines.append(f"Total de Histórias encontradas: **{len(issues)}**\n")
    
    total_sp = sum(i["story_points"] for i in issues)
    if "points" in args.fields or "all" in args.fields:
        lines.append(f"Total de Story Points: **{total_sp}**\n")
    
    lines.append("---\n")

    if not issues:
        lines.append("*Nenhuma história de usuário encontrada no backlog para os filtros especificados.*\n")
        return "\n".join(lines)

    titles_only = args.titles_only or args.no_description

    for idx, story in enumerate(issues, start=1):
        if titles_only:
            lines.append(f"{idx}. **[{story['key']}]** {story['title']}")
        else:
            lines.append(f"### [{story['key']}] {story['title']}")
            
            # Detalhes opcionais
            details = []
            if "status" in args.fields or "all" in args.fields:
                details.append(f"**Status**: `{story['status']}`")
            if "points" in args.fields or "all" in args.fields:
                details.append(f"**Story Points**: `{story['story_points']}`")
            if "assignee" in args.fields or "all" in args.fields:
                details.append(f"**Atribuído**: {story['assignee']}")
            if "priority" in args.fields or "all" in args.fields:
                details.append(f"**Prioridade**: {story['priority']}")
            if "parent" in args.fields or "all" in args.fields:
                if story['parent']:
                    details.append(f"**Parent/Epic**: `{story['parent']}`")
            if "labels" in args.fields or "all" in args.fields:
                if story['labels']:
                    details.append(f"**Labels**: `{', '.join(story['labels'])}`")
            if "components" in args.fields or "all" in args.fields:
                if story['components']:
                    details.append(f"**Componentes**: `{', '.join(story['components'])}`")

            if details:
                lines.append("- " + " | ".join(details))

            # Descrição
            if story['description'] and story['description'] != "Sem descrição":
                lines.append("- **Descrição**:")
                desc_lines = story['description'].split("\n")
                formatted_desc = "\n".join(f"  > {line}" for line in desc_lines)
                lines.append(f"{formatted_desc}")
            lines.append("")

    return "\n".join(lines)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Extrai e gera um relatório Markdown das Histórias de Usuário (US) no Backlog do Jira."
    )
    parser.add_argument(
        "--titles-only", action="store_true",
        help="Exporta apenas Chave e Título das US (sem descrição ou detalhes extensos)."
    )
    parser.add_argument(
        "--no-description", action="store_true",
        help="Oculta a descrição das US, mantendo outros campos."
    )
    parser.add_argument(
        "--fields", nargs="+", default=["status", "points"],
        choices=["status", "points", "assignee", "priority", "parent", "labels", "components", "all"],
        help="Campos adicionais a incluir no relatório (padrão: status points)."
    )
    parser.add_argument(
        "--status", type=str,
        help="Filtrar por um ou mais status (separados por vírgula, ex: 'To Do,Refinement')."
    )
    parser.add_argument(
        "--priority", type=str,
        help="Filtrar por prioridade (ex: 'High,Medium')."
    )
    parser.add_argument(
        "--component", type=str,
        help="Filtrar por componente."
    )
    parser.add_argument(
        "--label", type=str,
        help="Filtrar por label."
    )
    parser.add_argument(
        "--epic", type=str,
        help="Filtrar por chave do Epic ou Parent."
    )
    parser.add_argument(
        "--jql", type=str,
        help="Condição JQL customizada adicional para filtrar a busca."
    )
    parser.add_argument(
        "--issue-type", type=str, default="Story",
        help="Tipo de edição Jira (padrão: 'Story')."
    )
    parser.add_argument(
        "-o", "--output", type=str, default="backlog_stories_report.md",
        help="Caminho do arquivo Markdown de saída (salvo por padrão em 'results/get_backlog_stories/')."
    )
    return parser.parse_args()

def resolve_output_path(output_arg):
    """Garante que a saída seja salva no diretório results/get_backlog_stories/ se nenhum diretório for especificado."""
    if not output_arg:
        output_arg = "backlog_stories_report.md"
    
    dir_name = os.path.dirname(output_arg)
    if not dir_name:
        output_path = os.path.join("results", "get_backlog_stories", output_arg)
    else:
        output_path = output_arg
        
    abs_dir = os.path.dirname(os.path.abspath(output_path))
    os.makedirs(abs_dir, exist_ok=True)
    return output_path

def main():
    args = parse_args()
    session = setup_session()

    # 1. Resolver Board ID
    board_id = JIRA_BOARD_ID
    if not board_id:
        if JIRA_PROJECT_KEY:
            board_id = find_board_id(session, JIRA_PROJECT_KEY)
        if not board_id:
            print("Erro: Não foi possível determinar o Board ID. Configure JIRA_BOARD_ID ou JIRA_PROJECT_KEY no seu .env.")
            sys.exit(1)

    # 2. Descobrir campo Story Points
    story_points_field = find_story_points_field(session)

    # 3. Construir JQL
    jql = build_jql(args)
    print(f"Buscando itens do backlog no Board ID '{board_id}'...")
    print(f"Filtro JQL aplicado: {jql}")

    # 4. Buscar US no Backlog
    raw_issues = fetch_backlog_issues(session, board_id, jql, story_points_field)
    parsed_issues = [parse_issue(issue, story_points_field) for issue in raw_issues]
    print(f"Histórias encontradas no backlog: {len(parsed_issues)}")

    # 5. Gerar Markdown
    md_content = generate_markdown(parsed_issues, args)

    # 6. Salvar em arquivo
    output_path = resolve_output_path(args.output)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Relatório Markdown salvo em: {output_path}")

if __name__ == "__main__":
    main()
