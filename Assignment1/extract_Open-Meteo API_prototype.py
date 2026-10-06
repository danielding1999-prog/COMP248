import requests
import pandas as pd
def extract_forecast_data():
    """
    Extracts weather forecast data from the Open-Meteo API.
    
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.70,   # Toronto coordinates
        "longitude": -79.42,
        "daily": ["temperature_2m_max", "temperature_2m_min", "rain_sum"],
        "timezone": "America/Toronto",
        "forecast_days": 16  # Get the next 16 days
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an error for bad status codes (4xx or 5xx)
        data = response.json()
        print(data)
        
        # Parse the JSON response into a DataFrame
        forecast_df = pd.DataFrame({
            'date': pd.to_datetime(data['daily']['time']),
            'temp_max': data['daily']['temperature_2m_max'],
            'temp_min': data['daily']['temperature_2m_min'],
            'rain_sum': data['daily']['rain_sum'],
            'data_type': 'forecast'  # Add a label to distinguish from historical data
            # return true if the data is forecast data, false if it is historical data
        })
        forecast_df['is_forecast'] = forecast_df['data_type'] == 'forecast'

        
        
        
        print("✓ Weather forecast data extracted from API.")
        return forecast_df
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error
forecast_df = extract_forecast_data()
# print(forecast_df)