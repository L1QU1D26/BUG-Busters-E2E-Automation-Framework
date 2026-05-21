from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.constants import BASE_URL
from pages.base_page import BasePage


WAIT_TIMEOUT = 12


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.first_product = (By.CSS_SELECTOR, "a[href^='product.php?id=']")
        self.first_category = (By.CSS_SELECTOR, "a[href='mens-wear.php']")
        self.shop_menu = (By.CSS_SELECTOR, ".nav-link.dropdown-toggle")
        self.mens_shop_now = (
            By.XPATH,
            "//a[contains(@href,'mens-wear.php') and contains(.,'Shop Now')]"
        )
        self.add_to_cart = (By.CSS_SELECTOR, ".addToCart")
        self.cart_icon = (By.ID, "cartdesk")
        self.cart_count = (By.ID, "cartCount")
        self.cart_page_marker = (
            By.XPATH,
            "//*[contains(.,'Shopping Cart') or contains(.,'Cart')]"
        )
        self.filter_headers = (
            By.TAG_NAME,
            "h5"
        )
        self.product_links = (By.CSS_SELECTOR, "a[href^='product.php?id=']")
        self.product_detail_content = (
            By.XPATH,
            "//*[contains(.,'Description') or contains(.,'Add to Cart')]"
        )
        self.categories = (
            "mens-wear.php",
            "womens-wear.php",
            "kids-wear.php",
            "electronics.php",
        )

    def navigate_to_shop(self):
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.url_contains("shop.php")
        )

    def click_mens_shop_now(self):
        mens_shop = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.mens_shop_now)
        )
        self.driver.execute_script("arguments[0].click();", mens_shop)
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.url_contains("mens-wear.php")
        )

    def click_product(self):
        if not self.driver.find_elements(*self.first_product):
            category = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located(self.first_category)
            )
            self.driver.execute_script("arguments[0].click();", category)

        product = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.first_product)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            product,
        )
        self.driver.execute_script("arguments[0].click();", product)

    def is_product_page_displayed(self):
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.url_contains("product.php")
        )
        return WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.product_detail_content)
        ).is_displayed()

    def click_add_to_cart(self):
        button = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.add_to_cart)
        )
        self.driver.execute_script("arguments[0].click();", button)

        WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            lambda driver: self.get_cart_count() != "0"
        )

    def click_cart_icon(self):
        cart = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.cart_icon)
        )
        self.driver.execute_script("arguments[0].click();", cart)

    def is_cart_page_displayed(self):
        return WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.url_contains("cart.php")
        )

    def get_cart_count(self):
        return WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.cart_count)
        ).text

    def _open_category(self, category):
        self.driver.get(f"{BASE_URL}{category}")
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.url_contains(category)
        )

    def _visible_product_links(self):
        return WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.presence_of_all_elements_located(self.product_links)
        )

    def browse_categories_filters_and_products(self):
        for category in self.categories:
            self._open_category(category)

            filters = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
                lambda driver: [
                    header for header in driver.find_elements(*self.filter_headers)
                    if "FILTER BY" in header.text
                ]
            )
            products = self._visible_product_links()

            if not filters or not products:
                return False

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(self.driver, WAIT_TIMEOUT).until(
                lambda driver: driver.execute_script("return window.scrollY") > 0
            )
            self.driver.execute_script("window.scrollTo(0, 0);")

            product_url = products[min(1, len(products) - 1)].get_attribute("href")
            self.driver.get(product_url)
            if not self.is_product_page_displayed():
                return False

        return True
