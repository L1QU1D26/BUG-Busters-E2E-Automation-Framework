from pytest_bdd import scenarios, given, when, then
from pages.product_page import ProductPage
from config.constants import BASE_URL


scenarios("../features/product.feature")


@given("the user is on the products page")
def open_products_page(driver):
    driver.get(BASE_URL)


@when("the user clicks on a product")
def click_product(driver):
    product = ProductPage(driver)

    product.click_product()


@then("product details should be displayed")
def validate_product_page(driver):
    product = ProductPage(driver)

    assert product.is_product_page_displayed()


@given("the user is viewing a product")
def viewing_product(driver):
    driver.get(BASE_URL)

    product = ProductPage(driver)
    product.click_product()


@when("the user clicks Add to Cart")
def click_add_to_cart(driver):
    product = ProductPage(driver)

    product.click_add_to_cart()


@then("the product should be added to the cart")
def validate_cart_count(driver):
    product = ProductPage(driver)

    assert product.get_cart_count() == "1"