<div align="center">

# MLOps Project: Abalone Age Prediction

[![Python Version](https://img.shields.io/badge/python-3.10%20or%203.11-blue.svg)]()
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)
</div>

## 🎯 Project Overview

Welcome to your MLOps project! In this hands-on project, you'll build a complete machine learning system to predict the age of abalone (a type of sea snail) using physical measurements instead of the traditional time-consuming method of counting shell rings under a microscope.

**Your Mission**: Transform a simple ML model into a production-ready system with automated training, deployment, and prediction capabilities.

## 📊 About the Dataset

Traditionally, determining an abalone's age requires:
1. Cutting the shell through the cone
2. Staining it
3. Counting rings under a microscope (very time-consuming!)

**Your Goal**: Use easier-to-obtain physical measurements (shell weight, diameter, etc.) to predict the age automatically.

📥 **Download**: Get the dataset from the [Kaggle page](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset)


## 🚀 Quick Start

### Prerequisites
- GitHub account
- [Kaggle account](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F) (for dataset download)
- Python 3.10 or 3.11

### Setup Steps

1. **Fork this repository**
   - ⚠️ **Important**: Uncheck "Copy the `main` branch only" to get all project branches

2. **Add your team members** as admins to your forked repository

3. **Set up your development environment**:
   ```bash
   # Create and activate a virtual environment
   uv sync
   source venv/bin/activate # on Windows: venv\Scripts\activate

   # Install pre-commit hooks for code quality
    uv pip install pre-commit
    uv run pre-commit install
   ```

## 📋 What You'll Build

By the end of this project, you'll have created:

### 🤖 **Automated ML Pipeline**
- Training workflows using Prefect
- Automatic model retraining on schedule
- Reproducible model and data processing

### 🌐 **Prediction API**
- REST API for real-time predictions
- Input validation with Pydantic
- Docker containerization

### 📊 **Production-Ready Code**
- Clean, well-documented code
- Automated testing and formatting
- Proper error handling

## 📝 How to Work on This Project

### The Branch-by-Branch Approach

This project is organized into numbered branches, each representing a step in building your MLOps system. Think of it like a guided tutorial where each branch teaches you something new!

**Here's how it works**:

1. **Each branch = One pull request** with specific tasks
2. **Follow the numbers** (branch_0, branch_1, etc.) in order
3. **Read the PR instructions** (PR_0.md, PR_1.md, etc.) before starting
4. **Complete all TODOs** in that branch's code
5. **Create a pull request** when done
6. **Merge and move to the next branch**

### Step-by-Step Workflow

For each numbered branch:

```bash
# Switch to the branch
git checkout branch_number_i

# Get latest changes (except for branch_1)
git pull origin main
# Note: A VIM window might open - just type ":wq" to close it

# Push your branch
git push
```

Then:
1. 📖 Read the PR_i.md file carefully
2. 💻 Complete all the TODOs in the code
3. 🔧 Test your changes
4. 📤 Open **ONE** pull request to your main branch
5. ✅ Merge the pull request
6. 🔄 Move to the next branch

> **💡 Pro Tip**: Always integrate your previous work when starting a new branch (except branch_1)!

### 🔍 Understanding Pull Requests

Pull Requests (PRs) are how you propose and review changes before merging them into your main codebase. They're essential for team collaboration!

**Important**: When creating a PR, make sure you're merging into YOUR forked repository, not the original:

❌ **Wrong** (merging to original repo):
![PR Wrong](assets/PR_wrong.png)

✅ **Correct** (merging to your fork):
![PR Right](assets/PR_right.png)

## 💡 Development Tips

### Managing Dependencies

Use uv to manage dependencies. Install or update packages with:

```bash
uv add <package>==<version>
```

Then sync the environment and regenerate the dependency files:

```bash
uv sync
```

### Code Quality
- The pre-commit hooks will automatically format your code
- Remove all TODOs and unused code before final submission
- Use clear variable names and add docstrings

## 📊 Evaluation Criteria

Your project will be evaluated on:

### 🔍 **Code Quality**
- Clean, readable code structure
- Proper naming conventions
- Good use of docstrings and type hints

### 🎨 **Code Formatting**
- Consistent style (automated with pre-commit)
- Professional presentation

### ⚙️ **Functionality**
- Code runs without errors
- All requirements implemented correctly

### 📖 **Documentation & Reproducibility**
- Clear README with setup instructions
- Team member names and GitHub usernames
- Step-by-step instructions to run everything

### 🤝 **Collaboration**
- Effective use of Pull Requests
- Good teamwork and communication

---

## 🎯 Final Deliverables Checklist

When you're done, your repository should contain:

✅ **Automated Training Pipeline**
- [ ] Prefect workflows for model training
- [ ] Separate modules for training and inference
- [ ] Reproducible model and encoder generation

✅ **Automated Deployment**
- [ ] Prefect deployment for regular retraining

✅ **Production API**
- [ ] Working REST API for predictions
- [ ] Pydantic input validation
- [ ] Docker containerization

✅ **Professional Documentation**
- [ ] Updated README with team info
- [ ] Clear setup and run instructions
- [ ] All TODOs removed from code

---

**Ready to start? Head to branch_0 and read PR_0.md for your first task! 🚀**

# Prerequisites and Set-up

## Table of Contents

- [Terminals](#terminals)
  - [Linux and MacOS](#linux-and-macos)
  - [Windows](#windows)
- [Python Installation](#python-installation)
  - [MacOS](#macos)
  - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
  - [Windows (WSL)](#windows-wsl)
- [Docker Desktop](#docker-desktop)
  - [Download and Install Docker Desktop](#download-and-install-docker-desktop)
  - [Check your Installation - Docker Desktop](#check-your-installation---docker-desktop)
- [Git](#git)
  - [Download & Install](#download--install)
  - [Configure Git](#configure-git)
  - [Check your Installation - Git](#check-your-installation---git)
- [Install requirements](#install-requirements)

## Terminals

<details>
  <summary><b>Linux and MacOS</b></summary>

Use your native terminal application:
- **Linux**: Open the Terminal application (usually found in your applications menu or by pressing `Ctrl+Alt+T`)
- **MacOS**: Open Terminal.app (found in Applications > Utilities or search for it using Spotlight)

</details>

<details>
  <summary><b>Windows</b></summary>

For those of you working on Windows, we recommend using Windows Subsystem for Linux (WSL), which enables Unix-like commands.

1. **Open PowerShell** as Administrator
2. **Install WSL** (if not already installed):
   ```bash
   wsl --install
   ```
3. **Update WSL** (if already installed):
   ```bash
   wsl --update
   ```
4. **Run and exit WSL**: You can simply run `wsl` from any directory to enter WSL mode within that directory. You can exit WSL mode by hitting Ctrl+D.

> [!Note]
> After installation, you should use the WSL terminal for all commands in this project.
> If you encounter issues with the WSL installation, you can continue by using the [Git Bash terminal](https://git-scm.com/downloads/win)

</details>

## Python Installation

This project requires **Python 3.11**. Follow the instructions for your operating system:

<details>
  <summary><b>MacOS</b></summary>

The recommended way to install Python 3.11 on macOS is using **Homebrew**.

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3.11**:
   ```bash
   brew install python@3.11
   ```

3. **Verify the installation**:
   ```bash
   python3.11 --version
   ```

> [!Note]
> Do not use the system Python that comes with macOS, as it's intended for Apple development utilities.

</details>

<details>
  <summary><b>Linux</b></summary>
  If you're a real Linux user, you probably already have Python 3.11 installed, or you're about to compile it from source just for fun. Either way, you've got this.
</details>

<details>
  <summary><b>Windows</b></summary>

On WSL or on Git Bash, run follow the following instructions :

1. **Open terminal with WSL** and run:
   ```bash
   sudo apt update
   sudo apt install python3.11
   ```

2. **Verify the installation**:
   ```bash
   python3.11 --version
   ```

</details>

## Docker Desktop

Docker Desktop is a tool for MacOS and Windows machines for the building and sharing of containerized applications and microservices. It includes Docker Engine, Docker CLI client, Docker Compose, Notary, Kubernetes, and Credential Helper. It also features an intuitive user interface that makes managing your Docker images and containers locally much easier.

### Download and Install Docker Desktop

If you do not have `Docker Desktop` installed, you will need to install it. You can follow the official instructions:

- [Install Docker - Mac OS](https://docs.docker.com/desktop/install/mac-install/)
- [Install Docker - Linux](https://docs.docker.com/desktop/install/linux-install/)
- [Install Docker - Windows](https://docs.docker.com/desktop/install/windows-install/)

### Check your Installation - Docker Desktop

Once docker is installed, make sure that it is running correctly by running:

```bash
docker run -p 80:80 docker/getting-started
```

If you check the Docker App, you should see a 'getting started' container running. Once you've checked that this works correctly, remove the container via the UI.

<details>
    <summary><b>Optional</b></summary>
    You can also perform these operations directly from the command line, by running <code>docker ps</code> to check the running containers, <code>docker stop [CONTAINER-ID]</code> to stop it and <code>docker rm -f [CONTAINER-ID]</code> to remove it.
</details>


## Git


Git is a distributed version control system that allows multiple people to work on a project at the same time without overwriting each other's changes.
It's essential for any collaborative coding project.

### Download & Install

To install Git, follow the instructions on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Choose the instructions that match your operating system.

After installation, you can verify that Git is correctly installed by opening a terminal and typing:

```bash
git --version
```

This should return the version of Git that you installed.

### Configure Git

After installing Git, you need to configure it with your name and email address.
This is important because every Git commit uses this information, and it's immutably baked into the commits you start creating:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@foo.bar"
```

You can find full configuration instruction on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

### Check your Installation - Git

Open a terminal, you should be able to run the following commands:

```bash
git --version
```

Complete/check your setup with the following command (Type `:q` to exit):

```bash
git config --global --list
user.name=johndoe
user.email=johndoe@foo.bar
```

Try to reach pandas GitHub repo to check your connection to GitHub:

```bash
git ls-remote --get-url https://github.com/pandas-dev/pandas.git
```

## Install requirements

> [!Important]
> **About the `python` command:**
> The command to invoke Python depends on your installation method:
> - **MacOS (Homebrew)**: Use `python3.11` (or `python3` if you've configured aliases)
> - **Linux/WSL**: Use `python3.11` (or `python3` if available)
> - The examples below use `python` for simplicity, but **you may need to replace it with `python3` or `python3.11`** based on your system.
>
> To check which Python version a command uses, run: `python --version` or `python3 --version` or `python3.11 --version`

Follow these steps to set up your Python environment and install the required packages using `uv`.


1.  **Install `uv` globally (if not already present):**
    We recommend installing `uv` using `pipx` for a clean global installation, as done in our CI pipeline.
    ```bash
    python -m pip install --upgrade pip
    python -m pip install pipx && pipx ensurepath
    pipx install uv
    ```

2.  **Initialize Project Configuration:**
    Create an empty directory named `prerequisites` and initialize the configuration files using `uv init` inside it. This creates `pyproject.toml` and other necessary files.
    ```bash
    uv init
    ```

3.  **Add FastAPI Dependency:**
    Add the core web framework dependency using `uv add`. This updates both `pyproject.toml` and `uv.lock`.
    ```bash
    uv add fastapi
    ```

4.  **Install Dependencies:**
    Synchronize the virtual environment to install all dependencies listed in the newly created/updated files.
    ```bash
    uv sync
    ```

5.  **Activate the Virtual Environment:**
    ```bash
    source .venv/bin/activate
    ```

6.  **Verify your installation:**
    Check that all packages are installed correctly (you should see `fastapi` in the list):
    ```bash
    uv pip list
    ```
    Then, open a Python shell to verify imports:
    ```bash
    uv run python
    >>> import fastapi
    >>> fastapi.__version__ # Should be something like '0.118.0'
    >>> exit()
    ```

If you see the correct version and no errors, your environment is ready!

Thank you ✨ !
