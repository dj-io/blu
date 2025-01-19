import click
from apollo.create_repo import create_repo  # Import subcommands
from apollo.push_repo import push_repo

@click.group()
def apollo():
   """Apollo CLI - Tools for developer and engineer workflows.

   CREATE REPO -
   
   Username: Your Github Account username automatically gets cached into a global .config after you enter it
   
   Update username: in terminal open the .config file in an editor and update the username {"github_username": "update-here"}

    Automation tools: File management, GitHub actions, API integrations.
    Data utilities: Data extraction, transformation, and visualization.
    Task scheduling: Automate recurring workflows like backups and log parsing.
    """
pass

# Add subcommands to the CLI
apollo.command("create-repo", help="Create a new github Repository")(create_repo)
apollo.command("push_repo", help="Push an existing directory to a remote repository in github")(push_repo)

# Add future commands here
# apollo.command("data-utils")(data_utils)
# apollo.command("schedule-task")(schedule_task)

if __name__ == "__main__":
    apollo()