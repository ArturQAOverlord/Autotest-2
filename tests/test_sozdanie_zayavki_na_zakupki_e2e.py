from pages.login_page import login_page
from pages.main_page import main_page
from pages.zakupki_creation_page import zakupki_creation_page
from test_data import list_of_colums
from playwright.sync_api import expect
import time
from conftest import Initiator_login, Initiator_pass

def test_sozdanie_zayavki_na_zakupki_e2e(page, user):
    actual_page = login_page(page)

    page.goto('https://elma-test.kapitalbank.uz/login')

    actual_page.login(Initiator_login, Initiator_pass)

    actual_page = main_page(page)

    actual_page.redirect_to_zayavka_na_zakupki()

    actual_page = zakupki_creation_page(page)

    actual_page.check_fields_and_buttons()

    actual_page.check_all_table_headers(list_of_colums)
    
    actual_page.field_filler()

    actual_page.fill_table_row(
        row_index=1,
        name="random",
        description="desc",
        statya_name="AQA 2 Статья затрат Услуга/дополнительные согласующие",
        ed_izm_name="Услуга",
        currency_name="UZS",
        rate="1", 
        quantity="10",
        price="150000",
        nds_value="0%"
    )

    with page.expect_response(
        lambda response: response.url == "https://elma-test.kapitalbank.uz/api/widgets/execute"
    ) as response_info:
        actual_page.form_saver()

    response = response_info.value
    data = response.json()

    element_id = data["context"]["__id"]

    page.locator(f'a[href*="{element_id}"]').click()
    time.sleep(5) #Чтобы видно было, что открылся, можно убирать