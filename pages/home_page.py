from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):

    SEARCH_BOX = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default")
    DESKTOPS = (By.LINK_TEXT, "Desktops")

    def search_product(self, product):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        ).send_keys(product)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()

    def click_desktops(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DESKTOPS)
        ).click()