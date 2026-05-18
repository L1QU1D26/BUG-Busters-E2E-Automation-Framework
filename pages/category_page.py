from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CategoryPage(BasePage):

    TITLE = (By.TAG_NAME, "h2")

    def get_title(self):

        return self.driver.find_element(*self.TITLE).text