#Data ingestion is the process of importing large,
# assorted data files from multiple sources into a single,
# cloud-based storage medium
import os
import sys
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
from src.component.data_transformation import DataTransformation
## intitialize the Data Ingestion configuration
#In Python, a data class is a class that is designed to only hold data values.
# They aren't different from regular classes, but they usually don't have any other
# methods. They are typically used to store information that will be passed
# between different parts of a program or a system
@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## create the data ingestion class
#we want to create a class without any variable that why we use dataclass
#for not using __init__ we use dataclass

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()#above all three path will be get in ingestion_config

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')
#exception hsndling is used to resolve run time error
        try:
            df=pd.read_csv(os.path.join('Notebook/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            # os.path.dirname() is used to get the directory name from the specified path.
            #exit_ok=true used because if directry exist it will not make
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info('Raw data is created')

            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
            #saving train   and test data
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            logging.info('Exception occured at Data Ingestion Stage')
            raise CustomException(e,sys)

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path,test_data_path)