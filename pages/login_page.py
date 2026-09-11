class login_page:
    def __init__(self, page):
        self.page = page
        self.login_field = page.get_by_role("textbox", name="Электронная почта или логин")
        self.password_field = page.get_by_role("textbox", name="Пароль")
        self.login_button = page.get_by_role("button", name="Войти в систему")

    def login(self, login, password):
        self.login_field.fill(login)
        self.password_field.fill(password)
        self.login_button.click()

