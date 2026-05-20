from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#import time

class LoginPage(BasePage):
    USERNAME =(By.ID,"email")
    PASSWORD= (By.ID,"password")
    LOGIN_BUTTON= (By.ID,"loginBtn")
    PRODUCT_TITLE = (
    By.XPATH,
    "//a[text()='Shop']"
)

    def __init__(self, driver):
        super().__init__(driver)

    def login_site(self, email,password):
        self.driver.find_element(*self.USERNAME).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        button=self.driver.find_element(*self.LOGIN_BUTTON)
        button.click()

    def is_dashboard_displayed(self):
        text=self.driver.find_element(*self.PRODUCT_TITLE).text 
        print(text)
        return text == "Shop"
