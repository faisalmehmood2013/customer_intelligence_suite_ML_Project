"""
generate_structure.py
-----------------------
Yeh script aap ke diye gaye template (US Visa MLOps project)
ka EXACT pattern follow karta hai, lekin "Customer Intelligence Suite"
(multi-tier: CLV, Churn, Segmentation, Demand Forecast, Recommendation)
ke liye adapt kiya gaya hai.

PATTERN AAP KE TEMPLATE SE LIYA GAYA HAI:
    components/  -> data_ingestion, data_validation, data_transformation,
                    model_trainer, model_evaluation, model_pusher
    configuration/, constants/, entity/, exception/, logger/, pipline/, utils/

FARQ: Aap ke template mein YEH SAB EK pipeline ke liye tha (single model -
US Visa approval prediction). Hamare project mein 5 ALAG tiers hain, isliye
har tier ka apna "components/" folder hoga - lekin baqi structure
(configuration, constants, entity, exception, logger, utils) SHARED
rahega, kyunke yeh sab tiers ke liye COMMON/REUSABLE cheezen hain.

Har file mein DOCSTRING likha gaya hai jo batata hai us file ka role kya
hai - taake aap khud code likhते waqt bhool na jayen "yeh file kis liye hai".
"""

import os
from pathlib import Path

project_name = "customer_intelligence_suite"

# -----------------------------------------------------------------------
# Docstring content for each file - "yeh file kis liye hai" explanation
# -----------------------------------------------------------------------

DOCSTRINGS = {

    # ===================== ROOT LEVEL =====================
    f"{project_name}/__init__.py":
        '"""Root package for Customer Intelligence Suite - multi-tier ML system\nfor Retail/E-commerce (CLV, Churn, Segmentation, Demand Forecast, Recommendation)."""\n',

    # ===================== SHARED: CONFIGURATION =====================
    f"{project_name}/configuration/__init__.py":
        '"""Configuration package - DB connections, cloud storage configs,\nor any external service connection settings (shared across ALL tiers)."""\n',
    f"{project_name}/configuration/mongo_db_connection.py":
        '"""\nMongoDB connection setup (agar aap raw/processed data MongoDB mein\nstore karna chahein, alternative to flat CSV files).\n\nYeh OPTIONAL hai - agar aap sirf CSV/local files use kar\nrahe hain to is file ko khali rehne dein abhi, baad mein zaroorat\npar use karein.\n"""\n',
    f"{project_name}/configuration/aws_connection.py":
        '"""\nAWS S3 connection setup (agar model artifacts ya data ko cloud pe\nstore/deploy karna ho - model_pusher isko use karega).\n\nYeh Phase 7 (Docker/Deployment) ke waqt relevant hoga.\n"""\n',

    # ===================== SHARED: CONSTANTS =====================
    f"{project_name}/constants/__init__.py":
        '''"""
Constants package - SAB fixed values yahan rakhte hain (file paths,
column names, model parameters ke defaults, etc.) taake hardcoded
values code mein bar-bar na likhni paren.

Jaisे "TARGET_COLUMN = \'churned\'" ya
"TEST_SIZE = 0.2" jaisi values yahan define karenge, phir
har tier mein import karke use karenge. Isse agar value change
karni ho, EK jagah change karo, sab files mein automatically update ho jayegi.
"""

# -------- Shared Pipeline Constants --------
PIPELINE_NAME: str = "customer_intelligence_suite"
ARTIFACT_DIR: str = "artifacts"

# -------- Shared Data Constants --------
RAW_DATA_FILE_NAME: str = "online_retail_ii.csv"
TRAIN_TEST_SPLIT_RATIO: float = 0.2
RANDOM_STATE: int = 42

# -------- Shared Column Names (raw dataset se aate hain) --------
COL_INVOICE_NO: str = "InvoiceNo"
COL_STOCK_CODE: str = "StockCode"
COL_DESCRIPTION: str = "Description"
COL_QUANTITY: str = "Quantity"
COL_INVOICE_DATE: str = "InvoiceDate"
COL_UNIT_PRICE: str = "UnitPrice"
COL_CUSTOMER_ID: str = "CustomerID"
COL_COUNTRY: str = "Country"

# Tier-specific constants aap "tierX_xxx/constants.py" mein alag rakh
# sakte hain agar zaroorat pare (jaise CHURN_DAYS_THRESHOLD = 90)
''',

    # ===================== SHARED: ENTITY =====================
    f"{project_name}/entity/__init__.py":
        '"""Entity package - data ke \'structured shapes\' define karta hai\n(Config aur Artifact classes), taake har function ka input/output\nclearly defined ho, random dictionaries pass karne ke bajaye."""\n',
    f"{project_name}/entity/config_entity.py":
        '''"""
config_entity.py
------------------
Yahan hum CONFIG classes define karte hain - har tier/component ko
chalane ke liye kya settings chahiye (file paths, ratios, params).

Soch lein yeh "instruction cards" hain - jaise
DataIngestionConfig batayega "raw data kahan se aayega, processed
kahan jayega". Python mein @dataclass use karenge (clean aur readable).

Example structure (aap is tarah classes banayenge har component ke liye):

    @dataclass
    class DataIngestionConfig:
        raw_data_dir: str
        feature_store_file_path: str
        train_file_path: str
        test_file_path: str
        train_test_split_ratio: float

    @dataclass
    class CLVModelTrainerConfig:
        trained_model_file_path: str
        expected_score: float
        model_config_file_path: str

Aap har tier (CLV, Churn, Segmentation, etc.) ke liye alag Config
class banayenge jab us tier pe kaam shuru karein.
"""
''',
    f"{project_name}/entity/artifact_entity.py":
        '''"""
artifact_entity.py
---------------------
Yahan hum ARTIFACT classes define karte hain - har step ka OUTPUT
kaisa dikhega (file paths jo next step ko milenge).

Agar config_entity "instructions" hain, to artifact_entity
"results/proof" hai ke kaam ho gaya. Jaise DataIngestionArtifact
batayega "train_file_path yeh hai, test_file_path yeh hai" - taake
DataValidation component isko use kar sake.

Example structure:

    @dataclass
    class DataIngestionArtifact:
        train_file_path: str
        test_file_path: str

    @dataclass
    class ModelTrainerArtifact:
        trained_model_file_path: str
        metric_artifact: dict   # MAE, RMSE, R2 etc.

Yeh pattern ek "chain" banata hai: Ingestion ka Artifact -> Validation
ka Input, Validation ka Artifact -> Transformation ka Input, aur aage.
"""
''',

    # ===================== SHARED: EXCEPTION =====================
    f"{project_name}/exception/__init__.py":
        '''"""
exception/__init__.py
------------------------
Custom Exception class - jab error aaye, normal Python error ke
bajaye yeh batayega EXACT FILE NAME aur LINE NUMBER jahan error hui.

Yeh debugging ko BOHOT asaan banata hai. Aap ke template
mein bhi yehi pattern tha. Standard implementation:

    import sys

    class CustomException(Exception):
        def __init__(self, error_message, error_detail: sys):
            self.error_message = error_message
            _, _, exc_tb = error_detail.exc_info()
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename

        def __str__(self):
            return (f"Error in [{self.file_name}] at line [{self.lineno}]: "
                    f"{self.error_message}")

Usage: har function mein try/except ke andar
    raise CustomException(str(e), sys) from e
"""
''',

    # ===================== SHARED: LOGGER =====================
    f"{project_name}/logger/__init__.py":
        '''"""
logger/__init__.py
---------------------
Logging setup - print() statements ke bajaye proper LOG FILES banata
hai, jisme timestamp, log-level (INFO/ERROR/WARNING), aur message hota hai.

Jab Docker mein deploy hoga, "print()" se debug karna
mushkil hota hai - log FILES check karna behtar hota hai. Standard
implementation Python ke built-in 'logging' module se:

    import logging
    import os
    from datetime import datetime

    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_path, exist_ok=True)
    LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

Usage har file mein: from customer_intelligence_suite.logger import logging
                      logging.info("Data ingestion started")
"""
''',

    # ===================== SHARED: UTILS =====================
    f"{project_name}/utils/__init__.py":
        '"""Utils package - choti helper functions jo HAR tier mein\nbar-bar use hoti hain (file read/write, object save/load, etc.)."""\n',
    f"{project_name}/utils/main_utils.py":
        '''"""
main_utils.py
---------------
Common/reusable helper functions - SAB tiers yeh functions use karenge.

Yahan generic functions likhenge jaise:
    - read_yaml_file(path)       -> config/schema.yaml ya model.yaml padhne ke liye
    - write_yaml_file(path, data)
    - save_object(file_path, obj)        -> trained model (.pkl) save karna (joblib/pickle)
    - load_object(file_path)             -> saved model wapis load karna
    - save_numpy_array_data(path, array)  -> processed features save karna
    - load_numpy_array_data(path)

Yeh exact wahi cheezen hain jo har tier (CLV ho ya Churn) ko equally
chahiye hongi - isliye yahan ek hi jagah likhte hain, baar baar nahi.
"""
''',

    # ===================== SHARED: PIPELINE (Orchestration) =====================
    f"{project_name}/pipeline/__init__.py":
        '"""Pipeline package - har tier ka END-TO-END flow yahan orchestrate\nhota hai (ingestion -> validation -> transformation -> training -> evaluation)."""\n',
    f"{project_name}/pipeline/training_pipeline.py":
        '''"""
training_pipeline.py
-----------------------
MASTER orchestration file - SAB tiers ke training ko ek sequence mein
chalata hai (ya aap chahein to har tier ka apna run_training() call karein).

Yeh file basically "remote control" hai - jab aap
"python -m customer_intelligence_suite.pipeline.training_pipeline"
chalayenge, yeh andar se har tier ke components ko sahi order mein
call karega:

    1. Shared data ingestion (raw data load + clean)
    2. Tier1_CLV: feature engineering -> train -> evaluate -> save
    3. Tier2_Churn: feature engineering -> train -> evaluate -> save
    4. ... (aage jo tiers ban jayen)

Isko aap dheere-dheere banayenge - jab Tier 1 complete ho, sirf
Tier 1 ka call yahan add karein. Baad mein Tier 2 add karte jayen.
"""
''',
    f"{project_name}/pipeline/prediction_pipeline.py":
        '''"""
prediction_pipeline.py
-------------------------
Yeh file FLASK APP use karega - jab user koi data submit kare
(jaise "is customer ka CLV predict karo"), yeh file:
    1. Saved model (.pkl) load karega
    2. Input data ko sahi format/scaling mein convert karega
    3. Prediction return karega

training_pipeline.py "model BANANE" ke liye hai,
prediction_pipeline.py "ban chuke model SE PREDICT karne" ke liye hai -
yeh dono ALAG concerns hain (Training Time vs Inference/Serving Time).

Har tier ke liye yahan ek class/function hogi:
    - predict_clv(input_data)
    - predict_churn(input_data)
    - get_customer_segment(input_data)
"""
''',

    # ===================== APP-LEVEL FILES =====================
    "app.py":
        '''"""
app.py
--------
FLASK APPLICATION entry point - yeh file chalane se web server start
hota hai.

Yahan hum:
    1. Flask app initialize karenge
    2. Har tier ke routes register karenge (Blueprints use karke -
       jaise clv_routes, churn_routes, segment_routes)
    3. app.run() se server start karenge

Structure (jab banayenge):
    from flask import Flask
    from customer_intelligence_suite.pipeline.prediction_pipeline import ...

    app = Flask(__name__)

    @app.route("/predict/clv", methods=["POST"])
    def predict_clv():
        ...

    @app.route("/predict/churn", methods=["POST"])
    def predict_churn():
        ...

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)
"""
''',
    "demo.py":
        '''"""
demo.py
---------
Quick TESTING/EXPERIMENTATION script - isko aap use karenge individual
components ko TEST karne ke liye, bina poori pipeline chalaye.

Jaise aap ke template mein tha - yeh ek "scratchpad" hai.
Misal: agar sirf data_ingestion.py test karna ho, yahan likh kar
quickly run kar lein, poora Flask app chalane ki zaroorat nahi.
"""
''',
    "setup.py":
        '''"""
setup.py
----------
Yeh file project ko ek INSTALLABLE PYTHON PACKAGE banati hai
(taake "from customer_intelligence_suite.utils import ..." jaise
imports kaam karein, project ko kahin se bhi).

Standard setup.py (aap ke template jaisa hi):

    from setuptools import find_packages, setup

    setup(
        name="customer_intelligence_suite",
        version="0.0.1",
        author="Faisal",
        packages=find_packages(),
        install_requires=[],   # requirements.txt se separately install karenge
    )

Phir terminal mein: pip install -e .
"""
''',
    "requirements.txt":
        "# yahan saari libraries likhi jayengi jo project use karega\n"
        "# (pandas, numpy, scikit-learn, flask, etc.) - jab jo library use karein, yahan add karein\n",
    "Dockerfile":
        '''# Dockerfile
# -----------
# Yeh file Phase 7 (Deployment) mein banayenge.
# Yahan likhenge:
#   1. Konsi Python image base honi hai (FROM python:3.10-slim)
#   2. Requirements install karne ka command
#   3. App ka code container mein copy karna
#   4. Flask app ko expose/run karna (CMD ["python", "app.py"])
#
# Abhi yeh file KHALI hai - Phase 7 tak intezar karein.
''',
    ".dockerignore":
        "# yahan un files/folders ke naam likhenge jo Docker\n"
        "# image mein COPY nahi honi chahiye (jaise: __pycache__, .git, data/raw/*.csv agar bohot bara ho)\n"
        "__pycache__/\n*.pyc\n.git\n.env\nnotebooks/\n",

    # ===================== CONFIG FILES =====================
    "config/model.yaml":
        "# yahan har tier ke model hyperparameters\n"
        "# (jaise Ridge ka alpha range, RandomForest ka n_estimators) YAML format mein\n"
        "# define karenge - taake code badle bina settings change ho saken.\n",
    "config/schema.yaml":
        "# yahan raw dataset ka EXPECTED schema define karenge\n"
        "# (kaunse columns hone chahiye, kya data type, kya range) -\n"
        "# data_validation.py isko use karega yeh check karne ke liye ke\n"
        "# naya data 'sahi shape' mein hai ya nahi.\n",
}


# -----------------------------------------------------------------------
# TIER-SPECIFIC FILES (5 tiers, har ek ka apna components/ folder)
# -----------------------------------------------------------------------

TIERS = {
    "tier1_clv": {
        "full_name": "Tier 1: Customer Lifetime Value (CLV) - Regression",
        "target": "Monetary (future/total customer spend)",
        "algorithms": "Linear, Ridge, Lasso, ElasticNet, SVR, Decision Tree Regressor, Random Forest Regressor",
    },
    "tier2_churn": {
        "full_name": "Tier 2: Churn Prediction - Classification",
        "target": "Churned (0/1, based on 90-day inactivity rule)",
        "algorithms": "Logistic Regression, Naive Bayes, Decision Tree, SVM, Random Forest",
    },
    "tier3_segmentation": {
        "full_name": "Tier 3: Customer Segmentation - Unsupervised Clustering",
        "target": "None (Unsupervised) - groups customers by RFM similarity",
        "algorithms": "K-Means, Hierarchical Clustering",
    },
    "tier4_demand_forecast": {
        "full_name": "Tier 4: Demand Forecasting - Time Series Regression",
        "target": "Daily/Weekly aggregated Sales",
        "algorithms": "ARIMA, Prophet, Linear Regression with time-based features",
    },
    "tier5_recommendation": {
        "full_name": "Tier 5: Product Recommendation - Similarity-based",
        "target": "None (traditional) - 'customers who bought X also bought Y'",
        "algorithms": "Cosine Similarity, Collaborative Filtering",
    },
}

COMPONENT_FILES = {
    "__init__.py":
        lambda tier, info: f'"""Components package for {info["full_name"]}."""\n',

    "data_ingestion.py":
        lambda tier, info: f'''"""
data_ingestion.py  ({tier})
{"-" * (20 + len(tier))}
Raw dataset (Online Retail II) ko load karta hai aur is TIER ke liye
relevant raw slice nikalta hai (zyada tar sab tiers SAME raw data se
shuru honge - yeh shared cleaning ke baad ka data hoga).

Target/Goal: {info["target"]}

Yahan function banayenge jaise:
    def initiate_data_ingestion() -> DataIngestionArtifact:
        # 1. Cleaned data load karo (shared cleaning module se)
        # 2. Train/Test split karo
        # 3. train.csv, test.csv save karo artifacts/ folder mein
        # 4. DataIngestionArtifact return karo (file paths ke sath)
"""
''',

    "data_validation.py":
        lambda tier, info: f'''"""
data_validation.py  ({tier})
{"-" * (21 + len(tier))}
Check karta hai ke ingested data EXPECTED schema follow karta hai ya
nahi (config/schema.yaml se compare karke) - missing columns, wrong
dtypes, ya data drift detect karta hai.

Yahan function banayenge jaise:
    def validate_schema(dataframe) -> bool:
        # column names match? dtypes match? missing % threshold se kam?
"""
''',

    "data_transformation.py":
        lambda tier, info: f'''"""
data_transformation.py  ({tier})
{"-" * (25 + len(tier))}
FEATURE ENGINEERING yahan hoti hai - raw/validated data ko is tier ke
liye specific features mein convert karta hai, aur Scaling apply karta hai.

Target/Goal: {info["target"]}

Yahan banayenge:
    def transform_data(dataframe):
        # 1. Tier-specific features banao (RFM, ya time-aggregates, etc.)
        # 2. Target variable banao (agar Supervised hai)
        # 3. StandardScaler fit/transform karo
        # 4. Transformed train/test arrays return karo
"""
''',

    "model_trainer.py":
        lambda tier, info: f'''"""
model_trainer.py  ({tier})
{"-" * (19 + len(tier))}
Yahan MULTIPLE algorithms train hote hain aur GridSearchCV se best
hyperparameters dhunde jate hain.

Algorithms to try: {info["algorithms"]}

Yahan banayenge:
    def train_models(X_train, y_train):
        # Har algorithm ke liye GridSearchCV/RandomizedSearchCV
        # Best model + best params return karo (sab algorithms ka
        # comparison bhi yahan ho sakta hai)
"""
''',

    "model_evaluation.py":
        lambda tier, info: f'''"""
model_evaluation.py  ({tier})
{"-" * (21 + len(tier))}
Trained model ko TEST data pe evaluate karta hai, aur decide karta hai
ke yeh model "accept" hoga ya "reject" (agar koi purana/baseline model
already deployed hai, to naye model ko us se BEHTAR hona chahiye).

Yahan banayenge:
    def evaluate_model(model, X_test, y_test) -> dict:
        # MAE/RMSE/R2 (Regression) ya Accuracy/F1/ROC-AUC (Classification)
        # return karega, aur ek boolean "is_model_accepted" bhi
"""
''',

    "model_pusher.py":
        lambda tier, info: f'''"""
model_pusher.py  ({tier})
{"-" * (18 + len(tier))}
Accepted/final model ko "production-ready" location pe save/push
karta hai (jahan se Flask app/prediction_pipeline.py isko load karega).

Yahan banayenge:
    def push_model(trained_model_path, final_model_dir):
        # Model ko models/{tier}/final_model.pkl jaisi jagah copy karo
        # (Future mein: AWS S3 jaisi cloud storage pe bhi push kar sakte hain)
"""
''',
}


def write_file(filepath: Path, content: str):
    """Helper: Folder banata hai (agar na ho), aur file likhta hai (agar khali/missing ho)."""
    filedir = filepath.parent
    if str(filedir) != "":
        os.makedirs(filedir, exist_ok=True)

    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        with open(filepath, "w") as f:
            f.write(content)
    else:
        print(f"File already present (skipped): {filepath}")


def main():
    created_count = 0

    # ---- 1. SHARED files (configuration, constants, entity, exception, logger, utils, pipeline, app-level) ----
    for filepath_str, content in DOCSTRINGS.items():
        write_file(Path(filepath_str), content)
        created_count += 1

    # ---- 2. ROOT __init__.py for project_name explicitly (already in DOCSTRINGS, skip dup) ----

    # ---- 3. TIER-SPECIFIC folders: components/, entity overrides not needed (shared entity reused) ----
    for tier, info in TIERS.items():
        for fname, content_fn in COMPONENT_FILES.items():
            filepath = Path(f"{project_name}/{tier}/components/{fname}")
            write_file(filepath, content_fn(tier, info))
            created_count += 1

        # Each tier also gets its own __init__.py at the tier root level
        tier_init = Path(f"{project_name}/{tier}/__init__.py")
        write_file(tier_init, f'"""{info["full_name"]} package."""\n')
        created_count += 1

    # ---- 4. Flask app folder (routes per tier) ----
    flask_routes = {
        "app/__init__.py":
            '"""Flask application factory package."""\n',
        "app/routes/__init__.py":
            '"""Routes package - har tier ka apna Blueprint file."""\n',
        "app/routes/clv_routes.py":
            '"""\nclv_routes.py\n---------------\nFlask Blueprint for Tier 1 (CLV) endpoints.\n\nYahan banayenge:\n    @clv_bp.route("/predict/clv", methods=["POST"])\n    def predict_clv():\n        # request.json se input lo, prediction_pipeline call karo, JSON return karo\n"""\n',
        "app/routes/churn_routes.py":
            '"""\nchurn_routes.py\n-----------------\nFlask Blueprint for Tier 2 (Churn) endpoints.\n\nYahan banayenge:\n    @churn_bp.route("/predict/churn", methods=["POST"])\n    def predict_churn():\n        # request.json se input lo, prediction_pipeline call karo, JSON return karo\n"""\n',
        "app/routes/segment_routes.py":
            '"""\nsegment_routes.py\n-------------------\nFlask Blueprint for Tier 3 (Segmentation) endpoints.\n"""\n',
        "app/routes/forecast_routes.py":
            '"""\nforecast_routes.py\n--------------------\nFlask Blueprint for Tier 4 (Demand Forecast) endpoints.\n"""\n',
        "app/routes/recommend_routes.py":
            '"""\nrecommend_routes.py\n---------------------\nFlask Blueprint for Tier 5 (Recommendation) endpoints.\n"""\n',
        "app/templates/.gitkeep": "",
        "app/static/.gitkeep": "",
    }
    for filepath_str, content in flask_routes.items():
        write_file(Path(filepath_str), content)
        created_count += 1

    # ---- 5. Data and artifact folders ----
    data_folders = {
        "data/raw/.gitkeep": "",
        "data/processed/.gitkeep": "",
        "models/.gitkeep": "",
        "notebooks/.gitkeep": "",
        "tests/__init__.py": '"""Unit tests package."""\n',
    }
    for filepath_str, content in data_folders.items():
        write_file(Path(filepath_str), content)
        created_count += 1

    print(f"\nDone! {created_count} files/folders processed.")
    print(f"Project root: {project_name}/")


if __name__ == "__main__":
    main()
