from pages.base_page import BasePage
from locators.navigation_locators import NavigationLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class NavigationPage(BasePage):

    CATEGORY_LOCATORS = {
        "mens wear": NavigationLocators.MENS_WEAR,
        "womens wear": NavigationLocators.WOMENS_WEAR,
        "kids wear": NavigationLocators.KIDS_WEAR,
        "electronics": NavigationLocators.ELECTRONICS,
    }

    CATEGORY_URLS = {
        "mens wear": "mens-wear.php",
        "womens wear": "womens-wear.php",
        "kids wear": "kids-wear.php",
        "electronics": "electronics.php",
    }

    def __init__(self, driver):
        super().__init__(driver)

    def normalize_category(self, category):

        return category.strip().lower()

    def hover_shop_menu(self):

        shop = self.find_element(
            NavigationLocators.SHOP_MENU
        )

        ActionChains(self.driver).move_to_element(shop).perform()

    def click_mens_wear(self):

        self.hover_shop_menu()

        self.click(
            NavigationLocators.MENS_WEAR
        )

    def click_womens_wear(self):

        self.hover_shop_menu()

        self.click(
            NavigationLocators.WOMENS_WEAR
        )

    def click_kids_wear(self):

        self.hover_shop_menu()

        self.click(
            NavigationLocators.KIDS_WEAR
        )

    def click_electronics(self):

        self.hover_shop_menu()

        self.click(
            NavigationLocators.ELECTRONICS
        )

    def click_category(self, category):

        category_name = self.normalize_category(category)

        self.hover_shop_menu()

        category_link = self.wait.until(
            EC.visibility_of_element_located(
                self.CATEGORY_LOCATORS[category_name]
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            category_link
        )

        self.wait_for_category_page(category)

    def open_category(self, category):

        category_name = self.normalize_category(category)

        self.driver.get(
            self.CATEGORY_URLS[category_name]
        )

        self.wait_for_category_page(category)

    def click_category_menu_link(self, category):

        category_name = self.normalize_category(category)

        self.click(
            self.CATEGORY_LOCATORS[category_name]
        )

        self.wait_for_category_page(category)

    def wait_for_category_page(self, category):

        category_name = self.normalize_category(category)

        return self.wait_for_url_contains(
            self.CATEGORY_URLS[category_name]
        )

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

    def is_category_page_displayed(self, category):

        category_name = self.normalize_category(category)

        return self.CATEGORY_URLS[category_name] in self.driver.current_url

    def is_cart_page_displayed(self):

        return "cart.php" in self.driver.current_url

    def is_shop_page_displayed(self):

        return "shop.php" in self.driver.current_url
