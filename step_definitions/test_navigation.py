import time

from pytest_bdd import parsers, scenarios, given, when, then

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage


scenarios("../features/navigation.feature")

NAVIGATION_CATEGORIES = (
    "Mens Wear",
    "Womens Wear",
    "Kids Wear",
    "Electronics",
)

SCREEN_TIME = 2


@given("user is logged into the application")
def login_user(driver):

    login = LoginPage(driver)

    login.open_url()
    time.sleep(SCREEN_TIME)

    login.login_site("demo@demo.com", "demo")

    assert login.is_dashboard_displayed()
    time.sleep(SCREEN_TIME)


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


@when(parsers.parse('user clicks "{category}" from Shop menu'))
def click_category(driver, category):

    navigation = NavigationPage(driver)

    navigation.click_category(category)


@when("user slowly visits all Shop categories")
def slowly_visit_all_categories(driver):

    navigation = NavigationPage(driver)

    for category in NAVIGATION_CATEGORIES:
        navigation.click_category(category)
        assert navigation.is_category_page_displayed(category)
        time.sleep(SCREEN_TIME)


@then("Mens Wear page should be displayed")
def validate_mens_page(driver):

    navigation = NavigationPage(driver)

    assert navigation.is_mens_page_displayed()


@then(parsers.parse('"{category}" page should be displayed'))
def validate_category_page(driver, category):

    navigation = NavigationPage(driver)

    assert navigation.is_category_page_displayed(category)


@then("Electronics page should be displayed")
def validate_electronics_page(driver):

    navigation = NavigationPage(driver)

    assert navigation.is_electronics_page_displayed()
    time.sleep(SCREEN_TIME)


@when("user clicks cart icon")
def click_cart(driver):

    navigation = NavigationPage(driver)

    navigation.click_cart_icon()
    time.sleep(SCREEN_TIME)


@then("cart page should be displayed")
def validate_cart_page(driver):

    navigation = NavigationPage(driver)

    assert navigation.is_cart_page_displayed()
    time.sleep(SCREEN_TIME)


@when("user clicks Go To Back button")
def click_back(driver):

    navigation = NavigationPage(driver)

    navigation.click_go_back()
    time.sleep(SCREEN_TIME)


@then("shop page should be displayed")
def validate_shop_page(driver):

    navigation = NavigationPage(driver)

    assert navigation.is_shop_page_displayed()
    time.sleep(SCREEN_TIME)
