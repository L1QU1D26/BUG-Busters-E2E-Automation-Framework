from pages.home_page import HomePage
from pages.search_page import SearchPage

def test_search_product(setup):

    driver = setup

    home = HomePage(driver)
    search = SearchPage(driver)

    home.search_product("iPhone")

    assert "iPhone" in search.get_product_name()