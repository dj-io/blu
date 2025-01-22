import os
import questionary
import click
import getpass
from apollo.utils.run_command import run_command
from apollo.utils.config import load_allowed_users, cache_apollo_path, load_config
from halo import Halo

@click.option("--test", is_flag=True, help="Push the package to TestPyPI.")
@click.option("--prod", is_flag=True, help="Push the package to Prod PyPI.")
def deploy(test, prod):
    """
    Package and push the project to PyPI or TestPyPI.
    Use --test to push to TestPyPI, or --prod to push to Prod PyPI.
    """
    
    spinner = Halo(spinner="dots")

    """Prevent Unauthorized deployments."""
    username = getpass.getuser()
    allowed_users = load_allowed_users() 
    
    if username not in allowed_users:
        spinner.fail(f"Unauthorized user: {username}.")
        spinner.info(f"Only maintainers can deploy this package")
        exit(1)
        
    config = load_config()

    # ensure apollo path has been set
    cache_apollo_path(config)
    
    # run pwd from project dir to update path
    APOLLO_PATH = config["apollo_path"]
    
    # Determine the environment
    env_choice = "TestPyPI" if test else "Prod PyPI"
    token_env_var = "TEST_PYPI_TOKEN" if test else "PYPI_TOKEN"
    
    #pre-step: confirm tokens exist, enable token updates
    token = os.getenv(token_env_var)
    
    
    if not token:
        spinner.fail(f"No {env_choice} token found.")
        
        update_token = questionary.confirm(
            f"Would you like to set or update your {env_choice} token now?"
        ).ask()
        
        if update_token:
            manage_tokens_logic()
            token = os.getenv(token_env_var)
            if not token:
                spinner.fail(f"Error: {env_choice} token still not set. Aborting...")
                return
        else:
            spinner.fail("Aborting...")
            return
        
    spinner.succeed(f"token found in env variables")
    
    def manage_tokens_logic():
        """Logic to manage tokens (add, update, or delete)."""
        spinner.start("Managing authentication tokens...")

        # Step 1: Prompt to update tokens for TestPyPI and Prod PyPI
        update_test_token = questionary.confirm("Would you like to update your TestPyPI token?").ask()
        
        if update_test_token:
            test_token = questionary.text("Enter your new TestPyPI token:").ask()
            
            if test_token.strip():
                os.environ["TEST_PYPI_TOKEN"] = test_token.strip()
                spinner.succeed("TestPyPI token updated successfully.")

        update_prod_token = questionary.confirm("Would you like to update your Prod PyPI token?").ask()
        
        if update_prod_token:
            prod_token = questionary.text("Enter your new Prod PyPI token:").ask()
            
            if prod_token.strip():
                os.environ["PYPI_TOKEN"] = prod_token.strip()
                spinner.succeed("Prod PyPI token updated successfully.")

        spinner.info("Token management complete.")
    
    """Package and push the project to PyPI or TestPyPI."""

    # Step 1: Confirm the environment
    confirm_push = questionary.confirm(
        f"Are you sure you want to push to {env_choice}?"
    ).ask()

    if not confirm_push:
        spinner.fail("Aborting...")
        return

    # Step 2: Prompt the user for a changelog or release notes
    release_notes = questionary.text(
        "Enter release notes or changelog for this version (leave blank to skip):"
    ).ask()

   # Step 3: Ensure CHANGELOG.md exists and write release notes
    if release_notes.strip():
        changelog_path = "CHANGELOG.md"
        
        if not os.path.exists(changelog_path):
            with open(changelog_path, "w") as changelog_file:
                changelog_file.write("# Changelog\n\n")
            spinner.succeed(f"Created {changelog_path}.")
        
        with open(changelog_path, "a") as changelog_file:
            changelog_file.write(f"\n## Release Notes\n{release_notes.strip()}\n")
        spinner.info("Release notes appended to CHANGELOG.md.")

    # Step 4: Build the package
    os.environ["ENV"] = "prod"
    spinner.info(f"Environment variable 'ENV' set to 'prod'.")
    
    # print("Cleaning previous build artifacts...")
    run_command("rm -rf dist/ build/ *.egg-info", APOLLO_PATH, start="Cleaning previous build artifacts...")

    # print("Building the package...")
    run_command("python setup.py sdist bdist_wheel", APOLLO_PATH, start="Building the package...")
    

    # Step 5: Push to PyPI or TestPyPI
    repository_url = "--repository-url https://test.pypi.org/legacy/" if test else ""
    
    
    push_confirm = questionary.confirm(
        f"Proceed with uploading the package to {env_choice}?"
    ).ask()

    if not push_confirm:
        spinner.fail("Aborting...")
        return

    spinner.start(f"Pushing to {env_choice}...")
    # print(f"Using repository URL: {repository_url}") 
    run_command(f"twine upload {repository_url} dist/* -u __token__ -p {token}", APOLLO_PATH, start=f"Using repository URL: {repository_url}")

    spinner.succeed(f"Package successfully pushed to {env_choice}!")