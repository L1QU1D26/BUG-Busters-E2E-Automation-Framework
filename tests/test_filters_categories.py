from pages.home_page import HomePage
from pages.category_page import CategoryPage

def test_desktops_category(setup):

    driver = setup

    home = HomePage(driver)
    category = CategoryPage(driver)

    home.click_desktops()

    assert "Desktops" in category.get_title()