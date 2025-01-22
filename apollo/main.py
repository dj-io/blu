import click
import os
from dotenv import load_dotenv

from apollo.commands.gh_create import gh_create  # Import subcommands
from apollo.commands.gh_add import gh_add
from apollo.commands.build import build
from apollo.commands.deploy import deploy
from apollo.commands.linear import linear

# Load the environment variables
env_file = ".env.dev" if os.getenv("ENV") == "dev" else ".env.prod"
load_dotenv(env_file)

@click.group()
def apollo():
   """Apollo CLI - An AI-powered CLI designed to streamline DevOps and project management workflows through automation. 

   CREATE REPO
   
   Username: Your Github Account username automatically gets cached into a global .config after you enter it
   
   Update username: in terminal open the .config file in an editor and update the username {"github_username": "update-here"}
   Delete Repositories: in terminal open the .config file in an editor and update the cached_directories array [User/username/path]

    Automation tools: File management, GitHub actions, API integrations.
    Data utilities: Data extraction, transformation, and visualization.
    Task scheduling: Automate recurring workflows like backups and log parsing.
    """
pass

# Access APOLLO_DEV_MODE
if os.getenv("APOLLO_DEV_MODE") == "1":
    print("Developer mode enabled.")
    
    apollo.command("build", help="ReBuild a develop version of this package")(build)
    apollo.command("deploy", help="Distribute this package to Pypi, use --test or --prod to choose environment")(deploy)


# Add subcommands to the CLI
apollo.command("gh-create", help="Create a new github Repository")(gh_create)
apollo.command("gh-add", help="Push an existing directory to a remote repository in github")(gh_add)
apollo.command("linear", help="Generate issues & projects within your linear workspace, based on the contents of a file or directory...")(linear)

# Add future commands here
# apollo.command("data-utils")(data_utils)
# apollo.command("schedule-task")(schedule_task)

if __name__ == "__main__":
    apollo()