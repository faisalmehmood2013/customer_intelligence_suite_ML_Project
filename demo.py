import os
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge

from customer_intelligence_suite.logger import logging
from customer_intelligence_suite.exception.exception import CustomerIntelligenceException
from customer_intelligence_suite.utils.main_utils import (
    read_yaml_file,
    write_yaml_file,
    save_object,
    load_object,
    save_numpy_array_data,
    load_numpy_array_data,
    read_csv_data,
    drop_columns,
)


def run_demo():
    logging.info("===== DEMO START: Testing all utils functions =====")

    os.makedirs("demo_artifacts", exist_ok=True)

    # ---------------------------------------------------------------
    # 1. read_csv_data - ek sample CSV banate hain aur padhte hain
    # ---------------------------------------------------------------
    sample_df = pd.DataFrame({
        "CustomerID": [101, 102, 103],
        "Quantity": [10, 5, 8],
        "UnitPrice": [2.5, 5.0, 1.5],
    })
    sample_df.to_csv("demo_artifacts/sample_data.csv", index=False)
    loaded_df = read_csv_data("demo_artifacts/sample_data.csv")
    print("\n[1] read_csv_data output:\n", loaded_df)

    # ---------------------------------------------------------------
    # 2. drop_columns - CustomerID hata kar dekhte hain (ID column,
    #    model feature ke liye useless - jo humne pehle discuss kiya)
    # ---------------------------------------------------------------
    df_without_id = drop_columns(loaded_df, columns_to_drop=["CustomerID"])
    print("\n[2] drop_columns output (CustomerID removed):\n", df_without_id)

    # ---------------------------------------------------------------
    # 3. write_yaml_file + read_yaml_file - config jaisa data save karna
    # ---------------------------------------------------------------
    sample_config = {"ridge": {"alpha": [0.1, 1, 10]}}
    write_yaml_file("demo_artifacts/sample_config.yaml", sample_config, replace=True)
    loaded_config = read_yaml_file("demo_artifacts/sample_config.yaml")
    print("\n[3] YAML write+read output:", loaded_config)

    # ---------------------------------------------------------------
    # 4. save_numpy_array_data + load_numpy_array_data
    # ---------------------------------------------------------------
    dummy_array = df_without_id.to_numpy()
    save_numpy_array_data("demo_artifacts/sample_array.npy", dummy_array)
    loaded_array = load_numpy_array_data("demo_artifacts/sample_array.npy")
    print("\n[4] Numpy array save+load output:\n", loaded_array)

    # ---------------------------------------------------------------
    # 5. save_object + load_object - ek dummy model ke sath
    # ---------------------------------------------------------------
    dummy_model = Ridge(alpha=2.0)
    save_object("demo_artifacts/dummy_ridge_model.pkl", dummy_model)
    loaded_model = load_object("demo_artifacts/dummy_ridge_model.pkl")
    print("\n[5] Model save+load output - alpha value:", loaded_model.alpha)

    logging.info("===== DEMO END: All utils functions ran successfully =====")
    print("\nALL UTILS FUNCTIONS WORKED CORRECTLY - no errors.")


if __name__ == "__main__":
    try:
        run_demo()
    except Exception as e:
        raise CustomerIntelligenceException(e, sys) from e