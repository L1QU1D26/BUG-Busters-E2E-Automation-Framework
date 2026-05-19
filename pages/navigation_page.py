from selenium.webdriver.common.by import By
from base_page import BasePage


class NavigationPage(BasePage):

    def __init__(self, driver):
        super()._init_(driver)

        self.products_menu = (By.CSS_SELECTOR, ".nav-link.dropdown-toggle")
        self.view_all_products = (By.CSS_SELECTOR, ".dropdown-menu a[href='shop.php']")
        self.cart_icon = (By.ID, "cartdesk")
        self.product_category = (By.CSS_SELECTOR, ".product-offer")

    def click_products_menu(self):
        self.click(self.products_menu)

    def click_view_all_products(self):
        self.click(self.view_all_products)

    def click_cart_icon(self):
        self.click(self.cart_icon)

    def is_products_page_displayed(self):
        return self.get_text(self.product_category)