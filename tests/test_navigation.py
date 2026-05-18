from pages.home_page import HomePage
from pages.search_page import SearchPage

def test_product_validation(setup):

    driver = setup

    home = HomePage(driver)
    search = SearchPage(driver)

    home.search_product("MacBook")

    assert "MacBook" in search.get_product_name()