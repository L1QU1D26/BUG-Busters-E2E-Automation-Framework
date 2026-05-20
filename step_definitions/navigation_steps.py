from pages.navigation_page import NavigationPage


class TestNavigation:

    def test_navigation_to_products(self, driver):

        navigation = NavigationPage(driver)

        navigation.click_products_menu()
        navigation.click_view_all_products()

        assert navigation.is_products_page_displayed()