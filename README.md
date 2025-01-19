
 <h1 align="center"> Apollo CLI 🌔 </h1>

<p align="center">
  <a href="https://pypi.org/project/apollo-cli/">
    <img src="https://img.shields.io/pypi/v/apollo-cli.svg" alt="PyPI Version">
  </a>
  <a href="https://github.com/dj-io/apollo-cli/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/dj-io/apollo-cli.svg" alt="License">
  </a>
  <a href="https://github.com/dj-io/apollo-cli/actions">
    <img src="https://github.com/dj-io/apollo-cli/actions/workflows/ci.yml/badge.svg" alt="Build Status">
  </a>
</p>

Apollo CLI is a Python-based command-line interface designed to enhance the developer experience by automating common tasks and workflows. This tool simplifies tasks like managing GitHub repositories, navigating directories, and more, allowing developers to focus on building and delivering software efficiently.

#  Features ⚙️

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

### Via PyPI

Install the latest version using `pip`:

```bash
pip install apollo
```

### Via Source

Clone the repository and install it locally for development:
```bash
git clone https://github.com/dj-io/apollo-cli.git
cd apollo-cli
pip install -e .
```

## Usage

Apollo CLI provides a collection of commands designed to streamline your development workflows. After installation, the apollo command is available in your terminal.

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
  create-repo       Create and push a new repository to GitHub.
  push-existing     Push an existing local repository to a new GitHub repo.
```

## Apollos First Script

`apollo creat-repo`

The `create_repo` command is one of the features that kicked off Apollo CLI.
It allows developers to create a GitHub repository and push it from a local directory with minimal effort.

### Usage

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
apollo create-repo
```

2. Follow the interactive prompts:
    - Enter your GitHub username (cached for future runs).
    - Choose or create a directory for the repository:
	    - Use the current directory.
	    - Select an existing directory.
	    - Create a new directory.

3.	Apollo CLI will handle the following automatically:
	- Create the repository on GitHub.
	- Initialize a local Git repository.
	- Add a README.md file with the repository’s name and description.
	- Push the local repository to GitHub.

### Key Features

1. Interactive Directory Selection

Apollo CLI automatically detects directories and provides multiple options:
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


# Contributing

Contributions are welcome! To Contribute:

1. Fork the repository.

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

Guidelines:
- Ensure your code is well-documented and adheres to PEP 8 standards.
- Add tests for any new features or bug fixes.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments

Apollo CLI is inspired by the need to streamline development workflows. Special thanks to all contributors who have helped shape this project.

<!-- ### Technologies Used 📚

- `Python`: For functonality and logic processing
- `Questionary`: For interactive CLI prompts.
- `OS`: For file system operations.
- `Subprocess`: For running Git commands. -->