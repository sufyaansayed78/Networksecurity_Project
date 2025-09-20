from Networksecurity.Components.data_ingestion import DataIngestion
from Networksecurity.exception.exception import NetwrorkSecurityException
from Networksecurity.Logging.logger import logging 
from Networksecurity.entity.config_entity import DataIngestionConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig


import sys 





if __name__=="__main__":
  try : 
    trainingpipelineconfig = TrainingPipelineConfig()
    dataingestionconfig = DataIngestionConfig(trainingpipelineconfig) 
    dataingestion = DataIngestion(dataingestionconfig)
    logging.info("Initiate the data ingestion")
    dataingestionartifact = dataingestion.initiate_data_ingestion()
    print(dataingestionartifact)
  except Exception as e :
    raise NetwrorkSecurityException(e,sys)















