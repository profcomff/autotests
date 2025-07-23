import os
from dotenv import load_dotenv
from pathlib import Path
#BASE_DIR = Path(__file__).resolve().parent.parent
#os.getenv("/.env/.env")  # Можно переопределить через ОС


load_dotenv("C:/.env/.env")
# Загружает переменные из .env файла

# Теперь их можно использовать в тестах
api_token = os.getenv("API_TOKEN")
base_url = os.getenv("BASE_URL")