from pages.home_page import HomePage
from pages.category_page import CategoryPage

def test_navigation_flow(setup):

    driver = setup

    home = HomePage(driver)
    category = CategoryPage(driver)

    home.click_desktops()

    assert "Desktops" in category.get_title()