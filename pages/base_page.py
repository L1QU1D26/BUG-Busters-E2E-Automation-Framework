from selenium.webdriver.common.by import By


class BasePage:

    def _init_(self, driver):
        self.driver = driver

    def do_click(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text