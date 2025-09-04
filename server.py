from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv


load_dotenv("D:/4105/open_deep_research/.env")
repo_path = "D:/4105/GitPython"

mcp = FastMCP("Codebase")


@mcp.tool()
def list_files():
    """List files in the given folder path."""
    try:
        return [
            f for f in os.listdir(repo_path)
            if os.path.isfile(os.path.join(repo_path, f))
        ]
    except Exception as e:
        return [f"Error accessing path: {e}"]


@mcp.tool()
def read_file(file_name):
    """Read file contents from repo."""
    abs_path = os.path.join(repo_path, file_name)
    with open(abs_path, 'r', encoding='utf-8') as f:
        return f.read()

@mcp.tool()
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

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="sse")