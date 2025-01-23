from apollo.utils.run_command import run_command
from apollo.utils.config import load_config, cache_apollo_path
from halo import Halo
import os
import subprocess

def build():
    
    config = load_config()

    # ensure apollo path has been set
    cache_apollo_path(config)
    
    # run pwd from project dir to update path
    APOLLO_PATH = config["apollo_path"]
    
    # run pwd from project dir to update path in .config file 
    REQUIREMENTS_FILE = os.path.join(APOLLO_PATH, "requirements.txt")
    
    spinner = Halo(spinner="dots")

    if os.path.exists(REQUIREMENTS_FILE):
        try:
            run_command(f"pip3 install -r {REQUIREMENTS_FILE}", APOLLO_PATH, start="Checking for dependencies...")
            spinner.succeed("requirements.txt found. Installing dependencies...")
        except subprocess.CalledProcessError as e:
            spinner.fail(f"Failed to install dependencies: {e.stderr}")
            return
        
    """Clean and rebuild the package (developer only)."""
    while True:
        try:
            run_command("rm -rf dist/ build/ *.egg-info", APOLLO_PATH, start="Cleaning up old build artifacts...")
            spinner.succeed("Old build artifacts cleaned up.")
            
            run_command("python3 -m build", APOLLO_PATH, start="Building the package...")
            spinner.succeed("Package built successfully.")
            
            run_command("pip3 install dist/*.whl --force-reinstall", APOLLO_PATH, start="Installing locally for testing...")
            spinner.succeed("Package installed locally for testing.")
            
            spinner.succeed("Build completed successfully! 🎉")
            spinner.info("Ok to Test your local changes...")
            break
        except subprocess.CalledProcessError as e:
            spinner.fail(f"Build failed with error: {e.stderr}")
            retry = input("Would you like to fix the issue and retry? (yes/no): ").strip().lower()
            if retry == "yes":
                spinner.start("Waiting for fixes... Please resolve the issues before retrying.")
                spinner.stop()
            else:
                spinner.fail("Exiting build process.")
                break
                
        
