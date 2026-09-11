import requests

def add_user_in_group(id_group, token, initiator_uuid):
    url = f"https://elma-test.kapitalbank.uz/pub/v1/scheme/groups/{id_group}/add-items"

    payload = f"[\n\n    \"{initiator_uuid}\"\n\n]"
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200, f'Не добавился пользователь, есть проблемы {response.status_code}'
