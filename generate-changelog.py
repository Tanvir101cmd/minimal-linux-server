import subprocess
import re
from collections import defaultdict

# Define your preferred category headers and emojis
CATEGORIES = {
    'feat': 'Features',
    'fix': 'Bug Fixes',
    'docs': 'Documentation',
    'refactor': 'Refactoring',
    'perf': 'Performance',
    'chore': 'Miscellaneous Tasks',
    'ci': 'CI/CD Framework'
}

def generate_changelog():
    # Fetch log records separated by a rare delimiter to prevent collision
    cmd = ["git", "log", "--date=short", "--pretty=format:%ad||%s||%h"]
    log_output = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.strip()
    
    if not log_output:
        return

    # Structure: changelog[date][category] = [commits]
    changelog = defaultdict(lambda: defaultdict(list))
    
    for line in log_output.split('\n'):
        if "||" not in line:
            continue
        date, msg, commit_hash = line.split("||")
        
        # Skip loop-inducing action commits
        if "chore(changelog):" in msg or "auto-update changelog" in msg:
            continue
            
        # Parse Conventional Commit match rules
        match = re.match(r'^(\w+)(?:\(([^)]+)\))?!?\s*:\s*(.*)$', msg)
        
        if match:
            commit_type, scope, description = match.group(1).lower(), match.group(2), match.group(3)
            category = CATEGORIES.get(commit_type, 'Other Changes')
            
            scope_str = f"***({scope})*** " if scope else ""
            # Generates a direct clickable markdown link to your specific GitHub repo commits
            formatted_commit = f"{scope_str}{description.capitalize()} ([{commit_hash}](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/{commit_hash}))"
            changelog[date][category].append(formatted_commit)
        else:
            changelog[date]['Other Changes'].append(f"{msg} ([{commit_hash}](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/{commit_hash}))")

    # Compile structure into standard Markdown format
    markdown = ["# Changelog\n\nAll notable changes to this project will be documented in this file.\n"]
    
    for date in sorted(changelog.keys(), reverse=True):
        markdown.append(f"## {date}\n")
        
        # Print categories in our predefined explicit order if they have entries
        for cat_type, cat_heading in CATEGORIES.items():
            if cat_heading in changelog[date]:
                markdown.append(f"### {cat_heading}")
                for commit in changelog[date][cat_heading]:
                    markdown.append(f"- {commit}")
                markdown.append("") # Spacing spacer
                
        if 'Other Changes' in changelog[date]:
            markdown.append("### Other Changes")
            for commit in changelog[date]['Other Changes']:
                markdown.append(f"- {commit}")
            markdown.append("")

    with open("CHANGELOG.md", "w") as f:
        f.write("\n".join(markdown).strip() + "\n")

if __name__ == "__main__":
    generate_changelog()