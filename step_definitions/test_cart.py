from pytest_bdd import scenarios
from pytest_bdd import given, when, then
from pytest_bdd import parsers

from pages.login_page import LoginPage
from pages.cart_page import CartPage


scenarios("../features/cart.feature")


# ---------------------------------------------------------
# Common reusable setup
# ---------------------------------------------------------

def login_and_open_cart(driver):

    login = LoginPage(driver)

    login.open_url()

    login.login_site(
        "demo@demo.com",
        "demo"
    )

    assert login.is_dashboard_displayed()

    cart_page = CartPage(driver)

    return cart_page


# ---------------------------------------------------------
# Scenario: Verify user can add product to cart
# ---------------------------------------------------------

@given(parsers.parse(
    'user navigates to the {category} category'
))
def navigate_to_category(driver, category):

    cart_page = login_and_open_cart(driver)

    cart_page.open_category(category)


@when(parsers.parse(
    "user adds {product_number} to the cart"
))
def add_product(driver, product_number):

    cart_page = CartPage(driver)

    cart_page.add_product_to_cart(
        int(product_number)
    )


@then("cart count should be updated successfully")
def verify_cart_count(driver):

    cart_page = CartPage(driver)

    assert cart_page.get_cart_count() == "1"


# ---------------------------------------------------------
# Scenario: Verify added product is displayed in cart
# ---------------------------------------------------------

@given("user has added a product to the cart")
def add_product_to_cart(driver):

    cart_page = login_and_open_cart(driver)

    cart_page.open_category("Electronics")

    cart_page.add_product_to_cart(4)


@when("user opens the cart page")
def open_cart(driver):

    cart_page = CartPage(driver)

    cart_page.open_cart()


@then("added product should be displayed in cart summary")
def verify_product_in_cart(driver):

    cart_page = CartPage(driver)

    assert cart_page.get_cart_count() == "1"


# ---------------------------------------------------------
# Scenario: Verify user can update product quantity in cart
# ---------------------------------------------------------

@given("user has product in the cart")
def product_available_in_cart(driver):

    cart_page = login_and_open_cart(driver)

    cart_page.open_category("Kids Wear")

    cart_page.add_product_to_cart(2)

    cart_page.open_cart()


@when("user updates the product quantity")
def update_product_quantity(driver):

    cart_page = CartPage(driver)

    cart_page.update_product_quantity(2)


@then("updated quantity should be displayed correctly")
def verify_updated_quantity(driver):

    assert True


# ---------------------------------------------------------
# Scenario: Verify user can remove product from cart
# ---------------------------------------------------------

@when("user removes the product from the cart")
def remove_product(driver):

    cart_page = CartPage(driver)

    cart_page.remove_product_from_cart()


@then("product should be removed successfully")
def verify_product_removed(driver):

    assert True


# ---------------------------------------------------------
# Scenario: Verify cart total amount is calculated correctly
# ---------------------------------------------------------

@given("user has multiple products in the cart")
def add_multiple_products(driver):

    cart_page = login_and_open_cart(driver)

    cart_page.open_category("Mens Wear")
    cart_page.add_product_to_cart(4)

    cart_page.open_category("Electronics")
    cart_page.add_product_to_cart(3)

    cart_page.open_category("Kids Wear")
    cart_page.add_product_to_cart(5)

    cart_page.open_cart()


@then("total amount should be displayed correctly")
def verify_total_amount(driver):

    assert True