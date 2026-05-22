from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage
from pages.product_page import ProductPage

scenarios("../features/product.feature")


# =========================================
# COMMON LOGIN FLOW
# =========================================

def login_and_open(driver):

    login = LoginPage(driver)

    login.open_url()

    login.login_site(
        "demo@demo.com",
        "demo"
    )

    assert login.is_dashboard_displayed()


# =========================================
# MENS CATEGORY
# =========================================

@given("the user is on the mens products page")
def open_mens_products(driver):

    login_and_open(driver)

    product = ProductPage(driver)

    product.navigate_to_shop()

    product.open_mens_category()


@given("the user is viewing a mens product")
def viewing_mens_product(driver):

    login_and_open(driver)

    product = ProductPage(driver)

    product.navigate_to_shop()

    product.open_mens_category()

    product.click_product()


# =========================================
# WOMENS CATEGORY
# =========================================

@given("the user is on the womens products page")
def open_womens_products(driver):

    login_and_open(driver)

    product = ProductPage(driver)

    product.navigate_to_shop()

    product.open_womens_category()


# =========================================
# KIDS CATEGORY
# =========================================

@given("the user is on the kids products page")
def open_kids_products(driver):

    login_and_open(driver)

    product = ProductPage(driver)

    product.navigate_to_shop()

    product.open_kids_category()


# =========================================
# ELECTRONICS CATEGORY
# =========================================

@given("the user is on the electronics products page")
def open_electronics_products(driver):

    login_and_open(driver)

    product = ProductPage(driver)

    product.navigate_to_shop()

    product.open_electronics_category()


# =========================================
# ACTIONS
# =========================================

@when("the user clicks on a product")
def click_product(driver):

    product = ProductPage(driver)

    product.click_product()


@when("the user clicks Add to Cart")
def click_add_to_cart(driver):

    product = ProductPage(driver)

    product.click_add_to_cart()

    product.click_cart_icon()


# =========================================
# VALIDATIONS
# =========================================

@then("product details should be displayed")
def validate_product_details(driver):

    product = ProductPage(driver)

    assert product.is_product_page_displayed()


@then("the product should be added to the cart")
def validate_cart(driver):

    product = ProductPage(driver)

    assert product.is_cart_page_displayed()


@then("products should be visible")
def validate_products(driver):

    product = ProductPage(driver)

    assert product.are_products_visible()


@then("cart count badge should update")
def validate_cart_badge(driver):

    product = ProductPage(driver)

    assert int(product.get_cart_count()) >= 1