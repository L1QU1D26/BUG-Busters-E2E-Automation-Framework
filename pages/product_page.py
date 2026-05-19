from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.first_product = (By.CSS_SELECTOR, "a[href='product.php?id=21']")
        self.add_to_cart = (By.CSS_SELECTOR, ".addToCart")
        self.cart_count = (By.ID, "cartCount")

    def click_product(self):
        self.click(self.first_product)

    def click_add_to_cart(self):
        self.click(self.add_to_cart)

    def get_cart_count(self):
        return self.get_text(self.cart_count)
