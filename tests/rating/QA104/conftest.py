import os
from dotenv import load_dotenv
from pathlib import Path



load_dotenv()
# Загружает переменные из .env файла

# Теперь их можно использовать в тестах
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = os.getenv("BASE_URL")

BASE_HEADERS = {
    "Authorization": API_TOKEN
}