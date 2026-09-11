import requests

def check_user_in_group(id_group, token):

    url = f"https://elma-test.kapitalbank.uz/pub/v1/scheme/groups/{id_group}/users"

    payload = {}
    headers = {
    'Authorization': token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200, f'Не удалось выполнить запрос - {response.status_code}'
    
    return response