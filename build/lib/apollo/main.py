import click
from apollo.create_repo import create_repo  # Import subcommands

@click.group()
def apollo():
    """Apollo CLI Tool - A multi-command GitHub management tool."""
    pass

# Add subcommands to the CLI
apollo.command("create repo")(create_repo)

if __name__ == "__main__":
    apollo()