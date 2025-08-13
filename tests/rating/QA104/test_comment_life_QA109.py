import requests
import pytest
import json
from conftest import BASE_URL, BASE_HEADERS, HEADERS_USER_A

lecturer_id = 6799
text_filename = "text_example_3000_plus.txt"
try:
    with open(text_filename, "r", encoding="utf-8") as file:
        text_3000_plus=file.read()
except FileNotFoundError:
    print("файл не найден, создаю новый")
    with open(text_filename, "w") as new_file:
        new_file.write("base")
        text_3000_plus = new_file.read()
if len(text_3000_plus)<=3000:
    try:
        with open(text_filename,"a", encoding="utf-8") as file:
            while len(text_3000_plus)<=3000:
                text_3000_plus+="hello"
            file.write(text_3000_plus)
    except IOError as e:
        print(f"ошибка записи в файл: {e}")
        exit()

@pytest.mark.parametrize("subject", ["physics", 909, "", text_3000_plus])
@pytest.mark.parametrize("text", ["nhfkkff", 999, "", text_3000_plus])
@pytest.mark.parametrize("mark_kindness", [0, 1, 2, -2, -1, 3, -3, "huhuhuh"])
@pytest.mark.parametrize("mark_clarity", [0, 1, 2, -2, -1, 3, -3, "huhuhuh"])
@pytest.mark.parametrize("mark_freebie", [0, 1, 2, -2, -1, 3, -3, "huhuhuh"])
@pytest.mark.parametrize("is_anonymous", [0, True, False, "True"])
@pytest.mark.parametrize("subject_patch", ["physics", 909, "", text_3000_plus])
@pytest.mark.parametrize("text_patch", ["nhfkkff", 999, "", text_3000_plus])
@pytest.mark.parametrize("mark_kindness_patch", [0, 1, 2, -2, -1, 3, -3, "huhuhuh"])
@pytest.mark.parametrize("mark_freebie_patch", [0, 1, 2, -2, -1, 3, -3, "huhuhuh"])
@pytest.mark.parametrize("mark_clarity_patch", [0, 1, 2, -2, -1, 3, -3, "huhuhuh"])
def test_comment_life_cicle(
        subject, text, mark_kindness, mark_freebie,
        mark_clarity, is_anonymous, subject_patch, text_patch,
        mark_kindness_patch, mark_freebie_patch, mark_clarity_patch
):
    url = f"{BASE_URL}/rating/comment?lecturer_id={lecturer_id}"
    data = {
            "subject": subject,
            "text": text,
            "create_ts": "2025-08-08T09:22:54.745Z",
            "update_ts": "2025-08-08T09:22:54.745Z",
            "mark_kindness": mark_kindness,
            "mark_freebie": mark_freebie,
            "mark_clarity": mark_clarity,
            "is_anonymous": is_anonymous
            }
    expected_status_code = 200
    response_post = requests.post(url, headers=BASE_HEADERS, json=data)
    #assert response_post.status_code == expected_status_code
    print(response_post.status_code)
    response_post_json = response_post.json()
    print(response_post_json["subject"])
    print(response_post_json["text"])
    print(response_post_json["mark_kindness"])
    print(response_post_json["mark_freebie"])
    print(response_post_json["mark_clarity"])
    print(response_post_json["is_anonymous"])
    if expected_status_code == 200:
        response_get = requests.get(f"{url}/{response_post_json['uuid']}")
        assert response_get.status_code == 200
        """data_patch = {
                        "subject": subject_patch,
                        "text": text_patch,
                        "mark_kindness": mark_kindness_patch,
                        "mark_freebie": mark_freebie_patch,
                        "mark_clarity": mark_clarity_patch
                     }
        response_patch = requests.patch(f"{url}/{response_post_json['uuid']}",headers=BASE_HEADERS, json = data_patch)
        assert response_patch.status_code==200"""
        response_delete = requests.delete(f"{url}/{response_post_json['uuid']}",headers=BASE_HEADERS)
        assert response_delete.status_code == 200
        response_get = requests.get(f"{url}/{response_post_json['uuid']}")
        assert response_get.status_code == 404
