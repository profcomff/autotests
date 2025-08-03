import os
from dotenv import load_dotenv
from pathlib import Path



load_dotenv()
# Загружает переменные из .env файла

# Теперь их можно использовать в тестах
BASE_API_TOKEN_RATING = os.getenv("API_TOKEN_RATING")
print(BASE_API_TOKEN_RATING)
BASE_URL = os.getenv("BASE_URL")
print(BASE_URL)
API_TOKEN_USER_A = os.getenv("API_TOKEN_USER_A")
BASE_HEADERS = {
    "Authorization": BASE_API_TOKEN_RATING
}
HEADERS_USER_A = {
    "Authorization": API_TOKEN_USER_A
}