# MLOps Project — Abalone Age Prediction

**Contributors:** Basile Desjuzeur, Paul Lacombe, Thomas Milcent, Côme Malézieux & Nicolas Guillet  

---

## 1. Introduction

This project presents the development of a complete MLOps workflow for predicting the age of abalone, a marine mollusk, based on measurable physical characteristics.  

The objective is to move beyond model performance and implement a scalable, automated, and reproducible machine learning system integrating data orchestration, deployment, and observability.  

The work demonstrates how a standard data science pipeline can be structured, automated, and deployed following modern MLOps practices.

---

## 2. Project Objectives

The main objectives of this project are to:

- Automate data ingestion, preprocessing, and model training using **Prefect**.  
- Deploy a trained model through a **FastAPI** service for real-time inference.  
- Ensure full reproducibility through dependency management, version control, and containerization.  
- Integrate quality assurance mechanisms such as linting, formatting, and continuous integration workflows.  

The repository follows an incremental structure where each branch focuses on a distinct MLOps component, progressively building toward a complete end-to-end system.

---

## 3. Repository Structure

```

.
├── .github/workflows/       # Continuous integration and testing workflows
├── assets/                  # Documentation images and diagrams
├── data/                    # Local datasets (excluded from version control)
├── notebooks/               # Jupyter notebooks for analysis and exploration
├── src/                     # Core source code (data, model, API, orchestration)
├── pyproject.toml           # Project configuration and dependencies
├── requirements*.txt        # Dependency specification files
└── README.md

````

Each component of the repository is modular and independently testable, contributing to the reproducibility and maintainability of the workflow.

---

## 4. Dataset Description

The **Abalone dataset**, originally from the UCI Machine Learning Repository, provides various physical measurements of abalone specimens, including length, diameter, height, and shell weight.  

The task consists of predicting the number of rings, which serves as an estimate of the abalone’s age.  

This dataset was selected for its structured format and suitability for demonstrating data engineering, modeling, and deployment concepts within an MLOps framework.

---

## 5. Methodology

The methodology follows the structure of a full machine learning operations pipeline.  
Each stage was designed, implemented, and validated independently before integration into a unified workflow.

### 5.1 Data Processing and Modeling

Raw data is cleaned, encoded, and transformed into a modeling-ready format.  
The training phase involves testing and evaluating regression models using standard performance metrics.  

The modular design allows for easy substitution of models or data sources in future iterations.

---

### 5.2 Orchestration with Prefect

Workflow orchestration is handled by **Prefect**, which enables automation, scheduling, and monitoring of data pipelines.  
The Prefect UI provides visibility over task dependencies, execution logs, and error management.

#### Prefect Setup

To configure the local Prefect environment:

uv run prefect config set PREFECT_API_URL=http://0.0.0.0:4200/api
sqlite3 --version
uv run prefect server start --host 0.0.0.0

To reset the Prefect database if needed:

uv run prefect server database reset

The Prefect dashboard is accessible at [http://0.0.0.0:4200/dashboard](http://0.0.0.0:4200/dashboard), allowing interactive monitoring of flow executions.

This orchestration ensures reproducibility, traceability, and scalability of the workflow, facilitating continuous execution of model training and data updates.

---

### 5.3 Model Deployment with FastAPI

Model deployment is implemented using **FastAPI**, a lightweight and high-performance web framework for building APIs in Python.

FastAPI was chosen for its asynchronous architecture, automatic data validation through Pydantic, and compatibility with Dockerized environments.

The API serves as the interface between the model and external systems, exposing:

* **GET** endpoints for metadata or status checks.
* **POST** endpoints for predictions, validating inputs and returning inference results in JSON format.

FastAPI automatically generates interactive documentation under `/docs`, providing a user-friendly testing environment and complete visibility of the model interface.

---

### 5.4 Containerization and Reproducibility

The full project environment is containerized using **Docker**, ensuring consistent execution across different systems.
Dependencies are managed through **uv**, enabling deterministic builds and isolated environments.

Automated pre-commit hooks and CI workflows maintain code quality and enforce uniform development standards across contributors.

This design guarantees that every component—from data extraction to API deployment—can be reproduced, audited, and redeployed without manual intervention.

---

## 6. Development Workflow

Development followed a branch-based incremental strategy, where each branch introduced one functional enhancement or MLOps component.

All changes were version-controlled, reviewed, and merged progressively into the main branch.

This approach fostered iterative validation, modularity, and collaborative development.

Each branch corresponds to a clear milestone in the system’s construction, from local model training to full deployment and orchestration.

---

## 7. Results and Discussion

The resulting system demonstrates a fully operational MLOps architecture integrating orchestration, automation, and model deployment.

* **Prefect** provides a centralized orchestration layer ensuring observability, error handling, and scheduling of ML workflows.
* **FastAPI** offers an efficient inference layer for serving predictions through standardized REST endpoints.
* **Docker** and **uv** guarantee that environments are identical across all contributors and execution platforms.

This architecture illustrates the transition from a static, local machine learning model to a reproducible and scalable production pipeline.

The project emphasizes maintainability, transparency, and traceability at each stage of the ML lifecycle.

---

## 8. Conclusion

This project demonstrates how machine learning systems can be structured as end-to-end operational workflows.

By combining **Prefect** for orchestration and **FastAPI** for deployment, it delivers a reproducible and maintainable architecture for continuous model development and delivery.

The integration of automation, validation, and containerization ensures that every component of the pipeline—from data ingestion to real-time prediction—is both reliable and extensible.

Through this implementation, the team showcases the fundamental principles of modern MLOps: **reproducibility**, **scalability**, **observability**, and **collaborative development** within a production-oriented environment.

---
