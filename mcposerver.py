from mcp.server.fastmcp import FastMCP
import os
import git


repo_path = '../4105/GitPython' 

mcp = FastMCP("Codebase")

@mcp.tool()
def list_repo_files():
    """List all files in the repo."""
    repo = git.Repo(repo_path)
    return [item.path for item in repo.tree().traverse() if item.type == 'blob']


@mcp.tool()
def read_file(file_name):
    """Read file contents from repo."""
    abs_path = os.path.join(repo_path, file_name)
    with open(abs_path, 'r', encoding='utf-8') as f:
        return f.read()

@mcp.prompt()
def find_files_by_keyword_prompt(keyword):
    """Find file in the repo by the given keyword."""
    matching_files = []

    for dirpath, _, filenames in os.walk(repo_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if keyword in content:
                        matching_files.append(filepath)
            except Exception as e:
                continue

    return f"{len(matching_files)} files found: {', '.join(matching_files)}"