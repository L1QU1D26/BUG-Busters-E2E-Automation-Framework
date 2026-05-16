from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    # Locators
    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'btn-default')]")
    PRODUCT_TITLE = (By.XPATH, "//h4/a")
    CATEGORY = (By.LINK_TEXT, "Laptops & Notebooks")

    # Constructor
    def __init__(self, driver):
        super()._init_(driver)

    # Search product
    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)
        self.do_click(self.SEARCH_BUTTON)

    # Get product title
    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    # Open category
    def open_category(self):
        self.do_click(self.CATEGORY)