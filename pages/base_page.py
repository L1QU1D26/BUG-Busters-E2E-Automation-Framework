from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        
    def open_url(self):
        self.driver.get("https://shop.qaautomationlabs.com/")
        #self.driver.maximize_window()