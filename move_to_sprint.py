#!/usr/bin/env python3
"""
Script para mover Histórias de Usuário (US) do Backlog para uma Sprint no Jira via REST API Agile v1.0.
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

for path in possible_env_paths:
    if os.path.exists(path):
        load_dotenv(path)
        break

JIRA_BASE_URL = (os.getenv("JIRA_BASE_URL") or os.getenv("JIRA_URL", "")).strip().rstrip('/')
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "").strip()
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "").strip()
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "").strip()
JIRA_BOARD_ID = os.getenv("JIRA_BOARD_ID", "").strip()

def setup_session():
    if not JIRA_BASE_URL or not JIRA_EMAIL or not JIRA_API_TOKEN:
        print("Erro: JIRA_BASE_URL, JIRA_EMAIL e JIRA_API_TOKEN devem estar configurados no arquivo .env.")
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

def find_board_id(session, project_key):
    try:
        url = f"{JIRA_BASE_URL}/rest/agile/1.0/board"
        resp = session.get(url, params={"projectKeyOrId": project_key})
        if resp.status_code == 200:
            boards = resp.json().get("values", [])
            if boards:
                return boards[0].get("id")
    except Exception as e:
        print(f"Erro ao procurar board: {e}")
    return None

def find_sprint_id(session, board_id, sprint_name):
    url = f"{JIRA_BASE_URL}/rest/agile/1.0/board/{board_id}/sprint"
    start_at = 0
    max_results = 50
    sprint_name_clean = sprint_name.strip().lower()

    while True:
        resp = session.get(url, params={"startAt": start_at, "maxResults": max_results})
        if resp.status_code != 200:
            print(f"Erro ao buscar sprints do board {board_id}: {resp.status_code} - {resp.text}")
            break
        data = resp.json()
        values = data.get("values", [])
        for sprint in values:
            name = sprint.get("name", "").strip().lower()
            if name == sprint_name_clean or sprint_name_clean in name:
                return sprint.get("id"), sprint.get("name")
        if data.get("isLast", True) or len(values) < max_results:
            break
        start_at += len(values)

    return None, None

def move_issues_to_sprint(session, sprint_id, issue_keys, dry_run=False):
    if dry_run:
        print(f"[DRY-RUN] Movendo issues {issue_keys} para Sprint ID {sprint_id}")
        return True, "Simulado com sucesso"

    url = f"{JIRA_BASE_URL}/rest/agile/1.0/sprint/{sprint_id}/issue"
    payload = {"issues": issue_keys}
    resp = session.post(url, json=payload)
    if resp.status_code in [200, 204]:
        return True, "Issues movidas com sucesso!"
    else:
        return False, f"Erro {resp.status_code}: {resp.text}"

def parse_args():
    parser = argparse.ArgumentParser(description="Move US do Backlog para uma Sprint no Jira.")
    parser.add_argument("--sprint", type=str, default="Sprint 7", help="Nome da Sprint de destino (padrão: 'Sprint 7').")
    parser.add_argument("--keys", nargs="+", required=True, help="Lista de chaves de edições Jira (ex: SCRUM-35 SCRUM-36 SCRUM-48 HMS-28 HMS-29 SCRUM-38).")
    parser.add_argument("--board-id", type=str, help="ID do Board Jira (opcional).")
    parser.add_argument("--dry-run", action="store_true", help="Simula a movimentação sem alterar o Jira.")
    parser.add_argument("-y", "--yes", action="store_true", help="Executa sem pedir confirmação manual.")
    return parser.parse_args()

def main():
    args = parse_args()
    session = setup_session()

    board_id = args.board_id or JIRA_BOARD_ID
    if not board_id and JIRA_PROJECT_KEY:
        board_id = find_board_id(session, JIRA_PROJECT_KEY)
    
    if not board_id:
        print("Erro: Não foi possível determinar o Board ID. Forneça --board-id ou configure JIRA_BOARD_ID/JIRA_PROJECT_KEY no .env.")
        sys.exit(1)

    print(f"Buscando a Sprint '{args.sprint}' no Board {board_id}...")
    sprint_id, actual_sprint_name = find_sprint_id(session, board_id, args.sprint)

    if not sprint_id:
        print(f"Erro: Não foi possível encontrar a Sprint '{args.sprint}' no Board {board_id}.")
        sys.exit(1)

    print(f"Sprint encontrada: ID {sprint_id} - '{actual_sprint_name}'")
    print(f"Issues a serem movidas: {args.keys}")

    if not args.dry_run and not args.yes:
        confirm = input(f"\nConfirma a movimentação de {len(args.keys)} issue(s) para '{actual_sprint_name}'? (s/N): ").strip().lower()
        if confirm not in ['s', 'sim', 'y', 'yes']:
            print("Operação cancelada.")
            sys.exit(0)

    success, msg = move_issues_to_sprint(session, sprint_id, args.keys, dry_run=args.dry_run)
    
    report = {
        "sprint_name": actual_sprint_name,
        "sprint_id": sprint_id,
        "issues": args.keys,
        "success": success,
        "message": msg
    }

    out_dir = os.path.join("results", "move_to_sprint")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "sprint_move_report.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    if success:
        print(f"\n✓ Sucesso: {msg}")
    else:
        print(f"\n✗ Falha: {msg}")
    print(f"Relatório gerado em: {out_file}")

if __name__ == "__main__":
    main()
