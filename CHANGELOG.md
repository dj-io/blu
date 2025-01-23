<h1 align="center"> 📜 Change Log </h1>

<h3 align="center"> [1.1.0-beta] - 2025-01-21 </h3>

### Added
- **Spinner Integration:** Introduced terminal spinners using the `halo` library to enhance user experience during command executions.
- **Environment Management:** Added support for `.env.dev` and `.env.prod` files to streamline configuration for developer and production modes.
- **Change Logs in Deployment:** Integrated a prompt to accept release notes or changelogs during deployments. Automatically appends entries to a `CHANGELOG.md` file if provided.
- **Authentication Controls:** Restricted deployment access by validating against a list of allowed users in the configuration file (`allowed_users`).
- **Enhanced `.pypirc` Validation:** Automatically detects the `.pypirc` file, verifies its validity, and prompts users to create or update it with proper credentials for TestPyPI and ProdPyPI if missing.
- **Automated Version Incrementing**: Added logic to the deploy command to automatically increment the major, minor, or patch version in setup.py based on a specified flag. Preserves other version components during updates and initializes the version if missing.
- **Sanity Check Before Deployment:** Added logic to perform a sanity check (`twine check`) on built packages before uploading them to ensure no build errors. Generates logs if issues are detected.

### Changed
- **Deploy Command Enhancements:** Added robust prompts for deployment environments (TestPyPI/ProdPyPI) and ensured seamless transitions between them.
- **Improved Developer Mode:** Enhanced developer mode workflows, including automated setup instructions and build commands tailored for development environments.
- **Refactored `run_command`:** Updated to use spinners and log output for errors for better visibility of ongoing processes.
- **Verbose Output for Deploys:** Enabled verbose flag in deployment commands for more transparent feedback, regardless of success or failure.

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
