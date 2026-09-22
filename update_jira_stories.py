#!/usr/bin/env python3
"""
Script para atualização de Histórias de Usuário (US) no Jira via REST API v3.
Suporta atualização individual (via argumentos CLI) e atualização em lote (via arquivo JSON).
"""

import os
import sys
import json
import base64
import argparse
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente de múltiplos locais possíveis
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

JIRA_BASE_URL = (os.getenv("JIRA_BASE_URL") or os.getenv("JIRA_URL", "")).strip().rstrip('/')
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "").strip()
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "").strip()

def setup_session():
    """Configura e retorna a sessão HTTP para autenticação na API do Jira."""
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

def find_story_points_field(session):
    """Descobre dinamicamente o ID do campo customizado de Story Points."""
    try:
        url = f"{JIRA_BASE_URL}/rest/api/3/field"
        resp = session.get(url)
        if resp.status_code == 200:
            fields = resp.json()
            for field in fields:
                name = field.get("name", "").lower()
                if "story point" in name or "story_point" in name:
                    return field.get("id")
    except Exception as e:
        print(f"Aviso ao consultar campos do Jira: {e}")
    return "customfield_10016"

def parse_inline_marks(text):
    """Auxiliar para converter formatações inline (**negrito**, `código`) em nós de texto ADF."""
    if not text:
        return []
    import re
    tokens = re.split(r'(\*\*.*?\*\*|`.*?`)', text)
    content = []
    for token in tokens:
        if not token:
            continue
        if token.startswith('**') and token.endswith('**') and len(token) >= 4:
            content.append({
                "type": "text",
                "text": token[2:-2],
                "marks": [{"type": "bold"}]
            })
        elif token.startswith('`') and token.endswith('`') and len(token) >= 2:
            content.append({
                "type": "text",
                "text": token[1:-1],
                "marks": [{"type": "code"}]
            })
        else:
            content.append({
                "type": "text",
                "text": token
            })
    return content

def text_to_adf(text):
    """
    Converte texto Markdown estruturado para o formato ADF (Atlassian Document Format)
    nativo da API REST v3 do Jira, renderizando títulos, listas e negritos.
    """
    if isinstance(text, dict):
        return text
    if not text:
        return None
        
    import re
    lines = str(text).split('\n')
    blocks = []
    
    current_list_type = None  # 'bullet' ou 'ordered'
    current_list_items = []
    
    def flush_list():
        nonlocal current_list_type, current_list_items
        if not current_list_type or not current_list_items:
            return
        
        list_node_type = 'bulletList' if current_list_type == 'bullet' else 'orderedList'
        list_items_adf = []
        for item_text in current_list_items:
            list_items_adf.append({
                "type": "listItem",
                "content": [{
                    "type": "paragraph",
                    "content": parse_inline_marks(item_text)
                }]
            })
        blocks.append({
            "type": list_node_type,
            "content": list_items_adf
        })
        current_list_type = None
        current_list_items = []

    for line in lines:
        stripped = line.strip()
        
        # Régua Horizontal (--- ou ***)
        if stripped in ['---', '***', '___']:
            flush_list()
            blocks.append({"type": "rule"})
            continue
            
        # Títulos (# ## ###)
        heading_match = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if heading_match:
            flush_list()
            level = len(heading_match.group(1))
            h_text = heading_match.group(2)
            blocks.append({
                "type": "heading",
                "attrs": {"level": min(level, 6)},
                "content": parse_inline_marks(h_text)
            })
            continue
            
        # Lista com marcadores/bolinhas (- ou *)
        bullet_match = re.match(r'^[\-\*]\s+(.*)$', stripped)
        if bullet_match:
            if current_list_type and current_list_type != 'bullet':
                flush_list()
            current_list_type = 'bullet'
            current_list_items.append(bullet_match.group(1))
            continue
            
        # Lista numerada (1. 2. etc)
        ordered_match = re.match(r'^\d+\.\s+(.*)$', stripped)
        if ordered_match:
            if current_list_type and current_list_type != 'ordered':
                flush_list()
            current_list_type = 'ordered'
            current_list_items.append(ordered_match.group(1))
            continue
            
        # Linha em branco
        if not stripped:
            flush_list()
            continue
            
        # Parágrafo comum
        flush_list()
        blocks.append({
            "type": "paragraph",
            "content": parse_inline_marks(stripped)
        })

    flush_list()
    
    if not blocks:
        blocks = [{"type": "paragraph", "content": []}]

    return {
        "version": 1,
        "type": "doc",
        "content": blocks
    }

def resolve_user_account_id(session, user_identifier):
    """
    Tenta resolver o accountId de um usuário a partir do e-mail, nome ou accountId direto.
    """
    if not user_identifier or user_identifier.lower() in ["none", "unassigned", "nao atribuido", "sem responsável"]:
        return None
        
    # Se já parecer um accountId do Jira (ex: contendo ':' ou no formato de hash)
    if ":" in user_identifier or len(user_identifier) >= 24:
        return user_identifier
        
    url = f"{JIRA_BASE_URL}/rest/api/3/user/search"
    params = {"query": user_identifier}
    resp = session.get(url, params=params)
    if resp.status_code == 200:
        users = resp.json()
        if users:
            return users[0].get("accountId")
            
    print(f"Aviso: Não foi possível encontrar o usuário Jira para '{user_identifier}'.")
    return None

def transition_issue_status(session, issue_key, target_status, dry_run=False):
    """
    Transiciona o status de uma US para o status alvo fornecido.
    """
    url_transitions = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}/transitions"
    resp = session.get(url_transitions)
    if resp.status_code != 200:
        print(f"[{issue_key}] Erro ao buscar transições de status disponíveis: {resp.status_code} - {resp.text}")
        return False

    transitions = resp.json().get("transitions", [])
    matching_transition = None
    
    target_clean = target_status.strip().lower()
    for trans in transitions:
        trans_name = trans.get("name", "").lower()
        to_status_name = trans.get("to", {}).get("name", "").lower()
        if target_clean in [trans_name, to_status_name]:
            matching_transition = trans
            break

    if not matching_transition:
        available = [f"'{t.get('name')}' -> '{t.get('to', {}).get('name')}'" for t in transitions]
        print(f"[{issue_key}] Erro: Transição para o status '{target_status}' não disponível.")
        print(f"  Transições disponíveis: {', '.join(available) if available else 'Nenhuma'}")
        return False

    trans_id = matching_transition.get("id")
    trans_to_name = matching_transition.get("to", {}).get("name")
    
    if dry_run:
        print(f"  [DRY-RUN] Transicionar {issue_key} para '{trans_to_name}' (ID da transição: {trans_id})")
        return True

    payload = {"transition": {"id": trans_id}}
    post_resp = session.post(url_transitions, json=payload)
    if post_resp.status_code in [200, 204]:
        print(f"  ✓ Transicionado status de {issue_key} para '{trans_to_name}'")
        return True
    else:
        print(f"  ✗ Erro ao transicionar status de {issue_key}: {post_resp.status_code} - {post_resp.text}")
        return False

def update_single_issue(session, issue_key, update_data, story_points_field, dry_run=False):
    """
    Atualiza os campos de uma US individual no Jira.
    """
    issue_key = issue_key.strip().upper()
    print(f"\nProcessing update for issue: {issue_key}")
    
    fields_payload = {}
    
    # 1. Title / Summary
    if "summary" in update_data and update_data["summary"] is not None:
        fields_payload["summary"] = update_data["summary"]
        
    # 2. Story Points
    if "story_points" in update_data and update_data["story_points"] is not None:
        try:
            sp_val = float(update_data["story_points"])
            if sp_val.is_integer():
                sp_val = int(sp_val)
            fields_payload[story_points_field] = sp_val
        except (ValueError, TypeError):
            print(f"  Aviso: Valor de story_points inválido ('{update_data['story_points']}'). Ignorando.")

    # 3. Description
    if "description" in update_data and update_data["description"] is not None:
        fields_payload["description"] = text_to_adf(update_data["description"])
        
    # 4. Priority
    if "priority" in update_data and update_data["priority"] is not None:
        fields_payload["priority"] = {"name": update_data["priority"]}

    # 5. Assignee
    if "assignee" in update_data and update_data["assignee"] is not None:
        account_id = resolve_user_account_id(session, update_data["assignee"])
        if account_id:
            fields_payload["assignee"] = {"accountId": account_id}
        elif update_data["assignee"].lower() in ["none", "unassigned", "nao atribuido", "sem responsável"]:
            fields_payload["assignee"] = None

    # 6. Labels
    if "labels" in update_data and update_data["labels"] is not None:
        if isinstance(update_data["labels"], str):
            labels_list = [l.strip() for l in update_data["labels"].split(",") if l.strip()]
        elif isinstance(update_data["labels"], list):
            labels_list = update_data["labels"]
        else:
            labels_list = []
        fields_payload["labels"] = labels_list

    # 7. Components
    if "components" in update_data and update_data["components"] is not None:
        if isinstance(update_data["components"], str):
            comp_list = [{"name": c.strip()} for c in update_data["components"].split(",") if c.strip()]
        elif isinstance(update_data["components"], list):
            comp_list = [{"name": c} if isinstance(c, str) else c for c in update_data["components"]]
        else:
            comp_list = []
        fields_payload["components"] = comp_list

    fields_updated = False
    
    if fields_payload:
        if dry_run:
            print(f"  [DRY-RUN] Atualização de campos em {issue_key}:")
            print(f"    Payload JSON: {json.dumps(fields_payload, ensure_ascii=False, indent=6)}")
            fields_updated = True
        else:
            url_issue_v3 = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"
            resp = session.put(url_issue_v3, json={"fields": fields_payload})
            if resp.status_code in [200, 204]:
                print(f"  ✓ Campos atualizados com sucesso para {issue_key} (API v3)")
                fields_updated = True
            else:
                # Tenta fallback via API v2 com descrição em formato texto/markdown
                if "description" in update_data and isinstance(update_data["description"], str):
                    fields_payload_v2 = dict(fields_payload)
                    fields_payload_v2["description"] = update_data["description"]
                    url_issue_v2 = f"{JIRA_BASE_URL}/rest/api/2/issue/{issue_key}"
                    resp_v2 = session.put(url_issue_v2, json={"fields": fields_payload_v2})
                    if resp_v2.status_code in [200, 204]:
                        print(f"  ✓ Campos atualizados com sucesso para {issue_key} (API v2)")
                        fields_updated = True
                    else:
                        print(f"  ✗ Erro ao atualizar campos em {issue_key}: v3 ({resp.status_code}) / v2 ({resp_v2.status_code}) - {resp_v2.text}")
                else:
                    print(f"  ✗ Erro ao atualizar campos em {issue_key}: {resp.status_code} - {resp.text}")

    # 8. Status Transition (se especificado)
    status_updated = True
    if "status" in update_data and update_data["status"]:
        status_updated = transition_issue_status(session, issue_key, update_data["status"], dry_run=dry_run)

    return fields_updated or status_updated

def parse_args():
    parser = argparse.ArgumentParser(
        description="Script para atualização de Histórias de Usuário (US) no Jira via REST API v3."
    )
    
    # Modo Individual
    parser.add_argument("--key", type=str, help="Chave da US a ser atualizada (ex: SCRUM-27 ou PROJ-123).")
    parser.add_argument("--summary", "--title", type=str, help="Novo título / resumo da US.")
    parser.add_argument("--description", type=str, help="Nova descrição da US.")
    parser.add_argument("--points", "--story-points", type=float, help="Novo valor de Story Points.")
    parser.add_argument("--status", type=str, help="Novo status da US (ex: 'In Progress', 'Done', 'To Do').")
    parser.add_argument("--assignee", type=str, help="E-mail ou ID do novo responsável (ou 'none' para desatribuir).")
    parser.add_argument("--priority", type=str, help="Nova prioridade (ex: 'High', 'Medium', 'Low').")
    parser.add_argument("--labels", type=str, help="Novas labels separadas por vírgula (substitui labels existentes).")
    parser.add_argument("--components", type=str, help="Novos componentes separados por vírgula.")

    # Modo Batch
    parser.add_argument("--file", "-f", type=str, help="Caminho para arquivo JSON contendo lote de atualizações de US.")

    # Flags de Segurança / Controle
    parser.add_argument("--dry-run", action="store_true", help="Simula as alterações sem enviá-las ao Jira.")
    parser.add_argument("-y", "--yes", action="store_true", help="Confirma a execução das alterações sem solicitar confirmação manual.")

    return parser.parse_args()

def main():
    args = parse_args()
    session = setup_session()
    
    story_points_field = find_story_points_field(session)
    
    updates_list = []
    
    # 1. Coleta de atualizações do modo CLI individual
    if args.key:
        cli_update = {"key": args.key}
        if args.summary is not None: cli_update["summary"] = args.summary
        if args.description is not None: cli_update["description"] = args.description
        if args.points is not None: cli_update["story_points"] = args.points
        if args.status is not None: cli_update["status"] = args.status
        if args.assignee is not None: cli_update["assignee"] = args.assignee
        if args.priority is not None: cli_update["priority"] = args.priority
        if args.labels is not None: cli_update["labels"] = args.labels
        if args.components is not None: cli_update["components"] = args.components
        updates_list.append(cli_update)

    # 2. Coleta de atualizações do modo batch JSON
    if args.file:
        if not os.path.exists(args.file):
            print(f"Erro: O arquivo batch especificado '{args.file}' não foi encontrado.")
            sys.exit(1)
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                batch_data = json.load(f)
                if isinstance(batch_data, list):
                    updates_list.extend(batch_data)
                elif isinstance(batch_data, dict):
                    updates_list.append(batch_data)
        except Exception as e:
            print(f"Erro ao ler o arquivo JSON '{args.file}': {e}")
            sys.exit(1)

    if not updates_list:
        print("Erro: Nenhuma atualização especificada. Forneça --key com os campos desejados ou um arquivo JSON via --file.")
        print("Use python3 update_jira_stories.py --help para ver os detalhes de uso.")
        sys.exit(1)

    print(f"==================================================")
    print(f"  Jira Stories Update Script")
    print(f"  Total de US para atualizar: {len(updates_list)}")
    print(f"  Modo Simulação (Dry-Run): {'SIM' if args.dry_run else 'NÃO'}")
    print(f"==================================================")

    # Confirmação manual se não estiver em dry-run e não tiver a flag --yes
    if not args.dry_run and not args.yes:
        confirm = input("\nDeseja prosseguir com a atualização destas USs no Jira? (s/N): ").strip().lower()
        if confirm not in ['s', 'sim', 'y', 'yes']:
            print("Operação cancelada pelo usuário.")
            sys.exit(0)

    execution_log = {
        "dry_run": args.dry_run,
        "total_issues": len(updates_list),
        "success_count": 0,
        "fail_count": 0,
        "details": []
    }

    for item in updates_list:
        key = item.get("key")
        if not key:
            print("Aviso: Item de atualização ignorado pois não possui a chave 'key'.")
            execution_log["fail_count"] += 1
            execution_log["details"].append({"key": None, "status": "failed", "reason": "Missing key"})
            continue
            
        success = update_single_issue(session, key, item, story_points_field, dry_run=args.dry_run)
        if success:
            execution_log["success_count"] += 1
            execution_log["details"].append({"key": key, "status": "success"})
        else:
            execution_log["fail_count"] += 1
            execution_log["details"].append({"key": key, "status": "failed"})

    output_dir = os.path.join("results", "update_jira_stories")
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "update_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(execution_log, f, indent=4, ensure_ascii=False)

    print(f"\n==================================================")
    print(f"Resumo da Execução:")
    print(f"  Sucessos / Simulações válidas: {execution_log['success_count']}")
    print(f"  Falhas: {execution_log['fail_count']}")
    print(f"  Relatório salvo em: {report_path}")
    print(f"==================================================")

if __name__ == "__main__":
    main()
