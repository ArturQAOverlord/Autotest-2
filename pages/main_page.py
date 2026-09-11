class main_page:
    def __init__(self, page):
        self.page = page
        self.icon_razdel_zakupki = page.get_by_role("link", name="system_inbox Закупки")
        self.icon_prilozheniye_zayavki_na_zakupki = page.locator("div").filter(has_text="cart_plusЗаявки на закупки").nth(3)
        self.button_creation_zayavka_na_zakupki = page.locator("[data-test=\"createVacancyB\"]")

    def redirect_to_zayavka_na_zakupki(self):
        self.icon_razdel_zakupki.click()
        self.icon_prilozheniye_zayavki_na_zakupki.click()
        self.button_creation_zayavka_na_zakupki.click()


