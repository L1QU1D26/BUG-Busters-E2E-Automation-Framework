from selenium.webdriver.common.by import By
from test_pom.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.url = "https://example.com/login"

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open_login_page(self):
        self.open_url(self.url)

    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)