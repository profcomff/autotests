import requests 
from dotenv import load_dotenv
import os

load_dotenv()
URL = os.getenv("URL")

lect_id = 7000
def test_correct_id():
    response = requests.get(f"{URL}/{lect_id}")
    lecturer = response.json()
    assert response.status_code == 200
    expected_structure = {  #проверка json
        "id": int,
        "first_name": str,
        "last_name": str,
        "middle_name": str,
        "avatar_link": str,
        "timetable_id": int,
        
    }
    for field, expected_type in expected_structure.items():
        assert field in lecturer
        assert isinstance(lecturer[field], expected_type)


incorrect_id = 99999
def test_incorrect_id():
    response = requests.get(f"{URL}/{incorrect_id}")
    assert response.status_code == 404


invalid_format_id = "evw"
def test_invalid_format_id():
    response = requests.get(f"{URL}/{invalid_format_id}")
    error_response = response.json()
    assert response.status_code == 422
    expected_structure = { #проверка json 
        "detail": list
    }
    assert isinstance(error_response["detail"], list)