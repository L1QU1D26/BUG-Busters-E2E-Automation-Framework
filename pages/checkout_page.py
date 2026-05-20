from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutValidationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.proceed_to_checkout_btn = (
            By.XPATH,
            "//a[contains(translate(text(), "
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
            "'abcdefghijklmnopqrstuvwxyz'), 'proceed')]"
        )

        # Mandatory Billing Field Locators
        self.first_name = (By.ID, "firstname")
        self.last_name = (By.ID, "lastname")
        self.address = (By.ID, "address")
        self.city = (By.ID, "city")
        self.postcode = (By.ID, "pincode")
        self.phone = (By.ID, "phone")
        self.email = (By.ID, "email")

        # Continue Button Locator
        self.continue_btn = (By.ID, "continue")

        # Validation Errors Locator
        self.error_messages = (
            By.CSS_SELECTOR,
            ".error-message, .woocommerce-error li, span.error"
        )

        # Required Page URLs
        self.cart_page_url = "https://shop.qaautomationlabs.com/cart.php"
        self.checkout_page_url = "https://shop.qaautomationlabs.com/checkout.php"
        self.confirm_page_url = "https://shop.qaautomationlabs.com/confirm.php"

    def is_cart_page_displayed(self):
        """Validates that the user has landed on the cart page."""
        self.wait.until(EC.url_contains("cart.php"))
        return self.driver.current_url == self.cart_page_url

    def click_proceed_to_checkout(self):
        """Clicks the Proceed Checkout button."""

        try:
            self.click(self.proceed_to_checkout_btn)
        except Exception:
            proceed_btn = self.wait.until(
                EC.element_to_be_clickable(self.proceed_to_checkout_btn)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                proceed_btn
            )
            self.driver.execute_script(
                "arguments[0].click();",
                proceed_btn
            )

    def is_checkout_page_displayed(self):
        """Validates that the user has landed on the checkout page."""
        self.wait.until(EC.url_contains("checkout.php"))
        return self.driver.current_url == self.checkout_page_url

    def fill_all_required_details(
        self,
        first_name,
        last_name,
        address,
        city,
        postcode,
        phone,
        email
    ):
        """Fills out the billing form."""

        self.enter_text(self.first_name, first_name)
        self.enter_text(self.last_name, last_name)
        self.enter_text(self.address, address)
        self.enter_text(self.city, city)
        self.enter_text(self.postcode, postcode)
        self.enter_text(self.phone, phone)
        self.enter_text(self.email, email)

    def click_continue(self):
        """Clicks the Continue button."""

        try:
            self.click(self.continue_btn)
        except Exception:
            btn = self.wait.until(
                EC.element_to_be_clickable(self.continue_btn)
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
        self.wait.until(EC.url_contains("confirm.php"))
        return self.driver.current_url == self.confirm_page_url

    def clear_address_field(self):
        """Clears only address field."""

        addr_field = self.wait.until(
            EC.presence_of_element_located(self.address)
        )
        addr_field.clear()

    def clear_all_mandatory_fields(self):
        """Clears all mandatory checkout fields."""

        fields_to_clear = [
            self.first_name,
            self.last_name,
            self.address,
            self.city,
            self.postcode,
            self.phone,
            self.email
        ]

        for locator in fields_to_clear:
            field = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            field.clear()

    def get_validation_errors(self):
        """Returns all validation error messages."""

        errors = self.get_elements(self.error_messages)
        return [error.text for error in errors]