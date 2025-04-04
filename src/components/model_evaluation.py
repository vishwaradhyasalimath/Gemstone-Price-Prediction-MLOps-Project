import os
import sys
from sklearn.metrics import mean_squared_error,mean_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.logger.logger import logging
from dataclasses import dataclass
from exception.exception import customexception
from src.utils.utils import load_object

@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def initate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)