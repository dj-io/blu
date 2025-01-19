import os
import json
import subprocess
import questionary


def create_repo():
    
    CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config", "apollo")
    CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

    def get_github_username():
        """Retrieve the GitHub username from the config file or prompt the user to enter it."""
        # Ensure the config directory exists
        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)

        # If the config file exists, load and return the GitHub username
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                if "github_username" in config:
                    print(f"Loaded GitHub username: {config['github_username']}")
                    return config["github_username"]

        # Otherwise, prompt the user to enter their GitHub username
        github_username = input("Enter the GitHub account username: ").strip()

        # Save the username to the config file
        with open(CONFIG_FILE, "w") as f:
            json.dump({"github_username": github_username}, f)
            print(f"Saved GitHub username to {CONFIG_FILE}")

        return github_username

    def confirm_or_select_directory():
        """Confirm the Developer folder or prompt the user to select a different directory."""
        
        # Step 1: Ask if the user wants to use the current directory
        use_current_dir = questionary.confirm(
            "Would you like to use the current directory as the parent directory?"
        ).ask()

        if use_current_dir:
            # Set parent_dir to the current working directory
            parent_dir = os.getcwd()
            print(f"Using the current directory as the parent directory: {parent_dir}")
            
            return parent_dir
        
        # Step 2: Proceed with Developer directory logic if not using current_dir
        
        # Default Developer folder path in the user's home directory
        home_directory = os.path.expanduser("~")
        default_developer_path = os.path.join(home_directory, "Developer")

        # Check if the Developer folder exists
        if os.path.exists(default_developer_path):
            # If it exists, ask the user if they want to use it
            use_developer = questionary.confirm(
                f"A 'Developer' directory exists at {default_developer_path}. Would you like to use it to create your local repo?"
            ).ask()

            if use_developer:
                return default_developer_path  # Use the existing Developer folder

        # If it doesn't exist or the user doesn't want to use it, prompt for an alternative
        if not os.path.exists(default_developer_path):
            create_folder = questionary.confirm(
                f"A 'Developer' folder does not exist. Would you like to create one? You can house all future projects here."
            ).ask()

            if create_folder:
                os.makedirs(default_developer_path)
                print(f"Created 'Developer' folder at: {default_developer_path}")
                return default_developer_path
        
        # Present an options menu to choose from subdirectories under the home directory
        print("Detecting subdirectories in the home directory...")
        subdirectories = get_subdirectories(home_directory)
        
        if not subdirectories:
            # No subdirectories found, prompt the user to select or create a path
            selected_path = questionary.path(
                "No subdirectories found. Please select or create a directory to use as your base path:"
            ).ask()

            # If the selected directory does not exist, create it
            if not os.path.exists(selected_path):
                os.makedirs(selected_path)
                print(f"Created selected directory: {selected_path}")

            return selected_path
        
        # If subdirectories are found, present them in a menu
        directory_choice = questionary.select(
            "Please select a subdirectory to use or create a new one:",
            choices=list(subdirectories.keys()) + ["Create a new directory"],
        ).ask()

        if directory_choice == "Create a new directory":
            selected_path = questionary.path("Enter the path for the new directory:").ask()

            # If the selected directory does not exist, create it
            if not os.path.exists(selected_path):
                os.makedirs(selected_path)
                print(f"Created new directory: {selected_path}")

            return selected_path

        # Use the selected subdirectory
        return subdirectories[directory_choice]


    def get_subdirectories(base_path):
        """Get a dictionary of subdirectories within the base path."""
        subdirectories = {}
        
        try:
            for item in os.listdir(base_path):
                item_path = os.path.join(base_path, item)
                if os.path.isdir(item_path):  # Only include directories
                    subdirectories[item] = item_path
        except Exception as e:
            print(f"Error reading directories in '{base_path}': {e}")
            exit(1)
            
        return subdirectories


    BASE_PATH = confirm_or_select_directory()

    # Dynamically populate BASE_PATH_OPTIONS
    BASE_PATH_OPTIONS = get_subdirectories(BASE_PATH)


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
        
    """Create a new GitHub repository."""
    
    # Step 1: Prompt for repository details
    github_username = get_github_username()
    
    repo_name = input("Enter the name of the repository: ").strip()
    # gh_name = input("Enter the github account username: ").strip()
    repo_description = input("Enter a description for the repository: ").strip()
    private = input("Should the repository be private? (yes/no): ").strip().lower() == "yes"

    # Step 2: Create the GitHub repository using the CLI
    visibility = "private" if private else "public"
    
    print("Creating repository on GitHub using GitHub CLI...")
    run_command(f"gh repo create {repo_name} --{visibility} --description '{repo_description}' --confirm")

    # Step 3: Check if BASE_PATH_OPTIONS is a dictionary and handle subdirectories
    
    if isinstance(BASE_PATH_OPTIONS, dict) and BASE_PATH_OPTIONS:
        # Present the subdirectory choices, with a fallback option to create a new directory
        directory_choice = questionary.select(
            "Select a directory to use or create a new one:",
            choices=list(BASE_PATH_OPTIONS.keys()) + ["Use Selected Directory", "Create a new directory"],
        ).ask()

        if directory_choice == "Create a new directory":
            selected_path = questionary.path("Enter the path for the new directory:").ask()

            # If the selected directory does not exist, create it
            if not os.path.exists(selected_path):
                os.makedirs(selected_path)
                print(f"Created new directory: {selected_path}")

            parent_dir = selected_path

        elif directory_choice == "Use Selected Directory":
            parent_dir = BASE_PATH
            
        else:
            # Use the selected subdirectory
            parent_dir = BASE_PATH_OPTIONS[directory_choice]
    else:
        # No subdirectories present, set the parent directory to the current directory
        print(f"No subdirectories found. Using the current directory. {BASE_PATH}")
        parent_dir = BASE_PATH


    # Full path to the local repository directory
    full_local_dir = os.path.join(parent_dir, repo_name)

    # Step 4: Create the parent directory if it doesn't exist
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
        print(f"Parent directory '{parent_dir}' created.")

    # Create the repository directory if it doesn't exist
    if not os.path.exists(full_local_dir):
        os.makedirs(full_local_dir)
        print(f"Directory '{full_local_dir}' created.")
    else:
        print(f"Directory '{full_local_dir}' already exists. Proceeding...")

    # Step 5: Write the README.md file
    readme_path = os.path.join(full_local_dir, "README.md")
    
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {repo_name}\n\n{repo_description}")
    print(f"README.md created in '{full_local_dir}'.")

    # Step 6: Initialize the repository and commit
    print("Initializing Git repository...")
    run_command("git init", cwd=full_local_dir)

    print("Staging README.md...")
    run_command("git add README.md", cwd=full_local_dir)

    print('Committing with message "initializing repo with README"...')
    run_command('git commit -m "initializing repo with README"', cwd=full_local_dir)

    print("Renaming default branch to 'main'...")
    run_command("git branch -M main", cwd=full_local_dir)

    # Step 7: Add remote origin and push
    git_url = f"https://github.com/{github_username}/{repo_name}.git"  # Adjust if using SSH
    
    print(f"Adding remote origin: {git_url}...")
    run_command(f"git remote add origin {git_url}", cwd=full_local_dir)

    print("Pushing to remote repository...")
    run_command("git push -u origin main", cwd=full_local_dir)

    print("Repository successfully created and pushed!")