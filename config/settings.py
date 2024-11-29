import os

API_KEY = "sua_api_key_aqui"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_PATH = os.path.join(BASE_DIR, "../data/raw")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "../data/processed")
DB_PATH = os.path.join(BASE_DIR, "../data/weather.db")
