import pandas as pd
import requests
from config import URL

class Extractor:
    def __init__(self, weather_variable:list[str]):
        self.weather_variable = weather_variable
        
    def load_meteo_data(self):
        params = {
            "latitude": 43.70,   # Toronto coordinates
            "longitude": -79.42,
            "daily": self.weather_variable,
            "timezone": "America/Toronto",
            "forecast_days": 16  # Get the next 16 days
        }
        
        try:
            response = requests.get(URL, params=params)
            response.raise_for_status()  # Raises an error for bad status codes (4xx or 5xx)
            data = response.json()
            
            # Parse the JSON response into a DataFrame
            forecast_df = pd.DataFrame({
                var : data['daily'][var] for var in self.weather_variable})
            forecast_df['Date/Time'] = pd.to_datetime(data['daily']['time'])

            
            print("✓ Weather forecast data extracted from API.")
            
            return forecast_df
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error