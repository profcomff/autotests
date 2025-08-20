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

@pytest.mark.parametrize("data", [{
    "first_name": "string1",
    "last_name": "string",
    "middle_name": "string",
    "avatar_link": "string",
    "timetable_id": timetable_id
    }, {"first_name": "string",
    "last_name": "string2",
    "middle_name": "string",
    "avatar_link": "string",
    "timetable_id": timetable_id}, {
        "first_name": "string",
    "last_name": "string",
    "middle_name": "string3",
    "avatar_link": "string",
    "timetable_id": timetable_id},{
    "first_name": "string",
    "last_name": "string",
    "middle_name": "string",
    "avatar_link": "string4",
    "timetable_id": timetable_id}])
def test_patch_lecturer_strings(lecturer, data):
    url = f"{BASE_URL}/rating/lecturer/{lecturer}"
    response = requests.patch(url, json = data, headers = BASE_HEADERS)
    assert response.status_code == 200
    

@pytest.mark.parametrize("data", [{
    "first_name": "string1",
    "last_name": "string1",
    "middle_name": "string1",
    "avatar_link": "string1",
    "timetable_id": timetable_id + 1
    }])
def test_patch_lecturer_timetable_id(lecturer, data):
    url = f"{BASE_URL}/rating/lecturer/{lecturer}"
    response = requests.patch(url, json = data, headers = BASE_HEADERS)
    assert response.status_code == 200


@pytest.mark.parametrize("data", [
    {"first_name": "string",
    "last_name": "string",
    "middle_name": "string",
    "avatar_link": "string",
    "timetable_id": -1},
    {"first_name": "string",
    "last_name": "string",
    "middle_name": "string",
    "avatar_link": "string",
    "timetable_id": "sdfb"
    }])
def test_patch_lecturer_incorrect_timetable_id(lecturer, data):
    url = f"{BASE_URL}/rating/lecturer/{lecturer}"
    response = requests.patch(url, json = data, headers = BASE_HEADERS)
    assert response.status_code == 422

@pytest.mark.parametrize("data", [{
    "first_name": "string1",
    "last_name": "string1",
    "middle_name": "string1",
    "avatar_link": "string1",
    "timetable_id": timetable_id + 1
    }])
def test_patch_lecturer_without_authorization(lecturer, data):
    url = f"{BASE_URL}/rating/lecturer/{lecturer}"
    response = requests.patch(url, json = data)
    assert response.status_code == 401 or 403
