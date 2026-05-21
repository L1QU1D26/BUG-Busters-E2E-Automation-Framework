from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def open_url(self):

        self.driver.get("https://shop.qaautomationlabs.com/")
        #self.driver.maximize_window()

        self.driver.maximize_window()

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        element.click()

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

    def wait_for_url_contains(self, expected_text):

        return self.wait.until(
            EC.url_contains(expected_text)
        )

    def wait_for_page_ready(self):

        return self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    def scroll_to_element(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        return element

    def scroll_to_bottom(self):

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
