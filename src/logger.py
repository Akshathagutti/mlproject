import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'log',LOG_FILE)
os.makedirs(logs_path,exist_ok=False)

LOG_PATH_FILE = os.path.join(logs_path)

logging.basicConfig(
    filename=LOG_PATH_FILE,
     format = "[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
     level=logging.INFO
)

if __name__ == "__main__":
    logging.info("logging is started...")