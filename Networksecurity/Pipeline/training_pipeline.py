from Networksecurity.Components.data_ingestion import DataIngestion
from Networksecurity.exception.exception import NetwrorkSecurityException
from Networksecurity.Logging.logger import logging 
from Networksecurity.entity.config_entity import DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig
from Networksecurity.Components.data_validation import DataValidation
from Networksecurity.Components.data_validation import DataValidationConfig
from Networksecurity.Components.data_transformation import DataTransformation
from Networksecurity.Components.Model_trainer import ModelTrainer
import sys 

from Networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from Networksecurity.entity.artifacts_entity import(
    DataIngestionArtifact,
    DataTransformationArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact,
)

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Start data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info('Data ingestion completed')
            return data_ingestion_artifact

        except Exception as e :
            raise NetwrorkSecurityException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_ingestion_artifact
        except Exception as e :
            raise NetwrorkSecurityException(e,sys)

    def start_data_transformation(self,data_validation_artifact:DataTransformationArtifact):
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise NetwrorkSecurityException(e,sys)
   

    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact)-> ModelTrainerArtifact:
        try:
            self.model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config,

            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e :
            raise NetwrorkSecurityException(e,sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_validation_artifact=data_ingestion_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_ingestion_artifact)
            return model_trainer_artifact
        except Exception as e:
            raise NetwrorkSecurityException(e,sys)



















