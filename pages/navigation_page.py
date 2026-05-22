from pages.base_page import BasePage
from locators.navigation_locators import NavigationLocators
from selenium.webdriver.common.action_chains import ActionChains


class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_mens_wear(self):
        self.js_click(NavigationLocators.MENS_WEAR)

    def click_womens_wear(self):
        self.js_click(NavigationLocators.WOMENS_WEAR)

    def click_kids_wear(self):
        self.js_click(NavigationLocators.KIDS_WEAR)

    def click_electronics(self):
        self.js_click(NavigationLocators.ELECTRONICS)

    def click_cart_icon(self):

        self.click(
            NavigationLocators.CART_ICON
        )

    def click_go_back(self):

        self.click(
            NavigationLocators.GO_BACK
        )

    # VALIDATIONS

    def is_mens_page_displayed(self):

        return "mens-wear.php" in self.driver.current_url

    def is_womens_page_displayed(self):

        return "womens-wear.php" in self.driver.current_url

    def is_kids_page_displayed(self):

        return "kids-wear.php" in self.driver.current_url

    def is_electronics_page_displayed(self):

        return "electronics.php" in self.driver.current_url

    def is_cart_page_displayed(self):

        return "cart.php" in self.driver.current_url

    def is_shop_page_displayed(self):

        return "shop.php" in self.driver.current_url