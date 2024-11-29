import json
import pandas as pd
import os
from config.settings import RAW_DATA_PATH, PROCESSED_DATA_PATH

def transform_weather():
    raw_file_path = os.path.join(RAW_DATA_PATH, "weather.json")

    with open(raw_file_path, "r") as file:
        data = json.load(file)

    weather_data = data["consolidated_weather"]
    df = pd.DataFrame(weather_data)

    df_transformed = df[["applicable_date", "weather_state_name", "min_temp", "max_temp", "the_temp"]]
    df_transformed.rename(columns={
        "applicable_date": "date",
        "weather_state_name": "weather",
        "min_temp": "min_temp_c",
        "max_temp": "max_temp_c",
        "the_temp": "current_temp_c"
    }, inplace=True)

    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    processed_file_path = os.path.join(PROCESSED_DATA_PATH, "weather_processed.csv")
    df_transformed.to_csv(processed_file_path, index=False)

    print(f"Dados transformados e salvos em: {processed_file_path}")

if __name__ == "__main__":
    transform_weather()
