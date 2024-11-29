import sqlite3
import pandas as pd
from config.settings import PROCESSED_DATA_PATH, DB_PATH

def load_weather():
    processed_file = f"{PROCESSED_DATA_PATH}/weather_processed.csv"
    df = pd.read_csv(processed_file)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("weather", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    load_weather()
