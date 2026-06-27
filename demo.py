import sys
import pandas as pd

from customer_intelligence_suite.logger import logging
from customer_intelligence_suite.exception.exception import CustomerIntelligenceException


def load_dataset():
    """
    Jaan-boojh kar GALAT file path diya hai - taake error trigger ho
    aur hum dekh saken ke logging + custom exception sahi kaam kar
    rahe hain ya nahi.
    """
    try:
        logging.info("Trying to load the dataset...")
        df = pd.read_csv("data/raw/online_retail_ii.csv")  # Yeh file abhi exist nahi karti
        logging.info("Dataset loaded successfully.")
        return df

    except Exception as e:
        logging.error("An error occurred while loading the dataset.")
        raise CustomerIntelligenceException(e, sys) from e


if __name__ == "__main__":
    try:
        load_dataset()
    except CustomerIntelligenceException as e:
        print("Custom Exception Caught:")
        print(e)