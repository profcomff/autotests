import requests
import pytest
from static.settings import get_settings, Settings
from dotenv import load_dotenv
import os

settings: Settings = get_settings()

load_dotenv()
TOKEN = os.getenv("TOKEN")

class TestLecturerAPI:
    BASE_RATING_URL: str = "https://api.test.profcomff.com/rating"

    def test_get_lecturers_with_limit(self):
        url = f"{self.BASE_RATING_URL}/lecturer"
        params = {"limit": 10}
        response = requests.get(url, params=params)

        assert response.status_code == 200
        data = response.json()
        assert "lecturers" in data
        assert isinstance(data["lecturers"], list)
        assert len(data["lecturers"]) <= 10  # Check that the number of lecturers is not more than the limit
        assert "total" in data
        assert isinstance(data["total"], int)

    def test_post_lecturer(self):
        url = f"{self.BASE_RATING_URL}/lecturer"
        headers = {
            "Authorization": f"{TOKEN}"
        }
        body = {
            "first_name": "Test123",
            "last_name": "Test123",
            "middle_name": "Test123",
            "avatar_link": "string1232455.com",
            "timetable_id": 92442
        }
        response = requests.post(url, headers=headers, json=body)
        assert response.status_code == 200
        response_json = response.json()
        lecturer_id = response_json["id"]
        assert response_json["first_name"] == "Test123"
        assert response_json["last_name"] == "Test123"
        assert response_json["middle_name"] == "Test123"
        assert response_json["avatar_link"] == "string1232455.com"
        assert response_json["timetable_id"] == 92442

        delete_response = requests.delete(f"{url}/{lecturer_id}", headers=headers)
        assert delete_response.status_code == 200
