import requests
import pytest
import json
from conftest import BASE_URL, BASE_HEADERS

timetable_idbase = 5896550


@pytest.mark.parametrize("first_name, last_name, timetable_id, expected_status", [
                        ("Николай", "Николаев", timetable_idbase, 200),

                        ("Николай", 999, timetable_idbase, 422),
                        (999, "Николаев", timetable_idbase, 422),
                        (999, 999, timetable_idbase, 422),
                        ("", "Николаев", timetable_idbase, 200),
                        ("Николай", "", timetable_idbase, 200),
                        ("", "", timetable_idbase, 200),
                        (999, "", timetable_idbase, 422),
                        ("", 999, timetable_idbase, 422),
                        ("string", "Николаев", timetable_idbase, 200),
                        ("string", 999, timetable_idbase, 422),
                        (999, "string", timetable_idbase, 422),
                        ("Николай", "string", timetable_idbase, 200),
                        ("string", "", timetable_idbase, 200),
                        ("", "string", timetable_idbase, 200),
                        ("string", "string", timetable_idbase, 200),
                        ("Николай", "Николаев", "ag", 422),
                        ("Николай", 999, "ag", 422),
                        (999, "Николаев", "ag", 422),
                        (999, 999, "ag", 422),
                        ("", "Николаев", "ag", 422),
                        ("Николай", "", "ag", 422),
                        ("", "", "ag", 422),
                        (999, "", "ag", 422),
                        ("", 999, "ag", 422),
                        ("string", "Николаев", "ag", 422),
                        ("string", 999, "ag", 422),
                        (999, "string", "ag", 422),
                        ("Николай", "string", "ag", 422),
                        ("string", "", "ag", 422),
                        ("", "string", "ag", 422),
                        ("string", "string", "ag", 422)
])
def test_create_profile(first_name, last_name, timetable_id, expected_status):
    url = f"{BASE_URL}/lecturer"
    data = {
                "first_name": first_name,
                "last_name": last_name,
                "middle_name": "Иванович",
                "avatar_link": "",
                "timetable_id": timetable_id
            }

    response = requests.post(url, headers=BASE_HEADERS, json=data)
    assert response.status_code == expected_status
    response_json = response.json()


    if expected_status == 200:
        #проверка_поста
        get_response = requests.get(f"{url}/{response_json['id']}")
        assert get_response.status_code == 200
        assert get_response.json()["first_name"] == data["first_name"]
        assert get_response.json()["last_name"] == data["last_name"]
        #удаление_поста
        delete_response = requests.delete(f"{url}/{response_json['id']}", headers=BASE_HEADERS)
        assert delete_response.status_code == 200
        # проверка_удалённого_поста
        get_deleted_response = requests.get(f"{url}/{response_json['id']}")
        assert get_deleted_response.status_code == 404

