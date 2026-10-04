#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 22:12:49 2025

@author: Vaishali Siddeshwar
"""
from sklearn.metrics import mean_squared_error, r2_score

# 4. ModelEvaluator Class
class ModelEvaluator:
    def evaluate(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        return mse, r2
