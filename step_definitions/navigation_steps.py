from pytest_bdd import scenarios, given, when, then
from pages.navigation_page import NavigationPage
from config.constants import BASE_URL


scenarios("../features/navigate.feature")


@given("the user is on the homepage")
def open_homepage(driver):
    driver.get(BASE_URL)


@when("the user clicks on Products menu")
def click_products_menu(driver):
    navigation = NavigationPage(driver)

    navigation.click_products_menu()
    navigation.click_view_all_products()


@then("the products page should be displayed")
def validate_products_page(driver):
    navigation = NavigationPage(driver)

    assert navigation.is_products_page_displayed()


@when("the user clicks on Cart icon")
def click_cart_icon(driver):
    navigation = NavigationPage(driver)

    navigation.click_cart_icon()


@then("the cart page should open")
def validate_cart_page(driver):
    navigation = NavigationPage(driver)
    assert navigation.is_cart_page_displayed()