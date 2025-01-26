<h1 align="center"> 📜 Change Log </h1>

<h3 align="center"> [1.1.0-beta] - 2025-01-21 </h3>

### Added
- **Bulk Delete**: Implemented the gh_delete Command to delete GitHub repositories. Supports single or bulk deletion.. 
- **Spinner Integration:** Introduced terminal spinners using the `halo` library to enhance user experience during command executions.
- **Environment Management:** Added support for `.env.dev` and `.env.prod` files to streamline configuration for developer and production modes.
- **Change Logs in Deployment:** Integrated a prompt to accept release notes or changelogs during deployments. Automatically appends entries to a `CHANGELOG.md` file if provided.
- **Authentication Controls:** Restricted deployment access by validating against a list of allowed users in the configuration file (`allowed_users`).
- **Enhanced `.pypirc` Validation:** Automatically detects the `.pypirc` file, verifies its validity, and prompts users to create or update it with proper credentials for TestPyPI and ProdPyPI if missing.
- **Automated Version Incrementing**: Added logic to the deploy command to automatically increment the major, minor, or patch version in setup.py based on a specified flag. Preserves other version components during updates and initializes the version if missing.
- **Sanity Check Before Deployment:** Added logic to perform a sanity check (`twine check`) on built packages before uploading them to ensure no build errors. Generates logs if issues are detected.
- **Command Workflow Enhancements:** Updated various commands to cache gh auth responses for improved performance, reducing repetitive checks during operations like repository deletion or addition.
- **gh_add Command:** Command to push an existing local repository to a remote GitHub repository.
	- Single/Custom Directory Support: Prompts the user to confirm if the current directory should be used or locate another existing repository using locate_local_repo which automatically finds a corresponding repository.
	- Remote Repository Detection: Automatically detects if a remote repository with the same name exists on GitHub. If no matching repository is found, prompts the user to create a new remote repository.
	- Git Repository Validation: Ensures the directory is a Git repository. If not, it initializes Git, sets up .gitignore (creating it if necessary), and adds untracked files.
	- Upstream Configuration: Checks if an upstream branch is already configured for the local repository. If not, prompts to set one up and links the repository to the detected or newly created remote.
- **clean-up command:** Clean up and fix linting issues in the Apollo codebase.
	- Identify and resolve Python linting issues within the codebase.
	- Supports automatic code formatting using Flake8 and Black.
	- Allows users to provide a specific path (file or directory) using the --path flag, or defaults to the entire project if no path is provided.
	- Detects linting issues, resolves them, and provides a summary of remaining issues (if any).


### Changed
- **Deploy Command Enhancements:** Added robust prompts for deployment environments (TestPyPI/ProdPyPI) and ensured seamless transitions between them.
- **Improved Developer Mode:** Enhanced developer mode workflows, including automated setup instructions and build commands tailored for development environments.
- **Refactored `run_command`:** Updated to use spinners and log output for errors for better visibility of ongoing processes.
- **Verbose Output for Deploys:** Enabled verbose flag in deployment commands for more transparent feedback, regardless of success or failure.
- **Directory Detection**: Now works in two ways, one implementation handles guided directory detection, added full unguided directory detection (Locates a local repository based on a provided name)
- **--help**: Improved help menus, included -h and further command detail for all available commands

### Fixed
- **Error Handling:** Resolved spinner hangs when handling errors during token updates.
- **Configuration Sync:** Ensured the `load_config` function dynamically updates existing configurations when new keys are introduced to the default config.

### Removed
- **Token Management:** Implemented token management for PyPI deployments, allowing secure updates for TestPyPI and ProdPyPI tokens directly in the CLI.

---

<h3 align="center"> [1.0.0-beta] - 2025-01-14 </h3>

### Added
- **GitHub Repository Management:**
  - Introduced `apollo gh-create` for creating new repositories with interactive prompts.
  - Added support for caching GitHub usernames and directories for future use.
- **Directory Navigation Tools:** Included logic for automatic directory detection, subdirectory navigation, and creating new directories.
- **Build Command:** Added the `apollo build` command for cleaning and rebuilding the package, with dependency installation based on `requirements.txt`.
- **Deployment Command:** Enabled deployments to TestPyPI and ProdPyPI through the `apollo deploy` command.

### Changed
- **Command-Line Interaction:** Adopted the `Click` library for handling CLI commands and options, ensuring a more intuitive developer experience.
- **Directory Caching:** Improved directory management by introducing prompts to save frequently used paths in the configuration file.

### Fixed
- **Subdirectory Infinite Loops:** Resolved issues where infinite loops occurred during directory traversal.
- **Token Environment Variables:** Fixed missing environment variable errors by ensuring secure token storage for PyPI deployments.

### Removed
- **Legacy Path Handling:** Removed hardcoded paths and replaced them with dynamic configurations.

---
