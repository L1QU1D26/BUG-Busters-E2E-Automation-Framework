from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage:

    WAIT_TIME = 5
    FIRST_PRODUCT = (By.CSS_SELECTOR, "a[href='product.php?id=21']")
    ADD_TO_CART = (By.CSS_SELECTOR, ".addToCart")
    CART_COUNT = (By.ID, "cartCount")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIME)

    def click_product(self):
        self.driver.get("https://shop.qaautomationlabs.com/mens-wear.php")
        self.wait.until(EC.url_contains("mens-wear.php"))
        self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT)).click()

    def click_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()

    def is_product_detail_displayed(self):
        self.wait.until(EC.url_contains("product.php"))
        return "product.php" in self.driver.current_url

    def is_product_added_to_cart(self):
        self.wait.until(EC.text_to_be_present_in_element(self.CART_COUNT, "1"))
        return self.driver.find_element(*self.CART_COUNT).text == "1"
