import pandas as pd
import os
from config.settings import RAW_DATA_PATH, PROCESSED_DATA_PATH

def transform_weather():
    raw_file = f"{RAW_DATA_PATH}/weather.json"
    df = pd.read_json(raw_file)

    transformed_data = {
        "city": df["name"],
        "temperature_celsius": df["main"]["temp"] - 273.15,
        "humidity": df["main"]["humidity"],
        "weather": df["weather"][0]["description"]
    }
    df_transformed = pd.DataFrame([transformed_data])

    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    df_transformed.to_csv(f"{PROCESSED_DATA_PATH}/weather_processed.csv", index=False)

if __name__ == "__main__":
    transform_weather()
