import re

# Gen AI Settings
OPENAI_MODEL = 'o4-mini'
OPENAI_ENDPOINT = 'https://api.openai.com/v1/responses'
MAX_TOKENS = 100000

# Tool settings
DESTINATION_FILE = 'MERMAID.md'
MERMAID_HEADER = "## MermaidJS Diagram - Generated by [Code2Chart](https://github.com/scmgustafson/code2chart/tree/main)"
MERMAID_FOOTER = "<!-- END AUTOMATED MERMAID -->"

# File map settings
IGNORE_PATTERNS = (
    "venv", "samples", "favicon", ".git", 
    "node_modules", "public", ".next", "__tests__", "README.md", 
    "yarn.lock", ".DS_Store", ".env", "__pycache__", "lock",
    ".terraform", ".python", "requirements", "__init__"
)

# Mermaid syntax checker settings
TOTAL_RETRIES = 3
RETRY_DELAY = 5

# Define regexes for validating the mermaid output syntax (Lots of AI magic here, no touchy)
# Accept quoted labels and square bracket text
DIAG_START = re.compile(r'^\s*(graph|flowchart|sequenceDiagram|gantt|classDiagram)\b', re.IGNORECASE)
COMMENT_DEF = re.compile(r'^\s*%%')
# Matches: node -->|label| node, supports quoted node IDs
EDGE_DEF = re.compile(
    r'^\s*[\w.-]+(?:\s*\[.*?\]|\s*\".*?\")?\s*--[->|]*\|?.*?\|?\s*[\w.-]+(?:\s*\[.*?\]|\s*\".*?\")?\s*$'
)
# Matches: node[Label] or node["quoted"]
NODE_DEF = re.compile(
    r'^\s*[\w.-]+(?:\s*\[.*?\]|\s*\".*?\")?\s*$'
)
SUBGRAPH_DEF = re.compile(r'^\s*subgraph\b', re.IGNORECASE)
SUBGRAPH_END = re.compile(r'^\s*end\s*$', re.IGNORECASE)
CLASS_DEF = re.compile(r'^\s*classDef\b', re.IGNORECASE)
CLASS_ASSIGN = re.compile(r'^\s*class\b', re.IGNORECASE)