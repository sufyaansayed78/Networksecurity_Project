import yaml 
from Networksecurity.exception.exception import NetwrorkSecurityException
from Networksecurity.Logging.logger import logging 
import os,sys
import numpy as np 
import dill
import pickle 
#from Networksecurity.utils.main_utils.utils1 import read_yaml_file





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





























