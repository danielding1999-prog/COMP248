import pandas as pd

class CSVloader:
    def __init__ (self, CSV_path):
        self.CSV_path = CSV_path
        
    def load_CSV(self):
        df = pd.read_csv(self.CSV_path)
        return df
    