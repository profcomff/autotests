import requests
import pytest
from conftest import BASE_URL





@pytest.mark.parametrize("first_name, last_name, timetable_id, expected_status", [
                        ("Николай", "Николаев", 100, 403),
                        ("Николай", 999, 100, 403),
                        (999, "Николаев", 100, 403),
                        (999, 999, 100, 403),
                        ("", "Николаев", 100, 403),
                        ("Николай", "", 100, 403),
                        ("", "", 100, 403),
                        (999, "", 100, 403),
                        ("", 999, 100, 403),
                        ("string", "Николаев", 100, 403),
                        ("string", 999, 100, 403),
                        (999, "string", 100, 403),
                        ("Николай", "string", 100, 403),
                        ("string", "", 100, 403),
                        ("", "string", 100, 403),
                        ("string", "string", 100, 403),
                        ("Николай", "Николаев", "ag", 403),
                        ("Николай", 999, "ag", 403),
                        (999, "Николаев", "ag", 403),
                        (999, 999, "ag", 403),
                        ("", "Николаев", "ag", 403),
                        ("Николай", "", "ag", 403),
                        ("", "", "ag", 403),
                        (999, "", "ag", 403),
                        ("", 999, "ag", 403),
                        ("string", "Николаев", "ag", 403),
                        ("string", 999, "ag", 403),
                        (999, "string", "ag", 403),
                        ("Николай", "string", "ag", 403),
                        ("string", "", "ag", 403),
                        ("", "string", "ag", 403),
                        ("string", "string", "ag", 403)
])
def test_create_profile(first_name, last_name, timetable_id, expected_status):
    url = f"{BASE_URL}/lecturer"
    data = {
                "first_name":first_name,
                "last_name":last_name,
                "middle_name": "Иванович",
                "avatar_link": "",
                "timetable_id": 0
            }

    response = requests.post(url, json=data)
    assert response.status_code == expected_status
    response_json = response.json()



