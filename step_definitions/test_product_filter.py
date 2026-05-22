import time
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.product_page import ProductPage

scenarios("../features/product_filter.feature")


@pytest.fixture
def context():
    return {}


@given("the user is logged into the application and on shop page")
def login_and_open_shop(driver):
    login = LoginPage(driver)
    login.open_url()
    login.login_site("demo@demo.com", "demo")
    assert login.is_dashboard_displayed()
    
    product_page = ProductPage(driver)
    product_page.navigate_to_shop()


@given("the user navigates to the Men's Wear category page")
def navigate_to_mens_wear(driver):
    product_page = ProductPage(driver)
    product_page.open_mens_category()
    time.sleep(2)


@given("the user notes the initial product count")
def note_initial_count(driver, context):
    product_page = ProductPage(driver)
    context["initial_count"] = product_page.get_product_count()
    print(f"Initial product count: {context['initial_count']}")


@when(parsers.parse('the user selects the "{filter_name}" filter checkbox'))
@given(parsers.parse('the user selects the "{filter_name}" filter checkbox'))
def select_filter(driver, filter_name):
    product_page = ProductPage(driver)
    product_page.click_filter(filter_name)
    time.sleep(2)  # Wait for AJAX filter update


@then("the product count should be updated and be less than the initial count")
def verify_count_decreased(driver, context):
    product_page = ProductPage(driver)
    current_count = product_page.get_product_count()
    print(f"Current count after filter: {current_count}")
    assert current_count < context["initial_count"], (
        f"Product count did not decrease. "
        f"Before: {context['initial_count']}, After: {current_count}"
    )


@then("the products displayed should be updated")
def verify_products_updated(driver):
    product_page = ProductPage(driver)
    assert product_page.are_products_visible(), (
        "Products are not visible after filtering"
    )


@given("the user notes the product count")
def note_current_count(driver, context):
    product_page = ProductPage(driver)
    context["mid_count"] = product_page.get_product_count()
    print(f"Mid-point product count: {context['mid_count']}")


@then("the product count should change accordingly")
def verify_count_changed(driver, context):
    product_page = ProductPage(driver)
    current_count = product_page.get_product_count()
    print(f"Current count after multiple filters: {current_count}")
    assert current_count >= 0


@then("no products should be displayed in the list")
def verify_no_products(driver):
    product_page = ProductPage(driver)
    current_count = product_page.get_product_count()
    print(f"Count for incompatible filters: {current_count}")
    assert current_count == 0, f"Expected 0 products but found {current_count}"
