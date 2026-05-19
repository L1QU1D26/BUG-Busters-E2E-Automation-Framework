from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.shop_menu = (By.LINK_TEXT, "Shop")
        self.mens_wear_category = (By.LINK_TEXT, "Mens Wear")

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
        self.driver.find_element(*self.shop_menu).click()
        self.driver.find_element(*self.mens_wear_category).click()

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def update_product_quantity(self, quantity):
        quantity_element = self.driver.find_element(*self.quantity_input)
        quantity_element.clear()
        quantity_element.send_keys(str(quantity))

    def remove_product_from_cart(self):
        self.driver.find_element(*self.remove_button).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text