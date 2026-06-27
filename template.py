import os
from pathlib import Path

project_name = "customer_intelligence_suite"

# Yeh 5 tiers hain (CLV, Churn, Segmentation, Demand Forecast,Recommendation) - har tier ka apna "components/" folder banega, aap ke
# template ke pattern (data_ingestion, data_validation, data_transformation, model_trainer, model_evaluation, model_pusher) ko follow karte hue.

tiers = [
    "tier1_clv",
    "tier2_churn",
    "tier3_segmentation",
    "tier4_demand_forecast",
    "tier5_recommendation",
]

component_files = [
    "data_ingestion.py",
    "data_validation.py",
    "data_transformation.py",
    "model_trainer.py",
    "model_evaluation.py",
    "model_pusher.py",
]

list_of_files = [
    # ---------------- Root package init ----------------
    f"{project_name}/__init__.py",

    # ---------------- SHARED modules (sab tiers use karenge) ----------------
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",

    f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    f"{project_name}/exception/__init__.py",

    f"{project_name}/logger/__init__.py",

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    # ---------------- Flask app ----------------
    "app/__init__.py",
    "app/routes/__init__.py",
    "app/routes/clv_routes.py",
    "app/routes/churn_routes.py",
    "app/routes/segment_routes.py",
    "app/routes/forecast_routes.py",
    "app/routes/recommend_routes.py",
    "app/templates/.gitkeep",
    "app/static/.gitkeep",

    # ---------------- Data & artifact folders ----------------
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "models/.gitkeep",
    "notebooks/.gitkeep",

    # ---------------- Tests ----------------
    "tests/__init__.py",

    # ---------------- Root-level project files ----------------
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "README.md",
    ".gitignore",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

# Har tier ke liye uska __init__.py aur components/ wali 6 files add karo
for tier in tiers:
    list_of_files.append(f"{project_name}/{tier}/__init__.py")
    for comp_file in component_files:
        list_of_files.append(f"{project_name}/{tier}/components/__init__.py")
        list_of_files.append(f"{project_name}/{tier}/components/{comp_file}")

# Duplicate __init__.py entries (loop ki wajah se) ko hata kar unique list banate hain
list_of_files = list(dict.fromkeys(list_of_files))


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")