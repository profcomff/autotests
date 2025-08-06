import requests 
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("base_url")


def test_correct_id():
    response1 = requests.get(f"{base_url}/lecturer")
    json = response1.json()
    lect_id = json.get("lecturers")[0].get("id")
    response = requests.get(f"{base_url}/lecturer/{lect_id}")
    assert response.status_code == 200


incorrect_1 = 0
incorrect_2 = -1
def test_incorrect_id():
    response = requests.get(f"{base_url}/lecturer/{incorrect_1}")
    assert response.status_code == 404
    response = requests.get(f"{base_url}/lecturer/{incorrect_2}")
    assert response.status_code == 404


invalid_format_id = "evw"
def test_invalid_format_id():
    response = requests.get(f"{base_url}/lecturer/{invalid_format_id}")
    assert response.status_code == 422
