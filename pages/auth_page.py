from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # WEBSITE URL
        self.url = "https://shop.qaautomationlabs.com/"

        # LOGIN LOCATORS
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

        # LOGOUT LOCATORS
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    # OPEN WEBSITE
    def open_login_page(self):
        self.open_url(self.url)

    # LOGIN METHOD
    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)

    # LOGOUT METHOD
    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_button)