
 <h1 align="center"> BLU CLI 🌔 </h1>

<p align="center">
  <a href="https://pypi.org/project/blu-cli/0.1.0/">
    <img src="https://img.shields.io/pypi/v/blu-cli.svg" alt="PyPI Version">
  </a>
  <a href="https://github.com/dj-io/blu/blob/main/blu-cli/LICENSE">
    <img src="https://img.shields.io/github/license/dj-io/blu-cli.svg" alt="License">
  </a>
  <a href="https://github.com/dj-io/blu-cli/actions">
    <img src="https://img.shields.io/badge/Tests-Passing-brightgreen" alt="Build Status">
  </a>
  <!-- <a href="https://coveralls.io/github/psf/blu?branch=main"> -->
    <img src="https://img.shields.io/badge/coverage-36%25-brightgreen" alt="Coverage Status">
  <!-- </a> -->
  </a>
    <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style">
  </a>
</p>


<p align="center">
  <b>AI-Powered CLI for BLU</b>
</p>

<p align="center">
  🚀 Built with <b>Python, Click</b> and <b>Questionary</b>, The CLI handles the commands that enable users to integrate their projects with the Blu platform, every command should have the ability to take in any file or directory and scaffold project resources in convenient way.
</p>

# Table of Contents

- [Getting Started 🔑](#getting-started-🔑)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Developer Mode 🪄](#developer-mode-🪄)
    - [Setting Up Developer Mode](#setting-up-developer-mode)
    - [Using Developer Mode](#using-developer-mode)
- [General Usage 💡](#general-usage-💡️) ️
  - [Show Available Commands](#show-available-commands)
  - [Show Command Features: `blu <command> --help`](#show-command-features)
    - [Example Features](#example-features)
- [Guidelines](#guidelines)
- [Versioning](#versioning)
- [License 📜](#license-📜 )
- [Acknowledgments 🙏](#acknowledgments-🙏)


# Getting Started 🔑

### Prerequisites:

Ensure you have the following installed:

- **Python3** for running the scripts in this repo
- **Pip** pythons package manager used to install the pypi package BLU

### Installation:

1. Fork the repository.
    ```bash
    gh repo fork https://github.com/dj-io/blu.git --remote=true
    ```

2. Create a new branch to your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```

3. Commit your changes:
    ```bash
    git commit -m "Description of your changes"
    ```

4. Push to your branch:
    ```bash
    git push origin feature/your-feature-name
    ```

5. Open a pull request on Github.

### Developer Mode 🪄:

### Setting up developer mode

 >Developer mode enables additional CLI commands (e.g., blu build and blu deploy) that are not available in production. Follow these steps to configure and use developer mode:

---

**1. Create Environment Files**

  - Navigate to the root directory of the project.
  - Create .env.dev and .env.prod files based on the provided .env.sample file.

  ```bash
  cp .env.sample .env.dev
  cp .env.sample .env.prod
  ```
- Edit the .env.dev and .env.prod files with your environment-specific variables. For example:

```bash
BLU_DEV_MODE=1
```

**2. Enable Developer Mode.**
Run the following command in your terminal to enable developer mode:

  ```bash
  export ENV=dev
  ```

- This sets the ENV variable to dev for the current terminal session, which ensures the script loads .env.dev and enables developer-specific features.

### Using Developer Mode

Developer mode commands are available for contributors to streamline package development, testing, and deployment. These commands allow developers to rebuild and deploy blu.

---

**Available Commands**


1. **Build**

     Use the blu build command to rebuild the package during development. This ensures all changes to the codebase are reflected in the package. It will also install blu locally so that you can run the commands in the same fashion you would if installed via pip

    ```bash
    blu build
    ```
    - **The command includes prompts to**:
      - Cleans up old build artifacts.
      - Rebuilds the package into the dist/ directory
      - Installs the package locally for testing
      - Automatically installs missing dependencies from `requirements.txt`

2. **Deploy**
    Use the blu deploy command to package and deploy the CLI to PyPI (or TestPyPI)

    ```bash
    blu deploy
    ```
    -	The command includes prompts to:
        -	Select between TestPyPI or Prod PyPI.
        - Provide changelog or release notes.
        -	Confirm the deployment target.
        - Automatically detects the .pypirc file and verifies its validity.

    - Example

      ```bash
      blu deploy --test  # Deploy to TestPyPI
      blu deploy --prod  # Deploy to Prod PyPI
      ```

3. **Clean up**
    Use the blu clean-up command to run linting checks and automatically resolve using `flake8` and `black`

    ```bash
    blu clean-up
    ```
    -	The command includes prompts to:
        -	Confirm clean-up action if linting issues are found.
        - Traverses code base and runs black on each file with linting issues present

**Additional Notes**


  - `The deploy command is only executable with credentials provided upon request`
  - **Switching Modes**:
    - To switch back to production mode, run:
    ```bash
    export ENV=prod
    ```
    - This switch happens automatically during deployments.

  - **Ensuring a Valid** `.pypirc` **File Exists**:

    The deploy command relies on the `.pypirc` configuration file for TestPyPI and ProdPyPI deployments:

    **- Automatic Detection**
    - The CLI **automatically** detects the `.pypirc` file in your home directory **(~/.pypirc)** during deployment.

    - If the file is missing or lacks the necessary credentials for TestPyPI or ProdPyPI, the CLI will prompt you to create or update it.

    **- Structure of** .pypirc:

    Ensure your .pypirc file contains the correct repository configuration:
      ```ini
      [distutils]
      index-servers =
          pypi
          testpypi

      [pypi]
      repository = https://upload.pypi.org/legacy/
      username = __token__
      password = your-prod-token

      [testpypi]
      repository = https://test.pypi.org/legacy/
      username = __token__
      password = your-test-token
      ```

    **- Prompts for Missing Credentials**:

    - **DON'T WORRY**,	If the `.pypirc` file is incomplete (e.g., missing a repository, username, or password), the CLI will guide you through updating it!

  - Run `blu --help` in developer mode to view the full list of available commands
  -  If you modify .env.dev or .env.prod, reload your environment variables:
      ```bash
      source ~/.zshrc  # For Zsh
      source ~/.bashrc  # For Bash
      ```

## General Usage 💡

After setting up developer mode and running the build command, the blu cli is available in your terminal.

### Show Available Commands

Run the following to see a list of available commands and their descriptions:
```bash
blu --help
```

example output:
```bash
Usage: blu COMMAND [ARGS] [OPTIONS]...

Options:
  --help  Show this message and exit.

Commands:
  gh-create  Create and push a new repository to GitHub.
  gh-delete  Delete remote and local repositories, 1 by 1 or in bulk.
  gh-add     Push an existing local repository to a new GitHub repo.
```


### Show Command Features

Run the following to see a more descriptive output of commands features and usage:

```bash
blu <command> --help
```

example output:
```bash
Usage: blu gh-create [OPTIONS]

  Create a new GitHub repository and initialize it locally.

  Features:
      - Allows you to specify a repository name and description.
      - Option to choose whether the repository is public or private.
      - Automatically initializes the repository with a README.
      - Sets up a remote connection to GitHub using the GitHub CLI.


  Considerations:
      - Ensure you are authenticated with the GitHub CLI (`gh auth login`) before using this command.
      - Requires the GitHub CLI installed locally.

Options:
  -h, --help  Show this message and exit.
```

### Example Features

1. **Interactive Directory Selection**

    blu automatically detects directories and provides multiple options:

    - Use the current working directory.
    - Select an existing directory from a list.
    - Create a new directory if needed.

    **Example Prompt**:
    ```bash
    Would you like to use the current directory as the parent directory? (yes/no)
    ```

2. **Caching**

    The CLI stores information and preferences needed for use with various integrations i.e GitHub username for future use, eliminating repetitive inputs. If the username is already cached, the CLI will prompt you to reuse it.

    **Example Prompt**:
      ```bash
      Using cached GitHub username: dj-io
      ```


### Guidelines:

- Ensure your code is well-documented and adheres to **PEP 8** standards.
- Add **tests** for any new features or bug fixes.
- **Do Not Commit Sensitive Data**: Ensure .env.dev and .env.prod are excluded from version control by including them in .gitignore.
- **Testing Locally**: Use `blu build` to test changes locally before deploying to PyPI or TestPyPI.
- **Deploy Responsibly**: Always verify the environment (dev or prod) before running deployment commands to avoid accidental production deployments.

### Versioning:
Given a version number `major.minor.patch`, all:

  - Breaking backwards compatibility bumps the MAJOR
  - New additions without breaking backwards compatibility bumps the MINOR
  - Bug fixes and misc changes bump the PATCH

  **For more information on semantic versioning, please visit http://semver.org/.**


### License: 📜
Copyright Stratum Labs LLC.

This project is licensed under the Apache License. See the LICENSE file for details.

# Acknowledgments 🙏

Blu is inspired by internal tooling built to enhance software development team experience, with the intended purpose streamlining development workflows.

<!-- ### Technologies Used 📚

- `Python`: For functonality and logic processing
- `Questionary`: For interactive CLI prompts.
- `OS`: For file system operations.
- `Subprocess`: For running Git commands. -->
