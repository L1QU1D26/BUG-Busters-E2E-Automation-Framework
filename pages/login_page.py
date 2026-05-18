from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.username = ("id", "username")
        self.password = ("id", "password")
        self.login_btn = ("id", "login")

    def login(self, user, pwd):
        self.enter_text(self.username, user)
        self.enter_text(self.password, pwd)
        self.click(self.login_btn)