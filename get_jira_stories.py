import os
import sys
import json
import base64
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
        print(f"Loaded environment variables from: {path}")
        env_loaded = True
        break

if not env_loaded:
    print("Warning: No .env file found. Will try to use system environment variables.")

# Retrieve environment variables and strip whitespace/CRLF characters
JIRA_BASE_URL = (os.getenv("JIRA_BASE_URL") or os.getenv("JIRA_URL", "")).strip()
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "").strip()
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "").strip()
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "").strip()
JIRA_BOARD_ID = os.getenv("JIRA_BOARD_ID", "").strip()

if not JIRA_BASE_URL or not JIRA_EMAIL or not JIRA_API_TOKEN:
    print("Error: JIRA_BASE_URL, JIRA_EMAIL, and JIRA_API_TOKEN must be set in your .env file.")
    sys.exit(1)

# Clean up base url if needed
JIRA_BASE_URL = JIRA_BASE_URL.rstrip('/')

# Create requests session with basic auth header
session = requests.Session()
auth_str = f"{JIRA_EMAIL}:{JIRA_API_TOKEN}"
b64_auth = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
session.headers.update({
    "Authorization": f"Basic {b64_auth}",
    "Accept": "application/json",
    "Content-Type": "application/json"
})

def get_request(url, params=None):
    """Helper to perform requests with error handling."""
    response = session.get(url, params=params)
    if response.status_code != 200:
        print(f"Error requesting {url}: {response.status_code} - {response.text}")
        response.raise_for_status()
    return response.json()

def adf_to_text(adf):
    """Recursively converts Atlassian Document Format (ADF) to plain text."""
    if not adf:
        return ""
    if isinstance(adf, str):
        return adf
    text_parts = []
    if isinstance(adf, dict):
        if adf.get("type") == "text":
            return adf.get("text", "")
        # Add newlines for paragraph/heading transitions
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

def find_story_points_field():
    """Queries Jira fields to find the custom field key for Story Points."""
    print("Searching for Story Points field key...")
    try:
        fields = get_request(f"{JIRA_BASE_URL}/rest/api/3/field")
        for field in fields:
            name = field.get("name", "").lower()
            if "story point" in name or "story_point" in name:
                field_id = field.get("id")
                print(f"Found Story Points field: '{field.get('name')}' -> {field_id}")
                return field_id
    except Exception as e:
        print(f"Could not fetch fields metadata: {e}. Defaulting to 'customfield_10016'.")
    return "customfield_10016"

def find_board_id(project_key):
    """Finds the first board associated with the given project key."""
    print(f"Searching for board associated with project '{project_key}'...")
    try:
        boards_data = get_request(f"{JIRA_BASE_URL}/rest/agile/1.0/board", params={"projectKeyOrId": project_key})
        values = boards_data.get("values", [])
        if values:
            board_id = values[0].get("id")
            board_name = values[0].get("name")
            print(f"Found board: '{board_name}' (ID: {board_id})")
            return board_id
        else:
            print(f"No boards found for project '{project_key}'.")
    except Exception as e:
        print(f"Error searching for board: {e}")
    return None

def fetch_all_sprints(board_id):
    """Fetches all sprints for the board, handling pagination."""
    sprints = []
    start_at = 0
    max_results = 50
    while True:
        url = f"{JIRA_BASE_URL}/rest/agile/1.0/board/{board_id}/sprint"
        data = get_request(url, params={"startAt": start_at, "maxResults": max_results})
        values = data.get("values", [])
        sprints.extend(values)
        if data.get("isLast", True) or len(values) < max_results:
            break
        start_at += len(values)
    return sprints

def fetch_issues_for_sprint(board_id, sprint_id, story_points_field):
    """Fetches all stories in a specific sprint, handling pagination."""
    issues = []
    start_at = 0
    max_results = 50
    # Use configurable issue types from env, default to 'Story'
    issue_types = os.getenv("JIRA_ISSUE_TYPES", "Story")
    # Format for JQL, e.g. "Story" or "Story, Task" -> "('Story')" or "('Story', 'Task')"
    types_list = [f"'{t.strip()}'" for t in issue_types.split(",")]
    jql = f"issuetype in ({','.join(types_list)})"
    while True:
        url = f"{JIRA_BASE_URL}/rest/agile/1.0/board/{board_id}/sprint/{sprint_id}/issue"
        data = get_request(url, params={
            "startAt": start_at, 
            "maxResults": max_results,
            "jql": jql,
            "fields": f"summary,description,{story_points_field},status"
        })
        values = data.get("issues", [])
        issues.extend(values)
        if start_at + len(values) >= data.get("total", 0) or len(values) < max_results:
            break
        start_at += len(values)
    return issues

def fetch_backlog_issues(board_id, story_points_field):
    """Fetches all stories in the backlog, handling pagination."""
    issues = []
    start_at = 0
    max_results = 50
    # Use configurable issue types from env, default to 'Story'
    issue_types = os.getenv("JIRA_ISSUE_TYPES", "Story")
    types_list = [f"'{t.strip()}'" for t in issue_types.split(",")]
    jql = f"issuetype in ({','.join(types_list)})"
    while True:
        url = f"{JIRA_BASE_URL}/rest/agile/1.0/board/{board_id}/backlog"
        data = get_request(url, params={
            "startAt": start_at,
            "maxResults": max_results,
            "jql": jql,
            "fields": f"summary,description,{story_points_field},status"
        })
        values = data.get("issues", [])
        issues.extend(values)
        if start_at + len(values) >= data.get("total", 0) or len(values) < max_results:
            break
        start_at += len(values)
    return issues

def parse_issue(issue, story_points_field, sprint_name="Backlog"):
    """Parses a Jira issue into a clean dictionary."""
    fields = issue.get("fields", {})
    description = fields.get("description")
    
    # Standardize description text
    desc_text = adf_to_text(description) if description else "Sem descrição"
    
    story_points = fields.get(story_points_field)
    try:
        story_points = float(story_points) if story_points is not None else 0.0
        # Convert to int if it's a whole number
        if story_points.is_integer():
            story_points = int(story_points)
    except (ValueError, TypeError):
        story_points = 0

    return {
        "key": issue.get("key"),
        "title": fields.get("summary", ""),
        "description": desc_text,
        "story_points": story_points,
        "status": fields.get("status", {}).get("name", "N/A"),
        "sprint": sprint_name
    }

def main():
    # 1. Resolve Board ID
    board_id = JIRA_BOARD_ID
    if not board_id:
        if JIRA_PROJECT_KEY:
            board_id = find_board_id(JIRA_PROJECT_KEY)
        if not board_id:
            print("Error: Could not determine Board ID. Please provide JIRA_BOARD_ID or JIRA_PROJECT_KEY in your .env.")
            sys.exit(1)
    
    # 2. Find Story Points field
    story_points_field = find_story_points_field()

    report_data = {
        "sprints": {},
        "backlog": []
    }

    # 3. Fetch Sprints and their stories
    print("\nFetching sprints...")
    try:
        sprints = fetch_all_sprints(board_id)
        print(f"Found {len(sprints)} sprints.")
        
        for sprint in sprints:
            sprint_name = sprint.get("name")
            sprint_id = sprint.get("id")
            sprint_state = sprint.get("state")
            print(f"Fetching issues for sprint: {sprint_name} ({sprint_state})...")
            
            sprint_key = f"{sprint_name} ({sprint_state.upper()})"
            report_data["sprints"][sprint_key] = []
            
            issues = fetch_issues_for_sprint(board_id, sprint_id, story_points_field)
            for issue in issues:
                parsed = parse_issue(issue, story_points_field, sprint_name=sprint_name)
                report_data["sprints"][sprint_key].append(parsed)
                
            print(f"  -> Retrieved {len(report_data['sprints'][sprint_key])} stories.")
    except Exception as e:
        print(f"Could not fetch sprint information: {e}")

    # 4. Fetch Backlog stories
    print("\nFetching backlog issues...")
    try:
        backlog_issues = fetch_backlog_issues(board_id, story_points_field)
        for issue in backlog_issues:
            parsed = parse_issue(issue, story_points_field, sprint_name="Backlog")
            report_data["backlog"].append(parsed)
        print(f"  -> Retrieved {len(report_data['backlog'])} stories.")
    except Exception as e:
        print(f"Could not fetch backlog information: {e}")

    # 5. Export to JSON
    output_dir = os.path.join("results", "get_jira_stories")
    os.makedirs(output_dir, exist_ok=True)
    
    json_output_path = os.path.join(output_dir, "jira_stories.json")
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)
    print(f"\nSaved raw data to {json_output_path}")

    # 6. Generate Markdown Report
    md_output_path = os.path.join(output_dir, "jira_stories_report.md")
    with open(md_output_path, "w", encoding="utf-8") as f:
        f.write("# Relatório de Histórias de Usuário (Jira Board)\n\n")
        
        # Table of Contents / Summary
        f.write("## Resumo por Sprint\n")
        for sprint_key, stories in report_data["sprints"].items():
            total_sp = sum(s["story_points"] for s in stories)
            f.write(f"- **{sprint_key}**: {len(stories)} histórias, {total_sp} Story Points\n")
        f.write(f"- **Backlog**: {len(report_data['backlog'])} histórias, {sum(s['story_points'] for s in report_data['backlog'])} Story Points\n\n")
        f.write("---\n\n")
        
        # Sprints Section
        for sprint_key, stories in report_data["sprints"].items():
            f.write(f"## Sprint: {sprint_key}\n\n")
            if not stories:
                f.write("*Nenhuma história nesta sprint.*\n\n")
                continue
            
            for story in stories:
                f.write(f"### [{story['key']}] {story['title']}\n")
                f.write(f"- **Status**: `{story['status']}`\n")
                f.write(f"- **Story Points**: {story['story_points']}\n")
                f.write("- **Descrição**:\n")
                # Indent description lines
                desc_lines = story['description'].split("\n")
                formatted_desc = "\n".join(f"  > {line}" for line in desc_lines)
                f.write(f"{formatted_desc}\n\n")
            f.write("---\n\n")
            
        # Backlog Section
        f.write("## Backlog\n\n")
        if not report_data["backlog"]:
            f.write("*Nenhuma história no backlog.*\n\n")
        else:
            for story in report_data["backlog"]:
                f.write(f"### [{story['key']}] {story['title']}\n")
                f.write(f"- **Status**: `{story['status']}`\n")
                f.write(f"- **Story Points**: {story['story_points']}\n")
                f.write("- **Descrição**:\n")
                desc_lines = story['description'].split("\n")
                formatted_desc = "\n".join(f"  > {line}" for line in desc_lines)
                f.write(f"{formatted_desc}\n\n")

    print(f"Saved formatted markdown report to {md_output_path}")
    print("\nProcess finished successfully!")

if __name__ == "__main__":
    main()
