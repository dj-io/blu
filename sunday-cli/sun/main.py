import click
import os
import getpass
from dotenv import load_dotenv

from sun.commands.gh_create import gh_create  # Import subcommands
from sun.commands.gh_add import gh_add
from sun.commands.gh_delete import gh_delete
from sun.commands.gh_readme import gh_readme
from sun.commands.build import build
from sun.commands.deploy import deploy
from sun.commands.linear import linear
from sun.commands.clean_up import clean_up

# Load the environment variables
env_file = ".env.dev" if os.getenv("ENV") == "dev" else ".env.prod"
load_dotenv(env_file)

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(
    context_settings=CONTEXT_SETTINGS,
    help=f"""
        Sunday CLI - An AI-powered CLI Automating the entire Software Development Lifecycle

        Specify configs in the config.json file:\n
            /Users/{getpass.getuser()}/.config/sunday

        More configuration info: sun --help config
    """,
    epilog="\nRun 'sun <command> --help, -h' for more details on a specific command.\n",
)
def sunday():
    """"""


pass

# Access SUN_DEV_MODE
if os.getenv("SUN_DEV_MODE") == "1":
    print("Developer mode enabled.")

    sunday.command("build")(build)
    sunday.command("deploy")(deploy)
    sunday.command("clean-up")(clean_up)


# Add subcommands to the CLI
sunday.command("gh-create")(gh_create)
sunday.command("gh-add")(gh_add)
sunday.command("gh-delete")(gh_delete)
sunday.command("linear")(linear)
sunday.command("gh-readme")(gh_readme)

# Add future commands here
# sunday.command("data-utils")(data_utils)
# sunday.command("schedule-task")(schedule_task)

if __name__ == "__main__":
    sunday()
