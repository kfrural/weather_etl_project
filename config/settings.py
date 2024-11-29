import os


API_URL = "https://www.metaweather.com/api/location"

CITY_WOEID = 44418 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_DATA_PATH = os.path.join(BASE_DIR, "../data/raw") 
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "../data/processed") 
DB_PATH = os.path.join(BASE_DIR, "../data/weather.db") 

os.makedirs(RAW_DATA_PATH, exist_ok=True)
os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
