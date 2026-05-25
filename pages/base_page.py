from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        _timeout = int(os.getenv("CI_WAIT_TIMEOUT", "20"))
        self.wait = WebDriverWait(driver, _timeout)

    def open_url(self):

        self.driver.get("https://shop.qaautomationlabs.com/")

    def click(self, locator):

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()
        

    def enter_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def is_visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()
    
    def get_elements(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
    def find_element(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def js_click(self, locator):
        """JavaScript click — bypasses CSS visibility for hidden dropdown items.
        Required for headless Chrome where hover/ActionChains doesn't open dropdowns."""
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)