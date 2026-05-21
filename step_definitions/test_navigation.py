from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage


scenarios("../features/navigation.feature")


@given("user is logged into the application")
def login_user(driver):

    login = LoginPage(driver)

    login.open_url()
    login.login_site("demo@demo.com", "demo")

    assert login.is_dashboard_displayed()


@given("user is on mens wear page")
def open_mens_page(driver):

    login_user(driver)

    navigation = NavigationPage(driver)

    navigation.click_mens_wear()

    assert navigation.is_mens_page_displayed()


@when("user clicks Mens Wear from Shop menu")
def click_mens_wear(driver):

    navigation = NavigationPage(driver)

    navigation.click_mens_wear()


@then("Mens Wear page should be displayed")
def validate_mens_page(driver):

    navigation = NavigationPage(driver)

    assert navigation.is_mens_page_displayed()


@when("user clicks cart icon")
def click_cart(driver):

    navigation = NavigationPage(driver)

    navigation.click_cart_icon()


@then("cart page should be displayed")
def validate_cart_page(driver):

    navigation = NavigationPage(driver)

    assert navigation.is_cart_page_displayed()


@when("user clicks Go To Back button")
def click_back(driver):

    navigation = NavigationPage(driver)

    navigation.click_go_back()


@then("shop page should be displayed")
def validate_shop_page(driver):

    navigation = NavigationPage(driver)

    assert navigation.is_shop_page_displayed()