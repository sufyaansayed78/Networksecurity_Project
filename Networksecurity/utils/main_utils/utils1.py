import yaml 
from Networksecurity.exception.exception import NetwrorkSecurityException
from Networksecurity.Logging.logger import logging 
import os,sys
import numpy as np 
import dill
import pickle 
from Networksecurity.entity.artifacts_entity import ClassificationMatrixArtifact
from sklearn.metrics import f1_score,precision_score,recall_score,r2_score
from sklearn.model_selection import GridSearchCV



def read_yaml_file(filepath:str) -> dict:
    try:
        with open(filepath,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e :
        raise NetwrorkSecurityException(e,sys) from e 
    

def write_yaml_file(file_path:str,content:object,replace:bool = False)-> None:
    try :
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)
        
    except Exception as e :
        raise NetwrorkSecurityException(e,sys)

def save_numpy_array(file_path:str , array : np.array):
    try :
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)

    except Exception as e :
        raise NetwrorkSecurityException(e,sys) from e 

def save_object(filepath : str ,obj : object):

  try:
    logging.info("Saving the object as a pickle file")

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    #print("PREPROCESSOR FILE PATH ------------",p)
    with open(filepath,"wb") as fobj:
        pickle.dump(obj,fobj)
    logging.info("Object successfully saved as a pickle file ")
  except Exception as e:
      raise NetwrorkSecurityException(e,sys)


def load_numpy_array(filepath:str):
    try:
        with open(filepath,'rb') as obj:
            nparr = np.load(obj)
        return nparr 
    except Exception as e :
        raise NetwrorkSecurityException(e,sys)


def load_object(filepath:str):
    try :
        with open(filepath,'rb') as obj:
            return pickle.load(obj)
        
    except Exception as e :
        raise NetwrorkSecurityException(e,sys)


def classification_matrix(y_true,y_pred)->ClassificationMatrixArtifact:
    try:
        model_f1_sscore = f1_score(y_true,y_pred)
        model_recall_score = recall_score(y_true,y_pred)
        model_precision_score = precision_score(y_true,y_pred)

        classification_matrix = ClassificationMatrixArtifact(f1_score=model_f1_sscore,precision_score=model_precision_score,recall_score=model_recall_score)
        return classification_matrix
    except Exception as e:
        raise NetwrorkSecurityException(e,sys)
    
def evaluate_models(x_train,y_train,x_test,y_test,models,params):
    report = {}
    for model in models:
        grid = GridSearchCV(estimator=models[model],param_grid=params[model])
        grid.fit(x_train,y_train)
        models[model].set_params(**grid.best_params_)
        models[model].fit(x_train,y_train)

        y_train_pred = models[model].predict(x_train)
        y_test_pred = models[model].predict(x_test)
        train_model_score = r2_score(y_train,y_train_pred)
        test_model_score = r2_score(y_test,y_test_pred)
        report[model] = test_model_score

    return report 


class NetworkModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor 
            self.model = model 
        except Exception as e :
            raise NetwrorkSecurityException(e,sys)
    

    






















        























