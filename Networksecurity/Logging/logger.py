import logging
import os 
from  datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"LOGS",LOG_FILE)
#os.makedirs(logs_path,exist_ok=True)
#print(logs_path)
#LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(filename=logs_path,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO,

                    )

























