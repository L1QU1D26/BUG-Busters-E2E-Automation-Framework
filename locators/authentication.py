from selenium.webdriver.common.by import By

class LoginLocators:

    LOGIN_TEXT = (By.XPATH,"//span[text()='Login']")
    USERNAME =(By.ID,"email")
    PASSWORD= (By.ID,"password")
    LOGIN_BUTTON= (By.ID,"loginBtn")
    PRODUCT_TITLE = (By.XPATH,"//a[text()='Shop']")
    ERROR_MESSAGE = (By.ID,"errorMsg") 
    EMPTY_EMAIL = (By.ID,"emailerror") 
    EMPTY_PASS = (By.ID,"passerror")
    LOGOUT_BUTTON = (By.ID,"logoutBtn")


     
