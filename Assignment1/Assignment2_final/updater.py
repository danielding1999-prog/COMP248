from csvloader import CSVloader
import pandas as pd
from config import DATA_PATH

class Updater:
    def __init__(self, new_forecast, csvloader):
        self.forecast = new_forecast
        self.csvreader = csvloader

    # read the original weather_data.csv file
    def read_csv(self):
        return self.csvreader.load_CSV()
    # extract the data that has the data_type forecast001214
    def locate_records(self, dataset, column_name, data):
        return dataset.loc[dataset[column_name] == data]
    # compare with the new_forecast data

    # find the new rows of forecast data

    # append the row in the weather_data.csv