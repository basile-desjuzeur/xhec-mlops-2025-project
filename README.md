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


## More on fastapi

### First Steps
The simplest app you can create with FastAPI looks like this:
```python
from fastapi import FastAPI
# Initiate the FastAPI app that will be run
app = FastAPI()
# Initiate the homepage of the API
@app.get("/")
def index():
    return {"message": "This is the homepage of the API "}
```
The `app` variable is the main entry point of the API. All operations that are added to the API will be indexed using this entrypoint. To create an operation, you need to write a `function` and decorate it with a specific `operation` and `path`.
-  The function will specify the behaviour that you expect from you API. In this very simple example, we create a simple function that always returns the same value, a dictionary with a standard message.
FastAPI uses the decorator syntax to specify the `operation` and `path`:
-  `Operations` often refer to the methods of the HTTP protocol:
    - `POST`: Create (Used to create new resources)
    - `GET`: Read (Retrieve a representation of a resource)
    - `PUT`: Update (Update or Create a resource)
    - `DELETE`: Delete (Used to delete a resource)
    In our use cases, we will only deal with `POST` and `GET` operations
- The `path` refer to the last part of the URL after the endpoint. In our example, we created a root path that would look like this:
    ```https://my-endpoint/```
You can copy the code into a file called `main.py` in this `fast_api_tutorial` folder.
To launch the app, you should run in your terminal:
```bash
cd lessons/02-model-deployment/fast_api_tutorial
```
```bash
uvicorn main:app --reload
```
[`Uvicorn`](https://www.uvicorn.org/) is a tool that helps your Python web applications run quickly and handle many tasks at the same time. We are using it here to run our FastAPI application. The command we used tells it to look for the `app` object inside our `main.py` file. The `--reload` option relaunches the application every time the code changes (it should only be used in development).

## Check your new app
By default, `uvicorn` will deploy the app on your localhost on the port 8000 [http://localhost:8000](http://localhost:8000). Clicking on this link will show you the home page of your API and display the message you coded.
<details>
<summary> If you want more information on the meaning of host and port</summary>
> **Host**: In networking, a host refers to a device that is connected to a network and can send or receive data. For example, a computer, smartphone, or server can be referred to as a host in a network.
> **Port**: A port is a specific point where data can enter or leave a host. It is associated with a specific process or service in the host system. For example, web servers typically listen on port 80 for incoming HTTP requests.
- [Host vs Localhost vs Port](https://stackoverflow.com/questions/1946193/whats-the-whole-point-of-localhost-hosts-and-ports-at-all)
- [127.0.0.1 vs 0.0.0.0](https://stackoverflow.com/questions/20778771/what-is-the-difference-between-0-0-0-0-127-0-0-1-and-localhost)
</details>
A nice feature of FastAPI is that it automatically generates a documentation page accessible at [http://localhost:8000/docs](http://localhost:8000/docs)

## Create a POST operation
The next step is to create an operation that receives information from the user and uses it internally to modify its response. The `POST` operation is the way that we can communicate information to our endpoint.
```python
from fastapi import FastAPI
from pydantic import BaseModel
# Define a data model for the request body
class Item(BaseModel):
    name: str
# Initiate the FastAPI app
app = FastAPI()
# Initiate the homepage of the API
@app.get("/")
def index():
    return {"message": "This is the homepage of the API "}
# Define a POST operation for the path "/greet"
@app.post("/greet")
def greet_user(item: Item):
    return {"message": f"Hello, {item.name}"}
```
In this example, we define a POST operation at the path "/greet". The `function` we defined accepts one parameter `item` that is used to generate a simple greeting.
One useful feature of `FastAPI` is that it performs automatic data validation using python's type hints. To do so, it uses the [pydantic](https://docs.pydantic.dev/latest/) package, which allows us to create `models` that enforce data structures in our code. In our example, the operation expects a JSON body with a field "name". The Item class is a `pydantic` model that helps with data validation and serialization. When a POST request is made to "/greet" with a JSON body like {"name": "Alice"}, the server will respond with {"message": "Hello, Alice"}.
To run this application, overwrite the code in `main.py` and use the same command to launch the app:
```bash
uvicorn main:app --reload
```
### Testing the app
To test your new operation, you can connect to [localhost:8000/docs](localhost:8000/docs) and use the `Try it out` option to send your own request:
![Try it out](images/try_it_out.png)
You can modify the `Request body` to include your name:
![Request Body](images/request_body.png)
You can do the same operations directly from your terminal, by running:
```bash
# The curl command is a tool to transfer data from or to a server, using one of the supported protocols (HTTP, HTTPS, FTP, etc.)
# The -X option specifies a custom request method to use when communicating with the HTTP server. In this case, 'POST' is used.
curl -X 'POST' \
# The URL of the server to which the request is sent
  'http://localhost:8000/greet' \
# Headers are used to provide information to both the client and server. They define the operating parameters of an HTTP transaction.
# The -H option is used to include extra header information. 'accept: application/json' tells the server that the client expects JSON response.
  -H 'accept: application/json' \
# 'Content-Type: application/json' tells the server that the client is sending JSON data in the body of the request.
  -H 'Content-Type: application/json' \
# The -d option is used to send data in a POST request. It sends the following data to the server in JSON format.
  -d '{
  "name": "Student"
}'
```

<details>
    <summary>Curl in Windows</summary>
If you are using a Windows machine, the `curl` command will probably not be intalled. You can follow the instructions of this [tutorial](https://developer.zendesk.com/documentation/api-basics/getting-started/installing-and-using-curl/#using-curl-in-windows) to adapt the command.
</details>
You can also check that `pydantic` is performing the data validation well by sending a bad request:
```bash
curl -X 'POST' \
  'http://localhost:8000/greet' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": 70
}'
```
The response you get should be a `422` error:
```
{"detail":[{"type":"string_type","loc":["body","name"],"msg":"Input should be a valid string","input":70,"url":"https://errors.pydantic.dev/2.4/v/string_type"}]}
```

### Start Prefect (orchestration)
1. Set API URL:
   uv run prefect config set PREFECT_API_URL=http://0.0.0.0:4200/api
2. Start server:
   uv run prefect server start --host 0.0.0.0
3. (Optional) Reset DB:
   uv run prefect server database reset
4. Open dashboard:
   $BROWSER http://0.0.0.0:4200/dashboard

### Start API (FastAPI)
1. Install deps:
   pip install -r requirements.txt
2. Run locally:
   uv run uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
3. API docs:
   $BROWSER http://0.0.0.0:8000/docs

### Docker (containerized deployment)
1. Build:
   docker build -t abalone-api -f docker/Dockerfile .
2. Run:
   docker run --rm -p 8000:8000 abalone-api

### Ports
- Prefect dashboard: 4200
- FastAPI: 8000


Thank you ✨ !
