from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.products_menu = (
            By.XPATH,
            "//a[contains(text(),'Products')]"
        )

        self.view_all_products = (
            By.XPATH,
            "//a[contains(@href,'shop')]"
        )

        self.product_page_header = (
            By.XPATH,
            "//h2[contains(text(),'Products')]"
        )

    def click_products_menu(self):
        self.wait_until_clickable(self.products_menu)
        self.click(self.products_menu)

    def click_view_all_products(self):
        self.wait_until_clickable(self.view_all_products)
        self.click(self.view_all_products)

    def is_products_page_displayed(self):
        return self.is_displayed(self.product_page_header)