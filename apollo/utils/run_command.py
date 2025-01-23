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
            text=True,
            capture_output=True
        )
        spinner.succeed(f"{start} - Completed successfully.")
        
        # Display the standard output
        if result.stdout:
            print(result.stdout.strip())
        return result.stdout
    except subprocess.CalledProcessError as e:
        spinner.fail(f"{start} - Failed with error: ")
        
        if e.stdout or e.stderr:
            spinner.fail("\n".join(output.strip() for output in [e.stdout, e.stderr] if output))
        exit(1)