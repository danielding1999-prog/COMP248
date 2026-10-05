#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 22:13:44 2025

@author: Vaishali Siddeshwar
"""

# 5. Predictor Class
class Predictor:
    # passing external object into the constructor to use it in the class methods
    def __init__(self, model, preprocessor):
        self.model = model
        self.preprocessor = preprocessor

    def predict(self, input_data):
        input_scaled = self.preprocessor.transform_new_data(input_data)
        return list(self.model.predict(input_scaled))
