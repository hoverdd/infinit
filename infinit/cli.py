import click
from infinit.core import builder

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name")
@click.option("-f", "--folders", help="Comma-separated folder list")
@click.option("-F", "--files", help="File:Content pairs separated by |")
@click.option("-t", "--template", help="Predefined template (basic, web)")
def create(name, folders, files, template):
    """Create project structure"""
    try:
        builder.build(name, folders=folders, files=files, template=template)
    except ValueError as e:
        click.secho(f"[!] Error: {e}", fg="red")

if __name__ == "__main__":
    cli()