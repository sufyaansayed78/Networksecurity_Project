from Networksecurity.Components.data_ingestion import DataIngestion
from Networksecurity.exception.exception import NetwrorkSecurityException
from Networksecurity.Logging.logger import logging 
from Networksecurity.entity.config_entity import DataIngestionConfig,DataTransformationConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig
from Networksecurity.Components.data_validation import DataValidation
from Networksecurity.Components.data_validation import DataValidationConfig
from Networksecurity.Components.data_transformation import DataTransformation
import sys 





if __name__=="__main__":
  try : 
    trainingpipelineconfig = TrainingPipelineConfig()
    dataingestionconfig = DataIngestionConfig(trainingpipelineconfig) 
    dataingestion = DataIngestion(dataingestionconfig)
    data_validation_config = DataValidationConfig(trainingpipelineconfig)
    logging.info("Initiate the data ingestion")
    dataingestionartifact = dataingestion.initiate_data_ingestion()
    logging.info("Data initiation completed")
    data_validation = DataValidation(dataingestionartifact,data_validation_config)
    logging.info("Initiated Data Validation")
    data_validation_artifact = data_validation.initiate_data_validation()
    logging.info("data validation completed")
    #print(data_validation_artifact)
    data_transformation_config = DataTransformationConfig(training_pipeline_config=trainingpipelineconfig)
    data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)
    data_transformation_artifact = data_transformation.initiate_data_transformation()
    #print(data_transformation_artifact)
    logging.info("Data Transformation Completed")
  except Exception as e :
    raise NetwrorkSecurityException(e,sys)















