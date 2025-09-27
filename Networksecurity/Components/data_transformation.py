import sys
import numpy as np
import os 
import pandas as pd 
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline


from Networksecurity.constants.training_pipeline import TARGET_COLUMN
from Networksecurity.constants.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from Networksecurity.entity.artifacts_entity import (
    DataTransformationArtifact,DataValidationArtifact
)

from Networksecurity.entity.config_entity import DataTransformationConfig
from Networksecurity.exception.exception import NetwrorkSecurityException
from Networksecurity.Logging.logger import logging 
from Networksecurity.utils.main_utils.utils1 import save_numpy_array,save_object


class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config



        except Exception as e :
            raise NetwrorkSecurityException(e,sys)
        

    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e :
            raise NetwrorkSecurityException(e,sys)
        
    def get_data_transformer_object(cls)->Pipeline:
        
        try :
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            processor:Pipeline = Pipeline(
                steps=[("imputer",imputer)]
            )
            return processor
        except Exception as e :
            raise NetwrorkSecurityException(e,sys)



        
    
    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            input_feature_train_df = train_df.drop(columns=TARGET_COLUMN,axis=1 )
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)

            input_feature_test_df = test_df.drop(columns=TARGET_COLUMN,axis=1 )
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1,0)
            preprocessor = self.get_data_transformer_object()
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor_object.transform(input_feature_test_df)
            train_arr = np.c_[transformed_input_train_feature,np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature,np.array(target_feature_test_df)]
            save_numpy_array(self.data_transformation_config.transformed_train_file_path,train_arr)
            save_numpy_array(self.data_transformation_config.transformed_test_file_path,test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor_object)
            
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                trasnformed_test_file_path=self.data_transformation_config.transformed_test_file_path,


            )
            return data_transformation_artifact

            
        except Exception as e :
            raise NetwrorkSecurityException(e,sys)
         










































