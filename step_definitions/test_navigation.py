from pytest_bdd import given, scenarios, then, when
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage


scenarios("../features/navigate.feature")


@given("the user is on the homepage")
def open_homepage(driver):
    login = LoginPage(driver)

    login.open_url()
    login.login_site("demo@demo.com", "demo")


@when("the user clicks on Products menu")
def click_products_menu(driver):
    navigation = NavigationPage(driver)

    navigation.click_products_menu()
    navigation.click_view_all_products()


@then("the products page should be displayed")
def verify_products_page(driver):
    navigation = NavigationPage(driver)

    assert navigation.is_products_page_displayed()


@given("the user is logged in")
def login_user(driver):
    login = LoginPage(driver)

    login.open_url()
    login.login_site("demo@demo.com", "demo")

    assert login.is_dashboard_displayed()


@when("the user clicks on Cart icon")
def click_cart_icon(driver):
    navigation = NavigationPage(driver)

    navigation.click_cart_icon()


@then("the cart page should open")
def verify_cart_page(driver):
    assert WebDriverWait(driver, 8).until(
        EC.url_contains("cart.php")
    )
