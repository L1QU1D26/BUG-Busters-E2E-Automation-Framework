from pytest_bdd import given, when, then, scenarios
from pages.auth_page import AuthPage

scenarios("../features/authentication.feature")


@given("user is on login page")
def open_login_page(context):
    context.auth = AuthPage(context.driver)
    context.auth.open_login_page()


@when("user enters valid username and password")
def enter_credentials(context):
    context.auth.login("standard_user", "secret_sauce")


@when("user clicks on login button")
def click_login(context):
    context.auth.click_login()


@then("user should be redirected to homepage")
def verify_login(context):
    assert context.auth.is_logged_in()


@given("user is logged in")
def logged_in_user(context):
    context.auth = AuthPage(context.driver)
    context.auth.login("standard_user", "secret_sauce")


@when("user clicks on logout button")
def logout(context):
    context.auth.logout()


@then("user should be redirected to login page")
def verify_logout(context):
    assert context.auth.is_on_login_page()