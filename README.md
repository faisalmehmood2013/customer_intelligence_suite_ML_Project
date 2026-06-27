# Customer Intelligence Suite

A modular, multi-tier Machine Learning system for the Retail / E-commerce domain — built end-to-end from raw transactional data to a deployed, containerized prediction service.

This repository documents the project as it is built, step by step. Each completed phase is logged below with what was done and why, so the progress is transparent and reproducible.

---

## Project Overview

| | |
|---|---|
| **Domain** | Retail / E-commerce |
| **Dataset** | [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) (UCI Machine Learning Repository) — real UK-based e-commerce transactions, Dec 2009–Dec 2011 |
| **Learning Type** | Supervised (Regression + Classification), Unsupervised (Clustering), Time Series |
| **Final Deliverable** | Flask web application, containerized with Docker |
| **Future Extension** | Integration with LangChain / LangGraph (LLM reasoning) and n8n (automation) to evolve into a SaaS product |

### The Five Tiers

The project is organized into five independent prediction "tiers," all built from the same raw dataset through different feature engineering strategies.

| Tier | Problem Type | Goal | Algorithms |
|---|---|---|---|
| **1. Customer Lifetime Value (CLV)** | Regression | Predict a customer's future/total spend | Linear, Ridge, Lasso, ElasticNet, SVR, Decision Tree, Random Forest |
| **2. Churn Prediction** | Classification | Predict whether a customer will stop purchasing | Logistic Regression, Naive Bayes, Decision Tree, SVM, Random Forest |
| **3. Customer Segmentation** | Unsupervised (Clustering) | Group customers by purchasing behavior | K-Means, Hierarchical Clustering |
| **4. Demand Forecasting** | Time Series | Predict future sales volume | ARIMA, Prophet, Linear Regression with time features |
| **5. Product Recommendation** | Similarity-based | Suggest products based on purchase patterns | Cosine Similarity, Collaborative Filtering |

---

## Project Architecture

The codebase follows a modular, MLOps-style structure. Each tier has its own self-contained pipeline (`components/`), while common infrastructure (logging, exception handling, configuration, utilities) is shared across all tiers.

```
customer_intelligence_suite/
│
├── tier1_clv/                  → CLV pipeline (Regression)
│   └── components/             → data_ingestion, data_validation, data_transformation,
│                                  model_trainer, model_evaluation, model_pusher
├── tier2_churn/                → Churn pipeline (Classification)
│   └── components/
├── tier3_segmentation/         → Segmentation pipeline (Clustering)
│   └── components/
├── tier4_demand_forecast/      → Demand Forecasting pipeline (Time Series)
│   └── components/
├── tier5_recommendation/       → Recommendation pipeline
│   └── components/
│
├── configuration/              → Shared: DB / cloud connection settings
├── constants/                  → Shared: fixed values (paths, column names, defaults)
├── entity/                     → Shared: Config and Artifact data structures
├── exception/                  → Shared: custom exception handling
├── logger/                     → Shared: logging setup
├── utils/                      → Shared: reusable helper functions
└── pipeline/                   → Orchestrates training and prediction across tiers

app/                            → Flask application
├── routes/                     → One route file per tier (clv, churn, segment, forecast, recommend)
├── templates/
└── static/

data/                           → raw/ and processed/ datasets
models/                         → Saved, trained model artifacts
notebooks/                      → Exploratory and practice notebooks
tests/                          → Unit tests

app.py            → Flask application entry point
demo.py           → Quick experimentation / component testing script
setup.py          → Makes the project an installable Python package
requirements.txt  → Project dependencies
Dockerfile        → Containerization (added in the deployment phase)
.dockerignore
config/           → model.yaml and schema.yaml configuration files
```

**Design rationale:** Each tier (CLV, Churn, Segmentation, etc.) is treated as an independent ML pipeline with its own ingestion, validation, transformation, training, evaluation, and deployment steps — mirroring how separate models are managed in real production systems. Shared concerns (logging, exceptions, configuration, utilities) are factored out once and reused by every tier, avoiding duplication.

---

## Progress Log

This section is updated as each step is completed. Kept intentionally brief — detailed explanations live in code comments/docstrings, not here.

### ✅ Step 1 — Project Scaffolding
Designed the full multi-tier folder structure and built a `template.py` script that generates it (77 files/folders) in one run. Structure pushed to GitHub.

### ✅ Step 2 — Environment Setup
Created an isolated Conda environment for the project:
```bash
conda create -n mlproject python=3.12 -y
conda activate mlproject
```
Keeps project dependencies separate from the system Python installation.

### ✅ Step 3 — `setup.py`
Added `setup.py` so the project can be installed as an editable local package (enables clean imports like `from customer_intelligence_suite.utils import ...` from anywhere in the project).

### ✅ Step 4 — `requirements.txt`
Listed all dependencies for every tier (ML, time series, Flask, visualization, notebooks). Last line is `-e .`, which tells pip to install this project itself (via `setup.py`) in editable mode — so code changes are picked up immediately without reinstalling. Installed with:
```bash
pip install -r requirements.txt
```

### ⬜ Step 5 — *(To be defined)*

---

## Tech Stack

- **Language:** Python
- **ML Libraries:** scikit-learn, pandas, NumPy
- **Web Framework:** Flask
- **Containerization:** Docker
- **Dataset Source:** UCI Machine Learning Repository

---

## Getting Started

```bash
conda activate mlproject
pip install -r requirements.txt
```

See the Progress Log above for environment and setup details. Further run instructions (training, Flask app, Docker) will be added here as each tier becomes functional.

---

*This README is a living document and will be updated after every completed phase of the project.*
