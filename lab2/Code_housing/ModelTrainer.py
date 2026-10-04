#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 22:12:28 2025

@author: Vaishali Siddeshwar
"""
from sklearn.linear_model import LinearRegression

# 3. ModelTrainer Class
class ModelTrainer:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def get_model(self):
        return self.model