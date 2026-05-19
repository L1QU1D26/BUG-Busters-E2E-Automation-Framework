from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage

class CheckoutValidationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
        # WooCommerce Mandatory Billing Field Locators
        self.first_name = (By.ID, "firstname")
        self.last_name = (By.ID, "lastname")
        self.address = (By.ID, "address")
        self.state=(By.ID,"states")
        self.city = (By.ID, "city")
        self.postcode = (By.ID, "pincode")
        self.phone = (By.ID, "phone")
        self.email = (By.ID, "email")
        
        # Buttons and Errors
        self.continue_btn = (By.ID, "continue")
        # Grabs all individual error line items inside the error box
        self.error_messages = (By.CSS_SELECTOR, ".woocommerce-error li")

    def _clear_field(self, locator):
        """Helper method to ensure the field is completely empty"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()

    def clear_address_field(self):
        """Clears only the street address field"""
        self._clear_field(self.address_1)

    def clear_all_mandatory_fields(self):
        """Iterates through and clears all required WooCommerce billing fields"""
        fields_to_clear = [
            self.first_name, self.last_name, self.address_1, 
            self.city, self.postcode, self.phone, self.email
        ]
        for field_locator in fields_to_clear:
            self._clear_field(field_locator)

    def click_continue(self):
        """Clicks the 'Place order' button to trigger validation"""
        # A brief sleep is often required here because WooCommerce uses AJAX 
        # to calculate shipping/taxes which temporarily blocks the UI
        time.sleep(2) 
        self.click(self.place_order_btn)

    def get_validation_errors(self):
        """Returns a list of all visible error messages on the checkout page"""
        self.wait.until(EC.visibility_of_element_located(self.error_messages))
        elements = self.driver.find_elements(*self.error_messages)
        return [element.text for element in elements]