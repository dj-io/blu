
 <h1 align="center"> Apollo CLI 🌔 </h1>

<p align="center">
  <a href="https://pypi.org/project/apollo-o1/1.0.0/">
    <img src="https://img.shields.io/pypi/v/apollo-o1.svg" alt="PyPI Version">
  </a>
  <a href="https://github.com/dj-io/apollo-o1/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/dj-io/apollo-o1.svg" alt="License">
  </a>
    <a href="https://github.com/dj-io/apollo-o1/actions">
    <img src="https://img.shields.io/badge/Tests-Passing-brightgreen" alt="Build Status">
  </a>
</p>

Apollo-o1 CLI is a Python-based, AI Powered, command-line interface designed to enhance the Software Development Life Cycle experience by automating devOps and project management workflows. 

This tool simplifies tasks like managing source control repositories i.e Github, CI/CD i.e github actions, Project management workflows and more, allowing teams to focus on building and delivering software efficiently.

# Table of Contents

- [Features ⚙️](#-features-⚙️)
- [Getting Started 🔑](#getting-started-🔑)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage 🛠](#usage-🛠️) ️
  - [Show Available Commands](#show-available-commands)
  - [Apollo's First Script: `gh-create`](#apollos-first-script)
    - [Usage](#usage-1)
    - [Key Features](#key-features)
- [Contributing 💡](#contributing-💡)
  - [Developer Mode 🪄](#developer-mode-🪄)
    - [Setting Up Developer Mode](#setting-up-developer-mode)
    - [Using Developer Mode](#using-developer-mode)
  - [Guidelines](#guidelines)
  - [Versioning](#versioning)
- [License 📜](#license-📜 )  
- [Acknowledgments 🙏](#acknowledgments-🙏) 

# ️ Features ⚙️ 

 - **Automation Tools**: Scripts for automating repetitive tasks, such as data processing, file management, github actions, and API integration.
- **Data Utilities**: Scripts for data extraction, transformation, and analysis, including  
basic visualizations.
 - **Task Scheduling**: Scripts to schedule and automate recurring tasks (e.g., backups, log parsing).

 # Getting Started 🔑
 
 ### Prerequisites

Ensure you have the following installed:

- **Python3** for running the scripts in this repo
- **Pip3** pythons package manager used to install the pypi package apollo

## Installation

### Via [PyPI](https://pypi.org/project/apollo-o1/1.0.0/)

Install the latest version using `pip`:

```bash
pip install apollo
```

### Via Source

Clone the repository and install it locally:
```bash
git clone https://github.com/dj-io/apollo-cli.git
cd apollo-o1
pip install -r requirements.txt
```

## Usage 🛠

Apollo o1 provides a collection of commands designed to streamline your development workflows. After installation, the apollo command is available in your terminal.

### Show Available Commands

Run the following to see a list of available commands and their descriptions:
```bash
apollo --help
```

example output:
```bash
Usage: apollo [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  gh-create  Create and push a new repository to GitHub.
  gh-add     Push an existing local repository to a new GitHub repo.
```

## Apollos First Script

`apollo gh-create`

The `gh-create` command is one of the features that kicked off Apollo CLI.
It allows developers to create a GitHub repository and push it from a local directory with minimal effort.

### Usage 🛠️

 **Prerequisites**:
- Install [Github CLI](https://cli.github.com/) and authenticate using:
 ```bash
gh auth login
 ```
 
 - Ensure you have setup global Git configurations for Git username and email:

 ```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

**Command**:

1. Run the command:

```bash
apollo gh-create
```

2. Follow the interactive prompts:
    - Enter your GitHub username (cached for future runs).
    - Choose or create a directory for the repository:
	    - Use the current directory.
	    - Select an existing directory.
	    - Create a new directory.

3.	Apollo o1 will handle the following automatically:
	- Create the repository on GitHub.
	- Initialize a local Git repository.
	- Add a README.md file with the repository’s name and description.
	- Push the local repository to GitHub.

### Key Features

1. Interactive Directory Selection

Apollo o1 automatically detects directories and provides multiple options:
- Use the current working directory.
- Select an existing directory from a list.
- Create a new directory if needed.

**Example Prompt**:
```bash
Would you like to use the current directory as the parent directory? (yes/no)
```

2. Persistent GitHub Username

The CLI stores your GitHub username for future use, eliminating repetitive inputs. If the username is already cached, the CLI will prompt you to reuse it.

**Example Prompt**:
```bash
Use cached GitHub username: <username>? (yes/no)
```

3. GitHub Integration
- Automatically creates the repository on GitHub using the gh CLI.
- Adds a remote origin and pushes the code to GitHub.


# Contributing 💡

### Getting started:

1. Fork the repository.
    ```bash
    gh repo fork https://github.com/dj-io/apollo-o1.git --remote=true
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
 
 `Developer mode enables additional CLI commands (e.g., apollo build and apollo deploy) that are not available in production. Follow these steps to configure and use developer mode:`

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
APOLLO_DEV_MODE=1
```

**2. Enable Developer Mode.**
Run the following command in your terminal to enable developer mode:

  ```bash
  export ENV=dev
  ```

- This sets the ENV variable to dev, which ensures the script loads .env.dev and enables developer-specific features.

### Using Developer Mode

Developer mode commands are available for contributors to streamline package development, testing, and deployment. These commands allow developers to rebuild and deploy apollo.

---

**Available Commands**


1. **Build**
    
     Use the apollo build command to rebuild the package during development. This ensures all changes to the codebase are reflected in the package.

    ```bash
    apollo build
    ```
    - **The command includes prompts to**:
      - Cleans up old build artifacts.
      - Rebuilds the package into the dist/ directory
      - Installs the package locally for testing
      - Automatically installs missing dependencies from `requirements.txt`

2. **Deploy**
    Use the apollo deploy command to package and deploy the CLI to PyPI (or TestPyPI)

    ```bash
    apollo deploy
    ```
    -	The command includes prompts to:
        -	Select between TestPyPI or Prod PyPI.
        - Provide changelog or release notes.
        -	Confirm the deployment target.
        - Automatically detects the .pypirc file and verifies its validity.

    - Example

      ```bash
      apollo deploy --test  # Deploy to TestPyPI
      apollo deploy --prod  # Deploy to Prod PyPI
      ```

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
  
  - Run `apollo --help` in developer mode to view the full list of available commands
  -  If you modify .env.dev or .env.prod, reload your environment variables:
      ```bash
      source ~/.zshrc  # For Zsh
      source ~/.bashrc  # For Bash
      ```


### Guidelines:

- Ensure your code is well-documented and adheres to **PEP 8** standards.
- Add **tests** for any new features or bug fixes.
- **Do Not Commit Sensitive Data**: Ensure .env.dev and .env.prod are excluded from version control by including them in .gitignore.
- **Testing Locally**: Use apollo build to test changes locally before deploying to PyPI or TestPyPI.
- **Deploy Responsibly**: Always verify the environment (dev or prod) before running deployment commands to avoid accidental production deployments.

### Versioning:
Given a version number `major.minor.patch`, all: 

  - Breaking backwards compatibility bumps the MAJOR
  - New additions without breaking backwards compatibility bumps the MINOR
  - Bug fixes and misc changes bump the PATCH
  
  **For more information on semantic versioning, please visit http://semver.org/.**


### License: 📜
Copyright Stratum Labs LLC.

This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments 🙏

Apollo o1 is inspired by the need to streamline development workflows. Special thanks to all future contributors who will help shape this project.

<!-- ### Technologies Used 📚

- `Python`: For functonality and logic processing
- `Questionary`: For interactive CLI prompts.
- `OS`: For file system operations.
- `Subprocess`: For running Git commands. -->