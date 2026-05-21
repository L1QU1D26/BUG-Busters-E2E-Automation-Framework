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
        self.click_product_by_number(1)

    def click_product_by_number(self, product_number):

        product_links = self.get_elements(ProductLocators.PRODUCT_LINKS)
        index = max(product_number - 1, 0)

        if index >= len(product_links):
            index = len(product_links) - 1

        product = product_links[index]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            product
        )

        self.wait.until(lambda driver: product.is_displayed())
        product.click()
        self.wait_for_product_details()

    def click_add_to_cart(self):
        self.click(ProductLocators.ADD_TO_CART)
        self.wait_for_cart_count()

    def click_add_to_cart_by_number(self, product_number):

        add_buttons = self.get_elements(ProductLocators.ADD_TO_CART_BUTTONS)
        index = max(product_number - 1, 0)

        if index >= len(add_buttons):
            index = len(add_buttons) - 1

        button = add_buttons[index]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        self.wait.until(lambda driver: button.is_displayed() and button.is_enabled())
        button.click()
        self.wait_for_cart_count()

    def click_cart_icon(self):
        self.click(ProductLocators.CART_ICON)
        self.wait_for_url_contains("cart.php")

    def get_cart_count(self):
        return self.get_text(ProductLocators.CART_COUNT)

    def wait_for_products(self):

        return self.get_elements(ProductLocators.PRODUCT_LINKS)

    def wait_for_filters(self):

        return self.is_visible(ProductLocators.FILTER_SECTION)

    def scroll_through_products(self):

        self.wait_for_products()
        self.scroll_to_bottom()
        self.wait_for_page_ready()
        self.scroll_to_element(ProductLocators.FIRST_PRODUCT_NAME)

    def wait_for_product_details(self):

        self.wait_for_url_contains("product.php?id=")
        self.wait_for_page_ready()
        return self.is_visible(ProductLocators.PRODUCT_DETAIL_BODY)

    def wait_for_cart_count(self):

        return self.wait.until(
            lambda driver: self.get_cart_count().strip() not in ("", "0")
        )

    def is_product_page_displayed(self):
        try:
            return self.wait_for_product_details()
        except Exception:
            return False

    def is_cart_page_displayed(self):
        try:
            return self.wait_for_url_contains("cart.php")
        except Exception:
            return False
