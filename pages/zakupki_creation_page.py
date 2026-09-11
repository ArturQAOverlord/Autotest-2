from playwright.sync_api import expect
import time

class zakupki_creation_page:
    def __init__(self, page):
        self.page = page
        self.button_boolean = page.get_by_text("Внеплановая", exact=True)
        self.field_podrazdelenie_initiator = page.locator("elma-form-row").filter(has_text="Подразделение-инициатор").get_by_role("combobox")
        self.field_rukovoditel_kurator = page.locator("elma-form-row", has_text="Руководитель, курирующий данное подразделение")
        self.field_description_zakupki = page.locator("elma-form-row").filter(has_text="Описание предмета закупки:").get_by_role("textbox")
        self.button_recounter = page.get_by_role("button", name="Пересчитать таблицу")
        self.button_save = page.get_by_role("button", name="Сохранить")
        self.button_search = page.get_by_role("button", name="search").first

    def check_fields_and_buttons(self):
        expect(self.button_boolean).to_be_visible()
        self.button_boolean.click()
        expect(self.field_podrazdelenie_initiator).to_be_visible()
        expect(self.field_rukovoditel_kurator).to_be_visible()
        expect(self.field_description_zakupki).to_be_visible()
        expect(self.button_recounter).to_be_visible()
        expect(self.button_save).to_be_visible()

    def check_all_table_headers(self, list_of_colums):

        header_row = self.page.locator('elma-type-table-full-line[data-index="0"]').filter(visible=True).first
        
        for column_title in list_of_colums:
            clean_title = column_title.strip()

            column_locator = header_row.locator(f'th[title*="{clean_title}"]').first

            
        total_cell = self.page.get_by_role("row", name="Итого:", exact=False).get_by_text("Итого").first

    def field_filler(self):
        self.field_podrazdelenie_initiator.click()
        self.button_search.click()
        self.page.get_by_role("cell", name="AQA 2").click()

    def fill_table_row(self, row_index: int, name: str, description: str, statya_name: str, ed_izm_name: str, currency_name: str, rate: str, quantity: str, price: str, nds_value: str):

        row = self.page.locator(f'elma-type-table-full-line[data-index="{row_index}"]')

        cell_name = row.locator('td[data-columnindex="1"]')
        cell_name.click()
        row.locator("#naimenovanie_pozicii").fill(name)

        cell_desc = row.locator('td[data-columnindex="2"]')
        cell_desc.click()
        row.locator("#opisanie").fill(description)

        cell_statya = row.locator('td[data-columnindex="3"]')
        cell_statya.click()
        btn_search_statya = cell_statya.get_by_role("button", name="search")
        btn_search_statya.wait_for(state="visible")
        btn_search_statya.click()
        
        link_statya = self.page.get_by_role("link", name=statya_name)
        link_statya.wait_for(state="visible")
        link_statya.click()

        cell_ed_izm = row.locator('td[data-columnindex="6"]')
        cell_ed_izm.click()
        btn_search_ed = cell_ed_izm.get_by_role("button", name="search")
        btn_search_ed.wait_for(state="visible")
        btn_search_ed.click()
        
        link_ed = self.page.get_by_role("link", name=ed_izm_name, exact=True)
        link_ed.wait_for(state="visible")
        link_ed.click()

        cell_currency = row.locator('td[data-columnindex="7"]')
        cell_currency.click()
        btn_search_currency = cell_currency.get_by_role("button", name="search")
        btn_search_currency.wait_for(state="visible")
        btn_search_currency.click()
        
        link_currency = self.page.get_by_role("link", name=currency_name)
        link_currency.wait_for(state="visible")
        link_currency.click()

        cell_rate = row.locator('td[data-columnindex="8"]')
        cell_rate.click()

        input_rate = cell_rate.locator("input")
        input_rate.wait_for(state="visible")
        input_rate.fill(rate)

        cell_qty = row.locator('td[data-columnindex="9"]')
        cell_qty.click()
        input_qty = row.locator("#kolvo") if row.locator("#kolvo").count() > 0 else cell_qty.locator("input")
        input_qty.wait_for(state="visible")
        input_qty.fill(quantity)

        cell_price = row.locator('td[data-columnindex="10"]')
        cell_price.click()
        input_price = row.locator("#cena_za_edinicu") if row.locator("#cena_za_edinicu").count() > 0 else cell_price.locator("input")
        input_price.wait_for(state="visible")
        input_price.fill(price)

        cell_nds = row.locator('td[data-columnindex="12"]')
        cell_nds.click()
        dropdown_trigger = cell_nds.get_by_label("dropdown trigger")
        dropdown_trigger.wait_for(state="visible")
        dropdown_trigger.click()
        
        option_nds = self.page.get_by_role("option", name=nds_value)
        option_nds.wait_for(state="visible")
        option_nds.click()

    def form_saver(self):
        self.button_save.click()