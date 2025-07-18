# Infinit ⎯ Minimal Project Scaffolder

> **Zero-config folder generator**
> For hackers who want structure *now*
---

## 🚀 Installation

```bash
# Install with pipx (recommended)
pipx install infinit

# Or with pip
pip install infinit
```

---

## 📦 Usage

```bash
# Create project (HTB template)
infinit create myproj -t basic

# Custom structure
infinit create myproj -f "scans,loot" -F "README.md:# Findings"
```

### Available Templates

| Alias | Template Name | Structure                |
| ----- | ------------- | ------------------------ |
| `basic`   | HTB           | scans/, loot/, exploits/ |
| `web`   | Web           | static/, templates/      |

---

## 🛠 Development

```bash
# Install locally
pip install -e .

# Run tests
pytest
```

---

## 🔍 Philosophy

* **No YAML** ⎯ Configure via CLI
* **Zero Dependencies** ⎯ Only `click`
* **HTB-Ready** ⎯ Default pentest structure

---

## 📁 Key Files Structure

```
.
├── .gitignore
├── README.md
├── infinit/
│   ├── __init__.py
│   ├── cli.py          # Main CLI
│   └── core/
│       ├── __init__.py
│       ├── builder.py   # Logic
│       └── templates.py
└── pyproject.toml
```
