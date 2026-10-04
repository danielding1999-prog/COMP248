#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 22:11:55 2025

@author: Vaishali Siddeshwar
"""
from config import TARGET_COLUMN, TEST_SIZE, RANDOM_STATE
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline


# 2. Preprocessor Class
class Preprocessor:
    def __init__(self):
        self.target_column = TARGET_COLUMN
        self.column_transformer = None
        self.feature_names_out = None

    def split_and_transform(self, df):
        X = df.drop(columns=[self.target_column])
        y = df[self.target_column]

        # Auto-detect column types
        numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

        # Save for external transformation
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features

        # Pipelines for numeric columns
        numeric_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ])

        # Pipelines for categorical columns
        categorical_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
        ])

        self.column_transformer = ColumnTransformer(transformers=[
            ('num', numeric_pipeline, numeric_features),
            ('cat', categorical_pipeline, categorical_features)
        ])

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

        # Fit and transform
        X_train_transformed = self.column_transformer.fit_transform(X_train)
        X_test_transformed = self.column_transformer.transform(X_test)

        # Save feature names for inspection
        self.feature_names_out = self.get_feature_names()

        return X_train_transformed, X_test_transformed, y_train, y_test

    def transform_new_data(self, input_data_dict):
        expected_columns = self.numeric_features + self.categorical_features
        input_df = pd.DataFrame(input_data_dict, columns=expected_columns)

        return self.column_transformer.transform(input_df)

    def get_feature_names(self):
        """Optional: to inspect final feature names"""
        num = self.numeric_features
        cat = self.column_transformer.named_transformers_['cat'].get_feature_names_out(self.categorical_features)
        return list(num) + list(cat)
