#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 22:13:13 2025

@author: Vaishali Siddeshwar
"""
import pandas as pd

# 1. DataLoader Class
class DataLoader:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        df = pd.read_csv(self.path)
        return df
