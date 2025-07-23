import requests
import pytest
import json
from conftest import api_token, base_url #env_path

I = 5896550
#BASE_URL
#token_test

headers = {
    "Authorization": api_token
}

@pytest.mark.parametrize("first_name, last_name, timetable_id, expected_status", [
                        ("Николай", "Николаев", I, 200),

                        ("Николай", 999, I, 422),
                        (999, "Николаев", I, 422),
                        (999, 999, I, 422),
                        ("", "Николаев", I, 200),
                        ("Николай", "", I, 200),
                        ("", "", I, 200),
                        (999, "", I, 422),
                        ("", 999, I, 422),
                        ("string", "Николаев", I, 200),
                        ("string", 999, I, 422),
                        (999, "string", I, 422),
                        ("Николай", "string", I, 200),
                        ("string", "", I, 200),
                        ("", "string", I, 200),
                        ("string", "string", I, 200),
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
    url = f"{base_url}/lecturer"
    data = {
                "first_name": first_name,
                "last_name": last_name,
                "middle_name": "Иванович",
                "avatar_link": "",
                "timetable_id": timetable_id
            }

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == expected_status
    response_json = response.json()
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    #assert response_json["first_name"] == data["first_name"]
    #assert response_json["last_name"] == data["last_name"]
    #assert data["timetable_id"] == response_json["timetable_id"]

    if expected_status == 200:
        #проверка_поста
        get_response = requests.get(f"{url}/{response_json['id']}")
        assert get_response.status_code == 200
        assert get_response.json()["first_name"] == data["first_name"]
        assert get_response.json()["last_name"] == data["last_name"]
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        #удаление_поста
        delete_response = requests.delete(f"{url}/{response_json['id']}", headers=headers)
        print(delete_response)
        assert delete_response.status_code == 200
        # проверка_удалённого_поста
        get_deleted_response = requests.get(f"{url}/{response_json['id']}")
        assert get_deleted_response.status_code == 404
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
