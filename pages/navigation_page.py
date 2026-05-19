from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class NavigationPage:

    WAIT_TIME = 5
    PRODUCTS_MENU = (By.CSS_SELECTOR, ".nav-link.dropdown-toggle")
    VIEW_ALL_PRODUCTS = (By.CSS_SELECTOR, ".dropdown-menu a[href='shop.php']")
    CART_ICON = (By.ID, "cartdesk")
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, ".product-offer")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIME)

    def click_products_menu(self):
        menu = self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_MENU))
        ActionChains(self.driver).move_to_element(menu).perform()
        self.wait.until(EC.element_to_be_clickable(self.VIEW_ALL_PRODUCTS)).click()

    def click_cart_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()

    def is_products_page_displayed(self):
        self.wait.until(EC.url_contains("shop.php"))
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_CATEGORY)).is_displayed()

    def is_cart_page_opened(self):
        self.wait.until(EC.url_contains("cart"))
        return "cart" in self.driver.current_url.lower()
