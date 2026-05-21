import time

from pytest_bdd import parsers, scenarios, given, when, then

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.product_page import ProductPage

scenarios("../features/product.feature")

PRODUCT_CATEGORIES = (
    ("Mens Wear", 1),
    ("Womens Wear", 2),
    ("Kids Wear", 1),
    ("Electronics", 2),
)

SCREEN_TIME = 2


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
    product.wait_for_products()


@given("the user is logged in for product testing")
def login_for_product_testing(driver):

    login = LoginPage(driver)

    login.open_url()
    time.sleep(SCREEN_TIME)

    login.login_site("demo@demo.com", "demo")

    assert login.is_dashboard_displayed()
    time.sleep(SCREEN_TIME)


@given(parsers.parse('the user opens the "{category}" category'))
def open_category_page(driver, category):

    login = LoginPage(driver)
    navigation = NavigationPage(driver)
    product = ProductPage(driver)

    login.open_url()
    login.login_site("demo@demo.com", "demo")

    assert login.is_dashboard_displayed()

    navigation.click_category(category)

    assert navigation.is_category_page_displayed(category)
    product.wait_for_products()


@when("the user slowly checks products in all categories")
def slowly_check_all_product_categories(driver):

    navigation = NavigationPage(driver)
    product = ProductPage(driver)

    for category, product_number in PRODUCT_CATEGORIES:
        navigation.click_category(category)
        assert navigation.is_category_page_displayed(category)
        time.sleep(SCREEN_TIME)

        assert product.wait_for_filters()
        time.sleep(SCREEN_TIME)

        product.scroll_through_products()
        time.sleep(SCREEN_TIME)

        product.click_add_to_cart_by_number(1)
        time.sleep(SCREEN_TIME)

        product.click_product_by_number(product_number)
        assert product.is_product_page_displayed()
        time.sleep(SCREEN_TIME + 1)

        driver.back()
        navigation.wait_for_category_page(category)
        product.wait_for_products()
        time.sleep(SCREEN_TIME)

    product.click_cart_icon()
    time.sleep(SCREEN_TIME + 1)


@when("the user clicks on a product")
def click_product(driver):

    product = ProductPage(driver)

    # Click product NAME to open details page
    product.click_product()


@when(parsers.parse("the user opens product number {product_number:d}"))
def click_product_by_number(driver, product_number):

    product = ProductPage(driver)

    product.click_product_by_number(product_number)


@when("the user scrolls through the products")
def scroll_products(driver):

    product = ProductPage(driver)

    product.scroll_through_products()


@when(parsers.parse("the user adds product number {product_number:d} to the cart"))
def add_product_by_number_to_cart(driver, product_number):

    product = ProductPage(driver)

    product.click_add_to_cart_by_number(product_number)
    product.click_cart_icon()


@then("product details should be displayed")
def validate_product_details(driver):

    product = ProductPage(driver)

    assert product.is_product_page_displayed()
    time.sleep(SCREEN_TIME + 1)


@then("category filters should be visible")
def validate_filters(driver):

    product = ProductPage(driver)

    assert product.wait_for_filters()
    time.sleep(SCREEN_TIME)


@then(parsers.parse('products should be displayed for "{category}"'))
def validate_products_for_category(driver, category):

    navigation = NavigationPage(driver)
    product = ProductPage(driver)

    assert navigation.is_category_page_displayed(category)
    assert len(product.wait_for_products()) > 0


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
    time.sleep(SCREEN_TIME + 1)
