
TEMPLATES = {
    "basic": {
        "folders": ["scans", "loot", "exploits"],
        "files": {"README.md": "# {name}\n## Findings\n"}
    },
    "web": {
        "folders": ["static", "controllers"],
        "files": {"app.py": "from flask import Flask\napp = Flask(__name__)"}
    }
}