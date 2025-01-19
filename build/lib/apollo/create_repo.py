import os
import subprocess
import questionary



def create_repo():
    
    BASE_PATH = "/Users/dj/Developer"

    BASE_PATH_OPTIONS = {
        "dj-labs": {
            "Engineering Directory": f"{BASE_PATH}/dj-labs/development",
            "Development Directory": f"{BASE_PATH}/dj-labs/engineering", 
            "Research Directory": f"{BASE_PATH}/dj-labs/research",
        },
        "stratum-labs": f"{BASE_PATH}/stratum-labs",
    }
    # Helper function to run shell commands
    def run_command(command, cwd=None):
        """Run shell commands and display output."""
        try:
            result = subprocess.run(command, shell=True, cwd=cwd, check=True, text=True, capture_output=True)
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")
            exit(1)

    # Step 1: Prompt for repository details
    repo_name = input("Enter the name of the repository: ").strip()
    repo_description = input("Enter a description for the repository: ").strip()
    private = input("Should the repository be private? (yes/no): ").strip().lower() == "yes"

    # Step 2: Create the GitHub repository using the CLI
    visibility = "private" if private else "public"
    print("Creating repository on GitHub using GitHub CLI...")
    run_command(f"gh repo create {repo_name} --{visibility} --description '{repo_description}' --confirm")

    # Step 3: Select the parent directory group
    group_choice = questionary.select(
        "Which directory group would you like to use?",
        choices=list(BASE_PATH_OPTIONS.keys()),
    ).ask()

    # Step 4: Handle directory selection within the chosen group
    if isinstance(BASE_PATH_OPTIONS[group_choice], dict):
        # If the selected group contains multiple directories, show another menu
        directory_choice = questionary.select(
            f"Select a directory in '{group_choice}':",
            choices=list(BASE_PATH_OPTIONS[group_choice].keys()),
        ).ask()
        
        parent_dir = BASE_PATH_OPTIONS[group_choice][directory_choice]
    else:
        # If the selected group is a single directory
        parent_dir = BASE_PATH_OPTIONS[group_choice]

    # Full path to the local repository directory
    full_local_dir = os.path.join(parent_dir, repo_name)

    # Step 5: Create the parent directory if it doesn't exist
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
        print(f"Parent directory '{parent_dir}' created.")

    # Create the repository directory if it doesn't exist
    if not os.path.exists(full_local_dir):
        os.makedirs(full_local_dir)
        print(f"Directory '{full_local_dir}' created.")
    else:
        print(f"Directory '{full_local_dir}' already exists. Proceeding...")

    # Step 6: Write the README.md file
    readme_path = os.path.join(full_local_dir, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {repo_name}\n\n{repo_description}")
    print(f"README.md created in '{full_local_dir}'.")

    # Step 7: Initialize the repository and commit
    print("Initializing Git repository...")
    run_command("git init", cwd=full_local_dir)

    print("Staging README.md...")
    run_command("git add README.md", cwd=full_local_dir)

    print('Committing with message "initializing repo with README"...')
    run_command('git commit -m "initializing repo with README"', cwd=full_local_dir)

    print("Renaming default branch to 'main'...")
    run_command("git branch -M main", cwd=full_local_dir)

    # Step 8: Add remote origin and push
    git_url = f"https://github.com/dj-io/{repo_name}.git"  # Adjust if using SSH

    print(f"Adding remote origin: {git_url}...")
    run_command(f"git remote add origin {git_url}", cwd=full_local_dir)

    print("Pushing to remote repository...")
    run_command("git push -u origin main", cwd=full_local_dir)

    print("Repository successfully created and pushed!")