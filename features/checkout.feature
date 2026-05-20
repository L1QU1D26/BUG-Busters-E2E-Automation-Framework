Feature: Address Validation during Checkout

  Background:
    Given user launches the application login page
    And user logs in with valid credentials
    And user is on the cart page
    And user clicks on the proceed checkout button
    Then user should be landed on the checkout page

  Scenario: All details are filled successfully
    When user fills all required billing details
    And clicks on the continue button
    Then user should see the order confirmation

  Scenario: Empty address validation
    When user clears the address field
    And clicks on the continue button
    Then error message "Billing Street address is a required field" should be displayed

  Scenario: Missing mandatory fields validation
    When user clears all mandatory fields
    And clicks on the continue button
    Then validation errors should be displayed for all required fields