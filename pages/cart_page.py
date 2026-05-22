
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

    def cart_click(self, locator):

        self.js_click(locator)
        
    # Methods

    def open_category(self, category_name):
        """Navigate directly to the category page URL.
        Uses driver.get() instead of hover/click on the dropdown — the only
        reliable approach in headless Chrome where CSS :hover never triggers.
        Login session cookies persist across same-domain navigation calls.
        """
        category_urls = {
            "Mens Wear":    "https://shop.qaautomationlabs.com/mens-wear.php",
            "Womens Wear":  "https://shop.qaautomationlabs.com/womens-wear.php",
            "Kids Wear":    "https://shop.qaautomationlabs.com/kids-wear.php",
            "Electronics":  "https://shop.qaautomationlabs.com/electronics.php",
        }
        url = category_urls.get(category_name, "")
        if url:
            self.driver.get(url)
            print(f"Navigated to {category_name}: {url}")
        else:
            # Fallback for any unmapped category name
            self.js_click((CartLocators.CATEGORY_LINK_TEXT[0], category_name))
            print(f"JS-clicked category link: {category_name}")

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