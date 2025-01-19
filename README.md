<h1 align="center"> Python Scripts Repository 📦 </h1>

A curated collection of Python scripts and utilities developed to streamline workflows, automate tasks, and solve practical problems. This repository demonstrates proficiency in Python scripting, task automation, and problem-solving across various domains.

---

## Key Features ⚙️

- **Automation Tools**: Scripts for automating repetitive tasks, such as data processing, file management, github actions, and API integration.
- **Data Utilities**: Scripts for data extraction, transformation, and analysis, including basic visualizations.
- **Task Scheduling**: Scripts to schedule and automate recurring tasks (e.g., backups, log parsing).



## Example Scripts 🚀

### **GitHub Repository Automation**
- **Job**: Creates a GitHub repository, initializes a local directory, and sets up the initial push to the remote repository, using just a few prompts.
- **Flow**:
  - Prompts the user for repository details using `questionary`.
  - Automates repository creation via the GitHub CLI.
  - Initializes the local repository, commits the initial files, and pushes to the remote.
- **Usage**:
 1. **Prerequisites**:
    - Install [Github CLI](https://cli.github.com/) and authenticate using:
    ```
    gh auth login
    ```
    - Ensure you have setup global Git configurations for Git username and email:
    ```
    git config --global user.name "Your Name"
    git config --global user.email "youremail@example.com"
    ```
2. **Run the script**:
    ```
    python3 create_repo.py
    ```
3. **Follow the prompts** to create and push your new repository.



## Technologies Used 📚

- `Python`: For functonality and logic processing
- `Questionary`: For interactive CLI prompts.
- `OS`: For file system operations.
- `Subprocess`: For running Git commands.

## Getting Started 🔑

### Prerequisites

Ensure you have the following installed:

- **Python3** for running the scripts in this repo
- **Pip3** pythons package manager used to install the required dependencies listed in `requirements.txt` 

### Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/scripts.git
   ```
2. **CD into the Repository**:

   ```
   cd scripts
   ```

3. **Install Dependencies**: Use the provided requirements.txt to install the necessary libraries
    ``` 
    pip3 install -r requirements.txt
    ```

4. **Run scripts**: Navigate to the script you want to run and execute it:
    ```
    python3 create_repo.py
    ```