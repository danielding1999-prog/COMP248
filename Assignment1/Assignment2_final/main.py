from csvloader import CSVloader
from extractor import Extractor
from config import DATA_PATH
from Transformer import Transformer
from updater import Updater
import pandas as pd
from pathlib import Path


def main():

    file_path = Path('Weather_Data.csv')
    if not file_path.is_file():
        forecast_data = Extractor(["temperature_2m_max", "temperature_2m_min"]).load_meteo_data()
        loadCSV = CSVloader(DATA_PATH)
        historical_data = loadCSV.load_CSV()
        transformer = Transformer(["Date/Time", "Max Temp (°C)", "Min Temp (°C)"])
        historical_data_edit = transformer.get_target_columns(historical_data)
        # add data type to both historical dataframe and forecast dataframe
        historical_data_edit['Data_type'] = 'Historical'
        forecast_data['Data_type'] = 'Forecast'
        transformed_df = transformer.concat_data(historical_data_edit, forecast_data, column_mapping = { "temperature_2m_max":"Max Temp (°C)", "temperature_2m_min":"Min Temp (°C)" })
        # remove rows that have NAN in the fields
        transformed_df = transformed_df.dropna()
        # output a csv file so external system can use this
        transformed_df.to_csv("./Weather_Data.csv", index = False)
        print(1,2,3)
        
    # I think i should check if the weather_data.csv file exist, it it does not exist, the above code should be initiated
    # if it does exit, calling the dataupdater should be sufficient

    # I need a class that just fetch the right field from Meteo API
    # I need a class that could transform data into dataframe
    # I need a class that reads the csv file
    # I need to figure out how to not write the above code again
    else:

        new_forecast = Extractor(["temperature_2m_max", "temperature_2m_min"]).load_meteo_data()
        updater = Updater(new_forecast, CSVloader("./Weather_Data.csv"))
        weather_data = updater.read_csv()
        forecast_data = updater.locate_records(weather_data, 'Data_type', 'Forecast')
        print(forecast_data)



if __name__ == "__main__":
    main()