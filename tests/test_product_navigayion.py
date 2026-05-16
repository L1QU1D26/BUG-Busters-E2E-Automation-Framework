from pages.product_page import ProductPage


def test_product_search(setup):

    driver = setup
    driver.get("https://tutorialsninja.com/demo/")

    product = ProductPage(driver)

    product.search_product("MacBook")

    assert "MacBook" in product.get_product_title()


def test_category_navigation(setup):

    driver = setup
    driver.get("https://tutorialsninja.com/demo/")

    product = ProductPage(driver)

    product.open_category()

    assert "Laptops" in driver.page_source