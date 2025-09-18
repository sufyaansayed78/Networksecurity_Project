import os 
import sys
import json
from dotenv import load_dotenv


load_dotenv()

Mongo_url = os.getenv("MONGODB_URL")
print(Mongo_url)

import certifi 
ca = certifi.where()    #retirevs a list of CA's ( Certificate Authorities ) 


import pandas as pd 
import numpy as np 
import pymongo 

from Networksecurity.exception.exception import NetwrorkSecurityException
#from Networksecurity.Logging.logger import logging 

class NetworkDataExtract():
    def __init__(self):
         try :
              pass
         except Exception as e :
              raise NetwrorkSecurityException(e,sys)
         
    def csv_to_json_convertor(self,file_path):
         try :
              data = pd.read_csv(file_path)
              data.reset_index(drop=True,inplace=True)
              records=list(json.loads(data.T.to_json()).values()) 
              return records
         except Exception as e :
              raise NetwrorkSecurityException(e,sys)


    def insert_data_mongdb(self,records,database,collection):
          try :
               
               self.database = database
               self.collection = collection 
               self.records = records

               self.mongoclient = pymongo.MongoClient(Mongo_url)
               self.database = self.mongoclient[self.database]
               self.collection=self.database[self.collection]
               self.collection.insert_many(self.records)

               return(len(self.records))
          except Exception as e :
               raise NetwrorkSecurityException(e,sys)

if __name__=='__main__':
   FILE_PATH = r'Network_Data\phisingData.csv'
   DATABASE = "Sufyaan"
   Collection = "NetworkData"
   networkobj = NetworkDataExtract()
   records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
   no_of_records = networkobj.insert_data_mongdb(records,DATABASE,Collection)
   print(no_of_records)














