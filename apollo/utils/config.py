import os
import json
import questionary
from halo import Halo

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config", "apollo")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
DEFAULT_CONFIG = {"github_username": None, "cached_directories": [], "apollo_path": None}
spinner = Halo(spinner="dot")

def load_config():
    """Load configuration from the file or initialize default if it doesn't exist."""
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        spinner.info(f"Configuration file created at {CONFIG_FILE} with default values.")
    try:
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
            
        # Merge the loaded config with the default config to include new keys
        updated_config = { **DEFAULT_CONFIG, **config }    
        
        # If the config was updated with new keys, save it back to the file
        if config != updated_config:
            save_config(updated_config)
            spinner.info("Configuration file updated with new default keys....")
            
        return updated_config
    
    except json.JSONDecodeError:
        raise ValueError(f"Configuration file at {CONFIG_FILE} is not a valid JSON file.")


def load_allowed_users():
    """Load configuration from the file or initialize default if it doesn't exist."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
            return config.get("allowed_users", [])
    return []

    
def save_config(config):
    """Save configuration to the file."""
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def cache_username(config):
    # Cache GitHub username
    if not config["github_username"]:
        github_username = questionary.text("Enter your GitHub username:").ask()
        
        config["github_username"] = github_username.strip()
        save_config(config)
        spinner.info(f"GitHub username '{github_username}' saved for future use.")
    else:
        spinner.info(f"Using cached GitHub username: {config["github_username"]}")
        
    return config["github_username"]
        

def cache_apollo_path(config):
    # Cache apollo path
    if not config["apollo_path"]:
        APOLLO_PATH = os.getcwd()
        config["apollo_path"] = APOLLO_PATH 
        
        save_config(config)
        spinner.info(f"Apollo Path set as {APOLLO_PATH}")
    else:
        spinner.info(f"Using cached Path: '{config["apollo_path"]}'")
        
    return config["apollo_path"]