from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderStatusPage(BasePage):
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//*[@id='userForm']/div/div/div[2]/div[1]/div/a"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[@id='userForm']/div/div/div/p"
    )

   

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)

    def is_order_confirmation_page_loaded(self):
        return "order-received" in self.driver.current_url

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    