import os
from dotenv import load_dotenv
from pathlib import Path
import requests
import pytest
import json


load_dotenv(dotenv_path="C:/.env/.env")
# Загружает переменные из .env файла

# Теперь их можно использовать в тестах
LOGIN_RATING = os.getenv("LOGIN_RATING")
PASSWORD_RATING = os.getenv("PASSWORD_RATING")
BASE_URL = os.getenv("BASE_URL")

def get_token():
    url = f"{BASE_URL}/auth/email/login"
    data ={
          "email": LOGIN_RATING,
          "password": PASSWORD_RATING,
          "scopes": [],
          "session_name": "string"
          }
    post_response_token = requests.post(url, json=data)
    post_response_token_status_code = post_response_token.status_code
    post_response_token_json=post_response_token.json()
    return post_response_token_json["token"]

API_TOKEN_USER_A = os.getenv("API_TOKEN_USER_A")
BASE_HEADERS = {
    "Authorization": get_token()
}

HEADERS_USER_A = {
    "Authorization": API_TOKEN_USER_A
}
LAST_TIMETABLE_ID = 10



#@pytest.fixture()
#def get_last_timetable_id():
"""getall_limit = 1
getall_ofset = 0
timetable_id_list=[]
get_response_all = requests.get(f"{BASE_URL}/lecturer?limit={getall_limit}&offset={getall_ofset}&order_by=mark_weighted&asc_order=false")
get_response_all_json = get_response_all.json()
while len(timetable_id_list) < get_response_all_json["total"]:
    getall_ofset+=1
    get_response_all = requests.get(f"{BASE_URL}/lecturer?limit={getall_limit}&offset={getall_ofset}&order_by=mark_weighted&asc_order=false")
    get_response_all_json = get_response_all.json()
    print(get_response_all_json["lecturers"][0]["timetable_id"])
    timetable_id_list.append(get_response_all_json["lecturers"][0]["timetable_id"])
    print(getall_ofset)
print(len(timetable_id_list))
print(getall_ofset)
sorted(timetable_id_list)"""
