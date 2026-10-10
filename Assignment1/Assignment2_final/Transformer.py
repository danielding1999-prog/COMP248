import pandas as pd

class Transformer:
    def __init__(self, df):
        self.df = df
        
    def get_target_columns(self, target_columns):
        return self.df[target_columns]  
    
    def concat_data(self, df1, df2, column_mapping):
        df2_renamed = df2.rename(columns=column_mapping)
        return pd.concat([df1, df2_renamed])

    