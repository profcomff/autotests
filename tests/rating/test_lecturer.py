import requests
import pytest
from static.settings import get_settings, Settings

settings: Settings = get_settings()

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