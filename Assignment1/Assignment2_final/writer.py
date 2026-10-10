class Writer:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def write(self, df):
        df.to_csv(self.file_path, index = False)