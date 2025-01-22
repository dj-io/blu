import os
import json
from apollo.utils.config import load_config, save_config, cache_username
from halo import Halo

def gh_add():
  
  spinner = Halo(spinner="dots")
        
  # Load configuration
  config = load_config()
    
  # Ensure username exists
  cache_username(config)
    
  spinner.info(f"This is a developing command, it will allow you to push an existing directory to a remote repo in github stay tuned {config["github_username"]}")
    
