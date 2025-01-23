# Changelog


## Release Notes
# Changelog

---

## [1.1.0-beta] - 2025-01-21

### Added
- **Spinner Integration:** Introduced terminal spinners using the `halo` library to enhance user experience during command executions.
- **Environment Management:** Added support for `.env.dev` and `.env.prod` files to streamline configuration for developer and production modes.
- **Token Management:** Implemented token management for PyPI deployments, allowing secure updates for TestPyPI and ProdPyPI tokens directly in the CLI.
- **Change Logs in Deployment:** Integrated a prompt to accept release notes or changelogs during deployments. Automatically appends entries to a `CHANGELOG.md` file if provided.
- **Authentication Controls:** Restricted deployment access by validating against a list of allowed users in the configuration file (`allowed_users`).

### Changed
- **Deploy Command Enhancements:** Added robust prompts for deployment environments (TestPyPI/ProdPyPI) and ensured seamless transitions between them.
- **Improved Developer Mode:** Enhanced developer mode workflows, including automated setup instructions and build commands tailored for development environments.
- **Refactored `run_command`:** Updated to use spinners for better visibility of ongoing processes.

### Fixed
- **Error Handling:** Resolved spinner hangs when handling errors during token updates.
- **Configuration Sync:** Ensured the `load_config` function dynamically updates existing configurations when new keys are introduced to the default config.

---

## [1.0.0] - 2025-01-14

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
