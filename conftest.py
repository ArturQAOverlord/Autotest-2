import pytest 
import os
from dotenv import load_dotenv
from api_requests.check_user_in_group import check_user_in_group
from api_requests.add_user_in_group import add_user_in_group
from playwright.sync_api import expect
load_dotenv()
expect.set_options(timeout=15000)

id_group = os.getenv('ID_GROUP')
token = os.getenv('TOKEN')
Initiator_name = os.getenv('USER_NAME')
Initiator_login = os.getenv('USER_LOGIN')
Initiator_pass = os.getenv('USER_PASS')
Initiator_uuid = os.getenv('USER_UUID')

@pytest.fixture
def user():

    g = check_user_in_group(id_group, token)

    for i in g.json()['result']['result']:
        if i['__name'] == Initiator_name:
            break
    else:
         add_user_in_group(id_group, token, Initiator_uuid)
