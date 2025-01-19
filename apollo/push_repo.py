import os
import json
import subprocess
import questionary

def push_repo():
        
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
    
    print(f"This is a developing command, it will allow you to push an existing directory to a remote repo in github stay tuned {get_github_username()}")
    
