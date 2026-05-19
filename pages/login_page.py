from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # URL
        self.url = "https://example.com/login"

        # Locators
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    # Open login page
    def open_login_page(self):
        self.open_url(self.url)

    # Perform login action
    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)