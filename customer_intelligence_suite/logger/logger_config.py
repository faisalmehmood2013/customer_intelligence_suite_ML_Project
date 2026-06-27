import logging
import os
from datetime import datetime

from from_root import from_root

LOG_DIR = "logs"
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_DIR_PATH = os.path.join(from_root(), LOG_DIR)
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE_NAME)


def configure_logger() -> None:
    os.makedirs(LOG_DIR_PATH, exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )