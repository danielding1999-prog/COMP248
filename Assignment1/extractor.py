import pandas as pd
import requests

class MeteoLoader:
    def __init__(self, weather_variable:list[str]):
        self.weather_variable = weather_variable
        
    def load_meteo_data(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 43.70,   # Toronto coordinates
            "longitude": -79.42,
            "daily": self.weather_variable,
            "timezone": "America/Toronto",
            "forecast_days": 16  # Get the next 16 days
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raises an error for bad status codes (4xx or 5xx)
            data = response.json()
            
            # Parse the JSON response into a DataFrame
            forecast_df = pd.DataFrame({var : data['daily'][var] for var in self.weather_variable})
            
            print("✓ Weather forecast data extracted from API.")
            return meteo_df
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error