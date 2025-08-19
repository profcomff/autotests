import pytest
import requests 
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("BASE_URL")

def test_correct_id():
    response1 = requests.get(f"{base_url}/rating/lecturer")
    json = response1.json()
    lect_id = json.get("lecturers")[0].get("id")
    response = requests.get(f"{base_url}/rating/lecturer/{lect_id}")
    assert response.status_code == 200

@pytest.mark.parametrize("incorrect_id", [0, -1, -9999])
def test_incorrect_id(incorrect_id):
    response = requests.get(f"{base_url}/rating/lecturer/{incorrect_id}")
    assert response.status_code == 404
    
@pytest.mark.parametrize("invalid_format_id", ["sdfb", "&&"])
def test_invalid_format_id(invalid_format_id):
    response = requests.get(f"{base_url}/rating/lecturer/{invalid_format_id}")
    assert response.status_code == 422
    