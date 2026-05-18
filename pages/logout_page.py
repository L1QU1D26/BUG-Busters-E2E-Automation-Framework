from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # LOCATORS (example for SauceDemo-like app)
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    def open_menu(self):
        self.click(self.menu_button)

    def logout(self):
        self.click(self.logout_button)