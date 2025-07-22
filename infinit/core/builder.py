from pathlib import Path

import click
from infinit.core import templates

def build(name, folders=None, files=None, template=None):
    if not any([folders, files, template]):
        template = "basic"
    
    project_path = Path(name)
    project_path.mkdir(exist_ok=True)
    
    # Handle template
    if template:
        if template not in templates.TEMPLATES:
            click.echo(f"[!] Unknown template: {template}")
            return

        click.echo(f"[+] Using template: {template}")
        config = templates.TEMPLATES.get(template, {})
        folders = config.get("folders", [])
        files = config.get("files", {})
    
    # Create folders
    if folders:
        if isinstance(folders, str):
            folders = [f.strip() for f in folders.split(",")]
        for folder in folders:
            (project_path / folder).mkdir(parents=True, exist_ok=True)
            click.echo(f"[+] Created: {name}/{folder}")
    
    # Create files
    if files:
        if isinstance(files, str):
            files = dict(pair.split(":", 1) for pair in files.split("|"))
        for path, content in files.items():
            try:
                full_path = project_path / path
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.write_text(content.format(name=name))
                click.echo(f"[+] Created: {name}/{path}")
            except Exception as e:
                click.echo(f"[!] Failed to create {path}: {e}")
    click.echo(f"[+] Project `{name}` is created")