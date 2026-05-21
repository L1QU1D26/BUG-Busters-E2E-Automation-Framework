from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
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

           # more locators...


    def cart_click(self, locator):

        element = self.driver.find_element(*locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        element.click()

    # Methods

    def open_mens_wear_category(self):

        actions = ActionChains(self.driver)

        shop_element = self.driver.find_element(*self.shop_menu)

        actions.move_to_element(shop_element).perform()

        self.click(self.mens_wear_category)

        print("Clicked on Mens Wear category")

        print(self.driver.current_url)

        time.sleep(4)

    def add_product_to_cart(self):

        self.click(self.add_to_cart_button)

        print("Clicked on Add to Cart button")

        time.sleep(4)

    def open_cart(self):

        self.click(self.cart_icon)

        time.sleep(4)

    def update_product_quantity(self, quantity):
       

            quantity_element = self.driver.find_element(
                *self.quantity_input
            )

            quantity_element.clear()

            quantity_element = self.driver.find_element(
                *self.quantity_input
            )

            quantity_element.send_keys(str(quantity))

            time.sleep(4)

    print("Quantity updated successfully")
    def remove_product_from_cart(self):

        self.click(self.remove_button)
        time.sleep(4)

    def get_cart_count(self):

        return self.get_text(self.cart_count)
        