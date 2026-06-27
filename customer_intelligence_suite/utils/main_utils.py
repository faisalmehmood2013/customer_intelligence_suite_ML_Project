import os
import sys

import joblib
import numpy as np
import pandas as pd
import yaml

from customer_intelligence_suite.exception.exception import CustomerIntelligenceException
from customer_intelligence_suite.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a Python dictionary.

    Used for: reading config/model.yaml (hyperparameter ranges) and
    config/schema.yaml (expected dataset columns) across every tier.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes a Python dictionary/object to a YAML file.

    Used for: saving things like the best hyperparameters found by
    GridSearchCV, so they can be reviewed or reused later.
    """
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    """
    Saves any Python object (a trained model, a fitted scaler, etc.)
    to disk using joblib.

    Used in: every tier's model_trainer.py / model_pusher.py, to
    persist trained models and preprocessing objects.
    """
    try:
        logging.info(f"Saving object to file: {file_path}")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            joblib.dump(obj, file_obj)
        logging.info(f"Object saved successfully at: {file_path}")
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e


def load_object(file_path: str) -> object:
    """
    Loads a previously saved Python object (model, scaler) back from disk.

    Used in: prediction_pipeline.py and the Flask app, to load a
    trained model when making predictions on new data.
    """
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} does not exist")
        with open(file_path, "rb") as file_obj:
            return joblib.load(file_obj)
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e


def save_numpy_array_data(file_path: str, array: np.ndarray) -> None:
    """
    Saves a numpy array (e.g. scaled/transformed features) to disk.

    Used in: data_transformation.py, to persist the processed
    train/test arrays so model_trainer.py can load them later
    without redoing the transformation.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.ndarray:
    """
    Loads a previously saved numpy array back from disk.

    Used in: model_trainer.py, to load the processed features that
    data_transformation.py saved earlier.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e


def read_csv_data(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file into a pandas DataFrame, with consistent
    logging and error handling.

    Used in: every tier's data_ingestion.py, to load the raw or
    cleaned dataset.
    """
    try:
        logging.info(f"Reading CSV file from: {file_path}")
        return pd.read_csv(file_path)
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e


def drop_columns(df: pd.DataFrame, columns_to_drop: list) -> pd.DataFrame:
    """
    Drops a given list of columns from a DataFrame, if they exist.

    Generic/reusable: any tier can pass its own list of columns to
    drop (e.g. ID columns that aren't useful as model features).
    Tier-specific column names stay in that tier's own code, not here.
    """
    try:
        existing_cols = [col for col in columns_to_drop if col in df.columns]
        logging.info(f"Dropping columns: {existing_cols}")
        return df.drop(columns=existing_cols)
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e