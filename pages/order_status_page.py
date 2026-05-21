from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_status_locators import OrderStatusLocators


class OrderStatusPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderStatusLocators

    def click_place_order(self):
        self.click(self.locators.PLACE_ORDER_BUTTON)

    def is_thanks_page_loaded(self):
        self.wait.until(EC.url_contains(self.locators.THANKS_PAGE_URL))
        return self.locators.THANKS_PAGE_URL in self.driver.current_url

    def is_confirm_page_loaded(self):
        self.wait.until(EC.url_contains(self.locators.CONFIRM_PAGE_URL))
        return self.locators.CONFIRM_PAGE_URL in self.driver.current_url

    def is_place_order_button_visible(self):
        return self.is_visible(self.locators.PLACE_ORDER_BUTTON)

    def get_thank_you_message(self):
        return self.get_text(self.locators.THANK_YOU_MESSAGE)

    