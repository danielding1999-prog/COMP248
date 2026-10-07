import pandas as pd

class Transformer:
    def __init__(self, TARGET_COLUMNS):
        self.target_columns = TARGET_COLUMNS
        
    def get_target_columns(self, df):
        new_df = df[self.target_columns]
        return new_df
    
    def concat_data(self, df1, df2, column_mapping):
        df2_renamed = df2.rename(columns=column_mapping)
        return pd.concat([df1, df2_renamed])