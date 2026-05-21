from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage
from pages.product_page import ProductPage

scenarios("../features/product.feature")


@given("the user is on the products page")
def open_products_page(driver):

    login = LoginPage(driver)
    product = ProductPage(driver)

    # Login flow
    login.open_url()
    login.login_site("demo@demo.com", "demo")

    assert login.is_dashboard_displayed()

    # Navigate to Mens Wear products
    product.navigate_to_shop()
    product.click_mens_shop_now()


@when("the user clicks on a product")
def click_product(driver):

    product = ProductPage(driver)

    # Click product NAME to open details page
    product.click_product()


@then("product details should be displayed")
def validate_product_details(driver):

    product = ProductPage(driver)

    assert product.is_product_page_displayed()


@given("the user is viewing a product")
def viewing_product(driver):

    open_products_page(driver)

    product = ProductPage(driver)

    # Open product details page
    product.click_product()


@when("the user clicks Add to Cart")
def click_add_to_cart(driver):

    product = ProductPage(driver)

    # Add product
    product.click_add_to_cart()

    # Open cart page
    product.click_cart_icon()


@then("the product should be added to the cart")
def validate_cart(driver):

    product = ProductPage(driver)

    assert product.is_cart_page_displayed()


@when("the user checks all product categories")
def check_product_categories(driver):

    product = ProductPage(driver)

    assert product.browse_categories_filters_and_products()


@then("filters and products should be visible for each category")
def validate_category_filters_and_products(driver):

    product = ProductPage(driver)

    assert product.is_product_page_displayed()
