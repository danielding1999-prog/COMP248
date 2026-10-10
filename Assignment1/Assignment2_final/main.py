from csvloader import CSVloader
from extractor import Extractor
from config import DATA_PATH, COLUMN_MAPPING, URL
from Transformer import Transformer
from updater import Updater
import pandas as pd
from pathlib import Path



def main():

    file_path = Path('Weather_Data.csv')
    if not file_path.is_file():
        extractor = Extractor(URL)
        loader = CSVloader(DATA_PATH)
        transformer = Transformer(loader.load_CSV())
        historical_data = transformer.get_target_columns(['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)', "Total Precip (mm)"]).dropna()
        forecast_data = extractor.extract(["temperature_2m_max", "temperature_2m_min", "precipitation_sum"])
        historical_data['Data_type'] = 'Historical'
        forecast_data['Data_type'] = 'Forecast'
        Weather_data = transformer.concat_data(historical_data, forecast_data, COLUMN_MAPPING)
        Weather_data.to_csv("./Weather_Data.csv", index = False)
        
    else:
        extractor = Extractor(URL)
        new_forecast = extractor.extract(["temperature_2m_max", "temperature_2m_min"])
        new_forecast['Data_type'] = 'Forecast'
        updater = Updater(new_forecast, CSVloader("./Weather_Data.csv"))
        updater.read_csv()
        updater.update()


if __name__ == "__main__":
    main()