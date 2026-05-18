from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):

    PRODUCT = (By.CSS_SELECTOR, "h4")

    def get_product_name(self):

        return self.driver.find_element(*self.PRODUCT).text