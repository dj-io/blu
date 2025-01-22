import subprocess
from halo import Halo

# Helper function to run shell commands
def run_command(command, cwd=None, start="Process"):
    
    spinner = Halo(spinner="dots")
    """Run shell commands and display output."""
    try:
        spinner.start(start)
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
        )
        
        # Decode the output for the spinner
        stdout_message = result.stdout.decode("utf-8").strip()
        spinner.succeed(f"{start} - Completed successfully.")
        
        if stdout_message:
            print(stdout_message)  # Optionally, display the command output
        return stdout_message
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.decode("utf-8").strip()
        spinner.fail(f"{start} - Failed with error: {error_message}")
        exit(1)