from pages.base_page import BasePage
from locators.product_locators import ProductLocators
from locators.authentication import LoginLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_shop(self):
        self.click(LoginLocators.PRODUCT_TITLE)

    def click_mens_shop_now(self):
        self.click(ProductLocators.MEN_FASHION_SHOP_NOW)

    def click_product(self):
        self.click(ProductLocators.FIRST_PRODUCT_NAME)

    def click_add_to_cart(self):
        self.click(ProductLocators.ADD_TO_CART)

    def click_cart_icon(self):
        self.click(ProductLocators.CART_ICON)

    def get_cart_count(self):
        return self.get_text(ProductLocators.CART_COUNT)

    def is_product_page_displayed(self):
        return "product.php?id=" in self.driver.current_url.lower()

    def is_cart_page_displayed(self):
        return "cart.php" in self.driver.current_url.lower()