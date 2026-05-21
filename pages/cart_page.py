
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

    def cart_click(self, locator):

        element = self.driver.find_element(*locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        element.click()
        
    # Methods

    def open_category(self, category_name):
        # Use JS click to bypass CSS dropdown visibility in headless Chrome.
        # ActionChains hover does not trigger :hover dropdowns in headless mode.
        category_locator = (
            CartLocators.CATEGORY_LINK_TEXT[0],
            category_name
        )

        self.js_click(category_locator)

        print(f"Opened {category_name} category")

    def add_product_to_cart(self, product_index):
        try:
            badge = self.driver.find_element(*CartLocators.CART_COUNT)
            initial_count = int(badge.text) if badge.text.strip() else 0
        except Exception:
            initial_count = 0

        product_locator = (
            "xpath",
            f"(//button[contains(@class,'addToCart')])[{product_index}]"
        )

        self.cart_click(product_locator)
        print(f"Clicked on product {product_index}")

        # Wait for cart count to update
        try:
            self.wait.until(
                lambda d: int(d.find_element(*CartLocators.CART_COUNT).text or 0) > initial_count
            )
            print(f"Cart count updated to {self.get_cart_count()}")
        except Exception as e:
            print(f"Warning: Cart count did not update dynamically: {e}")


    def open_cart(self):

        self.cart_click(
            CartLocators.CART_ICON
        )

    def update_product_quantity(self, quantity):

        quantity_element = self.driver.find_element(
            *CartLocators.QUANTITY_INPUT
        )

        quantity_element.clear()

        quantity_element = self.driver.find_element(
            *CartLocators.QUANTITY_INPUT
        )

        quantity_element.send_keys(
            str(quantity)
        )

        print("Quantity updated successfully")

    def remove_product_from_cart(self):

        self.cart_click(
            CartLocators.REMOVE_BUTTON
        )

    def get_cart_count(self):

        return self.get_text(
            CartLocators.CART_COUNT
        )