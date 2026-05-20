from pytest_bdd import scenarios, given, when, then

from pages.product_page import ProductPage
from pages.navigation_page import NavigationPage
from config.constants import BASE_URL


scenarios("../features/product.feature")


@given("the user is on the products page")
def open_products_page(driver):

    driver.get(BASE_URL)

    navigation = NavigationPage(driver)

    navigation.click_products_menu()

    assert navigation.is_products_page_displayed()


@when("the user clicks on a product")
def click_product(driver):

    product = ProductPage(driver)

    product.click_product()


@then("product details should be displayed")
def validate_product_page(driver):

    product = ProductPage(driver)

    assert product.is_product_page_displayed()


@given("the user is viewing a product")
def open_product(driver):

    driver.get(BASE_URL)

    navigation = NavigationPage(driver)

    navigation.click_products_menu()
    navigation.click_view_all_products()

    assert navigation.is_products_page_displayed()

    product = ProductPage(driver)

    product.click_product()


@when("the user clicks Add to Cart")
def click_add_to_cart(driver):

    product = ProductPage(driver)

    product.click_add_to_cart()


@then("the product should be added to the cart")
def validate_cart_count(driver):

    product = ProductPage(driver)

    assert "1 item(s)" in product.get_cart_count()