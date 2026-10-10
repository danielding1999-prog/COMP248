import pandas as pd
from config import DATA_PATH, COLUMN_MAPPING

class Updater:
    def __init__(self, new_forecast, csvloader, Transformer, writer):
        self.forecast = new_forecast
        self.csvreader = csvloader
        self.Transformer = Transformer
        self.writer = writer

    def read_csv(self):
        self.weather_data = self.csvreader.load_CSV()

    def update(self):
        df = self.Transformer.concat_data(self.weather_data, self.forecast, COLUMN_MAPPING).drop_duplicates(subset=["Date/Time"], keep='last')
        self.writer.write(df)