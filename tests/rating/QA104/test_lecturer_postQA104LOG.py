import requests
import pytest
import json
from conftest import BASE_URL, BASE_HEADERS

timetable_idbase = 5896550


@pytest.mark.parametrize("first_name", ["", "Николай", 999, "string"])
@pytest.mark.parametrize("last_name", ["", "Николаев", 999, "string"])
@pytest.mark.parametrize("timetable_id", [timetable_idbase, "ag"])
def test_create_profile(first_name, last_name, timetable_id):
    url = f"{BASE_URL}/lecturer"
    data = {
                "first_name": first_name,
                "last_name": last_name,
                "middle_name": "Иванович",
                "avatar_link": "",
                "timetable_id": timetable_id
            }
    if type(first_name) == int or type(last_name) == int or type(timetable_id) == str : expected_status = 422
    else: expected_status=200
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

