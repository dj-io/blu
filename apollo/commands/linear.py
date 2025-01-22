from apollo.utils.config import load_config, cache_username
from halo import Halo

def linear():
    
    spinner = Halo(spinner="dots")
        
    config = load_config()
    cache_username(config)
    
    spinner.info(f"This is a developing command, It will look through a given file or directory and create issues or projects in linear based on the context of the file(s) {config["github_username"]}")