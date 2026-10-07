from csvloader import CSVloader
from extractor import MeteoLoader
from config import DATA_PATH
from Transformer import Transformer
import pandas as pd


def main():
    historical_data = CSVloader(DATA_PATH)
    forecast_data = MeteoLoader(["temperature_2m_max", "temperature_2m_min"])
    h = historical_data.load_CSV()
    f = forecast_data.load_meteo_data()
    transformer = Transformer(["Date/Time", "Max Temp (°C)", "Min Temp (°C)"])
    e = transformer.get_target_columns(h)
    # print(e)
    
    # f = f.rename(columns={"temperature_2m_max": "Max Temp (°C)", "temperature_2m_min": "Min Temp (°C)"})
    # print(f)
    transformed_df = transformer.concat_data(e, f, column_mapping = { "temperature_2m_max":"Max Temp (°C)", "temperature_2m_min":"Min Temp (°C)" })
    # f = f.rename(columns={"temperature_2m_max": "Max Temp (°C)", "temperature_2m_min": "Min Temp (°C)"})
    print(transformed_df)
    # print(f)



if __name__ == "__main__":
    main()