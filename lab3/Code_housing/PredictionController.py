#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 22:15:00 2025

@author: Vaishali Siddeshwar
"""
import pandas as pd
from Predictor import Predictor

class PredictionController:
    def __init__(self, model, preprocessor):
        self.model = model
        self.preprocessor = preprocessor

    def predict_single_instance(self, sample_dict):
        """
        Receives a dictionary of a single house instance from the UI,
        wraps it into a pandas DataFrame, and passes it to the predictor.
        """
        # Wrap the single dictionary in a list so pandas creates a 1-row DataFrame
        input_df = pd.DataFrame([sample_dict])
        
        # Instantiate and call the Predictor
        predictor = Predictor(self.model, self.preprocessor)
        predictions = predictor.predict(input_df)
        
        # Return the first prediction value
        return predictions[0]