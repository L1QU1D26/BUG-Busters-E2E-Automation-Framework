from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.shop_menu = (By.LINK_TEXT, "Shop")

        self.mens_wear_category = (
            By.LINK_TEXT,
            "Mens Wear"
        )

        self.add_to_cart_button = (
            By.XPATH,
            "(//button[contains(@class,'addToCart')])[1]"
        )

        self.cart_icon = (
            By.XPATH,
            "//a[contains(@href,'cart.php')]"
        )

        self.quantity_input = (
            By.XPATH,
            "(//input[@type='number'])[1]"
        )

        self.remove_button = (
            By.XPATH,
            "(//button[contains(@class,'remove')])[1]"
        )

        self.cart_count = (
            By.ID,
            "cartCount"
        )

    # Methods
    def open_mens_wear_category(self):
        self.click(self.shop_menu)
        self.click(self.mens_wear_category)

    def add_product_to_cart(self):
        self.click(self.add_to_cart_button)

    def open_cart(self):
        self.click(self.cart_icon)

    def update_product_quantity(self, quantity):
        self.enter_text(self.quantity_input, str(quantity))

    def remove_product_from_cart(self):
        self.click(self.remove_button)

    def get_cart_count(self):
        return self.get_text(self.cart_count)