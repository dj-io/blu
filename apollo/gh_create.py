import os
import json 
import questionary
from apollo.utils import run_command


def gh_create():
    
    
    CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config", "apollo")
    CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

    DEFAULT_CONFIG = {
        "github_username": None,
        "cached_directories": []
    }


    def load_config():
        if not os.path.exists(CONFIG_FILE):
            save_config(DEFAULT_CONFIG)
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)

    def save_config(config):
        """Save the configuration to the file."""
        # Ensure the config directory exists
        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)
            

    config = load_config()

    def get_subdirectories(base_path):
        """
        Recursively get all subdirectories within the base path until no further subdirectories exist
        or the user selects the current directory. Excludes .git directories.
        """
        subdirectories = {}
        try:
            # Only walk through one level at a time
            for directory in os.listdir(base_path):
                if directory == ".git":  # Skip .git directories
                    continue
                full_path = os.path.join(base_path, directory)
                if os.path.isdir(full_path):  # Only include directories
                    subdirectories[directory] = full_path
        except Exception as e:
            print(f"Error reading directories in '{base_path}': {e}")
            exit(1)

        return subdirectories

    def detect_directory():
        """
        Detect the directory to use for creating a local repository.
        Prioritizes the Developer folder and its subdirectories.
        """
        home_directory = os.path.expanduser("~")
        default_developer_path = os.path.join(home_directory, "Developer")

        def handle_subdirectories(base_path):
            """
            Handle subdirectories within a given base path.
            """
            while True:
                subdirectories = get_subdirectories(base_path)
                if not subdirectories:
                    print(f"No subdirectories found. Using '{base_path}' as the directory for the local repository.")
                    return base_path

                directory_choice = questionary.select(
                    "Select a subdirectory to use or create a new one:",
                    choices=list(subdirectories.keys()) + ["Use Current Directory", "Create a New Directory"],
                ).ask()

                if directory_choice == "Use Current Directory":
                    print(f"Using '{base_path}' as the directory for the local repository.")
                    return base_path
                elif directory_choice == "Create a New Directory":
                    new_directory = questionary.path("Enter the path for the new directory:").ask()
                    if not os.path.exists(new_directory):
                        os.makedirs(new_directory)
                        print(f"Created new directory: {new_directory}")
                    return new_directory
                else:
                    # Navigate into the selected subdirectory
                    base_path = subdirectories[directory_choice]

        # Prioritize the Developer directory
        if os.path.exists(default_developer_path):
            use_developer = questionary.confirm(
                f"A 'Developer' directory exists at {default_developer_path}. Would you like to use it to create your local repo?"
            ).ask()

            if use_developer:
                return handle_subdirectories(default_developer_path)

        # Offer to create the Developer directory if it doesn’t exist
        if not os.path.exists(default_developer_path):
            create_folder = questionary.confirm(
                f"A 'Developer' folder does not exist. Would you like to create one? You can house all future projects here."
            ).ask()

            if create_folder:
                os.makedirs(default_developer_path)
                print(f"Created 'Developer' folder at: {default_developer_path}")
                return default_developer_path

        print("Falling back to detecting subdirectories in the home directory...")
        return handle_subdirectories(home_directory)

            
    def confirm_or_select_directory():
        
        """Confirm the Developer folder or prompt the user to select a different directory."""
        
        if config["cached_directories"]:
            directory_choice = questionary.select(
                "Select a directory to use for creating the repository:",
                choices=config["cached_directories"] + ["Use Current Directory","Use Different Directory"],
            ).ask()

            if directory_choice == "Use Current Directory":
                # Set parent_dir to the current working directory
                parent_dir = os.getcwd()
                print(f"Using the current directory as the parent directory: {parent_dir}")
                
                return parent_dir
            elif directory_choice == "Use Different Directory":
                # Go through automatic directory detection logic
                parent_dir = detect_directory()
                return parent_dir
            else:
                parent_dir = directory_choice
                print(f"Using saved directory: {parent_dir}")
                return parent_dir
        else:
            use_current_dir = questionary.confirm(
                "Would you like to use the current directory as the parent directory?"
            ).ask()

            if use_current_dir:
                # Set parent_dir to the current working directory
                parent_dir = os.getcwd()
                print(f"Using the current directory as the parent directory: {parent_dir}")
                return parent_dir
            else:
                # No cached directories, go through automatic directory detection logic
                parent_dir = detect_directory()
                return parent_dir

    # cache the GitHub username in .config dir (creates apollo dir/config.json)
    def cache_username(config):
        if not config["github_username"]:
            github_username = questionary.text(
                "Enter your GitHub username:"
            ).ask()

            if github_username:
                config["github_username"] = github_username.strip()
                save_config(config)
                print(f"GitHub username '{github_username}' saved for future use.")
        else:
            print(f"Using cached GitHub username: {config['github_username']}")
    
    def save_directory_prompt(config, directory):
        """Prompt user to save the directory for future use."""
        save_dir = questionary.confirm(
            f"Would you like to save '{directory}' for future use?"
        ).ask()
        
        if save_dir:
            if directory not in config["cached_directories"]:
                config["cached_directories"].append(directory)
                save_config(config)
                print(f"Directory '{directory}' saved.")



    BASE_PATH = confirm_or_select_directory()
    BASE_PATH_OPTIONS = get_subdirectories(BASE_PATH)
    
    # Ensure github username is cached
    cache_username(config)
    github_username = config["github_username"]

        
    """Create a new GitHub repository."""
    
    # Prompt for repository details
    
    repo_name = input("Enter the name of the repository: ").strip()
    repo_description = input("Enter a description for the repository: ").strip()
    private = input("Should the repository be private? (yes/no): ").strip().lower() == "yes"

    # Create the GitHub repository using the CLI
    visibility = "private" if private else "public"
    
    print("Creating repository on GitHub using GitHub CLI...")
    run_command(f"gh repo create {repo_name} --{visibility} --description '{repo_description}' --confirm")

    # Check if BASE_PATH_OPTIONS is a dictionary and handle subdirectories
    
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
        print(f"No subdirectories found. ")
        print(f"Using the current directory. {BASE_PATH}")
        parent_dir = BASE_PATH
    
    # Full path to the local repository directory
    full_local_dir = os.path.join(parent_dir, repo_name)

    # Create the parent directory if it doesn't exist
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
        print(f"Parent directory '{parent_dir}' created.")

    # Create the repository directory if it doesn't exist
    if not os.path.exists(full_local_dir):
        os.makedirs(full_local_dir)
        print(f"Directory '{full_local_dir}' created.")
    else:
        print(f"Directory '{full_local_dir}' already exists. Proceeding...")

    # Write the README.md file
    readme_path = os.path.join(full_local_dir, "README.md")
    
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {repo_name}\n\n{repo_description}")
    print(f"README.md created in '{full_local_dir}'.")

    # Initialize the repository and commit
    print("Initializing Git repository...")
    run_command("git init", cwd=full_local_dir)

    print("Staging README.md...")
    run_command("git add README.md", cwd=full_local_dir)

    print('Committing with message "initializing repo with README"...')
    run_command('git commit -m "initializing repo with README"', cwd=full_local_dir)

    print("Renaming default branch to 'main'...")
    run_command("git branch -M main", cwd=full_local_dir)

    # Add remote origin and push
    git_url = f"https://github.com/{github_username}/{repo_name}.git"  # Adjust if using SSH
    
    print(f"Adding remote origin: {git_url}...")
    run_command(f"git remote add origin {git_url}", cwd=full_local_dir)

    print("Pushing to remote repository...")
    run_command("git push -u origin main", cwd=full_local_dir)

    print("Repository successfully created and pushed!")
    
    # Prompt to save the directory
    save_directory_prompt(config, parent_dir)