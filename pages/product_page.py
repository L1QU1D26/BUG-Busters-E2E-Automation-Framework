from pages.base_page import BasePage
from locators.product_locators import ProductLocators
from locators.authentication import LoginLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Navigation

    def navigate_to_shop(self):

        self.click(LoginLocators.PRODUCT_TITLE)

    def open_mens_category(self):

        self.click(ProductLocators.MEN_FASHION_SHOP_NOW)

    def open_womens_category(self):

        self.click(ProductLocators.WOMEN_FASHION_SHOP_NOW)

    def open_kids_category(self):

        self.click(ProductLocators.KIDS_FASHION_SHOP_NOW)

    def open_electronics_category(self):

        self.click(ProductLocators.ELECTRONICS_SHOP_NOW)

    # Product actions

    def click_product(self):

        self.click(ProductLocators.FIRST_PRODUCT_NAME)

    def click_add_to_cart(self):

        self.click(ProductLocators.ADD_TO_CART)

    def click_cart_icon(self):

        self.click(ProductLocators.CART_ICON)

    # Validations
    def get_cart_count(self):

        return self.get_text(
            ProductLocators.CART_COUNT
        )

    def is_product_page_displayed(self):

        return "product.php?id=" in self.driver.current_url.lower()

    def is_cart_page_displayed(self):

        return "cart.php" in self.driver.current_url.lower()

    def are_products_visible(self):

        return self.is_visible(
            ProductLocators.PRODUCT_LIST
        )

    def get_product_count(self):

        products = self.driver.find_elements(
            *ProductLocators.PRODUCT_CARDS
        )

        return len(products)

    def is_filter_visible(self):

        return self.is_visible(
            ProductLocators.SORT_DROPDOWN
        )

    def click_filter(self, filter_name):

        locator = (
            "xpath",
            f"//label[contains(text(),'{filter_name}')]"
        )

        self.js_click(locator)
        print(f"Clicked filter: {filter_name}")

    def scroll_page(self):

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )