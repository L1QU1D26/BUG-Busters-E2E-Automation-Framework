Feature: Checkout and Billing Validation

  Background:
    Given user launches the application login page
    And user logs in with valid credentials
    And user adds a product to cart
    And user is on the cart page
    And user clicks on the proceed checkout button
    Then user should be landed on the checkout page

  Scenario: All details are filled successfully
    When user fills all required billing details
    And clicks on the continue button
    Then user should see the order confirmation

  Scenario: Empty address validation
    When user fills all required billing details
    And user clears the address field
    And clicks on the continue button
    Then error message "Please enter your address." should be displayed

  Scenario: Missing first name validation
    When user fills all required billing details
    And user clears the first name field
    And clicks on the continue button
    Then error message "Please enter your first name." should be displayed