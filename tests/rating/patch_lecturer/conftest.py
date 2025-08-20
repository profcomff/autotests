import pytest
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_token():
    BASE_URL = os.getenv("BASE_URL")
    LOGIN_RATING = os.getenv("LOGIN_RATING")
    PASSWORD_RATING = os.getenv("PASSWORD_RATING")
    url = f"{BASE_URL}/auth/email/login"
    data ={
          "email": LOGIN_RATING,
          "password": PASSWORD_RATING,
          "scopes":[],
          "session_name": "string"
          }
    post_response_token = requests.post(url, json=data)
    post_response_token_json=post_response_token.json()
    return post_response_token_json.get("token")

BASE_URL = os.getenv("BASE_URL")
BASE_HEADERS = {"Authorization": get_token()}
timetable_id = 1583


@pytest.fixture(scope = "function")

def lecturer():
    url = f"{BASE_URL}/rating/lecturer"
    data = {
    "first_name": "string",
    "last_name": "string",
    "middle_name": "string",
    "avatar_link": "string",
    "timetable_id": timetable_id
    }
    response = requests.post(url, json = data, headers = BASE_HEADERS)
    lecturer_id = response.json().get("id")

    yield lecturer_id

    requests.delete(f"{url}/{lecturer_id}", headers = BASE_HEADERS)
