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

@when("user enters invalid credentials")
def enter_invalid_credentials(driver):
    page=LoginPage(driver)
    page.login_site("demo@wrong.com","demi")

@then("login error should display")
def verify_display_error(driver):
    page = LoginPage(driver)
    assert page.is_error_displayed()

@when("user enters empty username and valid password")
def empty_username(driver):
    page = LoginPage(driver)
    page.login_site("","demo")

@then("empty email error should display")
def verify_empty_email(driver):
    page = LoginPage(driver)
    assert page.empty_email_error()

@when("user enters valid username and empty password")
def empty_password(driver):
    page = LoginPage(driver)
    page.login_site("demo@demo.com","")

@then("empty password error should display")
def verify_empty_password(driver):
    page = LoginPage(driver)
    assert page.empty_pass_error()

@when("user clicks logout button")
def click_logout(driver):
    page = LoginPage(driver)
    page.click_logout()

@then("user should navigate to login page")
def verify_logout(driver):
    page = LoginPage(driver)
    assert page.is_login_page_displayed()

@when("user clicks browser back button")
def browser_back(driver):
    driver.back()
    driver.refresh()

@then("user should remain on login page")
def validate_session(driver):
    page = LoginPage(driver)
    assert page.is_login_page_displayed()
