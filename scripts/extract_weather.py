import requests
import os
from config.settings import API_KEY, RAW_DATA_PATH

def extract_weather():
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"
    response = requests.get(api_url)
    response.raise_for_status()

    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    with open(f"{RAW_DATA_PATH}/weather.json", "w") as f:
        f.write(response.text)

if __name__ == "__main__":
    extract_weather()
