import sys
from src.exception import CustomException
from src.logger import logging  
from src.utils import load_object
import pandas as pd
import numpy as np


# Code to be replaced with actual training pipeline

class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info("Loading training data")
            data_path = 'artifacts/processed_data.csv'
            data = pd.read_csv(data_path)

            logging.info("Splitting features and target variable")
            X = data.drop(columns=['target'])
            y = data['target']

            logging.info("Loading preprocessor and model")
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model_path = 'artifacts/model.pkl'
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            logging.info("Transforming features")
            X_transformed = preprocessor.transform(X)
            logging.info("Training the model")
            model.fit(X_transformed, y)
            logging.info("Model training completed")
            return model
        except Exception as e:
            raise CustomException(e, sys)
        
