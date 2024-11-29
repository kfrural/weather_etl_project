import requests
import os
from config.settings import API_URL, CITY_WOEID, RAW_DATA_PATH


def extract_weather():
    url = f"{API_URL}/{CITY_WOEID}/"
    response = requests.get(url)
    response.raise_for_status()  

    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    raw_file_path = os.path.join(RAW_DATA_PATH, "weather.json")
    with open(raw_file_path, "w") as file:
        file.write(response.text)

    print(f"Dados extraídos e salvos em: {raw_file_path}")

if __name__ == "__main__":
    extract_weather()
