import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutValidationPage
from pages.order_status_page import OrderStatusPage

scenarios("../features/order_status.feature")


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def checkout_page(driver):
    return CheckoutValidationPage(driver)


@pytest.fixture
def order_status_page(driver):
    return OrderStatusPage(driver)


@given(parsers.parse('user launches the application "{url}"'))
def launch_application(driver, url):
    driver.get(url)


@given("user logs in with valid credentials")
def login_user(login_page):

    login_page.login_site(
        "demo@demo.com",
        "demo"
    )


@given("user adds a product to cart")
def add_product_to_cart(cart_page):

    cart_page.open_category("Mens Wear")
    cart_page.add_product_to_cart(1)
    cart_page.open_cart()


@given("user navigates to checkout page")
def navigate_to_checkout(checkout_page):

    checkout_page.click_proceed_to_checkout()

    assert checkout_page.is_checkout_page_displayed(), \
        "User is not navigated to checkout page"


@given("user enters valid checkout details")
def enter_checkout_details(checkout_page):

    checkout_page.fill_all_required_details(
        first_name="Ganesh",
        last_name="Jangam",
        address="Lingampet",
        city="Kamareddy",
        state="Telangana",
        postcode="503108",
        phone="9876543210",
        email="ganesh@test.com"
    )


@given("clicks on the continue button")
@when("clicks on the continue button")
def click_continue_bg(checkout_page):

    checkout_page.click_continue()


@then("user should see the order confirmation")
def validate_confirm_page_order_status(checkout_page):

    assert checkout_page.is_confirm_page_displayed(), \
        "User is not navigated to confirmation page"


@when("user clicks on place order button")
def click_place_order(order_status_page):

    order_status_page.click_place_order()


@then("the thank you page should load successfully")
def validate_thanks_page(order_status_page):

    assert order_status_page.is_thanks_page_loaded(), \
        "Thank you page did not load successfully"


@then("the place order button should be visible")
def validate_place_order_button(order_status_page):

    assert order_status_page.is_place_order_button_visible(), \
        "Place Order button is not visible on confirm page"


@then(parsers.parse(
    'a thank you message "{expected_message}" should be displayed'
))
def validate_thank_you_message(order_status_page, expected_message):

    actual_message = order_status_page.get_thank_you_message()

    assert expected_message in actual_message, \
        f"Expected message: {expected_message}, " \
        f"but got: {actual_message}"