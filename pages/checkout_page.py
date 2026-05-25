from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators

# Generous timeout for page navigation on slow CI runners
NAV_TIMEOUT = 60


class CheckoutValidationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.locators = CheckoutLocators
        self.cart_page_url = CheckoutLocators.CART_PAGE_URL
        self.checkout_page_url = CheckoutLocators.CHECKOUT_PAGE_URL
        self.confirm_page_url = CheckoutLocators.CONFIRM_PAGE_URL

    def is_cart_page_displayed(self):
        """Validates that the user has landed on the cart page."""
        self.wait.until(EC.url_contains(self.cart_page_url))
        return self.driver.current_url == self.cart_page_url

    def click_proceed_to_checkout(self):
        """Clicks the Proceed Checkout button and waits for navigation to checkout.php."""

        nav_wait = WebDriverWait(self.driver, NAV_TIMEOUT)
        try:
            self.click(self.locators.PROCEED_TO_CHECKOUT)
        except Exception:
            proceed_btn = self.wait.until(
                EC.element_to_be_clickable(self.locators.PROCEED_TO_CHECKOUT)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                proceed_btn
            )
            self.driver.execute_script(
                "arguments[0].click();",
                proceed_btn
            )

        # Wait here with generous timeout so is_checkout_page_displayed
        # doesn't race against a slow CI network response.
        nav_wait.until(EC.url_contains("checkout.php"))

    def is_checkout_page_displayed(self):
        """Validates that the user has landed on the checkout page."""
        return "checkout.php" in self.driver.current_url

    def fill_all_required_details(
        self,
        first_name,
        last_name,
        address,
        city,
        state,
        postcode,
        phone,
        email
    ):
        """Fills out the billing form."""

        self.enter_text(self.locators.FIRST_NAME, first_name)
        self.enter_text(self.locators.LAST_NAME, last_name)
        self.enter_text(self.locators.ADDRESS, address)
        self.enter_text(self.locators.CITY, city)
        self.enter_text(self.locators.STATE, state)
        self.enter_text(self.locators.PINCODE, postcode)
        self.enter_text(self.locators.PHONE, phone)
        self.enter_text(self.locators.EMAIL, email)

    def click_continue(self):
        """Clicks the Continue button."""

        try:
            self.click(self.locators.CONTINUE_BUTTON)
        except Exception:
            btn = self.wait.until(
                EC.element_to_be_clickable(self.locators.CONTINUE_BUTTON)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                btn
            )
            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

    def is_confirm_page_displayed(self):
        """Validates that the user has landed on the confirm page."""
        # Use a generous timeout because CI runners can be slow to serve confirm.php
        WebDriverWait(self.driver, NAV_TIMEOUT).until(EC.url_contains("confirm.php"))
        return "confirm.php" in self.driver.current_url

    def clear_address_field(self):
        """Clears only the address field."""

        addr_field = self.wait.until(
            EC.presence_of_element_located(self.locators.ADDRESS)
        )
        addr_field.clear()

    def clear_first_name_field(self):
        """Clears only the first name field."""

        first_name_field = self.wait.until(
            EC.presence_of_element_located(self.locators.FIRST_NAME)
        )
        first_name_field.clear()

    def clear_all_mandatory_fields(self):
        """Clears all mandatory checkout fields."""

        fields_to_clear = [
            self.locators.FIRST_NAME,
            self.locators.LAST_NAME,
            self.locators.ADDRESS,
            self.locators.CITY,
            self.locators.STATE,
            self.locators.PINCODE,
            self.locators.PHONE,
            self.locators.EMAIL
        ]

        for locator in fields_to_clear:
            field = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            field.clear()

    def get_validation_errors(self):
        """Returns all validation error messages."""

        errors = self.get_elements(self.locators.ERROR_MESSAGES)
        return [error.text for error in errors]