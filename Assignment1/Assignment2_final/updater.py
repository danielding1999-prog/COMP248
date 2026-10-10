from csvloader import CSVloader
import pandas as pd
from config import DATA_PATH, COLUMN_MAPPING

class Updater:
    def __init__(self, new_forecast, csvloader):
        self.forecast = new_forecast
        self.csvreader = csvloader

    # read the original weather_data.csv file
    def read_csv(self):
        self.weather_data = self.csvreader.load_CSV()

    def update(self):
        forecast_renamed = self.forecast.rename(columns = COLUMN_MAPPING)
        pd.concat([self.weather_data, forecast_renamed]).drop_duplicates(subset=["Date/Time"], keep='last').to_csv("./Weather_Data.csv", index = False)

    # find the new rows of forecast data

    # append the row in the weather_data.csv