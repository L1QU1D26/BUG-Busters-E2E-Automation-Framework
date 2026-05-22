import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutValidationPage


scenarios("../features/checkout.feature")


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def checkout_page(driver):
    return CheckoutValidationPage(driver)


@given("user launches the application login page")
def launch_application(driver):
    driver.get("https://shop.qaautomationlabs.com/")


@given("user logs in with valid credentials")
def login_user(login_page):

    login_page.login_site(
        "demo@demo.com",
        "demo"
    )

    assert login_page.is_dashboard_displayed()


@given("user adds a product to cart")
def add_product_to_cart(cart_page):

    cart_page.open_category("Mens Wear")
    cart_page.add_product_to_cart(1)
    cart_page.open_cart()


@given("user is on the cart page")
def verify_cart_page(checkout_page):

    assert checkout_page.is_cart_page_displayed(), \
        "User is not on cart page"


@given("user clicks on the proceed checkout button")
def click_proceed_checkout(checkout_page):

    checkout_page.click_proceed_to_checkout()


@then("user should be landed on the checkout page")
def validate_checkout_page(checkout_page):

    assert checkout_page.is_checkout_page_displayed(), \
        "User is not navigated to checkout page"


@when("user fills all required billing details")
def fill_billing_details(checkout_page):

    checkout_page.fill_all_required_details(
        first_name="Ganesh",
        last_name="Jangam",
        address="Hyderabad",
        city="Hyderabad",
        state="Telangana",
        postcode="500001",
        phone="9876543210",
        email="ganesh@test.com"
    )


@given("clicks on the continue button")
@when("clicks on the continue button")
def click_continue(checkout_page):

    checkout_page.click_continue()


@then("user should see the order confirmation")
def validate_confirm_page(checkout_page):

    assert checkout_page.is_confirm_page_displayed(), \
        "User is not navigated to confirmation page"


@when("user clears the address field")
def clear_address(checkout_page):

    checkout_page.clear_address_field()


@when("user clears the first name field")
def clear_first_name(checkout_page):

    checkout_page.clear_first_name_field()


@then('error message "Please enter your address." should be displayed')
def validate_address_error(checkout_page):

    errors = checkout_page.get_validation_errors()

    assert any(
        "Please enter your address." in error
        for error in errors
    ), "Address validation message not displayed"


@then('error message "Please enter your first name." should be displayed')
def validate_first_name_error(checkout_page):

    errors = checkout_page.get_validation_errors()

    assert any(
        "Please enter your first name." in error
        for error in errors
    ), "First name validation message not displayed"


@then(parsers.parse('error message "{msg}" should be displayed'))
def validate_generic_error(checkout_page, msg):

    errors = checkout_page.get_validation_errors()

    assert any(
        msg in error
        for error in errors
    ), f"Validation message not displayed: {msg} - found: {errors}"


@when("user clears all mandatory fields")
def clear_all_fields(checkout_page):

    checkout_page.clear_all_mandatory_fields()


@then("validation errors should be displayed for all required fields")
def validate_all_errors(checkout_page):

    errors = checkout_page.get_validation_errors()

    expected_errors = [
        "Please enter your first name.",
        "Please enter your last name.",
        "Please enter your email.",
        "Please enter your phone.",
        "Please enter your address.",
        "Please enter your state.",
        "Please enter your city.",
        "Please enter your pin code."
    ]

    for expected_error in expected_errors:

        assert any(
            expected_error in error
            for error in errors
        ), f"Validation error missing: {expected_error}"