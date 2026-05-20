from pytest_bdd import scenarios
from pytest_bdd import given, when, then  

from pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("user open login page")
def open_login(driver):
    login = LoginPage(driver)
    login.open_url()
    
@when("user enters valid username and password")
def valid_login(driver):
    login = LoginPage(driver)
    login.login_site("demo@demo.com","demo")

@then("user should navigate to inventory page")
def login_page_verification(driver):
     page = LoginPage(driver)
     assert page.is_dashboard_displayed()