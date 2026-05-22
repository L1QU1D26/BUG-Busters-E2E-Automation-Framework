from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.authentication import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):
    

    def __init__(self, driver):
        super().__init__(driver)

    def login_site(self, email,password):
        self.enter_text(LoginLocators.USERNAME,email)
        self.enter_text(LoginLocators.PASSWORD,password)
        self.click(LoginLocators.LOGIN_BUTTON)
        

    def is_dashboard_displayed(self):       
        text=self.get_text(LoginLocators.PRODUCT_TITLE)
        print(text)
        return text == "Shop"
    
    def is_error_displayed(self):
        return self.is_visible(
            LoginLocators.ERROR_MESSAGE
        )
    
    def empty_email_error(self):
        return self.is_visible(
            LoginLocators.EMPTY_EMAIL
        )

    
    def empty_pass_error(self):
        return self.is_visible(
            LoginLocators.EMPTY_PASS
        )
    
    def click_logout(self):
        self.click(LoginLocators.LOGOUT_BUTTON)
       

    def is_login_page_displayed(self):
        #print(self.driver.current_url)
        self.wait.until(EC.visibility_of_element_located(LoginLocators.LOGIN_TEXT))
        return self.is_visible(LoginLocators.LOGIN_TEXT)
    

    
    

    
    
