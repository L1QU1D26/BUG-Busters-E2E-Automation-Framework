from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


WAIT_TIMEOUT = 8


class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.products_menu = (By.CSS_SELECTOR, ".nav-link.dropdown-toggle")
        self.view_all_products = (
            By.CSS_SELECTOR,
            ".dropdown-menu a[href='shop.php']"
        )
        self.cart_icon = (By.ID, "cartdesk")
        self.product_category = (
            By.XPATH,
            "//a[contains(@href,'mens-wear.php') and contains(.,'Shop Now')]"
        )

    def click_products_menu(self):
        menu = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.products_menu)
        )
        self.driver.execute_script("arguments[0].click();", menu)

    def click_view_all_products(self):
        view_all = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.view_all_products)
        )
        self.driver.execute_script("arguments[0].click();", view_all)

    def click_cart_icon(self):
        self.click(self.cart_icon)

    def is_products_page_displayed(self):
        return WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.product_category)
        ).is_displayed()
